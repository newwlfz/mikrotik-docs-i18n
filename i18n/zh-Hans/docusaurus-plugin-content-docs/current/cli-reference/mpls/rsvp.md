# Rsvp

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## mpls/traffic-eng

**条件：** !smips
**类型：** 目录

### mpls/traffic-eng/flow

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="N" typ="ingress"></ArgTableRow>
<ArgTableRow arg="E" typ="egress"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
<ArgTableRow arg="R" typ="reservation"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="vrf" typ="enum"></ArgTableRow>
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="sender" typ="string"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="out-labels" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="out-nexthop" typ="address (flags=46i)"></ArgTableRow>
<ArgTableRow arg="bw" typ="num"></ArgTableRow>
<ArgTableRow arg="style" typ="enum (unknown | shared | fixed)"></ArgTableRow>
<ArgTableRow arg="psb" typ="string"></ArgTableRow>
<ArgTableRow arg="blockade" typ="string"></ArgTableRow>
<ArgTableRow arg="resv" typ="string"></ArgTableRow>
<ArgTableRow arg="rsb" typ="string"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/interface

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="resource-class" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="refresh-time" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="use-udp" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="blockade-k-factor" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="te-metric" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="igp-flood-period" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="up-flood-thresholds" typ="multi { array-id, num [0 .. 100]
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="down-flood-thresholds" typ="multi { array-id, num [0 .. 100]
 }" unset="1"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="remaining-bw" typ="num"></ArgTableRow>
<ArgTableRow arg="remaining-bw-prios" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="lih" typ="num"></ArgTableRow>
<ArgTableRow arg="local-address-ip" typ="address (flags=46)"></ArgTableRow>
<ArgTableRow arg="local-address-ip6" typ="address (flags=46)"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/path

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="use-cspf" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1"></ArgTableRow>
<ArgTableRow arg="hops" typ="multi { array-id, array-id, super { address (flags=46)
, /bool
 } { address (flags=46)
, /bool
 }
 }" unset="1"></ArgTableRow>
</ArgTable>

### mpls/traffic-eng/tunnel

**条件：** !smips
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="F" typ="forwarding"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="from-address" typ="address (flags=46)" unset="1">隧道的入口地址。如果未设置，则选择最小的IP地址。</ArgTableRow>
<ArgTableRow arg="to-address" typ="address (flags=46)" mandatory="1">TE隧道的远端。</ArgTableRow>
<ArgTableRow arg="bandwidth" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="primary-path" typ="enum" unset="1">在 `/mpls/traffic-eng/path` 菜单中定义的主标签交换路径。</ArgTableRow>
<ArgTableRow arg="secondary-paths" typ="multi { array-id, enum
 }" unset="1">当主路径失败时，TE隧道使用的标签交换路径列表。路径在 `/mpls/traffic-eng/path` 菜单中定义。</ArgTableRow>
<ArgTableRow arg="primary-retry-interval" typ="time" unset="1">隧道尝试使用主路径的间隔时间。</ArgTableRow>
<ArgTableRow arg="secondary-standby" typ="bool" unset="1"></ArgTableRow>
<ArgTableRow arg="bandwidth-limit" typ="num" unset="1">定义TE隧道的实际带宽限制。限制以指定隧道 `bandwidth` 的百分比配置。</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-range" typ="composite { ,  }" unset="1">自动带宽调整范围。</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-reserve" typ="num" unset="1">指定额外预留带宽的百分比。</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-avg-interval" typ="time" unset="1">测量实际数据量的间隔时间，从中计算平均带宽。</ArgTableRow>
<ArgTableRow arg="auto-bandwidth-update-interval" typ="time" unset="1">隧道跟踪最高平均速率的间隔时间。</ArgTableRow>
<ArgTableRow arg="setup-priority" typ="num" unset="1">该参数用于决定此会话是否可以抢占其他会话。0 表示最高优先级。</ArgTableRow>
<ArgTableRow arg="holding-priority" typ="num" unset="1">用于决定此会话是否可以被其他会话抢占。0 表示最高优先级。</ArgTableRow>
<ArgTableRow arg="record-route" typ="bool" unset="1">如果启用，发送节点将收到关于LSP隧道实际经过路由的信息。Record Route 类似于路径向量，因此可用于环路检测。</ArgTableRow>
<ArgTableRow arg="affinity-include-all" typ="num" unset="1">仅当 `resource-class` 匹配所有指定比特位时使用该接口。</ArgTableRow>
<ArgTableRow arg="affinity-include-any" typ="num" unset="1">当 `resource-class` 匹配任意指定比特位时使用该接口。</ArgTableRow>
<ArgTableRow arg="affinity-exclude" typ="num" unset="1">当 `resource-class` 匹配任意指定比特位时不使用该接口。</ArgTableRow>
<ArgTableRow arg="reoptimize-interval" typ="time" unset="1">隧道重新优化当前路径的间隔时间。如果当前路径不是最佳路径，优化后将使用最佳路径。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="session" typ="string"></ArgTableRow>
<ArgTableRow arg="forwarding-on" typ="string"></ArgTableRow>
<ArgTableRow arg="primary" typ="string"></ArgTableRow>
<ArgTableRow arg="primary-pending" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary" typ="string"></ArgTableRow>
<ArgTableRow arg="secondary-pending" typ="string"></ArgTableRow>
</ArgTable>

#### mpls/traffic-eng/tunnel/reoptimize

**条件：** !smips
**类型：** 命令