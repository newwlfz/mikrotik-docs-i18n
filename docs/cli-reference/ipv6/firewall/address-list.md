# Address List

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/firewall/address-list

**Package:** ipv6
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Name of the address list where the IP address will be added.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip6Prefix
, string
 }">A single IPv6 address or prefix to add to the address list, or a DNS name.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Time after which the address will be removed from the address list. If the timeout is not specified, the address will be stored in the address list permanently.</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">Whether the entry is dynamically created.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="creation-time" typ="date">The time when the entry was created.</ArgTableRow>
</ArgTable>
