# Veth

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/veth

**条件：** !smips
**系统能力：** container
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">名称</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC地址</ArgTableRow>
<ArgTableRow arg="container-mac-address" typ="macAddr">容器MAC地址</ArgTableRow>
<ArgTableRow arg="address" typ="multi { address (flags=46/)
 }">地址</ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=4)">网关</ArgTableRow>
<ArgTableRow arg="gateway6" typ="address (flags=6)">IPv6网关</ArgTableRow>
<ArgTableRow arg="dhcp" typ="bool">DHCP</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="dhcp-address" typ="address (flags=46/)">DHCP地址</ArgTableRow>
</ArgTable>