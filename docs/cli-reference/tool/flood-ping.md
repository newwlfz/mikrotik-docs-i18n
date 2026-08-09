# Flood Ping

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/flood-ping

**Conditions:** !smips
**Package:** advanced-tools
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="sent" typ="num"></ArgTableRow>
<ArgTableRow arg="received" typ="num"></ArgTableRow>
<ArgTableRow arg="min-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="avg-rtt" typ="time"></ArgTableRow>
<ArgTableRow arg="max-rtt" typ="time"></ArgTableRow>
</ArgTable>
