# Scheduler

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/scheduler

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="start-date" typ="date"></ArgTableRow>
<ArgTableRow arg="start-time" typ="alt { enum (startup) { startup:0xffffffff }
, date
 }"></ArgTableRow>
<ArgTableRow arg="interval" typ="time"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="policy" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="run-count" typ="num"></ArgTableRow>
<ArgTableRow arg="next-run" typ="date"></ArgTableRow>
</ArgTable>
