# 检测互联网

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/detect-internet

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="detect-interface-list" typ="枚举"></ArgTableRow>
<ArgTableRow arg="lan-interface-list" typ="枚举"></ArgTableRow>
<ArgTableRow arg="wan-interface-list" typ="枚举"></ArgTableRow>
<ArgTableRow arg="internet-interface-list" typ="枚举"></ArgTableRow>
<ArgTableRow arg="request-interval" typ="时间"></ArgTableRow>
</ArgTable>

### interface/detect-internet/state

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="接口枚举"></ArgTableRow>
<ArgTableRow arg="state" typ="枚举 (无链路 | 未知 | 局域网 | 广域网 | 互联网 | 从属)"></ArgTableRow>
<ArgTableRow arg="state-change-time" typ="日期"></ArgTableRow>
<ArgTableRow arg="cloud-rtt" typ="时间"></ArgTableRow>
</ArgTable>