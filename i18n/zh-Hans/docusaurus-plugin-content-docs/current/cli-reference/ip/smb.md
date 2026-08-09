# SMB

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/smb

**条件：** !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="枚举 (no | auto | yes)"></ArgTableRow>
<ArgTableRow arg="domain" typ="字符串"></ArgTableRow>
<ArgTableRow arg="comment" typ="字符串"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="多值 { 数组ID, 接口枚举 { all:0 } { all:0 }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="字符串"></ArgTableRow>
</ArgTable>

### ip/smb/shares

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="动态">动态</ArgTableRow>
<ArgTableRow arg="X" typ="禁用">禁用</ArgTableRow>
<ArgTableRow arg="*" typ="默认">默认</ArgTableRow>
<ArgTableRow arg="r" typ="只读">只读</ArgTableRow>
<ArgTableRow arg="c" typ="需要加密">需要加密</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串" mandatory="1"></ArgTableRow>
<ArgTableRow arg="directory" typ="文件"></ArgTableRow>
<ArgTableRow arg="read-only" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="require-encryption" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="valid-users" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="invalid-users" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
</ArgTable>

### ip/smb/users

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="动态">动态</ArgTableRow>
<ArgTableRow arg="X" typ="禁用">禁用</ArgTableRow>
<ArgTableRow arg="*" typ="默认">默认</ArgTableRow>
<ArgTableRow arg="r" typ="只读">只读</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="read-only" typ="布尔值"></ArgTableRow>
</ArgTable>