# L3 硬件卸载

> L3 硬件卸载（L3 Hardware Offloading）通过将 CPU 密集型任务卸载到交换芯片，实现线速路由。本页详细介绍了如何为整个交换机、单个端口以及全局设置（如 IPv6 支持和 FastTrack 卸载）配置 L3HW，并警告了对现有连接可能产生的影响。

import WideTable from '@site/src/components/WideTable';

# L3 硬件卸载

**三层硬件卸载**（**L3HW**，也称为 IP 交换或硬件路由）允许将某些路由器功能卸载到交换芯片上。这使得数据包路由能够达到线速，而这是 CPU 根本无法实现的。

## 交换机配置

要启用三层硬件卸载，请为交换机设置 `l3-hw-offloading=yes`：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 交换机端口配置

可以为每个物理交换机端口配置三层硬件卸载。例如：

```ros
/interface/ethernet/switch/port/set sfp-sfpplus1 l3-hw-offloading=yes
```

请注意，交换机和端口的 l3hw 设置是不同的：

- 为交换机设置 `l3-hw-offloading=no` 会完全禁用卸载——所有数据包将由 CPU 路由。
- 但是，为交换机端口设置 `l3-hw-offloading=no` 仅禁用与该特定端口之间的硬件路由。此外，该端口仍然可以参与 Fasttrack 连接卸载。

要启用完整的硬件路由，请在所有交换机端口上启用 l3hw：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
```

要使所有数据包首先经过 CPU，并且仅卸载 Fasttrack 连接，请在所有端口上禁用 l3hw，但在交换芯片本身上保持启用：

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=no
```

:::info
**当入口和出口端口都具有 `l3-hw-offloading=yes` 时，数据包由硬件路由。**

如果入口和出口端口都具有 `l3-hw-offloading=no`，数据包将经过 CPU/防火墙，同时仅卸载 Fasttrack 连接。

可以通过仅在出口端口设置 `l3-hw-offloading=no` 来引导数据包经过 CPU/防火墙。但是，仅在入口端口设置 `l3-hw-offloading=no` 可能会导致不可预测的行为，例如，数据包可能仍由硬件路由并完全绕过 CPU/防火墙。
:::

下一个示例在所有端口上启用硬件路由，但上游端口（sfp-sfpplus16）除外。进出 sfp-sfpplus16 的数据包将进入 CPU，因此将受到防火墙/NAT 处理的影响。

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
/interface/ethernet/switch/port/set [find] l3-hw-offloading=yes
/interface/ethernet/switch/port/set sfp-sfpplus16 l3-hw-offloading=no
```

:::warning
现有的连接可能不受 `l3-hw-offloading` 设置更改的影响。
:::

### L3HW 设置

#### 基本设置

L3HW 设置菜单允许配置三层硬件卸载驱动程序的全局参数。

**子菜单：** `/interface/ethernet/switch/l3hw-settings`

| 属性 | 描述 |
| :-- | :-- |
| **autorestart** (*yes \| no*; 默认值： **no**) | 在发生错误时自动重启 l3hw 驱动程序。否则，如果发生错误，`l3-hw-offloading` 将被禁用，错误代码将显示在交换机设置和 [#monitor](./l3-hardware-offloading.md#monitor) 中。Autorestart 不适用于系统故障，例如 OOM（内存不足）。 |
| **fasttrack-hw** (*yes \| no*; 默认值： **yes**（如果支持）) | 启用或禁用 FastTrack 硬件卸载。除非需要保留硬件 TCAM 内存（例如，用于创建动态交换机 ACL 规则），否则请保持启用。并非所有交换芯片都支持 FastTrack 硬件卸载（请参阅 **hw-supports-fasttrack**）。 |
| **ipv6-hw** (*yes \| no*; 默认值： **no**) | 启用或禁用 IPv6 硬件卸载。由于 IPv6 路由占用大量硬件内存，仅在 IPv6 流量速度足以从硬件路由中获益时才启用它。 |
| **icmp-reply-on-error** (*yes \| no*; 默认值： **yes**) | 由于硬件无法发送 ICMP 消息，因此在发生错误（例如，“Time Exceeded”、“Fragmentation required”等）时，必须将数据包重定向到 CPU 以发送 ICMP 回复。启用 icmp-reply-on-error 有助于网络诊断，但可能会为 DDoS 攻击打开潜在漏洞。禁用 icmp-reply-on-error 会在发生错误时在硬件级别静默丢弃数据包。 |

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **hw-supports-fasttrack** (**yes \| no**) | 指示硬件（交换芯片）是否支持 FastTrack 硬件卸载。 |

#### 高级设置

此菜单允许针对特定用例调整 l3hw 设置。

:::danger
除非 MikroTik 支持或 MikroTik 认证路由工程师指示，否则**不建议**更改高级 L3HW 设置。应用不正确的设置可能会破坏 L3HW 操作。
:::

**子菜单：** `/interface/ethernet/switch/l3hw-settings`

| 属性 | 描述 |
| :-- | :-- |
| **route-queue-limit-high** (*数字*; 默认值： **256**) | 当 **route-queue-size**（参见 [#monitor](./l3-hardware-offloading.md#monitor)）超过此值时，交换机驱动程序停止路由索引。降低此值可加快路由处理，但会增加路由出现在 RouterOS 和硬件内存之间的延迟。设置 **route-queue-limit-high=0** 会在处理队列中有任何路由时禁用路由索引——这是最高效的 CPU 使用方式，但硬件卸载前的延迟最长。当只有静态路由时很有用。不建议与路由协议（如 BGP 或 OSPF）一起使用，因为路由表会频繁变化。 |
| **route-queue-limit-low** (*数字*; 默认值： **0**) | 当 **route-queue-size** 降至该值时，重新启用路由索引。不得超过上限。设置 **route-queue-limit-low=0** 会告诉交换机驱动程序在下次硬件卸载尝试之前处理所有挂起的路由。虽然这是期望的行为，但在持续的 BGP 馈送下可能会完全阻塞硬件卸载。 |
| **shwp-reset-counter** (*数字*; 默认值： **128**) | 重置最短硬件前缀（参见 [#monitor](./l3-hardware-offloading.md#monitor) 中的 **ipv4-shortest-hw-prefix** / **ipv6-shortest-hw-prefix**），并在路由表发生此数量的更改后尝试完整的路由表卸载。在部分卸载时，当整个路由表无法容纳在硬件内存中且较短的前缀被重定向到 CPU 时，理论上无需尝试卸载比 SHWP 短的路由前缀，因为那些无论如何都会被重定向到 CPU。然而，路由表的重大更改可能导致不同的索引布局，从而影响可硬件卸载的路由数量。因此，建议偶尔进行完整的表重新索引。降低此值可能允许更多路由被硬件卸载，但会增加 CPU 使用率，反之亦然。设置 **shwp-reset-counter=0** 会在每次路由表更改后始终进行完整的重新索引。此设置仅在部分卸载期间使用，当 **ipv4-shortest-hw-prefix=0**（以及相应的 ipv6）时无效。 |
| **partial-offload-chunk** (*数字*; 默认值： **1024**，最小值： 16) | 部分卸载中增量添加路由的最小数量。根据交换芯片型号，路由要么按原样卸载（RouterOS 中的每个路由条目对应于硬件内存中的一个条目），要么被索引，索引条目被写入硬件内存。此设置仅在后一种情况下用于部分卸载。根据索引碎片情况，单个 IPv4 路由添加可能占用 -3 到 +6 个 LPM 硬件内存块（某些路由添加可能由于索引碎片整理而降低所需的硬件内存量）。因此，无法预测硬件内存中可以容纳的确切路由数量。交换机驱动程序使用二分算法来查找适合硬件内存的最大路由数量。假设有 128k 条路由，全部无法容纳在硬件内存中。该算法将数量减半并尝试卸载 64k 条路由。假设卸载成功。在下一次迭代中，算法选择 96k，假设失败；然后 80k——再次失败；72k——成功，76k，依此类推，直到成功和失败数量之间的差异低于 **partial-offload-chunk** 值。降低 **partial-offload-chunk** 值会增加硬件卸载的路由数量，但也会提高 CPU 使用率，反之亦然。 |
| **route-index-delay-min** (*时间*; 默认值： **1s**) | 路由处理与其卸载之间的最小延迟。该延迟允许一起处理更多路由并一次性卸载，从而节省 CPU 使用率。它还通过减少每条路由的处理工作来加快整个路由表的卸载。另一方面，它减慢了单个路由的卸载。如果在延迟期间收到额外的路由，则延迟会重置为 **route-index-delay-min** 值。在延迟内不断添加路由会不断重置计时器，直到达到 **route-index-delay-max**。 |
| **route-index-delay-max** (*时间*; 默认值： **10s**) | 路由处理与其卸载之间的最大延迟。当达到最大延迟时，已处理的路由会被卸载，即使还有更多路由待处理。但是，**route-queue-limit-high** 的优先级高于此设置，这意味着当达到特定队列大小时，索引/卸载仍会暂停。 |
| **neigh-keepalive-interval** (*时间*; 默认值： **15s**，最小值： 5s) | 邻居（主机）keepalive 间隔。当主机（IP 邻居）被硬件卸载时，所有进出它的流量都由交换芯片路由，RouterOS 可能认为该邻居不活动并将其删除。为防止这种情况，交换机驱动程序必须通过定期向 RouterOS 发送刷新来保持已卸载的邻居处于活动状态。 |
| **neigh-discovery-interval** (*时间*; 默认值： **1m37s**，最小值： 30s) | 不幸的是，交换芯片不提供每个邻居的统计信息。因此，检查已卸载主机是否仍然活动的唯一方法是向所连接的网络发送定期的 ARP（IPv4）/邻居发现（IPv6）请求。增加该值会降低广播流量，但可能会使不活动的主机在硬件内存中保留更长时间。邻居发现在邻居 keepalive 工作内触发。因此，发现时间会向上舍入到下一个 keepalive 会话。为 **neigh-discovery-interval** 选择一个不能被 **neigh-keepalive-interval** 整除的值，以便在不同的会话中发送 ARP/ND 请求，防止广播突发。 |
| **neigh-discovery-burst-limit**(*数字*; 默认值： **64**) | 一次可以发送的 ARP/ND 请求的最大数量。 |
| **neigh-discovery-burst-delay** (*时间*; 默认值： **300ms**，最小值： 10ms) | 如果请求数量超过 **neigh-discovery-burst-limit**，则 ARP/ND 后续突发之间的延迟。 |

:::info
某些设置仅适用于特定的交换机型号。
:::

#### 监控

L3HW 监控功能已在 RouterOS 7.10 版本中引入。它允许监控与 L3HW 相关的交换芯片和驱动程序统计信息。

```ros
/interface/ethernet/switch/l3hw-settings/monitor
        ipv4-routes-total: 99363
           ipv4-routes-hw: 61250
          ipv4-routes-cpu: 38112
  ipv4-shortest-hw-prefix: 24
               ipv4-hosts: 87
        ipv6-routes-total: 15
           ipv6-routes-hw: 11
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 7
         route-queue-size: 118
     fasttrack-ipv4-conns: 2031
   fasttrack-hw-min-speed: 0
              nexthop-cap: 8192
            nexthop-usage: 93
    vxlan-mtu-packet-drop: 0
```

**统计信息**

| 属性 | 描述 |
| :-- | :-- |
| **ipv4-routes-total** | 交换机驱动程序处理的 IPv4 路由总数。 |
| **ipv4-routes-hw** | 硬件卸载的 IPv4 路由数量（也称为硬件路由） |
| **ipv4-routes-cpu** | 重定向到 CPU 的 IPv4 路由数量（也称为软件路由） |
| **ipv4-shortest-hw-prefix** | IPv4 的*最短硬件前缀（SHWP）*。如果整个 IPv4 路由表无法容纳在硬件内存中，则应用*部分卸载*，其中最长前缀被硬件卸载，而较短前缀被重定向到 CPU。此字段显示卸载到硬件内存的最短路由前缀（/x）。所有比此前缀短的前缀均由 CPU 处理。`ipv4-shortest-hw-prefix=0` 表示整个 IPv4 路由表已卸载到硬件内存。 |
| **ipv4-hosts** | 硬件卸载的 IPv4 主机（/32 路由）数量 |
| **ipv6-routes-total** <sup>1</sup> | 交换机驱动程序处理的 IPv6 路由总数。 |
| **ipv6-routes-hw** <sup>1</sup> | 硬件卸载的 IPv6 路由数量（也称为硬件路由） |
| **ipv6-routes-cpu** <sup>1</sup> | 重定向到 CPU 的 IPv6 路由数量（也称为软件路由） |
| **ipv6-shortest-hw-prefix** <sup>1</sup> | IPv6 的*最短硬件前缀（SHWP）*。如果整个 IPv6 路由表无法容纳在硬件内存中，则应用*部分卸载*，其中最长前缀被硬件卸载，而较短前缀被重定向到 CPU。此字段显示卸载到硬件内存的最短路由前缀（/x）。所有比此前缀短的前缀均由 CPU 处理。`ipv6-shortest-hw-prefix=0` 表示整个 IPv6 路由表已卸载到硬件内存。 |
| **ipv6-hosts** <sup>1</sup> | 硬件卸载的 IPv6 主机（/128 路由）数量 |
| **route-queue-size** | 等待交换芯片驱动程序处理的路由队列中的路由数量。在正常工作条件下，此字段为 0，表示所有路由都已由驱动程序处理。 |
| **nexthop-cap** | 下一跳容量。 |
| **nexthop-usage** | 当前使用的下一跳数量。 |
| **vxlan-mtu-packet-drop** | 由于超过接口 MTU 设置而丢弃的 VXLAN 数据包数量。 |
| **fasttrack-ipv4-conns** <sup>2</sup> | 硬件卸载的 FastTrack 连接数量。 |
| **fasttrack-hw-min-speed** <sup>2</sup> | 当用于存储 FastTrack 的硬件内存已满时，此字段显示硬件卸载的 FastTrack 连接的最小速度（以字节/秒为单位）。较慢的连接由 CPU 路由。 |

---

<sup>1</sup> 仅当启用 IPv6 硬件路由（`ipv6-hw=yes`）时，IPv6 统计信息才会出现  
<sup>2</sup> 仅当启用 FastTrack 连接的硬件卸载（`fasttrack-hw=yes`）时，FastTrack 统计信息才会出现

#### 高级监控

监控的高级版本，为高级用户提供额外的遥测数据。高级监控包含基本监控的所有数据以及下面列出的字段。

```ros
/interface/ethernet/switch/l3hw-settings/advanced> monitor once
        ipv4-routes-total: 29968
           ipv4-routes-hw: 29957
          ipv4-routes-cpu: 11
  ipv4-shortest-hw-prefix: 0
               ipv4-hosts: 3
        ipv6-routes-total: 4
           ipv6-routes-hw: 0
          ipv6-routes-cpu: 4
  ipv6-shortest-hw-prefix: 0
               ipv6-hosts: 0
         route-queue-size: 0
         route-queue-rate: 0
       route-process-rate: 0
     fasttrack-ipv4-conns: 0
     fasttrack-queue-size: 0
     fasttrack-queue-rate: 0
   fasttrack-process-rate: 0
   fasttrack-hw-min-speed: 0
   fasttrack-hw-offloaded: 0
    fasttrack-hw-unloaded: 0
                  lpm-cap: 54560
                lpm-usage: 31931
             lpm-bank-cap: 2728
           lpm-bank-usage: 46,0,0,0,2589,2591,1983,0,2728,2728,2728,2728,2728,2728,2728,2728,2728,170,0,0
                  pbr-cap: 8192
                pbr-usage: 0
             pbr-lpm-bank: 3
                nat-usage: 0
              nexthop-cap: 8192
            nexthop-usage: 85
```

**统计信息**

| 属性 | 描述 |
| :-- | :-- |
| **route-queue-rate** | 路由添加到交换机驱动程序处理队列的速率。换句话说，**route-queue-size** 的增长速率（路由/秒） |
| **route-process-rate** | 交换机驱动程序处理先前排队路由的速率。换句话说，**route-queue-size** 的缩减速率（路由/秒） |
| **fasttrack-queue-size** | 等待交换芯片驱动程序处理的 FastTrack 连接队列中的连接数量。 |
| **fasttrack-queue-rate** | FastTrack 连接添加到交换机驱动程序处理队列的速率。换句话说，**fasttrack-queue-size** 的增长速率（连接/秒） |
| **fasttrack-process-rate** | 交换机驱动程序处理先前排队 FastTrack 连接的速率。换句话说，**fasttrack-queue-size** 的缩减速率（连接/秒） |
| **fasttrack-hw-offloaded** | 卸载到硬件的 FastTrack 连接数量。计数器每秒（或每个监控间隔）重置一次。 |
| **fasttrack-hw-unloaded** | 从硬件卸载（重定向到软件路由）的 FastTrack 连接数量。计数器每秒（或每个监控间隔）重置一次。 |
| **lpm-cap** | LPM 硬件表的大小（LPM = 最长前缀匹配）。LPM 存储用于硬件路由的路由索引。并非所有交换芯片型号都使用 LPM。其他型号使用 TCAM。 |
| **lpm-usage** | 已使用的 LPM 块数量。**lpm-usage** / **lpm-cap** = 使用百分比。 |
| **lpm-bank-cap** | LPM 内存按 bank 组织——特殊的内存单元。bank 大小取决于交换芯片型号。此值显示单个 bank 的大小（以 LPM 块为单位）。**lpm-cap** / **lpm-bank-cap** = bank 数量（通常为 20）。 |
| **lpm-bank-usage** | 每个 bank 的 LPM 使用量（以 LPM 块为单位） |
| **pbr-cap** | 基于策略的路由（PBR）硬件表的大小。PBR 用于 FastTrack 连接的 NAT 卸载。 |
| **pbr-usage** | 已使用的 PBR 条目数量。**pbr-usage** / **pbr-cap** = 使用百分比。 |
| **pbr-lpm-bank** | PBR 与路由表共享 LPM 内存 bank。此值显示与 PBR 共享的 LPM bank 索引（0 = 第一个 bank）。 |
| **nat-usage** | 已使用的 NAT 硬件条目数量（用于 FastTrack 连接）。 |

### 接口列表

不可能直接使用接口列表来控制 `l3-hw-offloading`，因为接口列表可能包含虚拟接口（如 VLAN），而 `l3-hw-offloading` 设置必须仅应用于物理交换机端口。例如，如果同一个交换机端口（trunk 端口）上运行两个 VLAN 接口（vlan20 和 vlan30），则不可能在 vlan20 上启用硬件路由而在 vlan30 上保持禁用。

但是，接口列表可以用作端口选择器。以下示例演示了如何在 LAN 端口（属于“LAN”接口列表的端口）上启用硬件路由，并在 WAN 端口上禁用它：

```ros
:foreach i in=[/interface/list/member/find where list=LAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=yes
}

:foreach i in=[/interface/list/member/find where list=WAN] do={
    /interface/ethernet/switch/port/set [/interface/list/member/get $i interface] l3-hw-offloading=no
}
```

请注意，由于接口列表不直接用于硬件路由控制，**修改接口列表也不会自动反映在 l3hw 更改中**。例如，将交换机端口添加到“LAN”接口列表不会自动在其上启用 `l3-hw-offloading`。用户必须重新运行上述脚本才能应用更改。

### MTU

硬件支持最多 8 个 MTU 配置文件，这意味着用户可以为接口设置最多 8 个不同的 MTU 值：默认的 1500 加上七个自定义值。

:::tip
建议在更改接口上的 MTU/L2MTU 值时禁用 `l3-hw-offloading`。
:::

**MTU 更改示例**

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/set sfp-sfpplus1 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus2 mtu=9000 l2mtu=9022
/interface/set sfp-sfpplus3 mtu=10000 l2mtu=10022
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### 二层依赖

三层硬件处理位于二层硬件处理之上。因此，L3HW 卸载需要底层接口上的 L2HW 卸载。后者默认启用，但也有一些例外。例如，支持 Marvell Prestera 交换机的 MikroTik 设备仅支持一个硬件桥接。如果存在多个桥接，则其他桥接由 CPU 处理，并且不进行 L3HW。

另一个例子是 ACL 规则。如果规则将流量重定向到 CPU 进行软件处理，则不会触发硬件路由（L3HW）：

#### 在特定端口上禁用硬件处理的 ACL 规则

```ros
/interface/ethernet/switch/rule/add switch=switch1 ports=ether1 redirect-to-cpu=yes
```

:::tip
建议在 L2 配置期间关闭 L3HW 卸载。
:::

为确保第 3 层在软件和硬件方面与第 2 层同步，我们建议在配置第 2 层功能时禁用 L3HW。该建议适用于以下配置：

- 添加/移除/启用/禁用桥接。
- 向桥接添加/从桥接移除交换机端口。
- 绑定交换机端口 / 移除绑定。
- 更改 VLAN 设置。
- 更改交换机端口上的 MTU/L2MTU。
- 更改以太网（MAC）地址。

简而言之，在 `/interface/bridge/` 和 `/interface/vlan/` 下进行更改时，请禁用 `l3-hw-offloading`：

#### 二层配置模板

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no

/interface/bridge
# 在此处放置桥接配置更改

/interface/vlan
# 定义/更改 VLAN 接口
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

### MAC telnet

在 **98DX8xxx**、**98DX4xxx** 或 **98DX325x** 交换芯片上启用 L3HW 卸载时，MAC telnet 存在限制。来自 MAC Telnet 的数据包会被丢弃，无法到达 CPU，因此对设备的访问将失败。

如果希望将 MAC telnet 与 L3HW 结合使用，可以创建特定的 ACL 规则来强制这些数据包进入 CPU。

例如，如果需要在 sfp-sfpplus1 和 sfp-sfpplus2 上进行 MAC telnet 访问，则需要添加此 ACL 规则。可以使用 `ports` 设置选择更多接口。

```ros
/interface/ethernet/switch/rule
add dst-port=20561 ports=sfp-sfpplus1,sfp-sfpplus2 protocol=udp redirect-to-cpu=yes switch=switch1
```

### VLAN 间路由

由于 L3HW 依赖于 L2HW，而 L2HW 负责 VLAN 处理，因此 VLAN 间*硬件*路由需要底层有硬件桥接。即使特定 VLAN 只有一个 tagged 端口成员，该端口也必须是桥接成员。不要将 VLAN 接口直接分配给交换机端口！否则，L3HW 卸载将失败，流量将由 CPU 处理：

`/interface/vlan/add interface=ether2 name=vlan20 vlan-id=20`

而是将 VLAN 接口分配给桥接。这样，VLAN 配置会被卸载到硬件，并且在启用 L3HW 的情况下，流量将进行 VLAN 间硬件路由。

#### VLAN 配置示例

```ros
/interface/ethernet/switch/set 0 l3-hw-offloading=no
/interface/bridge/port/add bridge=bridge interface=ether2
/interface/bridge/vlan/add bridge=bridge tagged=bridge,ether2 vlan-ids=20
/interface/vlan/add interface=bridge name=vlan20 vlan-id=20
/ip/address/add address=192.0.2.1/24 interface=vlan20
/interface/bridge/set bridge vlan-filtering=yes
/interface/ethernet/switch/set 0 l3-hw-offloading=yes
```

:::info
对于 VLAN 间路由，桥接接口必须是每个可路由的 `/interface/bridge/vlan/` 条目的 tagged 成员。
:::

### 每 VLAN 卸载

从 RouterOS 7.21 开始，可以使用 `/interface/vlan` 菜单中的 `l3-hw-offloading=yes|no` 设置为每个单独的 VLAN 接口配置 L3HW 卸载。这提供了更精细的控制，可以决定哪些 VLAN（及其相关路由）被卸载到交换芯片，哪些由 CPU 处理。不再需要为了禁用特定 VLAN 的 L3HW 路由而在交换机端口上禁用 L3HW。

仅当满足以下**所有**条件时，VLAN 接口才会被卸载（获得 H 标志）：

- VLAN 接口具有 `l3-hw-offloading=yes`。
- VLAN 接口创建在硬件卸载的、启用 vlan-filtering 的桥接上。
- 作为 VLAN 成员的所有交换机端口都具有 l3-hw-offloading=yes。

对于 VLAN 间路由，入口和出口 VLAN 都必须进行硬件卸载，否则数据包将被发送到 CPU。

:::info
如果交换机端口承载多个具有不同 L3HW 设置的 VLAN，请保持端口的 `l3-hw-enabled=yes`。
:::

### L3HW MAC 地址范围限制（仅限 DX2000/DX3000 系列）

Marvell Prestera DX2000 和 DX3000 交换芯片存在硬件限制，只允许为每个接口配置 MAC 地址的最后一个（最低有效）八位字节。其他五个（最高有效）八位字节是全局配置的，因此所有接口（交换机端口、桥接、VLAN）必须相同。换句话说，MAC 地址必须采用“**XX:XX:XX:XX:XX:??**”格式，其中：

- “**XX:XX:XX:XX:XX**”部分对所有接口都是通用的。
- “**??**”是可变部分。

**此要求仅适用于第 3 层（路由）。** 第 2 层（桥接）不使用交换机的以太网地址。此外，它不适用于桥接端口，因为它们使用桥接的 MAC 地址。

公共五个八位字节的要求适用于：

- 启用了硬件路由（`l3-hw-offloading=yes`）的独立交换机端口（非桥接成员）。
- 桥接本身。
- VLAN 接口（默认使用桥接 MAC 地址的接口）。

## 路由配置

---

### 抑制硬件卸载

默认情况下，所有路由都是硬件候选路由。为了进一步微调要卸载的流量，每条路由都有一个选项来禁用/启用 **`suppress-hw-offload`**。

例如，如果我们知道大部分流量流向服务器所在的网络，我们可以仅启用到该特定目的地的卸载：

```ros
/ip/route/set [find where static && dst-address!="192.168.3.0/24"] suppress-hw-offload=yes
```

现在只有到 192.168.3.0/24 的路由具有 H 标志，表明它将是唯一有资格被选择进行硬件卸载的路由：

```ros
[admin@MikroTik] > /ip/route/print where static
Flags: A - ACTIVE; s - STATIC, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, DISTANCE
#     DST-ADDRESS       GATEWAY         D
0 As  0.0.0.0/0         172.16.2.1      1
1 As  10.0.0.0/8        10.155.121.254  1
2 AsH 192.168.3.0/24    172.16.2.1      1
```

:::danger
H 标志并不表示该路由实际上已被硬件卸载；它仅表示该路由可以被选择进行硬件卸载。
:::

### 路由过滤器

对于 OSPF 和 BGP 等动态路由协议，可以使用 [路由过滤器](../user-guides/routing-and-networking-protocols/route-selection-and-filtering.md) 来抑制硬件卸载。例如，要抑制所有 OSPF 实例路由的硬件卸载，请使用“**`suppress-hw-offload yes`**”属性：

```ros
/routing/ospf/instance
set [find name=instance1] in-filter-chain=ospf-input
/routing/filter/rule
add chain="ospf-input" rule="set suppress-hw-offload yes; accept"
```

### 卸载 Fasttrack 连接

防火墙过滤规则具有用于 Fasttrack 的 **`hw-offload`** 选项，允许微调连接卸载。由于用于 Fasttrack 连接的硬件内存非常有限，我们可以选择要卸载的连接类型，从而受益于接近线速的流量。下一个示例仅卸载 TCP 连接，而 UDP 数据包通过 CPU 路由，不占用硬件内存：

```ros
/ip/firewall/filter
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=established,related hw-offload=no
add action=accept chain=forward connection-state=established,related
```

### 无状态硬件防火墙

虽然连接跟踪和有状态防火墙只能由 CPU 执行，但硬件可以通过 [交换机规则（ACL）](./marvell-prestera-switch-chip-features.md#switch-rules-acl) 执行无状态防火墙。下一个示例在硬件级别阻止从 ether1 访问 MySQL 服务器，并将来自 ether2 和 ether3 的数据包重定向到 CPU/防火墙：

```ros
/interface/ethernet/switch/rule
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether1 new-dst-ports=""
add switch=switch1 dst-address=10.0.1.2/32 dst-port=3306 ports=ether2,ether3 redirect-to-cpu=yes
```

### 交换机规则（ACL）与 Fasttrack 硬件卸载

某些防火墙规则可以通过 [交换机规则（ACL）](./marvell-prestera-switch-chip-features.md#switch-rules-acl) 和 CPU [防火墙过滤器](../firewall-and-quality-of-service/firewall/filter.md) + Fasttrack 硬件卸载来实现。两种方案都能提供接近线速的性能。那么问题是用哪个？

首先，[并非所有设备都支持 Fasttrack 硬件卸载](./l3-hardware-offloading.md#l3hw-device-support)，如果没有硬件卸载，防火墙过滤器仅使用软件路由，这比硬件路由慢得多。其次，即使 Fasttrack 硬件卸载是一个选项，经验法则是：

:::tip
如果可能，始终使用交换机规则（ACL）。
:::

交换机规则与 Fasttrack 连接共享硬件内存。但是，硬件资源是为每个 Fasttrack 连接分配的，而单个 ACL 规则可以匹配多个连接。例如，如果您有一个连接到 sfp-sfpplus1 VLAN 10 的访客 WiFi 网络，并且不希望它访问您的内部网络，只需创建一个 ACL 规则：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=sfp-sfpplus1 vlan-id=10 dst-address=10.0.0.0/8 new-dst-ports=""
```

匹配的数据包将在硬件级别被丢弃。这比让*所有*访客数据包进入 CPU 进行防火墙过滤要好得多。

当然，ACL 规则不能匹配所有内容。例如，ACL 规则无法过滤连接状态：接受已建立的，丢弃其他的。这就是 Fasttrack 硬件卸载发挥作用的地方——默认将数据包重定向到 CPU 进行防火墙过滤，然后卸载已建立的 Fasttrack 连接。但是，为整个交换机或端口禁用 `l3-hw-offloading` 并不是唯一的选择。

:::info
定义带有 `redirect-to-cpu=yes` 的 ACL 规则，而不是在交换机端口上设置 `l3-hw-offloading=no`，以缩小进入 CPU 的流量范围。
:::

### 硬件卸载的 VRF

硬件卸载的 VRF 在 [98DX8xxx、98DX4xxx、98DX325x、98CX8410](#ccr2xxx-crs3xx-crs5xx-switch-98dx8xxx-and-98dx4xxx-series) 和 [98DX7xxx](#crs8xx-switch-98dx7xxx-series) 交换芯片上受支持。在 [98DX3xxx 和 98DX2xxx](#crs3xx-switch-98dx3xxx-and-98dx2xxx-series) 系列上不受支持。

如果路由在 VRF 中，并且出口接口具有 L3HW 能力，交换芯片将路由该数据包。您可以将任何具有 L3HW 能力的接口（以太网、绑定、桥接、VLAN）与 VRF 关联。始终将主接口与 VRF 关联，而不是带有 `S`（从属）标志的接口，例如桥接或绑定端口。Fasttrack、NAT 和 VXLAN 卸载仅限于 `main` 路由表。

VRF 在 `/ip/vrf` 下配置。有关更多详细信息，请参阅 [VRF](../user-guides/routing-and-networking-protocols/vrf) 手册。

98DX8208、98DX8212、98DX8332、98DX3257、98DX3255 支持最多 512 个 VRF 表。所有其他受支持的交换芯片支持最多 1024 个。

#### 通过 ACL 分配 VRF

L3HW 支持使用 ACL 交换机规则将 VRF 分配给入口流量。`/interface/ethernet/switch/rule` 中的 `new-vrf` 选项允许将匹配