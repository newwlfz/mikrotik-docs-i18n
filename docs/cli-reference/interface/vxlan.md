# Vxlan

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/vxlan

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">hw-offloaded</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="vni" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="group" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dont-fragment" typ="enum (disabled | enabled | auto | inherit)"></ArgTableRow>
<ArgTableRow arg="vtep-vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="vteps-ip-version" typ="enum (ipv4 | ipv6)"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="max-fdb-size" typ="num"></ArgTableRow>
<ArgTableRow arg="ttl" typ="num"></ArgTableRow>
<ArgTableRow arg="learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="checksum" typ="bool"></ArgTableRow>
<ArgTableRow arg="rem-csum" typ="enum (none | rx | tx | both)"></ArgTableRow>
<ArgTableRow arg="hw" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num {  }"></ArgTableRow>
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

### interface/vxlan/fdb

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="remote-ip" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
</ArgTable>

### interface/vxlan/vteps

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">hw-offloaded</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="remote-ip" typ="alt { ipAddr
, ip6Addr
 }" mandatory="1"></ArgTableRow>
</ArgTable>
