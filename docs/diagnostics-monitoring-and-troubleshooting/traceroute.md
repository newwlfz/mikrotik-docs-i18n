# Traceroute

> Traceroute displays the path a packet takes to reach a remote host by analyzing TTL values and ICMP 'Time Exceeded' messages, helping identify routing issues or bottlenecks in multi-hop networks.

# Traceroute

**Sub-menu:** `/tool/traceroute`

**Traceroute** displays the list of the routers that a packet travels through to get to a remote host. The **traceroute** or **tracepath** tool is available on practically all Unix-like operating systems and **tracert** on Microsoft Windows operating systems.

Traceroute operation is based on TTL value and an ICMP “Time Exceeded” message. Remember that TTL value in the IP header is used to avoid routing loops. Each hop decrements TTL value by 1. If the TTL reaches zero, the packet is discarded and an ICMP Time Exceeded message is sent back to the sender when this occurs.

Initially, by traceroute, the TTL value is set to 1 when the next router finds a packet with TTL = 1, it sets the TTL value to zero, and responds with an ICMP "time exceeded" message to the source. This message lets the source know that the packet traverses that particular router as a hop. Next time the TTL value is incremented by 1 and so on. Typically, each router in the path towards the destination decrements the TTL field by one unit until TTL reaches zero.

Using this command you can see how packets travel through the network and where it may fail or slow down. Using this information you can determine the computer, router, switch or other network device that is possibly causing network issues or failures.

## Quick Example

By tracing the route to a remote destination, you can determine if a connectivity issue resides within the local network, at the ISP gateway, or further upstream.

```ros
[admin@MikroTik] > tool traceroute 10.255.255.1
     ADDRESS                                    STATUS
   1       10.0.1.17 2ms 1ms 1ms 
   2    10.255.255.1 5ms 1ms 1ms
```

In this scenario, the output confirms a successful path to the target host `10.255.255.1` via a local gateway at `10.0.1.17`. This tool is particularly useful when troubleshooting multi-hop VPN tunnels or complex routing tables where traffic might be taking an unexpected exit interface. Monitoring the millisecond response times for each hop helps pinpoint specific bottlenecks or jitter in the network infrastructure.
