# HWMPplus mesh

> 本文档介绍 MikroTik RouterOS 中的 HWMP+ mesh 协议，这是一种基于混合无线 mesh 协议（HWMP）的无线 mesh 网络二层路由解决方案。内容包括接口属性、端口配置、FDB 状态，并包含一个动态 WDS 链路集成的示例。

# HWMPplus mesh

**子菜单:** `/interface/mesh`

HWMP+ 是 MikroTik 专有的用于无线 mesh 网络的二层路由协议。它基于 IEEE 802.11s 草案标准中的混合无线 mesh 协议（HWMP）。在 mesh 组网中，它可以替代（快速）生成树协议，以确保无环的最优路由。

但请注意，HWMP+ 协议与 IEEE 802.11s 草案标准中的 HWMP 不兼容。

请注意，你用于网络的分布式系统不一定是无线分布式系统（WDS）。HWMP+ mesh 路由不仅支持 WDS 接口，还支持 mesh 内的以太网接口。因此，你可以使用简单的基于以太网的分布式系统，或者将 WDS 和以太网链路结合使用！

:::warning
HWMPplus 不支持 [Wifi](../wifi/index.md) 接口，但可用于 [Wireless](./) 接口。
:::

## 属性

### Mesh

| 属性 | 描述 |
| :-- | :-- |
| **admin-mac** (*MAC 地址*; **默认值: 00:00:00:00:00:00**) | 管理性分配的 MAC 地址，当 **auto-mac** 设置禁用时使用 |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值: **enabled**) | 地址解析协议设置 |
| **auto-mac** (*布尔值*; 默认值: **no**) | 如果禁用，则使用 **admin-mac** 中的值作为 mesh 接口的 MAC 地址；否则，如果存在端口，则使用某个端口的地址 |
| **hwmp-default-hoplimit** (*整数: 1..255*; 默认值: ) | 生成的路由协议数据包的最大跳数；当 HWMP+ 数据包被转发 "hoplimit" 次后，将被丢弃 |
| **hwmp-prep-lifetime** (*时间*; 默认值: **5m**) | 从接收到的 PREP 或 PREQ 消息创建的路由的生存时间 |
| **hwmp-preq-destination-only** (*布尔值*; 默认值: **yes**) | 是否仅目的地可以响应 HWMP+ PREQ 消息 |
| **hwmp-preq-reply-and-forward** (*布尔值*; 默认值: **yes**) | 中间节点在响应 HWMP+ PREQ 消息后是否应转发该消息。仅在 **hwmp-preq-destination-only** 禁用时有用 |
| **hwmp-preq-retries** (*整数*; 默认值: **2**) | 在将特定 MAC 地址视为不可达之前，重试到该地址的路由发现的次数 |
| **hwmp-preq-waiting-time** (*时间*; 默认值: **4s**) | 等待第一个 PREQ 消息响应的时长。请注意，对于后续的 PREQ，等待时间会呈指数增长 |
| **hwmp-rann-interval** (*时间*; 默认值: **10s**) | 发送 HWMP+ RANN 消息的频率 |
| **hwmp-rann-lifetime** (*时间*; 默认值: **1s**) | 从接收到的 RANN 消息创建的路由的生存时间 |
| **hwmp-rann-propagation-delay** (*时间*; 默认值: **0.5s**) | 传播 RANN 消息前等待的时间。单位为秒 |
| **mesh-portal** (*布尔值*; 默认值: **no**) | 此接口是否为 mesh 网络中的门户 |
| **mtu** (*整数*; 默认值: **1500**) | 最大传输单元大小 |
| **name** (*字符串*; 默认值: ) | 接口名称 |
| **reoptimize-paths** (*布尔值*; 默认值: **no**) | 是否发送周期性的 PREQ 消息以查询已知的 MAC 地址。如果网络拓扑经常变化，启用此设置很有用。请注意，如果未收到对重新优化 PREQ 的回复，现有路径仍会保留（直到其超时） |

### 端口

| 属性 | 描述 |
| :-- | :-- |
| **active-port-type** (*只读: wireless \| WDS \| ethernet-mesh \| ethernet-bridge \| ethernet-mixed*; 默认值: ) | 实际使用的端口类型和状态 |
| **hello-interval** (*时间*; 默认值: **10s**) | 发送 HWMP+ Hello 消息的最大间隔。仅用于以太网类型的端口 |
| **interface** (*接口名称*; 默认值: ) | 要包含在 mesh 中的接口名称 |
| **mesh** (*接口名称*; 默认值: ) | 此端口所属的 mesh 接口 |
| **path-cost** (*整数: 0..65535*; 默认值: **10**) | 到接口的路径成本，由路由协议用于确定“最佳”路径 |
| **port-type** (*WDS \| auto \| ethernet \| wireless*; 默认值: ) | 要使用的端口类型auto - 根据底层接口类型自动确定端口类型WDS - 无线分布式系统接口。远程 MAC 地址从无线连接数据中学习ethernet - 远程 MAC 地址从 HWMP+ Hello 消息或接收/转发流量中的源 MAC 地址学习wireless - 远程 MAC 地址从无线连接数据中学习 |

### FDB 状态

| 属性 | 描述 |
| :-- | :-- |
| **mac-address** (*MAC 地址*) | 与此 FDB 条目对应的 MAC 地址 |
| **seq-number** (*整数*) | 路由协议中用于避免环路而使用的序列号 |
| **type** (*local \| outsider \| direct \| mesh \| neighbor \| larval \| unknown*) | 此 FDB 条目的类型local -- MAC 地址属于本地路由器自身outsider -- MAC 地址属于 mesh 网络外部的设备direct -- MAC 地址属于 mesh 网络中某接口上的无线客户端mesh -- MAC 地址属于可通过 mesh 网络到达的设备；它可以是 mesh 网络内部或外部的设备neighbor -- MAC 地址属于与此路由器直接相邻的 mesh 路由器larval -- MAC 地址属于可通过 mesh 网络到达的未知设备unknown -- MAC 地址属于未知设备 |
| **mesh** (*接口名称*) | 此 FDB 条目所属的 mesh 接口 |
| **on-interface** (*接口名称*) | 用于流量转发的 mesh 端口，类似于下一跳值 |
| **lifetime** (*时间*) | 如果此条目未用于流量转发，则剩余生存时间 |
| **age** (*时间*) | 此 FDB 条目的存在时间 |
| **metric** (*整数*) | 路由协议用于确定“最佳”路径的度量值 |

## 示例

![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-01.webp)

此示例使用静态 WDS 链路，这些链路在激活时动态添加为 mesh 端口。使用了两个不同的频率：一个用于 AP 互连，一个用于客户端连接到 AP，因此 AP 必须至少有两个无线接口。当然，所有连接也可以使用相同的频率，但由于潜在的干扰问题，这可能效果不佳。

在所有 AP 上重复此配置：

```ros
/interface/mesh/add disabled=no
/interface/mesh/port/add interface=wlan1 mesh=mesh1
/interface/mesh/port/add interface=wlan2 mesh=mesh1

 # 用于 AP 互连的接口 
/interface/wireless/set wlan1 disabled=no ssid=mesh frequency=2437 band=2ghz-b/g/n mode=ap-bridge \
 wds-mode=static-mesh wds-default-bridge=mesh1 

# 用于客户端连接的接口
 /interface/wireless/set wlan2 disabled=no ssid=mesh-clients frequency=5180 band=5ghz-a/n/ac mode=ap-bridge 

# 为每个要连接的 AP 添加一个静态 WDS 接口
/interface/wireless/wds/add disabled=no master-interface=wlan1 name=<远程端的描述性名称> \
 wds-address=<远程端的 MAC 地址> 
```

这里手动添加了 WDS 接口，因为使用了静态 WDS 模式。如果你使用 **wds-mode**=**dynamic-mesh**，所有 WDS 接口将自动创建。此处指定 **frequency** 和 **band** 参数只是为了生成一个有效的示例配置；mesh 协议操作绝不仅限于这些特定值，也并非针对这些值进行优化。

:::warning
你可能需要增加无线接口选项 **disconnect-timeout** 的值，以使协议更加稳定。
:::

在实际部署中，你还应该使用 `/interface/wireless/security-profile` 来保护无线连接。为简洁起见，此处未显示该配置。

路由器 A 上的结果（有一个客户端连接到 wlan2）：

```ros
[admin@A] > /interface/mesh/print
Flags: X - disabled, R - running
0 R name="mesh1" mtu=1500 arp=enabled mac-address=00:0C:42:0C:B5:A4 auto-mac=yes
admin-mac=00:00:00:00:00:00 mesh-portal=no hwmp-default-hoplimit=32
hwmp-preq-waiting-time=4s hwmp-preq-retries=2 hwmp-preq-destination-only=yes
hwmp-preq-reply-and-forward=yes hwmp-prep-lifetime=5m hwmp-rann-interval=10s
hwmp-rann-propagation-delay=1s hwmp-rann-lifetime=22s

[admin@A] > /interface/mesh/port/print detail
Flags: X - disabled, I - inactive, D - dynamic
0 interface=wlan1 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
1 interface=wlan2 mesh=mesh1 path-cost=10 hello-interval=10s port-type=auto port-type-used=wireless
2 D interface=router_B mesh=mesh1 path-cost=105 hello-interval=10s port-type=auto port-type-used=WDS
3 D interface=router_D mesh=mesh1 path-cost=76 hello-interval=10s port-type=auto port-type-used=WDS
```

此时 FDB（转发数据库）仅包含本地 MAC 地址、通过本地接口可达的非 mesh 节点以及直接 mesh 邻居的信息：

```ros
[admin@A] /interface/mesh/fdb/print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:AA 3m17s
A mesh1 neighbor 00:0C:42:00:00:BB router_B 1m2s
A mesh1 neighbor 00:0C:42:00:00:DD router_D 3m16s
A mesh1 direct 00:0C:42:0C:7A:2B wlan2 2m56s
A mesh1 local 00:0C:42:0C:B5:A4 2m56s

[admin@A] /interface/mesh/fdb/print detail
Flags: A - active, R - root
A mac-address=00:0C:42:00:00:AA type=local age=3m21s mesh=mesh1 metric=0 seqnum=4294967196
A mac-address=00:0C:42:00:00:BB type=neighbor on-interface=router_B age=1m6s mesh=mesh1 metric=132 seqnum=4294967196
A mac-address=00:0C:42:00:00:DD type=neighbor on-interface=router_D age=3m20s mesh=mesh1 metric=79 seqnum=4294967196
A mac-address=00:0C:42:0C:7A:2B type=direct on-interface=wlan2 age=3m mesh=mesh1 metric=10 seqnum=0
A mac-address=00:0C:42:0C:B5:A4 type=local age=3m mesh=mesh1 metric=0 seqnum=0
```

测试 ping 是否正常：

```ros
[admin@A] > /ping 00:0C:42:00:00:CC
00:0C:42:00:00:CC 64 byte ping time=108 ms
00:0C:42:00:00:CC 64 byte ping time=51 ms
00:0C:42:00:00:CC 64 byte ping time=39 ms
00:0C:42:00:00:CC 64 byte ping time=43 ms
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 39/60.2/108 ms
```

路由器 A 必须首先发现到路由器 C 的路径，因此第一次 ping 的时间稍长。现在 FDB 中也包含了一个类型为“mesh”的 00:0C:42:00:00:CC 条目。

另外，测试 ARP 解析是否正常，以及 IP 层的 ping 是否正常：

```ros
[admin@A] > /ping 10.4.0.3
10.4.0.3 64 byte ping: ttl=64 time=163 ms
10.4.0.3 64 byte ping: ttl=64 time=46 ms
10.4.0.3 64 byte ping: ttl=64 time=48 ms
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 46/85.6/163 ms
```

#### Mesh 路由追踪

还有一个 mesh 路由追踪命令，可以帮助你确定路由使用了哪些路径。

例如，对于此网络：

```ros
[admin@1] /interface/mesh/fdb/print
Flags: A - active, R - root
MESH TYPE MAC-ADDRESS ON-INTERFACE LIFETIME AGE
A mesh1 local 00:0C:42:00:00:01 7m1s
A mesh1 mesh 00:0C:42:00:00:02 wds4 17s 4s
A mesh1 mesh 00:0C:42:00:00:12 wds4 4m58s 1s
A mesh1 mesh 00:0C:42:00:00:13 wds4 19s 2s
A mesh1 neighbor 00:0C:42:00:00:16 wds4 7m1s
A mesh1 mesh 00:0C:42:00:00:24 wds4 18s 3s
```

到 00:0C:42:00:00:12 的路由追踪显示：

```ros
[admin@1] /interface/mesh/traceroute mesh1 00:0C:42:00:00:12
ADDRESS TIME STATUS
00:0C:42:00:00:16 1ms ttl-exceeded
00:0C:42:00:00:02 2ms ttl-exceeded
00:0C:42:00:00:24 4ms ttl-exceeded
00:0C:42:00:00:13 6ms ttl-exceeded
00:0C:42:00:00:12 6ms success
```

## 协议描述

### 反应模式

路由器 A 想要发现到 C 的路径：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-02.webp)  

路由器 C 向 A 发送单播响应：
![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-03.webp)

在反应模式下，HWMP+ 与 AODV（Ad-hoc 按需距离矢量）非常相似。所有路径都是按需发现的，通过在网络中泛洪路径请求（PREQ）消息来实现。目的节点或某个具有到目的节点路径的路由器将回复路径响应（PREP）。请注意，如果目的地址属于某个客户端，则该客户端所连接的 AP 将作为其代理（即代表其回复 PREQ）。

此模式最适合移动网络，和/或当大部分通信发生在 mesh 内部节点之间时。

### 主动模式

根节点通过泛洪 RANN 来宣告自身：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-04.webp)  

内部节点以 PREG 响应：
![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-05.webp)  

在主动模式下，某些路由器被配置为门户。一般来说，作为门户意味着该路由器具有到其他网络的接口，即它是 mesh 网络的入口/出口点。

门户将通过泛洪根节点通告（RANN）消息来宣告其存在。内部节点将回复路径注册（PREG）消息。此过程的结果将形成以门户为根的路由树。

到门户的路由将作为一种默认路由。如果内部路由器不知道到特定目的地的路径，它将把所有数据转发到其最近的门户。然后，门户将在需要时代表路由器发现路径。之后数据将流经门户。除非数据是发往门户本身或门户所连接的外部网络，否则这可能导致次优路由。

当大部分流量在内部 mesh 节点和少数门户节点之间流动时，主动模式最为适合。

### 拓扑变化检测

数据流路径：
![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-06.webp)

链路消失后，错误向上游传播：
![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-07.webp)  

HWMP+ 使用路径错误（PERR）消息来通知链路已消失。该消息被传播到所有上游节点，直至数据源。数据源在收到 PERR 后重新启动路径发现过程。

## 常见问题解答

**问：这比 RSTP 好在哪里？**

答：它为你提供了最优路由。RSTP 仅用于防止环路。

**问：路由选择是如何完成的？**

答：在发现过程之后，始终选择具有最佳度量的路由。还有一个配置选项可以定期重新优化已知路由。

路由度量计算为各个链路度量的总和。

链路度量的计算方式与 (R)STP 协议相同：

- 对于以太网链路，度量是静态配置的（例如，与 OSPF 相同）。
- 对于 WDS 链路，度量会根据实际链路带宽动态更新，而链路带宽又受无线信号强度和所选数据传输速率的影响。

目前，该协议不考虑链路上正在使用的带宽量，但未来可能会考虑。

**问：这比 OSPF/RIP/一般的三层路由好在哪里？**

答：WDS 网络通常是桥接的，而不是路由的。自配置能力对于 mesh 网络非常重要，而路由通常比桥接需要更多的配置。当然，你总可以在桥接网络上运行任何三层路由协议，但对于 mesh 网络来说，这通常意义不大。

:::warning
由于 mesh 协议不包含优化的二层组播转发，因此最好避免在 mesh 网络上转发任何组播流量（包括 OSPF）。如果你需要 OSPF，则必须配置使用单播模式的 [OSPF NBMA](../../user-guides/routing-and-networking-protocols/unicast/ospf/neighbour-relationship.md#discovery-on-nbma-subnets) 邻居。
:::

**问：性能和 CPU 要求如何？**

答：如果配置得当，协议本身消耗的资源将远少于 OSPF（例如）。单个路由器上的数据转发性能应接近桥接性能。

**问：它与现有使用 RSTP 的 mesh 设置如何协同工作？**

答：RSTP 网络的内部结构对 mesh 协议是透明的（因为 mesh hello 数据包在 RSTP 网络内部转发）。mesh 将 RSTP 网络中两个入口点之间的路径视为单个网段。另一方面，mesh 网络对 RSTP 不是透明的，因为 RSTP hello 数据包不会在 mesh 网络内部转发。

:::warning
如果 mesh 网络以两个或更多点连接到 RSTP 网络，则可能出现路由环路！
:::

请注意，如果你在两个接入点之间有 WDS 链路，则两端必须具有相同的配置（要么在两端都作为 mesh 端口，要么在两端都作为桥接接口的端口）。

你也可以将桥接接口作为 mesh 端口（例如，以便能够使用桥接防火墙）。

**问：我可以有多个网络入口/出口点吗？**

答：如果入口/出口点被配置为门户（即使用主动模式），mesh 网络内的每个路由器将选择其最近的门户并将所有数据转发给它。然后，门户将在需要时代表路由器发现路径。

**问：如何控制或过滤 mesh 流量？**

答：目前唯一的方法是使用桥接防火墙。创建一个桥接接口，将 WDS 接口和/或以太网接口放入该桥接中，然后将该桥接放入 mesh 接口中。然后配置桥接防火墙规则。

要匹配用于 mesh 流量封装的 MAC 协议，请使用 MAC 协议号 0x9AAA；要匹配 mesh 路由流量，请使用 MAC 协议号 0x9AAB。示例：

```ros
/interface/bridge/settings/set use-ip-firewall=yes 
/interface/bridge/filter/add chain=input action=log mac-protocol=0x9aaa 
/interface/bridge/filter/add chain=input action=log mac-protocol=0x9aab
```

:::warning
完全有可能创建无法正常工作的混合 mesh/桥接设置（例如，*问题示例 1* 中使用桥接代替交换机）。推荐的始终有效的故障安全方法是：为每个物理接口创建一个单独的桥接接口；然后将所有这些桥接接口添加为 mesh 端口。
:::

## 高级主题

我们都知道，创建有问题的二层桥接或路由设置很容易，并且调试起来可能很困难。（与三层路由设置相比。）因此，这里有几个可能给你带来问题的错误配置示例。请避免它们！

### 问题示例 1：mesh 内的以太网交换机

*路由器 A 在 mesh 外部；其余所有路由器都在 mesh 内部。对于路由器 B、C、D，所有接口都添加为 mesh 端口*：
![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-08.webp)

路由器 A 将无法与路由器 C 可靠通信。当 D 是以太网的指定路由器时，问题就会出现；如果 B 承担此角色，则一切正常。问题的主要原因是以太网交换机上的 MAC 地址学习。

考虑当路由器 A 想要向 C 发送数据时会发生什么。我们假设路由器 A 知道或向所有接口泛洪数据。无论哪种方式，数据都会到达交换机。交换机不知道目的 MAC 地址的任何信息，会将数据转发给 B 和 D。

现在会发生什么：

1. B 在 mesh 接口上接收到数据包。由于 MAC 地址不是 B 本地的，并且 B 知道它不是以太网网络的指定路由器，因此它只是忽略该数据包。
2. D 在 mesh 接口上接收到数据包。由于 MAC 地址不是 D 本地的，并且 D 是以太网网络的指定路由器，因此它启动到 C 的路径发现过程。

路径发现完成后，D 得知 C 可通过 B 到达。现在 D 封装数据包并将其转发回以太网网络。封装的数据包由交换机转发，由 B 接收并转发，并由 C 接收。到目前为止一切正常。

现在 C 很可能会响应数据包。由于 B 已经知道 A 在哪里，它将解封装并转发回复数据包。但现在交换机会学习到 C 的 MAC 地址可通过 B 到达！这意味着，下次当来自 A 的数据发往 C 时，交换机将*仅*将数据转发给 B（而 B 当然会静默地忽略该数据包）！

相反，如果 B 承担了指定路由器的角色，一切都会正常，因为流量不必两次通过以太网交换机。

***故障排除***：要么避免这种设置，要么在交换机上禁用 MAC 地址学习。请注意，在许多交换机上这是不可能的。

另请注意，如果满足以下任一条件，则不会出现问题：

- 路由器 A 支持并配置为使用 HWMP+。
- 或者将以太网交换机替换为支持 HWMP+ 且将以太网接口添加为 mesh 端口的路由器。

### 问题示例 2：无线模式

*考虑这个（无效的）设置示例*...*路由器 A 和 B 在 mesh 内部，路由器 C 在外部。对于路由器 A 和 B，所有接口都添加为 mesh 端口：*

![](https://manual.mikrotik.com/docs/wireless/abgn/img/hwmpplus-mesh-09.webp)

现在无法在路由器 B 上桥接 wlan1 和 wlan2。如果你了解 WDS 的工作原理，原因就非常明显了。WDS 通信使用四地址帧。这是因为对于无线多跳转发，你需要知道中间跳的地址，以及原始发送方和最终接收方的地址。相比之下，非 WDS 802.11 通信在帧中仅包含三个 MAC 地址。这就是为什么在站点模式下无法进行多跳转发的原因。

***故障排除*** 取决于你想要实现的目标：

1. 如果你希望路由器 C 充当无线或以太网流量的中继器，请在路由器 B 和路由器 C 之间配置 WDS 链路，并在所有节点上运行 mesh 路由协议。
2. 在其他情况下，将路由器 B 上的 wlan2 配置为 AP 模式，并将路由器 C 上的 WLAN 配置为站点模式。