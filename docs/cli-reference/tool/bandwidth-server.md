# Bandwidth Server

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/bandwidth-server

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="authenticate" typ="bool"></ArgTableRow>
<ArgTableRow arg="allocate-udp-ports-from" typ="num">Beginning of UDP port range</ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num">Maximal simultaneous test count</ArgTableRow>
<ArgTableRow arg="allowed-addresses4" typ="object { ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="allowed-addresses6" typ="object { ip6Prefix
 }"></ArgTableRow>
</ArgTable>

### tool/bandwidth-server/session

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="client" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | tcp)"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (receive | send | both)"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="random-data" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-current" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-10-second-average" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-total-average" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-current" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-10-second-average" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-total-average" typ="num"></ArgTableRow>
<ArgTableRow arg="lost-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-size" typ="range"></ArgTableRow>
<ArgTableRow arg="rx-size" typ="range"></ArgTableRow>
<ArgTableRow arg="tcp-connection-count" typ="num"></ArgTableRow>
<ArgTableRow arg="local-tx-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="remote-tx-speed" typ="num"></ArgTableRow>
</ArgTable>
