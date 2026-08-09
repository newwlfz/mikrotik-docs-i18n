# VPLS

> 本页介绍 MikroTik RouterOS 的虚拟专用局域网服务（VPLS）接口，详细说明其作为透明以太网隧道（使用 LDP 或 MP-BGP 协议）的用途。内容涵盖 VPLS 特性，如伪线信令、分片以及基于 BGP 的自动发现，同时包括 MPLS 标签分发的前提条件及 i

import DocCardList from '@theme/DocCardList';

# VPLS

虚拟专用局域网服务（VPLS）接口可视为一种隧道接口，类似于 [EoIP](../../../../virtual-private-networks/eoip.md) 接口，用于实现客户站点之间的透明以太网段转发。

VPLS 隧道的协商可通过 LDP 协议或 MP-BGP 完成——隧道两端点交换它们将用于该隧道的标签。

隧道中的数据转发通过在数据包上叠加两个标签实现：隧道标签和传输标签——后者用于确保流量传递到隧道的另一端。

MikroTik RouterOS 实现以下 VPLS 特性：

- VPLS LDP 信令（RFC 4762）。
- Cisco 风格静态 VPLS 伪线（RFC 4447 FEC 类型 0x80）。
- VPLS 伪线分片与重组（RFC 4623）。
- 基于 MP-BGP 的 VPLS 自动发现与信令（RFC 4761）。
- Cisco VPLS 基于 BGP 的自动发现（draft-ietf-l2vpn-signaling-08）。
- 支持基于 BGP 的 VPLS 多导入/导出 route-target 扩展团体（同时支持 RFC 4761 和 draft-ietf-l2vpn-signaling-08）。

## VPLS 前提条件

为使 VPLS 能够传输 MPLS 数据包，骨干网上应已运行一种标签分发协议；可以是 LDP、RSVP-TE 或静态绑定。

在继续之前，请熟悉 [LDP 所需的前提条件](../ldp.md#prerequisites-for-mpls) 以及 RSVP-TE 的前提条件。

如果使用 BGP 作为 VPLS 的发现和信令协议，骨干网应运行 iBGP，最好配置路由反射器。

## 配置示例

假设我们已经有一个来自 [LDP 配置示例](../ldp.md#example-setup) 的正常运行的 LDP 配置。

路由器 R1、R3 和 R4 连接到客户 A 的站点，路由器 R1 和 R3 连接到客户 B 的站点。客户要求站点之间具有透明的二层连接。