# 理解 BGP

> BGP 协议基础概述。

# 理解 BGP

**边界网关协议**（**BGP**）是一种外部网关协议（**EGP**）。它允许您建立域间动态路由系统。当网络拓扑发生变化时，该系统会自动更新 BGP 路由器上的路由表。

BGP 是一种基于**路径向量**算法的自治系统间路由协议。它通过互联网交换路由信息，是唯一设计用于在互联网规模下运行并处理与无关路由域多连接的协议。

BGP 旨在允许管理员实施复杂的路由策略。它不交换网络拓扑信息，而是交换可达性信息。因此，BGP 更适合**AS 间**环境以及信息源等特殊场景。如果您需要在网络中启用动态路由，请改用 OSPF。

:::info
SMIPS 设备（hAP lite、hAP lite TC 和 hAP mini）不支持 BGP。
:::

## 术语

- **AS** - 自治系统是在单一技术管理下、具有共同度量标准的一组路由器。
- **ASN** - 自治系统编号是自治系统的唯一标识符。ASN 可以是私有的或公共的。公共 ASN 在全球范围内唯一，由 RIPE 等监管机构分配。
- **AS Path** - 路由经过的自治系统序列。
- **路径属性** - 包含有关 AS 路径的附加信息，并用于路由策略。
- **路由策略** - 一组规则，用于控制路由信息的再分发并在多个可用路径中选择最佳路径。
- **NLRI** - 网络层可达性信息是 BGP 对等体之间交换的内容，表示如何到达前缀。
- **IGP** - 内部网关协议，如 OSPF 或 ISIS。
- **EGP** - 外部网关协议，如 BGP。
- **RR** - 路由反射器是一种 BGP 路由器，它在 **iBGP** 扬声器之间反射路由信息，从而无需全互联连接。
- **路由服务器** - 一种不参与流量转发的 BGP 路由器。路由通常甚至不会安装到 FIB 中。
- **环回地址** - 配置在虚拟桥接接口上的 /32（IPv4）或 /128（IPv6）地址，可充当环回接口。

BGP 连接有两种类型：

- **iBGP** - 连接同一 AS 内对等体的“内部”链路。
- **eBGP** - 连接属于两个不同 AS 的对等体的“外部”链路。

## 协议基础

BGP 路由器通过传输协议交换可达性信息；对于 BGP，该协议是 TCP（端口 179）。建立 TCP 连接后，这些路由器交换 **OPEN** 消息以协商并确认支持的能力。

在就使用的能力达成一致后，会话被视为**已建立**，对等体可以开始通过 **UPDATE** 消息交换 NLRI。这些消息指示路由到达目标网络（NLRI 前缀）应经过的 AS 序列（AS Path）。

对等体最初交换其完整路由表，在初始交换之后，随着路由表的变化发送增量更新。因此，BGP 不需要定期刷新整个 BGP 路由表。

BGP 维护路由表版本号，在连接期间，任意两个给定对等体之间的版本号必须相同。

**KEEPALIVE** 消息定期发送以确保连接正常运行。如果在**保持时间**间隔内未收到消息，则连接关闭。

为了响应错误或特殊情况，可以生成 **NOTIFICATION** 消息并发送到远程对等体；此消息类型还指示连接是否应立即关闭。

一个 AS 可能有多个 BGP 扬声器，并为其他 AS 提供中转服务。这意味着 BGP 扬声器必须保持 AS 内路由的一致视图。通过让 AS 内的所有 BGP 路由器相互建立直接的 **iBGP** 连接（全互联）或利用**路由反射器**设置，可以提供 AS 外部路由的一致视图。

通过使用一组管理策略（路由策略），AS 内的 BGP 扬声器就特定目的地使用哪个入口或出口点达成一致。此信息使用内部路由协议（**IGP**），例如 OSPF、RIP 或静态路由，传达给 AS 的内部路由器。在某些设置中，iBGP 也可以承担 IGP 协议的角色。

对于某些 BGP 属性，处理行为可能因连接类型而异；例如，**LOCAL-PREF** 属性不会通告给 **eBGP** 对等体。

RouterOS 将配置和会话监控分为四个菜单：

- 实例菜单（[`/routing/bgp/instance`](../../../../cli-reference/routing/bgp.md#routingbgpinstance)）
- 连接菜单（[`/routing/bgp/connection`](../../../../cli-reference/routing/bgp.md#routingbgpconnection)）
- 会话菜单（[`/routing/bgp/session`](../../../../cli-reference/routing/bgp.md#routingbgpsession)）
- 模板菜单（[`/routing/bgp/template`](../../../../cli-reference/routing/bgp.md#routingbgptemplate)）

## 路由来源

首次通告路由的 BGP 路由器会分配其来源并将其写入 **ORIGIN** 属性。  
有三种来源类型：

- 0 - 路由器最初通过 **IGP** 学习到该路由。如果路由是通过 BGP [`output.network`](../../../../cli-reference/routing/bgp.md#output.network) 学习到的，RouterOS 会分配此值。
- 1 - 路由器最初通过 **EGP** 学习到该路由。
- 2 - 来源未知/不完整。如果路由是通过 BGP [`output.redistribute`](../../../../cli-reference/routing/bgp.md#output.redistribute) 学习到的，RouterOS 会分配此值。

## 最佳路径选择

BGP 路由器可以从多个提供商接收全局路由表的多个副本，但默认情况下 BGP 只能有一条最佳路径。为了选择最佳路由，BGP 使用**最佳路径选择算法**。

只有路由有效时，算法才会对其进行评估。通常，路由在以下情况下被视为有效：

- 路由的 **NEXT_HOP** 有效且可达
- 从外部对等体接收的 **AS_PATH** 不包含本地 AS
- 路由未被[路由过滤器](../../../../cli-reference/routing/filter.md#routingfilter)拒绝

更多信息请阅读[下一跳选择与验证](./nexthop-selection.md)。

最佳路径算法还只比较由**单个 BGP 实例**接收的路由。由不同 BGP 实例安装的路由由通用算法进行比较；即比较路由距离，距离较低的路由优先。

如果满足所有条件，则执行以下操作：

1. 接收到的第一条路径自动被视为“最佳路径”。任何后续接收到的路径都与第一条接收到的路径进行比较，以确定新路径是否更好。
2. 优先选择 **WEIGHT** 最高的路径。
   此参数不是 BGP 标准的一部分，它是为了快速本地选择最佳路由而发明的。该参数是路由器本地的（在 BGP 输入中使用路由过滤器分配），不能通告。未分配 WEIGHT 的路由默认值为 0。
3. 优先选择 **LOCAL_PREF** 最高的路径。
   此属性仅在 AS 内使用。没有 LOCAL_PREF 属性的路径默认值为 100。
4. 优先选择 **AS_PATH** 最短的路径（如果 [`ignore-as-path-len`](../../../../cli-reference/routing/bgp.md#ignore-as-path-len) 设置为 **yes**，则跳过）。  
   每个 **AS_SET** 计为 1，无论集合大小如何。**AS_CONFED_SEQUENCE** 和 **AS_CONFED_SET** 不包含在 **AS_PATH** 长度中。
5. ~~优先选择通过聚合或 BGP 网络本地发起的路径~~
6. 优先选择 [**ORIGIN** 类型](#route-origin)最低的路径。

   内部网关协议（IGP）低于外部网关协议（EGP），EGP 低于 INCOMPLETE。

   换句话说，**IGP < EGP < INCOMPLETE**。
7. 优先选择 **multi-exit discriminator**（MED）最低的路径。

   路由器仅对具有相同邻居（最左侧）AS 的路径比较 MED 属性。在确定邻居 AS 时不考虑联盟。  
   没有显式 MED 值的路径被视为 MED 为 0。
8. 优先选择 **eBGP** 路径而非 **iBGP** 路径。
9. 如果启用了 `multipath`，则在此处中断并将路径视为相等。这将安装 BGP [ECMP](../../routing-decision.md#multipath-ecmp-routes) 路由。
10. 优先选择 **IGP 度量**最低的路径。
11. 优先选择来自 **router ID** 最低的 BGP 路由器的路由。如果路由带有 **ORIGINATOR_ID** 属性，则使用 **ORIGINATOR_ID** 代替路由器 ID。
12. 优先选择**路由反射集群列表**最短的路由。没有集群列表的路由被视为集群列表长度为 0。
13. 优先选择来自邻居地址最低的路径。

## 多实例

可能需要运行多个 BGP 实例以支持依赖于实例的功能，如 Layer3 VPN 和 [EVPN](../evpn.md)。RouterOS 允许您在 [`/routing/bgp/instance`](../../../../cli-reference/routing/bgp.md#routingbgpinstance) 菜单中添加多个实例。

请注意，[最佳路径选择](#best-path-selection)不适用于来自不同实例的路由。此外，默认再分发策略不会再分发从不属于同一实例的会话接收到的 BGP 路由。在这种情况下，如果需要此类再分发，请设置 [`output.redistribute`](../../../../cli-reference/routing/bgp.md#output.redistribute)`=bgp`。

## 支持的標準

- [RFC 4271](https://tools.ietf.org/html/rfc4271) 边界网关协议 4
- [RFC 4456](https://tools.ietf.org/html/rfc4456) BGP 路由反射
- [RFC 5065](https://tools.ietf.org/html/rfc5065) BGP 自治系统联盟
- [RFC 1997](https://tools.ietf.org/html/rfc1997) BGP 社区属性
- [RFC 8092](https://tools.ietf.org/html/rfc8092) BGP 大社区
- [RFC 4360](https://tools.ietf.org/html/rfc4360)、[5668](https://tools.ietf.org/html/rfc5668) BGP 扩展社区
- [RFC 2385](https://tools.ietf.org/html/rfc2385) BGPv4 的 TCP MD5 认证
- [RFC 5492](https://tools.ietf.org/html/rfc5492) BGP-4 能力通告
- [RFC 2918](https://tools.ietf.org/html/rfc2918) 路由刷新能力
- [RFC 4760](https://tools.ietf.org/html/rfc4760) BGP-4 多协议扩展
- [RFC 2545](https://tools.ietf.org/html/rfc2545) 使用 BGP-4 多协议扩展进行 IPv6 域间路由
- [RFC 4893](https://tools.ietf.org/html/rfc4893) BGP 对四字节 AS 编号空间的支持
- [RFC 4364](https://tools.ietf.org/html/rfc4364) BGP/MPLS IP 虚拟专用网络（VPN）
- [RFC 4761](https://tools.ietf.org/html/rfc4761) 使用 BGP 进行自动发现和信令的虚拟专用局域网服务（VPLS）
- draft-ietf-l2vpn-signaling-08 Cisco 基于 BGP 的 VPLS 自动发现
- [RFC 6286](https://tools.ietf.org/html/rfc6286) BGP-4 的 AS 范围唯一 BGP 标识符
- [RFC 4273](https://tools.ietf.org/html/rfc4273) SNMP 对等体表监控（OID 1.3.6.1.2.1.15.3.1）（仅 IPv4）
- [RFC 6793](https://www.rfc-editor.org/rfc/rfc6793) 4 字节 ASN 支持和聚合器属性。
- [RFC 4486](https://datatracker.ietf.org/doc/html/rfc4486) BGP 停止通知消息的子代码
- [RFC 4659](https://datatracker.ietf.org/doc/html/rfc4659) IPv6 的 MPLS VPN 扩展
- [RFC 8950](https://datatracker.ietf.org/doc/html/rfc8950) 使用 IPv6 下一跳通告 IPv4 网络层可达性信息（NLRI）
- [RFC 6811](https://datatracker.ietf.org/doc/html/rfc6811) BGP 前缀来源验证
- [RFC 6996](https://www.rfc-editor.org/rfc/rfc6996.html) 私有使用的自治系统（AS）保留
- [RFC 9234](https://datatracker.ietf.org/doc/rfc9234/) 使用 UPDATE 和 OPEN 消息中的角色进行路由泄漏预防和检测
- [RFC 5549](https://datatracker.ietf.org/doc/html/rfc5549) 使用 IPv6 下一跳通告 IPv4 网络层可达性信息