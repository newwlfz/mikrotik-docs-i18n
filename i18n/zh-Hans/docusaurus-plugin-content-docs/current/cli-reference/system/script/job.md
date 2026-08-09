# 任务

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/script/job

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="started" typ="日期"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举（命令 | 登录 | API登录）"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="script" typ="枚举"></ArgTableRow>
<ArgTableRow arg="owner" typ="字符串"></ArgTableRow>
<ArgTableRow arg="policy" typ="多选 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="数字"></ArgTableRow>
<ArgTableRow arg="trace" typ="字符串"></ArgTableRow>
</ArgTable>