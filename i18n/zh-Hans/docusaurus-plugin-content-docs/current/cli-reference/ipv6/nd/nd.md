# Nd

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/nd

**软件包:** ipv6
**类型:** 目录

IPv6 邻居发现（ND）协议在此配置。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum { all:0 }">
运行邻居发现的接口。
- all - 在所有运行中的接口上运行 ND。
</ArgTableRow>
<ArgTableRow arg="ra-interval" typ="super { time [3 .. 1250]
, -time [4 .. 1800]
 }">接口发送非请求组播路由器通告所允许的最小和最大间隔时间。</ArgTableRow>
<ArgTableRow arg="ra-delay" typ="time">接口发送组播路由器通告之间的最小时间。</ArgTableRow>
<ArgTableRow arg="mtu" typ="alt { enum (unspecified) { unspecified:0 }
, num
 }">
路由器通告中的 MTU 选项确保当链路 MTU 不明确时，链路上所有节点使用相同的 MTU 值。
- **unspecified** - 不发送 MTU 选项。
</ArgTableRow>
<ArgTableRow arg="reachable-time" typ="alt { enum (unspecified) { unspecified:0 }
, time [ .. 3600]
 }">RouterOS 在收到可达性确认后假定邻居可达的时间。用于邻居不可达检测（参见 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 7.3 节）。</ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="alt { enum (unspecified) { unspecified:0 }
, time
 }">重传邻居请求消息之间的时间。用于地址解析和邻居不可达检测（参见 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 7.2 和 7.3 节）。</ArgTableRow>
<ArgTableRow arg="ra-lifetime" typ="alt { enum (none) { none:0 }
, time [ .. 9000]
 }">设置 RA 生命周期。生命周期为 0 表示该路由器不是默认路由器。参见 [RFC 4861](https://tools.ietf.org/html/rfc4861) 第 6.2.1 节。</ArgTableRow>
<ArgTableRow arg="ra-preference" typ="enum (low | medium | high)">指定在路由器通告中传达给 IPv6 主机的路由器优先级。`ra-preference` 值帮助主机选择默认路由器以到达远程目的地。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="alt { enum (unspecified) { unspecified:0 }
, num [ .. 255]
 }">放置在出站单播数据包 IPv6 头部跳数字段中的默认值。</ArgTableRow>
<ArgTableRow arg="advertise-mac-address" typ="bool">设置后，在路由器通告中包含出站接口的链路层地址。</ArgTableRow>
<ArgTableRow arg="advertise-dns" typ="enum (no | yes | self)">
使用 RADVD 重新分发 DNS 服务器信息。

- `no` - 不通告 DNS 服务器。
- `yes` - 通告路由器上安装的 DNS 服务器。
- `self` - 通告接口链路本地地址作为 DNS 服务提供者。
</ArgTableRow>

<ArgTableRow arg="managed-address-configuration" typ="bool">指示主机是否应使用有状态自动配置（DHCPv6）获取地址。参见 [RFC 3315](https://tools.ietf.org/html/rfc3315)。</ArgTableRow>
<ArgTableRow arg="other-configuration" typ="bool">指示主机是否应使用有状态自动配置获取除地址外的其他信息。参见 [RFC 3315](https://tools.ietf.org/html/rfc3315)。</ArgTableRow>
<ArgTableRow arg="dns" typ="multi { address (flags=6)
 }">指定一个或多个 IPv6 地址，主机将接收这些地址用于 DNS 服务器配置。</ArgTableRow>
<ArgTableRow arg="pref64" typ="object { ip6Prefix
 }">指定一个或多个位于 /32、/40、/48、/56、/64 或 /96 子网内的 IPv6 前缀，主机将接收这些前缀作为 NAT64 前缀。</ArgTableRow>
</ArgTable>