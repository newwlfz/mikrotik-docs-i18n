# Flood Ping（泛洪 Ping）

> RouterOS 中的 Flood Ping 工具会持续发送 ICMP 回显请求，用于测试网络稳定性、测量丢包率，并在高流量条件下分析延迟，同时提供已发送/已接收数据包及往返时间的实时统计信息。

# Flood Ping（泛洪 Ping）

Flood Ping 工具是 RouterOS 中的一种诊断实用程序，旨在以尽可能高的速率向目标主机持续发送 ICMP 回显请求。它主要用于对网络稳定性进行压力测试，并测量高流量条件下的丢包率或延迟。

## 快速示例

要执行基本的负载测试或验证链路稳定性，您可以执行泛洪 ping 以向目标生成高频 ICMP 流量。该工具提供关于丢包率和往返时间（RTT）的实时统计信息，以帮助识别潜在的网络瓶颈。使用 `count` 参数限制测试持续时间，或省略该参数以无限期运行该工具，直到手动停止。

向 IPv4 目标执行高流量 ping 测试：

```ros
/tool/flood-ping address=10.155.114.1 count=1000
```

向 IPv6 目标执行泛洪 ping，以验证双栈性能：

```ros
/tool/flood-ping address=2001:0db8::2 count=500
```

示例输出：

```ros
[admin@MikroTik] > /tool/flood-ping address=10.155.114.1 count=1000
      sent: 1000
  received: 1000
   min-rtt:    0
   avg-rtt:    0
   max-rtt:    1

[admin@MikroTik] > /tool/flood-ping address=2001:0db8::2 count=500
      sent: 500
  received: 500
   min-rtt:   0
   avg-rtt:   0
   max-rtt:   3
```