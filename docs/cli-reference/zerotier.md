# zerotier

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# zerotier

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="online"></ArgTableRow>
<ArgTableRow arg="F" typ="tcp-fallback"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum {  } {  }
 }"></ArgTableRow>
<ArgTableRow arg="route-distance" typ="num"></ArgTableRow>
<ArgTableRow arg="backup-priorities" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="identity.public" typ="string"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="moons" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

## zerotier/controller

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="network" typ="string"></ArgTableRow>
<ArgTableRow arg="private" typ="bool"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="bool"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="multicast-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-range" typ="super { address (flags=4)
, [ -address (flags=4)]
 }"></ArgTableRow>
<ArgTableRow arg="ip6-range" typ="super { address (flags=6)
, [ -address (flags=6)]
 }"></ArgTableRow>
<ArgTableRow arg="ip6-rfc4193" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip6-6plane" typ="bool"></ArgTableRow>
<ArgTableRow arg="routes" typ="object { super { address (flags=46/)
, [ @address (flags=46)]
 } { address (flags=46/)
, [ @address (flags=46)]
 }
 }"></ArgTableRow>
</ArgTable>

### zerotier/controller/member

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="A" typ="authorized"></ArgTableRow>
<ArgTableRow arg="B" typ="bridge"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="network" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="zt-address" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="authorized" typ="bool"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="ip-address" typ="multi { array-id, address (flags=46)
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="lost" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-seen" typ="time"></ArgTableRow>
</ArgTable>

## zerotier/interface

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool"></ArgTableRow>
<ArgTableRow arg="network" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="allow-managed" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-global" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-default" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="bridge" typ="bool"></ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool"></ArgTableRow>
<ArgTableRow arg="network-name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
</ArgTable>

## zerotier/peer

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="B" typ="bonded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="zt-address" typ="string"></ArgTableRow>
<ArgTableRow arg="bonded" typ="bool"></ArgTableRow>
<ArgTableRow arg="latency" typ="time"></ArgTableRow>
<ArgTableRow arg="role" typ="string"></ArgTableRow>
<ArgTableRow arg="path" typ="multi { array-id, string
 }"></ArgTableRow>
</ArgTable>

### zerotier/peer/hint

**Package:** zerotier
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="identity" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }" mandatory="1"></ArgTableRow>
</ArgTable>
