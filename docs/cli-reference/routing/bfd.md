# Bfd

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/bfd

**Conditions:** BFD_AUTHENTICATION
**Type:** Directory

### routing/bfd/authentication

**Conditions:** BFD_AUTHENTICATION
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="T" typ="transmit">transmit</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (none | simple-password | keyed-md5 | meticulous-keyed-md5 | keyed-sha1 | meticulous-keyed-sha1)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string"></ArgTableRow>
<ArgTableRow arg="transmit-after" typ="date"></ArgTableRow>
<ArgTableRow arg="accept-before" typ="date"></ArgTableRow>
</ArgTable>

### routing/bfd/configuration

**Conditions:** BFD_AUTHENTICATION
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum" unset="1">The Virtual Routing and Forwarding instance to which this configuration applies.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">list of interfaces where BFD configuration should be active.</ArgTableRow>
<ArgTableRow arg="addresses" typ="object { alt { ip6Prefix
, ipPrefix
 } { ip6Prefix
, ipPrefix
 }
 }" unset="1">This config entry will only apply to BFD sessions established with these specific remote neighbors.</ArgTableRow>
<ArgTableRow arg="address-list" typ="enum" unset="1">Firewall address list name. BFD configuration will apply if remote IP address is contained within specified list.</ArgTableRow>
<ArgTableRow arg="min-tx" typ="time" unset="1">Desired transmit interval that the local router would like to use when sending BFD packets to the neighbor.</ArgTableRow>
<ArgTableRow arg="min-rx" typ="time" unset="1">Minimum receive interval that the local router requires between received BFD packets.</ArgTableRow>
<ArgTableRow arg="multiplier" typ="num" unset="1">This value is multiplied by the negotiated transmission interval to determine the **Hold Time**; if no packets within the Hold time are received - the neighbor is declared down. `Hold Time = negotiated interval Ã— multiplier`</ArgTableRow>
<ArgTableRow arg="forbid-bfd" typ="bool" unset="1">if = **yes**: BFD sessions matching criteria will be prohibited.</ArgTableRow>
<ArgTableRow arg="keyring" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

### routing/bfd/session

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="U" typ="up">up</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="multihop" typ="bool"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (admin-down | down | init | up)"></ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="desired-tx-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="actual-tx-interval" typ="time">real-time frequency at which the device currently sends BFD control packets.</ArgTableRow>
<ArgTableRow arg="required-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-rx" typ="time"></ArgTableRow>
<ArgTableRow arg="remote-min-tx" typ="time"></ArgTableRow>
<ArgTableRow arg="multiplier" typ="num"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="time"></ArgTableRow>
<ArgTableRow arg="packets-rx" typ="num"></ArgTableRow>
<ArgTableRow arg="packets-tx" typ="num"></ArgTableRow>
</ArgTable>
