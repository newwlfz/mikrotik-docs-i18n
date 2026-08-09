# 路由

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/route

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
<ArgTableRow arg="A" typ="active">活动</ArgTableRow>
<ArgTableRow arg="c" typ="connect">连接</ArgTableRow>
<ArgTableRow arg="s" typ="static">静态</ArgTableRow>
<ArgTableRow arg="r" typ="rip">RIP</ArgTableRow>
<ArgTableRow arg="b" typ="bgp">BGP</ArgTableRow>
<ArgTableRow arg="o" typ="ospf">OSPF</ArgTableRow>
<ArgTableRow arg="i" typ="is-is">IS-IS</ArgTableRow>
<ArgTableRow arg="d" typ="dhcp">DHCP</ArgTableRow>
<ArgTableRow arg="v" typ="vpn">VPN</ArgTableRow>
<ArgTableRow arg="m" typ="modem">调制解调器</ArgTableRow>
<ArgTableRow arg="y" typ="bgp-mpls-vpn">BGP-MPLS-VPN</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">硬件卸载</ArgTableRow>
<ArgTableRow arg="+" typ="ecmp">ECMP</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="dst-address" typ="地址 (标志=4/)"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="枚举"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="地址 (标志=4)" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="地址 (标志=46ivL)" unset="1"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="开关"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="枚举 (none | arp | ping | bfd)" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="数值" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="数值" unset="1"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="数值" unset="1"></ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="接口枚举" unset="1"></ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="布尔值" syscap="crs_prestera"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="immediate-gw" typ="多值 { 地址 (标志=46i)
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="地址 (标志=4iv)"></ArgTableRow>
</ArgTable>

### ip/route/check

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-ip" typ="IP地址"></ArgTableRow>
<ArgTableRow arg="dst-ip" typ="IP地址"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="字符串"></ArgTableRow>
<ArgTableRow arg="interface" typ="接口枚举"></ArgTableRow>
<ArgTableRow arg="nexthop" typ="IP地址"></ArgTableRow>
</ArgTable>