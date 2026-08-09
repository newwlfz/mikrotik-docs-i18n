# Iface

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/interface

**条件：** !smips
**类型：** 目录

配置 MPLS MTU（路径 MTU + MPLS 标签大小）在路径上可能存在多种 MTU 值的情况下非常有用。将 MPLS MTU 配置为能够通过所有跳点的最小值，可以确保 MPLS 数据包不会在不支持足够大 MTU 的设备上被静默丢弃。

```ros
[admin@rack1_b35_CCR1036] /mpls/interface> print 
Flags: X - disabled; * - builtin 
 0    ;;; router-test
      interface=ether1 mpls-mtu=1580 input=yes 

 1    ;;; router-test
      interface=ether2 mpls-mtu=1580 input=yes 

 2    interface=all mpls-mtu=1500  
```

如果接口未被列表中的任何条目匹配，则 MPLS MTU 将等于接口的 L2MTU。

:::info
列表中的条目是有序的，第一个（从上到下迭代）匹配接口的条目将被使用。
:::

条目的顺序很重要，因为不同的接口列表可能包含相同的接口，此外，该接口也可以被直接引用。

MPLS MTU 的选择方式如下：

- 如果接口匹配此表中的条目，则尝试使用配置的 MPLS MTU 值。
- 如果接口不匹配任何条目，则将 MPLS MTU 视为等于 L2MTU。
- 如果接口不支持 L2MTU，则将 MPLS MTU 视为等于 L3 MTU。

在 MPLS 入口路径上，MTU 由 min(MPLS MTU - 标签大小, l3mtu) 决定。这意味着在不支持 L2MTU 且默认 L3 MTU 设置为 1500 的接口上，最大路径 MTU 将为 1500 - 标签大小（该接口将无法在不分片的情况下传递完整的 IP 帧）。在这种情况下，L3MTU 必须增加最大观察到的标签大小。

更多关于 MTU 的信息，请参阅 [MTU in RouterOS](../../hardware/mtu-in-routeros.md) 文章。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="*" typ="builtin"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="enum ()" mandatory="1">要匹配的接口或接口列表的名称。</ArgTableRow>
<ArgTableRow arg="mpls-mtu" typ="num" unset="1">该选项表示在添加 MPLS 标签后，接口上可以承载的最大数据包大小。</ArgTableRow>
<ArgTableRow arg="input" typ="bool" unset="1">是否允许在接口上进行 MPLS 输入。</ArgTableRow>
</ArgTable>