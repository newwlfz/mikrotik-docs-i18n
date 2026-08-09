# 地址列表

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ipv6/firewall/address-list

**软件包：** ipv6
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="enum" mandatory="1">将IP地址添加到的地址列表名称。</ArgTableRow>
<ArgTableRow arg="address" typ="alt { ip6Prefix
, string
 }">要添加到地址列表的单个IPv6地址或前缀，或一个DNS名称。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">地址将从地址列表中移除的时间。如果未指定超时时间，地址将永久存储在地址列表中。</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">该条目是否为动态创建。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="creation-time" typ="date">条目创建的时间。</ArgTableRow>
</ArgTable>