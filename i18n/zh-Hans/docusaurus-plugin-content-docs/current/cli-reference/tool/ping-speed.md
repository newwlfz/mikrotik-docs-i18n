# Ping 速度

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/ping-speed

**条件：** !smips
**软件包：** advanced-tools
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="first-ping-size" typ="num"></ArgTableRow>
<ArgTableRow arg="second-ping-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time-between-pings" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="current" typ="num"></ArgTableRow>
<ArgTableRow arg="average" typ="num"></ArgTableRow>
</ArgTable>