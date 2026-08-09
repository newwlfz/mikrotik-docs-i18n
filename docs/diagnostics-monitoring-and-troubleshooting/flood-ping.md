# Flood Ping

> The Flood Ping tool in RouterOS sends continuous ICMP echo requests to test network stability, measure packet loss, and analyze latency under heavy traffic conditions with real-time statistics on sent/received packets and round-trip times.

# Flood Ping

The Flood Ping tool is a diagnostic utility in RouterOS designed to send a continuous stream of ICMP echo requests to a target host at the maximum possible rate. It is primarily used to stress-test network stability and measure packet loss or latency under heavy traffic conditions.

## Quick Example

To perform a basic load test or verify link stability, you can execute a flood-ping to generate high-frequency ICMP traffic towards a target. The tool provides real-time statistics on packet loss and round-trip time (RTT) to help identify potential network bottlenecks. Use the `count` parameter to limit the duration of the test or omit it to run the utility indefinitely until manually stopped.

Execute a high-volume ping test to an IPv4 destination:

```ros
/tool/flood-ping address=10.155.114.1 count=1000
```

Execute a flood-ping to an IPv6 destination to verify dual-stack performance:

```ros
/tool/flood-ping address=2001:0db8::2 count=500
```

Example Output:

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
