# Profile

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/profile

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="cpu" typ="枚举 (all | total)" syscap="smp"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="cpu" typ="数字" syscap="smp"></ArgTableRow>
<ArgTableRow arg="usage" typ="数字"></ArgTableRow>
</ArgTable>