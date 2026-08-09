# beep

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# beep

**类型：** 命令

使内置扬声器发出蜂鸣声。仅支持带有蜂鸣器的设备。请查看 [mikrotik.com](https://mikrotik.com) 上的设备页面。

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="frequency" typ="num">声音频率，单位为赫兹（Hz）</ArgTableRow>
<ArgTableRow arg="length" typ="time">声音持续时间，单位为秒</ArgTableRow>
</ArgTable>