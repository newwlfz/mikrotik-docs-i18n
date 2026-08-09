# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/settings

**条件：** !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="dynamic-label-range" typ="range">用于动态分配的标签号范围。前16个标签保留用于特殊用途（如RFC中所定义）。如果您打算静态配置标签，请调整动态默认范围，使其不包含将在静态配置中使用的数字。</ArgTableRow>
<ArgTableRow arg="propagate-ttl" typ="bool">是否将TTL值从IP头部复制到MPLS头部。如果此选项设置为**no**，则MPLS云内部的跳数将对traceroute不可见。</ArgTableRow>
<ArgTableRow arg="allow-fast-path" typ="bool">启用/禁用MPLS快速路径支持。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="mpls-fast-path-packets" typ="num"></ArgTableRow>
<ArgTableRow arg="mpls-fast-path-bytes" typ="num"></ArgTableRow>
</ArgTable>