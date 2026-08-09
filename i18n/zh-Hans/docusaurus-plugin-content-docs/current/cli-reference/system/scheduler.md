# 调度器

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/scheduler

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="start-date" typ="date"></ArgTableRow>
<ArgTableRow arg="start-time" typ="alt { enum (startup) { startup:0xffffffff }
, date
 }"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="run-count" typ="num"></ArgTableRow>
<ArgTableRow arg="next-run" typ="date"></ArgTableRow>
</ArgTable>