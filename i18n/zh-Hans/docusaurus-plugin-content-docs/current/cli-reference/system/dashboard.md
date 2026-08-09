# 仪表盘（Dashboard）

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/dashboard/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="uplink-interfaces" typ="multi { array-id, iface_enum { ,  } { ,  }
 }" unset="1"></ArgTableRow>
</ArgTable>

### system/dashboard/show

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-usage" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="hdd-usage" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ether" typ="super { num
, /num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi" typ="super { num
, /num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="total-bw" typ="super { num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="uplink-bw" typ="super { num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="ether-bw" typ="super { num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="wifi-bw" typ="super { num
, /num
 }"></ArgTableRow>
<ArgTableRow arg="lte-bw" typ="super { num
, /num
 }"></ArgTableRow>
</ArgTable>