# 脚本

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/script

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="无效"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="owner" typ="字符串"></ArgTableRow>
<ArgTableRow arg="policy" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="dont-require-permissions" typ="布尔"></ArgTableRow>
<ArgTableRow arg="source" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="last-started" typ="日期"></ArgTableRow>
<ArgTableRow arg="run-count" typ="数字"></ArgTableRow>
</ArgTable>

### system/script/environment

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="value" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
</ArgTable>