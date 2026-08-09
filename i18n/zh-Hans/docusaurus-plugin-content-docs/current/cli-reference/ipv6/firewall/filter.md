# 过滤器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/firewall/filter

**软件包：** ipv6
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="enum" mandatory="1">指定规则将被添加到哪个链。如果输入的名称与已定义的链不匹配，则会创建一个新链。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | jump | return | log | passthrough | add-src-to-address-list | add-dst-to-address-list | drop | reject | fasttrack-connection)">当数据包匹配规则时采取的动作：`accept` - 接受数据包。数据包不会传递给下一条防火墙规则。`add-dst-to-address-list` - 将目标地址添加到由 `address-list` 参数指定的地址列表中。`add-src-to-address-list` - 将源地址添加到由 `address-list` 参数指定的地址列表中。`drop` - 丢弃数据包。`fasttrack-connection` - 对连接进行快速跟踪。`jump` - 跳转到由 `jump-target` 参数值指定的用户自定义链。`log` - 向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC、协议、源IP:端口->目标IP:端口，以及数据包长度。数据包匹配后传递给列表中的下一条规则，类似于 `passthrough`。`passthrough` - 如果数据包匹配规则，则增加计数器并转到下一条规则（适用于统计）。`reject` - 拒绝数据包并发送ICMP响应。`return` - 将控制权返回到执行跳转的链。</ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()">要跳转到的目标链的名称。仅当 `action=jump` 时适用。</ArgTableRow>
<ArgTableRow arg="reject-with" typ="enum (icmp-no-route | icmp-admin-prohibited | icmp-not-neighbour | icmp-address-unreachable | icmp-port-unreachable | tcp-reset | icmp-err-src-routing-header | icmp-headers-too-long)">
指定数据包被拒绝时发送回的 [ICMP错误](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml#icmpv6-parameters-codes-2)。当 `action=reject` 时适用。

- `icmp-no-route` - 发送ICMP地址无路由消息。ICMP类型1，代码0
- `icmp-admin-prohibited` - 发送ICMP地址被禁止消息。ICMP类型1，代码1
- `icmp-not-neighbour` - 发送ICMP地址非成员消息。ICMP类型1，代码2
- `icmp-address-unreachable` - 发送ICMP地址不可达消息。ICMP类型1，代码3
- `icmp-port-unreachable` - 发送ICMP端口不可达消息。ICMP类型1，代码4
- `tcp-reset` - 发送重置TCP连接的ICMP消息。ICMP类型1，代码6
- `icmp-err-src-routing-header` - 发送源路由头中ICMP错误消息。ICMP类型1，代码7
- `icmp-headers-too-long` - 发送ICMP头过长消息。ICMP类型1，代码8
</ArgTableRow>

<ArgTableRow arg="connection-nat-state" typ="super { !
, ubit (srcnat, dstnat) { srcnat, dstnat }
 }">匹配已进行源NAT、目标NAT或两者兼有的连接。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }">基于TLS SNI主机名匹配HTTPS流量。接受GLOB语法进行通配符匹配。如果TLS握手帧被分片为多个TCP段，则此匹配器将无法匹配主机名。</ArgTableRow>
<ArgTableRow arg="connection-state" typ="super { !
, ubit (invalid, established, related, new, untracked) { invalid, established, related, new, untracked }
 }">解释特定数据包的连接跟踪分析数据：`established` - 属于现有连接的数据包。`invalid` - 在连接跟踪中没有确定状态的数据包（通常是严重乱序的数据包、具有错误序列号/确认号的数据包，或路由器资源过度使用的情况）。无效数据包不参与NAT，路由时仍包含原始源IP地址。您应该在防火墙过滤器的转发链和输入链中丢弃所有 `connection-state=invalid` 的数据包。`new` - 数据包已启动新连接，或与尚未在两个方向上看到数据包的连接相关联。`related` - 与现有连接相关但不属于该连接的数据包，例如ICMP错误或开始FTP数据连接的数据包。`untracked` - 在防火墙RAW表中设置为绕过连接跟踪的数据包。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, num
, ,num [0 .. 128]
 }">在达到给定值后，按地址或地址块匹配连接。您应该将此与 `connection-state=new` 和/或 `tcp-flags=syn` 一起使用，因为此匹配器非常消耗资源。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, enum (icmpv6) { , icmpv6:58 }
 }">按协议名称或编号匹配特定的IP协议。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ip6Prefix
 }">匹配源地址等于指定IP或属于指定IP范围的数据包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ip6Prefix
 }">匹配目标地址等于指定IP或属于指定IP范围的数据包。</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, enum
 }">将数据包的源地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, enum
 }">将数据包的目标地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表的名称。当动作是 `add-dst-to-address-list` 或 `add-src-to-address-list` 时适用。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, time [ .. 21474836]
,  }">地址将从由 `address-list` 参数指定的地址列表中移除的时间间隔。与 `add-dst-to-address-list` 或 `add-src-to-address-list` 动作配合使用。`none-dynamic` (`00:00:00`) 将地址保留在地址列表中直到重启。`none-static` 将地址永久保留在地址列表中，并将包含在配置导出/备份中。</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, ubit (unicast, local, anycast, multicast, unreachable) { unicast, local, anycast, multicast, unreachable }
 }">匹配源地址类型：`unicast` - 用于点对点传输的IP地址。`local` - 地址分配给路由器的某个接口。`anycast` - 发送到组中最近节点的数据包。`multicast` - 数据包被转发到定义的一组设备。`unreachable` - 地址不可达。</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, ubit (unicast, local, anycast, multicast, unreachable) { unicast, local, anycast, multicast, unreachable }
 }">匹配目标地址类型：`unicast` - 用于点对点传输的IP地址。`local` - 目标地址分配给路由器的某个接口。`anycast` - 发送到组中最近节点的数据包。`multicast` - 数据包被转发到定义的一组设备。`unreachable` - 地址不可达。</ArgTableRow>
<ArgTableRow arg="headers" typ="super { !
, ubit (hop, dst, route, frag, ah, esp, none, proto) { hop, dst, route, frag, ah, esp, none, proto }
, [ :enum (exact | contains) { exact:0, contains:1 }]
 }">匹配IPv6下一个头。有两种头匹配类型，由 `mode` 参数控制：`contains` - 软匹配，匹配至少选定的头。`exact` - 匹配选定头的精确集合。</ArgTableRow>
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
 }">匹配指定的TCP标志：`ack` - 确认数据。`cwr` - 拥塞窗口已减小。`ece` - ECN-回显标志（显式拥塞通知）。`fin` - 关闭连接。`psh` - 推送功能。`rst` - 重置连接。`syn` - 新连接。`urg` - 紧急数据。</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="super { enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, :num [0 .. 255]
 }">匹配IPv6头中的跳数限制字段。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, enum
 }">匹配由mangle功能标记了特定连接标记的数据包。如果设置为 `no-mark`，规则将匹配任何未标记的连接。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">基于连接跟踪助手的信息匹配相关连接的数据包。必须在 `/ip/firewall/service-port` 下启用相应的连接助手。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { num
, -num
 }">仅当特定连接已传输给定数量的字节时匹配数据包。0表示无穷大，例如 `connection-bytes=2000000-0` 表示规则在相关连接已传输超过2MB时匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, num
, -num
 }">允许基于连接的当前速度捕获流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, enum () {  }
 }">匹配由mangle功能标记了特定路由标记的数据包。</ArgTableRow>
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
 }">如果入接口是桥接，数据包实际进入路由器的接口。仅在桥接设置中启用 `use-ip-firewall` 时有效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, iface_enum {  } {  }
 }">如果出接口是桥接，数据包实际离开路由器的接口。仅在桥接设置中启用 `use-ip-firewall` 时有效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。工作方式与 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, enum
 }">匹配由mangle功能标记了特定数据包标记的数据包。如果设置为 `no-mark`，规则将匹配任何未标记的数据包。</ArgTableRow>
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
 }">如果任何（源或目标）端口匹配指定的端口或端口范围列表，则匹配。仅当 `protocol` 为TCP或UDP时适用。</ArgTableRow>
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
 }">匹配设置新优先级后数据包的优先级。优先级可能来自VLAN、WMM、DSCP、MPLS EXP位，或通过使用set-priority动作设置的优先级。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, num [0 .. 63]
 }">匹配DSCP IP头字段。</ArgTableRow>
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
匹配达到有限速率（数据包速率或比特速率）的数据包。带有此匹配器的规则将一直匹配直到达到此限制。参数按以下格式书写：`rate[/time],burst:mode`。

- `rate` - 要匹配的时间间隔内的数据包或比特计数。
- `time` - 指定不能超过数据包或比特速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 要匹配的初始数据包或比特数：此数字每10毫秒重新充电一次，因此burst应至少为每秒速率的1/100。
- `mode` - 数据包或比特模式。
</ArgTableRow>

<ArgTableRow arg="dst-limit" typ="super { num
, [ /time]
, ,num
, ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [ /time]
 }">
匹配直到给定速率被超过的数据包。速率定义为每个时间间隔的数据包数。与 `limit` 匹配器不同，每个流都有自己的限制。流由模式参数定义。参数按以下格式书写：`rate[/time],burst,mode[/expire]`。

- `rate` - 要匹配的每个流每个时间间隔的数据包计数。
- `time` - 指定每个流不能超过数据包计数速率的时间间隔（可选，如果未指定则使用1秒）。
- `burst` - 要匹配的每个流的初始数据包数：此数字每次/速率增加1，直到达到此数字。
- `mode` - 指定哪些唯一字段定义流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定没有数据包的流允许被删除的间隔（可选）。
</ArgTableRow>

<ArgTableRow arg="time" typ="super { !
, time [0 .. 86400]
, -time [0 .. 86400]
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }">根据数据包的到达时间和日期，或对于本地生成的数据包，根据离开时间和日期创建过滤器。匹配器考虑路由器上配置的时间和时区。</ArgTableRow>
<ArgTableRow arg="random" typ="super { num [1 .. 99]
 }">以给定的概率随机匹配数据包。</ArgTableRow>
<ArgTableRow arg="nth" typ="super { !
, num [1 .. ]
, [ ,num [1 .. ]]
 }">匹配每第n个数据包：`nth=2,1` 将匹配每2个数据包中的第1个，因此匹配规则匹配的所有流量的50%。</ArgTableRow>
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
<ArgTableRow arg="log" typ="bool">向系统日志添加一条消息，包含以下数据：入接口、出接口、源MAC、协议、源IP:端口->目标IP:端口，以及数据包长度。即使动作不是 `log`，也允许记录数据包，这对于调试防火墙很有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每条日志消息的开头添加指定的文本。当配置了 `action=log` 或 `log=yes` 时适用。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { enum (in | out) { in:0, out:1 }
, ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配IPsec使用的策略。值按以下格式书写：`direction, policy`。

- `in` - 在PREROUTING、INPUT和FORWARD链中有效。
- `out` - 在POSTROUTING、OUTPUT和FORWARD链中有效。
- `ipsec` - 如果数据包需要经过IPsec处理，则匹配。
- `none` - 匹配不需要经过IPsec处理的数据包。
</ArgTableRow>

</ArgTable>

#### ipv6/firewall/filter/reset-counters

**类型：** 命令

#### ipv6/firewall/filter/reset-counters-all

**类型：** 命令