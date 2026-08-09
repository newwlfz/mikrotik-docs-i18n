# Apptraffic（应用流量）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### tool/apptraffic/stats

**适用条件：** !mmips, !powerpc, !smips, !mipsel
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="说明">
<ArgTableRow arg="application" typ="string"></ArgTableRow>
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-out" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-in" typ="num"></ArgTableRow>
</ArgTable>

#### tool/apptraffic/stats/categories

**适用条件：** !mmips, !powerpc, !smips, !mipsel
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="说明">
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="bytes-out" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes-in" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-out" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-in" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-out" typ="num"></ArgTableRow>
<ArgTableRow arg="percent-in" typ="num"></ArgTableRow>
</ArgTable>

#### tool/apptraffic/stats/clear

**适用条件：** !mmips, !powerpc, !smips, !mipsel
**类型：** 命令