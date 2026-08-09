# Ping

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/ping

**类型：** 命令

完整文档请参阅 [Ping](../../diagnostics-monitoring-and-troubleshooting/ping)。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="address (flags=46v%Dm) {  }">目标主机的 IP 地址或 DNS 名称。参见 [地址标志](../../cli-reference/#address-flags)</ArgTableRow>
<ArgTableRow arg="interval" typ="time">ICMP 回显请求之间的时间间隔</ArgTableRow>
<ArgTableRow arg="size" typ="num">ICMP 数据负载的大小（字节）</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">ICMP 数据包的生存时间（TTL）值</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">在 IP 头中设置的 DSCP 值，用于 QoS 标记</ArgTableRow>
<ArgTableRow arg="do-not-fragment" typ="switch">在 IP 头中设置“不分片”标志</ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }">用于 ICMP 回显请求的源 IP 地址</ArgTableRow>
<ArgTableRow arg="arp-ping" typ="bool">使用 ARP 请求而非 ICMP 回显来发现主机</ArgTableRow>
<ArgTableRow arg="count" typ="num">发送的 ICMP 回显请求数量</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">发送 ping 的接口</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">用于路由 ping 请求的 VRF 表</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="seq" typ="num">ping 响应的序列号</ArgTableRow>
<ArgTableRow arg="host" typ="alt { ip6Addr
, macAddr
, ipAddr
 }">响应主机的 IP 或 MAC 地址</ArgTableRow>
<ArgTableRow arg="size" typ="num">接收到的 ICMP 数据包大小（字节）</ArgTableRow>
<ArgTableRow arg="ttl" typ="num">接收数据包中的生存时间（TTL）值</ArgTableRow>
<ArgTableRow arg="time" typ="time">ping 探测的往返时间</ArgTableRow>
<ArgTableRow arg="status" typ="string">ping 响应的状态</ArgTableRow>
<ArgTableRow arg="sent" typ="num">已发送的 ICMP 回显请求总数</ArgTableRow>
<ArgTableRow arg="received" typ="num">已接收的 ICMP 回显回复总数</ArgTableRow>
<ArgTableRow arg="packet-loss" typ="num">丢包百分比</ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time">测得的最小往返时间</ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time">测得的平均往返时间</ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time">测得的最大往返时间</ArgTableRow>
</ArgTable>