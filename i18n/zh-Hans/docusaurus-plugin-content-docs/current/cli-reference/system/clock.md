# 时钟

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/clock

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="date" typ="date"></ArgTableRow>
<ArgTableRow arg="time-zone-autodetect" typ="bool"></ArgTableRow>
<ArgTableRow arg="time-zone-name" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="gmt-offset" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-active" typ="bool"></ArgTableRow>
</ArgTable>

### system/clock/manual

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="time-zone" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-delta" typ="timezone"></ArgTableRow>
<ArgTableRow arg="dst-start" typ="date"></ArgTableRow>
<ArgTableRow arg="dst-end" typ="date"></ArgTableRow>
</ArgTable>