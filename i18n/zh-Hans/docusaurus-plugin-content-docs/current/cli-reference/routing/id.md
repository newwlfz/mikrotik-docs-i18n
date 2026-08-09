# 名称   动态ID     选择-D   选择

> -----------

导入 {ArgTableRow} 来自 '@site/src/components/common'；
导入 {ArgTable} 来自 '@site/src/components/common'；

-----------

## routing/id

**类型：** 目录

全局路由器ID选举配置。路由器ID可以显式配置，也可以从路由器的某个IP地址中选举产生。

对于每个VRF表，RouterOS会添加一个动态ID实例，从该VRF中的某个IP地址选举路由器ID：

```text
[admin@rack1_b33_CCR1036] /routing/id> print
标志：D - 动态，I - 非活动
列：名称，动态ID，选择动态ID，从VRF选择
#   名称   动态ID          选择-D   选择
0 D main   111.111.111.2   仅VRF    main

```

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">如果获取有效ID时出现问题，则该项可能变为非活动状态。</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="id" typ="ipAddr" unset="1">显式设置路由器ID。如果未设置路由器ID，RouterOS可以从配置的IP地址中选举一个。参见 `select-dynamic-id` 和 `select-from-vrf`。</ArgTableRow>
<ArgTableRow arg="select-dynamic-id" typ="ubit (any, only-static, only-loopback, only-vrf, only-active, lowest)" unset="1">
选择RouterOS用于路由器ID选举的IP地址：
- `any` - 路由器上找到的任何地址都可以被选举为路由器ID。
- `lowest` - 选择最低的IP地址。
- `only-static` - 仅选择静态配置的地址。
- `only-active` - 仅从活动IP地址中选择ID。
- `only-loopback` - 仅从环回地址中选择ID（环回地址是任何非点对点的/32地址）。
- `only-vrf` - 仅从选定的VRF中选择ID。与 `select-from-vrf` 配合使用。
</ArgTableRow>
<ArgTableRow arg="select-from-vrf" typ="enum" unset="1">从中选择IP地址用于ID选举的VRF。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="dynamic-id" typ="ipAddr">当前选定的ID。</ArgTableRow>
</ArgTable>