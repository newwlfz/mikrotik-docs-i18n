# 热点（Hotspot）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/hotspot

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="S" typ="HTTPS">HTTPS</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="alt { iface_enum
, iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="login-timeout" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="addresses-per-mac" typ="enum (unlimited)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="ip-of-dns-name" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="proxy-status" typ="string"></ArgTableRow>
</ArgTable>

### ip/hotspot/active

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="R" typ="radius">RADIUS</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">已阻止</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="server" typ="enum"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="login-by" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="session-time-left" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-time" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-total" typ="num"></ArgTableRow>
<ArgTableRow arg="advertisement" typ="enum (disabled | sleeping | pending | pending,block)"></ArgTableRow>
</ArgTable>

#### ip/hotspot/active/login

**软件包：** hotspot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
</ArgTable>

### ip/hotspot/cookie

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="M" typ="mac-cookie">MAC Cookie</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="expires-in" typ="time"></ArgTableRow>
</ArgTable>

### ip/hotspot/host

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="static">静态</ArgTableRow>
<ArgTableRow arg="H" typ="DHCP">DHCP</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="A" typ="authorized">已授权</ArgTableRow>
<ArgTableRow arg="P" typ="bypassed">已绕过</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="to-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="server" typ="enum"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-time" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="host-dead-time" typ="time"></ArgTableRow>
<ArgTableRow arg="bridge-port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="http-proxy" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="found-by" typ="string"></ArgTableRow>
</ArgTable>

#### ip/hotspot/host/make-binding

**软件包：** hotspot
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="comment" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (regular | bypassed | blocked)"></ArgTableRow>
</ArgTable>

### ip/hotspot/ip-binding

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="P" typ="bypassed">已绕过</ArgTableRow>
<ArgTableRow arg="B" typ="blocked">已阻止</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="address" typ="ipRange {  }"></ArgTableRow>
<ArgTableRow arg="to-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (regular | bypassed | blocked)"></ArgTableRow>
</ArgTable>

### ip/hotspot/profile

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="hotspot-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="html-directory" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="html-directory-override" typ="file"></ArgTableRow>
<ArgTableRow arg="install-hotspot-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="http-proxy" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="login-by" typ="ubit (mac, cookie, http-chap, https, http-pap, trial, mac-cookie)"></ArgTableRow>
<ArgTableRow arg="mac-auth-mode" typ="enum (mac-as-username | mac-as-username-and-password)"></ArgTableRow>
<ArgTableRow arg="mac-auth-password" typ="string { ,  }"></ArgTableRow>
<ArgTableRow arg="http-cookie-lifetime" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="ssl-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="split-user-domain" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="trial-uptime-limit" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="trial-uptime-reset" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="trial-user-profile" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="use-radius" typ="bool"></ArgTableRow>
<ArgTableRow arg="radius-accounting" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="radius-interim-update" typ="alt { , , enum (received) { received:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="nas-port-type" typ="enum (ethernet | cable | wireless-802.11)"></ArgTableRow>
<ArgTableRow arg="radius-default-domain" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="radius-location-id" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="radius-location-name" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="radius-mac-format" typ="enum (XX:XX:XX:XX:XX:XX | XXXX:XXXX:XXXX | XXXXXX:XXXXXX | XX-XX-XX-XX-XX-XX | XXXXXX-XXXXXX | XXXXXXXXXXXX | XX XX XX XX XX XX)"></ArgTableRow>
</ArgTable>

### ip/hotspot/reset-html

**软件包：** hotspot
**类型：** 命令

### ip/hotspot/service-port

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ports" typ="multi { num [1 .. 65535]
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

### ip/hotspot/user

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="server" typ="enum (all)"></ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="otp-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="routes" typ="string"></ArgTableRow>
<ArgTableRow arg="email" typ="string"></ArgTableRow>
<ArgTableRow arg="limit-uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="limit-bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="limit-bytes-total" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
</ArgTable>

#### ip/hotspot/user/profile

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="session-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="super { alt { enum (none) { none:0 }
, time
 } { enum (none) { none:0 }
, time
 }
 }"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="super { alt { enum (none) { none:0 }
, time
 } { enum (none) { none:0 }
, time
 }
 }"></ArgTableRow>
<ArgTableRow arg="status-autorefresh" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="shared-users" typ="enum (unlimited)"></ArgTableRow>
<ArgTableRow arg="add-mac-cookie" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-cookie-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="super { enum (bottom | first) { bottom:0xffffffff, first:0 }
 }"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="super { enum (none) { none:0 }
 }"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="super { enum
 }"></ArgTableRow>
<ArgTableRow arg="address-list" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="incoming-filter" typ="string"></ArgTableRow>
<ArgTableRow arg="outgoing-filter" typ="string"></ArgTableRow>
<ArgTableRow arg="incoming-packet-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="outgoing-packet-mark" typ="string"></ArgTableRow>
<ArgTableRow arg="on-login" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-logout" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="transparent-proxy" typ="bool"></ArgTableRow>
<ArgTableRow arg="open-status-page" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="advertise" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="advertise-url" typ="multi { , string
 }"></ArgTableRow>
<ArgTableRow arg="advertise-interval" typ="multi { , time
 }"></ArgTableRow>
<ArgTableRow arg="advertise-timeout" typ="alt { , enum (immediately | never) { immediately:0, never:0xffffffff }
, time
 }"></ArgTableRow>
</ArgTable>

#### ip/hotspot/user/reset-counters

**软件包：** hotspot
**类型：** 命令

### ip/hotspot/walled-garden

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="server" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) { GET, HEAD, POST, PUT, CONNECT, OPTIONS, DELETE, TRACE }
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="dst-address" typ="super { !
, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>

#### ip/hotspot/walled-garden/ip

**软件包：** hotspot
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="server" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipRange
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="string"></ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="src-address-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="dst-address-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (accept | drop | reject)"></ArgTableRow>
</ArgTable>

#### ip/hotspot/walled-garden/reset-counters

**软件包：** hotspot
**类型：** 命令

#### ip/hotspot/walled-garden/reset-counters-all

**软件包：** hotspot
**类型：** 命令