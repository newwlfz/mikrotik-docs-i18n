# Bridge（桥接）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/bridge

**条件：** MSRP_ENABLE
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="Y" typ="managed">受管</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="protocol-mode" typ="enum (none | stp | rstp | mstp)"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="enum (disabled | temporary-query | permanent)"></ArgTableRow>
<ArgTableRow arg="multicast-querier" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="startup-query-count" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="last-member-query-count" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="last-member-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="membership-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="querier-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="query-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="query-response-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="startup-query-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="igmp-version" typ="enum (2 | 3)"></ArgTableRow>
<ArgTableRow arg="mld-version" typ="enum (1 | 2)"></ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr {  }"></ArgTableRow>
<ArgTableRow arg="ageing-time" typ="time"></ArgTableRow>
<ArgTableRow arg="priority" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="max-message-age" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="forward-delay" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="transmit-hold-count" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="region-name" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="region-revision" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="max-hops" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="vlan-filtering" typ="bool"></ArgTableRow>
<ArgTableRow arg="ether-type" typ="enum (0x8100 | 0x88a8 | 0x9100)"></ArgTableRow>
<ArgTableRow arg="pvid" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="frame-types" typ="enum (admit-all | admit-only-vlan-tagged | admit-only-untagged-and-priority-tagged)"></ArgTableRow>
<ArgTableRow arg="ingress-filtering" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="dhcp-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-agent-circuit-id" typ="string">
指定要添加到通过桥接的 DHCP 消息中的 option 82 中继代理 circuit-id 子选项值。
字符串长度限制为 255 个字符，默认值为：$(INTERFACE):$(VID)。
字符串值可以包含变量，变量名必须用括号括起来并以美元符号开头。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支持以下变量：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
为了与之前版本兼容（此前 remote-id 值是固定的），当未启用 VLAN 过滤时，默认值表达式中出现的分号不包含在 remote-id 值中。
</ArgTableRow>
<ArgTableRow arg="dhcp-agent-remote-id" typ="string">
指定要添加到通过桥接的 DHCP 消息中的 option 82 中继代理 remote-id 子选项值。
字符串长度限制为 255 个字符，默认值为：$(BRIDGEMAC)。
字符串值可以包含变量，变量名必须用括号括起来并以美元符号开头。
示例：'some_arbitrary_text $(HOSTNAME) another_piece_of_text $(BRIDGEMAC)'。
支持以下变量：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="dhcpv6-snooping" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-circuit-id" typ="string">
指定要添加到通过桥接的 DHCPv6 消息中的 DHCPv6 option 18 值。
字符串长度限制为 255 个字符，默认值为：$(INTERFACE):$(VID)。
字符串值可以包含变量，变量名必须用括号括起来并以美元符号开头。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支持以下变量：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="dhcpv6-agent-remote-id" typ="string">
指定要添加到通过桥接的 DHCPv6 消息中的 DHCPv6 option 37 值。
字符串长度限制为 255 个字符，默认值为：$(BRIDGEMAC)。
字符串值可以包含变量，变量名必须用括号括起来并以美元符号开头。
示例：'some_arbitrary_text $(VID) another_piece_of_text $(INTERFACE)'。
支持以下变量：HOSTNAME、INTERFACE、VID 和 BRIDGEMAC。
</ArgTableRow>
<ArgTableRow arg="ra-guard" typ="bool"></ArgTableRow>
<ArgTableRow arg="port-cost-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="mvrp" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="msrp" typ="bool"></ArgTableRow>
<ArgTableRow arg="forward-reserved-addresses" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="max-learned-entries" typ="alt { enum (unlimited | auto) { unlimited:bridge::B_MAX_LEARN_UNLIMITED, auto:bridge::B_MAX_LEARN_AUTO }
, num
 }"></ArgTableRow>
<ArgTableRow arg="mlag-peer-port" typ="alt { iface_enum { none:nv::BADID } { none:nv::BADID }
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mlag-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="mlag-heartbeat" typ="alt { enum (none) { none:0 }
, time [1s .. 10s]
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>

### interface/bridge/calea

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum (input | forward | output)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (sniff | sniff-pc)"></ArgTableRow>
<ArgTableRow arg="sniff-target" typ="ipAddr {  }"></ArgTableRow>
<ArgTableRow arg="sniff-target-port" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="sniff-id" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="super { !
, alt { enum (length) { length:1,  }
, num [ .. 65535]
 } { enum (length) { length:1,  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="super { !
, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-type" typ="super { !
, enum (host | broadcast | multicast | other-host) { host:0, broadcast:1, multicast:2, other-host:3 }
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { num
, [ /time]
, ,num
 }"></ArgTableRow>
<ArgTableRow arg="802.3-sap" typ="super { !
, num [ .. 0xff]
 }"></ArgTableRow>
<ArgTableRow arg="802.3-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-opcode" typ="super { !
, alt { enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) { request:1, reply:2, request-reverse:3, reply-reverse:4, drarp-request:5, drarp-reply:6, drarp-error:7, inarp-request:8, inarp-reply:9, arp-nak:10 }
, num [ .. 65535]
 } { enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) { request:1, reply:2, request-reverse:3, reply-reverse:4, drarp-request:5, drarp-reply:6, drarp-error:7, inarp-request:8, inarp-reply:9, arp-nak:10 }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="arp-hardware-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-packet-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-gratuitous" typ="super { bool
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="super { !
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="super { !
, num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-encap" typ="super { !
, alt { enum (length) { length:1,  }
, num [ .. 65535]
 } { enum (length) { length:1,  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-type" typ="super { !
, alt { enum (config | tcn) { config:0, tcn:0x80 }
, num [ .. 255]
 } { enum (config | tcn) { config:0, tcn:0x80 }
, num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-flags" typ="super { !
, alt { enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 }
, num [ .. 255]
 } { enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 }
, num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-priority" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-cost" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-priority" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-msg-age" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-max-age" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-hello-time" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-forward-delay" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, num [0 .. 63]
 }"></ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="log" typ="bool"></ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
</ArgTable>

#### interface/bridge/calea/reset-counters

**类型：** 命令

#### interface/bridge/calea/reset-counters-all

**类型：** 命令

### interface/bridge/filter

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="all" typ="switch"></ArgTableRow>
<ArgTableRow arg="static" typ="switch"></ArgTableRow>
<ArgTableRow arg="dynamic" typ="switch"></ArgTableRow>
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | passthrough | drop | jump | return | log | mark-packet | set-priority)"></ArgTableRow>
<ArgTableRow arg="jump-target" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="new-packet-mark" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="new-priority" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="passthrough" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="in-interface" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge" typ="super { !
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="in-interface-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="out-interface-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="in-bridge-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="out-bridge-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="super { !
, alt { enum (length) { length:1,  }
, num [ .. 65535]
 } { enum (length) { length:1,  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="super { !
, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="packet-mark" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="packet-type" typ="super { !
, enum (host | broadcast | multicast | other-host) { host:0, broadcast:1, multicast:2, other-host:3 }
 }"></ArgTableRow>
<ArgTableRow arg="limit" typ="super { num
, [ /time]
, ,num
 }"></ArgTableRow>
<ArgTableRow arg="802.3-sap" typ="super { !
, num [ .. 0xff]
 }"></ArgTableRow>
<ArgTableRow arg="802.3-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-opcode" typ="super { !
, alt { enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) { request:1, reply:2, request-reverse:3, reply-reverse:4, drarp-request:5, drarp-reply:6, drarp-error:7, inarp-request:8, inarp-reply:9, arp-nak:10 }
, num [ .. 65535]
 } { enum (request | reply | request-reverse | reply-reverse | drarp-request | drarp-reply | drarp-error | inarp-request | inarp-reply | arp-nak) { request:1, reply:2, request-reverse:3, reply-reverse:4, drarp-request:5, drarp-reply:6, drarp-error:7, inarp-request:8, inarp-reply:9, arp-nak:10 }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="arp-hardware-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-packet-type" typ="super { !
, num [ .. 0xffff]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-address" typ="super { !
, ipAddr
, /num [ .. 32]
 }"></ArgTableRow>
<ArgTableRow arg="arp-src-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-dst-mac-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="arp-gratuitous" typ="super { bool
 }"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="super { !
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="super { !
, num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-encap" typ="super { !
, alt { enum (length) { length:1,  }
, num [ .. 65535]
 } { enum (length) { length:1,  }
, num [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-type" typ="super { !
, alt { enum (config | tcn) { config:0, tcn:0x80 }
, num [ .. 255]
 } { enum (config | tcn) { config:0, tcn:0x80 }
, num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-flags" typ="super { !
, alt { enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 }
, num [ .. 255]
 } { enum (topology-change | topology-change-ack) { topology-change:1, topology-change-ack:0x80 }
, num [ .. 255]
 }
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-priority" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-root-cost" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-priority" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-sender-address" typ="super { !
, macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="stp-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-msg-age" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-max-age" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-hello-time" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="stp-forward-delay" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ingress-priority" typ="super { !
, num [0 .. 63]
 }"></ArgTableRow>
<ArgTableRow arg="tls-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="log" typ="bool"></ArgTableRow>
<ArgTableRow arg="log-prefix" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
</ArgTable>

#### interface/bridge/filter/reset-counters

**类型：** 命令

#### interface/bridge/filter/reset-counters-all

**类型：** 命令

### interface/bridge/host

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="L" typ="local">本地</ArgTableRow>
<ArgTableRow arg="E" typ="external">外部</ArgTableRow>
<ArgTableRow arg="A" typ="aged">已老化</ArgTableRow>
<ArgTableRow arg="a" typ="aged-peer">已老化对端</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="on-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dhcpv4-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-server-id" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dhcpv4-status" typ="enum (bound | requesting | searching | renewing | rebinding | expired | relay-agent)"></ArgTableRow>
<ArgTableRow arg="dhcpv4-expires-after" typ="time"></ArgTableRow>
</ArgTable>

### interface/bridge/mdb

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="group" typ="address (flags=46m)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { array-id, iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="on-interface" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
</ArgTable>

### interface/bridge/monitor

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="state" typ="enum (disabled | disabled | enabled | enabled)"></ArgTableRow>
<ArgTableRow arg="current-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="bridge-id" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="root-bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="root-bridge-id" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="regional-root-bridge-id" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="root-path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="root-port" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="designated-port-count" typ="num"></ArgTableRow>
<ArgTableRow arg="mst-config-digest" typ="string"></ArgTableRow>
<ArgTableRow arg="fast-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-router" typ="bool"></ArgTableRow>
<ArgTableRow arg="igmp-querier" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="mld-querier" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="declared-vlan-ids" typ="multi { , , range
 }"></ArgTableRow>
<ArgTableRow arg="registered-vlan-ids" typ="multi { , , range
 }"></ArgTableRow>
<ArgTableRow arg="mlag-state" typ="string"></ArgTableRow>
<ArgTableRow arg="mlag-active-role" typ="enum (primary | secondary)"></ArgTableRow>
</ArgTable>

### interface/bridge/msrp

**条件：** MSRP_ENABLE
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="bridge" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rank" typ="num"></ArgTableRow>
<ArgTableRow arg="stream-id" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="talker" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="listener" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="dst-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vid" typ="num"></ArgTableRow>
<ArgTableRow arg="max-frame-size" typ="num"></ArgTableRow>
<ArgTableRow arg="max-interval-frames" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="active-talker" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="active-listener" typ="iface_