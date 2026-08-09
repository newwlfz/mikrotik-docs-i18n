# L2TP 服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/l2tp-server

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

### interface/l2tp-server/monitor

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

### interface/l2tp-server/server

**软件包：** ppp
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool">启用</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大MTU</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大MRU</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">MRRU</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">认证方式</ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)">保活超时</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">最大会话数</ArgTableRow>
<ArgTableRow arg="default-profile" typ="enum">默认配置文件</ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="enum (no | yes | required)">使用IPsec</ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string">IPsec密钥</ArgTableRow>
<ArgTableRow arg="caller-id-type" typ="enum (ip-address | number)">呼叫方ID类型</ArgTableRow>
<ArgTableRow arg="one-session-per-host" typ="bool">每主机单会话</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">允许快速路径</ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string">L2TPv3电路ID</ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes)">L2TPv3 Cookie长度</ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1)">L2TPv3摘要哈希</ArgTableRow>
<ArgTableRow arg="l2tpv3-ether-interface-list" typ="enum">L2TPv3以太网接口列表</ArgTableRow>
<ArgTableRow arg="accept-pseudowire-type" typ="enum (all | ether | ppp)">接受伪线类型</ArgTableRow>
<ArgTableRow arg="accept-proto-version" typ="enum (all | l2tpv2 | l2tpv3)">接受协议版本</ArgTableRow>
</ArgTable>