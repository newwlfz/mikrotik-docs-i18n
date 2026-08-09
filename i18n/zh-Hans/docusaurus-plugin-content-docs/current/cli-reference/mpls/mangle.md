# Mangle

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/mangle

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="chain" typ="ubit (forward, output)" unset="1"></ArgTableRow>
<ArgTableRow arg="exp" typ="ubit (0, 1, 2, 3, 4, 5, 6, 7)" unset="1"></ArgTableRow>
<ArgTableRow arg="set-exp" typ="enum (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7)" unset="1"></ArgTableRow>
<ArgTableRow arg="set-mark" typ="enum" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
</ArgTable>

### mpls/mangle/reset-counters

**类型：** 命令

### mpls/mangle/reset-counters-all

**类型：** 命令