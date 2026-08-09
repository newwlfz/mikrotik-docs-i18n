# 多机箱链路聚合组

> RouterOS 中的 MLAG 通过在两个设备上配置 LACP 绑定来实现物理冗余，使客户端感知到单一连接，同时确保故障切换。它使用 ICCP 进行对等通信，支持 STP 协议，并需要在专用端口上进行细致的 VLAN 配置。MLAG 对大型网络而言 CPU 占用较高，且与 L3 硬件卸载或 MVRP 的兼容性有限。

# 多机箱链路聚合组

## 引言

RouterOS 中的 MLAG（多机箱链路聚合组）实现允许在两个独立设备上配置 LACP 绑定，而客户端设备认为其连接的是同一台机器。这在交换机故障时提供了物理冗余。

两个对等节点建立 MLAG 接口，并通过 `mlag-peer-port` 使用 ICCP（机箱间控制协议）更新桥接主机表。RouterOS 的 ICCP 不需要 IP 配置；它发送带有 EtherType 0x88B5 和目的 MAC 地址 01:80:C2:00:00:0E 的未标记二层数据包。ICCP 数据包是链路本地的，意味着它们始终由 MLAG 设备自身接收和处理，绝不会转发到网络的其他部分。每个 MLAG 设备上的对等端口必须直接相互连接。还建议将对等端口使用的未标记 VLAN 与网络其余部分隔离，可以通过分配专用的未标记 VLAN（使用 `pvid`），或将对等端口设置为仅允许 VLAN 标记帧（使用 `frame-types=admit-only-vlan-tagged`）。对等端口可以配置为单个以太网接口或绑定接口。但是，建议使用绑定接口，因为它有助于防止单个接口故障影响连通性，尤其是在两个 MLAG 节点仍在运行时。

当 `mlag-peer-port` 运行且 ICCP 建立后，会进行主设备选举并选择系统 ID。优先级最低的对等节点将作为主设备。如果优先级相同，则桥接 MAC 地址最低的对等节点将成为主设备。该系统 ID 用于 STP BPDU 桥接标识符和 LACP 系统 ID。MLAG 支持 STP、RSTP 或 MSTP 协议。在两个节点的双连接桥接端口上使用相同的 STP 优先级和相同的 STP 配置。当 MLAG 桥接被选举为 STP 根时，两个设备在桥接监视器下都会显示为根桥接。

:::info
MLAG 按桥接接口配置。任何 RouterOS 设备（包括虚拟 CHR 实例）都可以用作 MLAG 节点。

桥接硬件卸载的 MLAG 仅在 [采用 Marvell Prestera 交换芯片的 MikroTik 设备](../bridging-and-switching/marvell-prestera-switch-chip-features.md) 上可用。所有其他设备仅支持软件方式的 MLAG。

:::

:::info
MLAG 与 [L3 硬件卸载](../bridging-and-switching/l3-hardware-offloading.md) 不兼容。使用 MLAG 时，必须禁用 L3 硬件卸载。

MLAG 与 [多 VLAN 注册协议（MVRP）](../bridging-and-switching/index.md#mvrp) 不兼容。双连接绑定上注册的 VLAN 不会同步到另一个 MLAG 节点。

:::

:::danger
在具有大量主机和 VLAN 的网络中，MLAG 主机同步可能对 CPU 和内存造成较大负担。对于采用单核 **MIPSBE CPU** 的交换机（例如 CRS326-24S+2Q+RM、CRS354-48P-4S+2Q+RM、CRS518-16XS-2XQ-RM），建议仅在最多 1,000 台主机的网络中使用 MLAG。

在主机数量较多的网络中，这些交换机上的 MLAG 可能导致意外行为。

:::

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/multi-chassis-link-aggregation-group-01.png)

### 数据包转发与负载均衡

BUM（广播、未知单播、组播）数据包转发分两个阶段进行。

#### 阶段 1 - 本地转发

当节点接收到 BUM 流量时，它会像传统（非 MLAG）设置一样，将数据包本地泛洪到同一 VLAN 的所有成员端口。此外，它还会通过对等端口将流量转发到另一个 MLAG 节点。

:::info
仅当对等端口也是该 VLAN 的成员时，才会通过对等端口进行转发。这就是文档强调对等端口应包含在跨越两个 MLAG 节点的所有 VLAN 中的原因。

:::

#### 阶段 2 - 对等节点远程转发

当对等节点通过对等端口接收到 BUM 流量时，它会将流量泛洪到同一 VLAN 的所有常规桥接端口。这些端口是没有指定 `mlag-id` 的端口（即独立以太网或绑定接口）。对于具有 `mlag-id` 的绑定接口，对等节点根据链路状态做出决策：

- 如果两条链路（本地和远程）都处于活动状态，则不会将流量泛洪到自己的 MLAG 绑定端口 - 这避免了重复数据包的发送，因为第一个节点已经处理了该流量。
- 如果远程对等节点的链路不活动，而本地链路活动，则对等节点会将流量泛洪到 MLAG 绑定以确保送达。

单播流量的行为类似，但与常规 LAG 相比，MLAG 有一个关键区别。在常规 LAG 设置中，出站数据包根据传输哈希策略在所有活动链路上进行负载均衡。在两条链路都活动的 MLAG 设置中，流量不会在两个交换机之间的对等端口上进行负载均衡。相反，流量仅通过 MLAG 的本地成员链路转发 - 它始终采用最短路径。仅当本地 MLAG 链路故障时才会使用对等端口。在这种情况下，流量通过对等端口转发到另一个节点以到达目的地。发生这种情况时，主机表也会更新在 MLAG 绑定上学习到的 MAC 地址条目，以指示目的地现在可通过对等端口到达。在 MLAG 绑定由 2 + 2 条活动链路（每个节点 2 条链路）组成的设置中，传输哈希仅在两条本地链路之间进行 - 而不是在所有四条链路上进行。当 MLAG 对用于多个双连接绑定且传入流量已经分布在两对上时，可以实现负载均衡。

## 快速设置

在此示例中，CRS317 和 CRS309 设备用作 MLAG 对等节点，任何具有两个 SFP+ 接口的设备都可以用作 LACP 客户端。两个对等节点上都使用 SFP+1 接口创建 `mlag-peer-port`，用于 ICCP，请参见下面的网络方案。

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/multi-chassis-link-aggregation-group-02.png)在 **Peer1** 和 **Peer2** 设备上配置 MLAG 的绑定接口，在两个对等设备上使用匹配的 `mlag-id` 设置，并设置 1 秒的 LACPDU 传输速率：

```ros
# Peer1
/interface/bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2 lacp-rate=1sec

# Peer2
/interface/bonding
add mlag-id=10 mode=802.3ad name=client-bond slaves=sfp-sfpplus2 lacp-rate=1sec
```

设置启用 `vlan-filtering` 的桥接接口。指定 `mlag-peer-port` 以启用 MLAG。要控制哪个设备成为主 MLAG 节点，请在首选设备上设置较低的 `mlag-priority` 值。在此示例中，我们希望 Peer1 成为主设备，因此我们设置其 `priority=50`。Peer2 保持默认优先级 128，使其成为备用设备。

在此示例中，我们希望两个 MLAG 节点都充当根桥接，因此我们使用 `priority=0x1000` 分配一个更优（更低）的桥接优先级。确保两个 MLAG 节点使用相同的优先级值。

可选地，您可以在桥接接口上设置 `frame-types=admit-only-vlan-tagged` 以禁用默认的未标记 VLAN 1（`pvid=1`）。

```routeros
# Peer1
/interface/bridge
add name=bridge1 vlan-filtering=yes mlag-peer-port=sfp-sfpplus1 mlag-priority=50 priority=0x1000 frame-types=admit-only-vlan-tagged

# Peer2
/interface/bridge
add name=bridge1 vlan-filtering=yes mlag-peer-port=sfp-sfpplus1 priority=0x1000 frame-types=admit-only-vlan-tagged
```

接下来，将必要的接口添加到桥接中。在此示例中，只需要添加对等端口（sfp-sfpplus1）和 client-bond 接口。

对于对等端口，我们通过将其配置为仅接受 VLAN 标记流量（`frame-types=admit-only-vlan-tagged`）来禁用默认的未标记 VLAN 1（`pvid=1`）。

对于 client-bond 接口，我们希望未标记流量属于 VLAN 10，因此我们在该接口上设置 `pvid=10`。

```ros
# Peer1
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=client-bond pvid=10

# Peer2
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=client-bond pvid=10
```

:::danger
MLAG 支持 STP、RSTP 或 MSTP 协议。在两个节点的双连接桥接端口上使用相同的 STP 优先级和相同的 STP 配置（例如 path-cost、priority、edge）。

:::

:::info
如果双连接绑定接口未连接到任何其他 RSTP/MSTP 桥接或交换机，您可以在两个 MLAG 节点的该接口上设置 `edge=yes`。

此设置允许绑定端口快速进入转发状态，有助于减少 MLAG 一侧重新可用时的数据包丢失。

:::

在此示例中，client-bond 接口对未标记流量使用 VLAN 10（通过 `pvid=10` 设置），我们还希望允许标记的 VLAN 20。为确保两个 VLAN 的流量可以在 MLAG 设备之间传递，我们需要在两个 MLAG 节点上将对等端口添加为 VLAN 10 和 20 的标记成员。将对等端口包含在其他桥接端口使用的所有 VLAN 中非常重要。这包括未标记和标记的 VLAN。以下是两个对等设备的配置命令：

```ros
# Peer1
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1,client-bond vlan-ids=20

# Peer2
/interface/bridge/vlan
add bridge=bridge1 tagged=sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1,client-bond vlan-ids=20
```

:::danger
桥接从属端口使用的所有 VLAN 也必须配置为对等端口的标记 VLAN，以便对等端口成为这些 VLAN 的成员并能转发数据。

:::

最后，检查对等设备上的 MLAG 状态，并确保客户端 LACP 的两个接口都处于活动状态。

```ros
# Peer1
[admin@Peer1] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 2                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: primary  

# Peer2
[admin@Peer2] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 1                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: secondary    

# Client
[admin@Client] > /interface/bonding/monitor bond1 
                    mode: 802.3ad
            active-ports: sfp-sfpplus1,sfp-sfpplus2
          inactive-ports: 
          lacp-system-id: 74:4D:28:7B:7F:96
    lacp-system-priority: 65535
  lacp-partner-system-id: B8:69:F4:1B:B0:7C

```

如果 **Client** 设备是 RouterOS，以下是创建常规 [LACP 绑定](./bonding.md#8023ad) 的配置命令。为加快 LACP 链路建立，请使用 1 秒的 LACPDU 传输速率：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=sfp-sfpplus1,sfp-sfpplus2 lacp-rate=1sec 
```

## MLAG 设置与监控

本节介绍可用的 MLAG 设置和监控选项。

**子菜单：** `/interface/bridge`

| 属性 | 描述 |
| :-- | :-- |
| **mlag-heartbeat** (*时间: 1s..10s \| none*; 默认值: **00:00:05**) | 此设置控制发送心跳消息以检查对等节点之间连接的频率。如果连续三个间隔未收到心跳消息，对等节点将记录有关潜在通信问题的警告。如果设置为 `none`，则完全不发送心跳消息。 |
| **mlag-peer-port** (*接口 \| 绑定;* 默认值: **none**) | 将用作对等端口的接口。两个对等设备通过这些对等端口使用机箱间通信来建立 MLAG 并更新主机表。对等端口可以配置为单个以太网接口或绑定接口。但是，建议使用绑定接口，因为它有助于防止单个接口故障影响连通性，尤其是在两个 MLAG 节点仍在运行时。建议将对等端口使用的未标记 VLAN 与网络其余部分隔离，可以通过分配专用的未标记 VLAN（使用 `pvid`），或将对等端口设置为仅允许 VLAN 标记帧（使用 `frame-types=admit-only-vlan-tagged`）。桥接从属端口使用的所有 VLAN 也必须配置为对等端口的标记 VLAN（在 `/interface/bridge/vlan` 表中），以便对等端口成为这些 VLAN 的成员并能转发数据。 |
| **mlag-priority** (*整数: 0..128;* 默认值: **128**) | 此设置更改选择主 MLAG 节点的优先级。数字越低表示优先级越高。如果两个 MLAG 节点具有相同的优先级，则桥接 MAC 地址最低的节点将成为主设备。 |

使用 `/interface/bridge/monitor` 命令查看当前的 MLAG 状态和活动角色。

```ros
 [admin@Peer1] > /interface/bridge/monitor [find name=bridge1]
                  state: enabled                 
    current-mac-address: B8:69:F4:1B:B0:7C       
              bridge-id: 0x1000.B8:69:F4:1B:B0:7C
            root-bridge: yes                     
         root-bridge-id: 0x1000.B8:69:F4:1B:B0:7C
         root-path-cost: 0                       
              root-port: none                    
             port-count: 2                       
  designated-port-count: 2                       
           fast-forward: no                      
             mlag-state: connected               
       mlag-active-role: primary   
```

| 属性 | 描述 |
| :-- | :-- |
| **mlag-state** (*connected \| connecting \| disabled*) | MLAG 状态。 |
| **mlag-active-role** (*primary \| secondary*) | `priority` 最低的对等节点将作为主设备。如果优先级相同，则桥接 MAC 地址最低的对等节点将成为主设备。主设备的 `system-id` 用于发送 (R/M)STP BPDU 桥接标识符和 LACP 系统 ID。 |

**子菜单：** `/interface/bonding`

| 属性 | 描述 |
| :-- | :-- |
| **mlag-id** (*整数: 0..4294967295*; 默认值: ) | 更改绑定接口的 MLAG ID。两个对等设备上应使用相同的 MLAG ID，以便成功为客户端设备创建单个 LAG。`mlag-peer-port` 不应配置 MLAG ID。 |

LACP 绑定接口和绑定从属端口可以使用 `monitor` 和 `monitor-slaves` 命令进行监控。更多详情请参见 [绑定监控](./bonding.md#bonding-monitoring)。