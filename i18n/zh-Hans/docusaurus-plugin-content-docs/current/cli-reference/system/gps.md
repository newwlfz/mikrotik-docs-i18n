# GPS

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/gps

**适用条件：** mmips
**软件包：** gps
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { enum (none) { none:nv::BADID }
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="init-channel" typ="num"></ArgTableRow>
<ArgTableRow arg="init-string" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="set-system-time" typ="bool"></ArgTableRow>
<ArgTableRow arg="coordinate-format" typ="enum (dms | dd | ddmm)"></ArgTableRow>
<ArgTableRow arg="gps-antenna-select" typ="enum (internal | external)" syscap="rb-gps"></ArgTableRow>
</ArgTable>

### system/gps/monitor

**软件包：** gps
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="date-and-time" typ="date"></ArgTableRow>
<ArgTableRow arg="latitude" typ="string"></ArgTableRow>
<ArgTableRow arg="longitude" typ="string"></ArgTableRow>
<ArgTableRow arg="altitude" typ="string"></ArgTableRow>
<ArgTableRow arg="speed" typ="string"></ArgTableRow>
<ArgTableRow arg="destination-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="true-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="magnetic-bearing" typ="string"></ArgTableRow>
<ArgTableRow arg="valid" typ="bool"></ArgTableRow>
<ArgTableRow arg="satellites" typ="num"></ArgTableRow>
<ArgTableRow arg="fix-quality" typ="num"></ArgTableRow>
<ArgTableRow arg="horizontal-dilution" typ="num"></ArgTableRow>
<ArgTableRow arg="data-age" typ="alt { enum (never) { never:0 }
, time
 }"></ArgTableRow>
</ArgTable>