# 打包

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/packing

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="packing" typ="枚举（无 | 简单 | 压缩头部 | 全部压缩）"></ArgTableRow>
<ArgTableRow arg="unpacking" typ="枚举（无 | 简单 | 压缩头部 | 全部压缩）"></ArgTableRow>
<ArgTableRow arg="aggregated-size" typ="数字"></ArgTableRow>
</ArgTable>