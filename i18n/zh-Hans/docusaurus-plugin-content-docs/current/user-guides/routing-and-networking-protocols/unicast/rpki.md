# RPKI

> RouterOS 支持通过资源公钥基础设施（RPKI）进行 BGP 前缀验证，利用 RTR 协议实现安全的路由来源验证。配置包括设置 RTR 服务器，并根据 RPKI 有效性状态应用过滤器以接受或拒绝路由。

# RPKI

RouterOS 实现了 [`RFC 8210`](https://tools.ietf.org/html/rfc8210) 中定义的资源公钥基础设施（RPKI）到路由器协议（Router Protocol）。RTR 是一种轻量级、低内存占用的协议，用于从 RPKI 验证器获取前缀验证数据。参见 [RIPE 博客](https://blog.apnic.net/2019/10/28/how-to-installing-an-rpki-validator/) 上的验证器设置示例。

配置位于 [`/routing/rpki`](../../../cli-reference/routing/rpki.md#routingrpki) 下。

## 基本示例

假设您的网络中有一台 IP 地址为 `192.168.1.1` 的 RTR 服务器：

```ros
/routing/rpki
add group=myRpkiGroup address=192.168.1.1 port=8282 refresh-interval=20
```

[`group`](../../../cli-reference/routing/rpki.md#group)、[`address`](../../../cli-reference/routing/rpki.md#address)、[`port`](../../../cli-reference/routing/rpki.md#port) 和 [`refresh-interval`](../../../cli-reference/routing/rpki.md#refresh-interval) 参数用于配置 RTR 连接。其他参数包括 [`vrf`](../../../cli-reference/routing/rpki.md#vrf)、[`preference`](../../../cli-reference/routing/rpki.md#preference)、[`retry-interval`](../../../cli-reference/routing/rpki.md#retry-interval) 和 [`expire-interval`](../../../cli-reference/routing/rpki.md#expire-interval)。

连接建立并接收到验证器数据库后，使用 [`rpki-check`](../../../cli-reference/routing/rpki.md#routingrpkirpki-check) 检查前缀有效性：

```text
[admin@rack1_b33_CCR1036] /routing/rpki> rpki-check group=myRpkiGroup prfx=70.132.18.0/24 origin-as=16509
    valid
```

在[路由过滤器](../route-selection-and-filtering.md)中使用缓存的数据库，根据 RPKI 有效性状态接受或拒绝前缀。首先设置一个 [`/routing/filter/rule`](../../../cli-reference/routing/filter.md#routingfilterrule)，定义哪个 RPKI 组执行验证。之后，过滤器可以匹配 RPKI 数据库中的状态。状态可以有以下四种值之一：

- **valid** - 数据库中有记录，且来源 AS 有效。
- **invalid** - 数据库中有记录，但来源 AS 无效。
- **unknown** - 数据库中没有关于该前缀和来源 AS 的信息。
- **unverified** - 当 RPKI 组的任何会话均未同步数据库时设置。使用此值处理 RPKI 完全故障的情况。

```ros
/routing/filter/rule
add chain=bgp_in rule="rpki-verify myRpkiGroup"
add chain=bgp_in rule="if (rpki invalid) { reject } else { accept }"
```