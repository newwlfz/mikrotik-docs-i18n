# DHCP 中继

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/dhcp-relay

**软件包：** dhcp
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="dhcp-server-vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="multi { ipAddr
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum (none) { none:0 }
, time
 }"></ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="add-relay-info" typ="bool"></ArgTableRow>
<ArgTableRow arg="relay-info-remote-id" typ="string"></ArgTableRow>
<ArgTableRow arg="local-address-as-src-ip" typ="bool"></ArgTableRow>
</ArgTable>

### ip/dhcp-relay/monitor

**软件包：** dhcp
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="requests" typ="num"></ArgTableRow>
<ArgTableRow arg="responses" typ="num"></ArgTableRow>
</ArgTable>

### ip/dhcp-relay/reset-counters

**软件包：** dhcp
**类型：** 命令