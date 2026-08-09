# RIP

> MikroTik RouterOS 支持 RIP 版本 2，用于在自治系统内交换路由信息，并基于跳数选择最优路径。配置可在 `/routing/rip` 下进行。

# RIP

MikroTik RouterOS 实现了 RIP 版本 2（RFC 2453）。不支持版本 1（RFC 1058）。

RIP 使自治系统中的路由器能够交换路由信息。它始终使用可用的最佳路径（即跳数最少，也就是经过路由器数量最少的路径）。配置可在 [`/routing/rip`](../../../cli-reference/routing/rip.md#routingripinstance) 下进行。