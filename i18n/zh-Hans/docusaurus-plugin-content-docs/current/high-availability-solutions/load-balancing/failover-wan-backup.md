# 故障转移（WAN 备份）

> 本文档介绍了如何使用 MikroTik RouterOS 中的递归路由配置 WAN 连接的故障转移，详细说明了基本及改进的监控配置步骤，以实现可靠的链路切换。

# 故障转移（WAN 备份）

## 简介

本文描述了一种使用递归路由和路由作用域的高级故障转移方法。当路由（无论是静态还是动态学习的）的下一跳并非本地路由器直接连接时，就会发生递归路由。有必要限制可用于查找直接下一跳的路由集合。例如，RIP 或 OSPF 路由的下一跳值应可直接到达，并且应仅使用连接路由进行查找。这通过 `scope` 和 `target-scope` 属性实现。

## 设置概述

假设我们的网关有两条公共网络上行链路（“ISP1”、“ISP2”）。第一条上行链路应为首选，第二条作为备份。

然后，我们将流量分为两部分，一部分命名为“ISP1”，另一部分命名为“ISP2”，分别通过 ether1 和 ether2 传输。在此设置中，我们希望监控两台主机：Host1 和 Host2。我们将使用 IP 为 8.8.8.8（Host1）和 8.8.4.4（Host2）的 Google DNS 服务器，但并非强制使用这些特定地址。

![failover.png](https://manual.mikrotik.com/docs/high-availability-solutions/load-balancing/img/failover-wan-backup-01.webp)

## 配置

### 基本故障转移

在配置故障转移之前，我们必须对通过两条上行链路传输的 LAN 流量进行伪装。这允许本地网络中的设备通过任一连接访问互联网：

```ros
/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=ether1
add chain=srcnat action=masquerade out-interface=ether2
```

接下来，我们需要在互联网上定义两个可达主机，以监控每条上行链路的状态。这些主机应可靠并响应 ICMP 请求。在此示例中，我们使用 Google 的 DNS 服务器（8.8.8.8 和 8.8.4.4）：

```ros
/ip/route 
add dst-address=8.8.8.8 scope=10 gateway=10.111.0.1
add dst-address=8.8.4.4 scope=10 gateway=10.112.0.1
```

最后，我们添加默认路由，该路由将通过两个测试主机递归解析。ISP1 连接作为主链路（配置较低的距离值）：

```ros
/ip/route/
add distance=1 gateway=8.8.8.8 target-scope=11 check-gateway=ping
add distance=2 gateway=8.8.4.4 target-scope=11 check-gateway=ping
```

此配置确保如果主上行链路不可用，流量会自动故障转移到备用连接。

### 提高检测可靠性

目前，我们依赖单一主机进行链路可达性监控。尽管 Google 服务很少不可用，但我们可以通过在每个链路上添加第二个监控主机来提高可靠性。

```ros
/ip/route
add dst-address=208.67.222.222 gateway=10.111.0.1 scope=10
add dst-address=208.67.220.220 gateway=10.112.0.1 scope=10

add distance=1 gateway=208.67.222.222 target-scope=11 check-gateway=ping
add distance=2 gateway=208.67.220.220 target-scope=11 check-gateway=ping
```

此配置创建了一条 ECMP 默认路由。如果只有一个网关变得不可达，第一条链路上的默认路由仍保持活动状态。只有当所有网关主机都变得不可达时，才会完全故障转移到第二条链路。