# ARP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/arp

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">无效</ArgTableRow>
<ArgTableRow arg="H" typ="dhcp">DHCP</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="P" typ="published">已发布</ArgTableRow>
<ArgTableRow arg="C" typ="complete">完整</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="ipAddr">IP地址</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">MAC地址</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">接口</ArgTableRow>
<ArgTableRow arg="published" typ="bool">已发布</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="string">状态</ArgTableRow>
<ArgTableRow arg="vrf" typ="enum">VRF</ArgTableRow>
</ArgTable>