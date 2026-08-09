# 历史记录

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/history

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="U" typ="可撤销"></ArgTableRow>
<ArgTableRow arg="R" typ="可重做"></ArgTableRow>
<ArgTableRow arg="F" typ="浮动撤销"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="redo" typ="配置"></ArgTableRow>
<ArgTableRow arg="undo" typ="配置"></ArgTableRow>
<ArgTableRow arg="action" typ="字符串"></ArgTableRow>
<ArgTableRow arg="by" typ="字符串"></ArgTableRow>
<ArgTableRow arg="policy" typ="多选 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="time" typ="日期"></ArgTableRow>
<ArgTableRow arg="trace" typ="字符串"></ArgTableRow>
</ArgTable>