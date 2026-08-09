# radius

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# radius

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="service" typ="ubit (ppp, login, hotspot, wireless, dhcp, ipsec, dot1x)"></ArgTableRow>
<ArgTableRow arg="called-id" typ="string"></ArgTableRow>
<ArgTableRow arg="domain" typ="string"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="authentication-port" typ="num"></ArgTableRow>
<ArgTableRow arg="accounting-port" typ="num"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="radsec-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="accounting-backup" typ="bool"></ArgTableRow>
<ArgTableRow arg="realm" typ="string"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="enum (udp | radsec)"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="require-message-auth" typ="enum (no | yes-for-request-resp)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## radius/incoming

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="accept" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
</ArgTable>

### radius/incoming/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="bad-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="acks" typ="num"></ArgTableRow>
<ArgTableRow arg="naks" typ="num"></ArgTableRow>
</ArgTable>

### radius/incoming/reset-counters

**Type:** Command

## radius/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pending" typ="num"></ArgTableRow>
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="accepts" typ="num"></ArgTableRow>
<ArgTableRow arg="rejects" typ="num"></ArgTableRow>
<ArgTableRow arg="resends" typ="num"></ArgTableRow>
<ArgTableRow arg="timeouts" typ="num"></ArgTableRow>
<ArgTableRow arg="bad-replies" typ="num"></ArgTableRow>
<ArgTableRow arg="last-request-rtt" typ="time"></ArgTableRow>
</ArgTable>

## radius/reset-counters

**Type:** Command
