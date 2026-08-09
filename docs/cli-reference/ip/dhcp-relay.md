# Dhcp Relay

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dhcp-relay

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dhcp-server-vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="multi { ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-relay-info" typ="bool"></ArgTableRow>
<ArgTableRow arg="relay-info-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="local-address-as-src-ip" typ="bool"></ArgTableRow>
</ArgTable>

### ip/dhcp-relay/monitor

**Package:** dhcp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="responses" typ="num"></ArgTableRow>
</ArgTable>

### ip/dhcp-relay/reset-counters

**Package:** dhcp
**Type:** Command
