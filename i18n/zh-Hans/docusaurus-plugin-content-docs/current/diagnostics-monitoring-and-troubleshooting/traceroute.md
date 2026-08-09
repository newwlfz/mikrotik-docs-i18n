# Traceroute

> Traceroute 通过分析 TTL 值和 ICMP “Time Exceeded” 消息，显示数据包到达远程主机所经过的路径，帮助识别多跳网络中的路由问题或瓶颈。

# Traceroute

**子菜单:** `/tool/traceroute`

**Traceroute** 显示数据包到达远程主机所经过的路由器列表。**traceroute** 或 **tracepath** 工具几乎在所有类 Unix 操作系统上可用，而 **tracert** 则用于微软 Windows 操作系统。

Traceroute 的工作原理基于 TTL 值和 ICMP “Time Exceeded” 消息。请记住，IP 头部中的 TTL 值用于避免路由环路。每一跳会将 TTL 值减 1。如果 TTL 值达到零，数据包将被丢弃，并向发送方发送 ICMP Time Exceeded 消息。

初始时，traceroute 将 TTL 值设置为 1。当下一个路由器发现 TTL = 1 的数据包时，它会将 TTL 值设置为零，并向源地址回复 ICMP “time exceeded” 消息。此消息让源地址知道数据包经过该特定路由器作为一跳。接下来 TTL 值递增 1，依此类推。通常，通往目的地的路径上的每个路由器都会将 TTL 字段减 1，直到 TTL 达到零。

使用此命令，您可以查看数据包如何通过网络传输，以及可能在何处失败或变慢。利用这些信息，您可以确定可能导致网络问题或故障的计算机、路由器、交换机或其他网络设备。

## 快速示例

通过追踪到远程目的地的路由，您可以确定连接问题是否存在于本地网络、ISP 网关或更上游的位置。

```ros
[admin@MikroTik] > tool traceroute 10.255.255.1
     ADDRESS                                    STATUS
   1       10.0.1.17 2ms 1ms 1ms 
   2    10.255.255.1 5ms 1ms 1ms
```

在此场景中，输出确认了通过本地网关 `10.0.1.17` 成功到达目标主机 `10.255.255.1` 的路径。该工具在排查多跳 VPN 隧道或复杂路由表（流量可能通过意外出口接口传输）时尤为有用。监控每一跳的毫秒级响应时间有助于精确定位网络基础设施中的特定瓶颈或抖动。