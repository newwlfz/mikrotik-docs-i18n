# 带宽服务器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/bandwidth-server

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authenticate" typ="bool"></ArgTableRow>
<ArgTableRow arg="allocate-udp-ports-from" typ="num">UDP端口范围的起始值</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">最大同时测试数量</ArgTableRow>
<ArgTableRow arg="allowed-addresses4" typ="object { ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="allowed-addresses6" typ="object { ip6Prefix
 }"></ArgTableRow>
</ArgTable>

### tool/bandwidth-server/session

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="client" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp)"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | send | both)"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="random-data" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-current" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-current" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-size" typ="range"></ArgTableRow>
<ArgTableRow arg="rx-size" typ="range"></ArgTableRow>
<ArgTableRow arg="tcp-connection-count" typ="num"></ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num"></ArgTableRow>
</ArgTable>