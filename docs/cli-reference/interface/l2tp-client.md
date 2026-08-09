# L2tp Client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/l2tp-client

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="enum (no | yes | exclusively)"></ArgTableRow>
<ArgTableRow arg="use-ipsec" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipsec-secret" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool"></ArgTableRow>
<ArgTableRow arg="allow" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
<ArgTableRow arg="random-source-port" typ="bool"></ArgTableRow>
<ArgTableRow arg="l2tp-proto-version" typ="enum (l2tpv2 | l2tpv3-ip | l2tpv3-udp)"></ArgTableRow>
<ArgTableRow arg="l2tpv3-circuit-id" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="l2tpv3-cookie-length" typ="enum (0 | 4-bytes | 8-bytes)"></ArgTableRow>
<ArgTableRow arg="l2tpv3-digest-hash" typ="enum (none | md5 | sha1)"></ArgTableRow>
</ArgTable>

### interface/l2tp-client/monitor

**Package:** ppp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="mru" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr"></ArgTableRow>
</ArgTable>
