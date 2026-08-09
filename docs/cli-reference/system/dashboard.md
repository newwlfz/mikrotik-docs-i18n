# Dashboard

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/dashboard/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="uplink-interfaces" typ="multi { array-id, iface_enum { ,  } { ,  }
 }" unset="1"></ArgTableRow>
</ArgTable>

### system/dashboard/show

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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
