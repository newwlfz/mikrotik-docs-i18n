# 池

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/pool

**软件包：** ipv6
**类型：** 目录

IP 池用于定义可供各种 RouterOS 工具使用的 IPv6 前缀，例如 DHCP 服务器、点对点服务器等。在可能的情况下，每个客户端（OWNER/INFO 对）都会获得相同的 IPv6 前缀。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1">池的名称。</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">另一个池的名称，用于动态获取前缀。</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="num" mandatory="1">该选项表示分配给客户端的前缀大小。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="time"></ArgTableRow>
</ArgTable>

### ipv6/pool/used

**软件包：** ipv6
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="pool" typ="enum">保留前缀的池的名称。</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix">从池中分配给客户端的 IPv6 前缀。</ArgTableRow>
<ArgTableRow arg="owner" typ="string">保留前缀的对象（如“DHCP”等）。</ArgTableRow>
<ArgTableRow arg="info" typ="string">显示从客户端接收到的 DUID 相关信息（十六进制值）。也可能包含十六进制的原始时间戳。</ArgTableRow>
</ArgTable>