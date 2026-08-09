# Fetch

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/fetch

**条件:** arm64
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="url" typ="string"></ArgTableRow>
<ArgTableRow arg="output" typ="enum (none | file | user | user-with-headers)">数据输出位置，适用于所有协议</ArgTableRow>
<ArgTableRow arg="http-method" typ="enum (get | post | put | delete | head | patch)"></ArgTableRow>
<ArgTableRow arg="http-auth-scheme" typ="enum (basic | digest)"></ArgTableRow>
<ArgTableRow arg="http-data" typ="string">POST 或 PUT 请求体数据</ArgTableRow>
<ArgTableRow arg="http-header-field" typ="multi { array-id, string
 }">添加 HTTP 头字段</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (no | yes | yes-without-crl)">HTTPS 证书验证</ArgTableRow>
<ArgTableRow arg="certificate" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="alt { address (flags=46vi)
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }">源地址，仅适用于 HTTP、HTTPS</ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (http | https | ftp | tftp | sftp)"></ArgTableRow>
<ArgTableRow arg="http-content-encoding" typ="enum (deflate | gzip)">对负载进行编码并添加相应的 Content-Encoding 头；仅适用于 HTTP POST 和 PUT</ArgTableRow>
<ArgTableRow arg="ip-type" typ="enum (any | ipv4 | ipv6)"></ArgTableRow>
<ArgTableRow arg="src-path" typ="file"></ArgTableRow>
<ArgTableRow arg="dst-path" typ="file"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="host" typ="string"></ArgTableRow>
<ArgTableRow arg="ascii" typ="bool">FTP 传输类型</ArgTableRow>
<ArgTableRow arg="upload" typ="bool">FTP 和 TFTP 传输方向</ArgTableRow>
<ArgTableRow arg="keep-result" typ="bool">已弃用，请使用 'output' 参数</ArgTableRow>
<ArgTableRow arg="idle-timeout" typ="alt { time [1 .. 604800]
, enum (none) { none:0 }
 }">秒，默认值为 10</ArgTableRow>
<ArgTableRow arg="http-max-redirect-count" typ="num">默认值为 0，即不进行重定向</ArgTableRow>
<ArgTableRow arg="http-percent-encoding" typ="bool">对路径中的每个字符进行百分号编码，但字母数字字符及以下字符除外：-._~/?^=:</ArgTableRow>
<ArgTableRow arg="http-version" typ="enum (http1_1 | http2)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
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