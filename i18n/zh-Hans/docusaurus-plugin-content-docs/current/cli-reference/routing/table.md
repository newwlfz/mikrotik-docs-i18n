# 表格

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/table

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="动态">动态</ArgTableRow>
<ArgTableRow arg="X" typ="禁用">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="无效">无效</ArgTableRow>
<ArgTableRow arg="U" typ="已使用">已使用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串">路由表的名称。</ArgTableRow>
<ArgTableRow arg="fib" typ="开关" unset="1">指示此表中的路由是否将安装到 [FIB](../../user-guides/routing-and-networking-protocols/routing-decision.md#forwarding-information-base) 中的标志。</ArgTableRow>
</ArgTable>