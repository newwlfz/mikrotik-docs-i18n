# Netwatch

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/netwatch

**软件包：** advanced-tools
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">Netwatch 探测器的名称。</ArgTableRow>
<ArgTableRow arg="host" typ="address (flags=46viD)" mandatory="1">待探测服务器的 IP 地址或域名。参见 [地址标志](../../cli-reference/#address-flags)</ArgTableRow>
<ArgTableRow arg="type" typ="enum (simple | icmp | tcp-conn | http-get | https-get | dns)">
探测器类型（默认值：**"simple"**）：
- simple - 简化的 ICMP 探测，选项比 "ICMP" 类型少，用于与旧版 Netwatch 向后兼容
- icmp - （ping 风格）一系列带统计信息的 ICMP 请求-响应
- tcp-conn - 测试到指定 IP 和端口服务器的 TCP 连接（三次握手）
- http-get - 执行 HTTP Get 请求并测试一系列正确的响应
- https-get - 执行 HTTPS Get 请求并测试一系列正确的响应
- dns - 对域名执行指定的 DNS 查询
</ArgTableRow>
<ArgTableRow arg="src-address" typ="address (flags=46)" unset="1">Netwatch 尝试用于到达主机的源 IP 地址。如果该地址未在路由器上配置或已丢失，则主机将被视为 "down"。参见 [地址标志](../../cli-reference/#address-flags)</ArgTableRow>
<ArgTableRow arg="interval" typ="time" unset="1">探测测试之间的时间间隔。（默认值：**10s**）</ArgTableRow>
<ArgTableRow arg="timeout" typ="time" unset="1">等待响应的最大时间限制。（默认值：**3s**）</ArgTableRow>
<ArgTableRow arg="start-delay" typ="time" unset="1">开始探测前等待的时间。（默认值：**3s**）（在添加、启用或系统启动时，当 "startup-delay" 值小于 "start-delay" 值时）</ArgTableRow>
<ArgTableRow arg="startup-delay" typ="time" unset="1">系统启动后等待直到启动 Netwatch 探测的时间。（默认值：**5m**）</ArgTableRow>
<ArgTableRow arg="ignore-initial-up" typ="bool" unset="1">指定当探测状态从 Unknown 变为 "Up" 时是否应运行 "Up" 脚本，用于帮助防止在启用探测或重启后出现误报。"no" 表示从 "Unknown" 到 "Up" 的变化不会被忽略。（默认值：**no**）</ArgTableRow>
<ArgTableRow arg="ignore-initial-down" typ="bool" unset="1">指定当探测状态从 Unknown 变为 "Down" 时是否应运行 "Down" 脚本。"no" 表示从 "Unknown" 到 "Down" 的变化不会被忽略。（默认值：**no**） **警告**：应谨慎使用，因为首次 "Down" 状态不会执行，Down 脚本只会在探测从 "Up" 变为 "Down" 状态时运行。</ArgTableRow>
<ArgTableRow arg="up-script" typ="alt { , string
 }" unset="1">在探测状态从 "Down" 变为 "Up" 时执行的脚本。</ArgTableRow>
<ArgTableRow arg="down-script" typ="alt { , string
 }" unset="1">在探测状态从 "Up" 变为 "Down" 时执行的脚本。</ArgTableRow>
<ArgTableRow arg="test-script" typ="alt { , string
 }" unset="1">在每次探测测试结束时执行的脚本。</ArgTableRow>
<ArgTableRow arg="packet-interval" typ="time" unset="1">ICMP 请求数据包发送之间的时间。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**50ms**）</ArgTableRow>
<ArgTableRow arg="packet-count" typ="num" unset="1">单次测试中发送的 ICMP 数据包总数。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**10**）</ArgTableRow>
<ArgTableRow arg="packet-size" typ="num" unset="1">IP ICMP 数据包的总大小。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**50**）</ArgTableRow>
<ArgTableRow arg="ttl" typ="num" unset="1">手动设置 ICMP 数据包的生存时间值。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**255**）</ArgTableRow>
<ArgTableRow arg="accept-icmp-time-exceeded" typ="bool" unset="1">ICMP "time exceeded" 消息是否应被视为有效响应。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**no**）</ArgTableRow>
<ArgTableRow arg="early-success-detection" typ="bool" unset="1">如果已知主机将被视为 "Up"，Netwatch 将不会等待所有数据包处理完毕再更改探测状态。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**no**）</ArgTableRow>
<ArgTableRow arg="early-failure-detection" typ="bool" unset="1">如果已知主机将被视为 "Down"，Netwatch 将不会等待所有数据包处理完毕再更改探测状态。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**no**）</ArgTableRow>
<ArgTableRow arg="thr-max" typ="time" unset="1">rtt-max 的失败阈值。（高于 thr-max 的值视为探测失败）此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-avg" typ="time" unset="1">rtt-avg 的失败阈值。（平均往返时间）此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**100ms**）</ArgTableRow>
<ArgTableRow arg="thr-stdev" typ="time" unset="1">rtt-stdev 的失败阈值。（往返时间的标准差）此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**250ms**）</ArgTableRow>
<ArgTableRow arg="thr-jitter" typ="time" unset="1">rtt-jitter 的失败阈值。（往返时间的抖动（= 最大值 - 最小值））此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-loss-percent" typ="num" unset="1">loss-percent 的失败阈值。（丢失数据包的百分比）此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**85%**）</ArgTableRow>
<ArgTableRow arg="thr-loss-count" typ="num" unset="1">loss-count 的失败阈值。（丢失数据包的数量）此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。（默认值：**4294967295（最大值）**）</ArgTableRow>
<ArgTableRow arg="port" typ="num" unset="1">TCP 端口。此参数特定于 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) 和 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) 探测类型。（默认值：**80**（TCP-conn、HTTP-GET）和 **443**（HTTPS-GET））</ArgTableRow>
<ArgTableRow arg="thr-tcp-conn-time" typ="time" unset="1">tcp-connect-time 的失败阈值，配置使用微秒，如果未指定时间单位（s/m/h），日志和状态页面以毫秒显示相同值。此参数特定于 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) 探测类型。（默认值：**1s**）</ArgTableRow>
<ArgTableRow arg="thr-http-time" typ="time" unset="1">http-resp-time 的失败阈值。此参数特定于 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) 探测类型。（默认值：**10s**）</ArgTableRow>
<ArgTableRow arg="http-codes" typ="multi { , , range [100 .. 599]
 }" unset="1">被视为探测 "Up" 状态的 HTTP 响应状态码范围。参见 [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 或 [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。此参数特定于 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) 探测类型。（默认值：**100-299**）</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)" unset="1">本地存储中应用于主机验证的证书。此参数特定于 [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#https-get-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool" unset="1">启用来自本地证书存储的信任链验证。此参数特定于 [**HTTPS-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#https-get-probe) 探测类型。（默认值：**no**）</ArgTableRow>
<ArgTableRow arg="record-type" typ="enum (A | AAAA | MX | NS)" unset="1">用于 DNS 探测的记录类型。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。（默认值：**A**）</ArgTableRow>
<ArgTableRow arg="dns-server" typ="address (flags=46)" unset="1">探测应向其发送请求的 DNS 服务器；如果未指定，将使用 `/ip/dns` 中的值。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。参见 [地址标志](../../cli-reference/#address-flags)</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="enum (unknown | down | up)" unset="1">探测的当前状态。</ArgTableRow>
<ArgTableRow arg="since" typ="date">上次状态更改的时间。</ArgTableRow>
<ArgTableRow arg="done-tests" typ="num">已完成的探测测试总数。</ArgTableRow>
<ArgTableRow arg="failed-tests" typ="num">失败的探测测试总数。</ArgTableRow>
<ArgTableRow arg="sent-count" typ="num">上次探测测试期间发送的 ICMP 数据包数量。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="response-count" typ="num">上次探测测试期间收到的 ICMP 响应数据包数量。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="loss-count" typ="num">上次探测测试期间丢失的 ICMP 响应数据包数量。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="loss-percent" typ="num">上次探测测试期间丢失的 ICMP 响应数据包百分比。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="rtt-avg" typ="time">平均往返时间值。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="rtt-min" typ="time">最小往返时间。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="rtt-max" typ="time">最大往返时间。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="rtt-jitter" typ="time">往返时间的抖动（= 最大值 - 最小值）。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="rtt-stdev" typ="time">往返时间的标准差。此参数特定于 [**ICMP**](../../diagnostics-monitoring-and-troubleshooting/netwatch#icmp-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="tcp-connect-time" typ="time">建立 TCP 连接所需的时间。此参数特定于 [**TCP-conn**](../../diagnostics-monitoring-and-troubleshooting/netwatch#tcp-conn-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="http-status-code" typ="num">HTTP 响应状态码（200 OK、404 Not Found 等）。参见 [mozilla-http-status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) 或 [RFC7231](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。此参数特定于 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="http-resp-time" typ="time">HTTP/S 服务器在收到请求后发送响应所需的时间，通常以毫秒为单位。此参数特定于 [**HTTP/S-GET**](../../diagnostics-monitoring-and-troubleshooting/netwatch#http-get-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr">IPv4 IP 地址 - A 记录类型探测的结果。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="ip6" typ="ip6Addr">IPv6 IP 地址 - AAAA 记录类型探测的结果。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="name-servers" typ="multi { array-id, string
 }">名称服务器 - NS 记录类型探测的结果。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。</ArgTableRow>
<ArgTableRow arg="mail-servers" typ="multi { array-id, string
 }">邮件服务器及其优先级 - MX 记录类型探测的结果。此参数特定于 [**DNS**](../../diagnostics-monitoring-and-troubleshooting/netwatch#dns-probe) 探测类型。</ArgTableRow>
</ArgTable>