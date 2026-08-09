# PPTP 客户端

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/pptp-client

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大MTU</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大MRU</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">MRRU</ArgTableRow>
<ArgTableRow arg="connect-to" typ="alt { ipAddr
, string
 }" mandatory="1">连接至</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用户名</ArgTableRow>
<ArgTableRow arg="password" typ="string">密码</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">配置文件</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)">保活超时</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively)">使用对端DNS</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">添加默认路由</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }">默认路由距离</ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool">按需拨号</ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)">允许</ArgTableRow>
</ArgTable>

### interface/pptp-client/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string">状态</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">运行时间</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">编码</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">MTU</ArgTableRow>
<ArgTableRow arg="mru" typ="num">MRU</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">本地地址</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">远程地址</ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr">本地IPv6地址</ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr">远程IPv6地址</ArgTableRow>
</ArgTable>