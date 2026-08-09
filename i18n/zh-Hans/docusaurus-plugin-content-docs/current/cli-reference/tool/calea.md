# Calea

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/calea

**软件包：** calea
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="case-id" typ="num"></ArgTableRow>
<ArgTableRow arg="case-name" typ="string"></ArgTableRow>
<ArgTableRow arg="intercept-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="intercept-port" typ="num"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (pcap | limited)"></ArgTableRow>
<ArgTableRow arg="file-root" typ="string"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-size" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcap-file-stop-count" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="pcap-file-hash-method" typ="enum (none | md5 | sha1 | sha256)"></ArgTableRow>
<ArgTableRow arg="limited-file-stop-interval" typ="time {  }"></ArgTableRow>
<ArgTableRow arg="limited-file-hash-method" typ="enum (none | md5 | sha1 | sha256)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="access-session-id" typ="num"></ArgTableRow>
<ArgTableRow arg="packets" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
</ArgTable>