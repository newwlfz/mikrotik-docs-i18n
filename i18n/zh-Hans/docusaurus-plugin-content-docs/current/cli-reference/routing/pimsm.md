# Pimsm

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/pimsm

**条件：** !smips
**类型：** 目录

### routing/pimsm/bsr

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hash-mask-length" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="enum (accept-any | accept-preferred | candidate | pending | elected)"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/candidate

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="scope4" typ="address (flags=4/)" unset="1"></ArgTableRow>
<ArgTableRow arg="scope6" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="hashmask-length" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="state" typ="enum (candidate | pending | elected)"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/rp-candidate

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="holdtime" typ="num"></ArgTableRow>
</ArgTable>

#### routing/pimsm/bsr/rp-set

**条件：** !smips
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/v)"></ArgTableRow>
<ArgTableRow arg="rp.address" typ="object { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="rp.priority" typ="object { num
 }"></ArgTableRow>
<ArgTableRow arg="rp.timeout" typ="object { time
 }"></ArgTableRow>
</ArgTable>

### routing/pimsm/igmp-interface-template

**条件：** !smips
**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1"></ArgTableRow>
</ArgTable>

### routing/pimsm/instance

**条件：** !smips
**类型：** 目录

instance 菜单定义了 PIM-SM 的主要设置。该实例随后用于所有其他 PIM 相关配置，如 interface-template、静态 RP 和 Bootstrap Router。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum">用于控制连接的 VRF 名称。</ArgTableRow>
<ArgTableRow arg="name" typ="string">实例的名称。</ArgTableRow>
<ArgTableRow arg="afi" typ="enum (ip | ipv6)">指定 PIM 的地址族。</ArgTableRow>
<ArgTableRow arg="switch-to-spt" typ="bool">当组播数据带宽阈值达到时，是否切换到最短路径树（SPT）。如果禁用此选项，路由器将不会从协议阶段一（注册封装）进入原生组播流量转发。建议启用此选项。</ArgTableRow>
<ArgTableRow arg="switch-to-spt-interval" typ="time">用于统计组播数据带宽的时间间隔，与 `switch-to-spt-bytes` 配合使用以确定是否达到切换阈值。</ArgTableRow>
<ArgTableRow arg="switch-to-spt-bytes" typ="num">组播数据带宽阈值。如果在指定时间间隔内达到此阈值，则切换到最短路径树（SPT）。如果配置值为 0，则立即进行切换。</ArgTableRow>
<ArgTableRow arg="crp-advertise-contained" typ="bool">当前未实现。</ArgTableRow>
<ArgTableRow arg="bsm-forward-back" typ="bool">当前未实现。</ArgTableRow>
<ArgTableRow arg="rp-hash-mask-length" typ="num">哈希掩码允许更改将多少个组映射到匹配的 RP 之一。</ArgTableRow>
<ArgTableRow arg="rp-static-override" typ="bool">更改静态 RP 的选择优先级。禁用时，bootstrap RP 集合具有更高优先级。启用时，静态 RP 具有更高优先级。</ArgTableRow>
<ArgTableRow arg="ssm-range" typ="address (flags=46/)">当前未实现。</ArgTableRow>
</ArgTable>

### routing/pimsm/interface

**条件：** !smips
**类型：** 目录

interface 菜单显示当前参与 PIM 的所有接口及其状态。此菜单包含由已定义的接口模板创建的动态和只读条目。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="P" typ="designated-router">指定路由器</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">加入跟踪</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum"></ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="dr" typ="switch"></ArgTableRow>
<ArgTableRow arg="join-tracking" typ="switch"></ArgTableRow>
<ArgTableRow arg="priority" typ="num"></ArgTableRow>
<ArgTableRow arg="propogation-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="override-interval" typ="time"></ArgTableRow>
</ArgTable>

### routing/pimsm/interface-template

**条件：** !smips
**类型：** 目录

interface template 菜单定义了哪些接口将参与 PIM，以及将使用的每接口配置。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">此接口模板所属的 PIM 实例名称。</ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { iface_enum {  } {  }
 }" unset="1">将参与 PIM 的接口列表。</ArgTableRow>
<ArgTableRow arg="hello-period" typ="time">Hello 消息的周期性发送间隔。</ArgTableRow>
<ArgTableRow arg="hello-delay" typ="time">接口启动或检测到新邻居时，初始 Hello 消息的随机化发送间隔。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">指定路由器（DR）优先级。在每个网络上选举一个指定路由器。仅当所有邻居都通告了优先级选项时才使用该优先级。数值最大的优先级被优先选择。如果优先级相同或未使用优先级，则选择 IP 地址数值最大的路由器。</ArgTableRow>
<ArgTableRow arg="join-prune-period" typ="time"></ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">设置剪枝挂起定时器的值。上游路由器使用它来确定在剪枝启用了加入抑制的接口之前，应等待多长时间的 Join 覆盖消息。</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">设置在启用了加入抑制的网络上调度延迟的覆盖 Join 消息时，用于随机化的最大时间段。</ArgTableRow>
<ArgTableRow arg="join-tracking-support" typ="bool">设置 Hello 消息中 LAN 剪枝延迟选项中的跟踪（T）位的值。启用后，路由器通告其禁用加入抑制的意愿。如果禁用了加入抑制，上游路由器可以显式跟踪各个下游路由器的加入成员关系。除非链路上的所有 PIM 路由器都协商了此能力，否则无法实现显式跟踪和禁用加入抑制机制。</ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address (flags=46)
 }" unset="1"></ArgTableRow>
</ArgTable>

### routing/pimsm/neighbor

**条件：** !smips
**类型：** 目录

neighbor 菜单显示所有检测到的正在运行 PIM 的邻居及其状态。此菜单包含动态和只读条目。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="R" typ="designated-router">指定路由器</ArgTableRow>
<ArgTableRow arg="J" typ="join-tracking">加入跟踪</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum">检测到该邻居的 PIM 实例名称。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46i)">显示邻居的 IP 地址以及检测到该邻居的本地接口。</ArgTableRow>
<ArgTableRow arg="priority" typ="num">指示邻居的优先级值。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">显示如果未收到新的 Hello 消息，邻居从列表中移除前的剩余时间。保持时间等于邻居的 `hello-period * 3.5`。</ArgTableRow>
<ArgTableRow arg="designated-router" typ="bool">显示该邻居是否被选举为指定路由器（DR）。</ArgTableRow>
<ArgTableRow arg="propagation-delay" typ="time">指示邻居在 Hello 消息的 LAN 剪枝延迟选项中通告的传播延迟值。</ArgTableRow>
<ArgTableRow arg="override-interval" typ="time">指示邻居在 Hello 消息的 LAN 剪枝延迟选项中通告的覆盖间隔值。</ArgTableRow>
<ArgTableRow arg="join-tracking" typ="bool">指示邻居在 Hello 消息的 LAN 剪枝延迟选项中通告的跟踪（T）位的值。</ArgTableRow>
</ArgTable>

### routing/pimsm/static-rp

**条件：** !smips
**类型：** 目录

static-rp 菜单允许手动定义组播组到 RP 的映射。这种机制对故障不具备鲁棒性，但至少提供了一种基本的互操作机制。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">未激活</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum" mandatory="1">此静态 RP 所属的 PIM 实例名称。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46/)">属于特定 RP 的组播组。</ArgTableRow>
<ArgTableRow arg="address" typ="address (flags=46)">静态 RP 的 IP 地址。</ArgTableRow>
</ArgTable>

### routing/pimsm/uib-g

**条件：** !smips
**类型：** 目录

上游信息库菜单显示任意源组播（\*,G）和特定源组播（S,G）组及其状态。这些菜单仅包含只读条目。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="R" typ="rp-local">RP 本地</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum">创建该组播组的 PIM 实例名称。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">组播组地址。</ArgTableRow>
<ArgTableRow arg="rp" typ="address (flags=46i)">该组的汇聚点（RP）地址。</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">反向路径转发（RPF）指示该组的 Join 消息所指向的路由器地址和出接口。</ArgTableRow>
<ArgTableRow arg="rp-local" typ="bool">指示组播路由器本身是否为 RP。</ArgTableRow>
</ArgTable>

### routing/pimsm/uib-sg

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="K" typ="keepalive">保持活动</ArgTableRow>
<ArgTableRow arg="S" typ="spt-bit">最短路径树（SPT）位指示转发是否在（S,G）最短路径树上进行，还是在（\*,G）树上进行。路由器可以具有（S,G）状态，但在构建特定源树期间仍可能在（\*,G）状态上进行转发。当 SPT 位为 false 时，仅使用（\*,G）转发状态将来自 S 的数据包转发到 G。当 SPT 位为 true 时，同时使用（\*,G）和（S,G）转发状态。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="instance" typ="enum">创建该组播组的 PIM 实例名称。</ArgTableRow>
<ArgTableRow arg="group" typ="address (flags=46i)">组播组地址。</ArgTableRow>
<ArgTableRow arg="source" typ="address (flags=46i)">组播组的源 IP 地址。</ArgTableRow>
<ArgTableRow arg="rpf" typ="address (flags=46i)">反向路径转发（RPF）指示该组的 Join 消息所指向的路由器地址和出接口。</ArgTableRow>
<ArgTableRow arg="register" typ="enum (join | join-pending | prune)"></ArgTableRow>
</ArgTable>