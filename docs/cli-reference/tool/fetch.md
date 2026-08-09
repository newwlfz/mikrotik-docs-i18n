# Fetch

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/fetch

**Conditions:** arm64
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="url" typ="string"></ArgTableRow>
<ArgTableRow arg="output" typ="enum (none | file | user | user-with-headers)">where to output data, works for all protocols</ArgTableRow>
<ArgTableRow arg="http-method" typ="enum (get | post | put | delete | head | patch)"></ArgTableRow>
<ArgTableRow arg="http-auth-scheme" typ="enum (basic | digest)"></ArgTableRow>
<ArgTableRow arg="http-data" typ="string">POST or PUT request body data</ArgTableRow>
<ArgTableRow arg="http-header-field" typ="multi { array-id, string
 }">add http header fields</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">https certificate validation</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { address (flags=46vi)
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }">source address for HTTP, HTTPS only</ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (http | https | ftp | tftp | sftp)"></ArgTableRow>
<ArgTableRow arg="http-content-encoding" typ="enum (deflate | gzip)">encode payload and add corresponding Content-Encoding header; for HTTP POST and PUT only</ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (any | ipv4 | ipv6)"></ArgTableRow>
<ArgTableRow arg="src-path" typ="file"></ArgTableRow>
<ArgTableRow arg="dst-path" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="host" typ="string"></ArgTableRow>
<ArgTableRow arg="ascii" typ="bool">ftp transfer type</ArgTableRow>
<ArgTableRow arg="upload" typ="bool">ftp and tftp transfer direction</ArgTableRow>
<ArgTableRow arg="keep-result" typ="bool">depracated, use 'output' argument</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { time [1 .. 604800]
, enum (none) { none:0 }
 }">seconds, default 10</ArgTableRow>
<ArgTableRow arg="http-max-redirect-count" typ="num">default 0, i.e. no redirects</ArgTableRow>
<ArgTableRow arg="http-percent-encoding" typ="bool">percent-encodes every character in path except for alphanumeric and the following characters: -._~/?^=:</ArgTableRow>
<ArgTableRow arg="http-version" typ="enum (http1_1 | http2)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (none | connecting | requesting | downloading | uploading | finished | failed)"></ArgTableRow>
<ArgTableRow arg="code" typ="num"></ArgTableRow>
<ArgTableRow arg="downloaded" typ="num"></ArgTableRow>
<ArgTableRow arg="uploaded" typ="num"></ArgTableRow>
<ArgTableRow arg="total" typ="num"></ArgTableRow>
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="data" typ="string"></ArgTableRow>
<ArgTableRow arg="http-headers" typ="object { super { string
, : string
 } { string
, : string
 }
 }"></ArgTableRow>
</ArgTable>
