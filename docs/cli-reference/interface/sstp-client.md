# Sstp Client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/sstp-client

**Package:** ppp
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="H" typ="hw-crypto">hw-crypto</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="max-mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="max-mru" typ="num"></ArgTableRow>
<ArgTableRow arg="mrru" typ="num"></ArgTableRow>
<ArgTableRow arg="connect-to" typ="address (flags=D46v)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="http-proxy" typ="alt { ipAddr
, ip6Addr
, string
 }"></ArgTableRow>
<ArgTableRow arg="proxy-port" typ="num"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="verify-server-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="verify-server-address-from-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="profile" typ="enum"></ArgTableRow>
<ArgTableRow arg="keepalive-timeout" typ="enum (disabled)"></ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool"></ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="dial-on-demand" typ="bool"></ArgTableRow>
<ArgTableRow arg="authentication" typ="ubit (pap, chap, mschap1, mschap2)"></ArgTableRow>
<ArgTableRow arg="pfs" typ="enum (no | yes | required)"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2)"></ArgTableRow>
<ArgTableRow arg="ciphers" typ="ubit (aes256-sha, aes256-gcm-sha384)"></ArgTableRow>
<ArgTableRow arg="add-sni" typ="bool"></ArgTableRow>
</ArgTable>

### interface/sstp-client/monitor

**Package:** ppp
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="encoding" typ="string"></ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="remote-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="local-ipv6-address" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote-ipv6-address" typ="ip6Addr"></ArgTableRow>
</ArgTable>
