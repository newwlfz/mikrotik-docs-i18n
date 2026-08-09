# port

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# port

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="baud-rate" typ="枚举 (自动 | 50 | 75 | 110 | 134 | 150 | 200 | 300 | 600 | 1200 | 1800 | 2400 | 4800 | 9600 | 19200 | 38400 | 57600 | 115200 | 230400 | 460800 | 500000 | 576000 | 921600 | 1000000 | 1152000 | 1500000 | 2000000 | 2500000 | 3000000 | 3500000 | 4000000)"></ArgTableRow>
<ArgTableRow arg="data-bits" typ="枚举 (7 | 8)"></ArgTableRow>
<ArgTableRow arg="parity" typ="枚举 (无 | 奇校验 | 偶校验)"></ArgTableRow>
<ArgTableRow arg="stop-bits" typ="枚举 (1 | 2)"></ArgTableRow>
<ArgTableRow arg="flow-control" typ="枚举 (xon-xoff | 硬件 | 无)"></ArgTableRow>
<ArgTableRow arg="rts" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="dtr" typ="布尔值"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="used-by" typ="字符串"></ArgTableRow>
<ArgTableRow arg="device" typ="字符串"></ArgTableRow>
<ArgTableRow arg="channels" typ="数字"></ArgTableRow>
<ArgTableRow arg="line-state" typ="多值 { array-id, 枚举 (dtr | rts | cts | dcd | ri | dsr) { dtr:1, rts:2, cts:5, dcd:6, ri:7, dsr:8 }
 }"></ArgTableRow>
</ArgTable>

## port/remote-access

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="A" typ="active">已激活</ArgTableRow>
<ArgTableRow arg="B" typ="busy">忙碌</ArgTableRow>
<ArgTableRow arg="L" typ="logging-active">日志记录已激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="枚举"></ArgTableRow>
<ArgTableRow arg="channel" typ="数字"></ArgTableRow>
<ArgTableRow arg="remote-addresses" typ="对象 { 超级 { 地址 (标志=46/)
, [ -地址 (标志=46)]
, [ @数字]
 } { 地址 (标志=46/)
, [ -地址 (标志=46)]
, [ @数字]
 }
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="替代 { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="ip-port" typ="数字"></ArgTableRow>
<ArgTableRow arg="protocol" typ="枚举 (tcp-server | rfc2217 | tcp-client | udp)"></ArgTableRow>
<ArgTableRow arg="log-file" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-peer" typ="ip6Addr {  }"></ArgTableRow>
<ArgTableRow arg="active-peer-port" typ="数字 {  }"></ArgTableRow>
</ArgTable>