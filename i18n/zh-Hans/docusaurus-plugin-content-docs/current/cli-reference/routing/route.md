# 路由

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## routing/route

**类型：** 目录

一个只读表，列出了所有地址族的路由，以及所有被过滤的路由及其所有可能的路由属性。

包含各种路由类型的表格默认输出示例：

```ros
[admin@MikroTik] /routing/route> print
Flags: A - ACTIVE; c, s, a, l, y - COPY; H - HW-OFFLOADED
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
    DST-ADDRESS                 GATEWAY           AFI    D  SCOPE  TA  IMMEDIATE-GW
 lH 10.0.0.0/8                                    ip     0
;;; defconf
As  10.0.0.0/8                  10.155.130.1      ip     1     30  10  10.155.130.1%ether1
 lH 10.155.130.0/25                               ip     0
Ac  10.155.130.0/25             ether1            ip     0     10      ether1
 aH 10.155.130.12/32                              ip     0
 lH 111.13.0.0/24                                 ip     0
Ac  111.13.0.0/24               ether2            ip     0     10      ether2
 aH 111.13.0.1/32                                 ip     0
Ac  111.111.111.2/32            loopback@vrfTest  ip     0     10      loopback
Ac  2111:4::/64                 ether2            ipv6   0     10      ether2
Ac  fe80::%ether1/64            ether1            ipv6   0     10      ether1
Ac  fe80::%ether2/64            ether2            ipv6   0     10      ether2
Ac  fe80::%ether3/64            ether3            ipv6   0     10      ether3
Ac  fe80::%ether4/64            ether4            ipv6   0     10      ether4
Ac  3333::2/128                 loopback@vrfTest  ipv6   0     10      loopback
Ac  fe80::%loopback/64          loopback@vrfTest  ipv6   0     10      loopback
Ay  111.111.111.2/32&65530:100  loopback@vrfTest  vpnv4  0     10   5  loopback
Ay  3333::2/128&65530:100       loopback@vrfTest  vpnv6  0     10   5  loopback
A H ether1                                        link   0
A H ether2                                        link   0
A H ether3                                        link   0
A H ether4                                        link   0
A H loopback                                      link   0
```

包含一些 BGP、OSPF 和其他路由的详细输出示例：

```ros
[admin@MikroTik] /routing/route> print detail
Flags: X - disabled, F - filtered, U - unreachable, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, y - copy; H - hw-offloaded;
+ - ecmp, B - blackhole
  o   afi=ip4 contribution=best-candidate dst-address=0.0.0.0/0 routing-table=main gateway=10.155.101.1%ether1 immediate-gw=10.155.101.1%ether1
       distance=110 scope=20 target-scope=10 belongs-to="OSPF route"
       ospf.metric=2 .tag=111 .type=ext-type-1
       debug.fwp-ptr=0x203425A0

 Ad + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 vrf-interface=ether1 belongs-to="DHCP route"
       debug.fwp-ptr=0x20342060

 As + afi=ip4 contribution=active dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1
       distance=1 scope=30 target-scope=10 belongs-to="Static route"
       debug.fwp-ptr=0x20342060

 Fb   afi=ip4 contribution=filtered dst-address=1.0.0.0/24 routing-table=main gateway=10.155.101.1 immediate-gw=10.155.101.1%ether1 distance=20
       scope=40 target-scope=10 belongs-to="BGP IP routes from 10.155.101.217" rpki=valid
       bgp.peer-cache-id=*B000002 .aggregator="13335:172.68.180.1" .as-path="65530,100,9002,13335" .atomic-aggregate=yes .origin=igp
       debug.fwp-ptr=0x20342960

```

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="F" typ="filtered">该标志表示路由是否被路由过滤器过滤，并被排除在最佳路由之外。</ArgTableRow>
<ArgTableRow arg="U" typ="unreachable">该标志表示路由的下一跳是否不可达。</ArgTableRow>
<ArgTableRow arg="A" typ="active">该标志表示路由是否被选为活动路由，并有资格被添加到 FIB 中。</ArgTableRow>
<ArgTableRow arg="c" typ="connect">连接</ArgTableRow>
<ArgTableRow arg="s" typ="static">静态</ArgTableRow>
<ArgTableRow arg="r" typ="rip">RIP</ArgTableRow>
<ArgTableRow arg="b" typ="bgp">该标志表示此路由是否由 [BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) 协议添加。</ArgTableRow>
<ArgTableRow arg="n" typ="bgp-net">BGP 网络</ArgTableRow>
<ArgTableRow arg="o" typ="ospf">OSPF</ArgTableRow>
<ArgTableRow arg="i" typ="isis">IS-IS</ArgTableRow>
<ArgTableRow arg="d" typ="dhcp">该标志表示路由是否由 DHCP 服务添加。</ArgTableRow>
<ArgTableRow arg="v" typ="vpn">该标志表示路由是否由某个 VPN 协议（PPPoE、L2TP、SSTP 等）添加。</ArgTableRow>
<ArgTableRow arg="m" typ="modem">该标志表示路由是否由 LTE 或 3G 调制解调器添加。</ArgTableRow>
<ArgTableRow arg="a" typ="ldp-address">该标志表示路由条目是否为 LDP 地址。</ArgTableRow>
<ArgTableRow arg="l" typ="ldp-mapping">该标志表示路由条目是否为 LDP 映射。</ArgTableRow>
<ArgTableRow arg="g" typ="slaac">SLAAC</ArgTableRow>
<ArgTableRow arg="y" typ="bgp-mpls-vpn">该标志表示作为 L3VPN 路由进行重新分发的路由副本。VPNv4/6 相关属性附加在此路由上。</ArgTableRow>
<ArgTableRow arg="e" typ="evpn">EVPN</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offloaded">表示路由是否有资格在支持的硬件上进行硬件卸载。</ArgTableRow>
<ArgTableRow arg="+" typ="ecmp">该标志表示路由是否作为 [等价多路径](../../user-guides/routing-and-networking-protocols/routing-decision.md#multipath-ecmp-routes) 路由添加到 FIB 中。</ArgTableRow>
<ArgTableRow arg="B" typ="blackhole">该标志表示是否为黑洞路由。</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="afi" typ="enum (bad | ip | ipv6 | l2vpn | vpnv4 | vpnv6 | l2vpn-cisco | mip4 | mip6 | link | l2vpn-link | evpn)" unset="1">此路由所属的地址族。</ArgTableRow>
<ArgTableRow arg="contribution" typ="enum (filtered | unreachable | candidate | best-candidate | active)">显示路由在选择过程中的贡献状态，例如 “filtered, active, candidate”。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=46i/SR)"></ArgTableRow>
<ArgTableRow arg="routing-table" typ="enum">此路由所属的路由表。</ArgTableRow>
<ArgTableRow arg="ve-id" typ="num"></ArgTableRow>
<ArgTableRow arg="ve-block-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="ve-block-size" typ="num"></ArgTableRow>
<ArgTableRow arg="label" typ="num"></ArgTableRow>
<ArgTableRow arg="pref-src" typ="address (flags=46)" unset="1"></ArgTableRow>
<ArgTableRow arg="gateway" typ="address (flags=46ivL)">配置的网关，实际解析的网关请参见 `immediate-gw` 参数。</ArgTableRow>
<ArgTableRow arg="nexthop-id" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="immediate-gw" typ="multi { address (flags=46i)
 }">显示实际（已解析的）网关和将用于数据包转发的接口。显示格式为 `[ip%interface]`。</ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)" unset="1">当前使用的网关检查选项。</ArgTableRow>
<ArgTableRow arg="distance" typ="num" unset="1"></ArgTableRow>
<ArgTableRow arg="scope" typ="num" unset="1">用于下一跳查找过程的范围。 [了解更多>>](../../user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup)</ArgTableRow>
<ArgTableRow arg="target-scope" typ="num" unset="1">用于下一跳查找过程的目标范围。 [了解更多>>](../../user-guides/routing-and-networking-protocols/routing-decision.md#nexthop-lookup)。</ArgTableRow>
<ArgTableRow arg="vrf-interface" typ="iface_enum" unset="1">仅限内部使用的参数，用于标识路由应添加到哪个 VRF。由动态添加路由的服务使用，例如 DHCP 客户端。出于调试目的显示。</ArgTableRow>
<ArgTableRow arg="belongs-to" typ="string">描述性信息，显示路由的来源。</ArgTableRow>
<ArgTableRow arg="local-address" typ="address (flags=46iv)">连接网络的本地 IP 地址。</ArgTableRow>
<ArgTableRow arg="route-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="total-cost" typ="num"></ArgTableRow>
<ArgTableRow arg="rpki" typ="enum (unknown | valid | invalid)" unset="1">来自 [RPKI](../../user-guides/routing-and-networking-protocols/unicast/rpki.md) 验证过程的前缀当前状态。</ArgTableRow>
<ArgTableRow arg="bgp.session" typ="enum">安装该路由的 [BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) 会话。参见 `/routing/bgp/session` 菜单。</ArgTableRow>
<ArgTableRow arg="bgp.aggregator" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.as-path" typ="string">**`AS_PATH`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.cluster-list" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.communities" typ="multi { string
 }">**`COMMUNITIES`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.ext-communities" typ="multi { string
 }">**`EXTENDED_COMMUNITIES`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.large-communities" typ="multi { string
 }">**`LARGE_COMMUNITIES`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.unknown" typ="multi { string
 }">未知 [BGP](../../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) 属性的十六进制数据块。</ArgTableRow>
<ArgTableRow arg="bgp.originator-id" typ="address (flags=4)"></ArgTableRow>
<ArgTableRow arg="bgp.nexthop" typ="multi { address (flags=4)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.out-nexthop" typ="multi { address (flags=4iv)
 }"></ArgTableRow>
<ArgTableRow arg="bgp.weight" typ="num"></ArgTableRow>
<ArgTableRow arg="bgp.local-pref" typ="num">**`LOCAL_PREF`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.igp-metric" typ="num">**`IGP_METRIC`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.pmsi" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.med" typ="num">**`MED`** BGP 属性的值。</ArgTableRow>
<ArgTableRow arg="bgp.atomic-aggregate" typ="bool"></ArgTableRow>
<ArgTableRow arg="bgp.origin" typ="enum (igp | egp | incomplete)"></ArgTableRow>
<ArgTableRow arg="bgp.esi" typ="string"></ArgTableRow>
<ArgTableRow arg="bgp.otc" typ="num"></ArgTableRow>
<ArgTableRow arg="route-distinguisher" typ="string"></ArgTableRow>
<ArgTableRow arg="rip.tag" typ="num"></ArgTableRow>
<ArgTableRow arg="rip.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.tag" typ="num"></ArgTableRow>
<ArgTableRow arg="ospf.type" typ="enum (intra | inter | ext-type-1 | ext-type-2 | nssa-type-1 | nssa-type-2)"></ArgTableRow>
<ArgTableRow arg="isis.type" typ="enum (l1 | l2 | l1-inter | l1-ext | l2-ext | l1-inter-ext)"></ArgTableRow>
<ArgTableRow arg="isis.metric" typ="num"></ArgTableRow>
<ArgTableRow arg="mpls.labels" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="mpls.in-label" typ="num">映射的 MPLS 入站标签。</ArgTableRow>
<ArgTableRow arg="mpls.out-label" typ="num">映射的 MPLS 出站标签。</ArgTableRow>
<ArgTableRow arg="ldp.peer-id" typ="num"></ArgTableRow>
<ArgTableRow arg="ldp.label" typ="num">LDP 映射的 MPLS 标签。</ArgTableRow>
<ArgTableRow arg="mtu" typ="num"></ArgTableRow>
<ArgTableRow arg="hoplimit" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.fwp-ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.route-ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.refs" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.size" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.input.raw" typ="string"></ArgTableRow>
<ArgTableRow arg="debug.merge.refs" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.size" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.ptr" typ="num"></ArgTableRow>
<ArgTableRow arg="debug.merge.raw" typ="string"></ArgTableRow>
</ArgTable>

### routing/route/rule

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">非活动</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src-address" typ="address (flags=4iv/)" unset="1"></ArgTableRow>
<ArgTableRow arg="dst-address" typ="address (flags=4iv/)" unset="1"></ArgTableRow>
<ArgTableRow arg="routing-mark" typ="enum" unset="1"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" unset="1"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (lookup | lookup-only-in-table | unreachable | drop)"></ArgTableRow>
<ArgTableRow arg="table" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="min-prefix" typ="num" unset="1"></ArgTableRow>
</ArgTable>