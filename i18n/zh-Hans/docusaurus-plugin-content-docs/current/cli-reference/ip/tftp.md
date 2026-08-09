# TFTP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/tftp

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ip-addresses" typ="对象 { 备选 { ip6Prefix
, ipRange
 } { ip6Prefix
, ipRange
 }
 }"></ArgTableRow>
<ArgTableRow arg="req-filename" typ="字符串"></ArgTableRow>
<ArgTableRow arg="real-filename" typ="字符串"></ArgTableRow>
<ArgTableRow arg="allow" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="read-only" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="allow-rollover" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="allow-overwrite" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="reading-window-size" typ="备选 { 枚举 (none | pipelining) { none:0, pipelining:tftpd::WINDOW_PIPELINING }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="hits" typ="数值"></ArgTableRow>
</ArgTable>

### ip/tftp/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="max-block-size" typ="枚举 (512 | 1454 | 4096 | 8192)">允许协商的最大块大小</ArgTableRow>
</ArgTable>