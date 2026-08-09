# BFD

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/bfd

**条件：** BFD_AUTHENTICATION
**类型：** 目录

### routing/bfd/authentication

**条件：** BFD_AUTHENTICATION
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="T" typ="transmit">发送</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (none | simple-password | keyed-md5 | meticulous-keyed-md5 | keyed-sha1 | meticulous-keyed-sha1)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="transmit-after" typ="date"></ArgTableRow>
<ArgTableRow arg="accept-before" typ="date"></ArgTableRow>
</ArgTable>

### routing/bfd/configuration

**条件：** BFD_AUTHENTICATION
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum" unset="1">此配置所适用的虚拟路由转发（VRF）实例。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">应启用 BFD 配置的接口列表。</ArgTableRow>
<ArgTableRow arg="addresses" typ="object { alt { ip6Prefix
, ipPrefix
 } { ip6Prefix
, ipPrefix
 }
 }" unset="1">此配置条目仅适用于与这些特定远程邻居建立的 BFD 会话。</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum" unset="1">防火墙地址列表名称。如果远程 IP 地址包含在指定列表中，则 BFD 配置将生效。</ArgTableRow>
<ArgTableRow arg="min-tx" typ="time" unset="1">本地路由器在向邻居发送 BFD 数据包时希望使用的期望发送间隔。</ArgTableRow>
<ArgTableRow arg="min-rx" typ="time" unset="1">本地路由器在接收 BFD 数据包之间要求的最小接收间隔。</ArgTableRow>
<ArgTableRow arg="multiplier" typ="num" unset="1">此值乘以协商后的传输间隔以确定**保持时间**；如果在保持时间内未收到任何数据包，则邻居将被宣告为宕机。`保持时间 = 协商间隔 × 乘数`</ArgTableRow>
<ArgTableRow arg="forbid-bfd" typ="bool" unset="1">如果 = **yes**：匹配条件的 BFD 会话将被禁止。</ArgTableRow>
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

### routing/bfd/session

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="U" typ="up">运行中</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (admin-down | down | init | up)"></ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="desired-tx-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="actual-tx-interval" typ="time">设备当前发送 BFD 控制数据包的实际频率。</ArgTableRow>
<ArgTableRow arg="required-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="multiplier" typ="num"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="packets-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-tx" typ="num"></ArgTableRow>
</ArgTable>