# VRRP

> 本页介绍 MikroTik RouterOS 中的虚拟路由器冗余协议（VRRP），说明其如何通过 IPv4/IPv6 组播通信及路由器间的优先级选举机制提供路由器冗余。内容涵盖 VRRP 配置、虚拟 MAC 地址分配、Owner/Master/Backup 角色，并强调版本兼容性及 VRRPv3 中已弃用认证的警告。

# VRRP

## 概述

本章介绍 RouterOS 对虚拟路由器冗余协议（VRRP）的支持。

在较大型的局域网中，通常使用动态路由协议（OSPF 或 RIP）；然而，有些因素可能使得使用动态路由协议变得不可取。一种替代方案是使用静态路由，但如果静态配置的下一跳发生故障，主机将无法与其他主机通信。

在 IPv6 网络中，主机通过接收邻居发现（ND）协议使用的路由器通告来获知路由器。ND 协议本身已具备检测不可达路由器的机制。然而，检测到不可达路由器可能需要长达 38 秒的时间。虽然可以调整参数以加快检测速度，但这会增加 ND 流量开销，尤其是在主机数量众多的情况下。VRRP 可以在无额外流量开销的情况下，于 3 秒内检测到不可达路由器。

虚拟路由器冗余协议（VRRP）通过将多台路由器组合成一个称为 *虚拟路由器*（VR）的逻辑组来提供解决方案。RouterOS 中的 VRRP 实现基于 VRRPv2 RFC 3768 和 VRRPv3 RFC 5798。

建议所有使用相同 VRID 实现 VRRP 的设备使用相同版本的 RouterOS。

:::warning
根据 RFC 规定，VRRP v3 已弃用认证功能。

:::

## 协议概述

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/vrrp-01.webp)

VRRP 的目的是与所有关联到虚拟路由器 ID 的 VRRP 路由器通信，并通过它们之间的优先级选举过程支持路由器冗余。

所有消息均通过使用协议号 112（VRRP）的 IPv4 或 IPv6 组播数据包发送。IPv4 数据包的目的地址为 *224.0.0.18*，IPv6 数据包的目的地址为 *FF02:0:0:0:0:0:0:12*。数据包的源地址始终是发送该数据包接口的主 IP 地址。在 IPv6 网络中，源地址是接口的链路本地地址。

这些数据包始终以 TTL=255 发送，并且不会被路由器转发。如果路由器因任何原因收到 TTL 较低的数据包，该数据包将被丢弃。

每个 VR 节点都有一个分配的 MAC 地址。该 MAC 地址用作 Master 发送的所有周期性消息的源地址。

虚拟路由器由 VRID 和一组映射的 IPv4 或 IPv6 地址定义。主路由器被称为映射的 IPv4/IPv6 地址的 **所有者**。对于 IPv4 和 IPv6 使用相同的 VRID 没有限制；但是，它们将是两个不同的虚拟路由器。

只有 Master 路由器发送周期性的通告消息以最小化流量。只有当 Backup 具有更高优先级且未禁止抢占时，它才会尝试抢占 Master。

:::tip
属于同一 VR 的所有 VRRP 路由器必须配置相同的通告间隔。如果间隔不匹配，路由器将丢弃接收到的通告数据包。

:::

## 虚拟路由器（VR）

虚拟路由器（VR）由一个 Owner 路由器和一台或多台属于同一网络的 Backup 路由器组成。

VR 包括：

- 每台 VRRP 路由器上配置的 VRID。
- 每台路由器上配置的相同虚拟 IP。
- 每台路由器上配置的 Owner 和 Backup。在给定的 VR 上只能有一个 Owner。

### 虚拟 MAC 地址

VRRP 根据 VRRP 数据包的标准 MAC 前缀和 VRID 号自动为 VRRP 接口分配 MAC 地址。前五个八位组是 00:00:5E:00:01，最后一个八位组是配置的 VRID。例如，如果虚拟路由器的 VRID 为 49，则虚拟 MAC 地址将为 *00:00:5E:00:01:31*。

:::warning
虚拟 MAC 地址无法手动设置或编辑。

:::

### Owner

VR 的 Owner 路由器是默认的 Master 路由器，并作为 VR 中包含的所有子网的 Owner 运行。Owner 路由器上的优先级必须为最高值（255），并且虚拟 IP 与真实 IP 相同（拥有虚拟 IP 地址）。

:::warning
RouterOS 无法配置为 Owner。除非非 RouterOS 设备被设置为 Owner，否则纯虚拟 IP 配置是唯一有效的配置。

:::

### Master

VR 中的 Master 路由器作为其配置网络的物理网关运行。Master 的选择由优先级值控制。Master 状态描述了 Master 路由器的行为。在示例网络中，**R1** 是 Master 路由器。当 R1 不再可用时，R2 成为 Master。

### Backup

VR 必须至少包含一台 Backup 路由器。Backup 路由器必须为该 VR 配置与 Master 相同的虚拟 IP。Backup 路由器的默认优先级为 100。当当前主路由器不再可用时，具有最高优先级的 Backup 路由器将成为当前 Master。每当具有更高优先级的路由器变为可用时，它就会切换为 Master。有时这种操作并非必要。要覆盖此行为，应禁用抢占模式。

### 虚拟地址

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/vrrp-02.webp)

与 VR 关联的虚拟 IP 必须在所有 VR 节点上相同并设置。所有虚拟和真实地址应来自同一网络。

:::warning
RouterOS 无法配置为 Owner。VRRP 地址和真实 IP 地址不应相同。

:::

如果 VR 的 Master 关联了多个 IP 地址，则属于同一 VR 的 Backup 路由器也必须关联相同的虚拟 IP 地址集。如果 Master 上的虚拟地址不在 Backup 上，则存在配置错误，VRRP 通告数据包将被丢弃。

所有虚拟路由器成员都可以配置为虚拟 IP 与物理 IP 不同。这种虚拟地址可以称为浮动或纯虚拟 IP 地址。这种设置的优点是为管理员提供了灵活性。由于虚拟 IP 地址不是任何参与路由器的真实地址，管理员可以更改这些物理路由器或其地址，而无需重新配置虚拟路由器本身。

在 IPv6 网络中，第一个地址始终是与 VR 关联的链路本地地址。如果配置了多个 IPv6 地址，则它们会在链路本地地址之后添加到通告数据包中。

### IPv4 ARP

给定 VR 的 Master 使用 VR 分配的 MAC 地址响应 ARP 请求。虚拟 MAC 地址也用作 Master 发送的通告数据包的源 MAC 地址。对于非虚拟 IP 地址的 ARP 请求，路由器使用系统 MAC 地址响应。Backup 路由器不响应虚拟 IP 的 ARP 请求。

### IPv6 ND

如您所知，在 IPv6 网络中，使用邻居发现协议代替 ARP。当路由器成为 Master 时，会为与虚拟路由器关联的每个 IPv6 地址发送一个带有路由器标志的主动 ND 邻居通告。

## VRRP 状态机

![](https://manual.mikrotik.com/docs/high-availability-solutions/img/vrrp-03.webp)

从图中可以看出，每个 VRRP 节点可以处于以下三种状态之一：

- 初始化状态
- 备份状态
- 主状态

### 初始化状态

此状态的目的是等待启动事件。收到此事件时，将执行以下操作：

- 如果优先级为 255：
- \* 对于 IPv4，发送通告数据包并广播 ARP 请求。
- \* 对于 IPv6，为与虚拟路由器关联的每个 IPv6 地址发送一个主动 ND 邻居通告，并将目标地址设置为与 VR 关联的链路本地地址。
- \* 转换到 MASTER 状态。
- 否则转换到 BACKUP 状态。

### 备份状态

处于备份状态时：

- 在 IPv4 网络中，节点不响应 ARP 请求，也不转发与 VR 关联的 IP 的流量。
- 在 IPv6 网络中，节点不响应 ND 邻居请求消息，也不为与 VR 关联的 IPv6 地址发送 ND 路由器通告消息。

路由器的主要任务是接收通告数据包并检查主节点是否可用。

Backup 路由器在两种情况下会将自身转换为主状态：

- 如果通告数据包中的优先级为 0。
- 当 Preemption\_Mode 设置为 yes 且通告中的优先级低于本地优先级时。

转换到主状态后，节点：

- 在 IPv4 中广播一个免费 ARP 请求。
- 在 IPv6 中为每个关联的 IPv6 地址发送一个主动 ND 邻居通告。

在其他情况下，通告数据包将被丢弃。当收到关闭事件时，转换到初始化状态。

:::warning
如果 Owner 路由器变为可用，则忽略抢占模式。

:::

### 主状态

当设置 MASTER 状态时，节点充当与 VR 关联的 IPv4/IPv6 地址的转发路由器。

在 IPv4 网络中，Master 节点响应与 VR 关联的 IPv4 地址的 ARP 请求。在 IPv6 网络中，Master 节点：

- 响应关联 IPv6 地址的 ND 邻居请求消息。
- 为关联的 IPv6 地址发送 ND 路由器通告。

如果主节点收到通告数据包：

- 如果优先级为 0，则立即发送通告。
- 如果通告数据包中的优先级大于节点的优先级，则转换到备份状态。
- 如果通告数据包中的优先级等于节点的优先级，且发送方的主 IP 地址大于本地主 IP 地址，则转换到备份状态。
- 在其他情况下忽略通告。

当收到关闭事件时，发送优先级=0 的通告数据包并转换到初始化状态。

### 连接跟踪同步

与不同的高可用性功能类似，RouterOS v7 支持 VRRP 连接跟踪同步。

VRRP 连接跟踪同步要求 RouterOS [连接跟踪](../firewall-and-quality-of-service/connection-tracking.md) 正在运行。默认情况下，连接跟踪以 `auto` 模式工作。如果 VRRP 设备不包含任何防火墙规则，则需要手动启用连接跟踪：

```ros
/ip/firewall/connection/tracking/set enabled=yes
```

要同步连接跟踪条目，请按如下方式配置设备：

```ros
/interface/vrrp/set vrrp1 sync-connection-tracking=yes
```

在日志部分验证配置：

```ros
16:14:06 vrrp,info vrrp1 now MASTER, master down timer
16:14:06 vrrp,info vrrp1 stop CONNTRACK
16:14:06 vrrp,info vrrp1 starting CONNTRACK MASTER
```

连接跟踪条目仅从 Master 设备同步到 Backup 设备。

当同时启用 `sync-connection-tracking` 和 `preemption-mode` 时，如果具有更高 VRRP 优先级的路由器上线，连接会先被同步，然后该更高优先级的路由器才会成为 VRRP 主路由器。

:::tip
如果在两台设备之间配置了多个 VRRP 接口且需要 `sync-connection-tracking=yes`，则必须仅在其中一台 VRRP 接口上启用它，最好是在指定为 `group-authority` 的接口上启用。

:::

## 配置 VRRP

### IPv4

设置虚拟路由器非常简单，只需两个操作 - 创建 VRRP 接口并设置虚拟路由器的 IP 地址。

例如，将 VRRP 添加到 ether1 并将 VR 的地址设置为 192.168.1.1

```ros
/interface/vrrp/add name=vrrp1 interface=ether1
/ip/address/add address=192.168.1.2/24 interface=ether1
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

请注意，添加 VRRP 时仅指定了 'interface' 参数。这是唯一需要手动设置的参数。其他参数如果未指定，将设置为其默认值：`vrid=1, priority=100` 和 `authentication=none`。

:::warning
如果 VRRP 接口上配置的地址与路由器任何其他接口上的地址来自同一子网，则 VRRP 接口上的地址必须具有 /32 掩码。

:::

在 VRRP 正常运行之前，ether1 上需要正确的 IP 地址。在此示例中，为 192.168.1.2/24。

### IPv6

要使 VRRP 在 IPv6 网络中工作，必须启用几个额外的选项 - 需要 v3 支持，并且协议类型应设置为 IPv6：

```ros
/interface/vrrp/add name=vrrp1 interface=ether1 version=3 v3-protocol=ipv6
```

现在 VRRP 接口已设置，我们可以添加全局地址并启用 ND 通告：

```ros
/ipv6/address/add address=FEC0:0:0:FFFF::1/64 advertise=yes interface=vrrp1
```

与 IPv4 情况不同，无需额外的地址配置。IPv6 使用链路本地地址在节点之间通信。

## 参数

VRRP 接口参数。

**子菜单：** `/interface/vrrp`

##### 可写设置

| 属性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | ARP 解析协议模式。 |
| **arp-timeout**(*整数;* 默认值：**auto**) | 在从 IP 收到数据包后，ARP 记录在 ARP 表中保留的时间。值 `auto` 等于 IP/设置中的 `arp-timeout` 值，默认为 3。 |
| **authentication** (*ah \| none \| simple*; 默认值：**none**) | 用于 VRRP 通告数据包的认证方法。- `none` - 仅在低安全性网络中使用，例如，局域网上的两个 VRRP 节点。- `ah` - IP 认证头。该算法提供针对配置错误、重放攻击以及数据包损坏或修改的强大保护。当您对局域网上节点的管理控制有限时，应使用它。使用 HMAC-MD5。- `simple` - 使用明文密码。防止本地网络上路由器的意外配置错误。 |
| **comment** (*字符串*; 默认值：) | 接口的简短描述。 |
| **connection-tracking-mode** (*active-active \| passive-active*; 默认值：**passive-active**) | 指定连接跟踪同步的模式。此设置仅在启用 `sync-connection-tracking=yes` 时相关。- `passive-active` - 将此模式用于传统 VRRP 设置，即使用一个主路由器和一台或多台备份路由器。在此模式下，只有主设备通过向备份设备发送更新来执行连接跟踪同步。备份设备不发送连接跟踪数据。- `active-active` - 将此模式用于具有多个 VRRP 组以实现负载均衡的设置。每个 VRRP 组都有自己的主路由器，这些主路由器可以位于不同的物理设备上。使用 `active-active` 模式，所有活动主路由器可以相互同步连接跟踪数据。`active-active` 模式下的每个 VRRP 组必须使用**唯一**的 `connection-tracking-port` 值。在多个组之间重用相同的端口可能导致连接跟踪表不同步。**重要提示：** 在多个 VRRP 组中使用 `passive-active` 模式可能导致连接跟踪表不同步，因为只有一个主路由器处理同步，其他路由器不交换跟踪数据。示例配置：<pre><code>R1`/interface/vrrp`add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=100 sync-connection-tracking=yes vrid=1add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=100 sync-connection-tracking=yes vrid=2R2`/interface/vrrp`add connection-tracking-mode=active-active connection-tracking-port=8275 interface=ether1 name=vrrp30 priority=55 sync-connection-tracking=yes vrid=1add connection-tracking-mode=active-active connection-tracking-port=8276 interface=ether1 name=vrrp40 priority=155 sync-connection-tracking=yes vrid=2</code></pre> |
| **connection-tracking-port** (*整数;* 默认值：**8275**) | 指定用于连接跟踪同步的 UDP 端口。此设置仅在启用 `sync-connection-tracking=yes` 时相关。 |
| **group-authority** (*none \| self \| vrrp-interface;* 默认值：**none**) | 允许多个 VRRP 接口分组，以便它们共享相同的 VRRP 状态。在一个组内，选择一个组权威接口。它控制其他组成员的状态，并且是唯一发送 VRRP 通告的接口。当组权威 VRRP 接口转换到备份状态时，所有组成员也转换到备份状态。如果在任何组成员上检测到故障，例如由于其父接口上的链路断开，所有组成员都转换到故障状态。- `none` - VRRP 接口不分组，独立运行，拥有自己的 VRRP 状态机。- `self` - VRRP 接口充当组权威。它控制其他分组 VRRP 接口的状态机，并负责发送和接收 VRRP 通告。- `vrrp-interface` - VRRP 接口是组成员。其状态机遵循指定 VRRP 接口的状态。例如，VRRP 实例在 LAN 和 WAN 网络上运行，它们之间有 NAT。如果一台设备上的一个 VRRP 实例是 Master，另一个是 Backup，则整个网络会因 NAT 故障而无法正常工作。将 LAN 和 WAN VRRP 接口分组可确保它们同时为 VRRP Master 或 Backup。在 VRRP 组中，VRRP 通告仅由组权威发送。在典型的 WAN+LAN 设置中，应使用 LAN 网络作为组权威，以将 VRRP 控制流量保留在内部网络中。<pre><code>`/interface/vrrp`add name=vrrp-wan interface=sfp-sfpplus1 vrid=1 priority=100add name=vrrp-lan interface=bridge1 vrid=2 priority=100set [find] group-authority=vrrp-lan</code></pre> |
| **interface** (*字符串*; 默认值：) | VRRP 实例将运行的接口名称。 |
| **interval** (*时间 [10ms..4m15s]*; 默认值：**1s**) | VRRP 间隔定义 VRRP 主路由器向备份路由器发送通告数据包的频率。此间隔直接决定备份接收确认主路由器正常运行的 keepalive 信息的频率。较短的间隔会增加通告数据包的速率，从而可以更快地检测主路由器故障，但也会增加对数据包丢失、处理延迟和计时器不准确的敏感性。较长的间隔会减少控制流量并提高稳定性，但代价是故障转移检测速度较慢。主路由器停机间隔由配置的 VRRP 间隔和路由器优先级推导得出，其计算允许在触发故障转移前错过多个通告。**警告：** 配置低于 1 秒的 VRRP 间隔可能导致不可预测的行为和意外的主角色更改。 |
| **mtu** (*只读*; 默认值：) | 第 3 层 MTU 大小。自 RouterOS v7.7 起，VRRP 接口始终使用从属接口的 MTU。 |
| **name** (*字符串*; 默认值：) | VRRP 接口名称。 |
| **on-backup** (*字符串*; 默认值：) | 节点切换到备份状态时执行的脚本。 |
| **on-master** (*字符串*; 默认值：) | 节点切换到主状态时执行的脚本。 |
| **on-fail** (*字符串*; 默认值：) | 节点发生故障时执行的脚本。 |
| **password** (*字符串*; 默认值：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 认证所需的密码。如果不使用认证，可以忽略。 |
| **preemption-mode** (*yes \| no*; 默认值：**yes**) | 主节点是否始终具有优先级。当设置为 'no' 时，即使备份节点的优先级高于当前主节点，在当前主节点发生故障之前，备份节点也不会被选举为主节点。如果 Owner 路由器变为可用，则忽略此设置。 |
| **priority** (*整数: 1..254*; 默认值：**100**) | 用于主路由器选举算法的 VRRP 节点优先级。数字越大表示优先级越高。'255' 保留给拥有 VR IP 的路由器，'0' 保留给主路由器以表示其正在释放责任。 |
| **remote-address** (*IPv4;* 默认值：) | 指定用于连接跟踪同步的其他 VRRP 路由器的远程地址。如果未设置，系统会通过 VRRP 自动检测远程地址。远程地址仅在 `sync-connection-tracking=yes` 时使用。显式设置远程地址有以下好处：- 连接跟踪同步启动更快，因为无需等待 VRRP 的初始消息交换来检测远程地址。- VRRP 主路由器选举更快。- 连接跟踪数据可以通过不同的网络接口发送，例如，两个路由器之间的专用安全线路。同步连接跟踪使用 UDP 端口 8275。 |
| **v3-checksum-as-v2** (*yes \| no*; 默认值：**no**) | 控制 VRRPv3 IPv4 校验和的计算是否包含 IPv4 伪头。不同供应商对 RFC 5798 第 5.2.8 节关于 IPv4 校验和计算中伪头的解释不同。基于 Linux 的实现（包括 FRR）对 IPv4 和 IPv6 都包含伪头，而 Cisco 仅对 IPv6 包含伪头。- `no`（默认）- 在校验和计算中包含 IPv4 伪头。与其他基于 Linux 的 VRRPv3 实现兼容。- `yes` - 在校验和计算中排除 IPv4 伪头。使用此设置以兼容 Cisco 和其他不为 IPv4 包含伪头的供应商。此设置仅适用于 VRRPv3 与 IPv4。它对 VRRPv3 IPv6 或 VRRPv2 没有影响。**重要提示：** 同一虚拟路由器中的所有 VRRP 路由器必须对此设置使用相同的值。值不匹配将导致“校验和错误”错误，并且 VRRP 通告数据包将被丢弃。 |
| **v3-protocol** (*ipv4 \| ipv6*; 默认值：**ipv4**) | VRRPv3 将使用的协议。仅在 **version** 为 3 时有效。 |
| **version** (*整数 [2, 3]*; 默认值：**3**) | 要使用的 VRRP 版本。 |
| **vrid** (*整数: 1..255*; 默认值：**1**) | 虚拟路由器标识符。每个虚拟路由器必须具有唯一的 ID 号。 |
| **sync-connection-tracking**(*字符串*; 默认值：**no**) | 将连接跟踪条目从 Master 设备同步到 Backup 设备。VRRP 连接跟踪同步要求 RouterOS [连接跟踪](../firewall-and-quality-of-service/connection-tracking.md) 正在运行。 |

##### 只读标志

| 属性 | 描述 |
| :-- | :-- |
| **backup** | VRRP 接口处于备份状态。 |
| **disabled** | VRRP 接口已被用户禁用。 |
| **failure** | VRRP 接口处于故障状态，例如由于其父接口上的链路断开。 |
| **grp-authority** | VRRP 接口是 `group-authority`。它控制其他组成员的状态，并且是唯一发送 VRRP 通告的接口。 |
| **grp-member** | VRRP 接口是组成员。其状态机遵循指定 `group-authority` 接口的状态。 |
| **invalid** | VRRP 接口处于无效状态，例如由于配置错误。 |
| **master** | VRRP 接口处于主状态。 |