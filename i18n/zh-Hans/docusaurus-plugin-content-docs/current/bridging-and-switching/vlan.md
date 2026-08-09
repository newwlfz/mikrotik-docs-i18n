# VLAN

> 本页介绍 MikroTik RouterOS 中的 VLAN 功能，解释如何使用 IEEE 802.1Q 标准创建和管理虚拟局域网，以实现高效的网络分段，并详细说明 VLAN 接口、Trunk、Q-in-Q 标记及接口属性。

# VLAN

**子菜单:** `/interface/vlan`

**标准:** `IEEE 802.1Q, IEEE 802.1ad`

虚拟局域网（VLAN）是一种 Layer 2 方法，允许在单个物理接口（以太网、无线等）上创建多个虚拟局域网，从而高效地隔离 LAN。

您可以使用 MikroTik RouterOS（以及 Cisco IOS、Linux 和其他路由器系统）来标记这些数据包，并接受和路由已标记的数据包。

由于 VLAN 工作在 OSI Layer 2，它可以像任何其他网络接口一样使用，没有任何限制。VLAN 可以顺利通过常规的以太网桥接。

您还可以通过无线链路传输 VLAN，并在单个无线接口上放置多个 VLAN 接口。请注意，由于 VLAN 不是完整的隧道协议（即它没有额外的字段来传输发送方和接收方的 MAC 地址），因此通过 VLAN 进行桥接与桥接普通无线接口具有相同的限制。换句话说，虽然无线客户端可以参与放置在无线接口上的 VLAN，但无法将处于 Station 模式的无线接口上的 VLAN 与任何其他接口进行桥接。

## 802.1Q

用于虚拟局域网（VLAN）的最常用协议是 IEEE 802.1Q。它是一种标准化的封装协议，定义了如何将四字节的 VLAN 标识符插入以太网报头中。

每个 VLAN 被视为一个独立的子网。这意味着，默认情况下，特定 VLAN 中的主机无法与属于另一个 VLAN 的主机通信，即使它们连接到同一台交换机。因此，如果您需要 VLAN 间通信，则需要路由器。RouterOS 每个接口支持多达 4094 个 VLAN 接口，每个接口具有唯一的 VLAN ID。VLAN 优先级也可以使用和操作。

当 VLAN 扩展到多台交换机时，交换机间的链路必须成为“Trunk”，数据包在此链路上被标记以指示它们属于哪个 VLAN。Trunk 承载多个 VLAN 的流量；它就像一条点对点链路，在交换机之间或交换机与路由器之间传输带标记的数据包。

:::info
IEEE 802.1Q 标准保留了一些具有特殊用途的 VLAN ID；以下 VLAN ID 不应在通用 VLAN 设置中使用：0、1、4095
:::

## Q-in-Q

原始的 802.1Q 只允许一个 VLAN 报头；而 Q-in-Q 则允许两个或更多 VLAN 报头。在 RouterOS 中，可以通过在一个 VLAN 接口之上添加另一个 VLAN 接口来配置 Q-in-Q。示例：

```ros
/interface/vlan
add name=vlan1 vlan-id=11 interface=ether1
add name=vlan2 vlan-id=12 interface=vlan1
```

如果任何数据包通过 'vlan2' 接口发送，则会在以太网报头中添加两个 VLAN 标签 - '11' 和 '12'。

## 属性

**子菜单:** `/interface/vlan`

| 属性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; 默认值：**enabled**) | 地址解析协议设置<code>disabled</code> - 接口将不使用 ARP<code>enabled</code> - 接口将使用 ARP<code>local-proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到同一接口<code>proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到其他接口<code>reply-only</code> - 接口将仅回复来自 IP/ARP 表中静态条目匹配的 IP 地址/MAC 地址组合的请求。不会自动在 IP/ARP 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-timeout** (*auto \| 整数*; 默认值：**auto**) | 在从 IP 地址未收到数据包后，ARP 记录在 ARP 表中保留的时间。值 `auto` 等于 IP/设置中的 `arp-timeout` 值，默认为 30 秒。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 更改接口是否被禁用。 |
| **interface** (*名称*; 默认值：) | VLAN 将工作在其上的接口名称。**重要提示：** 将 VLAN 接口添加到启用了 [vlan-filtering](./#bridge-vlan-filtering) 的 [bridge](./#bridge-vlan-filtering) 中，将自动将桥接接口标记为成员端口。带有注释“added by vlan on bridge”的动态条目将出现在 `/interface/bridge/vlan` 菜单下。 |
| **l3-hw-offloading** (*yes \| no*; 默认值：**yes**) | 在每个 VLAN 接口上启用或禁用 [L3HW](./l3-hardware-offloading.md)。此设置仅适用于支持 L3HW 卸载的设备，并从 RouterOS v7.21 开始可用。更多详情 - [Per-VLAN offloading](l3-hardware-offloading.md#per-vlan-offloading)。 |
| **mvrp** (*yes \| no*; 默认值：**no**) | 指定此 VLAN 是否应通过多 VLAN 注册协议（MVRP）作为申请人声明其属性。其主要用例是在连接到支持 [MVRP](index.md#mvrp) 的桥接器的以太网接口（例如“单臂路由器”设置）上创建的 VLAN。在已经是启用 MVRP 的桥接器一部分的 VLAN 接口上启用此选项无效，因为在这种情况下桥接器管理 MVRP。此属性仅在 `use-service-tag` 被禁用时生效。 |
| **mtu** (*整数: 68..65535*; 默认值：**1500**) | Layer3 最大传输单元 |
| **name** (*字符串*; 默认值：) | 接口名称 |
| **use-service-tag** (*yes \| no*; 默认值：) | IEEE 802.1ad 兼容服务标签 |
| **vlan-id** (*整数: 1..4094*; 默认值：**1**) | 用于区分 VLAN 的虚拟局域网标识符或标签。对于属于同一 VLAN 的所有计算机，此值必须相同。 |

:::info
MTU 应设置为 1500 字节，与以太网接口相同。但这可能不适用于某些不支持接收/发送带有 VLAN 报头的全尺寸以太网数据包（1500 字节数据 + 4 字节 VLAN 报头 + 14 字节以太网报头）的以太网卡。在这种情况下，可以使用 MTU 1496，但请注意，如果必须通过接口发送较大的数据包，这将导致数据包分段。同时，请记住，如果源和目标之间的路径 MTU 发现无法正常工作，MTU 1496 可能会导致问题。
:::

## 设置示例

---

### 视频示例

[VLANs pt1](http://youtube.com/watch?v=US2EU6cgHQU), [VLANs pt2](http://youtube.com/watch?v=YMwOrc0LDP8), [VLANs pt3](http://youtube.com/watch?v=7a_z1jAdIME)

### Layer2 VLAN 示例

您可以使用多种可能的配置，但每种配置类型都是为特定设备集设计的，因为某些配置方法将利用内置交换芯片的优势并获得更大的吞吐量。请参阅 [Basic VLAN switching](./user-guides/basic-vlan-switching.md) 指南，了解每种设备类型应使用哪种配置以获得最大可能的吞吐量和兼容性。该指南展示了如何设置非常基本的 VLAN Trunk/接入端口配置。

还有其他一些设置 VLAN 标记或 VLAN 交换的方法，但推荐的方法是使用 [Bridge VLAN Filtering](index.md#bridge-vlan-filtering)。确保您没有使用任何 [已知的 Layer2 错误配置](./user-guides/layer2-misconfiguration.md)。

### Layer3 VLAN 示例

#### 简单 VLAN 路由

假设我们有几台 MikroTik 路由器连接到一个集线器。请记住，集线器是 OSI 物理层设备（如果路由器之间有集线器，那么从 L3 的角度来看，就像它们之间有一条以太网电缆连接）。为简化起见，假设所有路由器都使用 ether1 接口连接到集线器，并已按下图所示分配了 IP 地址。然后在每台路由器上创建 VLAN 接口。

R2 和 R4 的配置如下所示：

R2:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

R4:

```ros
[admin@MikroTik] /interface/vlan> add name=VLAN2 vlan-id=2 interface=ether1 disabled=no

[admin@MikroTik] /interface/vlan> print 
Flags: X - disabled, R - running, S - slave 
 #    NAME                  MTU   ARP        VLAN-ID INTERFACE                
0 R  VLAN2                 1500  enabled    2       ether1
```

下一步是为 VLAN 接口分配 IP 地址。

R2:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.3/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.4/24        10.0.1.0        10.0.1.255      ether1
   1   10.20.0.1/24       10.20.0.0       10.20.0.255     pc1
   2   10.10.10.3/24      10.10.10.0      10.10.10.255    vlan2

 [admin@MikroTik] /ip/address> 
```

R4:

```ros
 [admin@MikroTik] /ip/address> add address=10.10.10.5/24 interface=VLAN2
 [admin@MikroTik] /ip/address> print
 Flags: X - disabled, I - invalid, D - dynamic
   #   ADDRESS            NETWORK         BROADCAST       INTERFACE
   0   10.0.1.5/24        10.0.1.0        10.0.1.255      ether1
   1   10.30.0.1/24       10.30.0.0       10.30.0.255     pc2
   2   10.10.10.5/24      10.10.10.0      10.10.10.255    vlan2

[admin@MikroTik] /ip/address> 
```

此时，应该可以从路由器 R2 ping 通路由器 R4，反之亦然：

```ros
 "从 R2 ping R4:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.5

 10.10.10.5 64 byte ping: ttl=255 time=4 ms

 10.10.10.5 64 byte ping: ttl=255 time=1 ms

 2 packets transmitted, 2 packets received, 0% packet loss

 round-trip min/avg/max = 1/2.5/4 ms

 "从 R4 ping R2:"
 
 [admin@MikroTik] /ip/address> /ping 10.10.10.3
 10.10.10.3 64 byte ping: ttl=255 time=6 ms
 10.10.10.3 64 byte ping: ttl=255 time=1 ms
 2 packets transmitted, 2 packets received, 0% packet loss
 round-trip min/avg/max = 1/3.5/6 ms 
```

为确保 VLAN 设置正常工作，请尝试从 R2 ping R1。如果 ping 超时，则说明 VLAN 已成功隔离。

```ros
 "从 R2 ping R1:"

 [admin@MikroTik] /ip/address> /ping 10.10.10.2
 10.10.10.2 ping timeout
 10.10.10.2 ping timeout
 3 packets transmitted, 0 packets received, 100% packet loss 
```

#### VLAN 间路由

如果在交换机上实现了多个 VLAN，则需要路由器来提供 VLAN 之间的通信。交换机工作在 OSI Layer 2，因此它仅使用以太网报头进行转发，不检查 IP 报头。因此，我们必须使用路由器作为每个 VLAN 的网关。没有路由器，主机将无法在其自身 VLAN 之外进行通信。上述 VLAN 之间的路由过程称为 VLAN 间通信。

为了说明 VLAN 间通信，我们将创建一个 Trunk，通过 MikroTik 路由器和支持 VLAN Trunk 的可管理交换机之间的单条链路承载来自三个 VLAN（VLAN2、VLAN3 和 VLAN4）的流量。

如上图所示，每个 VLAN 都有自己独立的子网（广播域）：

- VLAN 2 – 10.10.20.0/24。
- VLAN 3 – 10.10.30.0/24。
- VLAN 4 – 10.10.40.0/24。

大多数交换机上的 VLAN 配置都很简单。我们需要定义哪些端口是 VLAN 的成员，并定义一个可以承载交换机与路由器之间带标记帧的“Trunk”端口。

创建 VLAN 接口：

```ros
/interface/vlan
add name=VLAN2 vlan-id=2 interface=ether1 disabled=no
add name=VLAN3 vlan-id=3 interface=ether1 disabled=no
add name=VLAN4 vlan-id=4 interface=ether1 disabled=no
```

为 VLAN 添加 IP 地址：

```ros
/ip/address 
add address=10.10.20.1/24 interface=VLAN2
add address=10.10.30.1/24 interface=VLAN3
add address=10.10.40.1/24 interface=VLAN4
```

#### RouterOS /32 和 IP 无编号地址

在 RouterOS 中，要创建带地址的点对点隧道，您必须使用网络掩码为 '/32' 的地址，这实际上为您提供了与某些供应商的无编号 IP 地址相同的功能。

有 RouterA 和 RouterB 两台路由器，它们分别是网络 10.22.0.0/24 和 10.23.0.0/24 的一部分，并使用 VLAN 作为承载来连接这些路由器，配置如下：

RouterA:

```ros
 /ip/address/add address=10.22.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.22.0.1/32 interface=vlan1 network=10.23.0.1
 /ip/route/add gateway=10.23.0.1 dst-address=10.23.0.0/24 
```

RouterB:

```ros
 /ip/address/add address=10.23.0.1/24 interface=ether1
 /interface/vlan/add interface=ether2 vlan-id=1 name=vlan1
 /ip/address/add address=10.23.0.1/32 interface=vlan1 network=10.22.0.1
 /ip/route/add gateway=10.22.0.1 dst-address=10.22.0.0/24 
```