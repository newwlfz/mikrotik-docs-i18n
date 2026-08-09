# Ping Speed

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/ping-speed

**Conditions:** !smips
**Package:** advanced-tools
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="first-ping-size" typ="num"></ArgTableRow>
<ArgTableRow arg="second-ping-size" typ="num"></ArgTableRow>
<ArgTableRow arg="time-between-pings" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="current" typ="num"></ArgTableRow>
<ArgTableRow arg="average" typ="num"></ArgTableRow>
</ArgTable>
