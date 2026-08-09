# Mesh

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/mesh

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="auto-mac" typ="bool"></ArgTableRow>
<ArgTableRow arg="admin-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="mesh-portal" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-default-hoplimit" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-waiting-time" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-destination-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-preq-reply-and-forward" typ="bool"></ArgTableRow>
<ArgTableRow arg="hwmp-prep-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-propagation-delay" typ="num"></ArgTableRow>
<ArgTableRow arg="hwmp-rann-lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="reoptimize-paths" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
</ArgTable>

### interface/mesh/fdb

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="A" typ="active">active</ArgTableRow>
<ArgTableRow arg="R" typ="root">root</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mesh" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (local | outsider | direct | mesh | neighbor | larval | unknown)"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="on-interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="lifetime" typ="time"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="metric" typ="num"></ArgTableRow>
<ArgTableRow arg="seq-number" typ="num"></ArgTableRow>
</ArgTable>

### interface/mesh/port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mesh" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="path-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="port-type" typ="enum (auto | WDS | wireless | ethernet)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="active-port-type" typ="enum (wireless | WDS | ethernet-mesh | ethernet-bridge | ethernet-mixed)"></ArgTableRow>
<ArgTableRow arg="dr-address" typ="macAddr"></ArgTableRow>
</ArgTable>

### interface/mesh/traceroute

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mesh" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="time" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (success | ttl-exceeded | no-route | timeout)"></ArgTableRow>
</ArgTable>
