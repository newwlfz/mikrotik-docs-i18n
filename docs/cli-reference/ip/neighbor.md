# Neighbor

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/neighbor

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="identity" typ="string"></ArgTableRow>
<ArgTableRow arg="platform" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="unpack" typ="enum (none | simple | uncompress-headers | uncompress-all)"></ArgTableRow>
<ArgTableRow arg="age" typ="time"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="software-id" typ="string"></ArgTableRow>
<ArgTableRow arg="board" typ="string"></ArgTableRow>
<ArgTableRow arg="ipv6" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface-name" typ="string"></ArgTableRow>
<ArgTableRow arg="system-description" typ="string"></ArgTableRow>
<ArgTableRow arg="system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)"></ArgTableRow>
<ArgTableRow arg="system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)"></ArgTableRow>
<ArgTableRow arg="discovered-by" typ="ubit (cdp, lldp, mndp)"></ArgTableRow>
<ArgTableRow arg="running" typ="multi { array-id, string
 }" unset="1"></ArgTableRow>
</ArgTable>

### ip/neighbor/discovery-settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="discover-interface-list" typ="super { !
, enum
 }"></ArgTableRow>
<ArgTableRow arg="discover-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="lldp-med" typ="bool"></ArgTableRow>
<ArgTableRow arg="lldp-med-net-policy-vlan" typ="alt { enum (disabled) { disabled:nv::BADID }
, num [ .. 4094]
 }"></ArgTableRow>
<ArgTableRow arg="lldp-mac-phy-config" typ="bool"></ArgTableRow>
<ArgTableRow arg="lldp-max-frame-size" typ="bool"></ArgTableRow>
<ArgTableRow arg="lldp-vlan-info" typ="bool"></ArgTableRow>
<ArgTableRow arg="lldp-poe-power" typ="bool" syscap="poe"></ArgTableRow>
<ArgTableRow arg="lldp-dcbx" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="protocol" typ="ubit (cdp, lldp, mndp)"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (tx-and-rx | tx-only | rx-only)"></ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string"></ArgTableRow>
</ArgTable>

### ip/neighbor/lldp

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="multi { iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="address4" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="address6" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr"></ArgTableRow>
<ArgTableRow arg="lldp-chassis-id-subtype" typ="enum (chassis-component | interface-alias | port-component | mac-address | network-address | interface-name | local)"></ArgTableRow>
<ArgTableRow arg="lldp-chassis-id" typ="string"></ArgTableRow>
<ArgTableRow arg="lldp-port-id-subtype" typ="enum (interface-alias | port-component | mac-address | network-address | interface-name | agent-circuit-id | local)"></ArgTableRow>
<ArgTableRow arg="lldp-port-id" typ="string"></ArgTableRow>
<ArgTableRow arg="lldp-port-description" typ="string"></ArgTableRow>
<ArgTableRow arg="lldp-system-name" typ="string"></ArgTableRow>
<ArgTableRow arg="lldp-system-description" typ="string"></ArgTableRow>
<ArgTableRow arg="lldp-ttl" typ="time"></ArgTableRow>
<ArgTableRow arg="lldp-system-caps" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)"></ArgTableRow>
<ArgTableRow arg="lldp-system-caps-enabled" typ="ubit (other, repeater, bridge, wlan-ap, router, telephone, docsis-cable-device, station-only)"></ArgTableRow>
</ArgTable>
