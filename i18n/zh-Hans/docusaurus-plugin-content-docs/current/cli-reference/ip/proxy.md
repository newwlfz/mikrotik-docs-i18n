# 代理

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/proxy

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-address" typ="object { alt { ipAddr
, ip6Addr
 } { ipAddr
, ip6Addr
 }
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="multi { num [1 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="anonymous" typ="bool"></ArgTableRow>
<ArgTableRow arg="parent-proxy" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="parent-proxy-port" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-administrator" typ="string"></ArgTableRow>
<ArgTableRow arg="max-cache-size" typ="alt { enum (none | unlimited) { none:0, unlimited:0xffffffff }
, num
 }"></ArgTableRow>
<ArgTableRow arg="max-cache-object-size" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-on-disk" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-client-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="max-server-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="max-fresh-time" typ="time"></ArgTableRow>
<ArgTableRow arg="serialize-connections" typ="bool"></ArgTableRow>
<ArgTableRow arg="always-from-cache" typ="bool"></ArgTableRow>
<ArgTableRow arg="cache-hit-dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-path" typ="string"></ArgTableRow>
</ArgTable>

### ip/proxy/access

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) { GET, HEAD, POST, PUT, CONNECT, OPTIONS, DELETE, TRACE }
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny | redirect | url-append)"></ArgTableRow>
<ArgTableRow arg="action-data" typ="string {  }">重定向 URL/追加 URL</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>

#### ip/proxy/access/reset-counters

**类型：** 命令

#### ip/proxy/access/reset-counters-all

**类型：** 命令

### ip/proxy/cache

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) { GET, HEAD, POST, PUT, CONNECT, OPTIONS, DELETE, TRACE }
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/cache-contents

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="uri" typ="string"></ArgTableRow>
<ArgTableRow arg="file-size" typ="num"></ArgTableRow>
<ArgTableRow arg="last-modified" typ="date"></ArgTableRow>
<ArgTableRow arg="last-modified-time" typ="date"></ArgTableRow>
<ArgTableRow arg="last-accessed" typ="date"></ArgTableRow>
<ArgTableRow arg="last-accessed-time" typ="date"></ArgTableRow>
</ArgTable>

#### ip/proxy/cache/reset-counters

**类型：** 命令

#### ip/proxy/cache/reset-counters-all

**类型：** 命令

### ip/proxy/clear-cache

**类型：** 命令

### ip/proxy/connections

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="server">服务器</ArgTableRow>
<ArgTableRow arg="C" typ="client">客户端</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="last-protocol" typ="enum (HTTP/1.0 | HTTP/1.1 | FTP)"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (rx-header | resolving | connecting | waiting | rx-body | tx-header | tx-body | idle)"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/direct

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, multi { , , range [ .. 65535]
 } { , , range [ .. 65535]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-port" typ="super { !
, num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-host" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="super { !
, string
 }"></ArgTableRow>
<ArgTableRow arg="method" typ="super { !
, enum (GET | HEAD | POST | PUT | CONNECT | OPTIONS | DELETE | TRACE) { GET, HEAD, POST, PUT, CONNECT, OPTIONS, DELETE, TRACE }
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (allow | deny)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
</ArgTable>

#### ip/proxy/direct/reset-counters

**类型：** 命令

#### ip/proxy/direct/reset-counters-all

**类型：** 命令

### ip/proxy/inserts

**类型：** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="successes" typ="num"></ArgTableRow>
<ArgTableRow arg="denied" typ="num"></ArgTableRow>
<ArgTableRow arg="too-large" typ="num"></ArgTableRow>
<ArgTableRow arg="no-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="errors" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/lookups

**类型：** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="successes" typ="num"></ArgTableRow>
<ArgTableRow arg="not-found" typ="num"></ArgTableRow>
<ArgTableRow arg="non-cacheable" typ="num"></ArgTableRow>
<ArgTableRow arg="denied" typ="num"></ArgTableRow>
<ArgTableRow arg="expired" typ="num"></ArgTableRow>
<ArgTableRow arg="no-expiration-info" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/monitor

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="enum (stopped | running | invalid-address | building-cache | passthrough)"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="client-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="server-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="hits" typ="num"></ArgTableRow>
<ArgTableRow arg="cache-used" typ="num"></ArgTableRow>
<ArgTableRow arg="total-ram-used" typ="num"></ArgTableRow>
<ArgTableRow arg="received-from-servers" typ="num"></ArgTableRow>
<ArgTableRow arg="sent-to-clients" typ="num"></ArgTableRow>
<ArgTableRow arg="hits-sent-to-clients" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/refreshes

**类型：** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="url-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="request-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="expired" typ="num"></ArgTableRow>
<ArgTableRow arg="response-max-age" typ="num"></ArgTableRow>
<ArgTableRow arg="config-max-fresh" typ="num"></ArgTableRow>
<ArgTableRow arg="heuristic" typ="num"></ArgTableRow>
<ArgTableRow arg="other" typ="num"></ArgTableRow>
</ArgTable>

### ip/proxy/reset-html

**类型：** 命令