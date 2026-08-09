# Dhcp Server

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/dhcp-server

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="alt { enum (static-only) { static-only:0xffffffff }
, enum
 }">Pool from which dynamic prefix bindings will acquire prefixes</ArgTableRow>
<ArgTableRow arg="address-pool" typ="alt { enum (static-only) { static-only:0xffffffff }
, enum
 }">Pool from which dynamic address bindings will acquire addresses (pool prefix length must be 128)</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">Duration of the newly created and extended bindings</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">Append Rapid Commit option to use two packet Solicit-Reply exchange</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">Use RADIUS server for authentication</ArgTableRow>
<ArgTableRow arg="preference" typ="num">Advertise message preference, the highest server preference value is preferred over all others</ArgTableRow>
<ArgTableRow arg="binding-script" typ="alt { , string
 }"></ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, alt { enum
, enum
 } { enum
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">distance for issued client bindings in routing table</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }">Address lists to which the binding prefix/address will be added (can be overridden by binding address-lists parameter)</ArgTableRow>
<ArgTableRow arg="ignore-ia-na-bindings" typ="bool">Server will ignore IA_NA options in the messages sent by the client and will act as if the message didn't contain them</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="duid" typ="string"></ArgTableRow>
</ArgTable>

### ipv6/dhcp-server/binding

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="radius">radius</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip6Prefix
 }">Assigns an individual address or prefix to the client</ArgTableRow>
<ArgTableRow arg="duid" typ="string" mandatory="1">hex string</ArgTableRow>
<ArgTableRow arg="iaid" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ia-type" typ="enum (na | pd)"></ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)">Name of the server that can offer this binding to the client</ArgTableRow>
<ArgTableRow arg="life-time" typ="time"></ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="enum">for addresses, pool with prefix length 128</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, alt { enum
, enum
 } { enum
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string">Bit rate limit for the client</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool"></ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, string
 }">Address lists to which the binding prefix/address will be added (overrides server address-lists parameter)</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom)"></ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="queue-type" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-server" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (waiting | offered | bound)"></ArgTableRow>
<ArgTableRow arg="expires-after" typ="time"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="alt { enum (never | sometime) { never:0xffffffff, sometime:0xfffffffe }
, time
 }"></ArgTableRow>
<ArgTableRow arg="client-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-last-sent" typ="string"></ArgTableRow>
<ArgTableRow arg="reconfigure-status" typ="string"></ArgTableRow>
</ArgTable>

#### ipv6/dhcp-server/binding/make-static

**Package:** dhcp
**Type:** Command

#### ipv6/dhcp-server/binding/send-reconfigure

**Package:** dhcp
**Type:** Command

### ipv6/dhcp-server/option

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="code" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="raw-value" typ="string"></ArgTableRow>
</ArgTable>

#### ipv6/dhcp-server/option/sets

**Package:** dhcp
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="options" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>
