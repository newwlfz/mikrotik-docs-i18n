# MPLS

> MPLS 是一种路由技术，它使用标签来加速数据包转发，而无需分析 IP 头。RouterOS 支持 MPLS 交换、LDP/RSVP-TE 协议、VPLS 和 MP-BGP VPN，但不包括某些 LDP/TE 功能。

import DocCardList from '@theme/DocCardList';

MPLS 代表多协议标签交换（MultiProtocol Label Switching）。与使用 IP 路由不同，MPLS 基于附加在数据包上的标签（而非 IP 头中的字段，如目的地址，以及路由表）来决定数据包的转发决策（出接口和下一跳路由器）。这种方法加快了转发过程，因为下一跳查找比路由查找（寻找最长匹配前缀）更简单。

转发过程的效率是 MPLS 的主要优势。但请注意，MPLS 转发会禁用网络层（例如 IP）头的处理。因此，您不能对 MPLS 转发的数据包应用基于网络层的操作，如 NAT 和过滤。请在 MPLS 云的入口或出口处应用任何基于网络层的操作，其中入口是首选方法。这样，您打算丢弃的流量就不会穿过 MPLS 骨干网。

MPLS 通过 LDP 协议为活动路由分发标签来运作，带标签的数据包与不带标签的数据包走相同的路径。当路由器沿着某条路由转发不带标签的数据包时，如果它已从下一跳收到了该路由的标签，它就会在数据包上打上标签并将其发送到下一跳，在那里 MPLS 会沿着路径进一步交换它。当路由器收到一个带有它已分配给特定路由的标签的数据包时，它会用从该路由的下一跳收到的标签替换数据包标签，并将数据包发送到下一跳。标签交换路径（LSP）确保数据传送到 MPLS 云的出口点。MPLS 应用正是基于这种标签交换路径的概念。

建立标签交换路径的另一种方式是通过使用 RSVP-TE 协议的流量工程隧道（TE 隧道）。流量工程隧道允许显式路由的 LSP 和基于约束的路径选择（其中约束是接口属性和可用带宽）。

由于 MPLS 引入了复杂性和新协议，并为路由和桥接网络增加了不同的概念，因此在生产网络中实施 MPLS 之前，您应该深入了解 MPLS 概念。一些建议的阅读材料：

- 多协议标签交换 [http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching](http://en.wikipedia.org/wiki/Multiprotocol_Label_Switching)
- RFC3031 多协议标签交换架构 [http://www.ietf.org/rfc/rfc3031.txt](http://www.ietf.org/rfc/rfc3031.txt)
- Luc De Ghein 著《MPLS 基础》 [http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974](http://www.amazon.com/MPLS-Fundamentals-Luc-Ghein/dp/1587051974)

:::info
此功能在 SMIPS 设备（hAP lite、hAP lite TC 和 hAP mini）上不受支持。
:::

## 支持的功能

RouterOS 支持以下与 MPLS 相关的功能：

- 支持倒数第二跳弹出（PHP）的 MPLS 交换。
- 支持 IPv4 和 IPv6 的静态本地标签绑定。
- 支持 IPv4 和 IPv6 的静态远程标签绑定。
- 支持 IPv4 和 IPv6 的标签分发协议（[RFC 3036](https://tools.ietf.org/html/rfc3036)、[RFC 5036](https://tools.ietf.org/html/rfc5036) 和 [RFC 7552](https://tools.ietf.org/html/rfc7552)）：
  - 下游主动标签通告。
  - 独立标签分发控制。
  - 宽松标签保留。
  - 定向会话建立。
  - 可选环路检测。
  - ECMP 支持。
- 虚拟专用局域网服务（VPLS）：
  - VPLS LDP 信令（[RFC 4762](https://tools.ietf.org/html/rfc4762)）。
  - Cisco 风格静态 VPLS 伪线（[RFC 4447](https://tools.ietf.org/html/rfc4447) FEC 类型 0x80）。
  - VPLS 伪线分片与重组（[RFC 4623](https://tools.ietf.org/html/rfc4623)）。
  - 基于 MP-BGP 的 VPLS 自动发现和信令（[RFC 4761](https://tools.ietf.org/html/rfc4761)）。
  - Cisco VPLS 基于 BGP 的自动发现（[draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)）。
  - 支持基于 BGP 的 VPLS 的多个导入/导出路由目标扩展团体（[RFC 4761](https://tools.ietf.org/html/rfc4761) 和 [draft-ietf-l2vpn-signaling-08](https://tools.ietf.org/html/draft-ietf-l2vpn-signaling-08)）。
- RSVP-TE 隧道：
  - 隧道头端。
  - 显式路径。
  - 用于 TE 隧道的 OSPF 扩展。
  - CSPF 路径选择。
  - 在 TE 隧道上转发 VPLS 和 MPLS IP VPN 流量。
  - 入口 TE 隧道速率限制和自动预留带宽调整。更多信息，请参阅 [流量工程](./traffic-eng.md)。
  - 所有隧道带宽设置均以比特每秒为单位指定和显示。
- 基于 MP-BGP 的 MPLS IP VPN。
- 基于 MP-BGP 的 MPLS VPN 的每前缀和每 VRF 标签分发策略。
- 用于 MPLS TE 的 OSPF 扩展。
- 支持 OSPF 作为 CE-PE 协议。
- 对指定 VRF 执行 Ping 和 Traceroute。
- 控制 MPLS 中网络层 TTL 的传播。
- 支持 RIP 作为 CE-PE 协议。
- 每 VRF BGP 实例的重分发设置。

## RouterOS 尚不具备的 MPLS 功能

- LDP 功能：
  - 下游按需标签通告。
  - 有序标签分发控制。
  - 保守标签保留。
- TE 功能：
  - 快速重路由。
  - 链路/节点保护。
- 支持 BGP 作为标签分发协议。

<DocCardList />