# Filter

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/filter

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="community" typ="alt { super { num [ .. 0xffff]
, :num [ .. 0xffff]
 } { num [ .. 0xffff]
, :num [ .. 0xffff]
 }
, enum (internet | graceful-shutdown | accept-own | route-filter-xlate-4 | route-filter-4 | route-filter-xlate-6 | route-filter-6 | llgr-stale | no-llgr | accept-own-nh | blackhole | no-export | no-advertise | no-export-subconfed | no-peer) { internet:r5fc1::WK_INTERNET, graceful-shutdown:r5fc1::WK_GRACEFUL_SHUTDOWN, accept-own:r5fc1::WK_ACCEPT_OWN, route-filter-xlate-4:r5fc1::WK_ROUTE_FILTER_XLATE_4, route-filter-4:r5fc1::WK_ROUTE_FILTER_4, route-filter-xlate-6:r5fc1::WK_ROUTE_FILTER_XLATE_6, route-filter-6:r5fc1::WK_ROUTE_FILTER_6, llgr-stale:r5fc1::WK_LLGR_STALE, no-llgr:r5fc1::WK_NO_LLGR, accept-own-nh:r5fc1::WK_ACCEPT_OWN_NH, blackhole:r5fc1::WK_BLACKHOLE, no-export:r5fc1::WK_NO_EXPORT, no-advertise:r5fc1::WK_NO_ADVERTISE, no-export-subconfed:r5fc1::WK_NO_EXPORT_SUBCONFED, no-peer:r5fc1::WK_NOPEER }
 }"></ArgTableRow>
<ArgTableRow arg="community" typ="alt { super { enum (rt | soo) { rt:r5fc2::VALUE_TYPE_RT, soo:r5fc2::VALUE_TYPE_SOO }
, :address (flags=R)
 } { enum (rt | soo) { rt:r5fc2::VALUE_TYPE_RT, soo:r5fc2::VALUE_TYPE_SOO }
, :address (flags=R)
 }
, num
 }"></ArgTableRow>
<ArgTableRow arg="community" typ="super { num
, :num
, :num
 }"></ArgTableRow>
</ArgTable>

### routing/filter/chain

**Type:** Directory

Dynamic list of filter rule chains that can be referenced in BGP/OSPF or other routing protocol configuration.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

### routing/filter/community-ext-list

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Reference name.</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">
List of extended communities expressed as a **raw** integer value or in the typed format: `type:value`, where type can be:
- `rt` - route-target
- `soo` -  site of origin.

The value depends on the type.
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.</ArgTableRow>
</ArgTable>

### routing/filter/community-large-list

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Reference name.</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">List of large communities expressed in the following format: `admin:value1:value2`, where each section can be an integer [0..4294967295].</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.</ArgTableRow>
</ArgTable>

### routing/filter/community-list

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Reference name.</ArgTableRow>
<ArgTableRow arg="communities" typ="object {  }">
List of communities expressed either as a **well-known** name or in the following format: `as:number`, where each section can be integer [0..65535].
Accepted **well-known** names:
- `accept-own`
- `graceful-shutdown`
- `no-advertise`
- `no-llgr`
- `route-filter-6`
- `accept-own-nh`
- `internet`
- `no-export`
- `no-peer`
- `route-filter-xlate-4`
- `blackhole`
- `llgr-stale`
- `local-as`
- `route-filter-4`
- `route-filter-xlate-6`
</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">Regexp matcher to match communities. The community set with only the regexp parameter cannot be used to append/delete communities.</ArgTableRow>
</ArgTable>

### routing/filter/filter-wizard

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="super { !
, alt { enum
, address (flags=46/+)
 } { enum
, address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="dst-len" typ="super { !
, range [ .. 128]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="super { !
, alt { enum
, address (flags=46/+)
 } { enum
, address (flags=46/+)
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="match-chain" typ="super { !
, enum
 }" unset="1">returns true if provided chain did not reject</ArgTableRow>
<ArgTableRow arg="routing-table" typ="super { !
, enum
 }" unset="1">name of the routing table the route was imported from</ArgTableRow>
<ArgTableRow arg="afi" typ="super { !
, ubit (ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco) { ip, ipv6, l2vpn, vpnv4, vpnv6, l2vpn-cisco }
 }" unset="1">address family of the route</ArgTableRow>
<ArgTableRow arg="protocol" typ="super { !
, ubit (connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn) { connected, static, rip, ospf, isis, bgp, vpn, dhcp, fantasy, modem, slaac, bgp-mpls-vpn }
 }" unset="1">protocol type from which the route was imported</ArgTableRow>
<ArgTableRow arg="bgp-atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-local-origin" typ="bool">returns true if prefix is locally originated, e.g BGP network</ArgTableRow>
<ArgTableRow arg="suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="blackhole" typ="bool">matches blackhole routes</ArgTableRow>
<ArgTableRow arg="ospf-type" typ="super { !
, enum (intra | inter | ext1 | ext2 | nssa1 | nssa2) { intra:0, inter:1, ext1:2, ext2:3, nssa1:7, nssa2:8 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki" typ="super { !
, enum (unknown | valid | invalid) { unknown:r5r::RPKI_UNKNOWN, valid:r5r::RPKI_VALID, invalid:r5r::RPKI_INVALID }
 }" unset="1">RPKI validation status of the prefix</ArgTableRow>
<ArgTableRow arg="bgp-origin" typ="super { !
, ubit (igp, egp, incomplete) { igp, egp, incomplete }
 }" unset="1">matches BGP Origin attribute</ArgTableRow>
<ArgTableRow arg="bgp-as-path" typ="string">regexp that matches BGP AS-Path attribute, see documentation for more details</ArgTableRow>
<ArgTableRow arg="bgp-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-ext-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-match" typ="super { !
, enum () {  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities" typ="object {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-large-communities-list-name" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="distance" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="scope-target" typ="super { !
, alt { enum
, range [ .. 255]
 } { enum
, range [ .. 255]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-weight" typ="super { !
, alt { enum
, range [ .. 65535]
 } { enum
, range [ .. 65535]
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-local-pref" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-med" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-out-med" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="bgp-as-path-length" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="ospf-metric" typ="super { !
, alt { enum
, range
 } { enum
, range
 }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-distance" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="set-scope" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-scope-target" typ="alt { enum () {  }
, num [1 .. 255]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-weight" typ="alt { enum () {  }
, num [ .. 65535]
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-local-pref" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }">set a value of the BGP Local-Pref attribute</ArgTableRow>
<ArgTableRow arg="set-bgp-med" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-bgp-out-med" typ="alt { enum () {  }
, num
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="set-suppress-hw-offload" typ="bool" syscap="crs_prestera"></ArgTableRow>
<ArgTableRow arg="set-use-te-nexthop" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-blackhole" typ="bool"></ArgTableRow>
<ArgTableRow arg="set-gw-check" typ="enum (none | arp | ping | bfd)">set gateway check</ArgTableRow>
<ArgTableRow arg="set-gateway" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="set-comment" typ="string"></ArgTableRow>
<ArgTableRow arg="set-bgp-communities" typ="object {  }">set a value of the BGP Communities attribute</ArgTableRow>
<ArgTableRow arg="set-bgp-communities-list" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="set-bgp-ext-communities" typ="object {  }"></ArgTableRow>
<ArgTableRow arg="set-bgp-large-communities" typ="object {  }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum ()" unset="1"></ArgTableRow>
<ArgTableRow arg="jump-target-chain" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="rpki-verify" typ="enum" unset="1">Enable RPKI verification in the current chain from specified RPKI group</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>

### routing/filter/num-list

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="range" typ="range"></ArgTableRow>
</ArgTable>

### routing/filter/rule

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="rule" typ="remote"></ArgTableRow>
</ArgTable>

### routing/filter/select-rule

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="chain" typ="enum" unset="1" mandatory="1"></ArgTableRow>
<ArgTableRow arg="do-where" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-num" typ="super { enum () {  }
, >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-group-prfx" typ="super { enum () {  }
, >enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-num" typ="super { enum () {  }
, >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) { largest-none-best:r5srl::SELECT_CMP_LB, largest-none-worst:r5srl::SELECT_CMP_LW, smallest-none-best:r5srl::SELECT_CMP_SB, smallest-none-worst:r5srl::SELECT_CMP_SW }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-select-prfx" typ="super { enum () {  }
, >enum (largest-none-best | largest-none-worst | smallest-none-best | smallest-none-worst) { largest-none-best:r5srl::SELECT_CMP_LB, largest-none-worst:r5srl::SELECT_CMP_LW, smallest-none-best:r5srl::SELECT_CMP_SB, smallest-none-worst:r5srl::SELECT_CMP_SW }
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="do-take" typ="num"></ArgTableRow>
<ArgTableRow arg="do-jump" typ="enum"></ArgTableRow>
</ArgTable>

### routing/filter/sync

**Type:** Command

### routing/filter/test-as-path-regexp

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="regexp" typ="string"></ArgTableRow>
<ArgTableRow arg="as-path" typ="object { num
 }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="result" typ="string"></ArgTableRow>
</ArgTable>
