# Mangle（数据包标记）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/mangle

**类型：** 目录（Directory）

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定规则将被添加到哪个链。如果输入的名称与已定义的链不匹配，则会创建一个新链。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | sniff-tzsp | sniff-pc | drop | mark-packet | mark-connection | change-mss | change-dscp | strip-ipv4-options | change-ttl | mark-routing | set-priority | clear-df | fasttrack-connection | route)">
当数据包与规则匹配时要执行的操作：
- `accept` - 接受数据包。数据包不会传递给下一条防火墙规则。
- `add-dst-to-address-list` - 将目标地址添加到由 `address-list` 参数指定的地址列表中。
- `add-src-to-address-list` - 将源地址添加到由 `address-list` 参数指定的地址列表中。
- `jump` - 跳转到由 `jump-target` 参数值指定的用户自定义链。
- `log` - 向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC地址、协议、源IP:端口-&gt;目标IP:端口以及数据包长度。数据包匹配后传递给列表中的下一条规则，类似于 `passthrough`。
- `passthrough` - 如果数据包与规则匹配，则增加计数器并转到下一条规则（用于统计）。
- `sniff-tzsp` - 将数据包发送到远程支持TZSP的系统（如Wireshark）。使用 `sniff-target` 和 `sniff-target-port` 参数设置远程目标（Wireshark推荐端口37008）。数据包匹配后传递给列表中的下一条规则，类似于 `passthrough`。
- `sniff-pc` - 将数据包发送到远程RouterOS CALEA服务器。数据包匹配后传递给列表中的下一条规则，类似于 `passthrough`。
- `drop` - 静默丢弃数据包。
- `mark-packet` - 使用指定的 `new-packet-mark` 标记数据包。
- `mark-connection` - 使用指定的 `new-connection-mark` 标记连接。
- `change-mss` - 将数据包的最大分段大小（MSS）字段值更改为 `new-mss` 参数指定的值。
- `change-dscp` - 将区分服务代码点（DSCP）字段值更改为 `new-dscp` 参数指定的值。
- `change-ttl` - 将数据包的生存时间（TTL）字段值更改为 `new-ttl` 参数指定的值。
- `mark-routing` - 在数据包上放置由 `new-routing-mark` 参数指定的标记。此类标记仅用于策略路由目的。对于由FastTrack处理的数据包，请勿应用除 `main` 之外的任何其他路由标记，因为FastTrack只能在主路由表中工作。
- `set-priority` - 设置数据包的优先级。
- `clear-df` - 清除不分片（Don't Fragment）标志。
- `fasttrack-connection` - 标记连接以进行FastTrack处理。数据包匹配后传递给列表中的下一条规则，类似于 `passthrough`。
- `route` - 通过忽略正常的路由决策（仅限prerouting链），强制将数据包发送到由 `route-dst` 参数指定的网关IP。
- `strip-ipv4-options` - 从IP头部剥离IPv4选项字段。该操作实际上并不移除IPv4选项，而是将所有选项字节替换为NOP。后续使用 `ipv4-options=any` 的匹配器仍将匹配该数据包。
</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳转到的目标链的名称。仅当 `action=jump` 时适用。</ArgTableRow>
<ArgTableRow arg="new-packet-mark" typ="enum ()">设置新的数据包标记值。</ArgTableRow>
<ArgTableRow arg="new-connection-mark" typ="enum ()">设置新的连接标记值。</ArgTableRow>
<ArgTableRow arg="new-routing-mark" typ="enum ()">设置新的 `routing-mark` 值。在RouterOS v7中，路由标记必须事先作为新的 [路由表](../../../user-guides/routing-and-networking-protocols/policy-routing.md) 创建。</ArgTableRow>
<ArgTableRow arg="new-mss" typ="alt { , enum (clamp-to-pmtu) { clamp-to-pmtu:65535 }
, num [40 .. 65534]
 }">为数据包设置新的MSS。**重要提示：** Clamp-to-pmtu功能会设置IP头中的DF位，以动态发现路径的PMTU。主机在该路径上发送所有数据报时都会设置DF位，直到收到ICMP目标不可达消息（代码含义为“需要分片且已设置DF”）。收到此类消息后，源主机将降低其对该路径的假定PMTU。</ArgTableRow>
<ArgTableRow arg="new-dscp" typ="enum (from-priority-to-high-3-bits | from-priority)">设置新的DSCP值。</ArgTableRow>
<ArgTableRow arg="new-priority" typ="alt { , enum (from-dscp | from-ingress | from-dscp-high-3-bits) { from-dscp:65536, from-ingress:65537, from-dscp-high-3-bits:65538 }
, num [0 .. 63]
 }">为数据包设置新的优先级。这可以是VLAN、WMM、DSCP或MPLS EXP优先级 [了解更多](../../../bridging-and-switching/user-guides/wmm-and-vlan-priority.md)。此属性也可用于设置内部优先级。</ArgTableRow>
<ArgTableRow arg="new-ttl" typ="super { , enum (set | increment | decrement) { set:0, increment:1, decrement:2 }
, :num [0 .. 255]
 }">设置新的TTL值。</ArgTableRow>
<ArgTableRow arg="passthrough" typ="bool {  }">是否让数据包传递到下一条规则。</ArgTableRow>
<ArgTableRow arg="tcp-flags" typ="super { !,
, multi { array-id, array-id, super { !
, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 } { !
, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 } { array-id, array-id, super { !
, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 } { !
, enum (fin | syn | rst | psh | ack | urg | ece | cwr) { fin:0, syn:1, rst:2, psh:3, ack:4, urg:5, ece:6, cwr:7 }
 }
 }
 }">
匹配指定的TCP标志：
- `ack` - 确认数据。
- `cwr` - 拥塞窗口已减小。
- `ece` - ECN-echo标志（显式拥塞通知）。
- `fin` - 关闭连接。
- `psh` - 推送功能。
- `rst` - 重置连接。
- `syn` - 新连接。
- `urg` - 紧急数据。
</ArgTableRow>
<ArgTableRow arg="p2p" typ="super { !
, enum (fasttrack | gnutella | direct-connect | edonkey | bit-torrent | blubster | soulseek | winmx | warez | all-p2p) { fasttrack:0x01, gnutella:0x02, direct-connect:0x03, edonkey:0x04, bit-torrent:0x05, blubster:0x06, soulseek:0x07, winmx:0x08, warez:0x09, all-p2p:0xFF }
 }">匹配某些未加密的P2P协议。已弃用，因为现在大多数流量都已加密，需要深度数据包检测才能识别。仅支持IPv4。</ArgTableRow>
<ArgTableRow arg="connection-state" typ="super { !
, ubit (invalid, established, related, new, untracked) { invalid, established, related, new, untracked }
 }">
解释特定数据包的连接跟踪分析数据：
 - `established` - 属于现有连接的数据包。
 - `invalid` - 在连接跟踪中没有确定状态的数据包（通常是严重乱序的数据包、序列号/确认号错误的数据包，或路由器资源过度使用的情况）。无效数据包不参与NAT（因为只有connection-state=new的数据包才参与），并且在路由时仍包含原始源IP地址。您应该在防火墙过滤器的forward和input链中丢弃所有 `connection-state=invalid` 的数据包。
 - `new` - 数据包已启动新连接，或与尚未在两个方向上看到数据包的连接相关联。
 - `related` - 与现有连接相关但不属于该连接的数据包，例如ICMP错误或开始FTP数据连接的数据包。
 - `untracked` - 被设置为绕过防火墙RAW表中连接跟踪的数据包。
</ArgTableRow>
<ArgTableRow arg="connection-nat-state" typ="super { !
, ubit (srcnat, dstnat) { srcnat, dstnat }
 }">
匹配已进行源NAT、目标NAT或两者兼有的连接。`connection-state=related` 连接的connection-nat-state由第一个数据包的方向决定，如果连接跟踪需要使用dst-nat将此连接传送到与主连接相同的主机，则即使根本没有dst-nat规则，它也将处于connection-nat-state=dstnat状态。
`ein-snat` 和 `ein-dnat` 是在使用端点独立NAT（endpoint-independent NAT）时的源和目标NAT连接。
</ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr {  }">用于发送嗅探数据包的IP地址。</ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num {  }">用于发送嗅探数据包的端口。</ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num {  }">嗅探会话的ID。</ArgTableRow>
<ArgTableRow arg="route-dst" typ="ipAddr {  }">为 `route` 操作指定路由目标。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }">基于TLS SNI主机名匹配HTTPS流量。接受GLOB语法进行通配符匹配。如果TLS握手帧被分片为多个TCP段，则匹配器将无法匹配主机名。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, num
, ,num
 }">在达到给定值后，按地址或地址块匹配连接。您应该将此与 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因为该匹配器非常消耗资源。</ArgTableRow>
<ArgTableRow arg="layer7-protocol" typ="super { !
, enum
 }">在layer7协议菜单中定义的Layer7过滤器名称。</ArgTableRow>
<ArgTableRow arg="realm" typ="super { !
, num
 }">匹配路由域（routing realm）。仅支持IPv4。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, enum () {  }
 }">匹配由协议名称或编号指定的特定IP协议。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipRange
 }">匹配源地址等于指定IP或属于指定IP范围的数据包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipRange
 }">匹配目标地址等于指定IP或属于指定IP范围的数据包。</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { bool
 }">匹配分片数据包。第一个（起始）分片不计入。如果启用了连接跟踪，则不会有分片，因为系统会自动重组每个数据包。仅支持IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { num
, ,time
, ,num
, ,num
 }">
尝试检测TCP和UDP扫描。参数格式如下：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 来自同一主机的具有不同目标端口的最新TCP/UDP数据包的总权重，用于判定为端口扫描序列。
- `DelayThreshold` - 来自同一主机的具有不同目标端口的数据包的延迟，用于判定为可能的端口扫描子序列。
- `LowPortWeight` - 具有特权目标端口（&lt;1024）的数据包的权重。
- `HighPortWeight` - 具有非特权目标端口的数据包的权重。仅支持IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配IPv4头部选项。
- `any` - 匹配至少具有一个IPv4选项的数据包。
- `loose-source-routing` - 匹配具有宽松源路由选项的数据包。
- `no-record-route` - 匹配没有记录路由选项的数据包。
- `no-router-alert` - 匹配没有路由器告警选项的数据包。
- `no-source-routing` - 匹配没有源路由选项的数据包。
- `no-timestamp` - 匹配没有时间戳选项的数据包。
- `record-route` - 匹配具有记录路由选项的数据包。
- `router-alert` - 匹配具有路由器告警选项的数据包。
- `strict-source-routing` - 匹配具有严格源路由选项的数据包。
- `timestamp` - 匹配具有时间戳的数据包。仅支持IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, ubit (unicast, local, broadcast, multicast, blackhole) { unicast, local, broadcast, multicast, blackhole }
 }">
匹配源地址类型：
- `unicast` - 用于点对点传输的IP地址。
- `local` - 该地址分配给路由器的某个接口。
- `broadcast` - 数据包发送到子网中的所有设备。
- `multicast` - 数据包转发到定义的一组设备。
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, ubit (unicast, local, broadcast, multicast, blackhole) { unicast, local, broadcast, multicast, blackhole }
 }">
匹配目标地址类型：
- `unicast` - 用于点对点传输的IP地址。
- `local` - 目标地址分配给路由器的某个接口。
- `broadcast` - 数据包发送到子网中的所有设备。
- `multicast` - 数据包转发到定义的一组设备。
</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, enum
 }">将数据包的源地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, enum
 }">将数据包的目标地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="multi { array-id, array-id, super { !
, enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 } { !
, enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 }
 }">
将来自HotSpot客户端的数据包与各种HotSpot匹配器进行匹配。
- `auth` - 匹配已认证的HotSpot客户端数据包。
- `from-client` - 匹配来自HotSpot客户端的数据包。
- `http` - 匹配发送到HotSpot服务器的HTTP请求。
- `local-dst` - 匹配发往HotSpot服务器的数据包。
- `to-client` - 匹配发送到HotSpot客户端的数据包。仅支持IPv4。
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表的名称。当操作为 `add-dst-to-address-list` 或 `add-src-to-address-list` 时适用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, time [ .. 21474836]
,  }">
地址将从由 `address-list` 参数指定的地址列表中移除的时间间隔。与 `add-dst-to-address-list` 或 `add-src-to-address-list` 操作结合使用。
- `none-dynamic` (`00:00:00`) 将地址保留在地址列表中直到重启。
- `none-static` 将地址永久保留在地址列表中，并将包含在配置导出/备份中。
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, :num [0 .. 255]
 }">匹配数据包的TTL值。仅支持IPv4。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, enum
 }">匹配由mangle功能使用特定连接标记标记的数据包。如果设置为 `no-mark`，则规则将匹配任何未标记的连接。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">基于连接跟踪助手的信息匹配相关连接的数据包。必须在 `/ip/firewall/service-port` 下启用相应的连接助手。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { num
, -num
 }">仅当通过特定连接传输了给定数量的字节时才匹配数据包。0表示无穷大，例如 `connection-bytes=2000000-0` 表示如果通过相关连接传输了超过2MB的数据，则规则匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, num
, -num
 }">允许基于连接的当前速度捕获流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, enum () {  }
 }">匹配由mangle功能使用特定路由标记标记的数据包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, iface_enum {  } {  }
 }">数据包进入路由器的接口。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, iface_enum {  } {  }
 }">数据包离开路由器的接口。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, iface_enum {  } {  }
 }">如果入接口是桥接，则数据包实际进入路由器的接口。仅在桥接设置中启用了 `use-ip-firewall` 时有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, iface_enum {  } {  }
 }">如果出接口是桥接，则数据包实际离开路由器的接口。仅在桥接设置中启用了 `use-ip-firewall` 时有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, enum
 }">匹配由mangle功能使用特定数据包标记标记的数据包。如果设置为 `no-mark`，则规则将匹配任何未标记的数据包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">源端口和源端口范围的列表。仅当协议为TCP或UDP时适用。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">目标端口号或端口号范围的列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">如果任何（源或目标）端口与指定的端口或端口范围列表匹配，则匹配。仅当 `protocol` 为TCP或UDP时适用。</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, num [0 .. 255]
, [ :range [ .. 255]]
 }">匹配ICMP类型：代码字段。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, macAddr
 }">匹配数据包的源MAC地址。</ArgTableRow>
<ArgTableRow arg="content" typ="super { !
, string
 }">匹配包含指定文本的数据包。</ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, num [0 .. 63]
 }">匹配入站数据包的优先级。优先级可能来自VLAN、WMM、DSCP或MPLS EXP位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, num [0 .. 63]
 }">匹配设置新优先级后数据包的优先级。优先级可能来自VLAN、WMM、DSCP、MPLS EXP位，或通过使用set-priority操作设置的优先级。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, num [0 .. 63]
 }">匹配DSCP IP头部字段。</ArgTableRow>
<ArgTableRow arg="tos" typ="super { !
, num [0 .. 255]
, [ /num [0 .. 255]]
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { !
, num [1 .. 32000000000]
, [ /time [1 .. ]]
, ,num [ .. 2000000000]
, [ :enum (packet | bit) { packet:0, bit:1 }]
 }">
以有限速率（数据包速率或比特速率）匹配数据包。具有此匹配器的规则将匹配直到达到此限制。参数格式如下：`rate[/time],burst:mode`。
- `rate` - 每个时间间隔内要匹配的数据包或比特数。
- `time` - 指定不能超过数据包或比特速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 要匹配的初始数据包或比特数：此数字每10毫秒重新充电一次，因此burst至少应为每秒速率的1/100。
-  `mode` - 数据包或比特模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { num
, [ /time]
, ,num
, ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [ /time]
 }">
匹配数据包直到超过给定速率。速率定义为每个时间间隔的数据包数。与 `limit` 匹配器不同，每个流都有自己的限制。流由模式参数定义。参数格式如下：`rate[/time],burst,mode[/expire]`。
- `rate` - 每个时间间隔内每个流要匹配的数据包数。
- `time` - 指定每个流不能超过数据包计数速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 每个流要匹配的初始数据包数：此数字在每次时间/速率时增加1，直到达到此数字。
- `mode` - 指定哪些唯一字段定义流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定没有数据包的流将被允许删除的间隔（可选）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, time [0 .. 86400]
, -time [0 .. 86400]
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }">根据数据包的到达时间和日期，或对于本地生成的数据包，根据离开时间和日期创建过滤器。匹配器会考虑路由器上配置的时间和时区。</ArgTableRow>
<ArgTableRow arg="random" typ="super { num [1 .. 99]
 }">以给定的概率随机匹配数据包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, num [1 .. ]
, [ ,num [1 .. ]]
 }">匹配每第n个数据包：`nth=2,1` 将匹配每2个数据包中的第1个，因此，匹配规则的所有流量中的50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }">匹配IP数据包的TCP MSS值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, :num [1 .. ]
, /num [0 .. ]
 }">PCC匹配器允许将流量划分为相等的流，并能够将具有特定选项集的数据包保持在一个特定的流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, num [ .. 65535]
, -num [ .. 65535]
 }">匹配指定大小或大小范围（以字节为单位）的数据包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC地址、协议、源IP:端口-&gt;目标IP:端口以及数据包长度。即使操作不是 `log`，也允许记录数据包，这对于调试防火墙很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每条日志消息的开头添加指定的文本。当配置了 `action=log` 或 `log=yes` 时适用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { enum (in | out) { in:0, out:1 }
, ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配IPsec使用的策略。值格式如下：`direction, policy`。
- `in` - 在PREROUTING、INPUT和FORWARD链中有效。
- `out` - 在POSTROUTING、OUTPUT和FORWARD链中有效。
- `ipsec` - 如果数据包需要经过IPsec处理，则匹配。
- `none` - 匹配不需要经过IPsec处理的数据包。
</ArgTableRow>
</ArgTable>

#### ip/firewall/mangle/reset-counters

**类型：** 命令（Command）

#### ip/firewall/mangle/reset-counters-all

**类型：** 命令（Command）