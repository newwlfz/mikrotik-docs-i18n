# 理解 OSPF

> OSPF 协议基础概述。

# 理解 OSPF

OSPF（开放最短路径优先）是一种内部网关协议（IGP），旨在同一自治系统（AS）内的路由器之间分发路由信息。

该协议基于链路状态技术，相比距离矢量协议（如 RIP）具有多项优势：

- 不存在跳数限制。
- 组播地址用于发送路由信息更新。
- 仅在网络拓扑发生变化时发送更新。
- 通过将路由器划分为区域来逻辑定义网络。
- 注入 AS 的外部路由会被传输并打上标签。

然而，OSPF 也存在一些缺点：

- OSPF 对 CPU 和内存要求较高，因为 SPF 算法必须维护多份路由信息副本。
- 实现起来比 RIP 更为复杂。

## 术语

请查阅以下术语以理解 OSPF 的运作方式。您将在整个文档中遇到这些术语。

- **邻居（Neighbor）**：运行 OSPF 且相邻接口分配到同一区域的路由器。Hello 数据包用于发现邻居，除非您手动配置邻居。
- **邻接关系（Adjacency）**：路由器与其对应的 DR 和 BDR 之间的逻辑连接。除非形成邻接关系，否则路由器不会交换路由信息。
- **链路（Link）**：分配给任何给定网络的网络或路由器接口。
- **接口（Interface）**：路由器上的物理接口。当您将接口添加到 OSPF 时，它便成为用于构建链路数据库的链路。
- **LSA**：链路状态通告（Link State Advertisement），一种包含链路状态和路由信息的数据包，在 OSPF 邻居之间共享。
- **DR**：指定路由器（Designated Router），为最小化形成的邻接关系数量而选出的路由器。OSPF 在广播网络中使用此选项。
- **BDR**：备份指定路由器（Backup Designated Router），作为 DR 的热备。BDR 接收来自相邻路由器的所有路由更新，但不泛洪 LSA 更新。
- **[区域（Area）](./areas-and-virtual-links.md)**：为建立分层网络而进行的逻辑分组。
- **ABR**：区域边界路由器（Area Border Router），连接到多个区域的路由器。ABR 负责连接区域之间的路由汇总和更新抑制。
- **ASBR**：自治系统边界路由器（Autonomous System Boundary Router），连接到外部网络（位于不同 AS）的路由器。当您在该路由器上将其他协议的路由导入 OSPF 时，该路由器即成为 ASBR。
- **NBMA**：非广播多路访问网络。这些网络允许多路访问，但不具备广播能力。您必须在此类网络上手动配置 OSPF 邻居。
- **广播（Broadcast）**：具有广播能力的网络，例如以太网。
- **点对点（Point-to-point）**：一种无需 DR 和 BDR 的网络类型。
- **Router-ID**：用于标识 OSPF 路由器的 IP 地址。如果您未手动配置 OSPF [`router-id`](../../../../cli-reference/routing/ospf.md#router-id)，路由器将使用其分配的某个 IP 地址作为 Router-ID。
- **链路状态（Link State）**：两台路由器之间链路的状态。它定义了路由器接口与其相邻路由器之间的关系。
- **开销（Cost）**：链路状态协议为每条链路分配的值。[`cost`](../../../../cli-reference/routing/ospf.md#cost) 值取决于介质的速率。每个路由器接口在其输出侧都有相关的开销，称为接口输出开销。
- **自治系统（Autonomous System）**：使用共同路由协议交换路由信息的一组路由器。

## 支持的标准

- RFC [2328](https://tools.ietf.org/html/rfc2328) - OSPF 版本 2
- RFC [3101](https://tools.ietf.org/html/rfc3101) - OSPF 非完全末梢区域（NSSA）选项
- RFC [3630](https://tools.ietf.org/html/rfc3630) - OSPF 版本 2 的流量工程（TE）扩展
- RFC [4577](https://tools.ietf.org/html/rfc4577) - OSPF 作为 BGP/MPLS IP 虚拟专用网络（VPN）的提供商/客户边缘协议
- RFC [5329](https://tools.ietf.org/html/rfc5329) - OSPF 版本 3 的流量工程扩展
- RFC [5340](https://tools.ietf.org/html/rfc5340) - 用于 IPv6 的 OSPF
- RFC [5643](https://tools.ietf.org/html/rfc5643) - OSPFv3 的管理信息库
- RFC [6549](https://tools.ietf.org/html/rfc6549) - OSPFv2 多实例扩展
- RFC [6565](https://tools.ietf.org/html/rfc6565) - OSPFv3 作为提供商边缘到客户边缘（PE-CE）路由协议
- RFC [6845](https://tools.ietf.org/html/rfc6845) - OSPF 混合广播和点对多点接口类型
- RFC [7471](https://tools.ietf.org/html/rfc7471) - OSPF 流量工程（TE）度量扩展