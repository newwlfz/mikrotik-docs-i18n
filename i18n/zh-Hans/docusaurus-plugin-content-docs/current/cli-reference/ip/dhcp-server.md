# DHCP 服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dhcp-server

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)"></ArgTableRow>
<ArgTableRow arg="dynamic-lease-identifiers" typ="ubit (client-mac, client-id, opt-82)"></ArgTableRow>
<ArgTableRow arg="bootp-support" typ="enum (none | static | dynamic)"></ArgTableRow>
<ArgTableRow arg="bootp-lease-time" typ="alt { , enum (lease-time | forever) { lease-time:0, forever:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="server-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-arp" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">仅在 add-dns-entries=yes 时使用。如果非空，则为 DNS 条目附加后缀，并在响应中添加选项 15（域名）。</ArgTableRow>
<ArgTableRow arg="authoritative" typ="enum (no | after-10sec-delay | after-2sec-delay | yes)"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)"></ArgTableRow>
<ArgTableRow arg="client-mac-limit" typ="enum (unlimited)">单个客户端 MAC 地址可获得的最大租约数量</ArgTableRow>
<ArgTableRow arg="conflict-detection" typ="bool">在分配租约前使用 ARP 和 ICMP 检测 IP 地址冲突</ArgTableRow>
<ArgTableRow arg="use-framed-as-classless" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="support-broadband-tr101" typ="bool">按照 RFC 4679 和宽带论坛 TR-101 的规定，将额外的选项 82 子选项传递给 RADIUS 服务器</ArgTableRow>
</ArgTable>

### ip/dhcp-server/alert

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="valid-server" typ="multi { macAddr
 }"></ArgTableRow>
<ArgTableRow arg="on-alert" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="alert-timeout" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="unknown-server" typ="multi { macAddr
 }"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/alert/reset-alert

**软件包：** dhcp
**类型：** 命令

### ip/dhcp-server/config

**软件包：** dhcp
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="store-leases-disk" typ="alt { enum (immediately | never) { immediately:0, never:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="accounting" typ="bool"></ArgTableRow>
<ArgTableRow arg="interim-update" typ="time"></ArgTableRow>
<ArgTableRow arg="radius-password" typ="alt { bool
, string
 }"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/lease

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="radius">RADIUS</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">已阻止</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="alt { ipAddr
, enum
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="use-src-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="routes" typ="object { composite { ,  } { ,  }
 }">客户端连接时在服务器上出现的路由</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (bottom | first)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="block-access" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="agent-circuit-id" typ="string">如果非空，即使 MAC 或 client-id 不同，也使用它通过选项 82 匹配租约</ArgTableRow>
<ArgTableRow arg="agent-remote-id" typ="string">如果非空，即使 MAC 或 client-id 不同，也使用它通过选项 82 匹配租约</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="enum (waiting | testing | declined | offered | bound | authorizing | conflict)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time
 }"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="active-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="active-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="active-client-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-server" typ="enum"></ArgTableRow>
<ArgTableRow arg="active-agent-circuit-id" typ="string"></ArgTableRow>
<ArgTableRow arg="active-agent-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
<ArgTableRow arg="class-id" typ="string">最近一次收到的 DHCP 请求中的 DHCP 选项 60</ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/lease/check-status

**软件包：** dhcp
**类型：** 命令

#### ip/dhcp-server/lease/make-static

**软件包：** dhcp
**类型：** 命令

#### ip/dhcp-server/lease/send-reconfigure

**软件包：** dhcp
**类型：** 命令

### ip/dhcp-server/matcher

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)" mandatory="1">全局或单个服务器</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">此条目使用的地址池</ArgTableRow>
<ArgTableRow arg="option-set" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { num [1 .. 254]
, enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1">要匹配的选项内容，以字符串或带 0x 前缀的十六进制表示</ArgTableRow>
<ArgTableRow arg="matching-type" typ="enum (exact | substring)" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/network

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="netmask" typ="num"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="alt { , multi { ipAddr
 } { ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">不会向客户端发送任何服务器</ArgTableRow>
<ArgTableRow arg="wins-server" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="ntp-server" typ="alt { , multi { ipAddr
 } { ipAddr
 }
 }"></ArgTableRow>
<ArgTableRow arg="ntp-none" typ="bool">不会向客户端发送任何服务器</ArgTableRow>
<ArgTableRow arg="caps-manager" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="next-server" typ="ipAddr">用于下一个引导阶段的 siaddr</ArgTableRow>
<ArgTableRow arg="boot-file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/option

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="alt { num [1 .. 254]
, enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string">0x - 精确十六进制值，'' - 字符串或 IP 地址值</ArgTableRow>
<ArgTableRow arg="force" typ="bool">始终在回复中包含此选项</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

#### ip/dhcp-server/option/sets

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>

### ip/dhcp-server/setup

**软件包：** dhcp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="network" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ippool" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="send-dns" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="lease-time" typ="time"></ArgTableRow>
</ArgTable>