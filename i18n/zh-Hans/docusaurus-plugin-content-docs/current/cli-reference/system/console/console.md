# 控制台

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/console

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="默认"></ArgTableRow>
<ArgTableRow arg="X" typ="禁用"></ArgTableRow>
<ArgTableRow arg="W" typ="卡住"></ArgTableRow>
<ArgTableRow arg="U" typ="使用中"></ArgTableRow>
<ArgTableRow arg="F" typ="空闲"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="枚举"></ArgTableRow>
<ArgTableRow arg="channel" typ="数字"></ArgTableRow>
<ArgTableRow arg="term" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="vcno" typ="数字"></ArgTableRow>
</ArgTable>