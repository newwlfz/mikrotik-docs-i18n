# Swos

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/swos

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**系统能力：** swos
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address-acquisition-mode" typ="枚举 (dhcp-with-fallback | static | dhcp-only)"></ArgTableRow>
<ArgTableRow arg="static-ip-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="字符串"></ArgTableRow>
<ArgTableRow arg="allow-from" typ="复合 { ,  }"></ArgTableRow>
<ArgTableRow arg="allow-from-ports" typ="ubit (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32)"></ArgTableRow>
<ArgTableRow arg="allow-from-vlan" typ="数字"></ArgTableRow>
</ArgTable>

### system/swos/load-config

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file" typ="文件 {  }"></ArgTableRow>
</ArgTable>

### system/swos/password

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="new-password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="confirm-new-password" typ="字符串"></ArgTableRow>
</ArgTable>

### system/swos/reset-config

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**类型：** 命令

### system/swos/save-config

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file" typ="字符串"></ArgTableRow>
</ArgTable>

### system/swos/upgrade

**条件：** !i386, !mmips, !powerpc, !tile, !smips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="version" typ="字符串"></ArgTableRow>
<ArgTableRow arg="status" typ="字符串"></ArgTableRow>
</ArgTable>