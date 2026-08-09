# 许可证

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/license

**类型：** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="software-id" typ="string" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="old-software-id" typ="string" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="nlevel" typ="num" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="features" typ="ubit (AP, synchronous, radiolan, wireless, extra-channels, , , )" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="expires-in" typ="time" syscap="nochr"></ArgTableRow>
<ArgTableRow arg="system-id" typ="string" syscap="chr"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (free | p1 | p10 | p-unlimited)" syscap="chr"></ArgTableRow>
<ArgTableRow arg="limited-upgrades" typ="bool" syscap="chr"></ArgTableRow>
<ArgTableRow arg="next-renewal-at" typ="date" syscap="chr"></ArgTableRow>
<ArgTableRow arg="deadline-at" typ="date" syscap="chr"></ArgTableRow>
</ArgTable>

### system/license/generate-new-id

**系统能力：** chr
**类型：** 命令

### system/license/output

**系统能力：** nochr
**类型：** 命令

### system/license/renew

**系统能力：** chr
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="account" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="level" typ="enum (p1 | p10 | p-unlimited)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>