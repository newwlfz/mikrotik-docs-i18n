# Vpls

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/vpls

**Conditions:** !smips
**Type:** Directory

List of all VPLS interfaces. This menu also shows dynamically created BGP-based VPLS interfaces.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="B" typ="bgp-signaled">bgp-signaled</ArgTableRow>
<ArgTableRow arg="C" typ="cisco-bgp-signaled">cisco-bgp-signaled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the interface.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer 3 Maximum Transmission Unit.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Static MAC address of the interface. Automatically generated when not set.</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">Address Resolution Protocol.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }">Time until an ARP entry expires. Set to `auto` to use the interface-type default value.</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">Specifies whether to detect if an interface is running. If set to `no`, the interface will always have the `running` flag.</ArgTableRow>
<ArgTableRow arg="peer" typ="address (flags=46v)" mandatory="1">The IP address of the remote peer (RFC 4762 Section 3.1).</ArgTableRow>
<ArgTableRow arg="vpls-id" typ="address (flags=R)" unset="1">A unique number that identifies the VPLS tunnel. Encoding is a 2byte+4byte or 4byte+2byte number (RFC 4762 Section 3.2).</ArgTableRow>
<ArgTableRow arg="cisco-static-id" typ="num" unset="1">Cisco-style VPLS tunnel ID (RFC 4447 FEC type 0x80).</ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) article.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">[Bridge](../interface/bridge.md) the VPLS interface belongs to.</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">Cost of the [bridge port](../interface/bridge.md#path-cost).</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">When set to `none`, [bridge horizon](../interface/bridge.md#horizon) is not used.</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when [bridge `vlan-filtering`](../interface/bridge.md#vlan-filtering) is set to `yes`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bgp-vpls" typ="enum">Name of the [BGP VPLS](../routing/bgp.md#routingbgpvpls) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).</ArgTableRow>
<ArgTableRow arg="bgp-vpls-prfx" typ="string">Prefix of the [BGP VPLS](../routing/bgp.md#routingbgpvpls) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).</ArgTableRow>
</ArgTable>

### interface/vpls/monitor

**Conditions:** !smips
**Type:** Command

Command displays the current VPLS interface status.

For example:

```ros
[admin@10.0.11.23] /interface/vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status: 
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="remote-label" typ="num">MPLS label assigned by the remote peer for this pseudowire (RFC 4447 Section 5.1).</ArgTableRow>
<ArgTableRow arg="local-label" typ="num">MPLS label assigned locally for this pseudowire (RFC 4447 Section 5.1).</ArgTableRow>
<ArgTableRow arg="remote-status" typ="ubit (not-forwarding, attachment-circuit-rx-fault, attachment-circuit-tx-fault, pw-rx-fault, pw-tx-fault)">Pseudowire status received from the remote peer via LDP status signaling (RFC 4447 Section 5.4).</ArgTableRow>
<ArgTableRow arg="remote-group" typ="num">Group ID of the remote peer, used for LDP status withdrawal aggregation (RFC 4447 Section 5.3).</ArgTableRow>
<ArgTableRow arg="te-tunnel" typ="enum">Name of the transport interface. Shown when VPLS is running over a [Traffic Engineering](../../user-guides/routing-and-networking-protocols/mpls/traffic-eng.md) tunnel.</ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, address
, iface_enum
 }">Transport nexthops in use.</ArgTableRow>
</ArgTable>
