# Dhcp Relay

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-relay

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Relay will listen to messages originating from clients on this interface</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="object { alt { composite { ,  } { ,  }
, ip6Addr
 } { composite { ,  } { ,  }
, ip6Addr
 }
 }" mandatory="1">Servers to which the relay message will be forwarded</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, enum
 }">Options that are added to Relay-Forward messages. Note that option 18 (interface-id) is added automatically so that relay can relay the reply message correctly.</ArgTableRow>
<ArgTableRow arg="link-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }">If secs field in DHCP packet is smaller than delay-threshold, then this packet is ignored</ArgTableRow>
<ArgTableRow arg="store-relayed-bindings" typ="bool">Add routes to valid bindings found in reply messages</ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/monitor

**Package:** dhcp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="responses" typ="num"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/option

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
<ArgTableRow arg="only-if-mac-available" typ="bool">Option is added only if packet originated from client (not another relay) and MAC address is deducible</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-relay/reset-counters

**Package:** dhcp
**Type:** Command

### ipv6/dhcp-relay/routes

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="relay" typ="enum"></ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="peer-address" typ="ip6Addr">used as gateway</ArgTableRow>
<ArgTableRow arg="life-time" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
</ArgTable>
