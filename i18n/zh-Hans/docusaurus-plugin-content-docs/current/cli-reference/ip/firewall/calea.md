# Calea

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/calea

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="filter" typ="alt { enum (all) { all:0 }
, bool
, enum (prerouting | input | forward | output | postrouting) { prerouting:1, input:2, forward:3, output:4, postrouting:5 }
 }">Calea 规则的过滤配置。</ArgTableRow>
<ArgTableRow arg="chain" typ="enum (prerouting | input | forward | output | postrouting)" mandatory="1">指定规则将被添加到的链。如果输入的名称与已定义链不匹配，则将创建一个新链。</ArgTableRow>
<ArgTableRow arg="action" typ="enum (sniff | sniff-pc)">
当数据包匹配规则时采取的动作：
- `sniff` - 嗅探数据包。
- `sniff-pc` - 嗅探数据包并将其发送到指定的数据包捕获目标。
</ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr {  }">发送嗅探数据包的目标 IP 地址。</ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num {  }">发送嗅探数据包的目标端口。</ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num {  }">嗅探会话的 ID。</ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }">基于 TLS SNI 主机名匹配 HTTPS 流量。支持 GLOB 语法进行通配符匹配。如果 TLS 握手帧被分片为多个 TCP 段，则此匹配器将无法匹配主机名。</ArgTableRow>
<ArgTableRow arg="connection-limit" typ="super { !
, num
, ,num
 }">在达到给定值后，按地址或地址块匹配连接。由于该匹配器资源消耗较高，建议与 `connection-state=new` 和/或 `tcp-flags=syn` 配合使用。</ArgTableRow>
<ArgTableRow arg="layer7-protocol" typ="super { !
, enum
 }">在 layer7 协议菜单中定义的 Layer7 过滤器名称。</ArgTableRow>
<ArgTableRow arg="realm" typ="super { !
, num
 }">匹配路由 realm。仅适用于 IPv4。</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, enum () {  }
 }">按协议名称或编号匹配特定的 IP 协议。</ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipRange
 }">匹配源地址等于指定 IP 或属于指定 IP 范围的数据包。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipRange
 }">匹配目的地址等于指定 IP 或属于指定 IP 范围的数据包。</ArgTableRow>
<ArgTableRow arg="fragment" typ="super { bool
 }">匹配分片数据包。首片（起始分片）不计入。如果启用了连接跟踪，则不会存在分片，因为系统会自动重组每个数据包。仅适用于 IPv4。</ArgTableRow>
<ArgTableRow arg="psd" typ="super { num
, ,time
, ,num
, ,num
 }">
尝试检测 TCP 和 UDP 扫描。参数格式如下：`WeightThreshold, DelayThreshold, LowPortWeight, HighPortWeight`。
- `WeightThreshold` - 来自同一主机的具有不同目的端口的最新 TCP/UDP 数据包的总权重，用于判定为端口扫描序列。
- `DelayThreshold` - 来自同一主机的具有不同目的端口的数据包的延迟，用于判定为可能的端口扫描子序列。
- `LowPortWeight` - 具有特权目的端口（&lt;1024）的数据包的权重。
- `HighPortWeight` - 具有非特权目的端口的数据包的权重。仅适用于 IPv4。
</ArgTableRow>
<ArgTableRow arg="ipv4-options" typ="super { enum (strict-source-routing | loose-source-routing | no-source-routing | record-route | no-record-route | timestamp | no-timestamp | router-alert | no-router-alert | any | none) { strict-source-routing:0x1, loose-source-routing:0x2, no-source-routing:0x4, record-route:0x8, no-record-route:0x10, timestamp:0x20, no-timestamp:0x40, router-alert:0x80, no-router-alert:0x100, any:0x200, none:0x400 }
 }">
匹配 IPv4 头部选项。
- `any` - 匹配至少具有一个 IPv4 选项的数据包。
- `loose-source-routing` - 匹配具有松散源路由选项的数据包。
- `no-record-route` - 匹配没有记录路由选项的数据包。
- `no-router-alert` - 匹配没有路由器告警选项的数据包。
- `no-source-routing` - 匹配没有源路由选项的数据包。
- `no-timestamp` - 匹配没有时间戳选项的数据包。
- `record-route` - 匹配具有记录路由选项的数据包。
- `router-alert` - 匹配具有路由器告警选项的数据包。
- `strict-source-routing` - 匹配具有严格源路由选项的数据包。
- `timestamp` - 匹配具有时间戳的数据包。仅适用于 IPv4。
</ArgTableRow>
<ArgTableRow arg="src-address-type" typ="super { !
, ubit (unicast, local, broadcast, multicast, blackhole) { unicast, local, broadcast, multicast, blackhole }
 }">
匹配源地址类型：
- `unicast` - 用于点对点传输的 IP 地址。
- `local` - 地址分配给路由器的某个接口。
- `broadcast` - 数据包发送到子网中的所有设备。
- `multicast` - 数据包转发到定义的一组设备。
</ArgTableRow>
<ArgTableRow arg="dst-address-type" typ="super { !
, ubit (unicast, local, broadcast, multicast, blackhole) { unicast, local, broadcast, multicast, blackhole }
 }">
匹配目的地址类型：
- `unicast` - 用于点对点传输的 IP 地址。
- `local` - 目的地址分配给路由器的某个接口。
- `broadcast` - 数据包发送到子网中的所有设备。
- `multicast` - 数据包转发到定义的一组设备。
</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, enum
 }">将数据包的源地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, enum
 }">将数据包的目的地址与用户定义的地址列表进行匹配。仅支持一个列表。</ArgTableRow>
<ArgTableRow arg="hotspot" typ="multi { array-id, array-id, super { !
, enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 } { !
, enum (from-client | auth | local-dst | to-client | http) { from-client:0, auth:1, local-dst:2, to-client:3, http:4 }
 }
 }">
将来自 HotSpot 客户端的数据包与各种 HotSpot 匹配器进行匹配。
- `auth` - 匹配已认证的 HotSpot 客户端数据包。
- `from-client` - 匹配来自 HotSpot 客户端的数据包。
- `http` - 匹配发送到 HotSpot 服务器的 HTTP 请求。
- `local-dst` - 匹配发往 HotSpot 服务器的数据包。
- `to-client` - 匹配发送到 HotSpot 客户端的数据包。仅适用于 IPv4。
</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum ()">要使用的地址列表名称。适用于动作为 `add-dst-to-address-list` 或 `add-src-to-address-list` 的情况。</ArgTableRow>
<ArgTableRow arg="address-list-timeout" typ="alt { enum (none-dynamic | none-static) { none-dynamic:0, none-static:0xffffffff }
, time [ .. 21474836]
,  }">
地址将从 `address-list` 参数指定的地址列表中移除的时间间隔。与 `add-dst-to-address-list` 或 `add-src-to-address-list` 动作配合使用。
- `none-dynamic` (`00:00:00`) 将地址保留在地址列表中直到重启。
- `none-static` 将地址永久保留在地址列表中，并包含在配置导出/备份中。
</ArgTableRow>
<ArgTableRow arg="ttl" typ="super { enum (equal | not-equal | less-than | greater-than) { equal:0, not-equal:1, less-than:2, greater-than:3 }
, :num [0 .. 255]
 }">匹配数据包的 TTL 值。仅适用于 IPv4。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="super { !
, enum
 }">匹配由 mangle 功能标记了特定连接标记的数据包。如果设置为 `no-mark`，规则将匹配任何未标记的连接。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="super { !
, enum (ftp | pptp | h323 | sip | irc | quake3 | tftp) { ftp:0, pptp:1, h323:2, sip:3, irc:4, quake3:5, tftp:6 }
 }">基于连接跟踪助手的信息匹配相关连接的数据包。必须在 `/ip/firewall/service-port` 下启用相应的连接助手。</ArgTableRow>
<ArgTableRow arg="connection-bytes" typ="super { num
, -num
 }">仅当特定连接已传输给定字节数时匹配数据包。0 表示无穷大，例如 `connection-bytes=2000000-0` 表示当相关连接已传输超过 2MB 时规则匹配。</ArgTableRow>
<ArgTableRow arg="connection-rate" typ="super { !
, num
, -num
 }">允许基于连接的当前速率捕获流量。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="super { !
, enum () {  }
 }">匹配由 mangle 功能标记了特定路由标记的数据包。</ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, iface_enum {  } {  }
 }">数据包进入路由器的接口。</ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, iface_enum {  } {  }
 }">数据包离开路由器的接口。</ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。功能与 `in-interface` 相同。</ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。功能与 `out-interface` 相同。</ArgTableRow>
<ArgTableRow arg="in-bridge-port" typ="super { !
, iface_enum {  } {  }
 }">当入站接口为桥接时，数据包实际进入路由器的接口。仅在桥接设置中启用了 `use-ip-firewall` 时生效。</ArgTableRow>
<ArgTableRow arg="out-bridge-port" typ="super { !
, iface_enum {  } {  }
 }">当出站接口为桥接时，数据包实际离开路由器的接口。仅在桥接设置中启用了 `use-ip-firewall` 时生效。</ArgTableRow>
<ArgTableRow arg="in-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。功能与 `in-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="out-bridge-port-list" typ="super { !
, enum
 }">在接口列表中定义的接口集合。功能与 `out-bridge-port` 相同。</ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, enum
 }">匹配由 mangle 功能标记了特定数据包标记的数据包。如果设置为 `no-mark`，规则将匹配任何未标记的数据包。</ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">源端口和源端口范围的列表。仅适用于协议为 TCP 或 UDP 的情况。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">目的端口号或端口号范围的列表。</ArgTableRow>
<ArgTableRow arg="port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }">如果任意（源或目的）端口匹配指定的端口或端口范围列表，则匹配。仅适用于 `protocol` 为 TCP 或 UDP 的情况。</ArgTableRow>
<ArgTableRow arg="icmp-options" typ="super { !
, num [0 .. 255]
, [ :range [ .. 255]]
 }">匹配 ICMP 类型：代码字段。</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, macAddr
 }">匹配数据包的源 MAC 地址。</ArgTableRow>
<ArgTableRow arg="content" typ="super { !
, string
 }">匹配包含指定文本的数据包。</ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, num [0 .. 63]
 }">匹配入站数据包的优先级。优先级可能来自 VLAN、WMM、DSCP 或 MPLS EXP 位。</ArgTableRow>
<ArgTableRow arg="priority" typ="super { !
, num [0 .. 63]
 }">匹配设置新优先级后数据包的优先级。优先级可能来自 VLAN、WMM、DSCP、MPLS EXP 位，或通过使用 set-priority 动作设置的优先级。</ArgTableRow>
<ArgTableRow arg="dscp" typ="super { !
, num [0 .. 63]
 }">匹配 DSCP IP 头部字段。</ArgTableRow>
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
- `time` - 指定不能超过数据包或比特速率的时间间隔（可选，未指定时使用 1 秒）。
- `burst` - 初始匹配的数据包或比特数：该数字每 10ms 重新充电一次，因此 burst 至少应为每秒速率的 1/100。
- `mode` - 数据包或比特模式。
</ArgTableRow>
<ArgTableRow arg="dst-limit" typ="super { num
, [ /time]
, ,num
, ,enum (dst-address | dst-address-and-port | src-address | src-and-dst-addresses | addresses-and-dst-port) { dst-address:1, dst-address-and-port:3, src-address:4, src-and-dst-addresses:5, addresses-and-dst-port:7 }
, [ /time]
 }">
匹配数据包直到给定速率被超过。速率定义为每个时间间隔的数据包数。与 `limit` 匹配器不同，每个流都有其自己的限制。流由模式参数定义。参数格式如下：`rate[/time],burst,mode[/expire]`。
- `rate` - 每个时间间隔内每个流要匹配的数据包数。
- `time` - 指定每个流不能超过数据包计数速率的时间间隔（可选，未指定时使用 1 秒）。
- `burst` - 每个流初始匹配的数据包数：该数字在每次时间/速率时增加 1，直到达到此数字。
- `mode` - 指定哪些唯一字段定义流（src-address、dst-address、src-and-dst-address、dst-address-and-port、addresses-and-dst-port）。
- `expire` - 指定无数据包的流允许被删除的时间间隔（可选）。
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
 }">匹配每第 n 个数据包：`nth=2,1` 将匹配每 2 个数据包中的第 1 个，因此匹配规则所匹配的所有流量的 50%。</ArgTableRow>
<ArgTableRow arg="tcp-mss" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }">匹配 IP 数据包的 TCP MSS 值。</ArgTableRow>
<ArgTableRow arg="per-connection-classifier" typ="super { !
, enum (src-address | dst-address | both-addresses | src-port | src-address-and-port | dst-port | dst-address-and-port | both-ports | both-addresses-and-ports) { src-address:1, dst-address:2, both-addresses:3, src-port:4, src-address-and-port:5, dst-port:8, dst-address-and-port:10, both-ports:12, both-addresses-and-ports:15 }
, :num [1 .. ]
, /num [0 .. ]
 }">PCC 匹配器允许将流量划分为相等的流，并能够将具有特定选项集的数据包保留在特定的流中。</ArgTableRow>
<ArgTableRow arg="packet-size" typ="super { !
, num [ .. 65535]
, -num [ .. 65535]
 }">匹配指定大小或大小范围（以字节为单位）的数据包。</ArgTableRow>
<ArgTableRow arg="log" typ="bool">向系统日志添加一条消息，包含以下数据：in-interface、out-interface、src-mac、protocol、src-ip:port-&gt;dst-ip:port 以及数据包长度。即使动作不是 `log`，也允许记录数据包，这对于调试防火墙非常有用。</ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string">在每条日志消息的开头添加指定文本。适用于配置了 `action=log` 或 `log=yes` 的情况。</ArgTableRow>
<ArgTableRow arg="ipsec-policy" typ="super { enum (in | out) { in:0, out:1 }
, ,enum (none | ipsec) { none:0, ipsec:1 }
 }">
匹配 IPsec 使用的策略。值格式如下：`direction, policy`。
- `in` - 在 PREROUTING、INPUT 和 FORWARD 链中有效。
- `out` - 在 POSTROUTING、OUTPUT 和 FORWARD 链中有效。
- `ipsec` - 匹配受 IPsec 处理的数据包。
- `none` - 匹配不受 IPsec 处理的数据包。
</ArgTableRow>
</ArgTable>

#### ip/firewall/calea/reset-counters

**类型：** 命令

#### ip/firewall/calea/reset-counters-all

**类型：** 命令