# Ping

> The page documents the MikroTik RouterOS Ping tool, which uses ICMP Echo messages to test host connectivity and measure round-trip delays. It explains parameters like TTL, interval, count, and supports both IPv4/IPv6 addresses and DNS names. MAC Ping is also briefly mentioned in the context of multicast discovery.

# Ping

[*Ping CLI Reference*](../cli-reference/tool/ping)

Ping uses the Internet Control Message Protocol (ICMP) Echo messages to determine if a remote host is active or inactive and to determine the round-trip delay when communicating with it. The Ping tool sends an ICMP (type 8) message to the host and waits for the ICMP echo-reply (type 0). The interval between these events is called a round trip. If the response (that is called pong) has not come until the end of the interval, we assume it has timed out. The second significant parameter reported is TTL (Time to Live). It is decremented at each machine in which the packet is processed. The packet will reach its destination only when the TTL is greater than the number of routers between the source and the destination.

### Quick Example

RouterOS Ping tool allows you to configure various additional parameters like:

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

Let's take a look at a very simple example:

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

The same we can achieve with a shorter CLI command:

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

It is also possible to ping a multicast address to discover all hosts belonging to a multicast group:

```ros
[admin@MikroTik] > /ping ff02::1
HOST                                    SIZE  TTL TIME  STATUS                                         
fe80::20c:42ff:fe49:fceb                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe72:a1b0                56    64  1ms   echo reply                                     
fe80::20c:42ff:fe28:7945                56    64  1ms   echo reply                                     
fe80::21a:4dff:fe5d:8e56                56    64  3ms   echo reply                                     
    sent=1 received=4 packet-loss=-300% min-rtt=1ms avg-rtt=1ms max-rtt=3ms 
```

Ping by DNS name:

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
When you use the domain name and CLI for ping, the router [DNS](../network-management/dns) will be used to resolve the address. When you use the [WinBox](../management-tools/winbox) Tools/Ping, your computer's DNS will be used to resolve the given address.
:::

### MAC Ping

This submenu allows enabling the [MAC Ping server](../management-tools/mac-server).

When MAC ping is enabled, other hosts on the same broadcast domain can use the ping tool to ping a MAC address:

```ros
[admin@MikroTik]  > /tool/mac-server/ping/set enabled=yes 
```

Ping MAC address:

```ros
[admin@MikroTik]  > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

:::info
By default, a MAC ping attempts to reach the destination through all active interfaces. This can generate unwanted traffic and duplicate replies if the destination is reachable via multiple interfaces. To restrict a MAC ping to a specific interface, use the interface selector (append `%` followed by the interface name to the MAC address). For example: `/ping 00:11:22:33:44:55%ether1`
:::
