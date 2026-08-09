# Address List

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/address-list

**Type:** Directory

Firewall address lists allow a user to create lists of IP addresses grouped together under a common name. Firewall filter, mangle, and NAT facilities can then use those address lists to match packets against them.

The address list records can also be updated dynamically via the `action=add-src-to-address-list` or `action=add-dst-to-address-list` items found in NAT, Mangle, and Filter facilities.

Firewall rules with action `add-src-to-address-list` or `add-dst-to-address-list` work in passthrough mode, which means that the matched packets will be passed to the next firewall rules.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Name of the address list where the IP address will be added.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipRange
, string
 }">A single IP address or range of IPs to add to the address list, or a DNS name. You can input, for example, `192.168.0.0-192.168.1.255` and it will auto-modify the typed entry to 192.168.0.0/23 on saving. IP-IP ranges are supported only for IPv4 addresses.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Time after which the address will be removed from the address list. If the timeout is not specified, the address will be stored in the address list permanently otherwise the address will be stored in RAM and will be removed after a system's reboot.</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">Whether the entry is dynamically created.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="creation-time" typ="date">The time when the entry was created.</ArgTableRow>
</ArgTable>
