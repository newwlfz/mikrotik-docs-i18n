# 常见问题解答

> 常见问题解答。

# 常见问题解答

## 为什么 eBGP 无法连接到环回地址？

eBGP 默认只能连接一跳之内的邻居。环回地址需要额外一跳，因为它通过所连接的网络进行路由。对于多跳会话，请设置 [`multihop`](../../../../cli-reference/routing/bgp.md#multihop)`=yes`。

## BGP 网络同步具体是什么意思？

除非路由表中存在匹配的活动 IGP 或已连接路由（精确前缀匹配），否则 BGP 不会通告该网络。同步的主要原因是避免路由环路。如果 IGP 不可靠，或必须始终通告网络，则为每个要通告的网络前缀添加静态黑洞路由，或在 [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp.md#routingbgpconnection) 配置中设置 [`output.network-blackhole=yes`](../../../../cli-reference/routing/bgp.md#output.network)，以自动为每个 BGP 网络添加活动黑洞路由。

## 如何隐藏自己的 AS？

如果 [`/routing/bgp/connection`](../../../../cli-reference/routing/bgp.md#routingbgpconnection) 配置中的 [`output.default-prepend`](../../../../cli-reference/routing/bgp.md#output.default-prepend) 设置为 0，或输出 [路由过滤器](../../../../cli-reference/routing/filter.md#routingfilter) 中的 `bgp-path-prepend` 设置为 0，则对端的 AS 会从 **AS_PATH** 中移除。

## 远程对端多次预置其 AS。如何覆盖预置？

可以通过在 BGP 输入 [路由过滤器](../../../../cli-reference/routing/filter.md#routingfilter) 中设置 `bgp-path-peer-prepend 1` 来移除远程对端的预置。

## BGP 未选择 AS 路径最短的路由，或其他指标被忽略

BGP 最佳路径选择仅适用于由同一 [BGP 实例](../../../../cli-reference/routing/bgp.md#routingbgpinstance) 接收的路由。

## 从一个对端接收的 BGP 路由未通告给另一个对端

最常见的配置错误：

- 输出 [过滤器](../../../../cli-reference/routing/filter.md#routingfilter) 阻止了重分发。
- 两个对端未运行在同一个 [BGP 实例](../../../../cli-reference/routing/bgp.md#routingbgpinstance) 上。