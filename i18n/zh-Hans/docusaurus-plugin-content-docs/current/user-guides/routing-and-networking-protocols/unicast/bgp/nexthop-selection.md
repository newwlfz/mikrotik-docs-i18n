# 下一跳选择

> BGP 在输入和输出时的下一跳选择流程。

# 下一跳选择

RouterOS 不对 BGP 输入执行严格的下一跳检查；相反，它依赖于用户创建的[过滤规则](../../../../cli-reference/routing/filter.md#routingfilter)。

输入时执行的操作：

- 从 BGP **NEXT_HOP** 属性中读取下一跳。
- 对于多协议 NLRI，检查下一跳是否具有有效长度：
  - 如果长度无效，发送 Update 错误通知并退出。
  - 存储下一跳值。
  - 如果更新消息中出现链路本地下一跳：
    - 确定连接接口。
    - 存储链路本地地址和接口。
- 应用输入过滤规则中的下一跳操作。
- 将路由发送到主计算进程，在该进程中确定下一跳的可达性。

## BGP 输出

- 如果 [`nexthop-choice`](../../../../cli-reference/routing/bgp.md#nexthop-choice) 不是 `force-self`，或者路由 AFI 不是 IPv4 或 IPv6：
  - 如果对等体是路由反射器，或者 [`nexthop-choice`](../../../../cli-reference/routing/bgp.md#nexthop-choice) 是 `propagate`，或者对等体不是 eBGP：
    - 检查下一跳 AFI，并尝试设置出站链路本地下一跳。
    - 检查下一跳 AFI，并尝试设置出站下一跳。
  - 如果出站下一跳仍未设置，且 BGP 对等体不是多跳：
    - 遍历可用的立即下一跳，并尝试设置出站下一跳和 LL 下一跳。
  - 如果出站下一跳等于远程 [`router-id`](../../../../cli-reference/routing/bgp.md#router-id)，则取消设置出站下一跳。
  - 如果出站下一跳等于远程对等体的地址，则取消设置出站下一跳。
  - 如果对等体地址的接口不等于 LL 下一跳的接口，则取消设置出站 LL 下一跳。
  - 如果出站 LL 下一跳等于远程对等体的地址，则取消设置出站 LL 下一跳。
- 如果出站下一跳仍未设置，检查 AFI 并设置对等体的本地地址。
- 如果出站下一跳仍未设置，且路由 AFI 是 IPv6 或 L2VPN：
  - 如果对等体的本地地址是 IPv4，则将出站下一跳设置为 IPv6 映射的对等体本地地址。