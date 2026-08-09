# lcd

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# lcd

**适用条件：** !smips
**系统能力：** lcd
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="touch-screen" typ="bool"></ArgTableRow>
<ArgTableRow arg="backlight-timeout" typ="alt { enum (never) { never:0 }
, time [30s .. 2h]
 }"></ArgTableRow>
<ArgTableRow arg="read-only-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="time-interval" typ="enum (min | hour | daily | weekly)"></ArgTableRow>
<ArgTableRow arg="default-screen" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="color-scheme" typ="enum (dark | light)"></ArgTableRow>
<ArgTableRow arg="flip-screen" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/backlight

**适用条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="state" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/interface

**适用条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="displayed">已显示</ArgTableRow>
<ArgTableRow arg="W" typ="default-wireless">默认无线</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="max-speed" typ="num" mandatory="1"></ArgTableRow>
</ArgTable>

### lcd/interface/default-wireless

**适用条件：** !smips
**类型：** 命令

### lcd/interface/display

**适用条件：** !smips
**类型：** 命令

### lcd/interface/pages

**适用条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>

## lcd/pin

**适用条件：** !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="pin-number" typ="string"></ArgTableRow>
<ArgTableRow arg="hide-pin-number" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/recalibrate

**适用条件：** !smips
**类型：** 命令

## lcd/screen

**适用条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

## lcd/show

**适用条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="screen" typ="enum ()"></ArgTableRow>
</ArgTable>

## lcd/take-screenshot

**适用条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
</ArgTable>