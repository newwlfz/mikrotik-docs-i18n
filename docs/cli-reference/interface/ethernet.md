# Ethernet

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/ethernet

**Conditions:** i386
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="S" typ="slave">slave</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="l2mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="orig-mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool" syscap="uefi"></ArgTableRow>
<ArgTableRow arg="auto-negotiation" typ="bool"></ArgTableRow>
<ArgTableRow arg="advertise" typ="multi { , array-id,  }"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="enum (off | on | auto)"></ArgTableRow>
<ArgTableRow arg="cable-settings" typ="enum (short | standard | default)"></ArgTableRow>
<ArgTableRow arg="mdix-enable" typ="bool"></ArgTableRow>
<ArgTableRow arg="speed" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="composite { ,  }" syscap="switch"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on | forced-on-a | forced-on-bt)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-priority" typ="num" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-enabled" typ="bool" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-address" typ="alt { ipAddr
, ip6Addr
, macAddr
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-timeout" typ="time" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-interval" typ="alt { enum (none) { none:0 }
, time
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="sfp-rate-select" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-ignore-rx-los" typ="bool"></ArgTableRow>
<ArgTableRow arg="combo-mode" typ="enum (auto | copper | sfp)"></ArgTableRow>
<ArgTableRow arg="fec-mode" typ="enum (off | auto | fec74 | fec91)"></ArgTableRow>
<ArgTableRow arg="sfp-shutdown-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="passthrough-interface" typ="iface_enum { none:0 }" syscap="pcie_passthrough"></ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)"></ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="loop-protect" typ="enum (default | off | on)"></ArgTableRow>
<ArgTableRow arg="loop-protect-send-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="loop-protect-disable-time" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" syscap="switch"></ArgTableRow>
<ArgTableRow arg="loop-protect-status" typ="enum (off | on | disabled)"></ArgTableRow>
</ArgTable>

### interface/ethernet/switch

**Conditions:** !smips
**Syscap:** multiswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="mirror-source" typ="iface_enum { none:0 }" syscap="switch-mirror1"></ArgTableRow>
<ArgTableRow arg="mirror-target" typ="iface_enum { none:0, cpu:0xffffffff }" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="mirror-egress-target" typ="enum (none)" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="rspan" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="rspan-ingress-vlan-id" typ="num" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="rspan-egress-vlan-id" typ="num" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="switch-all-ports" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-flow-control" typ="bool" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">Layer 3 hardware offloading</ArgTableRow>
<ArgTableRow arg="qos-hw-offloading" typ="bool" syscap="crs_prestera">Quality of Service hardware offloading</ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="bridge-type" typ="enum (customer-vid-used-as-lookup-vid | service-vid-used-as-lookup-vid)"></ArgTableRow>
<ArgTableRow arg="drop-if-no-vlan-assignment-on-ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="drop-if-invalid-or-src-port-not-member-of-vlan-on-ports" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="unknown-vlan-lookup-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="forward-unknown-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-svid-in-one2one-vlan-lookup" typ="bool"></ArgTableRow>
<ArgTableRow arg="use-cvid-in-one2one-vlan-lookup" typ="bool"></ArgTableRow>
<ArgTableRow arg="mac-level-isolation" typ="bool"></ArgTableRow>
<ArgTableRow arg="multicast-lookup-mode" typ="enum (dst-mac-and-vid-always | dst-ip-and-vid-for-ipv4)"></ArgTableRow>
<ArgTableRow arg="override-existing-when-ufdb-full" typ="bool"></ArgTableRow>
<ArgTableRow arg="unicast-fdb-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="ingress-mirror0" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ingress-mirror1" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ingress-mirror-ratio" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="egress-mirror0" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="egress-mirror1" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="egress-mirror-ratio" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="fdb-uses" typ="enum (mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="vlan-uses" typ="enum (mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="mirror-egress-if-ingress-mirrored" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror-tx-on-mirror-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-qos-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="mirrored-packet-drop-precedence" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="bypass-vlan-ingress-filter-for" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing-for" typ="ubit ()"></ArgTableRow>
<ArgTableRow arg="bypass-l2-security-check-filter-for" typ="ubit ()"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (ADMtek | IC-Plus-175C | IC-Plus-178C | IC-Plus-175D | Atheros-8316 | Atheros-7240 | Atheros-8227 | Atheros-8327 | Atheros-8236 | QCA-8513L | Atheros-8327N | QCA-8519 | QCA-8511 | QCA-8337 | MediaTek-MT7621 | Realtek-RTL8367 | Marvell-98DX3236 | Marvell-98DX8216 | Marvell-98DX8208 | Marvell-98DX8332 | Marvell-98DX8212 | Marvell-98DX3257 | IPQ-PPE | Marvell-98DX8525 | Marvell-98PX1012 | Marvell-98DX4310 | Marvell-98DX224S | Marvell-98DX226S | Marvell-88E6393X | Marvell-98DX3255 | Marvell-88E6191X | Marvell-98DX2528 | Marvell-98CX8410 | Marvell-88E6341 | MediaTek-MT7531 | Marvell-88E6190 | Marvell-98DX7335 | Marvell-98DX3510 | Marvell-98DX3550 | MediaTek-MT7531AE | Marvell-98DX1508M | Alder | Marvell-98DX3530 | Marvell-98DX4550 | QCA-8386 | EN7523 | Marvell-98DX2521 | Marvell-98DX2556 | Marvell-98DX2588)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (QCA-8513L | QCA-8519 | QCA-8511)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/qos

**Syscap:** crs_prestera
**Type:** Directory

##### interface/ethernet/switch/qos/profile

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">QoS Profile name</ArgTableRow>
<ArgTableRow arg="pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="automap" typ="bool">Should DSCP and PCP values be automatically mapped to the profile?</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/map

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">QoS Map name</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/map/vlan

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="pcp" typ="multi { , , range [0 .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dei-only" typ="bool">Map only if DEI/CFI bit is set</ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/map/ip

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="map" typ="enum"></ArgTableRow>
<ArgTableRow arg="dscp" typ="multi { , , range [0 .. 63]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum" mandatory="1"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/priority-flow-control

**Syscap:** !prestera-ac3
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">PFC Profile name</ArgTableRow>
<ArgTableRow arg="traffic-class" typ="multi { array-id, num [ .. 7]
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rx" typ="bool">Receive (and obey) PFC frames</ArgTableRow>
<ArgTableRow arg="tx" typ="bool">Transmit PFC frames</ArgTableRow>
<ArgTableRow arg="pause-threshold" typ="alt { , num [ .. 100]
, num [1536 .. ]
 }">Transmit a pause frame (XOFF) when the total size of queued packets reaches this threshold</ArgTableRow>
<ArgTableRow arg="resume-threshold" typ="alt { , num [ .. 100]
, num [256 .. ]
 }">Transmit a resume frame (XON) when the total size of queued packets lowers down to this threshold</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/tx-manager

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Tx Manager name</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { num [ .. 100]
, num [1536 .. 67108864]
 }">The number of bytes (or %) exclusively reserved for the Tx Manager. The value gets split on active queues of assigned ports.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-id" typ="num"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/tx-manager/queue

**Syscap:** crs_prestera
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="schedule" typ="enum (strict-priority | low-priority-group | high-priority-group)">Schedule tx either by strict priority of the traffic class or round-robin within the group</ArgTableRow>
<ArgTableRow arg="weight" typ="num">Weight value for priority group</ArgTableRow>
<ArgTableRow arg="queue-buffers" typ="alt { num [ .. 100]
, num [1536 .. 67108864]
 }" syscap="!prestera-cpss">Per-queue reserved buffers. The number of bytes (or % of tx-manager) exclusively reserved for the queue.</ArgTableRow>
<ArgTableRow arg="use-shared-buffers" typ="bool" syscap="!prestera-cpss">Allow using the shared buffer pool when the port or queue buffers are full</ArgTableRow>
<ArgTableRow arg="wred" typ="bool" syscap="!prestera-ac3">Weighted Random Early Detection</ArgTableRow>
<ArgTableRow arg="ecn" typ="bool" syscap="!prestera-ac3">Explicit Congestion Notification - ECN marking</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tx-manager" typ="enum"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="wred-actual" typ="bool" syscap="!prestera-ac3">Actual WRED value</ArgTableRow>
<ArgTableRow arg="ecn-actual" typ="bool" syscap="!prestera-ac3">Actual ECN value</ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="multicast-buffers" typ="num">Maximum amount of packet buffers for multicast traffic (% of total buffer memory)</ArgTableRow>
<ArgTableRow arg="mirror-buffers" typ="num" syscap="!prestera-cpss">Maximum amount of packet buffers for mirrored traffic (% of total buffer memory)</ArgTableRow>
<ArgTableRow arg="mirror-profile" typ="enum">A QoS profile to apply to mirrored packets</ArgTableRow>
<ArgTableRow arg="shared-buffers" typ="num">Amount of packet buffers that are shared between ports (% of total buffer memory)</ArgTableRow>
<ArgTableRow arg="lossless-buffers" typ="num" syscap="!prestera-ac3">The size of the lossless shared pool (% of shared buffers)</ArgTableRow>
<ArgTableRow arg="lossless-traffic-class" typ="multi { array-id, num [ .. 7]
 }" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="wred-threshold" typ="enum (low | medium | high)" syscap="!prestera-ac3">A relative queue fill level to start a random tail drop or ECN marking</ArgTableRow>
<ArgTableRow arg="total-desc" typ="num" syscap="(option and !prestera-cpss)"></ArgTableRow>
<ArgTableRow arg="total-buff" typ="num" syscap="(option and !prestera-cpss)"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="total-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="total-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="total-byte-cap" typ="num"></ArgTableRow>
<ArgTableRow arg="total-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="multicast-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="multicast-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="multicast-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="multicast-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-egress-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="mirror-egress-byte-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="shared-packet-cap" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-packet-use" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-byte-cap" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="shared-byte-use" typ="num" syscap="prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="lossy-pool-packet-use" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-packet-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossy-pool-byte-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lossless-pool-byte-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="wred-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="wred-byte-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/qos/port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="profile" typ="enum" syscap="crs_prestera">QoS profile to assign to ingress packets by default</ArgTableRow>
<ArgTableRow arg="map" typ="enum" syscap="crs_prestera">QoS Packet-to-Profile mapping</ArgTableRow>
<ArgTableRow arg="trust-l2" typ="enum (ignore | trust | keep)" syscap="crs_prestera">Trust Layer 2 header (PCP) for QoS mapping</ArgTableRow>
<ArgTableRow arg="trust-l3" typ="enum (ignore | trust | keep)" syscap="crs_prestera">Trust Layer 3 header (DSCP) for QoS mapping</ArgTableRow>
<ArgTableRow arg="tx-manager" typ="enum" syscap="crs_prestera">QoS Tx Manager for egress traffic on this port</ArgTableRow>
<ArgTableRow arg="pfc" typ="enum" syscap="!prestera-ac3">Priority Flow Control profile for ingress traffic on this port</ArgTableRow>
<ArgTableRow arg="egress-rate-queue0" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue1" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue2" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue3" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue4" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue5" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue6" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate-queue7" typ="num" syscap="switch-rate"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue0-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue1-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue2-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue3-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue4-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue5-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue6-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue7-shared-packet-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue0-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue1-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue2-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue3-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue4-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue5-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue6-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue7-shared-byte-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue0-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue7-packet-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue0-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue7-byte-cap" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue0-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue1-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue2-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue3-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue4-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue5-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue6-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue7-packet-use" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="queue0-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue1-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue2-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue3-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue4-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue5-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue6-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="queue7-byte-use" typ="num"></ArgTableRow>
<ArgTableRow arg="byte-max" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="queue0-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue1-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue2-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue3-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue4-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue5-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue6-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="queue7-byte-max" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc0-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc1-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc2-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc3-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc4-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc5-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc6-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc7-pause-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc0-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc1-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc2-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc3-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc4-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc5-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc6-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc7-resume-threshold" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc0-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc1-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc2-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc3-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc4-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc5-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc6-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc7-use" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pfc-paused-tc" typ="multi { array-id, num
 }" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc-unknown" typ="multi { num
 }" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc-rx" typ="multi { num
 }" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pfc-tx" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { num
 }" syscap="prestera-cpss"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { num
 }" syscap="prestera-cpss"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/qos/port/reset-counters

**Type:** Command

#### interface/ethernet/switch/port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ingress-customer-tpid-override" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-customer-tpid-override" typ="num"></ArgTableRow>
<ArgTableRow arg="ingress-service-tpid-override" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-service-tpid-override" typ="num"></ArgTableRow>
<ArgTableRow arg="drop-secure-static-mac-move" typ="bool"></ArgTableRow>
<ArgTableRow arg="drop-dynamic-mac-move" typ="bool"></ArgTableRow>
<ArgTableRow arg="learn-limit" typ="num"></ArgTableRow>
<ArgTableRow arg="allow-unicast-loopback" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-multicast-loopback" typ="bool"></ArgTableRow>
<ArgTableRow arg="action-on-static-station-move" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop)"></ArgTableRow>
<ArgTableRow arg="drop-when-ufdb-entry-src-drop" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile-override" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-type" typ="enum (edge-port | network-port)"></ArgTableRow>
<ArgTableRow arg="allow-fdb-based-vlan-translate" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow-mac-based-service-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all)"></ArgTableRow>
<ArgTableRow arg="allow-mac-based-customer-vlan-assignment-for" typ="enum (none | untagged-and-priority-tagged-frame-only | tagged-frame-only | all)"></ArgTableRow>
<ArgTableRow arg="filter-untagged-frame" typ="bool"></ArgTableRow>
<ArgTableRow arg="filter-priority-tagged-frame" typ="bool"></ArgTableRow>
<ArgTableRow arg="filter-tagged-frame" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-vlan-tag-table-lookup-key" typ="enum (egress-vid | according-to-bridge-type)"></ArgTableRow>
<ArgTableRow arg="egress-vlan-mode" typ="enum (untagged | tagged | unmodified)"></ArgTableRow>
<ArgTableRow arg="ingress-mirror-to" typ="enum (none | mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="ingress-mirroring-according-to-vlan" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-mirror-to" typ="enum (none | mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="qos-scheme-precedence" typ="multi { array-id, enum (pcp-based | vlan-based | protocol-based | da-based | sa-based | dscp-based | ingress-acl-based) { pcp-based:0, vlan-based:1, protocol-based:2, da-based:3, sa-based:4, dscp-based:5, ingress-acl-based:6,  }
 }"></ArgTableRow>
<ArgTableRow arg="default-customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="default-service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="pcp-propagation-for-initial-pcp" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-pcp-propagation" typ="bool"></ArgTableRow>
<ArgTableRow arg="dscp-based-qos-dscp-to-dscp-mapping" typ="bool"></ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dei" typ="bool"></ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-pcp" typ="bool"></ArgTableRow>
<ArgTableRow arg="pcp-or-dscp-based-qos-change-dscp" typ="bool"></ArgTableRow>
<ArgTableRow arg="pcp-based-qos-drop-precedence-mapping" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dscp-mapping" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="pcp-based-qos-dei-mapping" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="pcp-based-qos-pcp-mapping" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="pcp-based-qos-priority-mapping" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="priority-to-queue" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="per-queue-scheduling" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-counter-includes" typ="ubit (device-loopback, fdb-hash-violation, exceeded-port-learn-limitation, dynamic-station-move, static-station-move, ufdb-source-drop, host-source-drop, unknown-host, ingress-vlan-filtered)"></ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter0-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)"></ArgTableRow>
<ArgTableRow arg="queue-custom-drop-counter1-includes" typ="ubit (red, yellow, green, queue0, queue1, queue2, queue3, queue4, queue5, queue6, queue7)"></ArgTableRow>
<ArgTableRow arg="policy-drop-counter-includes" typ="ubit (ingress-policing, ingress-acl, egress-policing, egress-acl)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="ingress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-customer-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="ingress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-service-tpid" typ="num"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-leakage-profile" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/port/reset-counters

**Type:** Command

#### interface/ethernet/switch/unicast-fdb

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="A" typ="active"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { enum
, enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | src-drop | dst-drop | src-and-dst-drop | ingress-port-policing-bypass | src-redirect-to-cpu | dst-redirect-to-cpu | src-and-dst-redirect-to-cpu)"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="age" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/unicast-fdb/flush

**Type:** Command

#### interface/ethernet/switch/multicast-fdb

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { macAddr
, ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="bypass-vlan-filter" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/reserved-fdb

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | drop)"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-vlan-filter" typ="bool"></ArgTableRow>
<ArgTableRow arg="bypass-ingress-port-policing" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/vlan

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="svl" typ="bool"></ArgTableRow>
<ArgTableRow arg="learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="flood" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/egress-vlan-tag

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="tagged-ports" typ="multi { array-id,  }"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/ingress-vlan-translation

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="protocol" typ="alt { enum (length | llc-bpdu) { length:1, llc-bpdu:0x4242,  }
, num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="sa-learning" typ="bool"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any)"></ArgTableRow>
<ArgTableRow arg="service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="service-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any)"></ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="alt { enum (customer-vid) { customer-vid:4096 }
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="alt { enum (service-vid) { service-vid:4096 }
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool"></ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/egress-vlan-translation

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any)"></ArgTableRow>
<ArgTableRow arg="service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="service-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-vlan-format" typ="enum (untagged-or-tagged | priority-tagged-or-tagged | tagged | any)"></ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="alt { enum (customer-vid) { customer-vid:4096 }
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="alt { enum (service-vid) { service-vid:4096 }
, num [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="pcp-propagation" typ="bool"></ArgTableRow>
<ArgTableRow arg="swap-vids" typ="enum (no | assign-cvid-to-svid)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/mac-based-vlan

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="macAddr" mandatory="1"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/one2one-vlan-switching

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="alt { enum
, enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-vid" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/protocol-based-vlan

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="frame-type" typ="enum (ethernet | rfc-1042 | llc)"></ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { enum () {  }
, num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="set-service-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all)"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="set-customer-vid-for" typ="enum (none | untagged-or-priority-tagged | tagged | all)"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="set-qos-for" typ="enum (none | untagged-or-priority-tagged | tagged | all)"></ArgTableRow>
<ArgTableRow arg="qos-group" typ="enum (none)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/dscp-to-dscp

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="new-dscp" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="original-dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="hex" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/dscp-qos-map

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dei" typ="num"></ArgTableRow>
<ArgTableRow arg="pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="hex" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/qos-group

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="dei" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum ()"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/shaper

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="port" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="target" typ="enum (queue0 | queue1 | queue2 | queue3 | queue4 | queue5 | queue6 | queue7 | wrr-group0 | wrr-group1 | port)"></ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet)"></ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
<ArgTableRow arg="burst" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/port-isolation

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (src | dst)"></ArgTableRow>
<ArgTableRow arg="forwarding-type" typ="ubit (bridged, routed)"></ArgTableRow>
<ArgTableRow arg="traffic-type" typ="ubit (unicast, multicast, broadcast)"></ArgTableRow>
<ArgTableRow arg="registration-status" typ="ubit (known, unknown)"></ArgTableRow>
<ArgTableRow arg="protocol-type" typ="ubit (arp, nd, dhcpv4, dhcpv6, ripv1)"></ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
<ArgTableRow arg="port-profile" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/port-leakage

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (src | dst)"></ArgTableRow>
<ArgTableRow arg="forwarding-type" typ="ubit (bridged, routed)"></ArgTableRow>
<ArgTableRow arg="traffic-type" typ="ubit (unicast, multicast, broadcast)"></ArgTableRow>
<ArgTableRow arg="registration-status" typ="ubit (known, unknown)"></ArgTableRow>
<ArgTableRow arg="protocol-type" typ="ubit (arp, nd, dhcpv4, dhcpv6, ripv1)"></ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
<ArgTableRow arg="port-profile" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/acl

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="table" typ="enum (ingress | egress)"></ArgTableRow>
<ArgTableRow arg="invert-match" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="dst-ports" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="service-vid" typ="super { !
, range [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="service-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-vid" typ="super { !
, range [ .. 4095]
 }"></ArgTableRow>
<ArgTableRow arg="customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="customer-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="src-l3-port" typ="super { !
, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-l3-port" typ="super { !
, range [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="custom-fields" typ="object { super { !
, super { enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, :num [ .. 127]
, :range [ .. 65535]
, [ /num [ .. 65535]]
 } { enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, :num [ .. 127]
, :range [ .. 65535]
, [ /num [ .. 65535]]
 }
 } { !
, super { enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, :num [ .. 127]
, :range [ .. 65535]
, [ /num [ .. 65535]]
 } { enum (start-of-frame | end-of-l2-header | end-of-l3-header) { start-of-frame:0, end-of-l2-header:1, end-of-l3-header:2 }
, :num [ .. 127]
, :range [ .. 65535]
, [ /num [ .. 65535]]
 }
 }
 }"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="drop-precedence" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dst-addr-registered" typ="bool"></ArgTableRow>
<ArgTableRow arg="service-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged)"></ArgTableRow>
<ArgTableRow arg="customer-tag" typ="enum (untagged | priority-tagged | tagged | tagged-or-priority-tagged)"></ArgTableRow>
<ArgTableRow arg="mac-src-address" typ="super { macAddr
, [ /macAddr]
 }"></ArgTableRow>
<ArgTableRow arg="mac-dst-address" typ="super { macAddr
, [ /macAddr]
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { enum (ip-or-ipv6 | non-ip) { , ip-or-ipv6:0x10000, non-ip:0x10001 }
, num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="lookup-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (tcp | udp | udp-lite | other)"></ArgTableRow>
<ArgTableRow arg="fragmented" typ="bool"></ArgTableRow>
<ArgTableRow arg="first-fragment" typ="bool"></ArgTableRow>
<ArgTableRow arg="ttl" typ="enum (0 | 1 | max | other)"></ArgTableRow>
<ArgTableRow arg="ip-dst" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="ip-src" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="ecn" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-dst" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="ipv6-src" typ="ip6Prefix"></ArgTableRow>
<ArgTableRow arg="mac-isolation-profile" typ="enum (promiscuous | isolated | community1 | community2)"></ArgTableRow>
<ArgTableRow arg="src-mac-addr-state" typ="enum (sa-found | sa-not-found | dynamic-station-move | static-station-move)"></ArgTableRow>
<ArgTableRow arg="flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (forward | redirect-to-cpu | copy-to-cpu | send-to-new-dst-ports | drop)"></ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { , array-id,  }"></ArgTableRow>
<ArgTableRow arg="new-flow-id" typ="num"></ArgTableRow>
<ArgTableRow arg="attack-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="ingress-vlan-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="egress-vlan-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="isolation-filter-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="new-registered-state" typ="bool"></ArgTableRow>
<ArgTableRow arg="src-mac-learn" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror-to" typ="enum (mirror0 | mirror1)"></ArgTableRow>
<ArgTableRow arg="new-service-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="new-customer-vid" typ="num"></ArgTableRow>
<ArgTableRow arg="egress-vlan-translate-bypass" typ="bool"></ArgTableRow>
<ArgTableRow arg="new-service-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="new-service-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="new-customer-pcp" typ="num"></ArgTableRow>
<ArgTableRow arg="new-customer-dei" typ="num"></ArgTableRow>
<ArgTableRow arg="new-dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="new-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="new-drop-precedence" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="policer" typ="enum"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/acl/policer

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="yellow-rate" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="yellow-burst" typ="num"></ArgTableRow>
<ArgTableRow arg="red-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="red-burst" typ="num"></ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet)"></ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3)"></ArgTableRow>
<ArgTableRow arg="color-awareness" typ="bool"></ArgTableRow>
<ArgTableRow arg="bucket-coupling" typ="bool"></ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark)"></ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 1]
 }"></ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 63]
 }"></ArgTableRow>
<ArgTableRow arg="red-action" typ="enum (drop | forward | remark)"></ArgTableRow>
<ArgTableRow arg="new-dei-for-red" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 1]
 }"></ArgTableRow>
<ArgTableRow arg="new-pcp-for-red" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="new-dscp-for-red" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 63]
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="green-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="yellow-counter" typ="num"></ArgTableRow>
<ArgTableRow arg="red-counter" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/trunk

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="member-ports" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/ingress-port-policer

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="port" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rate" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="burst" typ="num"></ArgTableRow>
<ArgTableRow arg="meter-unit" typ="enum (bit | packet)"></ArgTableRow>
<ArgTableRow arg="meter-len" typ="enum (layer-1 | layer-2 | layer-3)"></ArgTableRow>
<ArgTableRow arg="yellow-action" typ="enum (drop | forward | remark)"></ArgTableRow>
<ArgTableRow arg="new-dei-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 1]
 }"></ArgTableRow>
<ArgTableRow arg="new-pcp-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 7]
 }"></ArgTableRow>
<ArgTableRow arg="new-dscp-for-yellow" typ="alt { enum (remap) { remap:0xffffffff }
, num [ .. 63]
 }"></ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (arp-or-nd, tcp-control, broadcast, unregistered-multicast, registered-multicast, unknown-unicast, known-unicast)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/policer-qos-map

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1" syscap="multiswitch"></ArgTableRow>
<ArgTableRow arg="dscp-for-yellow" typ="num"></ArgTableRow>
<ArgTableRow arg="pcp-for-yellow" typ="num"></ArgTableRow>
<ArgTableRow arg="dei-for-yellow" typ="num"></ArgTableRow>
<ArgTableRow arg="dscp-for-red" typ="num"></ArgTableRow>
<ArgTableRow arg="pcp-for-red" typ="num"></ArgTableRow>
<ArgTableRow arg="dei-for-red" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/l3hw-settings

**Syscap:** crs_prestera
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="autorestart" typ="bool" syscap="!prestera-cpss">Automatically restarts L3HW in case of driver failure</ArgTableRow>
<ArgTableRow arg="fasttrack-hw" typ="bool {  }" syscap="!prestera-ac3">Hardware offloading of FastTrack connections</ArgTableRow>
<ArgTableRow arg="ipv6-hw" typ="bool">IPv6 hardware offloading</ArgTableRow>
<ArgTableRow arg="icmp-reply-on-error" typ="bool">In case of a packet error (TTL, MTU, etc.), either redirect the packet to the CPU for ICMP reply (yes) or silently drop (no)</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="hw-supports-fasttrack" typ="bool">Does the hardware supports FastTrack offloading?</ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/l3hw-settings/advanced

**Syscap:** crs_prestera
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="route-queue-limit-high" typ="num" syscap="!prestera-cpss">Disable indexing if the number of routes in queue exceeds this value</ArgTableRow>
<ArgTableRow arg="route-queue-limit-low" typ="num" syscap="!prestera-cpss">Re-enable indexing if the number of routes in queue drops down to this value</ArgTableRow>
<ArgTableRow arg="shwp-reset-counter" typ="num">Reset the Shortest HW Prefix and try the full route table offloading after this amount of changes in the routing table</ArgTableRow>
<ArgTableRow arg="partial-offload-chunk" typ="num" syscap="prestera-bc2">Minimum number of routes for incremental adding in partial offloading</ArgTableRow>
<ArgTableRow arg="route-index-delay-min" typ="time" syscap="!prestera-cpss">Minimum time between route processing and table indexing</ArgTableRow>
<ArgTableRow arg="route-index-delay-max" typ="time">Maximum time between route processing and table indexing</ArgTableRow>
<ArgTableRow arg="neigh-keepalive-interval" typ="time" syscap="!prestera-cpss">The interval between keeping alive hw-offloaded neighbors (hosts)</ArgTableRow>
<ArgTableRow arg="neigh-discovery-interval" typ="time" syscap="!prestera-cpss">The interval between sending ARP/ND requests to check availability of hw-offloaded neighbors</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-limit" typ="num" syscap="!prestera-cpss">Limits the amount or ARP/ND requests that can be sent at once</ArgTableRow>
<ArgTableRow arg="neigh-discovery-burst-delay" typ="time" syscap="!prestera-cpss">The interval between ARP/ND request bursts</ArgTableRow>
<ArgTableRow arg="neigh-dump-retries" typ="num" syscap="!prestera-cpss">The maximum retry count to offload a neighbor table in case of failure</ArgTableRow>
</ArgTable>

###### interface/ethernet/switch/l3hw-settings/advanced/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="error-code" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory)"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num"></ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="route-queue-rate" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="route-process-rate" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-queue-size" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-queue-rate" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-process-rate" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-hw-offloaded" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-hw-unloaded" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="lpm-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lpm-usage" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lpm-bank-cap" typ="num" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="lpm-bank-usage" typ="multi { array-id, num
 }" syscap="!prestera-ac3"></ArgTableRow>
<ArgTableRow arg="pbr-cap" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pbr-usage" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="pbr-lpm-bank" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="nat-usage" typ="num" syscap="prestera-bc2"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/l3hw-settings/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="enum (ok | stopping | starting | fib-failure | net-failure | switch-failure | fasttrack-failure | out-of-memory)"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-total" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-hw" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-routes-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-shortest-hw-prefix" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv4-hosts" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-total" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-hw" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-routes-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-shortest-hw-prefix" typ="num"></ArgTableRow>
<ArgTableRow arg="ipv6-hosts" typ="num"></ArgTableRow>
<ArgTableRow arg="route-queue-size" typ="num" syscap="!prestera-cpss"></ArgTableRow>
<ArgTableRow arg="nexthop-cap" typ="num"></ArgTableRow>
<ArgTableRow arg="nexthop-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="vxlan-mtu-packet-drop" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-ipv4-conns" typ="num" syscap="prestera-bc2"></ArgTableRow>
<ArgTableRow arg="fasttrack-hw-min-speed" typ="num" syscap="prestera-bc2"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/reset-counters

**Conditions:** !smips
**Type:** Command

#### interface/ethernet/switch/port

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="vlan-mode" typ="enum (disabled | fallback | check | secure)" syscap="oldswitch"></ArgTableRow>
<ArgTableRow arg="vlan-header" typ="enum (leave-as-is | always-strip | add-if-missing)" syscap="oldswitch"></ArgTableRow>
<ArgTableRow arg="default-vlan-id" typ="num" syscap="oldswitch"></ArgTableRow>
<ArgTableRow arg="mirror-ingress" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="mirror-egress" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="mirror-ingress-target" typ="enum (none)" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="ingress-rate" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="egress-rate" typ="num" syscap="switch-rate"></ArgTableRow>
<ArgTableRow arg="storm-rate" typ="num" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="limit-unknown-unicasts" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="limit-unknown-multicasts" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="limit-broadcasts" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="l3-hw-offloading" typ="bool" syscap="crs_prestera">Layer 3 Hardware Offloading. Hardware routing via this port.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/port/reset-counters

**Type:** Command

#### interface/ethernet/switch/port-isolation

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="forwarding-override" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="switch" typ="enum"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/host

**Syscap:** oldswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, alt { enum
, iface_enum
 } { enum
, iface_enum
 }
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="drop" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="share-vlan-learned" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/vlan

**Syscap:** oldswitch
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="independent-learning" typ="bool"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/rule

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="D" typ="dynamic"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="switch" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="ports" typ="multi { array-id, enum
 }" syscap="!crs_prestera"></ArgTableRow>
<ArgTableRow arg="src-mac-address" typ="super { macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="dst-mac-address" typ="super { macAddr
, /macAddr
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="alt { enum () {  }
, num [ .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="vlan-header" typ="bool"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { ipAddr
, /alt { ipAddr
, num [ .. 32]
 } { ipAddr
, num [ .. 32]
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { ipAddr
, /alt { ipAddr
, num [ .. 32]
 } { ipAddr
, num [ .. 32]
 }
 }"></ArgTableRow>
<ArgTableRow arg="protocol" typ="alt { enum () {  }
, num [ .. 255]
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="range"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="range"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { ip6Addr
, /alt { ip6Addr
, num
 } { ip6Addr
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { ip6Addr
, /alt { ip6Addr
, num
 } { ip6Addr
, num
 }
 }"></ArgTableRow>
<ArgTableRow arg="traffic-class" typ="num"></ArgTableRow>
<ArgTableRow arg="flow-label" typ="num"></ArgTableRow>
<ArgTableRow arg="copy-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="redirect-to-cpu" typ="bool"></ArgTableRow>
<ArgTableRow arg="mirror" typ="bool" syscap="switch-mirror-prestera"></ArgTableRow>
<ArgTableRow arg="new-dst-ports" typ="multi { array-id, alt { enum
, iface_enum
 } { enum
, iface_enum
 }
 }">Set new-dst-ports to an empty string to drop packets on the hardware level</ArgTableRow>
<ArgTableRow arg="mirror-ports" typ="multi { array-id, enum
 }" syscap="switch-mv88e6xxx"></ArgTableRow>
<ArgTableRow arg="new-qos-profile" typ="enum" syscap="crs_prestera">Assign QoS profile to the matched packets</ArgTableRow>
<ArgTableRow arg="keep-qos-fields" typ="bool {  }" syscap="crs_prestera">Keep the original QoS fields (PCP, DSCP) or replace them from the QoS profile?</ArgTableRow>
<ArgTableRow arg="new-vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="new-vlan-priority" typ="num"></ArgTableRow>
<ArgTableRow arg="new-vrf" typ="enum" syscap="prestera-cpss">Assign VRF to the matched packets</ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="internal-priority" typ="num"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/prbs/start-prbs

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="phy" typ="bool"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/prbs/stop-prbs

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="phy" typ="bool"></ArgTableRow>
</ArgTable>

##### interface/ethernet/switch/prbs/reset-prbs

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="phy" typ="bool"></ArgTableRow>
</ArgTable>

#### interface/ethernet/switch/stats

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="driver-rx-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="driver-rx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="driver-tx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-bytes" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-short" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-64" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-65-127" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-128-255" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-256-511" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-512-1023" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-1518" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1519-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-too-long" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-broadcast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-pause" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-multicast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fcs-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-align-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-fragment" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-overflow" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-control" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unknown-op" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-length-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-code-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-carrier-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-jabber" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-drop" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-ip-header-checksum-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-tcp-checksum-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-udp-checksum-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-bytes" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-short" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-64" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-65-127" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-128-255" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-256-511" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-512-1023" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-1518" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1519-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-too-long" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-broadcast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multicast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-underrun" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-multiple-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-single-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-excessive-deferred" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-deferred" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-late-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-total-collision" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-pause-honored" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-jabber" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fcs-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-control" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-fragment" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-carrier-sense-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-64" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-65-127" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-128-255" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-256-511" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-512-1023" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-1518" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1519-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom0-drop-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue-custom1-drop-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="policy-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="custom-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="current-learned" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="not-learned" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-unicast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-unicast" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-error-events" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-rx-1024-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rx-1024-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-1024-max" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-codewords" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-corrected" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-uncorrected" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="rs-fec-symbol-error" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-rx-block" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-corrected" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="fc-fec-block-uncorrected" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue0-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue1-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue2-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue3-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue4-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue5-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue6-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-queue7-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue0-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue1-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue2-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue3-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue4-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue5-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue6-byte" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-packet" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="tx-drop-queue7-byte" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

### interface/ethernet/blink

**Type:** Command

### interface/ethernet/cable-test

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (unknown | link-ok | no-link | initializing | auto-init-failed)"></ArgTableRow>
<ArgTableRow arg="cable-pairs" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
</ArgTable>

### interface/ethernet/monitor

**Conditions:** i386
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="status" typ="enum (unknown | link-ok | no-link | initializing | auto-init-failed)"></ArgTableRow>
<ArgTableRow arg="auto-negotiation" typ="enum (incomplete | done | no-negotiation | failed | restarted | disabled | not-supported)"></ArgTableRow>
<ArgTableRow arg="rate" typ="enum (unknown | 10Mbps | 100Mbps | 1Gbps | 2.5Gbps | 5Gbps | 10Gbps | 25Gbps | 40Gbps | 50Gbps | 100Gbps | 200Gbps | 400Gbps)"></ArgTableRow>
<ArgTableRow arg="full-duplex" typ="bool"></ArgTableRow>
<ArgTableRow arg="tx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="rx-flow-control" typ="bool"></ArgTableRow>
<ArgTableRow arg="fec" typ="enum (off | fec74 | fec91)"></ArgTableRow>
<ArgTableRow arg="supported" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="sfp-supported" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="advertising" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="link-partner-advertising" typ="multi { array-id,  }"></ArgTableRow>
<ArgTableRow arg="default-cable-setting" typ="enum (short | standard)"></ArgTableRow>
<ArgTableRow arg="combo-state" typ="enum (copper | sfp)"></ArgTableRow>
<ArgTableRow arg="sfp-module-present" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-rx-loss" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-tx-fault" typ="bool"></ArgTableRow>
<ArgTableRow arg="sfp-type" typ="enum (unknown | SFP/SFP+/SFP28/SFP56 | DWDM-SFP/SFP+ | QSFP | QSFP+ | QSFP28/QSFP56 | QSFPDD | QSFP-CMIS)"></ArgTableRow>
<ArgTableRow arg="sfp-cmis-revision" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="sfp-cmis-module-state" typ="enum (low-power | power-up | ready | power-down | fault)"></ArgTableRow>
<ArgTableRow arg="sfp-connector-type" typ="enum (unknown | SC | LC | optical-pigtail | multifiber-parallel-optic-1x12 | multifiber-parallel-optic-1x16 | copper-pigtail | no-separable-connector | RJ45)"></ArgTableRow>
<ArgTableRow arg="sfp-encoding" typ="enum (unspecified | 8B/10B | 4B/5B | nrz | manchester | sonet | 64B/66B | 256B/257B | pam4)"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-sm" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om1" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om2" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om3" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om4" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-om5" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-cable-assembly" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-link-length-copper-active-om4" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-name" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-part-number" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-revision" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-vendor-serial" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-manufacturing-date" typ="string"></ArgTableRow>
<ArgTableRow arg="sfp-power-class" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-max-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-wavelength" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-dwdm-channel-spacing" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-supply-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-tx-bias-current" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-tx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-rx-power" typ="num"></ArgTableRow>
<ArgTableRow arg="sfp-mac" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="phy-regs" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="eeprom-checksum" typ="bool"></ArgTableRow>
<ArgTableRow arg="eeprom" typ="string"></ArgTableRow>
</ArgTable>

### interface/ethernet/poe

**Syscap:** (poe or poe-in)
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on)" syscap="(!poe-4p-power and poe)"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-priority" typ="num" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-enabled" typ="bool" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-address" typ="alt { ipAddr
, ip6Addr
, macAddr
 }" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-ping-timeout" typ="time" syscap="poe"></ArgTableRow>
<ArgTableRow arg="power-cycle-interval" typ="alt { enum (none) { none:0 }
, time
 }" syscap="poe"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="poe-controller" typ="string" syscap="(poe and option)"></ArgTableRow>
</ArgTable>

#### interface/ethernet/poe/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="poe-out" typ="enum (off | auto-on | forced-on | forced-on-a | forced-on-bt)" syscap="poe"></ArgTableRow>
<ArgTableRow arg="poe-voltage" typ="enum (auto | low | high)" syscap="poe">PoE out voltage selection</ArgTableRow>
<ArgTableRow arg="poe-out-status" typ="enum (disabled | waiting-for-load | powered-on | overload | short-circuit | voltage-too-low | current-too-low | power-cycle | voltage-too-high | controller-error | controller-upgrade | voltage-on-poe-in | no-valid-PSU | controller-init | low-voltage-too-low | lldp-power-off)"></ArgTableRow>
<ArgTableRow arg="poe-out-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-current" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power" typ="num"></ArgTableRow>
<ArgTableRow arg="poe-out-power-pair" typ="enum (b | a | bt)"></ArgTableRow>
<ArgTableRow arg="power-cycle-host-alive" typ="bool"></ArgTableRow>
<ArgTableRow arg="power-cycle-after" typ="time"></ArgTableRow>
</ArgTable>

#### interface/ethernet/poe/power-cycle

**Syscap:** poe
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
</ArgTable>

#### interface/ethernet/poe/settings

**Syscap:** poesettings
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ether1-poe-in-long-cable" typ="bool" syscap="poeattiny"></ArgTableRow>
<ArgTableRow arg="psu-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin1-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin2-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-in-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="version" typ="string" syscap="poeattiny"></ArgTableRow>
<ArgTableRow arg="routerboard-max-self-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-out-limit-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="psu2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="jack2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin1-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="2pin2-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
<ArgTableRow arg="poe-in-poe-out-max-power" typ="num" syscap="poepwrchg"></ArgTableRow>
</ArgTable>

### interface/ethernet/reset-counters

**Type:** Command

### interface/ethernet/reset-mac-address

**Type:** Command
