# E Mail

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/e-mail

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="alt { ip6Addr
, ipAddr
, string
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="from" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">TLS certificate validation</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="last-status" typ="enum (none | resolving-dns | in-progress | failed | succeeded)"></ArgTableRow>
<ArgTableRow arg="last-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
</ArgTable>

### tool/e-mail/send

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="server" typ="alt { ip6Addr
, ipAddr
, string
 }"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="to" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="cc" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="from" typ="string"></ArgTableRow>
<ArgTableRow arg="subject" typ="string"></ArgTableRow>
<ArgTableRow arg="body" typ="string"></ArgTableRow>
<ArgTableRow arg="file" typ="multi { array-id, file
 }"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="tls" typ="enum (no | yes | starttls)"></ArgTableRow>
<ArgTableRow arg="certificate-verification" typ="enum (no | yes | yes-without-crl)">TLS certificate validation</ArgTableRow>
</ArgTable>
