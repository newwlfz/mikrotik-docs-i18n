# 路由选择与过滤

> MikroTik RouterOS 中的路由过滤采用类脚本语法来匹配前缀并根据条件修改路由距离，其属性分为只读和可读/可写两类，分别用于匹配器和动作。

# 路由选择与过滤

## 路由过滤

### 过滤语法

路由过滤规则使用类脚本语法。以下示例匹配来自 192.168.1.0/24 子网且前缀长度大于 24 的前缀，并将默认距离增加 1。如果不匹配，则将默认距离减 1。

```ros
/routing/filter/rule
  add chain=myChain \
  rule="if (dst in 192.168.1.0/24 && dst-len>24) {set distance +1; accept} else {set distance -1; accept}"
```

一条过滤规则可以由多个匹配器和动作组成：

```text
if ( [匹配器] ) { [动作] } else { [动作] }
```

属性分为两种类型：

- 仅可读 — 属性值只读，不可重写。它们只能用于匹配器。
- 可读/可写 — 属性值既可读也可写。它们可用于过滤动作和匹配器。

对于仅数值属性，可读属性可以通过布尔运算符与其他可读属性或常量值进行匹配。

```text
[匹配器]:
[可读属性] [布尔运算符] [可读属性]

[动作]:
[动作] [可写属性] [值]
```

如果匹配器只有一种可能的操作，则不需要布尔运算符。

无布尔运算符的示例：

```text
if ( protocol connected ) { accept }
```

带布尔运算符的示例：

```text
if ( bgp-med < 30 ) { accept }
```

对于只读标志属性，匹配器不需要布尔运算符或值。

```text
if ( ospf-dn ) { reject }
```

:::info
路由过滤链的默认动作是 `reject`。
:::

#### 仅可读属性

| 属性 | 类型 | 描述 |
| :-- | :-- | :-- |
| ***数值属性*** |  |  |
| `dst-len` |  | 目标前缀长度 |
| `bgp-path-len` |  | BGP AS-PATH 的当前长度 |
| `bgp-input-local-as` |  | 发送前缀的本地对等体的 AS 号 |
| `bgp-input-remote-as` |  | 接收前缀的远程对等体的 AS 号 |
| `bgp-output-local-as` |  | 将通告前缀的对等体的 AS 号 |
| `bgp-output-remote-as` |  | 前缀将被通告到的对等体的 AS 号 |
| `ospf-metric` |  | 当前 OSPF 度量值 |
| `ospf-tag` |  | 当前 OSPF 标签 |
| `rip-metric` |  | 当前 RIP 度量值 |
| `rip-tag` |  | 当前 RIP 标签 |
| ***标志属性*** |  |  |
| `active` |  | 指示路由是否处于活动状态 |
| `bgp-atomic-aggregate` |  |  |
| `bgp-communities-empty` |  | 指示 BGP Communities 属性是否为空 |
| `bgp-ext-communities-empty` |  | 指示 BGP Extended Communities 属性是否为空 |
| `bgp-large-communities-empty` |  | 指示 BGP Large Communities 属性是否为空 |
| `bgp-network` |  | 指示前缀是否源自 BGP networks |
| `ospf-dn` |  | 指示 OSPF 路由是否设置了 DN 位。 |
| ***前缀属性*** |  |  |
| `dst` |  | 目标 |
| `ospf-fwd` |  | 当前 OSPF 转发地址 |
| `bgp-input-local-addr` |  | 发送前缀的本地对等体的 IP 地址 |
| `bgp-input-remote-addr` |  | 接收前缀的远程对等体的 IP 地址 |
| `bgp-output-local-addr` |  | 将通告前缀的对等体的 IP 地址 |
| `bgp-output-remote-addr` |  | 前缀将被通告到的对等体的 IP 地址 |
| 其他属性 |  |  |
| `afi` | `ipv4 \| ipv6 \| l2vpn \| l2vpn-cisco \| vpnv4 \| vpnv6` | 路由的地址族。 |
| `bgp-as-path` | `numeric_regexp` | AS 路径 [正则表达式匹配](#as-path-regexp-matching) |
| `bgp-as-path-slow-legacy` | `string_regexp` | **已弃用**。极慢的旧式 AS 路径匹配。此参数仅应在从旧版 ROS v6 配置迁移时作为临时匹配器使用。[了解更多>>](#as-path-regexp-matching) |
| `chain` | `chain_name` |  |
| `origin` | `string` | 匹配路由的来源实例，例如，可以匹配从特定 OSPF 实例导入的路由：`if (origin <instance_name>) {}` |
| `ospf-type` | `ext1 \| ext2 \| inter \| intra \| nssa1 \| nssa2` | OSPF 路由类型：ext1 - 外部（Type 5 LSA）且使用 type1 度量ext2 - 外部（Type 5 LSA）且使用 type2 度量inter - 区域间路由（Type 3 LSA）intra - 区域内路由（Type 1/2 LSA）nssa1 - Type 7 LSA 且使用 type1 度量nssa2 - Type 7 LSA 且使用 type2 度量 |
| `protocol` | `bgp \| connected \| dhcp \| fantasy \| modem \| ospf \| rip \| static \| slaac \| vpn` | 导入路由的协议类型。 |
| `rpki` | `invalid \| unknown \| valid \| unverified` | 前缀的 [RPKI](./unicast/rpki.md) 验证状态 |
| `rtab` | `routing_table_name` | 导入路由的路由表名称 |
| `vrf` | `vrf_name` | 导入路由的 VRF 名称 |

#### 可写属性

| 属性 | 类型 | 描述 |
| :-- | :-- | :-- |
| ***数值属性*** |  |  |
| `distance` |  | 路由距离 |
| `scope` |  |  |
| `scope-target` |  | 目标范围 |
| `bgp-weight` |  | BGP WEIGHT 属性 |
| `bgp-med` |  | BGP MED 属性是路由器本地的。它也用于 iBGP 对等体的输出。 |
| `bgp-out-med` |  | 将发送到远程对等体的 BGP MED 属性。应在 eBGP 对等体的输出链中使用。 |
| `bgp-local-pref` |  | BGP LOCALPREF 属性 |
| `bgp-igp-metric` |  | BGP IGP METRIC |
| `bgp-path-peer-prepend` |  | 预置最后接收的远程对等体的 ASN。如果前缀源自路由器本身，则此参数在路由器输出上不会产生任何效果，因为 ASN 尚不存在。    如果在 BGP 输入中用作匹配器，则可以过滤超过特定预置次数的前缀。例如，如果远程对等体预置其 ASN 5 次，但我们希望最多允许预置 4 次，则可以使用：`if (bgp-path-peer-prepend > 4) {reject}`    此参数还会覆盖从远程对等体接收的任何预置，例如，如果远程对等体预置了其 AS 3 次，我们可以通过在 BGP 输入中设置 `bgp-path-peer-prepend 1` 来移除该预置 |
| `bgp-path-prepend` |  | 预置路由器的 ASN，应在 BGP 输出中使用。 |
| `ospf-ext-metric` |  | OSPF 外部路由度量值 |
| `ospf-ext-tag` |  | OSPF 外部路由标签 |
| `rip-ext-metric` |  | RIP 外部路由度量值 |
| `rip-ext-tag` |  | RIP 外部路由标签 |
| ***标志属性*** |  |  |
| `ospf-ext-dn` |  | 外部 OSPF 路由的 DN 位 |
| `blackhole` |  | 黑洞路由 |
| `suppress-hw-offload` |  | 是否 [抑制 L3 硬件卸载](../../bridging-and-switching/l3-hardware-offloading.md#suppressing-hw-offload) |
| `use-te-nexthop` |  |  |
| ***其他属性*** |  |  |
| `gw` | `ipv4/6 address` | IPv4/IPv6 地址或接口名称。在 BGP 输出的情况下，可以在以下设置中调整网关：是 BGP 反射器nexthop-choice 设置为 propagate非 eBGP 且未设置 nexthop-choice=force-self。 |
| `gw-ll` | `ipv6 address` | ipv6 链路本地下一跳属性。在 BGP 输出的情况下，可以在以下设置中调整网关：是 BGP 反射器nexthop-choice 设置为 propagate非 eBGP 且未设置 `nexthop-choice=force-self`。 |
| `gw-interface` | `interface_name` | 网关的接口部分。如果需要为下一跳附加特定接口，则应使用此参数，例如（`1.2.3.4%ether1`） |
| `gw-check` | `none \| arp \| icmp \| bfd \| bfd-mh` |  |
| `pref-src` | `ipv4/6 address` |  |
| `bgp-origin` | `igp \| egp \| incomplete` |  |
| `ospf-ext-fwd` | `ipv4/6 address` | 外部 OSPF 路由的转发地址 |
| `ospf-ext-type` | `type1 \| type2` | OSPF 外部路由类型 |
| `comment` | `string` |  |
| `bgp-communities` | `inline_community_set \| community_list_name` | BGP Communities 属性定义于 [RFC 1997](https://tools.ietf.org/html/rfc1997)。每个 community 为 32 位。 |
| `bgp-ext-communities` | `inline_ext_community_set \| ext_community_list_name` | BGP Extended Communities 属性定义于 [RFC 4360](https://tools.ietf.org/html/rfc4360)。RouterOS 解析 `site-of-origin`（前缀为 `soo:`）和 `route-target`（前缀为 `rt:`）扩展社区。例如，`set bgp-ext-communities rt:1111:2.3.4.5;` 可以设置/匹配 64 位十六进制的原始扩展社区值，例如，`set bgp-ext-communities 0x.........;` |
| `bgp-large-communities` | `inline_large_community_set \| large_community_list_name` | BGP Large Communities 属性定义于 [RFC 8092](https://datatracker.ietf.org/doc/html/rfc8092)。适用于所有 ASN，包括 32 位 ASN。每个 community 长度为 12 字节，由 3 部分组成：`global_admin:local_part_1:local_part_2`。 |

#### 命令

| 命令 | 参数 | 描述 |
| :-- | :-- | :-- |
| `accept` |  | 接受匹配的前缀并停止处理该链。 |
| `reject` |  | 拒绝匹配的前缀并停止处理该链，该前缀将作为“已过滤”存储在内存中，不会成为最佳路径的候选。 |
| `return` |  | 返回到父链 |
| `jump` | `jump chain_name` | 跳转到指定链 |
| `unset` | `unset prop_name` | 用于取消设置以下属性的值：`pref-src, bgp-med, bgp-out-med, bgp-local-pref` |
| `append` |  | 在列表或字符串末尾追加。可以追加以下属性值：`bgp-communities, bgp-ext-communities, bgp-large-communities, comment` |
| `filter` |  | 删除动作的逆操作（删除除指定值以外的所有内容）。可以过滤以下属性的值：`bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `delete` |  | 删除指定属性的值。可以删除以下属性的值：`bgp-communities, bgp-ext-communities, bgp-large-communities` |
| `set` | `prop_writeable value` | 该命令用于为可写属性设置新值。可以从其他匹配类型的可读属性中设置值。对于数值属性，可以在值前加上 +/- 来按给定数量递增或递减当前属性值。例如，`set bgp-local-pref +1` 将当前 LOCAL\_PREF 递增 1，或者从另一个可读数值属性中提取值，`set distance +ospf-ext-metric` |
| `rpki-verify` | `rpki_group_name` | 在当前链中从指定的 RPKI 组启用 [RPKI](./unicast/rpki.md) 验证。 |

#### 运算符

##### 匹配器运算符

| 运算符 | 描述 | 示例 |
| :-- | :-- | :-- |
| `&&` | 逻辑与运算符 | `if (dst in 192.168.0.0/16 && dst-len in 16-32) {reject;}` |
| `\|\|` | 逻辑或运算符 | `if (dst in 192.168.0.0/16 \|\| dst-len in 16-32) {reject;}` |
| `not` | 逻辑非运算符 | `if (not bgp-network) {reject; }` |

##### 数值属性运算符

| 运算符 | 描述 |
| :-- | :-- |
| `in` | 如果值在提供的数值范围内，则返回 true。数值范围可以写成以下格式：`{int..int}`，`{int-int}` |
| `==` | 如果数值相等，则返回 true |
| `!=` | 如果数值不相等，则返回 true |
| `>` | 如果左侧数值大于右侧数值，则返回 true |
| `<` | 如果左侧数值小于右侧数值，则返回 true |
| `>=` | 如果左侧数值大于或等于右侧数值，则返回 true |
| `<=` | 如果左侧数值小于或等于右侧数值，则返回 true |

##### 前缀运算符

| 运算符 | 描述 |
| :-- | :-- |
| `in` | 如果前缀是所提供网络的子网，则返回 true。如果使用该运算符来匹配地址列表中的前缀（例如 `dst in list_name`），则只匹配精确前缀。 |
| `!=` | 如果前缀不等于提供的值，则返回 true |
| `==` | 如果前缀等于提供的值，则返回 true |

:::info
地址列表在设计上匹配主机地址，这意味着它也会匹配属于地址列表中任何范围的 /32 前缀。排除 /32 前缀被通告的解决方法是使用 dst-len `if (dst in list_name && dst-len < 32) {}`
:::

##### BGP Community 运算符

| 运算符 | 描述 | 示例 |
| :-- | :-- | :-- |
| `equal` | 如果提供的 communities 与路由的属性值相等，则返回 true |  |
| `equal-list` | 如果提供的 `community-list` 中的 communities 与路由的属性值相等，则返回 true |  |
| `any` | 如果路由的属性值包含至少一个提供的 communities，则返回 true |  |
| `any-list` | 如果路由的属性值包含至少一个来自所提供列表的 community，则返回 true |  |
| `includes` | 如果路由的属性值包含指定的 communities，则返回 true |  |
| `includes-list` | 如果路由的属性值包含指定 `communities-list` 中的所有 communities，则返回 true |  |
| `subset` | 如果路由的 community 子集与列表中的 communities 匹配，则返回 true | `1:1,3:3` 将匹配 `1:1,2:2,3:3` |
| `subset-list` | 与 `subset` 相同，但匹配来自 community 列表的 communities。 |  |
| `any-regexp` | 与 `any` 相同，但通过正则表达式匹配 |  |
| `subset-regexp` | 与 `subset` 相同，但通过正则表达式匹配 |  |

##### 字符串运算符

| 运算符 | 描述 |
| :-- | :-- |
| `find` | 检查提供的子字符串是否是属性值的一部分 |
| `regexp` | 匹配属性值的字符串正则表达式 |

### 删除 BGP Communities

路由过滤允许使用 `delete` 命令清除 BGP communities。`delete` 命令根据 community 类型接受多个参数：

- **communities**：
  - `wk` - 匹配并移除公认 communities。
  - `other` - 匹配并移除非公认的其他 communities。
  - `regexp` - 用于匹配应删除的 communities 的正则表达式模式。
  - `<community-list name>` - 从指定的 `community-list` 中删除 communities。
- **ext-communities**：
  - `rt` - 匹配并移除 **RouteTarget**。
  - `soo` - 匹配并移除 **Site-of-Origin**。
  - `other` - 匹配并移除非 **RT** 或 **SOO** 的其他扩展 communities。
  - `regexp` - 用于匹配应删除的扩展 communities 的正则表达式模式。
  - `<community-ext-list name>` - 从指定的 `community-ext-list` 中删除 communities。
- **large-communities**：
  - `all` - 移除所有内容。
  - `regexp` - 用于匹配应删除的大型 communities 的正则表达式模式。
  - `<community-large-list name>` - 从指定的 `community-large-list` 中删除大型 communities。

可以指定多种 community 类型，例如，从 community-ext 列表中删除所有 SOO、其他类型的扩展 communities 以及特定的 RT：

```ros
/routing/filter/community-ext-list
add list=myRTList communities="rt:1.1.1.1:222"
/routing/filter/rule
add chain=myChain rule="delete bgp-ext-communities soo,other,myRTList;"
```

### AS-PATH 正则表达式匹配

AS 路径是自治系统号（ASN）的序列。例如，AS 路径 `123 456 789` 表示路由源自 AS 789，并在到达目的地之前经过 AS 456。要应用路由策略，请使用正则表达式（regexp）匹配 AS 路径中的特定 AS 号或 AS 号集合。

有两种常见的方式处理 AS 路径数据：

- 将整个 AS 路径转换为字符串，并让正则表达式对字符串进行操作（ROS v6 或 Cisco 风格）。
- 让正则表达式将每个 AS 路径条目作为数字进行操作（ROS v7，Juniper 风格）。

第一种方法按字符匹配。第二种方法按 AS 号匹配。第二种方法比字符串匹配方法更快，消耗的资源更少。

这一变化要求管理员使用新的正则表达式策略。来自 RouterOS v6 的旧正则表达式模式不能直接复制粘贴，因为它们可能导致语法错误或意外结果。

以这个基本的 AS 路径过滤规则为例：

```ros
/routing/filter/rule
add chain=myChain rule="if (bgp-as-path .1234.) {accept}"
```

此正则表达式模式匹配 AS 路径中间任意位置的 ASN 1234。使用旧式字符串匹配方法，相同的模式匹配任何包含至少六个字符且包含子字符串 `1234` 的 ASN 的 AS 路径。等效的旧式模式是 `._1234_.`。

例如，旧式字符串模式 `1234[5-9]` 匹配字符串中任意位置的 12345 到 12349。这将产生诸如 `12345 3434` 和 `11 9123467 22` 之类的匹配。使用新式匹配器，相同的模式匹配包含精确 ASN 1234 后跟 5 到 9 的 ASN 的 AS 路径，例如 `1234 7 111` 或 `111 1234 5 222`。它不匹配 `12345 3434`。

:::danger
在实现之间复制正则表达式模式可能会产生意外或危险的结果。

不要直接从 ROS v6 或 Cisco 配置中复制正则表达式模式，它们不直接兼容。在某些情况下可能导致意外甚至危险的配置。
:::

:::info
AS-Path 参数必须存在才能应用正则表达式匹配器。这意味着无法使用正则表达式匹配不存在（空）的 AS-Path，即 `^$`。应改用 `bgp-path-len`。
:::

#### 正则表达式测试工具

RouterOS 内置了正则表达式检查工具，可帮助管理员验证正则表达式。该工具还支持 num-list 值，因此您可以在将正则表达式应用于路由过滤器之前，针对任何 AS 路径进行测试。

```ros
/routing/filter/num-list/add list=test range=100-1500

/routing/filter/test-as-path-regexp regexp="[[:test:]]5678\$" as-path="1234,5678"
```

#### 支持的运算符

| 运算符 | 描述 | 示例 | 示例说明 | 示例匹配 |
| :-- | :-- | :-- | :-- | :-- |
| `^` | 表示路径的开头 | `^1234` | 将匹配以 ASN 1234 开头的 AS 路径 |  |
| `$` | 表示路径的结尾 | `1234$` | 将匹配源 ASN 为 1234 的 AS 路径 |  |
| `*` | 列出的 ASN 出现零次或多次 | `^1234*$` | 将匹配空 AS 路径或 ASN 1234 可能多次出现的 AS 路径 | **匹配：**  1234  1234 1234 1234  空路径  **不匹配：**  1234 5678 |
| `+` | 列出的 ASN 出现一次或多次 | `1234+` | 将匹配 ASN 1234 至少出现一次的 AS 路径 | **匹配：**  1234  3 1234 6  **不匹配：**  12345 678 |
| `?` | 列出的 ASN 出现零次或一次 | `^1234? 5678` | 将匹配可能以 ASN 1234 开头（出现一次）或不以 ASN 1234 开头的 AS 路径。 | **匹配**：  5678  1234 5678  **不匹配：**  1234 1234 5678  12345 5678 |
| `.` | 任意 ASN 出现一次 | `^.$` | 将匹配长度为 1 的任何 AS 路径。 | **匹配：**  12345  45678  **不匹配：**  1234 5678 |
|  `\|`  | 匹配两侧 ASN 中的任意一个 | `^(1234\|5678)` | 将匹配以 ASN 1234 或 5678 开头的 AS 路径 | **匹配**：  1234  5678  1234 5678  **不匹配：**  91011 |
| `[ ]`  `[^ ]` | 表示 AS 号集合，必须匹配列表中的一个 AS 号。  在左括号后使用 ^ 来否定该集合。  也可以使用 [[:numset\_name:]] 引用 [num-list](#community-and-num-lists) 中预定义的 num-lists | `^[1234 5678 1-100]` | 将匹配以 1234、5678 或 1 到 100 范围内的数字开头的 AS 路径 | **匹配：**  1234  99  5678  **不匹配：**  101 |
| `()` | 要匹配的正则表达式项分组 | `^(1234$\|5678)` | 将匹配以 1234 开头和结尾的 AS 路径，或以 5678 开头的 AS 路径 | **匹配：**  1234  5678 9999  **不匹配：**  1234 5678 |

:::warning
不支持重复范围 {}。
:::

### Community 和 Num 列表

可以从 `/routing/filter/num-list` 菜单配置常用数字列表。这些数字列表可以在过滤规则中使用，以简化过滤设置过程。

类似地，您也可以定义 community、扩展 community 和大型 community 列表。Community 集可用于匹配、追加和设置。

例如，匹配列表中的 communities 并清除该属性：

```ros
/routing/filter/community-list
add communities=111:222 list=myCommunityList

/routing/filter/rule
add chain=myChain rule="if (bgp-communities equal-list myCommunityList) {delete bgp-communities wk,other; accept;}"
```

## 路由选择

路由选择规则控制如何从可用的候选路由中选择输出路由。默认情况下，如果未设置选择规则，输出会选择最佳路由。

以下路由表显示了两条候选路由和一条最佳路由。默认情况下，当 BGP 选择要发送的路由时，它会选择活动路由。

```text
[admin@4] /routing/route> print where dst-address=1.0.0.0/24
Flags: A - ACTIVE; b, y - COPY
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS  GATEWAY         AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
 b 1.0.0.0/24   10.155.101.217  ip4        19     40            30  10.155.109.254%ether1
Ab 1.0.0.0/24   10.155.101.232  ip4        20     40            30  10.155.109.254%ether1
 b 1.0.0.0/24   10.155.101.231  ip4        20     40            30  10.155.109.254%ether1
```

如果您需要偏好非活动路由，请使用选择规则。

RouterOS 中的选择规则从 `/routing/filter/select-rule` 菜单配置。

选择规则也可以调用路由过滤器，以便根据过滤规则选择路由。例如，要模拟默认的输出选择，请使用以下规则集：

```ros
/routing/filter/rule
add chain=get_active rule="if (active) {accept}"

/routing/filter/select-rule
add chain=my_select_chain do-where=get_active
```

选择规则也可用于限制为 BGP Add-path 选择的额外路径数量，例如最多 3 条路径：

```ros
/routing/filter/select-rule add chain=select-for-addpath do-take=3
```

## 路由过滤向导

由于使用类脚本语法编写过滤规则较为复杂，因此引入了路由过滤向导，该向导可生成具有 ROSv6 风格语法的过滤规则。

快速演示：

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard <tab>
action        dst                   ospf-type         scope-target      set-gw-check                use-te-nexthop
afi           dst-len               protocol          set-bgp-...       set-scope
bgp-...       gateway               routing-table     set-blackhole     set-scope-target
blackhole     jump-target-chain     rpki              set-comment       set-suppress-hw-offload
chain         match-chain           rpki-verify       set-distance      set-use-te-nexthop
distance      ospf-metric           scope             set-gateway       suppress-hw-offload

[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 set-bgp-ext-communities=rt:2:2
  result: Filter rule 'if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }' added

[admin@CCR2004_2XS_111] /routing/filter> /routing/filter/rule/print
Flags: X - disabled, I - inactive
 0   ;;; added by filter-wizard
     chain=vpn-in rule="if (afi vpnv4) { set bgp-ext-communities rt:2:2; accept; }"
```

过滤向导在列表末尾添加规则，并为其添加注释 `added by filter-wizard`。

当您尝试添加包含不可接受值的过滤器时返回的错误会打印在 CLI 中，并记录在系统日志中，主题为 `route,error`。

```routeros
[admin@CCR2004_2XS_111] /routing/filter> filter-wizard action=accept chain=vpn-in afi=vpnv4 match-chain=vpn-in
  result: Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

[admin@CCR2004_2XS_111] /routing/filter> /log/print
 2025-05-19 13:05:15 route,error Error adding 'if (chain vpn-in && afi vpnv4) { accept; }'match with 'vpn-in' creates chain loop (6)

```