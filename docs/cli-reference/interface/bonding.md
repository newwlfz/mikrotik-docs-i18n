# Bonding

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/bonding

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="forced-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="slaves" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb)"></ArgTableRow>
<ArgTableRow arg="primary" typ="iface_enum { none:0 }"></ArgTableRow>
<ArgTableRow arg="link-monitoring" typ="enum (none | arp | mii)"></ArgTableRow>
<ArgTableRow arg="arp-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="arp-ip-targets" typ="multi { array-id, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="mii-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="down-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="up-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="lacp-rate" typ="enum (30secs | 1sec)"></ArgTableRow>
<ArgTableRow arg="transmit-hash-policy" typ="enum (layer-2 | layer-3-and-4 | layer-2-and-3 | encap-2-and-3 | encap-3-and-4)"></ArgTableRow>
<ArgTableRow arg="min-links" typ="num"></ArgTableRow>
<ArgTableRow arg="mlag-id" typ="num"></ArgTableRow>
<ArgTableRow arg="lacp-user-key" typ="num"></ArgTableRow>
<ArgTableRow arg="lacp-mode" typ="enum (passive | active)"></ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>

### interface/bonding/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum (balance-rr | active-backup | balance-xor | broadcast | 802.3ad | balance-tlb | balance-alb)"></ArgTableRow>
<ArgTableRow arg="active-ports" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="inactive-ports" typ="multi { array-id, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="lacp-system-id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="lacp-system-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="lacp-partner-system-id" typ="macAddr"></ArgTableRow>
</ArgTable>

### interface/bonding/monitor-slaves

**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="P" typ="partner">partner</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="bond" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="once" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="key" typ="num"></ArgTableRow>
<ArgTableRow arg="flags" typ="string"></ArgTableRow>
<ArgTableRow arg="partner-sys-id" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="partner-sys-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-key" typ="num"></ArgTableRow>
<ArgTableRow arg="partner-flags" typ="string"></ArgTableRow>
</ArgTable>
