# 规则

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/rule

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="地址 (标志=64iv/)" unset="1">匹配源地址。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="地址 (标志=64iv/)" unset="1">匹配目的地址。</ArgTableRow>
<ArgTableRow arg="routing-mark" typ="枚举" unset="1">匹配特定的路由标记。</ArgTableRow>
<ArgTableRow arg="interface" typ="接口枚举" unset="1">匹配入接口。</ArgTableRow>
<ArgTableRow arg="action" typ="枚举 (lookup | lookup-only-in-table | unreachable | drop | mangle)">
对匹配数据包执行的操作：
- drop - 静默丢弃数据包。
- lookup - 在路由表中执行查找。
- lookup-only-in-table - 仅在指定的路由表中执行查找（参见 `table` 参数）。
- unreachable - 生成 ICMP 不可达消息并发送至源地址。
- mangle - 通过防火墙 mangle 规则执行操作。
</ArgTableRow>
<ArgTableRow arg="table" typ="枚举 (local)">用于查找的路由表名称。</ArgTableRow>
<ArgTableRow arg="min-prefix" typ="数字" unset="1">对于由此路由规则处理的数据包，隐藏路由表中指定前缀长度的路由。这等同于 Linux IP 规则中的 `suppress_prefixlength`。例如，将该值设置为 0 可在路由决策中抑制默认路由。</ArgTableRow>
<ArgTableRow arg="vrf" typ="开关"></ArgTableRow>
<ArgTableRow arg="realm" typ="数字 {  }" unset="1"></ArgTableRow>
<ArgTableRow arg="chain" typ="枚举" unset="1">路由决策规则所使用的链名称。默认情况下，当未指定链时使用 `user`。如果链名称与内置路由决策名称匹配，则用户创建的规则会添加在该决策之后。例如，如果 `chain=mangle`，则此链中用户创建的规则位于 `mangle` 决策之后。</ArgTableRow>
</ArgTable>