# Raw

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/raw

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定规则将被添加到哪个链。如果输入与已定义链的名称不匹配，则将创建一个新链。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | drop | notrack)">
数据包匹配规则时要执行的操作：
- `accept` - 接受数据包。数据包不会传递到下一条防火墙规则。
- `add-dst-to-address-list` - 将目标地址添加到由 `address-list` 参数指定的地址列表中。
- `add-src-to-address-list` - 将源地址添加到由 `address-list` 参数指定的地址列表中。
- `jump` - 跳转到由 `jump-target` 参数值指定的用户自定义链。
- `log` - 向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC、协议、源IP:端口-&gt;目标IP:端口以及数据包长度。数据包匹配后，会传递到列表中的下一条规则，类似于 `passthrough`。
- `passthrough` - 如果数据包匹配规则，则增加计数器并转到下一条规则（用于统计）。
- `return` - 将控制权返回到发起跳转的链。
- `drop` - 丢弃数据包。
- `notrack` - 不将数据包发送到连接跟踪。当您仍需要使用常规防火墙但不需要连接跟踪时非常有用。
</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳转到的目标链的名称。仅当 `action=jump` 时适用。</ArgTableRow>
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
- `ece` - ECN-Echo标志（显式拥塞通知）。
- `fin` - 关闭连接。
- `psh` - 推送功能。
- `rst` - 重置连接。
- `syn` - 新连接。
- `urg` - 紧急数据。
</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }">基于TLS SNI主机名匹配HTTPS流量。接受GLOB语法进行通配符匹配。如果TLS握手帧被分段为多个TCP段，则此匹配器将无法匹配主机名。</ArgTableRow>
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
 }">源端口及源端口范围的列表。仅当协议为TCP或UDP时适用。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">目标端口号或端口号范围的列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">如果任意（源或目标）端口匹配指定的端口或端口范围列表，则匹配。仅当 `protocol` 为TCP或UDP时适用。</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, num [0 .. 255]
, [ :range [ .. 255]]
 }">匹配ICMP类型:代码字段。</ArgTableRow>
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
匹配达到有限速率（数据包速率或比特速率）的数据包。带有此匹配器的规则将匹配直到达到此限制。参数按以下格式编写：`rate[/time],burst:mode`。
- `rate` - 每个时间间隔内要匹配的数据包或比特数。
- `time` - 指定不能超过数据包或比特速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 初始匹配的数据包或比特数：此数字每10毫秒重新充电一次，因此burst至少应为每秒速率的1/100。
- `mode` - 数据包或比特模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { num
, [ /time]
, ,num
, ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [ /time]
 }">
匹配数据包直到超过给定速率。速率定义为每个时间间隔的数据包数。与 `limit` 匹配器不同，每个流都有自己的限制。流由模式参数定义。参数按以下格式编写：`rate[/time],burst,mode[/expire]`。
- `rate` - 每个流每个时间间隔要匹配的数据包数。
- `time` - 指定每个流不能超过数据包计数速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 每个流初始匹配的数据包数：此数字在每次时间/速率时重新充电一个，直到达到此数字。
- `mode` - 指定哪些唯一字段定义流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定没有数据包的流允许被删除的间隔（可选）。
</ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, time [0 .. 86400]
, -time [0 .. 86400]
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }">基于数据包的到达时间和日期，或对于本地生成的数据包，基于离开时间和日期创建过滤器。匹配器会考虑路由器上配置的时间和时区。</ArgTableRow>
<ArgTableRow arg="random" typ="super { num [1 .. 99]
 }">以给定概率随机匹配数据包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, num [1 .. ]
, [ ,num [1 .. ]]
 }">匹配每第n个数据包：`nth=2,1` 将匹配每2个数据包中的第一个，因此，匹配规则的所有流量中的50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }">匹配IP数据包的TCP MSS值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, :num [1 .. ]
, /num [0 .. ]
 }">PCC匹配器允许将流量划分为相等的流，并能够将具有特定选项集的数据包保留在特定的流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, num [ .. 65535]
, -num [ .. 65535]
 }">匹配指定大小或大小范围（以字节为单位）的数据包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC、协议、源IP:端口-&gt;目标IP:端口以及数据包长度。即使操作不是 `log`，也允许记录数据包，这对于调试防火墙非常有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每条日志消息的开头添加指定的文本。适用于配置了 `action=log` 或 `log=yes` 的情况。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { enum (in | out) { in:0, out:1 }
, ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配IPsec使用的策略。值按以下格式编写：`direction, policy`。
- `in` - 在PREROUTING、INPUT和FORWARD链中有效。
- `out` - 在POSTROUTING、OUTPUT和FORWARD链中有效。
- `ipsec` - 如果数据包受IPsec处理，则匹配。
- `none` - 匹配不受IPsec处理的数据包。
</ArgTableRow>
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
 }">匹配分片数据包。第一个（起始）分片不计入。如果启用了连接跟踪，则不会有分片，因为系统会自动重组每个数据包。仅限IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { num
, ,time
, ,num
, ,num
 }">
尝试检测TCP和UDP扫描。参数按以下格式编写：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 来自同一主机的具有不同目标端口的最新TCP/UDP数据包的总权重，被视为端口扫描序列。
- `DelayThreshold` - 来自同一主机的具有不同目标端口的数据包的延迟，被视为可能的端口扫描子序列。
- `LowPortWeight` - 具有特权目标端口（&lt;1024）的数据包的权重。
- `HighPortWeight` - 具有非特权目标端口的数据包的权重。仅限IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配IPv4头部选项。
- `any` - 匹配至少具有一个IPv4选项的数据包。
- `loose-source-routing` - 匹配具有松散源路由选项的数据包。
- `no-record-route` - 匹配没有记录路由选项的数据包。
- `no-router-alert` - 匹配没有路由器警报选项的数据包。
- `no-source-routing` - 匹配没有源路由选项的数据包。
- `no-timestamp` - 匹配没有时间戳选项的数据包。
- `record-route` - 匹配具有记录路由选项的数据包。
- `router-alert` - 匹配具有路由器警报选项的数据包。
- `strict-source-routing` - 匹配具有严格源路由选项的数据包。
- `timestamp` - 匹配具有时间戳的数据包。仅限IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, ubit (unicast, local, broadcast, multicast, blackhole) { unicast, local, broadcast, multicast, blackhole }
 }">
匹配源地址类型：
- `unicast` - 用于点对点传输的IP地址。
- `local` - 地址分配给路由器的某个接口。
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
- `to-client` - 匹配发送到HotSpot客户端的数据包。仅限IPv4。
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表的名称。适用于操作为 `add-dst-to-address-list` 或 `add-src-to-address-list` 的情况。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, time [ .. 21474836]
,  }">
地址将从由 `address-list` 参数指定的地址列表中移除的时间间隔。与 `add-dst-to-address-list` 或 `add-src-to-address-list` 操作结合使用。
- `none-dynamic` (`00:00:00`) 将地址保留在地址列表中直到重启。
- `none-static` 将地址永久保留在地址列表中，并将包含在配置导出/备份中。
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, :num [0 .. 255]
 }">匹配数据包的TTL值。仅限IPv4。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bytes" typ="num">规则匹配的字节总数。</ArgTableRow>
<ArgTableRow arg="packets" typ="num">规则匹配的数据包总数。</ArgTableRow>
</ArgTable>

#### ip/firewall/raw/reset-counters

**类型：** 命令

#### ip/firewall/raw/reset-counters-all

**类型：** 命令