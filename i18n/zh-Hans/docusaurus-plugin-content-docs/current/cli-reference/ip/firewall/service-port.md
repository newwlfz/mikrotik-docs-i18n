# 服务端口

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/service-port

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="ports" typ="multi { , num [0 .. 65535]
 }">服务所使用的端口号。</ArgTableRow>
<ArgTableRow arg="sip-direct-media" typ="bool">是否启用 SIP 直接媒体。</ArgTableRow>
<ArgTableRow arg="sip-timeout" typ="time">SIP 超时值。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">服务的名称。</ArgTableRow>
</ArgTable>