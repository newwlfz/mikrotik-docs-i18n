# 区域与虚拟链路

> 理解OSPF区域和虚拟链路的概念。

# 区域与虚拟链路

OSPF的一个显著特性是能够将一个AS划分为多个路由区域，每个区域拥有自己独立的邻居集合。设想一个拥有300多台路由器且它们之间存在多条链路的庞大网络。每当网络中某条链路发生抖动或其他拓扑变化时，该变化会被泛洪到网络中的所有OSPF设备。这会给网络带来沉重负担，甚至导致停机，因为对于如此庞大的网络，[网络收敛](../../routing-decision.md)可能需要较长时间。

大型单区域网络可能引发严重问题：

- 每当网络拓扑发生变化时，每台路由器都会重新计算数据库。该过程消耗CPU资源。
- 每台路由器都保存着完整的链路状态数据库，用于展示整个网络的拓扑。这会占用内存资源。
- 路由表的完整副本以及路由表条目的数量可能远大于网络数量，这会占用更多的内存资源。
- 更新大型数据库需要更多带宽。

引入区域概念可以实现更好的资源管理，因为一个区域内的拓扑变化不会被泛洪到网络中的其他区域。区域的概念使得网络管理和区域间的路由汇总变得简单，显著减少了每台OSPF邻居需要存储的数据库大小。这意味着每个区域都有自己独立的链路状态数据库和相应的最短路径树。有关OSPF邻居如何相互发现并同步数据库的更多信息，请参阅[邻居关系](./neighbour-relationship.md)。

区域的结构对其他区域是不可见的。这种知识隔离使得协议在使用多个区域时更具可扩展性。路由表计算消耗更少的CPU资源，路由流量也相应减少。

然而，多区域配置增加了额外的复杂性。不应将少于50台路由器的网络划分为多个区域。一个区域内路由器的最大数量主要取决于你用于路由表计算的CPU性能。

![](img/areas.png#gh-light-mode-only)
![](img/areas_dark.png#gh-dark-mode-only)

OSPF区域具有唯一的32位标识符（Area ID）。Area ID为0.0.0.0的区域（称为骨干区域）是主区域，任何其他区域都应连接到该区域。连接多个区域的路由器称为**ABR**（区域边界路由器），其主要职责是连接区域间的路由汇总和更新抑制。连接另一个路由域的路由器称为**ASBR**（自治系统边界路由器）。

每个区域都有自己独立的链路状态数据库，由描述该区域内所有路由器如何互连的路由器LSA和网络LSA组成。关于区域拓扑的详细信息对其他所有区域是隐藏的。路由器LSA和网络LSA不会被泛洪到区域边界之外。区域边界路由器（**ABR**）通过OSPF汇总LSA将寻址信息从一个区域泄露到另一个区域。这使得路由器在向来自其他区域的目的地转发数据时，能够选择最佳的ABR，这被称为**区域内路由**。有关路由表计算方式的更多信息，请参阅[路由表计算](./routing-calculation.md)。

区域间的路由信息交换本质上是一种距离矢量算法。为了防止算法收敛问题（如计数到无穷大），所有区域都必须直接连接到**骨干区域**，从而形成简单的星型拓扑。骨干区域的Area ID始终为0.0.0.0，且不可更改。有关路由决策过程的更多信息，请参阅[路由决策](../../routing-decision.md)。

在[`/routing/ospf/area`](../../../../cli-reference/routing/ospf.md#routingospfarea)菜单中配置RouterOS区域。例如，一个ABR路由器的配置，包含多个连接的区域、一个Stub区域和一个默认区域：

```ros
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=stub_area area-id=1.1.1.1 instance=v2inst type=stub
add name=another_area area-id=2.2.2.2 instance=v2inst type=default
```

OSPF可以有5种类型的区域，通过[`type`](../../../../cli-reference/routing/ospf.md#type)参数配置。每种区域类型定义了该区域支持的LSA类型：

- 标准/默认 - OSPF数据包可以在该区域中传输。它支持类型1、2、3、4和5的LSA。
- 骨干 - 如前所述，这是任何其他区域连接的主区域。它基本上与标准区域相同，但使用ID 0.0.0.0标识。
- [Stub](#stub区域) - 该区域不接受任何外部路由。
- [完全Stub](#完全stub区域) - Stub区域的一种变体。
- [非完全Stub (NSSA)](#nssa) - Stub区域的一种变体。

## LSA类型

在继续详细了解每种区域类型之前，请先熟悉LSA类型：

- ***类型1*** - （路由器LSA）由区域内的路由器发送，包括直接连接链路列表。这些LSA不会跨越ABR或ASBR。
- ***类型2*** - （网络LSA）为区域内的每个“传输网络”生成。传输网络至少有两台直接连接的OSPF路由器。以太网是传输网络的一个例子。类型2 LSA列出构成传输网络的每台连接路由器，并由DR生成。
- ***类型3*** - （汇总LSA）ABR发送类型3汇总LSA。类型3 LSA将区域拥有的任何网络通告给OSPF AS中的其他区域。默认情况下，OSPF为源区域中定义的每个子网通告类型3 LSA，这可能导致泛洪问题。应在ABR上使用手动汇总。
- ***类型4*** - （ASBR汇总LSA）通告ASBR地址并显示ASBR的位置，通告其地址而非其路由表。
- ***类型5*** - （外部LSA）通告通过ASBR学习到的路由，并泛洪到除Stub区域外的所有区域。此LSA分为两个子类型：***外部类型1***和***外部类型2***。
- ***类型6*** - （组成员LSA）为OSPF的组播扩展定义，RouterOS不使用。
- ***类型7*** - 类型7 LSA通知ABR关于导入到NSSA区域的外部路由。然后ABR将这些LSA转换为**类型5**外部LSA，并泛洪到OSPF网络的其余部分。
- ***类型8*** - 外部属性LSA（OSPFv2）/ 链路本地LSA（OSPFv3）。
- ***类型9*** - 链路本地范围不透明（OSPFv2）/ 区域内前缀LSA（OSPFv3）。此类型的LSA不会被泛洪到本地（子）网络之外。
- ***类型10*** - 区域本地范围不透明。此类型的LSA不会被泛洪到其关联区域的范围之外。
- ***类型11*** - 不透明LSA，在整个AS中泛洪（范围与**类型5**相同）。它不会在Stub区域和NSSA中泛洪。

:::note
如果没有ASBR，网络将没有LSA类型4和5。
:::

## 标准区域

此区域支持1、2、3、4和5类型的LSA。

![](img/basic-multi-area.jpg#gh-light-mode-only)
![](img/basic-multi-area_dark.png#gh-dark-mode-only)

一个使用默认区域的简单多区域网络。在此示例中，来自area1的所有网络被泛洪到骨干区域，来自骨干区域的所有网络被泛洪到area1。

**R1**

```ros
/ip/address/add address=10.0.3.1/24 interface=ether1
/ip/address/add address=10.0.2.1/24 interface=ether2
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=default instance=v2inst
/routing/ospf/interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.3.0/24 area=area1
```

**R2**

```ros
/ip/address/add address=10.0.1.1/24 interface=ether2
/ip/address/add address=10.0.2.2/24 interface=ether1
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
/routing/ospf/interface-template
add networks=10.0.2.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=backbone_v2
```

**R3**

```ros
/ip/address/add address=10.0.3.2/24 interface=ether2
/ip/address/add address=10.0.4.1/24 interface=ether1
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.3
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=default instance=v2inst
/routing/ospf/interface-template
add networks=10.0.3.0/24 area=area1
add networks=10.0.4.0/24 area=area1
```

## Stub区域

Stub区域的主要目的是防止此类区域承载外部路由。从这些区域到外部世界的路由基于[默认路由](#外部路由信息与默认路由)。Stub区域减少了区域内的数据库大小以及区域内路由器的内存需求。

![](img/stub-example.jpg#gh-light-mode-only)
![](img/stub-example_dark.png#gh-dark-mode-only)

Stub区域有一些限制。ASBR路由器不能位于区域内部，且Stub区域不能用作虚拟链路的传输区域。这些限制的存在是因为Stub区域被配置为不承载外部路由。

此区域支持1、2和3类型的LSA。

考虑前面的示例。Area1被配置为Stub区域，这意味着路由器R2和R3将不会从骨干区域接收任何路由信息，除了默认路由。

R1：

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst

/routing/ospf/interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
add networks=10.0.3.0/24 area=area1
```

R2：

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing/ospf/interface-template
add networks=10.0.1.0/24 area=area1
```

R3：

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.3
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=stub instance=v2inst
/routing/ospf/interface-template
add networks=10.0.3.0/24 area=area1
```

如果未设置[`default-cost`](../../../../cli-reference/routing/ospf.md#default-cost)参数，则不会生成stub区域类型3默认LSA。

## 完全Stub区域

完全Stub区域是Stub区域的扩展。完全Stub区域阻止外部路由和汇总（区域间）路由进入该区域。只有区域内路由被注入到该区域。完全Stub区域配置为带有附加[`no-summaries`](../../../../cli-reference/routing/ospf.md#no-summaries)标志的Stub区域。此区域支持类型1、类型2 LSA，以及带有默认路由的类型3 LSA。

```ros
/routing/ospf/area
add name=totally_stubby_area area-id=1.1.1.1 instance=v2inst type=stub no-summaries
```

## NSSA

非完全Stub区域（NSSA）适用于需要注入外部路由，但不注入类型5 LSA路由的情况。另请参阅[理解OSPF](./understanding-ospf.md#支持的协议标准)以获取NSSA的RFC参考。

![](img/nssa-example.jpg#gh-light-mode-only)
![](img/nssa-example_dark.png#gh-dark-mode-only)

图示显示了两个区域（骨干区域和area1）以及到位于area1中路由器的RIP连接。Area1必须配置为Stub区域，但同时必须将外部RIP路由注入到骨干区域。在这种情况下，Area1应配置为NSSA。

配置示例不涵盖[RIP](../rip.md)配置。

**R1**

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.1
/routing/ospf/area
add name=backbone_v2 area-id=0.0.0.0 instance=v2inst
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing/ospf/interface-template
add networks=10.0.0.0/24 area=backbone_v2
add networks=10.0.1.0/24 area=area1
```

**R2**

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.0.0.2
/routing/ospf/area
add name=area1 area-id=1.1.1.1 type=nssa instance=v2inst
/routing/ospf/interface-template
add networks=10.0.1.0/24 area=area1
```

:::info
虚拟链路不能用于NSSA区域。使用[`nssa-translator`](../../../../cli-reference/routing/ospf.md#nssa-translator)参数控制类型7到类型5 LSA的转换。
:::

## 外部路由信息与默认路由

在OSPF路由域的边缘，可以找到运行其他路由协议的路由器，称为**AS边界路由器（ASBR）**。这些路由器的任务是将从其他路由协议学习到的路由信息导入到OSPF路由域中。外部路由可以根据度量类型在两个不同的级别导入。

- 类型1 - OSPF度量是内部OSPF开销和外部路由开销的总和。
- 类型2 - OSPF度量仅等于外部路由开销。

:::tip
类型1外部路径始终优先于类型2外部路径。当所有路径都是类型2外部路径时，通告的类型2度量最小的路径始终优先。（RFC2328）
:::

外部路由可以通过多种方式导入，并按列出的顺序处理：

- 选择匹配[`redistribute`](../../../../cli-reference/routing/ospf.md#redistribute)或[`originate-default`](../../../../cli-reference/routing/ospf.md#originate-default)实例参数的路由。
- 如果指定了输出路由过滤链：
  - 如果使用了[`redistribute`](../../../../cli-reference/routing/ospf.md#redistribute)或[`originate-default`](../../../../cli-reference/routing/ospf.md#originate-default)参数，则仅处理选定的路由。
  - 否则，处理所有活动路由。
- 在[`out-filter-select`](../../../../cli-reference/routing/ospf.md#out-filter-select)中处理选定的路由。

仍然需要[路由过滤](../../route-selection-and-filtering.md)来设置路由开销和类型（需要时）。

配置示例选择并重新分发所有静态和RIP路由：

```ros
/routing/ospf/instance
add name=v2inst version=2 router-id=1.2.3.4 redistribute=static,rip
```

默认路由的重新分发是一种特殊情况，应使用`originate-default`参数：

```ros
/routing/ospf/instance
set v2inst originate-default=if-installed
```

当重新分发由`originate-default`和`redistribute`参数控制时，会引入默认路由过滤的一些边界情况。

- 如果启用了`redistribute`，则选择所有匹配重新分发参数的路由。
- 如果`originate-default=never`，默认路由将被拒绝。
- 将选定的路由（如果未设置redistribute参数，则为所有路由）通过[`out-filter-select`](../../../../cli-reference/routing/ospf.md#out-filter-select)（如果已配置）。
- 将选定的路由通过[`out-filter-chain`](../../../../cli-reference/routing/ospf.md#out-filter-chain)（如果已配置）。有关路由过滤参考，请参阅[`/routing/filter`](../../../../cli-reference/routing/filter.md)。
- 如果[`originate-default`](../../../../cli-reference/routing/ospf.md#originate-default)设置为`always`或`if-installed`：
  - OSPF创建一个没有属性的伪默认路由。
  - 将此路由通过[`out-filter-chain`](../../../../cli-reference/routing/ospf.md#out-filter-chain)，可以在其中应用属性，但操作被忽略（始终接受）。

有关重新分发值的完整列表，请参阅[`/routing/ospf/instance`](../../../../cli-reference/routing/ospf.md#routingospfinstance)。

## 路由汇总

路由汇总是将多条路由合并为单个通告。它在区域边界（ABR）处完成。

应朝骨干方向进行汇总。这样，骨干区域接收所有聚合路由，并将已汇总的路由注入到其他区域。存在两种类型的汇总：区域间路由汇总和外部路由汇总。

区域间路由汇总作用于区域边界（ABR）。它不适用于通过重新分发注入到OSPF的外部路由。默认情况下，ABR为特定区域中的每条路由创建一个汇总LSA，并在相邻区域中通告它。

范围允许为多条路由仅创建一个汇总LSA，并向相邻区域发送单个通告，或者完全抑制通告。

如果使用[`advertise`](../../../../cli-reference/routing/ospf.md#advertise)参数配置了范围，则如果特定区域在该范围内有任何路由，则为每个范围通告单个汇总LSA。否则（当`advertise`参数被禁用时），不会创建汇总LSA，也不会在区域边界外通告。

区域间路由汇总可以在[`/routing/ospf/area/range`](../../../../cli-reference/routing/ospf.md#routingospfarearange)菜单中配置。

考虑两个区域，骨干区域和area1。Area1有来自10.0.0.0/16范围的多个/24路由，当可以汇总时，不必将每个/24子网泛洪到骨干区域。在连接area1与骨干区域的路由器上，可以设置区域范围：

```ros
/routing/ospf/area/range
add prefix=10.0.0.0/16 area=area1 advertise=yes cost=10
```

有关[`advertise`](../../../../cli-reference/routing/ospf.md#advertise)和[`cost`](../../../../cli-reference/routing/ospf.md#cost)参数的参考，请参阅[`/routing/ospf/area/range`](../../../../cli-reference/routing/ospf.md#routingospfarearange)。

:::info
对于活动范围（即至少有一条来自指定区域的OSPF路由落在该范围内），会创建类型为'blackhole'的路由并安装到路由表中。
:::

外部路由汇总可以通过使用[路由过滤](../../route-selection-and-filtering.md)来实现。考虑与上一个示例相同的场景，只是area1有从其他协议重新分发的/24路由。要发送单个汇总LSA，请添加一条[黑洞路由](../../../../cli-reference/ip/route.md)并配置适当的[`/routing/filter/rule`](../../../../cli-reference/routing/filter.md)以仅接受汇总路由：

```ros
/ip/route/add dst-address=10.0.0.0/16 blackhole
/routing/ospf/instance
set v2inst out-filter-chain=ospf_out
/routing/filter/rule
add chain=ospf_out rule="if (dst == 10.0.0.0/16) {accept} else {reject}"
```

## 虚拟链路

所有OSPF区域必须连接到骨干区域，但有时物理连接是不可能的。为了克服这一限制，可以通过使用**虚拟链路**在逻辑上连接区域。

有两种常见场景可以使用虚拟链路：

- 连接分散的骨干区域。
- 连接没有直接连接到骨干区域的远程区域。

### 骨干区域分区

OSPF允许通过虚拟链路连接骨干区域的不连续部分。当两个独立的OSPF网络合并为一个大型网络时，可能需要这样做。虚拟链路可以配置在从两侧接触骨干区域并共享一个公共区域的独立ABR之间。

![](img/vlink-backbone.jpg#gh-light-mode-only)
![](img/vlink-backbone_dark.png#gh-dark-mode-only)

当不存在公共区域时，可以创建额外的区域作为传输区域。这在前面的图像中有所说明。

非骨干区域被分区时不需要虚拟链路。OSPF不会主动尝试修复区域分区。当区域被分区时，每个组件简单地成为一个单独的区域。骨干区域在新区域之间执行路由。某些目的地可以通过**区域内**路由到达。区域分区需要**区域间**路由。

然而，要在分区后保持完整路由，地址范围不能被分割到区域分区的多个组件中。考虑使用[BFD](../bfd.md)来加快虚拟链路上的故障检测。

### 无物理连接到骨干区域

一个区域可能没有到骨干区域的物理连接。虚拟链路为断开的区域提供了到骨干区域的逻辑路径。必须在共享公共区域的两个ABR之间建立链路，其中一个ABR连接到骨干区域。

![](img/virtual-link2.jpg#gh-light-mode-only)
![](img/virtual-link2_dark.png#gh-dark-mode-only)

R1和R2都是ABR，R1连接到骨干区域。Area2将用作**传输区域**，R1是进入骨干区域的**入口点**。必须在两台路由器上配置虚拟链路。

在[`/routing/ospf/interface`](../../../../cli-reference/routing/ospf.md#routingospfinterface)菜单中添加虚拟链路配置。必须在两台路由器上配置[`vlink-transit-area`](../../../../cli-reference/routing/ospf.md#vlink-transit-area)和[`vlink-neighbor-id`](../../../../cli-reference/routing/ospf.md#vlink-neighbor-id)参数。基于图示的配置如下：

R1：

```ros
/routing/ospf/interface
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=2.2.2.2
```

R2：

```ros
/routing/ospf/interface
add vlink-transit-area=area2 area=backbone_v2 type=virtual-link vlink-neighbor-id=1.1.1.1
```