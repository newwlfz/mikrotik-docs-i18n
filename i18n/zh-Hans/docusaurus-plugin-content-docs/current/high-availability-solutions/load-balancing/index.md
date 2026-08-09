# 负载均衡

> MikroTik RouterOS 中的网络负载均衡允许在不使用动态路由的情况下，将流量分配到多条链路上，支持基于连接或基于数据包的方法。文档包含设置示例，如故障转移配置，以及使用防火墙 mangle、bonding、OSPF 和 ECMP 的均衡技术比较。

import DocCardList from '@theme/DocCardList';

# 负载均衡

- [故障转移（WAN 备份）](./failover-wan-backup.md)
- [防火墙标记](../../firewall-and-quality-of-service/firewall/mangle.md)
- [Bonding 负载均衡](../bonding.md)
- [OSPF 负载均衡](../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md)
- [每连接分类器](./per-connection-classifier.md)

## 简介

网络负载均衡是指在两条或多条链路上分配流量的能力。

有两种均衡方法：

- 基于数据包 - 单个流中的每个数据包可以通过不同链路转发。此方法在 TCP 和安全连接上尤其可靠，但仅当您能够控制两个均衡端点时才有效。
- 基于连接 - 同一连接（流）的所有数据包始终通过一条链路发送。在只有一端均衡由我们控制的情况下（例如，具有多个 WAN 连接的家庭路由器），此方法是强制性的。

| 方法 |  | 基于连接 | 基于数据包 |
| :-- | :-- | :-- | :-- |
|  防火墙 Mangle | Nth | **是** | **是** |
|  | PCC（每连接分类器） | **是** | 否 |
|  | 其他匹配器 | **是** | **是** |
| ECMP（等价多路径） |  | **是** | **否** |
| Bonding |  | 否 | **是** |
| OSPF |  | **是** | 否 |
| BGP |  | **是** | 否 |

## 简单故障转移示例

最简单的故障转移设置是使用多个网关，其中一个网关处于活动状态，当第一个网关发生故障时，另一个网关接管。

要实现此功能，请为备用网关配置较大的 **distance** 值，并为第一个网关配置 **check-gateway**：

```ros
/ip/route/add gateway=192.168.1.1 distance=1 check-gateway=ping
/ip/route/add gateway=192.168.2.1 distance=2
```

*check-gateway* 将确保仅在实际流量能够到达网关时才认为网关处于活动状态。当 ping 失败时，第一个网关将变为非活动状态，第二个网关将接管；当第一个网关恢复后，它将重新变为活动状态，并使第二个网关重新作为备份工作。

## 相关主题

<DocCardList />