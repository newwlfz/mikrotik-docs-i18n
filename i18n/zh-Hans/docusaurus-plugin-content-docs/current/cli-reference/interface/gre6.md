# GRE6

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/gre6

**软件包：** ipv6
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="local-address" typ="ip6Addr">本地地址</ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=6Dvi)" mandatory="1">远程地址</ArgTableRow>
<ArgTableRow arg="keepalive" typ="super { time [1 .. ]
, [ ,num [1 .. ]]
 }">保活</ArgTableRow>
<ArgTableRow arg="dscp" typ="num">差分服务代码点</ArgTableRow>
<ArgTableRow arg="clamp-tcp-mss" typ="bool">钳制TCP最大报文段长度</ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="bool">不分片</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string" syscap="security">IPsec密钥</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="actual-mtu" typ="num">实际最大传输单元</ArgTableRow>
<ArgTableRow arg="current-remote-address" typ="ip6Addr">当前远程地址</ArgTableRow>
</ArgTable>