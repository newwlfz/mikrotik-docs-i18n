# NAT-PMP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/nat-pmp

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="布尔值"></ArgTableRow>
</ArgTable>

### ip/nat-pmp/interfaces

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="禁用">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="动态">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="接口枚举" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举（外部 | 内部）" mandatory="1"></ArgTableRow>
<ArgTableRow arg="forced-ip" typ="超级 { IP地址
 }"></ArgTableRow>
</ArgTable>