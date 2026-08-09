# PPTP 服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/pptp-server

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">用户</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="mru" typ="num">最大接收单元</ArgTableRow>
<ArgTableRow arg="client-address" typ="string">客户端地址</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">运行时间</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">编码</ArgTableRow>
</ArgTable>

### interface/pptp-server/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string">状态</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">运行时间</ArgTableRow>
<ArgTableRow arg="user" typ="string">用户</ArgTableRow>
<ArgTableRow arg="caller-id" typ="string">呼叫方ID</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">编码</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="mru" typ="num">最大接收单元</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">本地地址</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">远程地址</ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr">本地IPv6地址</ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr">远程IPv6地址</ArgTableRow>
</ArgTable>

### interface/pptp-server/server

**软件包：** ppp
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool">启用</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大接收单元</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">最大接收重建单元</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">认证方式</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)">保活超时</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">默认配置文件</ArgTableRow>
</ArgTable>