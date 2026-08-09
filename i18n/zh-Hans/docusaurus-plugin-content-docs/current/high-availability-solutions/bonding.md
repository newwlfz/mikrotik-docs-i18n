# Bonding（链路聚合）

> Bonding 允许将多个以太网接口组合成单个虚拟链路，以获得更高带宽和故障转移能力。MikroTik RouterOS 支持多种模式，包括 LACP 以及针对特定芯片的硬件卸载功能。

# Bonding（链路聚合）

## 概述

---

Bonding 是一种允许将多个类似以太网的接口聚合到单个虚拟链路中的技术，从而获得更高的数据速率并提供故障转移能力。

:::warning
接口 Bonding 并不会创建具有更大链路速度的接口。接口 Bonding 创建的是一个虚拟接口，可以在多个接口之间进行负载均衡。更多详情请参阅 [LAG 接口与负载均衡](../bridging-and-switching/user-guides/layer2-misconfiguration.md#lag-interfaces-and-load-balancing) 页面。

:::

:::info
搭载 Marvell Prestera 交换机以及 88E6393X、88E6191X、88E6190 交换芯片的 MikroTik 设备支持 Bonding 接口的桥接硬件卸载功能。

仅 `802.3ad`（LACP）、`balance-xor`（静态 LAG）和 `active-backup` Bonding 模式支持硬件卸载；其他 Bonding 模式将使用 CPU 资源。

搭载 Marvell Prestera 交换机的 MikroTik 设备将始终使用 Layer2+Layer3+Layer4 作为传输哈希策略，而 88E6393X、88E6191X、88E6190 交换芯片仅限于 Layer2 传输哈希。在使用硬件卸载时手动更改传输哈希策略将不会生效。

更多详情请参阅 [Marvell Prestera 交换芯片特性](../bridging-and-switching/marvell-prestera-switch-chip-features.md)。

:::

## 快速设置指南

---

假设我们在每台路由器（Router1 和 Router2）上有两个以太网接口，并希望在这两台路由器之间获得最大数据速率。要实现此目标，请按照以下步骤操作：

1. 确保将要被绑定到 Bonding 接口的接口上没有配置 IP 地址。
2. 在 Router1 上添加 Bonding 接口和 IP 地址：

   ```ros
   /interface/bonding/add slaves=ether1,ether2 name=bond1
   /ip/address/add address=172.16.0.1/24 interface=bond1
   ```

3. 在 Router2 上执行相同操作：

   ```ros
   /interface/bonding/add slaves=ether1,ether2 name=bond1
   /ip/address/add address=172.16.0.2/24 interface=bond1
   ```

4. 从 Router1 测试链路：

   ```ros
   [admin@Router1] > ping 172.16.0.2
     SEQ HOST                                 SIZE TTL TIME  STATUS                   
       0 172.16.0.2                             56  64 0ms  
       1 172.16.0.2                             56  64 0ms  
       2 172.16.0.2                             56  64 0ms  
       sent=3 received=3 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
   ```

:::warning
Bonding 接口需要几秒钟才能与其对端建立连接。

:::

## 链路监控

---

启用可用的链路监控选项之一至关重要。在上述示例中，如果某个 Bonded 链路发生故障，Bonding 驱动程序将继续通过故障链路发送数据包，从而导致网络性能下降。RouterOS Bonding 目前支持两种监控从属设备链路状态的方法：MII 和 ARP 监控。由于 Bonding 驱动程序的限制，无法同时使用这两种方法。

### ARP 监控

ARP 监控通过发送 ARP 查询并利用响应来判断链路是否正常运行。ARP 回复不会被验证——从属接口收到的任何数据包都会将该接口标记为活动状态。这种方法可以确保流量确实在链路上传输。

当使用 balance-rr 或 balance-xor 模式时，所连接的交换机必须配置为在所有链路路径上均匀分布数据包。否则，来自目标的所有 ARP 回复都将在同一个从属接口上收到，这可能导致其他 Bonded 链路显示为故障状态。

ARP 监控通过配置三个属性来启用：`link-monitoring`、`arp-ip-targets` 和 `arp-interval`。可以指定多个 ARP 目标地址，这在高可用性设置中特别有用。依赖单一目标会形成潜在的故障点——配置额外的目标可以提高 ARP 监控机制的可靠性。

在 Router1 上启用 ARP 监控：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp arp-ip-targets=172.16.0.2
```

在 Router2 上启用 ARP 监控：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=arp arp-ip-targets=172.16.0.1
```

RouterOS 中 `arp-interval` 值默认为 100ms，在此示例中无需修改。要验证链路监控是否正常工作，请断开其中一条电缆链路。您可能会观察到一些 ping 超时，直到 ARP 监控检测到链路故障。

```text
[admin@MikroTik] > /ping 172.16.0.2
  SEQ HOST                                     SIZE TTL TIME  STATUS                                 
    0 172.16.0.2                                 56  64 0ms  
    1 172.16.0.2                                 56  64 0ms  
    2 172.16.0.2                                 56  64 0ms  
    3 172.16.0.2                                 56  64 0ms  
    4 172.16.0.2                                              timeout                                
    5 172.16.0.2                                 56  64 0ms  
    6 172.16.0.2                                 56  64 0ms  
    sent=7 received=6 packet-loss=14% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```

:::note
ARP 监控不需要在设备上配置 IP 地址——无论任何接口上设置了什么 IP 地址，它都能正常工作。

:::

:::danger
当 ARP 监控处于活动状态时，Bonding 从属接口将发送不带 VLAN 标签的 ARP 请求，即使在与 `arp-ip-targets` 地址处于同一子网的 VLAN 接口上配置了 IP 地址也是如此。

:::

### MII 监控

MII 监控仅监控本地接口的状态。MII Type 1 是一种由设备驱动程序确定链路是 up 还是 down 的方法。如果设备驱动程序不支持此选项，则链路将始终显示为 up。MII 监控的主要缺点是，即使检测到链路为 up，也无法确定该链路是否真的能够传输数据包。MII 监控通过设置 `link-monitoring` 和 `mii-interval` 参数来配置。

在 Router1 和 Router2 上启用 MII Type1 监控：

```ros
/interface/bonding/set [find name=bond1] link-monitoring=mii
```

我们将 `mii-interval` 保留为其默认值（100ms）。拔掉其中一根电缆时，与 ARP 链路监控相比，故障将被几乎立即检测到。

## Bonding 模式

---

### 802.3ad

802.3ad 模式是一种 IEEE 标准，也称为 LACP（链路聚合控制协议）。它提供聚合链路的自动配置，只需最少的交换机配置。该标准还要求帧按顺序交付，因此连接不应出现数据包乱序现象。此外，聚合中的所有设备必须以相同的速度和双工模式运行。

LACP 根据哈希协议头信息在活动端口之间平衡出站流量，并接受来自任何活动端口的入站流量。哈希包括以太网源地址和目标地址、VLAN 标签（如果可用）以及 IPv4/IPv6 源地址和目标地址。计算方法取决于 `transmit-hash-policy` 参数。不建议使用 ARP 链路监控，因为由于 LACP 对端设备上的传输哈希策略，ARP 回复数据包可能只到达一个从属端口。这可能导致传输流量不平衡，因此 MII 链路监控是推荐选项。

:::warning
layer-3-and-4 传输哈希模式与 LACP 不完全兼容。更多详情请参阅 https://www.kernel.org/doc/Documentation/networking/bonding.txt

:::

### balance-xor

此模式使用哈希协议头在活动端口之间平衡出站流量，并接受来自任何活动端口的入站流量。该模式与 LACP 非常相似，只是它并非标准化协议。此模式可以与所连接交换机上的静态链路聚合组（LAG）接口配置一起使用。

### balance-rr

设置此模式后，数据包将从第一个可用从属接口到最后一个按顺序传输。balance-rr 模式是唯一可以将属于同一 TCP/IP 连接的数据包通过多个接口发送的 Bonding 模式。当使用多个发送和接收链路时，数据包通常会乱序到达，从而导致分段重传。对于 UDP 等其他协议，如果客户端软件能够容忍乱序数据包，则这不是问题。如果使用交换机来聚合链路，则需要适当的交换机端口配置；但是，许多交换机不支持 balance-rr。[快速设置指南](#quick-setup-guide) 演示了 balance-rr Bonding 模式的使用。如您所见，设置非常简单。Balance-rr 对于绑定多条无线链路也很有用；但是，它要求所有 Bonded 链路具有相等的带宽。如果某个 Bonded 链路的带宽下降，则 Bond 的总带宽将等于最慢的 Bonded 链路的带宽。

### active-backup

此模式仅使用一个活动从属接口来传输数据包。只有当主从属接口发生故障时，备用从属接口才会变为活动状态。Bonding 接口的 MAC 地址会在活动端口上呈现，以防止交换机混淆。Active-backup 是使用多个互连交换机的高可用性设置的最佳选择。

:::warning
当两台路由器设备直接连接时，ARP 监控无法正常工作。在这种情况下，必须使用 MII 监控，或者在路由器设备与其对端之间放置一台交换机。

:::

### broadcast

当端口配置为广播模式时，所有从属端口将相同的数据传输到目的地。此模式提供容错能力，但不提供负载均衡。

### balance-tlb

此模式按对端平衡出站流量。每个 Bonded 链路可以以不同的速度和双工设置运行，并且与其他 Bonding 模式不同，不需要特定的交换机配置。此模式的限制是它仅支持 MII 链路监控（配置 ARP 监控将被忽略），并且入站流量不进行负载均衡。入站流量将使用指定为“primary”接口的链路。

#### 配置示例

假设路由器有两条链路 - **ether1** 最大带宽为 10Mbps，**ether2** 最大带宽为 5Mbps。第一条链路带宽更大，因此我们将其设置为主链路：

```ros
/interface/bonding/add mode=balance-tlb slaves=ether1,ether2 primary=ether1
```

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/bonding-01.webp)

交换机无需额外配置。上图说明了 balance-tlb 模式的工作原理。如您所见，路由器可以与连接到交换机的所有客户端通信，总带宽为两条链路之和（15Mbps）。但您已经知道，balance-tlb 不均衡入站流量。在我们的示例中，客户端与路由器通信的总带宽为主链路的带宽，即我们配置中的 10Mbps。

### balance-alb

该模式与 balance-tlb 基本相同，但入站 IPv4 流量也会进行负载均衡。接收负载均衡通过 ARP 协商实现。Bonding 驱动程序在本地生成的 ARP 消息发出时拦截它们，并用 Bond 中某个从属接口的唯一地址覆盖源硬件地址，以便不同的对端使用不同的硬件地址。仅支持 MII 链路监控（配置 ARP 链路监控将被忽略）。此模式的另一个缺点是它要求设备驱动程序具备更改 MAC 地址的能力。该模式与 `local-proxy-arp` 设置不兼容。

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/bonding-02.webp)  
上图说明了 balance-alb 模式的工作原理。与 balance-tlb 模式相比，来自客户端的流量也可以使用备用链路与路由器通信。

## Bonding 监控

---

自 RouterOS 6.48 版本起，可以监控 Bonding 接口和 Bonding 端口。对于 `802.3ad` Bonding 模式，提供了更详细的监控选项。

```text
/interface/bonding/monitor [find] 
                      mode: 802.3ad           active-backup
              active-ports: ether4            ether6
                            ether5            
            inactive-ports:                   ether7
            lacp-system-id: CC:2D:E0:11:22:33 
      lacp-system-priority: 65535             
    lacp-partner-system-id: B8:69:F4:44:55:66
```

| 属性 | 描述 |
| :-- | :-- |
| **mode** (*802.3ad \| active-backup \| balance-alb \| balance-rr \| balance-tlb \| balance-xor \| broadcast*) | 使用的 Bonding 模式 |
| **active-ports** (*interface*) | 显示活动的 Bonding 端口 |
| **inactive-ports**(*interface*) | 显示非活动的 Bonding 端口（例如，禁用或备用接口） |
| **lacp-system-id** (*MAC address*) | 显示本地 LACP 系统 ID |
| **lacp-system-priority** (*integer*) | 显示本地 LACP 优先级 |
| **lacp-partner-system-id** (*MAC address*) | 显示对端 LACP 系统 ID |

要监控单个 Bonding 端口，请使用 `monitor-slaves` 命令。

```text
/interface/bonding/monitor-slaves bond1
Flags: A - active, P - partner 
 AP port=ether4 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 

 AP port=ether5 key=17 flags="A-GSCD--" partner-sys-id=D4:CA:6D:12:06:65 partner-sys-priority=65535 partner-key=9 partner-flags="A-GSCD--" 
```

| 属性 | 描述 |
| :-- | :-- |
| **port** (*interface*) | 使用的 Bonding 端口 |
| **key** (*integer*) | 显示本地 LACP 聚合键。低 6 位根据单个端口链路速度和双工自动分配。高 10 位可以使用 `lacp-user-key` 设置手动指定（自 RouterOS v7.3 起可用）。 |
| **flags** (*string*) | 显示本地 LACP 标志： A - activity（链路活动，否则为被动） T - timeout（链路使用 1 秒短超时，否则使用 30 秒超时） G - aggregation（链路可聚合） S - synchronization（链路已同步） C - collecting（链路能够收集传入帧） D - distributing（链路能够分发传出帧） F - defaulted（链路使用默认的对端信息，表示未从对端收到 LACPDU） E - expired（链路已过期） |
| **partner-sys-id** (*MAC address*) | 显示对端 LACP 系统 ID |
| **partner-sys-priority** (*integer*) | 显示对端 LACP 优先级 |
| **partner-key** (*integer*) | 显示对端 LACP 聚合键 |
| **partner-flags** (*string*) | 显示对端 LACP 标志 |

## 属性描述

---

本节介绍可用的 Bonding 设置。

| 属性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | 接口的地址解析协议。<code>disabled</code> - 接口将不使用 ARP<code>enabled</code> - 接口将使用 ARP<code>proxy-arp</code> - 接口将使用 ARP 代理功能<code>reply-only</code> - 接口将仅回复来自 `/ip/arp` 表中作为静态条目输入的匹配 IP 地址/MAC 地址组合的请求。不会自动在 `/ip/arp` 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-interval** (*time*; 默认值：**00:00:00.100**) | 以毫秒为单位的时间，定义监控 ARP 请求的频率 |
| **arp-ip-targets** (*IP address*; 默认值：) | 当 `link-monitoring` 设置为 arp 时将监控的 IP 目标地址。可以指定多个 IP 地址，用逗号分隔 |
| **comment** (*string*; 默认值：) | 接口的简短描述 |
| **disabled** (*yes \| no*; 默认值：**no**) | 更改 Bonding 接口是否禁用 |
| **down-delay** (*time*; 默认值：**00:00:00**) | 如果检测到链路故障，Bonding 接口将在 down-delay 时间内被禁用。该值应为 mii-interval 的倍数，否则将向下取整到最接近的值。此属性仅在 `link-monitoring` 设置为 `mii` 时生效。 |
| **forced-mac-address** (*MAC address*; 默认值：**none**) | 默认情况下，Bonding 接口将使用第一个选定的从属接口的 MAC 地址。此属性允许为 Bond 接口配置静态 MAC 地址（全零、广播或多播地址将不适用）。RouterOS 将自动更改从属接口的 MAC 地址，并且它将在 `/interface/ethernet` 配置导出中可见 |
| **lacp-mode** (*active \| passive*; 默认值：**active**) | 指定端口是主动还是被动参与 LACP： <code>active</code> - 端口主动发起 LACP 通信，无论对端的 LACP 模式如何（即，即使对端保持沉默，它也会“发言”），<code>passive</code> - 端口仅响应 LACP 消息，除非对端处于主动模式，否则不会主动发起（即，它“监听”并仅在对方发言时响应）。 |
| **lacp-rate** (*1sec \| 30secs*; 默认值：**30secs**) | 链路聚合控制协议速率指定与 Bonding 对端交换 LACPDU 的频率。用于确定链路是否 up 或网络中是否发生了其他变化。LACP 试图适应这些变化以提供故障转移。 |
| **lacp-user-key**(*integer: 0..1023*; 默认值：**0**) | 指定端口键的高 10 位。低 6 位根据单个端口链路速度和双工自动分配。此设置自 RouterOS v7.3 起可用。 |
| **link-monitoring** (*arp \| mii \| none*; 默认值：**mii**) | 用于监控链路（up 或 down）的方法<code>arp</code> - 使用地址解析协议来确定远程接口是否可达<code>mii</code> - 使用媒体独立接口来确定链路状态。链路状态确定依赖于设备驱动程序。<code>none</code> - 不使用任何链路监控方法。**警告：** 某些 Bonding 模式需要特定的链路监控才能正常工作。 |
| **min-links** (*integer: 0..4294967295*; 默认值：**0**) | Bonding 变为活动状态所需的活动从属链路数量 |
| **mii-interval** (*time*; 默认值：**00:00:00.100**) | 监控链路故障的频率（仅当 link-monitoring 为 mii 时使用此参数） |
| **mlag-id** (*integer: 0..4294967295*; 默认值：) | 更改 Bonding 接口的 MLAG ID。两台对端设备应使用相同的 MLAG ID 以成功创建单个 MLAG。更多详情请参阅 [MLAG](./multi-chassis-link-aggregation-group.md)。 |
| **mode** (*802.3ad \| active-backup \| balance-alb \| balance-rr \| balance-tlb \| balance-xor \| broadcast*; 默认值：**balance-rr**) | 指定一种 Bonding 策略<code>802.3ad</code> - LACP，IEEE 802.3ad 动态链路聚合。在此模式下，接口被聚合到一个组中，每个从属接口共享相同的速度。它提供容错和负载均衡。出站流量的从属接口选择根据 transmit-hash-policy 进行。<code>active-backup</code> - 提供链路备份。一次只能有一个从属接口处于活动状态。另一个从属接口仅在第一个发生故障时才变为活动状态。<code>balance-alb</code> - 自适应负载均衡。与 balance-tlb 相同，但接收流量也进行负载均衡。设备驱动程序应支持更改其 MAC 地址。<code>balance-rr</code> - 轮询负载均衡。Bonding 接口中的从属接口将按顺序传输和接收数据。它提供负载均衡和容错。<code>balance-tlb</code> - 出站流量根据每个从属接口的当前负载进行分配。入站流量不进行负载均衡，由当前从属接口接收。如果接收从属接口发生故障，则另一个从属接口接管故障从属接口的 MAC 地址。<code>balance-xor</code> - 静态 LAG，根据选定的 transmit-hash-policy 进行传输。此模式提供负载均衡和容错。<code>broadcast</code> - 同时在所有接口上广播相同的数据。这提供容错，但在某些较慢的机器上会降低流量吞吐量。**重要提示：** 搭载 Marvell Prestera 交换机以及 88E6393X、88E6191X、88E6190 交换芯片的 MikroTik 设备支持 Bonding 接口的桥接硬件卸载。仅 `802.3ad`（LACP）、`balance-xor`（静态 LAG）和 `active-backup` Bonding 模式支持硬件卸载，其他 Bonding 模式将使用 CPU 资源。 |
| **mtu** (*integer*; 默认值：**1500**) | 最大传输单元，以字节为单位。必须小于或等于 Bonding 从属接口中最小的 L2MTU 值。Bonding 接口的 L2MTU 由其从属接口中最低的 L2MTU 值决定 |
| **name** (*string*; 默认值：) | Bonding 接口的名称 |
| **primary** (*string*; 默认值：**none**) | 控制活动从属端口之间的主接口，仅适用于 active-backup、balance-tlb 和 balance-alb 模式。对于 active-backup 模式，它控制哪个运行中的接口负责发送和接收流量。对于 balance-tlb 模式，它控制哪个运行中的接口负责接收所有流量，但对于 balance-alb 模式，它控制哪个接口负责接收非均衡流量（非 IPv4 流量）。当没有接口被选为主接口时，设备将自动选择配置为第一个的接口。 |
| **slaves** (*string*; 默认值：**none**) | 至少两个类似以太网的接口，用逗号分隔，将用于 Bonding |
| **up-delay** (*time*; 默认值：**00:00:00**) | 如果链路已启动，Bonding 接口将在 up-delay 时间内被禁用，在此时间之后启用。该值应为 mii-interval 的倍数，否则将向下取整到最接近的值。此属性仅在 `link-monitoring` 设置为 `mii` 时生效。 |
| **transmit-hash-policy** (*encap-2-and-3 \| encap-3-and-4 \| layer-2 \| layer-2-and-3 \| layer-3-and-4*; 默认值：**layer-2**) | 选择在 balance-xor 和 802.3ad 模式下用于从属接口选择的传输哈希策略 <code>encap-2-and-3</code> - 此策略的工作方式类似于 layer-2-and-3 方法用于分配流量，但使用一个过程来同时分析封装的数据包头。如果使用了封装协议（如隧道），它可能会选择内部头而不是外部头。当 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道在 Bonding 接口上运行时，RouterOS 可以使用此功能。<code>encap-3-and-4</code> - 此策略的工作方式类似于 layer-3-and-4 方法用于分配流量，但使用一个过程来同时分析封装的数据包头。如果使用了封装协议（如隧道），它可能会选择内部头而不是外部头。当 6to4、GRE、GRE6、IPIP、IPIP6、PPPoE 或 PPTP 等隧道在 Bonding 接口上运行时，RouterOS 可以使用此功能。<code>layer-2</code> - 使用硬件 MAC 地址的 XOR 来生成哈希。此算法会将发往特定网络对端的所有流量放在同一个从属接口上。此算法符合 802.3ad 标准。<code>layer-2-and-3</code> - 此策略使用 layer2 和 layer3 协议信息的组合来生成哈希。使用硬件 MAC 地址和 IP 地址的 XOR 来生成哈希。此算法会将发往特定网络对端的所有流量放在同一个从属接口上。对于非 IP 流量，公式与 layer2 传输哈希策略相同。此策略旨在提供比单独使用 layer2 更均衡的流量分布，尤其是在需要 layer3 网关设备才能到达大多数目的地的环境中。此算法符合 802.3ad 标准。<code>layer-3-and-4</code> - 此策略在可用时使用上层协议信息来生成哈希。这允许发往特定网络对端的流量跨越多个从属接口，尽管单个连接不会跨越多个从属接口。对于分片的 TCP 或 UDP 数据包以及所有其他 IP 协议流量，源端口和目标端口信息将被省略。对于非 IP 流量，公式与 layer2 传输哈希策略相同。此算法不完全符合 802.3ad 标准。**重要提示：** 搭载 Marvell Prestera 交换机的 MikroTik 设备将始终使用 Layer2+Layer3+Layer4 作为传输哈希策略，而 88E6393X、88E6191X、88E6190 交换芯片仅限于 Layer2 传输哈希。在使用硬件卸载时手动更改传输哈希策略将不会生效。 |

## 另请参阅

- [配置示例 - 带 Bond 的 VLAN](../bridging-and-switching/marvell-prestera-switch-chip-features.md#configuration-example---vlans-with-bonds)