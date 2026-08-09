# Macvlan

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/macvlan

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC地址</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">最大传输单元</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">仅支持具有MAC地址的接口用于macvlan</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (private | bridge)">在桥接模式下，macvlan接口允许相互通信</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">地址解析协议</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }">ARP超时时间</ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on)">环路保护</ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time">环路保护发送间隔</ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time">环路保护禁用时间</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="l2mtu" typ="num">二层最大传输单元</ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled)">环路保护状态</ArgTableRow>
</ArgTable>