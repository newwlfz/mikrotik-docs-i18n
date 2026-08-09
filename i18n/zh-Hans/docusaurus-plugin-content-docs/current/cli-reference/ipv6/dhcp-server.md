# DHCP 服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-server

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="alt { enum (static-only) { static-only:0xffffffff }
, enum
 }">动态前缀绑定将从中获取前缀的地址池</ArgTableRow>
<ArgTableRow arg="address-pool" typ="alt { enum (static-only) { static-only:0xffffffff }
, enum
 }">动态地址绑定将从中获取地址的地址池（地址池前缀长度必须为128）</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">新建及续租绑定的持续时间</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">附加快速提交选项，以使用两包Solicit-Reply交换</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">使用RADIUS服务器进行认证</ArgTableRow>
<ArgTableRow arg="preference" typ="num">通告消息优先级，服务器优先级值最高者将被优先选择</ArgTableRow>
<ArgTableRow arg="binding-script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, alt { enum
, enum
 } { enum
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">路由表中已分配客户端绑定的距离值</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }">绑定前缀/地址将被添加到的地址列表（可由绑定的address-lists参数覆盖）</ArgTableRow>
<ArgTableRow arg="ignore-ia-na-bindings" typ="bool">服务器将忽略客户端发送消息中的IA_NA选项，并视为消息中不包含这些选项</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-server/binding

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="R" typ="radius">RADIUS</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="alt { ip6Prefix
 }">为客户端分配单个地址或前缀</ArgTableRow>
<ArgTableRow arg="duid" typ="string" mandatory="1">十六进制字符串</ArgTableRow>
<ArgTableRow arg="iaid" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ia-type" typ="enum (na | pd)"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)">可向客户端提供此绑定的服务器名称</ArgTableRow>
<ArgTableRow arg="life-time" typ="time"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="enum">用于地址，前缀长度为128的地址池</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, alt { enum
, enum
 } { enum
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">客户端的比特率限制</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }">绑定前缀/地址将被添加到的地址列表（覆盖服务器的address-lists参数）</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-server" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (waiting | offered | bound)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time
 }"></ArgTableRow>
<ArgTableRow arg="client-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>

#### ipv6/dhcp-server/binding/make-static

**软件包：** dhcp
**类型：** 命令

#### ipv6/dhcp-server/binding/send-reconfigure

**软件包：** dhcp
**类型：** 命令

### ipv6/dhcp-server/option

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

#### ipv6/dhcp-server/option/sets

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>