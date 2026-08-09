# Pool

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ipv6/pool

**Package:** ipv6
**Type:** Directory

IP pools are used to define ipv6 prefixes that can be used by various RouterOS utilities, for example, DHCP server, Point-to-Point servers and more. Whenever possible, the same IPv6 prefix is given out to each client (OWNER/INFO pair).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the pool.</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="from-pool" typ="enum">Name of another pool from which to acquire prefix dynamically.</ArgTableRow>
<ArgTableRow arg="prefix-length" typ="num" mandatory="1">The option represents the prefix size that will be given out to the client.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="actual-prefix" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="valid-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="preferred-lifetime" typ="time"></ArgTableRow>
</ArgTable>

### ipv6/pool/used

**Package:** ipv6
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="pool" typ="enum">Name of the pool the prefix is reserved from.</ArgTableRow>
<ArgTableRow arg="prefix" typ="ip6Prefix">IPv6 prefix that is assigned to the client from the pool.</ArgTableRow>
<ArgTableRow arg="owner" typ="string">What reserved the prefix ("DHCP", etc.)</ArgTableRow>
<ArgTableRow arg="info" typ="string">Shows DUID related information received from the client (value in hex). Can contain also a raw timestamp in hex.</ArgTableRow>
</ArgTable>
