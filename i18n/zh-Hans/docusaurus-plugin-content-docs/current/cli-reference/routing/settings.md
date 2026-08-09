# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/settings

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="single-process" typ="bool">启用后，所有与路由相关的进程将合并为单个路由进程，以减少内存占用。禁用后，路由相关进程将独立运行，在某些配置下可提升性能与稳定性。默认情况下，仅对内存为 64 MB 或更低的设备启用单进程模式。此更改需重启设备方可生效。</ArgTableRow>
<ArgTableRow arg="dynamic-in-chain" typ="enum" unset="1">用于处理所有动态添加路由的链名称。</ArgTableRow>
<ArgTableRow arg="connected-in-chain" typ="enum" unset="1">用于处理 `connected` 路由的链名称。</ArgTableRow>
<ArgTableRow arg="check-gateway-ping-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="check-gateway-ping-count" typ="num"></ArgTableRow>
<ArgTableRow arg="policy-rules" typ="object { enum
 }">定义路由决策规则的顺序。默认情况下，`user` 是用户自定义 `/routing/rule` 条目添加的链。您可以在列表中的任意位置添加自定义链。</ArgTableRow>
</ArgTable>