# Ldp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/ldp

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="lsr-id" typ="ipAddr" unset="1">Unique label switching router's ID.</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num" unset="1">Max path vector limit used for loop detection. Works in combination with the `loop-detect` property.</ArgTableRow>
<ArgTableRow arg="hop-limit" typ="num" unset="1">Max hop limit used for loop detection. Works in combination with the `loop-detect` property.</ArgTableRow>
<ArgTableRow arg="loop-detect" typ="bool" unset="1">Defines whether to run LSP loop detection. Will not work correctly if not enabled on all LSRs. Should be used only on non-TTL networks such as ATMs.</ArgTableRow>
<ArgTableRow arg="use-explicit-null" typ="bool" unset="1">Whether to distribute explicit-null label bindings.</ArgTableRow>
<ArgTableRow arg="distribute-for-default" typ="bool" unset="1">Defines whether to map label for the default route.</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, address (flags=46)
 }" unset="1">Specifies LDP session connection origin addresses and also advertises these addresses as transport addresses to LDP neighbors.</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this instance will operate on.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">Determines supported address families by the instance.</ArgTableRow>
<ArgTableRow arg="preferred-afi" typ="enum (ip | ipv6)" unset="1">Determines which address family connection is preferred. Value is also set in dual-stack element (if used).</ArgTableRow>
</ArgTable>

### mpls/ldp/accept-filter

**Conditions:** !smips
**Type:** Directory

List of label bindings that should be accepted from LDP neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum (any)" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">Prefix to match.</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">Neighbor to which this filter applies.</ArgTableRow>
<ArgTableRow arg="accept" typ="bool" unset="1">Whether to accept label bindings from the neighbors for the specified prefix. If parameter is unset then matching prefix is not accepted.</ArgTableRow>
</ArgTable>

### mpls/ldp/advertise-filter

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum (any)" unset="1"></ArgTableRow>
<ArgTableRow arg="prefix" typ="address (flags=46/)" unset="1">Prefix to match.</ArgTableRow>
<ArgTableRow arg="neighbor" typ="address (flags=46/)" unset="1">Neighbor to which this filter applies.</ArgTableRow>
<ArgTableRow arg="advertise" typ="bool" unset="1">Whether to advertise label bindings to the neighbors for the specified prefix. If parameter is unset then matching prefix is not advertised.</ArgTableRow>
</ArgTable>

### mpls/ldp/interface

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">Name of the interface or interface list where LDP will be listening.</ArgTableRow>
<ArgTableRow arg="hello-interval" typ="time" unset="1">The interval between hello packets that the router sends out on the specified interface/s. The default value is 5s.</ArgTableRow>
<ArgTableRow arg="hold-time" typ="time" unset="1">Specifies the interval after which a neighbor discovered on the interface is declared as not reachable. The default value is 15s.</ArgTableRow>
<ArgTableRow arg="transport-addresses" typ="multi { array-id, address (flags=46)
 }" unset="1">Used transport addresses if they differ from LDP Instance settings.</ArgTableRow>
<ArgTableRow arg="accept-dynamic-neighbors" typ="bool" unset="1">Defines whether to discover neighbors dynamically or use only statically configured in LDP neighbors menu.</ArgTableRow>
<ArgTableRow arg="afi" typ="ubit (ip, ipv6)" unset="1">Determines interface address family. Only AFIs that are configured as supported by the instance are taken into account. If the value is not explicitly specified then it is considered to be equal to the instance-supported AFIs.</ArgTableRow>
</ArgTable>

### mpls/ldp/local-mapping

**Conditions:** !smips
**Type:** Directory

This sub-menu shows labels bound to the routes locally in the router. In this menu, static mappings can also be configured if there is no intention to use LDP dynamically.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether binding is active and can be selected as a candidate for forwarding.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether the entry was dynamically added.</ArgTableRow>
<ArgTableRow arg="E" typ="egress">egress</ArgTableRow>
<ArgTableRow arg="G" typ="gateway">Whether the destination is reachable through the gateway.</ArgTableRow>
<ArgTableRow arg="L" typ="local">Whether the destination is locally reachable on the router.</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this mapping belongs to.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" unset="1" mandatory="1">Destination prefix the label is assigned to.</ArgTableRow>
<ArgTableRow arg="label" typ="alt { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, num [16 .. 1048576]
 }" mandatory="1">Label number assigned to destination.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="adv-path" typ="string"></ArgTableRow>
<ArgTableRow arg="peers" typ="object { composite { ,  } { ,  }
 }">IP address and label space of the peer to which this entry was advertised.</ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>

### mpls/ldp/neighbor

**Conditions:** !smips
**Type:** Directory

List of discovered and statically configured LDP neighbors.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="O" typ="operational">Indicates whether the peer is operational.</ArgTableRow>
<ArgTableRow arg="C" typ="active-connect">Indicates that active role has been selected and the router is trying to establish the session.</ArgTableRow>
<ArgTableRow arg="W" typ="passive-wait">Indicates whether the peer is in a passive role and currently is waiting for the session to be initialized.</ArgTableRow>
<ArgTableRow arg="T" typ="throttled">Indicates whether session is in throttled state. Session is throttled after initialization failure, max throttle time 120s.</ArgTableRow>
<ArgTableRow arg="t" typ="sending-targeted-hello">Whether targeted hellos are being sent to the neighbor.</ArgTableRow>
<ArgTableRow arg="v" typ="vpls">Whether neighbor is used by LDP signaled VPLS tunnel.</ArgTableRow>
<ArgTableRow arg="p" typ="passive">Indicates whether the peer is in a passive role.</ArgTableRow>
<ArgTableRow arg="d" typ="on-demand">Downstream On Demand label distribution.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="transport" typ="address (flags=46vi)" mandatory="1">Remote transport address.</ArgTableRow>
<ArgTableRow arg="send-targeted" typ="bool" unset="1">Specifies whether to try to send targeted hellos, used for targeted (not directly connected) LDP sessions.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="object { composite { ,  } { ,  }
 }">LSR-ID and label space of the neighbor.</ArgTableRow>
<ArgTableRow arg="local-transport" typ="address (flags=46)">Selected local transport address.</ArgTableRow>
<ArgTableRow arg="addresses" typ="multi { array-id, address (flags=46)
 }">List of discovered addresses on the neighbor.</ArgTableRow>
<ArgTableRow arg="path-vector-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="on-demand" typ="bool">Downstream On Demand label distribution.</ArgTableRow>
<ArgTableRow arg="used-afi" typ="ubit (ip, ipv6)">Used transport AFI.</ArgTableRow>
</ArgTable>

### mpls/ldp/remote-mapping

**Conditions:** !smips
**Type:** Directory

The Sub-menu shows label bindings for routes received from other routers. Static mapping can be configured if there is no intention to use LDP dynamically. This table is used to build the Forwarding Table

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">Whether binding is active and can be selected as a candidate for forwarding.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Whether entry was dynamically added.</ArgTableRow>
<ArgTableRow arg="V" typ="vpls">vpls</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vrf" typ="enum" unset="1">Name of the VRF table this mapping belongs to.</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46/)" mandatory="1">Destination prefix the label is assigned to.</ArgTableRow>
<ArgTableRow arg="label" typ="alt { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, num [16 .. 1048576]
 }" mandatory="1">Label number assigned to destination.</ArgTableRow>
<ArgTableRow arg="nexthop" typ="address (flags=46i)" mandatory="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="peer" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
<ArgTableRow arg="pw-fec" typ="string"></ArgTableRow>
</ArgTable>
