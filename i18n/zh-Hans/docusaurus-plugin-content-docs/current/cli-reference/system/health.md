# 健康状态

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/health

**适用条件：** !i386
**系统能力：** health
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="state-after-reboot" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="core" typ="num"></ArgTableRow>
<ArgTableRow arg="3.3v" typ="num"></ArgTableRow>
<ArgTableRow arg="5v" typ="num"></ArgTableRow>
<ArgTableRow arg="12v" typ="num"></ArgTableRow>
<ArgTableRow arg="lm87-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="board-temp" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage1" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage2" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage3" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage4" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage5" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage6" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage7" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage8" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage9" typ="num"></ArgTableRow>
<ArgTableRow arg="voltage10" typ="num"></ArgTableRow>
<ArgTableRow arg="temp1" typ="num"></ArgTableRow>
<ArgTableRow arg="temp2" typ="num"></ArgTableRow>
<ArgTableRow arg="temp3" typ="num"></ArgTableRow>
<ArgTableRow arg="fan1" typ="num"></ArgTableRow>
<ArgTableRow arg="fan2" typ="num"></ArgTableRow>
<ArgTableRow arg="fan3" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="bool"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="value" typ="alt { num
, num
, num
, num
, num
, enum (ok | fail | not-present | idle | no-input) { ok:0, fail:1, not-present:2, idle:3, no-input:4 }
, string
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (C | RPM | V | A | W |  | )"></ArgTableRow>
</ArgTable>

### system/health/settings

**适用条件：** !i386, tile
**系统能力：** health-settings
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="fan-full-speed-temp" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fan-target-temp" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fan-min-speed-percent" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="fan-control-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="fan-mode" typ="enum (manual | auto)"></ArgTableRow>
<ArgTableRow arg="use-fan" typ="enum (auxiliary | main)"></ArgTableRow>
<ArgTableRow arg="use-fan2" typ="enum (auxiliary | main)"></ArgTableRow>
<ArgTableRow arg="fan-switch" typ="enum (auto | on | off)"></ArgTableRow>
<ArgTableRow arg="fan-on-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-overtemp-startup-delay" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="active-fan" typ="enum (auxiliary | main | none)"></ArgTableRow>
<ArgTableRow arg="active-fan2" typ="enum (auxiliary | main | none)"></ArgTableRow>
</ArgTable>

#### system/health/settings/detect-fans

**适用条件：** !i386
**类型：** 命令