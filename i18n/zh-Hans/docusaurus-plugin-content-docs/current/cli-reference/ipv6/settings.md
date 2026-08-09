# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/settings

**软件包：** ipv6
**类型：** 设置目录

此菜单允许您配置各种与 IPv6 相关的内核及系统级网络参数。这些设置控制操作系统如何处理 IP 流量和网络通信。

:::note
更改 IPv6 设置不会动态移除现有的 SLAAC 配置，需要重启路由器才能生效。

:::

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="disable-ipv6" typ="bool">在系统范围内禁用或启用 IPv6。禁用时，将阻止生成链路本地地址。</ArgTableRow>
<ArgTableRow arg="forward" typ="bool">启用或禁用接口之间的数据包转发。</ArgTableRow>
<ArgTableRow arg="multipath-hash-policy" typ="enum (l3 | l4 | l3-inner)">
指定用于 [ECMP](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) 路由的 IPv6 哈希策略：
- l3 - 对源 IP、目的 IP、流标签和 IP 协议进行第 3 层哈希。
- l3-inner - 第 3 层哈希，或如果可用则进行内部第 3 层哈希。
- l4 - 对源 IP、目的 IP、IP 协议、源端口和目的端口进行第 4 层哈希。
</ArgTableRow>
<ArgTableRow arg="accept-redirects" typ="bool">接受或拒绝 ICMP 重定向消息。在主机上启用，在路由器上禁用。</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements" typ="enum (no | yes-if-forwarding-disabled | yes)">控制对路由器通告（RA）消息的接受。启用时，路由器使用 [无状态地址配置](../../system-information-and-utilities/neighbor-discovery.md#statelessaddressautoconfiguration) 获取地址。</ArgTableRow>
<ArgTableRow arg="accept-router-advertisements-on" typ="enum">指定监听传入路由器通告（RA）的接口。</ArgTableRow>
<ArgTableRow arg="disable-link-local-address" typ="bool">禁用非 VPN 接口的自动链路本地地址生成。当您需要手动配置链路本地地址时使用此选项。</ArgTableRow>
<ArgTableRow arg="stale-neighbor-detect-interval" typ="num">设置系统检查过期 IPv6 邻居条目并探测其以验证可达性的间隔时间。</ArgTableRow>
<ArgTableRow arg="stale-neighbor-timeout" typ="num">过期 IPv6 邻居条目被清除的超时时间。</ArgTableRow>
<ArgTableRow arg="min-neighbor-entries" typ="num">设置设备必须为其分配内存的 IPv6 邻居条目的最小数量。</ArgTableRow>
<ArgTableRow arg="soft-max-neighbor-entries" typ="num">设置系统应处理的 IPv6 邻居条目的预期最大数量。</ArgTableRow>
<ArgTableRow arg="max-neighbor-entries" typ="num">
设置 IPv6 邻居条目的最大数量。自 RouterOS 7.1 版本起，默认值取决于已安装的内存大小：
- 64 MiB 时为 1024
- 128 MiB 时为 2048
- 256 MiB 时为 4096
- 512 MiB 时为 8192
- 1024 MiB 或更高时为 16384

设置高于默认值的数值会增加内存不足的风险。
</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">为 IPv6 流量启用 [快速路径](../../firewall-and-quality-of-service/packet-flow-in-routeros#fast-path)。</ArgTableRow>
</ArgTable>
Fasttrack 和 fastpath 的值是自该功能上次启用或系统重启以来的累计值。

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ipv6-fast-path-active" typ="bool">指示 IPv6 快速路径功能当前是否处于活动状态。</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-packets" typ="num">已通过 IPv6 快速路径处理的数据包总数。</ArgTableRow>
<ArgTableRow arg="ipv6-fast-path-bytes" typ="num">已通过 IPv6 快速路径处理的字节总数。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-active" typ="bool">指示 IPv6 fasttrack 功能当前是否处于活动状态。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-packets" typ="num">已通过 IPv6 fasttrack 处理的数据包总数。</ArgTableRow>
<ArgTableRow arg="ipv6-fasttrack-bytes" typ="num">已通过 IPv6 fasttrack 处理的字节总数。</ArgTableRow>
</ArgTable>