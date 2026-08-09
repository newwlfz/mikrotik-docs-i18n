# 串行接口

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/serial-interface/read

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="enum">端口列表中的端口名称</ArgTableRow>
<ArgTableRow arg="time" typ="time">串行终端访问的超时时间（捕获模式）</ArgTableRow>
<ArgTableRow arg="size" typ="num">从串行终端读取的最大字节数（捕获模式）</ArgTableRow>
<ArgTableRow arg="until" typ="string">从串行终端读取，直到出现提供的字符序列（捕获模式）</ArgTableRow>
<ArgTableRow arg="as-string" typ="switch">不将输出解释为控制台值（在捕获模式下）</ArgTableRow>
</ArgTable>

### system/serial-interface/serial-terminal

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="enum">端口列表中的端口名称</ArgTableRow>
<ArgTableRow arg="channel" typ="num">将使用的端口通道（默认为 0）</ArgTableRow>
<ArgTableRow arg="write" typ="string">以非交互方式将提供的值写入串行终端</ArgTableRow>
</ArgTable>

### system/serial-interface/start

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="enum">端口列表中的端口名称</ArgTableRow>
<ArgTableRow arg="channel" typ="num">将使用的端口通道（默认为 0）</ArgTableRow>
</ArgTable>

### system/serial-interface/stop

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="enum">端口列表中的端口名称</ArgTableRow>
<ArgTableRow arg="channel" typ="num">将使用的端口通道（默认为 0）</ArgTableRow>
</ArgTable>

### system/serial-interface/write

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="port" typ="enum">端口列表中的端口名称</ArgTableRow>
<ArgTableRow arg="data" typ="string">以非交互方式将提供的值写入串行终端</ArgTableRow>
</ArgTable>