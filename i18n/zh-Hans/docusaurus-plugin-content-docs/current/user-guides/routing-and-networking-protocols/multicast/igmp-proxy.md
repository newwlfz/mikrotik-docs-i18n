# IGMP 代理

> RouterOS 中的 IGMP 代理功能通过转发 IGMP 帧来实现组播路由，为某些拓扑结构提供了一种比 PIM-SM 更简单的替代方案。它支持基本的组播转发，资源占用极少，但不支持复杂的路由设置和环路检测。

# IGMP 代理

互联网组管理协议（IGMP）代理可以实现组播路由。它转发 IGMP 帧，通常在无需使用 PIM 等更高级协议时使用。

## IGMP 代理特性

- 实现组播路由的最简单方式。
- 可用于因某种原因不适合使用 PIM-SM 的拓扑结构。
- 相比 PIM-SM，资源占用略少。
- 配置简便。

另一方面，IGMP 代理不太适合复杂的组播路由设置。与基于 PIM 的解决方案相比，IGMP 代理不支持多个上游接口，且无法检测或避免路由环路。

默认情况下，IGMP 代理的上游接口会发送 IGMPv3 成员资格报告，并根据接收到的查询报文检测上游设备（例如组播路由器）所使用的 IGMP 版本。如果接收到 IGMPv1/v2 查询报文，上游端口将回退到较低的 IGMP 版本。当 IGMPv1/v2 查询器存在定时器（400 秒）到期后，它将转换回 IGMPv3。IGMP 代理的下游接口仅发送 IGMPv2 查询报文。

:::warning
RouterOS v7 在主 **system** 软件包中提供 IGMP 代理配置。较旧版本的 RouterOS 需要额外安装 **multicast** 软件包才能使用 IGMP 代理。有关更多详细信息，请参阅 [软件包](../../../getting-started/installation-and-upgrade/packages.md)。
:::

## 示例

---

要将来自 ether2 接口的所有组播数据转发到下游的 bridge 接口（订阅者连接处），请使用以下配置。两个接口都应配置 IP 地址。

```ros
/routing/igmp-proxy/interface
add interface=ether2 upstream=yes
add interface=bridge1

[admin@MikroTik] /routing/igmp-proxy/interface/print
Flags: U - UPSTREAM
Columns: INTERFACE, THRESHOLD
#   INTERFACE  THRESHOLD
0 U ether2             1
1   bridge1            1
```

如果组播发送方地址位于本地路由器无法直接到达的 IP 子网中，您可能还需要在上游接口上配置 `alternative-subnets`：

```ros
/routing/igmp-proxy/interface
set [find upstream=yes] alternative-subnets=192.168.50.0/24,192.168.60.0/24
```