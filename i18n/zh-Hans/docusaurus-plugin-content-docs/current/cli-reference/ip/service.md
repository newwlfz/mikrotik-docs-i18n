# 服务

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/service

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="c" typ="connection">连接</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
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

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="container" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="netns" typ="num"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="proto" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="local" typ="ip6Addr"></ArgTableRow>
<ArgTableRow arg="remote" typ="composite { ,  }"></ArgTableRow>
</ArgTable>

### ip/service/webserver

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
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