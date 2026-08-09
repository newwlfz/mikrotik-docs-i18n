# Vrrp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/vrrp

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="G" typ="grp-authority">组权威</ArgTableRow>
<ArgTableRow arg="g" typ="grp-member">组成员</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="M" typ="master">主设备</ArgTableRow>
<ArgTableRow arg="B" typ="backup">备份设备</ArgTableRow>
<ArgTableRow arg="F" typ="failure">故障</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group-master" typ="iface_enum { :0, none:0, self:vrrp::LOOPBACK_ID }">已弃用</ArgTableRow>
<ArgTableRow arg="group-authority" typ="iface_enum { :0, none:0, self:vrrp::LOOPBACK_ID }">控制整个组的VRRP接口权威</ArgTableRow>
<ArgTableRow arg="vrid" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="preemption-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication" typ="enum (none | simple | ah)"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="on-backup" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-master" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="on-fail" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3)"></ArgTableRow>
<ArgTableRow arg="v3-protocol" typ="enum (ipv4 | ipv6)"></ArgTableRow>
<ArgTableRow arg="sync-connection-tracking" typ="bool">主备设备之间的连接跟踪数据交换</ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr {  }">强制指定Conntrack数据的发送方或接收方地址</ArgTableRow>
<ArgTableRow arg="connection-tracking-mode" typ="enum (passive-active | active-active)"></ArgTableRow>
<ArgTableRow arg="connection-tracking-port" typ="num {  }">用于Conntrack数据同步的端口</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>