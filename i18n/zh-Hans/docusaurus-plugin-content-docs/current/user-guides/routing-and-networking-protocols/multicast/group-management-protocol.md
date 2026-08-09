# Group Management Protocol

> Group Management Protocol 使接口无需专用客户端即可接收组播流，支持 IGMP 和 MLD 协议。它允许通过发送成员报告和响应查询来测试组播路由，并在禁用时自动清理。

# Group Management Protocol

Group Management Protocol 允许任何接口成为组播流的接收者。它使得在不使用专用 IGMP 或 MLD 客户端的情况下，测试组播路由和交换配置成为可能。该选项自 RouterOS v7.4 起可用，并支持 IGMP v1、v2、v3 以及 MLD v1、v2 协议。

接口默认使用 IGMP v3 和 MLD v2。若收到 IGMP v1、v2 或 MLD v1 查询，接口将回退至相应版本。一旦在接口上创建 Group Management Protocol，它将发送未经请求的成员报告（加入）数据包，并响应查询消息。若配置被移除或禁用，接口将发送离开消息。

## 示例

---

此示例演示如何在接口上配置简单的组播监听器。

首先，在接口上添加 IP 地址：

```ros
/ip/address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
```

然后，在同一接口上配置 Group Management Protocol：

```ros
/routing/gmp
add groups=229.1.1.1 interfaces=ether1
```

现在，您可以检查组播网络，以确认路由器或交换机是否已创建相应的组播转发条目，以及接口是否正在接收组播数据（参见接口统计信息，或使用 [Packet Sniffer](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 和 [Torch](../../../diagnostics-monitoring-and-troubleshooting/torch.md)）。