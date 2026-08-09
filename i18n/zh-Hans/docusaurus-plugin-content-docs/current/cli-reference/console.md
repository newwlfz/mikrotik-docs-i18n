# console

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# console

**类型：** 目录

## console/inspect

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="request" typ="ubit (self, child, completion, highlight, syntax, error)"></ArgTableRow>
<ArgTableRow arg="path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="input" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="enum (self | child | completion | highlight | syntax | error)"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="node-type" typ="enum (path | dir | cmd | arg)"></ArgTableRow>
<ArgTableRow arg="completion" typ="string"></ArgTableRow>
<ArgTableRow arg="style" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="preference" typ="num"></ArgTableRow>
<ArgTableRow arg="show" typ="bool"></ArgTableRow>
<ArgTableRow arg="highlight" typ="multi { , enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="symbol" typ="string"></ArgTableRow>
<ArgTableRow arg="symbol-type" typ="enum (collection | explanation | definition)"></ArgTableRow>
<ArgTableRow arg="nested" typ="num"></ArgTableRow>
<ArgTableRow arg="nonorm" typ="bool"></ArgTableRow>
<ArgTableRow arg="text" typ="string"></ArgTableRow>
</ArgTable>

## console/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="sanitize-names" typ="bool">将文件和脚本名称中的保留字符替换为下划线</ArgTableRow>
<ArgTableRow arg="log-script-errors" typ="bool">将后台脚本失败写入日志</ArgTableRow>
<ArgTableRow arg="tab-width" typ="num">全屏编辑器中的默认制表符宽度</ArgTableRow>
</ArgTable>