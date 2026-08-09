# Simple

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## queue/simple

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="target" typ="object { alt { iface_enum
, alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 } { iface_enum
, alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dst" typ="alt { ipPrefix
, ip6Prefix
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="packet-marks" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="queue" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="limit-at" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="max-limit" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-limit" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-threshold" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="burst-time" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="bucket-size" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="total-queue" typ="enum"></ArgTableRow>
<ArgTableRow arg="total-limit-at" typ="num"></ArgTableRow>
<ArgTableRow arg="total-max-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="total-burst-time" typ="time"></ArgTableRow>
<ArgTableRow arg="total-bucket-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time" typ="super { !
, time
, -time
, ,ubit (sun, mon, tue, wed, thu, fri, sat) { sun, mon, tue, wed, thu, fri, sat }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="dropped" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-dropped" typ="num"></ArgTableRow>
<ArgTableRow arg="rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="packet-rate" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-packet-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-packets" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-queued-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="queued-bytes" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-queued-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="pcq-queues" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="total-pcq-queues" typ="num"></ArgTableRow>
</ArgTable>

### queue/simple/reset-counters

**Type:** Command

### queue/simple/reset-counters-all

**Type:** Command
