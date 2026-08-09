# VPLS

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## interface/vpls

**条件：** !smips
**类型：** 目录

所有VPLS接口的列表。此菜单也显示基于BGP动态创建的VPLS接口。

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">禁用</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">动态</ArgTableRow>
<ArgTableRow arg="B" typ="bgp-signaled">BGP信令</ArgTableRow>
<ArgTableRow arg="C" typ="cisco-bgp-signaled">Cisco BGP信令</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="string">接口名称。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">三层最大传输单元。</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">接口的静态MAC地址。未设置时自动生成。</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">地址解析协议。</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { enum (auto) { auto:0 }
, time
 }">ARP条目过期时间。设置为 `auto` 以使用接口类型的默认值。</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">指定是否检测接口是否在运行。若设置为 `no`，接口将始终带有 `running` 标志。</ArgTableRow>
<ArgTableRow arg="peer" typ="address (flags=46v)" mandatory="1">远端对等体的IP地址（RFC 4762 第3.1节）。</ArgTableRow>
<ArgTableRow arg="vpls-id" typ="address (flags=R)" unset="1">标识VPLS隧道的唯一编号。编码为2字节+4字节或4字节+2字节的数字（RFC 4762 第3.2节）。</ArgTableRow>
<ArgTableRow arg="cisco-static-id" typ="num" unset="1">Cisco风格的VPLS隧道ID（RFC 4447 FEC类型0x80）。</ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">伪线类型（RFC 4447 第5.2节）。默认使用 `raw-ethernet`。</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">向远端对等体通告的L2MTU值（RFC 4447 第5.2节）。</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">启用或禁用控制字（RFC 4623 第4节）。常规VPLS隧道与Cisco风格VPLS隧道的默认值不同。Cisco风格默认禁用控制字。更多信息请参阅 [VPLS控制字](../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) 文章。</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">VPLS接口所属的[桥接](../interface/bridge.md)。</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">[桥接端口](../interface/bridge.md#path-cost)的开销。</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">设置为 `none` 时，不使用[桥接水平分割](../interface/bridge.md#horizon)。</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">分配给动态桥接接口的端口VLAN ID（pvid）。仅当桥接 [`vlan-filtering`](../interface/bridge.md#vlan-filtering) 设置为 `yes` 时适用。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bgp-vpls" typ="enum">用于创建动态VPLS接口的[BGP VPLS](../routing/bgp.md#routingbgpvpls)实例名称（RFC 4761 第3.2节）。</ArgTableRow>
<ArgTableRow arg="bgp-vpls-prfx" typ="string">用于创建动态VPLS接口的[BGP VPLS](../routing/bgp.md#routingbgpvpls)实例前缀（RFC 4761 第3.2节）。</ArgTableRow>
</ArgTable>

### interface/vpls/monitor

**条件：** !smips
**类型：** 命令

该命令显示当前VPLS接口状态。

例如：

```ros
[admin@10.0.11.23] /interface/vpls> monitor vpls2
remote-label: 800000
local-label: 43
remote-status: 
transport: 10.255.11.201/32
transport-nexthop: 10.0.11.201
imposed-labels: 800000
```

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="remote-label" typ="num">远端对等体为此伪线分配的MPLS标签（RFC 4447 第5.1节）。</ArgTableRow>
<ArgTableRow arg="local-label" typ="num">本地为此伪线分配的MPLS标签（RFC 4447 第5.1节）。</ArgTableRow>
<ArgTableRow arg="remote-status" typ="ubit (not-forwarding, attachment-circuit-rx-fault, attachment-circuit-tx-fault, pw-rx-fault, pw-tx-fault)">通过LDP状态信令从远端对等体接收的伪线状态（RFC 4447 第5.4节）。</ArgTableRow>
<ArgTableRow arg="remote-group" typ="num">远端对等体的组ID，用于LDP状态撤销聚合（RFC 4447 第5.3节）。</ArgTableRow>
<ArgTableRow arg="te-tunnel" typ="enum">传输接口名称。当VPLS运行在[流量工程](../../user-guides/routing-and-networking-protocols/mpls/traffic-eng.md)隧道上时显示。</ArgTableRow>
<ArgTableRow arg="nexthops" typ="object { enum (expl-null | alert | expl-null6 | impl-null) { expl-null:0, alert:1, expl-null6:2, impl-null:3 }
, address
, iface_enum
 }">正在使用的传输下一跳。</ArgTableRow>
</ArgTable>