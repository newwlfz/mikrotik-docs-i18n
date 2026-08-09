# 带宽测试

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/bandwidth-test

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="地址（标志=46viD）"></ArgTableRow>
<ArgTableRow arg="protocol" typ="枚举（udp | tcp）"></ArgTableRow>
<ArgTableRow arg="local-udp-tx-size" typ="范围"></ArgTableRow>
<ArgTableRow arg="remote-udp-tx-size" typ="范围"></ArgTableRow>
<ArgTableRow arg="direction" typ="枚举（receive | transmit | both）"></ArgTableRow>
<ArgTableRow arg="connection-count" typ="数值"></ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="数值"></ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="数值"></ArgTableRow>
<ArgTableRow arg="user" typ="字符串"></ArgTableRow>
<ArgTableRow arg="password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="duration" typ="时间"></ArgTableRow>
<ArgTableRow arg="random-data" typ="布尔值"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="枚举（connecting | can not start test | can not connect | remote is busy | test unsupported | running | disconnected | authentication failed | done testing）"></ArgTableRow>
<ArgTableRow arg="duration" typ="时间"></ArgTableRow>
<ArgTableRow arg="tx-current" typ="数值"></ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="数值"></ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="数值"></ArgTableRow>
<ArgTableRow arg="rx-current" typ="数值"></ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="数值"></ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="数值"></ArgTableRow>
<ArgTableRow arg="lost-packets" typ="数值"></ArgTableRow>
<ArgTableRow arg="random-data" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="direction" typ="枚举（receive | transmit | both）"></ArgTableRow>
<ArgTableRow arg="tx-size" typ="范围"></ArgTableRow>
<ArgTableRow arg="rx-size" typ="范围"></ArgTableRow>
<ArgTableRow arg="connection-count" typ="数值"></ArgTableRow>
<ArgTableRow arg="local-cpu-load" typ="数值"></ArgTableRow>
<ArgTableRow arg="remote-cpu-load" typ="数值"></ArgTableRow>
<ArgTableRow arg="tcp-info" typ="多值 { 字符串
 }"></ArgTableRow>
</ArgTable>