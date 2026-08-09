# OSPF

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/ospf

**类型：** 目录

### routing/ospf/area

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="T" typ="transit-capable">可中转</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">区域名称</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">该区域所属的 OSPF 实例名称。</ArgTableRow>
<ArgTableRow arg="area-id" typ="ipAddr">OSPF 区域标识符。如果路由器在多个区域中有网络，则必须始终存在一个 `area-id=0.0.0.0`（骨干区域）的区域。骨干区域始终包含所有区域边界路由器。骨干区域负责在非骨干区域之间分发路由信息。骨干区域必须是连续的，即不能有断开的段。但是，区域边界路由器不需要物理连接到骨干区域 - 可以通过虚拟链路模拟连接。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (default | stub | nssa)">区域类型。更多关于区域类型的信息，请参阅 [OSPF 用户指南](../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md#understanding-ospf-areas)。</ArgTableRow>
<ArgTableRow arg="no-summaries" typ="switch">标志参数，如果设置，则该区域将不会在 stub 区域中泛洪汇总 LSA。</ArgTableRow>
<ArgTableRow arg="default-cost" typ="num" unset="1">注入到该区域的 LSA 的默认开销。如果未设置该值，则不会生成 stub 区域类型-3 默认 LSA。</ArgTableRow>
<ArgTableRow arg="nssa-translator" typ="enum (candidate | no | yes)" unset="1">
该参数指示哪个 ABR 将用作从 `type-7` 到 `type-5` LSA 的转换器。仅当区域类型为 NSSA 时适用。
- yes - 路由器将始终用作转换器。
- no - 路由器将永远不会用作转换器。
- candidate - OSPF 选举一个候选路由器作为转换器。
</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="transit-capable" typ="bool"></ArgTableRow>
</ArgTable>

#### routing/ospf/area/range

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
<ArgTableRow arg="A" typ="advertise">通告</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">与此范围关联的 OSPF 区域。</ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" mandatory="1">此范围的网络前缀。</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">是否创建汇总 LSA 并将其通告到相邻区域。</ArgTableRow>
<ArgTableRow arg="cost" typ="num" unset="1">此范围将创建的汇总 LSA 的开销。默认 - 使用所有路由（即落在该范围内的路由）的最大开销。</ArgTableRow>
</ArgTable>

### routing/ospf/instance

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3)">此实例将运行的 OSPF 版本（v2 用于 IPv4，v3 用于 IPv6）。</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">此 OSPF 实例操作的 VRF 表。</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ipAddr
, enum
 }">OSPF 路由器 ID。可以显式设置为 IP 地址，或设置为 router-id 实例的名称。</ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1">用于输出选择的路由过滤器选择链的名称。输出仅操作**外部**路由。</ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">指定默认路由（`0.0.0.0/0`）的分发方法。</ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1">用于传入前缀的 [路由过滤器](../../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md#route-filtering) 链的名称。</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-address" typ="address (flags=64)" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-area" typ="ipAddr" unset="1">用于 MPLS 流量工程（TE）的区域。TE Opaque LSA 在此区域中生成。最多只能有一个 OSPF 实例配置 `mpls-te-area`。</ArgTableRow>
<ArgTableRow arg="domain-id" typ="address (flags=R)" unset="1">MPLS 相关参数。标识实例的 OSPF 域。该值作为 BGP 扩展团体属性附加到在 BGP 中作为 VPNv4 路由重新分发的 OSPF 路由上，并在 BGP VPNv4 路由重新分发回 OSPF 时用于确定为该路由生成 `inter-area` 还是 `AS-external` LSA。默认情况下使用 Null domain-id，如 [RFC 4577](https://tools.ietf.org/html/rfc4577) 所述。</ArgTableRow>
<ArgTableRow arg="domain-tag" typ="num" unset="1">如果设置，则用于路由重新分发（作为此路由器生成的所有外部 LSA 中的路由标签），以及路由计算（忽略所有具有此路由标签的外部 LSA）。用于与较旧的 Cisco 系统互操作。默认情况下不设置。</ArgTableRow>
<ArgTableRow arg="use-dn" typ="bool" unset="1">强制使用或忽略 DN 位。在某些 CE-PE 场景中用于将 `intra-area` 路由注入 VRF。如果未设置该参数，则根据 RFC 使用 DN 位。</ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">启用特定路由类型的重新分发。</ArgTableRow>
</ArgTable>

### routing/ospf/interface

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=4i)" unset="1"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | virtual-link)">
此接口上的 OSPF 网络类型。请注意，如果接口配置不存在，则默认网络类型在 PtP 接口上为 'ptp'，在所有其他接口上为 'broadcast'。
- `broadcast` - 适用于以太网和其他支持多播的链路层的网络类型。选举指定路由器（DR）。
- `nbma` - 非广播多路访问（Non-Broadcast Multiple Access）。协议报文发送到每个邻居的单播地址。需要手动配置邻居。选举指定路由器（DR）。
- `ptp` - 适用于仅由两个节点组成的网络。不选举指定路由器（DR）。
- `ptmp` - 点对多点（Point-to-Multipoint）。比 NBMA 更容易配置，因为它不需要手动配置邻居。不选举指定路由器（DR）。这是最健壮的网络类型，因此适用于无线网络，如果 'broadcast' 模式对它们来说效果不佳。
- `ptp-unnumbered` - 与 ptp 工作方式相同，只是远程邻居没有关联到特定 PTP 接口的 IP 地址。例如，在 Cisco 设备上使用 IP unnumbered 的情况下。
- `virtual-link` - 用于虚拟链路的接口。
</ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="vlink-transit-area" typ="enum" unset="1">两个路由器共同拥有的非骨干区域，虚拟链路将在此区域上建立。虚拟链路不能通过 stub 区域建立。</ArgTableRow>
<ArgTableRow arg="vlink-neighbor-id" typ="ipAddr" unset="1">指定应通过虚拟链路连接的邻居的**路由器 ID**。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="state" typ="enum (down | loopback | ptp | passive | waiting | standby | dr-other | bdr | dr)"></ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="vlink-remote-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>

### routing/ospf/interface-template

**类型：** 目录

接口模板定义了通用的网络和接口匹配规则，以及要分配给匹配接口的参数。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">匹配接口将关联到的 OSPF 区域。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">匹配器。要匹配的接口。接受特定的接口名称或接口列表的名称。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="networks" typ="object { address (flags=46/)
 }" unset="1">匹配器。与区域关联的网络前缀。OSPF 将在所有具有至少一个地址落在此范围内的接口上启用。请注意，此检查使用地址的网络前缀（即不是本地地址）。对于点对点接口，这意味着远程端点的地址。</ArgTableRow>
<ArgTableRow arg="prefix-list" typ="enum" unset="1">包含应通告到 v3 接口的网络的地址列表名称。</ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast)">
此接口上的 OSPF 网络类型。请注意，如果接口配置不存在，则默认网络类型在 PtP 接口上为 'ptp'，在所有其他接口上为 'broadcast'。
- `broadcast` - 适用于以太网和其他支持多播的链路层的网络类型。选举指定路由器（DR）。
- `nbma` - 非广播多路访问（Non-Broadcast Multiple Access）。协议报文发送到每个邻居的单播地址。需要手动配置邻居。选举指定路由器（DR）。
- `ptp` - 适用于仅由两个节点组成的网络。不选举指定路由器（DR）。
- `ptmp` - 点对多点（Point-to-Multipoint）。比 NBMA 更容易配置，因为它不需要手动配置邻居。不选举指定路由器（DR）。这是最健壮的网络类型，因此适用于无线网络，如果 'broadcast' 模式对它们来说效果不佳。
- `ptp-unnumbered` - 与 ptp 工作方式相同，只是远程邻居没有关联到特定 PTP 接口的 IP 地址。例如，在 Cisco 设备上使用 IP unnumbered 的情况下。
</ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time">丢失的链路状态通告（LSA）重新发送的时间间隔。当路由器向其邻居发送链路状态通告（LSA）时，该 LSA 会一直保留，直到收到确认。如果在规定时间内（参见 transmit-delay）未收到确认，路由器将尝试重新传输该 LSA。</ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time">链路状态传输延迟是估计在接口上传输链路状态更新报文所需的时间。</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time">路由器在此接口上发送 **HELLO** 报文的时间间隔。此间隔越小，检测拓扑变化的速度就越快；代价是 OSPF 协议流量增加。此值在特定网络上的所有路由器上必须相同，否则它们之间将无法建立邻接关系。</ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time">指定邻居被宣告死亡后的时间间隔。此间隔在 hello 报文中通告。此值在特定网络上的所有路由器上必须相同，否则它们之间将无法建立邻接关系。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">
路由器的优先级。用于在广播网络中确定指定路由器（DR）。优先级值最高的路由器优先。优先级值 0 表示该路由器完全没有资格成为指定路由器（DR）或备份指定路由器（BDR）。

默认值为 128，如果您为 DR/BDR 选举设置了严格的优先级，请记住这一点。
</ArgTableRow>
<ArgTableRow arg="cost" typ="num">接口开销，表示为链路状态度量。</ArgTableRow>
<ArgTableRow arg="passive" typ="switch">如果启用，则路由器不会在匹配的接口上发送或接收 OSPF 流量。</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (simple | md5 | sha1 | sha256 | sha384 | sha512)" unset="1">
指定 OSPF 协议报文（消息）的认证方法。

- `simple` - 明文认证。
- `md5` - 密钥化消息摘要 5（MD5）认证。
- `sha*` - HMAC-SHA 认证 RFC5709。

如果未设置该参数，则不使用认证。
</ArgTableRow>
<ArgTableRow arg="auth-key" typ="string" unset="1">要使用的认证密钥，应在网络段的所有邻居上匹配。</ArgTableRow>
<ArgTableRow arg="auth-id" typ="num" unset="1">密钥 ID 用于计算消息摘要（在启用 MD5 或 SHA 认证时使用）。该值应与同一区域的所有 OSPF 路由器匹配。</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### routing/ospf/lsa

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="self-originated">LSA 是否由路由器自身发起。</ArgTableRow>
<ArgTableRow arg="F" typ="flushing">正在清除</ArgTableRow>
<ArgTableRow arg="W" typ="wraparound">回绕</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum">此 LSA 所属的区域。</ArgTableRow>
<ArgTableRow arg="link" typ="address (flags=4i)"></ArgTableRow>
<ArgTableRow arg="link-instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="originator" typ="ipAddr">LSA 记录的发起者。</ArgTableRow>
<ArgTableRow arg="id" typ="ipAddr">LSA 记录 ID</ArgTableRow>
<ArgTableRow arg="sequence" typ="num">链路 LSA 被更新的次数。</ArgTableRow>
<ArgTableRow arg="age" typ="num">上次更新发生的时间（以秒为单位）距今多久。</ArgTableRow>
<ArgTableRow arg="checksum" typ="num"></ArgTableRow>
<ArgTableRow arg="body" typ="string"></ArgTableRow>
</ArgTable>

### routing/ospf/neighbor

**类型：** 目录

当前活动的 OSPF 邻居列表。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="V" typ="virtual">虚拟</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">发现此邻居的接口名称。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">OSPF 邻居路由器的 IP 地址。</ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="router-id" typ="ipAddr">邻居路由器的**路由器 ID**</ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr">指定路由器（DR）的 IP 地址。</ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr">备份指定路由器（BDR）的 IP 地址。</ArgTableRow>
<ArgTableRow arg="state" typ="string">
- `Down` - 未从邻居收到任何 Hello 报文。
- `Attempt` - 仅适用于 NBMA 网络。该状态表示未从邻居收到任何近期信息。
- `Init` - 已从邻居收到 Hello 报文，但双向通信尚未建立（其自身的 RouterID 未列在 Hello 报文中）。
- `2-way` - 此状态表示双向通信已建立。DR 和 BDR 选举在此状态期间进行。路由器根据其是否为 DR 或 BDR，以及链路是点对点链路还是虚拟链路来建立邻接关系。
- `ExStart` - 路由器尝试建立用于报文信息交换的初始序列号。具有较高 ID 的路由器成为主路由器并开始交换。
- `Exchange` - 路由器交换数据库描述（DD）报文。
- `Loading` - 在此状态下，实际交换链路状态信息。向邻居发送链路状态请求报文，以请求在 Exchange 状态期间发现的任何新 LSA。
- `Full` - 邻接关系完成，邻居路由器完全邻接。LSA 信息在相邻路由器之间同步。路由器仅与其 DR 和 BDR 达到 Full 状态。P2P 链路除外。
</ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-retransmits" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="db-summaries" typ="num"></ArgTableRow>
<ArgTableRow arg="adjacency" typ="time">自邻接关系建立以来经过的时间。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

### routing/ospf/static-neighbor

**类型：** 目录

OSPF 邻居的静态配置。对于非广播多路访问网络是必需的。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="area" typ="enum" mandatory="1">邻居所属区域的名称。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)" mandatory="1">可用于到达邻居 IP 的单播 IP 地址和接口。例如，`address=1.2.3.4%ether1` 表示 IP 为 `1.2.3.4` 的邻居可通过 `ether1` 接口到达。</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="poll-interval" typ="time">向处于 `down` 状态（即没有来自它们的流量）的邻居发送 hello 报文的频率。</ArgTableRow>
</ArgTable>