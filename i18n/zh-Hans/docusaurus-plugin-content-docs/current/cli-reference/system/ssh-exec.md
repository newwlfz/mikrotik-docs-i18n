# SSH 执行

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/ssh-exec

**软件包：** security
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="alt { ipAddr
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="command" typ="string"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { ipAddr
, ip6Addr
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="output-to-file" typ="string">将输出写入文件，而非写入'output'变量</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="exit-code" typ="num"></ArgTableRow>
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>