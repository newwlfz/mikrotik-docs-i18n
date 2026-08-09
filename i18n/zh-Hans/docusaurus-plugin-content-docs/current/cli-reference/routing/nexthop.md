# Nexthop

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/nexthop

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="unresolved">未解析</ArgTableRow>
<ArgTableRow arg="R" typ="reachable">可达</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="afi" typ="enum (bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link)" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46iv)"></ArgTableRow>
<ArgTableRow arg="gw-state" typ="enum (unreachable | reachable | recursive | inactive)"></ArgTableRow>
<ArgTableRow arg="prev-reachable" typ="bool"></ArgTableRow>
<ArgTableRow arg="scope" typ="num"></ArgTableRow>
<ArgTableRow arg="target-scope" typ="num"></ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)"></ArgTableRow>
<ArgTableRow arg="gw-check-ok" typ="bool"></ArgTableRow>
<ArgTableRow arg="interface-ok" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp-vpn" typ="bool"></ArgTableRow>
<ArgTableRow arg="hops" typ="num"></ArgTableRow>
<ArgTableRow arg="routes" typ="num"></ArgTableRow>
<ArgTableRow arg="immediate-gw.address" typ="object { address (flags=64iv)
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.weight" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.flap-count" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.interface-idx" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.mpls-peer-id" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.mpls-label" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="immediate-gw.blackhole" typ="object { bool
 }"></ArgTableRow>
<ArgTableRow arg="links" typ="object { enum (output | input) { output:r5n::LT_OUTPUT, input:r5n::LT_INPUT }
, address (flags=46iv/)
, num
, num
, switch
, switch
, switch
 }"></ArgTableRow>
</ArgTable>

### routing/nexthop/dump-dot

**类型：** 命令