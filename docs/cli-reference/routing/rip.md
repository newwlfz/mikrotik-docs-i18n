# Rip

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/rip

**Type:** Directory

### routing/rip/instance

**Type:** Directory

The maximum metric of a RIP route is 15. A metric higher than 15 is considered 'infinity' and routes with such a metric are considered unreachable. Thus RIP cannot be used on networks with more than 15 hops between any two routers, and using redistribute metrics larger than 1 further reduces this maximum hop count.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the instance.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">Name of the VRF to be used for connections.</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)"></ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">Whether to originate default route.</ArgTableRow>
<ArgTableRow arg="route-timeout" typ="num">Specifies the time interval after which the route is considered invalid.</ArgTableRow>
<ArgTableRow arg="route-gc-timeout" typ="num"></ArgTableRow>
<ArgTableRow arg="update-interval" typ="num"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1">Routing table name where routes will be installed.</ArgTableRow>
</ArgTable>

### routing/rip/interface

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="bfd" typ="bool"></ArgTableRow>
</ArgTable>

### routing/rip/interface-template

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address (flags=46)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="split-horizon" typ="bool"></ArgTableRow>
<ArgTableRow arg="poison-reverse" typ="bool"></ArgTableRow>
<ArgTableRow arg="key-chain" typ="enum" unset="1">Name of the key-chain which contains the MD5 key. Should be set only when MD5 authentication is needed.</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">Password for plain-text authentication. Should be set only when plain-text authentication is needed.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (passive | strict)" unset="1"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### routing/rip/keys

**Type:** Directory

MD5 authentication key chains.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1">Key identifier. This number is included in MD5 authenticated RIP messages, and determines which key to use to check authentication for a specific message.</ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1">Authentication key. Maximal length 16 characters</ArgTableRow>
<ArgTableRow arg="valid-from" typ="date">The key is valid from this date and time.</ArgTableRow>
<ArgTableRow arg="valid-till" typ="date">The key is valid until this date and time.</ArgTableRow>
</ArgTable>

### routing/rip/neighbor

**Type:** Directory

This submenu is used to define neighboring routers to exchange routing information with. Normally there is no need to add the neighbors, if multicasting is working properly within the network. If there are problems with exchanging routing information, neighbor routers can be added to the list. It will force the router to exchange the routing information with the neighbor using regular unicast packets.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="routes" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-total" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="entries-bad" typ="num"></ArgTableRow>
<ArgTableRow arg="last-update" typ="time">Time from last update.</ArgTableRow>
</ArgTable>

### routing/rip/static-neighbor

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
</ArgTable>
