# Pimsm

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/pimsm

**Conditions:** !smips
**Type:** Directory

### routing/pimsm/bsr

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hash-mask-length" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (accept-any | accept-preferred | candidate | pending | elected)"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/candidate

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hashmask-length" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (candidate | pending | elected)"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/rp-candidate

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="holdtime" typ="num"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/rp-set

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/v)"></ArgTableRow>
<ArgTableRow arg="rp.address" typ="object { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="rp.priority" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="rp.timeout" typ="object { time
 }"></ArgTableRow>
</ArgTable>

### routing/pimsm/igmp-interface-template

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1"></ArgTableRow>
</ArgTable>

### routing/pimsm/instance

**Conditions:** !smips
**Type:** Directory

The instance menu defines the main PIM-SM settings. The instance is then used for all other PIM-related configurations like interface-template, static RP, and Bootstrap Router.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum">Name of the VRF for control connections.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the instance.</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)">Specifies address family for PIM.</ArgTableRow>
<ArgTableRow arg="switch-to-spt" typ="bool">Whether to switch to Shortest Path Tree (SPT) if multicast data bandwidth threshold is reached. The router will not proceed from protocol phase one (register encapsulation) to native multicast traffic flow if this option is disabled. It is recommended to enable this option.</ArgTableRow>
<ArgTableRow arg="switch-to-spt-interval" typ="time">Time interval in which to account for multicast data bandwidth, used in conjunction with `switch-to-spt-bytes` to determine if the switching threshold is reached.</ArgTableRow>
<ArgTableRow arg="switch-to-spt-bytes" typ="num">Multicast data bandwidth threshold. Switching to Shortest Path Tree (SPT) happens if this threshold is reached in the specified time interval. If a value of 0 is configured, switching will happen immediately.</ArgTableRow>
<ArgTableRow arg="crp-advertise-contained" typ="bool">Currently not implemented.</ArgTableRow>
<ArgTableRow arg="bsm-forward-back" typ="bool">Currently not implemented.</ArgTableRow>
<ArgTableRow arg="rp-hash-mask-length" typ="num">The hash mask allows changing how many groups to map to one of the matching RPs.</ArgTableRow>
<ArgTableRow arg="rp-static-override" typ="bool">Changes the selection priority for static RP. When disabled, the bootstrap RP set has a higher priority. When enabled, static RP has a higher priority.</ArgTableRow>
<ArgTableRow arg="ssm-range" typ="address (flags=46/)">Currently not implemented.</ArgTableRow>
</ArgTable>

### routing/pimsm/interface

**Conditions:** !smips
**Type:** Directory

The interface menu shows all interfaces that are currently participating in PIM and their statuses. This menu contains dynamic and read-only entries that get created by defined interface templates.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="P" typ="designated-router">designated-router</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">join-tracking</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dr" typ="switch"></ArgTableRow>
<ArgTableRow arg="join-tracking" typ="switch"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="propogation-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="override-interval" typ="time"></ArgTableRow>
</ArgTable>

### routing/pimsm/interface-template

**Conditions:** !smips
**Type:** Directory

The interface template menu defines which interfaces will participate in PIM and what per-interface configuration will be used.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the PIM instance this interface template belongs to.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">List of interfaces that will participate in PIM.</ArgTableRow>
<ArgTableRow arg="hello-period" typ="time">Periodic interval for Hello messages.</ArgTableRow>
<ArgTableRow arg="hello-delay" typ="time">Randomized interval for the initial Hello message on interface startup or detecting a new neighbor.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">The Designated Router (DR) priority. A single Designated Router is elected on each network. The priority is used only if all neighbors have advertised a priority option. The numerically largest priority is preferred. In case of a tie or if priority is not used - the numerically largest IP address is preferred.</ArgTableRow>
<ArgTableRow arg="join-prune-period" typ="time"></ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">Sets the value for a prune pending timer. It is used by upstream routers to figure out how long they should wait for a Join override message before pruning an interface that has join suppression enabled.</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">Sets the maximum time period over which to randomize when scheduling a delayed override Join message on a network that has join suppression enabled.</ArgTableRow>
<ArgTableRow arg="join-tracking-support" typ="bool">Sets the value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message. When enabled, a router advertises its willingness to disable Join suppression. It is possible for upstream routers to explicitly track the join membership of individual downstream routers if Join suppression is disabled. Unless all PIM routers on a link negotiate this capability, explicit tracking and the disabling of the Join suppression mechanism are not possible.</ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address (flags=46)
 }" unset="1"></ArgTableRow>
</ArgTable>

### routing/pimsm/neighbor

**Conditions:** !smips
**Type:** Directory

The neighbor menu shows all detected neighbors that are running PIM and their statuses. This menu contains dynamic and read-only entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="designated-router">designated-router</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">join-tracking</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance this neighbor is detected on.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">Shows the neighbor's IP address and local interface the neighbor is detected on.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">Indicates the neighbor's priority value.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Shows the remaining time after the neighbor is removed from the list if no new Hello message is received. The hold time equals neighbor's `hello-period * 3.5`.</ArgTableRow>
<ArgTableRow arg="designated-router" typ="bool">Shows whether the neighbor is elected as Designated Router (DR).</ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">Indicates the neighbor's value of the propagation delay in the LAN Prune Delay option in the Hello message.</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">Indicates the neighbor's value of the override interval in the LAN Prune Delay option in the Hello message.</ArgTableRow>
<ArgTableRow arg="join-tracking" typ="bool">Indicates the neighbor's value of a Tracking (T) bit in the LAN Prune Delay option in the Hello message.</ArgTableRow>
</ArgTable>

### routing/pimsm/static-rp

**Conditions:** !smips
**Type:** Directory

The static-rp menu allows manually defining the multicast group to RP mappings. Such a mechanism is not robust to failures but does at least provide a basic interoperability mechanism.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1">The name of the PIM instance this static RP belongs to.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)">The multicast group that belongs to a specific RP.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">The IP address of the static RP.</ArgTableRow>
</ArgTable>

### routing/pimsm/uib-g

**Conditions:** !smips
**Type:** Directory

The upstream information base menus show the any-source multicast (\*,G) and source-specific multicast (S,G) groups and their statuses. These menus contain only read-only entries.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="rp-local">rp-local</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance the multicast group is created on.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">The multicast group address.</ArgTableRow>
<ArgTableRow arg="rp" typ="address (flags=46i)">The address of the Rendezvous Point for this group.</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.</ArgTableRow>
<ArgTableRow arg="rp-local" typ="bool">Indicates whether the multicast router itself is the RP.</ArgTableRow>
</ArgTable>

### routing/pimsm/uib-sg

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="K" typ="keepalive">keepalive</ArgTableRow>
<ArgTableRow arg="S" typ="spt-bit">The Shortest Path Tree (SPT) bit indicates whether forwarding is taking place on the (S,G) Shortest Path Tree or on the (\*,G) tree. A router can have an (S,G) state and still be forwarding on a (\*,G) state during the interval when the source-specific tree is being constructed. When the SPT bit is false, only the (\*,G) forwarding state is used to forward packets from S to G. When the SPT bit is true, both (\*,G) and (S,G) forwarding states are used.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum">Name of the PIM instance the multicast group is created on.</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">The multicast group address.</ArgTableRow>
<ArgTableRow arg="source" typ="address (flags=46i)">The source IP address of the multicast group.</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">The Reverse Path Forwarding (RPF) indicates the router address and outgoing interface that a Join message for that group is directed to.</ArgTableRow>
<ArgTableRow arg="register" typ="enum (join | join-pending | prune)"></ArgTableRow>
</ArgTable>
