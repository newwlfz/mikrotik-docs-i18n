# Rsvp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/traffic-eng

**Conditions:** !smips
**Type:** Directory

### mpls/traffic-eng/flow

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="N" typ="ingress"></ArgTableRow>
<ArgTableRow arg="E" typ="egress"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
<ArgTableRow arg="R" typ="reservation"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="sender" typ="string"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="out-labels" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="out-nexthop" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="bw" typ="num"></ArgTableRow>
<ArgTableRow arg="style" typ="enum (unknown | shared | fixed)"></ArgTableRow>
<ArgTableRow arg="psb" typ="string"></ArgTableRow>
<ArgTableRow arg="blockade" typ="string"></ArgTableRow>
<ArgTableRow arg="resv" typ="string"></ArgTableRow>
<ArgTableRow arg="rsb" typ="string"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/interface

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="resource-class" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="refresh-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="use-udp" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="blockade-k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="te-metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="igp-flood-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="up-flood-thresholds" typ="multi { array-id, num [0 .. 100]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="down-flood-thresholds" typ="multi { array-id, num [0 .. 100]
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="remaining-bw" typ="num"></ArgTableRow>
<ArgTableRow arg="remaining-bw-prios" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="lih" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address-ip" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="local-address-ip6" typ="address (flags=46)"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/path

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-cspf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="hops" typ="multi { array-id, array-id, super { address (flags=46)
, /bool
 } { address (flags=46)
, /bool
 }
 }" unset="1"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/tunnel

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="from-address" typ="address (flags=46)" unset="1">Ingress address of the tunnel. If not set, the least IP address is picked.</ArgTableRow>
<ArgTableRow arg="to-address" typ="address (flags=46)" mandatory="1">Remote end of the TE tunnel.</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="primary-path" typ="enum" unset="1">Primary label switching paths defined in the `/mpls/traffic-eng/path` menu.</ArgTableRow>
<ArgTableRow arg="secondary-paths" typ="multi { array-id, enum
 }" unset="1">List of label switching paths used by the TE tunnel if the primary path fails. Paths are defined in the `/mpls/traffic-eng/path` menu.</ArgTableRow>
<ArgTableRow arg="primary-retry-interval" typ="time" unset="1">Interval after which the tunnel will try to use the primary path.</ArgTableRow>
<ArgTableRow arg="secondary-standby" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bandwidth-limit" typ="num" unset="1">Defines the actual bandwidth limitation of the TE tunnel. Limit is configured in percent of the specified tunnel `bandwidth`.</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-range" typ="composite { ,  }" unset="1">Auto bandwidth adjustment range.</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-reserve" typ="num" unset="1">Specifies the percentage of additional bandwidth to reserve.</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-avg-interval" typ="time" unset="1">Interval in which the actual amount of data is measured, from which average bandwidth is calculated.</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-update-interval" typ="time" unset="1">Interval during which the tunnel keeps track of the highest average rate.</ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1">The parameter is used to decide whether this session can preempt another session. 0 sets the highest priority.</ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1">Used to decide whether this session can be preempted by another session. 0 sets the highest priority.</ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1">If enabled, the sender node will receive information about the actual route that the LSP tunnel traverses. Record Route is analogous to a path vector, and hence can be used for loop detection.</ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1">Use the interface only if `resource-class` matches all of the specified bits.</ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1">Use the interface if `resource-class` matches any of specified bits.</ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1">Do not use the interface if `resource-class` matches any of the specified bits.</ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1">Interval after which the tunnel will re-optimize the current path. If the current path is not the best path then after optimization the best path will be used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="forwarding-on" typ="string"></ArgTableRow>
<ArgTableRow arg="primary" typ="string"></ArgTableRow>
<ArgTableRow arg="primary-pending" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary-pending" typ="string"></ArgTableRow>
</ArgTable>

#### mpls/traffic-eng/tunnel/reoptimize

**Conditions:** !smips
**Type:** Command
