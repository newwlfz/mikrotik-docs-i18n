# Service

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/service

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">invalid</ArgTableRow>
<ArgTableRow arg="c" typ="connection">connection</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="address" typ="object { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="available-from" typ="object { alt { ipPrefix
, ip6Prefix
 } { ipPrefix
, ip6Prefix
 }
 }"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="tls-version" typ="enum (any | only-1.2)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="max-sessions" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="container" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="netns" typ="num"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="proto" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="local" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote" typ="composite { ,  }"></ArgTableRow>
</ArgTable>

### ip/service/webserver

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="index-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="webfig-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="graphs-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="rest-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="crl-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="scep-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="acme-plain" typ="bool"></ArgTableRow>
<ArgTableRow arg="index-secure" typ="bool"></ArgTableRow>
<ArgTableRow arg="webfig-secure" typ="bool"></ArgTableRow>
<ArgTableRow arg="graphs-secure" typ="bool"></ArgTableRow>
<ArgTableRow arg="rest-secure" typ="bool"></ArgTableRow>
</ArgTable>
