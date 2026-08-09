# Ping

> 本文档介绍了 MikroTik RouterOS 的 Ping 工具，该工具使用 ICMP Echo 消息来测试主机连通性并测量往返延迟。文中解释了 TTL、间隔、计数等参数，并支持 IPv4/IPv6 地址和 DNS 名称。此外，还简要提及了在多播发现场景下的 MAC Ping。

# Ping

[*Ping CLI 参考*](../cli-reference/tool/ping)

Ping 使用互联网控制消息协议（ICMP）的 Echo 消息来确定远程主机是否处于活动状态，并测量与其通信时的往返延迟。Ping 工具向主机发送一个 ICMP（类型 8）消息，并等待 ICMP 回显应答（类型 0）。这两个事件之间的间隔称为一个往返。如果在间隔结束前未收到响应（即 pong），则视为超时。报告的另一个重要参数是 TTL（生存时间）。TTL 在每台处理该数据包的机器上递减。只有当 TTL 大于源与目标之间的路由器数量时，数据包才能到达目的地。

### 快速示例

RouterOS Ping 工具允许您配置各种附加参数，例如：

- arp-ping
- address
- src-address
- count
- dscp
- interface
- interval
- routing-table
- size
- ttl

让我们看一个非常简单的示例：

```ros
[admin@MikroTik] > /tool/ping address=10.155.126.252 count=5 interval=200ms  
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

我们也可以通过更简短的 CLI 命令实现同样的效果：

```ros
[admin@MikroTik] > /ping 10.155.126.252 count=5 interval=50ms               
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 10.155.126.252                             56  64 0ms  
    1 10.155.126.252                             56  64 0ms  
    2 10.155.126.252                             56  64 0ms  
    3 10.155.126.252                             56  64 0ms  
    4 10.155.126.252                             56  64 0ms  
    sent=5 received=5 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms
```

还可以通过 Ping 多播地址来发现属于某个多播组的所有主机：

```ros
[admin@MikroTik] > /ping ff02::1
HOST                                    SIZE  TTL TIME  STATUS                                         
fe80::20c:42ff:fe49:fceb                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe72:a1b0                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe28:7945                56    64  1ms   echo reply                                     
fe80::21a:4dff:fe5d:8e56                56    64  3ms   echo reply                                     
    sent=1 received=4 packet-loss=-300% min-rtt=1ms avg-rtt=1ms max-rtt=3ms 
```

通过 DNS 名称进行 Ping：

```ros
[admin@MikroTik]  > /ping www.google.com count=5 interval=50ms
  SEQ HOST                                     SIZE TTL TIME  STATUS                                                                                                                                                                              
    0 216.58.207.228                             56  51 14ms 
    1 216.58.207.228                             56  51 13ms 
    2 216.58.207.228                             56  51 13ms 
    3 216.58.207.228                             56  51 13ms 
    4 216.58.207.228                             56  51 13ms 
    sent=5 received=5 packet-loss=0% min-rtt=13ms avg-rtt=13ms max-rtt=14ms
```

:::info
当您使用域名和 CLI 进行 Ping 时，路由器将使用其 [DNS](../network-management/dns) 来解析地址。当您使用 [WinBox](../management-tools/winbox) 的 Tools/Ping 时，将使用您计算机的 DNS 来解析给定地址。
:::

### MAC Ping

此子菜单允许启用 [MAC Ping 服务器](../management-tools/mac-server)。

当 MAC ping 启用时，同一广播域内的其他主机可以使用 Ping 工具来 Ping 一个 MAC 地址：

```ros
[admin@MikroTik]  > /tool/mac-server/ping/set enabled=yes 
```

Ping MAC 地址：

```ros
[admin@MikroTik]  > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

:::info
默认情况下，MAC ping 会尝试通过所有活动接口到达目的地。如果目的地可通过多个接口访问，这可能会产生不必要的流量和重复的应答。要将 MAC ping 限制到特定接口，请使用接口选择器（在 MAC 地址后附加 `%` 和接口名称）。例如：`/ping 00:11:22:33:44:55%ether1`
:::