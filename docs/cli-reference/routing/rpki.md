# Rpki

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/rpki

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="enum">Group assigned to the database.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">RTR server address.</ArgTableRow>
<ArgTableRow arg="port" typ="num">RTR server port.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">VRF table used to bind the connection.</ArgTableRow>
<ArgTableRow arg="preference" typ="num" unset="1">When multiple RTR sources exist, a higher number indicates higher preference. If preference is not configured, RouterOS prefers the lowest remote IP within the group. If remote IPs are equal, RouterOS prefers the lowest remote port.</ArgTableRow>
<ArgTableRow arg="refresh-interval" typ="num" unset="1">Interval in seconds to poll the validator for the newest data.</ArgTableRow>
<ArgTableRow arg="retry-interval" typ="num" unset="1">Interval in seconds to retry after a failed data poll from the validator.</ArgTableRow>
<ArgTableRow arg="expire-interval" typ="num" unset="1">Interval in seconds for which polled data remains valid when no valid update is received from the validator.</ArgTableRow>
</ArgTable>

### routing/rpki/rpki-check

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="origin-as" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>

### routing/rpki/rpki-query

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="exact" typ="switch"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="results" typ="string"></ArgTableRow>
</ArgTable>

### routing/rpki/session

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="group" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (idle | connecting | prepare | loading | sync | error)"></ArgTableRow>
<ArgTableRow arg="version" typ="num"></ArgTableRow>
<ArgTableRow arg="session" typ="num"></ArgTableRow>
<ArgTableRow arg="serial" typ="num"></ArgTableRow>
<ArgTableRow arg="expires" typ="time"></ArgTableRow>
</ArgTable>
