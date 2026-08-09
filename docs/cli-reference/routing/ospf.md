# Ospf

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/ospf

**Type:** Directory

### routing/ospf/area

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="T" typ="transit-capable">transit-capable</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">The name of the area</ArgTableRow>
<ArgTableRow arg="instance" typ="enum" mandatory="1">Name of the OSPF instance this area belongs to.</ArgTableRow>
<ArgTableRow arg="area-id" typ="ipAddr">OSPF area identifier. If the router has networks in more than one area, then an area with `area-id=0.0.0.0` (the backbone) must always be present. The backbone always contains all area border routers. The backbone is responsible for distributing routing information between non-backbone areas. The backbone must be contiguous, i.e. there must be no disconnected segments. However, area border routers do not need to be physically connected to the backbone - connection to it may be simulated using a virtual link.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (default | stub | nssa)">The area type. Read more on the area types in the [OSPF user guides](../../user-guides/routing-and-networking-protocols/unicast/ospf/index.md#understanding-ospf-areas).</ArgTableRow>
<ArgTableRow arg="no-summaries" typ="switch">Flag parameter, if set then the area will not flood summary LSAs in the stub area.</ArgTableRow>
<ArgTableRow arg="default-cost" typ="num" unset="1">Default cost of injected LSAs into the area. If the value is not set, then stub area type-3 default LSA will not be originated.</ArgTableRow>
<ArgTableRow arg="nssa-translator" typ="enum (candidate | no | yes)" unset="1">
The parameter indicates which ABR will be used as a translator from `type-7` to `type-5` LSA. Applicable only if area type is NSSA.
- yes - the router will be always used as a translator.
- no - the router will never be used as a translator.
- candidate - OSPF elects one of the candidate routers to be a translator.
</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="transit-capable" typ="bool"></ArgTableRow>
</ArgTable>

#### routing/ospf/area/range

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="A" typ="advertise">advertise</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="area" typ="enum" mandatory="1">The OSPF area associated with this range.</ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" mandatory="1">The network prefix of this range.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool">Whether to create a summary LSA and advertise it to the adjacent areas.</ArgTableRow>
<ArgTableRow arg="cost" typ="num" unset="1">The cost of the summary LSA this range will create. Default - use the largest cost of all routes used (i.e. routes that fall within this range).</ArgTableRow>
</ArgTable>

### routing/ospf/instance

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (2 | 3)">OSPF version this instance will be running (v2 for IPv4, v3 for IPv6).</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">The VRF table this OSPF instance operates on.</ArgTableRow>
<ArgTableRow arg="router-id" typ="alt { ipAddr
, enum
 }">OSPF Router ID. Can be set explicitly as an IP address, or as the name of the router-id instance.</ArgTableRow>
<ArgTableRow arg="out-filter-select" typ="enum" unset="1">Name of the routing filter select chain, used for output selection. Output operates only with **external** routes.</ArgTableRow>
<ArgTableRow arg="out-filter-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="originate-default" typ="enum (never | always | if-installed)" unset="1">Specifies the default route (`0.0.0.0/0`) distribution method.</ArgTableRow>
<ArgTableRow arg="in-filter-chain" typ="enum" unset="1">Name of the [routing filter](../../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md#route-filtering) chain used for incoming prefixes.</ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-address" typ="address (flags=64)" unset="1"></ArgTableRow>
<ArgTableRow arg="mpls-te-area" typ="ipAddr" unset="1">The area used for MPLS traffic engineering. TE Opaque LSAs are generated in this area. No more than one OSPF instance can have `mpls-te-area` configured.</ArgTableRow>
<ArgTableRow arg="domain-id" typ="address (flags=R)" unset="1">MPLS-related parameter. Identifies the OSPF domain of the instance. This value is attached to OSPF routes redistributed in BGP as VPNv4 routes as a BGP extended community attribute and used when BGP VPNv4 routes are redistributed back to OSPF to determine whether to generate an `inter-area` or `AS-external` LSA for that route. By default Null domain-id is used, as described in [RFC 4577](https://tools.ietf.org/html/rfc4577).</ArgTableRow>
<ArgTableRow arg="domain-tag" typ="num" unset="1">If set, then used in route redistribution (as route-tag in all external LSAs generated by this router), and in route calculation (all external LSAs having this route tag are ignored). Needed for interoperability with older Cisco systems. By default not set.</ArgTableRow>
<ArgTableRow arg="use-dn" typ="bool" unset="1">Forces use or ignoring of the DN bit. Useful in some CE-PE scenarios to inject `intra-area` routes into VRF. If a parameter is unset, then the DN bit is used according to RFC.</ArgTableRow>
<ArgTableRow arg="redistribute" typ="ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, bgp-mpls-vpn, slaac)" unset="1">Enable redistribution of specific route types.</ArgTableRow>
</ArgTable>

### routing/ospf/interface

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=4i)" unset="1"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | virtual-link)">
The OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'ptp' on PtP interfaces and 'broadcast' on all other interfaces.
- `broadcast` - Network type suitable for Ethernet and other multicast capable link layers. Elects designated router.
- `nbma` - Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated router.
- `ptp` - Suitable for networks that consist only of two nodes. Does not elect a designated router.
- `ptmp` - Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Does not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for them
- `ptp-unnumbered` - Works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case IP unnumbered is used on Cisco devices.
- `virtual-link` - Interface for virtual link.
</ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="vlink-transit-area" typ="enum" unset="1">A non-backbone area the two routers have in common over which the virtual link will be established. Virtual links can not be established through stub areas.</ArgTableRow>
<ArgTableRow arg="vlink-neighbor-id" typ="ipAddr" unset="1">Specifies the **router-id** of the neighbor which should be connected over the virtual link.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (down | loopback | ptp | passive | waiting | standby | dr-other | bdr | dr)"></ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="vlink-remote-address" typ="address (flags=46)"></ArgTableRow>
</ArgTable>

### routing/ospf/interface-template

**Type:** Directory

The interface template defines common network and interface matches and what parameters to assign to a matched interface.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="area" typ="enum" mandatory="1">The OSPF area to which the matching interface will be associated.</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">Matcher. Interfaces to match. Accepts specific interface names or the name of the interface list.</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="networks" typ="object { address (flags=46/)
 }" unset="1">Matcher. The network prefix associated with the area. OSPF will be enabled on all interfaces that have at least one address falling within this range. Note that the network prefix of the address is used for this check (i.e. not the local address). For point-to-point interfaces, this means the address of the remote endpoint.</ArgTableRow>
<ArgTableRow arg="prefix-list" typ="enum" unset="1">Name of the address list containing networks that should be advertised to the v3 interface.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (broadcast | nbma | ptp | ptp-unnumbered | ptmp | ptmp-broadcast)">
The OSPF network type on this interface. Note that if interface configuration does not exist, the default network type is 'ptp' on PtP interfaces and 'broadcast' on all other interfaces.
- `broadcast` - Network type suitable for Ethernet and other multicast capable link layers. Elects designated router.
- `nbma` - Non-Broadcast Multiple Access. Protocol packets are sent to each neighbor's unicast address. Requires manual configuration of neighbors. Elects designated router.
- `ptp` - Suitable for networks that consist only of two nodes. Does not elect a designated router.
- `ptmp` - Point-to-Multipoint. Easier to configure than NBMA because it requires no manual configuration of a neighbor. Does not elect a designated router. This is the most robust network type and as such suitable for wireless networks, if 'broadcast' mode does not work well enough for them
- `ptp-unnumbered` - Works the same as ptp, except that the remote neighbor does not have an associated IP address to a specific PTP interface. For example, in case IP unnumbered is used on Cisco devices.
</ArgTableRow>
<ArgTableRow arg="retransmit-interval" typ="time">Time interval after which the lost link state advertisement will be resent. When a router sends a link state advertisement (LSA) to its neighbor, the LSA is kept until the acknowledgment is received. If the acknowledgment was not received in time (see transmit-delay), the router will try to retransmit the LSA.</ArgTableRow>
<ArgTableRow arg="transmit-delay" typ="time">Link-state transmit delay is the estimated time it takes to transmit a link-state update packet on the interface.</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time">The interval between **HELLO** packets that the router sends out on this interface. The smaller this interval is, the faster topological changes will be detected; the tradeoff is more OSPF protocol traffic. This value must be the same for all the routers on a specific network, otherwise, adjacency between them will not form.</ArgTableRow>
<ArgTableRow arg="dead-interval" typ="time">Specifies the interval after which a neighbor is declared dead. This interval is advertised in hello packets. This value must be the same for all routers on a specific network, otherwise, adjacency between them will not form.</ArgTableRow>
<ArgTableRow arg="priority" typ="num">
Router's priority. Used to determine the designated router in a broadcast network. The router with the highest priority value takes precedence. Priority value 0 means the router is not eligible to become a designated or backup designated router at all.

Default value is 128, keep this in mind if you had strict priorities set for DR/BDR election.
</ArgTableRow>
<ArgTableRow arg="cost" typ="num">Interface cost expressed as link state metric.</ArgTableRow>
<ArgTableRow arg="passive" typ="switch">If enabled, then the router does not send or receive OSPF traffic on the matching interfaces.</ArgTableRow>
<ArgTableRow arg="auth" typ="enum (simple | md5 | sha1 | sha256 | sha384 | sha512)" unset="1">
Specifies authentication method for OSPF protocol messages.

- `simple` - plain text authentication.
- `md5` - keyed Message Digest 5 authentication.
- `sha*` - HMAC-SHA authentication RFC5709.

If the parameter is unset, then authentication is not used.
</ArgTableRow>
<ArgTableRow arg="auth-key" typ="string" unset="1">The authentication key to be used, should match on all the neighbors of the network segment.</ArgTableRow>
<ArgTableRow arg="auth-id" typ="num" unset="1">The key id is used to calculate a message digest (used when MD5 or SHA authentication is enabled). The value should match all OSPF routers from the same region.</ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>

### routing/ospf/lsa

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="self-originated">Whether the LSA originated from the router itself.</ArgTableRow>
<ArgTableRow arg="F" typ="flushing">flushing</ArgTableRow>
<ArgTableRow arg="W" typ="wraparound">wraparound</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum">The area this LSA belongs to.</ArgTableRow>
<ArgTableRow arg="link" typ="address (flags=4i)"></ArgTableRow>
<ArgTableRow arg="link-instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="type" typ="string"></ArgTableRow>
<ArgTableRow arg="originator" typ="ipAddr">An originator of the LSA record.</ArgTableRow>
<ArgTableRow arg="id" typ="ipAddr">LSA record ID</ArgTableRow>
<ArgTableRow arg="sequence" typ="num">A number of times the LSA for a link has been updated.</ArgTableRow>
<ArgTableRow arg="age" typ="num">How long ago (in seconds) the last update occurred.</ArgTableRow>
<ArgTableRow arg="checksum" typ="num"></ArgTableRow>
<ArgTableRow arg="body" typ="string"></ArgTableRow>
</ArgTable>

### routing/ospf/neighbor

**Type:** Directory

List of currently active OSPF neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="V" typ="virtual">virtual</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="area" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum">Name of the interface this neighbor was discovered.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">An IP address of the OSPF neighbor router.</ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="router-id" typ="ipAddr">Neighbor router's **RouterID**</ArgTableRow>
<ArgTableRow arg="dr" typ="ipAddr">An IP address of the Designated Router.</ArgTableRow>
<ArgTableRow arg="bdr" typ="ipAddr">An IP address of the Backup Designated Router.</ArgTableRow>
<ArgTableRow arg="state" typ="string">
- `Down` - No Hello packets have been received from a neighbor.
- `Attempt` - Applies only to NBMA clouds. The state indicates that no recent information was received from a neighbor.
- `Init` - Hello packet received from the neighbor, but bidirectional communication is not established (Its own RouterID is not listed in the Hello packet).
- `2-way` - This state indicates that bi-directional communication is established. DR and BDR elections occur during this state. Routers build adjacencies based on whether the router is DR or BDR, and the link is point-to-point or a virtual link.
- `ExStart` - Routers try to establish the initial sequence number that is used for the packet information exchange. The router with a higher ID becomes the master and starts the exchange.
- `Exchange` - Routers exchange database description (DD) packets.
- `Loading` - In this state, actual link state information is exchanged. Link State Request packets are sent to neighbors to request any new LSAs that were found during the Exchange state.
- `Full` - Adjacency is complete, and neighbor routers are fully adjacent. LSA information is synchronized between adjacent routers. Routers achieve the full state with their DR and BDR only. An exception is P2P links.
</ArgTableRow>
<ArgTableRow arg="state-changes" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-retransmits" typ="num"></ArgTableRow>
<ArgTableRow arg="ls-requests" typ="num"></ArgTableRow>
<ArgTableRow arg="db-summaries" typ="num"></ArgTableRow>
<ArgTableRow arg="adjacency" typ="time">Elapsed time since adjacency was formed.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

### routing/ospf/static-neighbor

**Type:** Directory

Static configuration of the OSPF neighbors. Required for non-broadcast multi-access networks.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="area" typ="enum" mandatory="1">Name of the area the neighbor belongs to.</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)" mandatory="1">The unicast IP address and an interface that can be used to reach the IP of the neighbor. For example, `address=1.2.3.4%ether1` indicates that a neighbor with IP `1.2.3.4` is reachable on the `ether1` interface.</ArgTableRow>
<ArgTableRow arg="instance-id" typ="num"></ArgTableRow>
<ArgTableRow arg="poll-interval" typ="time">How often to send hello messages to the neighbors that are in a `down` state (i.e., there is no traffic from them).</ArgTableRow>
</ArgTable>
