# Torch

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/torch

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="src-address" typ="super { !
, ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, ipPrefix
 }"></ArgTableRow>
<ArgTableRow arg="src-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="dst-address6" typ="super { !
, ip6Prefix
 }"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum (any)"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum (any)"></ArgTableRow>
<ArgTableRow arg="port" typ="enum (any)"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="alt { num [ .. 4095]
, enum (any) { any:0xffff }
 }"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="vlan-id" typ="num"></ArgTableRow>
<ArgTableRow arg="mac-protocol" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="ip-protocol" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dscp" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rx" typ="num"></ArgTableRow>
<ArgTableRow arg="tx-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="rx-packets" typ="num"></ArgTableRow>
</ArgTable>
