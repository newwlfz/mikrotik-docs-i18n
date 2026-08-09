# Socks

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/socks

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="connection-idle-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="max-connections" typ="num"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="version" typ="enum (4 | 5)"></ArgTableRow>
<ArgTableRow arg="auth-method" typ="enum (none | password)"></ArgTableRow>
</ArgTable>

### ip/socks/access

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="super { !
, alt { ipRange
, ip6Prefix
 } { ipRange
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="src-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="super { !
, alt { ipRange
, ip6Prefix
, string
 } { ipRange
, ip6Prefix
, string
 }
 }"></ArgTableRow>
<ArgTableRow arg="dst-port" typ="super { !
, num [0 .. 65535]
, -num [0 .. 65535]
 }"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (deny | allow)"></ArgTableRow>
</ArgTable>

### ip/socks/connections

**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (unknown | out | in)"></ArgTableRow>
<ArgTableRow arg="tx" typ="num"></ArgTableRow>
<ArgTableRow arg="rx" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="user" typ="enum"></ArgTableRow>
</ArgTable>

### ip/socks/users

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="only-one" typ="bool"></ArgTableRow>
<ArgTableRow arg="rate-limit" typ="string"></ArgTableRow>
</ArgTable>
