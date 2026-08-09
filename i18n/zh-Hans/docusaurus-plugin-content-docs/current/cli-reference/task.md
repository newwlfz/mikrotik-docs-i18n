# 任务

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# 任务

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="T" typ="terminated">已终止</ArgTableRow>
<ArgTableRow arg="C" typ="current">当前</ArgTableRow>
<ArgTableRow arg="A" typ="autosave">自动保存</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="term-pid" typ="num"></ArgTableRow>
<ArgTableRow arg="task-id" typ="num"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="source" typ="string"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="save-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="append" typ="switch"></ArgTableRow>
</ArgTable>

## 任务/添加

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="source" typ="string">应在后台执行的命令</ArgTableRow>
<ArgTableRow arg="switch-to" typ="switch">立即切换到后台视图</ArgTableRow>
<ArgTableRow arg="append" typ="switch">将输出追加到文件</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">输出的默认文件名</ArgTableRow>
<ArgTableRow arg="save-interval" typ="time">设置文件名时的自动保存间隔</ArgTableRow>
<ArgTableRow arg="max-lines" typ="num">最大缓冲区行数</ArgTableRow>
<ArgTableRow arg="save-timestamp" typ="switch">在保存的文件中添加时间戳</ArgTableRow>
<ArgTableRow arg="no-header-paging" typ="switch">不将页眉分页到输出</ArgTableRow>
<ArgTableRow arg="max-size" typ="num">最大保存文件大小</ArgTableRow>
</ArgTable>

## 任务/下一个

**类型：** 命令

## 任务/终止

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="id" typ="num"></ArgTableRow>
</ArgTable>