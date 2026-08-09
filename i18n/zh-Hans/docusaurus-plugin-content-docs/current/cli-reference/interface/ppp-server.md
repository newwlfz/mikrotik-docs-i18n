# PPP 服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ppp-server

**软件包：** ppp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num">最大MTU</ArgTableRow>
<ArgTableRow arg="max-mru" typ="num">最大MRU</ArgTableRow>
<ArgTableRow arg="mrru" typ="num">MRRU</ArgTableRow>
<ArgTableRow arg="port" typ="enum">端口</ArgTableRow>
<ArgTableRow arg="data-channel" typ="num">数据通道</ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)">认证方式</ArgTableRow>
<ArgTableRow arg="profile" typ="enum">配置文件</ArgTableRow>
<ArgTableRow arg="modem-init" typ="string">调制解调器初始化</ArgTableRow>
<ArgTableRow arg="ring-count" typ="num">振铃次数</ArgTableRow>
<ArgTableRow arg="null-modem" typ="bool">无调制解调器</ArgTableRow>
</ArgTable>

### interface/ppp-server/monitor

**软件包：** ppp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string">状态</ArgTableRow>
<ArgTableRow arg="uptime" typ="time">运行时间</ArgTableRow>
<ArgTableRow arg="user" typ="string">用户</ArgTableRow>
<ArgTableRow arg="caller-id" typ="string">主叫号码</ArgTableRow>
<ArgTableRow arg="encoding" typ="string">编码方式</ArgTableRow>
<ArgTableRow arg="connect-speed" typ="num">连接速率</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">MTU</ArgTableRow>
<ArgTableRow arg="mru" typ="num">MRU</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">本地地址</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr">远端地址</ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr">本地IPv6地址</ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr">远端IPv6地址</ArgTableRow>
</ArgTable>