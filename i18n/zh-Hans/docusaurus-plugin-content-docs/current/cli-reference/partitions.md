# 分区

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# 分区

**条件：** !i386, !smips, !mmips
**系统能力：** partitions
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="A" typ="active">活动</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="fallback-to" typ="enum (etherboot | next)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
</ArgTable>

## 分区/激活

**条件：** !i386, !smips, !mmips
**类型：** 命令

## 分区/复制到

**条件：** !i386, !smips, !mmips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## 分区/重新分区

**条件：** !i386, !smips, !mmips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="partitions" typ="num"></ArgTableRow>
</ArgTable>

## 分区/从配置恢复

**条件：** !i386, !smips, !mmips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## 分区/保存配置到

**条件：** !i386, !smips, !mmips
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>