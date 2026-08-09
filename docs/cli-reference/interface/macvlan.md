# Macvlan

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/macvlan

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Only interfaces with a MAC address are supported for macvlan</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (private | bridge)">In bridge mode macvlan interfaces are allowed to talk to eachother</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on)"></ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled)"></ArgTableRow>
</ArgTable>
