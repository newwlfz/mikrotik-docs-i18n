# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/settings

**类型：** 设置目录

此菜单允许您配置各种与 IPv4 和 IPv6 相关的内核及系统级网络参数。这些设置控制操作系统如何处理 IP 流量和网络通信。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ip-forward" typ="bool">启用或禁用接口间的数据包转发。根据 [RFC 1812](https://tools.ietf.org/html/rfc1812) 将路由器的所有配置参数重置为默认值。</ArgTableRow>
<ArgTableRow arg="send-redirects" typ="bool">发送 ICMP 重定向。在路由器上启用此选项。</ArgTableRow>
<ArgTableRow arg="accept-source-route" typ="bool">接受带有 SRR 选项的数据包。接受源路由（SSRR/LSRR）数据包是众所周知的安全风险，除非网络设置需要，否则应保持禁用。</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">接受 ICMP 重定向消息。在主机上启用，在路由器上禁用。</ArgTableRow>
<ArgTableRow arg="secure-redirects" typ="bool">仅接受来自默认网关列表中列出的网关的 ICMP 重定向消息。</ArgTableRow>
<ArgTableRow arg="rp-filter" typ="enum (no | strict | loose)">
启用或禁用源地址验证。
- `no` - 不验证源地址。
- `strict` - 严格模式，如 [RFC 3704](https://tools.ietf.org/html/rfc3704) 严格反向路径所定义。每个传入的数据包都会根据 FIB 进行测试，如果接口不是最佳反向路径，则数据包检查将失败。默认情况下，失败的数据包将被丢弃。
- `loose` - 松散模式，如 [RFC 3704](https://tools.ietf.org/html/rfc3704) 松散反向路径所定义。每个传入数据包的源地址都会根据 FIB 进行测试，如果源地址无法通过任何接口到达，则数据包检查将失败。

[RFC 3704](https://tools.ietf.org/html/rfc3704) 建议启用 `strict` 模式以防止来自 DDoS 攻击的 IP 欺骗。

如果您使用非对称路由、复杂路由或 VRRP，则 `strict` 模式会引起问题，请改用 `loose` 模式。
</ArgTableRow>
<ArgTableRow arg="ipv4-multipath-hash-policy" typ="enum (l3 | l4 | l3-inner)">
用于 [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) 路由的 IPv4 哈希策略。

- l3 - 对源和目标 IP 地址进行第 3 层哈希。
- l3-inner - 第 3 层哈希，或内部第 3 层哈希（如果可用）。
- l4 - 对源和目标 IP 地址、IP 协议、源端口和目标端口进行第 4 层哈希。
</ArgTableRow>

<ArgTableRow arg="tcp-syncookies" typ="bool">当套接字的 SYN 积压队列溢出时发送 syncookies。这有助于防止 SYN 洪水攻击。但是，syncookies 违反了 TCP 协议，并阻止使用 TCP 扩展，这可能会降低某些服务（例如 SMTP 中继）的性能。这种性能下降可能会对与您联系的客户端和中继可见。</ArgTableRow>
<ArgTableRow arg="tcp-timestamps" typ="enum (disabled | random-offset | enabled)">启用或禁用 TCP 时间戳，或为 TCP 时间戳添加随机偏移（默认行为）。禁用时间戳有助于减少性能下降峰值。</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
设置 Linux `gc_thresh3`。ARP 表中允许的最大邻居数。默认值取决于已安装的 RAM 大小。可以设置高于默认值的值，但这会增加内存不足的风险。
特定 RAM 大小的默认值：

- 64 MiB 为 2048，
- 128 MiB 为 4096，
- 256 MiB 为 8192，
- 512 MiB 或更高为 16384。

ARP 缓存存储 ARP 条目，如果其中一些条目不完整，它们可能会在缓存中停留无限期的时间。只有当缓存中的条目数小于允许的最大数量的四分之一时，才会发生这种情况。这样做的原因是为了防止在 ARP 表未接近满时不必要的垃圾回收运行。
</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="time">在所有使用 ARP 的接口上设置 Linux `base_reachable_time`（`base_reachable_time_ms`）。ARP 条目的初始有效性是在找到邻居后从区间 [`timeout/2 - 3*timeout/2`]（默认为 15 秒到 45 秒）中选取的。可以使用后缀 ms、s、m、h、d 分别表示毫秒、秒、分钟、小时或天。如果未设置后缀，则使用秒（s）。该参数表示如果在此时间内没有与特定 MAC/IP 通信，有效的 ARP 记录将被视为完整的时间。该参数并不表示 ARP 条目从 ARP 缓存中删除的时间（请参阅 `max-neighbor-entries` 设置）。</ArgTableRow>
<ArgTableRow arg="icmp-rate-limit" typ="num">限制向特定目标发送类型与 icmp-rate-mask 匹配的 ICMP 数据包的最大速率。值为 `0` 表示不进行任何限制，其他值表示响应之间的最小间隔（以毫秒为单位）。</ArgTableRow>
<ArgTableRow arg="icmp-rate-mask" typ="num">限制速率的 ICMP 类型掩码。有关更多信息，请参阅 [Linux 手册页](http://man7.org/linux/man-pages/man7/icmp.7.html)。</ArgTableRow>
<ArgTableRow arg="icmp-errors-use-inbound-interface-address" typ="bool">启用后，发送 ICMP 错误消息回复时，源地址将等于导致错误的接收接口的主地址。用于复杂的网络调试。</ArgTableRow>
<ArgTableRow arg="ipv4-high-fragment-thresh" typ="num">
设置内核可能为所有分片重组队列（每个接口和每个流）消耗的内存上限（以字节为单位）。当缓存使用的总内存达到此限制时，内核开始丢弃新到达的分片，导致数据包被丢弃。提高限制可以减少在严重分片情况下（例如高吞吐量链路与 VPN，或 MTU 受限路径）的丢弃概率，但也会提高可使用的最大 RAM 量。

默认值取决于已安装的 RAM 大小：

- 64 MiB RAM 为 512 KiB，
- 128 MiB RAM 为 1024 KiB，
- 256 MiB RAM 为 2048 KiB，
- 512 MiB RAM 为 4096 KiB，
- 1 GiB RAM 为 16 MiB，
- 2 GiB RAM 或更高为 32 MiB。
</ArgTableRow>

<ArgTableRow arg="ipv4-fragment-time" typ="num">IPv4 分片在内存中保留的时间（以秒为单位）。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">允许 [快速路径](../../firewall-and-quality-of-service/packet-flow-in-routeros#fast-path)</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ipv4-fast-path-active" typ="bool">指示快速路径是否处于活动状态。</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-packets" typ="num">经过快速路径的数据包数量。</ArgTableRow>
<ArgTableRow arg="ipv4-fast-path-bytes" typ="num">经过快速路径的字节数。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-active" typ="bool">指示 fasttrack 是否处于活动状态。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-packets" typ="num">经过 fasttrack 的数据包数量。</ArgTableRow>
<ArgTableRow arg="ipv4-fasttrack-bytes" typ="num">经过 fasttrack 的字节数。</ArgTableRow>
</ArgTable>