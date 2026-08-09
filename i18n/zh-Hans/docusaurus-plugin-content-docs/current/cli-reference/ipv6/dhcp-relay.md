# DHCP 中继

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-relay

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">中继将监听此接口上来自客户端的消息</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="object { alt { composite { ,  } { ,  }
, ip6Addr
 } { composite { ,  } { ,  }
, ip6Addr
 }
 }" mandatory="1">中继消息将被转发到的服务器</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, enum
 }">添加到中继转发消息中的选项。请注意，选项18（接口ID）会自动添加，以便中继能够正确转发回复消息。</ArgTableRow>
<ArgTableRow arg="link-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }">如果DHCP数据包中的秒数字段小于延迟阈值，则忽略此数据包</ArgTableRow>
<ArgTableRow arg="store-relayed-bindings" typ="bool">为回复消息中找到的有效绑定添加路由</ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/monitor

**软件包：** dhcp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="responses" typ="num"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/option

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
<ArgTableRow arg="only-if-mac-available" typ="bool">仅当数据包源自客户端（而非另一个中继）且MAC地址可推导时，才添加此选项</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/reset-counters

**软件包：** dhcp
**类型：** 命令

### ipv6/dhcp-relay/routes

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="relay" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="peer-address" typ="ip6Addr">用作网关</ArgTableRow>
<ArgTableRow arg="life-time" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
</ArgTable>