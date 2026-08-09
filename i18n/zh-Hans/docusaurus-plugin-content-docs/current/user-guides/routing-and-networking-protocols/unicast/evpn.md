# EVPN

> 本页介绍用于二层和三层VPN服务的EVPN技术，详细说明BGP控制平面、MPLS/VXLAN封装以及EVPN路由类型（Type-1至Type-5）。文中解释了NVO术语，如NVE、VNI和MAC-VRF，描述了通过入口复制处理BUM流量，并概述了对称/非对称IRB。

# EVPN

以太网虚拟专用网络（EVPN）是一种在不同网络分段之间扩展二层和三层连接的技术。MPLS或VXLAN封装通过基于MPLS或IP的网络传输以太网帧。

BGP EVPN用作多种数据平面封装（包括二层和三层VPN服务）的控制平面。MP-BGP承载MAC地址、MAC/IP绑定和IP前缀。

RFC7432是初始EVPN标准，定义了BGP作为MPLS数据平面的控制平面。RFC8365扩展了对额外数据平面（VXLAN、NVGRE和MPLS over GRE）的支持，并将EVPN定义为网络虚拟化覆盖（NVO）。

## 术语

- NVO：网络虚拟化覆盖，用于提供二层和三层VPN服务。
- NVE：网络虚拟化端点，是NVO环境中的提供商边缘（PE）节点。负责VPN流量的封装/解封装。在VXLAN情况下，这定义了VTEP（虚拟隧道端点）。
- VNI：虚拟网络标识符
- EVI：EVPN实例
- RD：[路由区分符](../route-distinguisher-and-route-target.md#route-distinguisher)是附加到IP前缀以使其唯一化的64位前缀，多个租户可以使用重叠的IP范围。
- RT：[路由目标](../route-distinguisher-and-route-target.md#route-targets)是BGP扩展团体属性，用于控制路由的导入和导出。通常，RT基于AS号和MAC-VRF的VNI。
- MAC-VRF：PE（VTEP）上用于MAC地址的[VRF](../vrf.md)表。需要RD和RT。
- BUM：广播、未知单播和组播流量是VXLAN网络中的多目的地二层流量。
- 入口复制：处理BUM流量的单播方法。使用IMET路由自动发现远端对等体。入口设备将BUM流量复制到与二层VNI关联的所有VTEP。
- ESI - 以太网分段标识符

为使MP-BGP承载EVPN，定义了新的AFI/SAFI 25（L2 VPN）/70（EVPN）。NLRI中的下一跳地址是通告EVPN路由的VTEP的IP地址。

共有五种EVPN路由类型：

- Type‑1：（以太网A‑D）通告多归属以太网分段的可达性。
- Type‑2：（MAC通告 / MACIP）通告由特定EVI学习到的MAC/IP绑定的MAC地址。
- Type‑3：（包含性组播IMET）通告二层域的成员资格，允许自动发现VTEP。
- Type‑4：（以太网分段）用于发现连接到同一共享以太网分段的VTEP，用于EVPN多归属模型（active‑active或active‑standby转发）。
- Type‑5：（IP前缀）将IP前缀通告到EVPN域中，允许创建经典三层VPN（参见[`/routing/bgp/vpn`](../../../cli-reference/routing/bgp.md#routingbgpvpn)）。

数据平面封装通过封装扩展团体属性值定义：

- 8 - VXLAN（目前ROS仅支持此封装）
- 9 - NVGRE
- 10 - MPLS
- 11 - MPLSoGRE

有两种方法支持EVPN的子网间路由：对称和非对称集成路由与桥接（IRB）。两种方法的主要区别在于，对称方法在入口和出口VTEP上都支持路由和桥接，而非对称方法仅在入口支持路由，出口仅支持桥接。对称IRB需要为L3VNI配置[VRF](../vrf.md)实例。

## 路由列表

RouterOS将在[`/routing/route`](../../../cli-reference/routing/route.md)列表中显示本地和接收到的EVPN路由。

本地生成的路由将具有**e-evpn**标志。例如：

```routeros
[admin@ros_leaf_3] /routing/route> print where evpn
Flags: e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
  DST-ADDRESS                                     GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE
e [10.155.101.133:1010]macip:0|0C:50:85:84:00:01  203.0.255.133  evpn       200     40            10
e [10.155.101.133:1010]imet:0|203.0.255.133       203.0.255.133  evpn       200     40            10
e [203.0.255.133:4]imet:0|203.0.255.133           203.0.255.133  evpn       200     40            10

```

EVPN数据编码在`dst-address`参数中：

```
    Dst [rd]type:x|y
         ^  ^    ^
         |  |    + - 其中 x - tag或ESI；y - 类型特定数据（可显示MAC地址、IP地址、以太网分段等）
         |  +------- EVPN路由类型名称（macip、imet、es、ad、prefix）
         +---------- 方括号中的路由区分符

```

## 配置示例

### 基本配置示例

基本二层EVPN VXLAN配置：

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes pvid=40
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=40

/ip/address
add address=203.0.113.1 interface=lo

/interface/vxlan
add bridge=bridge1 bridge-pvid=40 local-address=203.0.113.1 name=vxlan1 vni=100040 learning=no

/routing/bgp/instance
add as=65000 name=evpn-inst

/routing/bgp/connection
add afi=evpn instance=evpn-inst local.address=203.0.113.1 .role=ebgp multihop=yes name=to-leaf-lo remote.address=203.0.113.2 .as=65001

/routing/bgp/evpn
add instance=evpn-inst name=bgp-evpn-1o vni=100040
```

对于仅有一个VNI的简单设置，无需设置路由区分符或[`import.route-targets`](../../../cli-reference/routing/bgp.md#import.route-targets)/[`export.route-targets`](../../../cli-reference/routing/bgp.md#export.route-targets)。

:::info
当未指定[RT](../route-distinguisher-and-route-target.md#route-targets)或[RD](../route-distinguisher-and-route-target.md#route-distinguisher)时，将自动派生值。路由目标设置为`<PE ASN>:<VNI>`，路由区分符设置为`<PE地址>:<从配置ID派生的数字>`。
:::

EVPN配置直接映射到具有匹配VNI的VXLAN配置。

### 与Arista EOS和ROS的桥接EVPN VXLAN覆盖

#### 拓扑

对于此示例，我们将使用以下拓扑：

![](img/evpn_eos_ros.jpg#gh-light-mode-only)
![](img/evpn_eos_ros_dark.png#gh-dark-mode-only)

- 203.0.255.0/24地址范围用于环回地址
- 172.16.0.0/16范围内的子网用于leaf和spine路由器的underlay连接
- 192.168.0.0/16范围内的子网用于VLAN上的主机寻址。

#### Underlay配置

Underlay连接取决于现有网络；可以使用eBGP、[OSPF](./ospf/areas-and-virtual-links.md)、ISIS，甚至静态路由。在此示例中，我们使用OSPF作为underlay路由协议来通告环回接口地址的路由。

**Ros\_Spine**

```routeros
/ip/address
add address=203.0.255.138 interface=lo
add address=172.16.1.1/30 interface=ether3
add address=172.16.2.1/30 interface=ether4
add address=172.16.3.1/30 interface=ether5
add address=172.16.4.1/30 interface=ether6
add address=172.16.5.1/30 interface=ether7

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Ros\_Leaf\_3**

```routeros
/ip/address
add address=203.0.255.133 interface=lo
add address=172.16.3.2/30 interface=ether10

/routing/ospf/instance
add name=evpn_underlay
/routing/ospf/area
add disabled=no instance=evpn_underlay name=evpn-underlay-bb
/routing/ospf/interface-template
add area=evpn-underlay-bb disabled=no networks=172.16.0.0/16
add area=evpn-underlay-bb disabled=no interfaces=lo passive
```

**Eos\_Leaf**

```
interface Ethernet1
   no switchport
   ip address 172.16.5.2/30
!
interface Loopback0
   ip address 203.0.255.128/32
!
ip routing
!
router ospf 100
   router-id 203.0.255.135
   redistribute connected
   network 172.16.1.0/30 area 0.0.0.0
!

```

#### BGP EVPN覆盖

对于[BGP](./bgp/understanding-bgp.md)覆盖，我们使用带有环回地址的[`multihop`](../../../cli-reference/routing/bgp.md#multihop) eBGP。

为简化配置，使用BGP [`/routing/bgp/template`](../../../cli-reference/routing/bgp.md#routingbgptemplate)设置公共参数，并配置[`/routing/bgp/connection`](../../../cli-reference/routing/bgp.md#routingbgpconnection)监听整个环回地址范围。这种方法具有良好的可扩展性：添加更多leaf路由器时无需更改spine路由器上的配置。

此外，建议设置[`nexthop-choice`](../../../cli-reference/routing/bgp.md)进行传播，尤其是在有多个spine的情况下。如果使用iBGP作为覆盖，则spine应为路由反射器，并且默认进行下一跳传播。

**Ros\_Spine** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp.md#routingbgpinstance)

```routeros
/routing/bgp/instance
add as=65000 name=bgp-instance-1
/routing/bgp/template
set default afi=evpn multihop=yes nexthop-choice=propagate
/routing/bgp/connection
add instance=bgp-instance-1 local.address=203.0.255.138 .role=ebgp name=evpn_leafs remote.address=\
    203.0.255.0/24 templates=default
```

**Ros\_Leaf\_3** — [`/routing/bgp/instance`](../../../cli-reference/routing/bgp.md#routingbgpinstance), [`/routing/bgp/connection`](../../../cli-reference/routing/bgp.md#routingbgpconnection)

```routeros
/routing/bgp/instance
add as=65003 disabled=no name=bgp-instance-1
/routing/bgp/connection
add afi=evpn instance=bgp-instance-1 local.address=203.0.255.133 .role=ebgp multihop=yes name=to_spine remote.address=\
    203.0.255.138
```

**Eos\_Leaf**

```
service routing protocols model multi-agent
!
router bgp 65005
   neighbor SPINE_EVPN peer group
   neighbor SPINE_EVPN remote-as 65000
   neighbor SPINE_EVPN update-source Loopback0
   neighbor SPINE_EVPN ebgp-multihop 10
   neighbor SPINE_EVPN send-community extended
   neighbor 203.0.255.138 peer group SPINE_EVPN
   !
   address-family evpn
      neighbor SPINE_EVPN activate
!
```

##### 验证BGP连接

检查[`/routing/bgp/session`](../../../cli-reference/routing/bgp.md#routingbgpsession)以验证BGP对等状态。

**Eos\_Leaf**

```
localhost#show bgp summary
BGP summary information for VRF default
Router identifier 203.0.255.128, local AS number 65005
Neighbor               AS Session State AFI/SAFI                AFI/SAFI State   NLRI Rcd   NLRI Acc
------------- ----------- ------------- ----------------------- -------------- ---------- ----------
203.0.255.138       65000 Established   IPv4 Unicast            Advertised              0          0
203.0.255.138       65000 Established   L2VPN EVPN              Negotiated              6          6
```

**Ros\_Leaf\_3**

```routeros
[admin@ros_leaf_3] /routing/bgp/session> print
Flags: E - established
 0 E name="to_spine-1" instance=bgp-instance-1
     remote.address=203.0.255.138 .as=65000 .id=203.0.255.138 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7 .bytes=682 .eor=""
     local.address=203.0.255.133 .as=65003 .id=203.0.255.133 .cluster-id=203.0.255.133 .capabilities=mp,rr,gr,as4 .afi=evpn .messages=7
     .bytes=698 .eor=""
     output.procid=20
     input.procid=20 ebgp
     multihop=yes hold-time=3m keepalive-time=1m uptime=1s620ms last-started=2025-05-29 11:01:38 prefix-count=0
```

#### VXLAN和EVPN配置

**Ros\_Leaf\_3**

仅用于演示目的，在RouterOS leaf上，我们将向主机发送带VLAN标签的流量。

应禁用VXLAN学习，因为我们使用[BGP EVPN](../../../cli-reference/routing/bgp.md#routingbgpevpn)进行发现。EVPN配置在[`/routing/bgp/evpn`](../../../cli-reference/routing/bgp.md#routingbgpevpn)菜单下完成。

```routeros
/interface/bridge
add name=bridge1 pvid=10 vlan-filtering=yes
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 learning=no local-address=203.0.255.133 mac-address=C2:16:F6:B2:CC:D3 name=vxlan1 vni=1010
/interface/bridge/port
add bridge=bridge1 interface=ether11 pvid=10
/ip/address
add address=192.168.10.133/24 interface=bridge1
/routing/bgp/evpn
add disabled=no export.route-targets=1010:1010 import.route-targets=1010:1010 instance=bgp-instance-1 name=bgp-evpn-1 vni=1010
```

**Eos\_Leaf**

在Arista路由器上，我们设置VLAN trunk，未标记的流量将发送到主机。

```
vlan 10
!
interface Ethernet2
   switchport trunk allowed vlan 10
   switchport mode trunk
!
interface Vlan10
   ip address 192.168.10.128/24
!
interface Vxlan1
   vxlan source-interface Loopback0
   vxlan vlan 10 vni 1010
!
router bgp 65501
   vlan 10
      rd 203.0.255.128:1010
      route-target both 1010:1010
      redistribute learned
```

**Host\_1**

```routeros
/ip/address
add address=192.168.10.132/24 interface=ether2
```

**Host\_3**

```routeros
/interface/vlan
add interface=ether2 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.129/24 interface=vlan10
```

#### 验证L2VPN服务

让我们验证leaf路由器上是否存在**IMET**路由，以及**VTEP**是否已被发现。

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"imet"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                               GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]imet:0|203.0.255.128  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]imet:0|203.0.255.133   203.0.255.133  evpn       200     40            10

[admin@ros_leaf_3] /interface/vxlan/vteps> print
Flags: D - DYNAMIC
Columns: INTERFACE, REMOTE-IP
#   INTERFACE  REMOTE-IP
0 D vxlan1     203.0.255.128
```

在Arista上：

```
localhost#show bgp evpn route-type imet
BGP routing table information for VRF default
Router identifier 203.0.255.135, local AS number 65501
Route status codes: * - valid, > - active, S - Stale, E - ECMP head, e - ECMP
                    c - Contributing to ECMP, % - Pending BGP convergence
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

          Network                Next Hop              Metric  LocPref Weight  Path
 * >      RD: 203.0.255.128:1010 imet 203.0.255.128
                                 -                     -       -       0       i
 * >      RD: 203.0.255.133:256 imet 203.0.255.133
                                 203.0.255.133         -       100     0       65000 65003 i

localhost#show interfaces vxlan1
Vxlan1 is up, line protocol is up (connected)
  Hardware is Vxlan
  Source interface is Loopback0 and is active with 203.0.255.128
  Listening on UDP port 4789
  Replication/Flood Mode is headend with Flood List Source: EVPN
  Remote MAC learning via EVPN
  VNI mapping to VLANs
  Static VLAN to VNI mapping is
    [10, 1010]
  Note: All Dynamic VLANs used by VCS are internal VLANs.
        Use 'show vxlan vni' for details.
  Static VRF to VNI mapping is not configured
  Headend replication flood vtep list is:
    10 203.0.255.133
  Shared Router MAC is 0000.0000.0000

localhost#show vxlan flood vtep vlan 10
          VXLAN Flood VTEP Table
--------------------------------------------------------------------------------

VLANS                            Ip Address
-----------------------------   ------------------------------------------------
10                              203.0.255.133

```

此时，我们可以尝试从**host\_1** ping **host\_3**：

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:50:85:84:00:01

[admin@host_1] /ip/address> /ping 192.168.10.129
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.129                             56  64 17ms26us
    1 192.168.10.129                             56  64 13ms119us
    2 192.168.10.129                             56  64 17ms192us
```

**host-3**

```routeros
[admin@host_1] /interface> print
...
1 R ether2  ether           1500  0C:74:39:88:00:01
```

现在，通过查看MACIP路由，我们应该能够看到EVPN用于学习远端MAC地址。

如果我们查看**ros\_leaf**上的路由，可以看到路由器203.0.255.128发送了MAC地址为0C:74:39:88:00:01的macip路由，该MAC地址是位于**eos\_leaf**后面的**host\_1**的MAC地址。

Eos还发送用于arp/nd抑制的MAC/IP绑定。遗憾的是，在撰写本文时，RouterOS尚不具备此功能。

```routeros
[admin@ros_leaf_3] /routing/route> print where dst-address~"macip"
Flags: A - ACTIVE; b - BGP, e - EVPN
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS                                                   GATEWAY        AFI   DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01                 203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
 e [203.0.255.133:256]macip:0|0C:50:85:84:00:01                  203.0.255.133  evpn       200     40            10
Ab [203.0.255.128:1010]macip:0|0C:74:39:88:00:01|192.168.10.129  203.0.255.128  evpn        20     40            30  172.16.3.1%ether10
```

Arista还允许额外查看"vxlan mac table"中远程学习的MAC地址，而"vlan mac-address table"则同时包含本地MAC地址：

```
localhost#show bgp evpn route-type mac-ip detail
BGP routing table information for VRF default
Router identifier 203.0.255.128, local AS number 65005
BGP routing table entry for mac-ip 0c50.8584.0001, Route Distinguisher: 203.0.255.133:256
 Paths: 1 available
  65000 65003
    203.0.255.133 from 203.0.255.138 (203.0.255.138)
      Origin IGP, metric -, localpref 100, weight 0, tag 0, valid, external, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 0 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000
BGP routing table entry for mac-ip 0c74.3988.0001 192.168.10.129, Route Distinguisher: 203.0.255.128:1010
 Paths: 1 available
  Local
    - from - (0.0.0.0)
      Origin IGP, metric -, localpref -, weight 0, tag 0, valid, local, best
      Extended Community: Route-Target-AS:1010:1010 TunnelEncap:tunnelTypeVxlan
      VNI: 1010 ESI: 0000:0000:0000:0000:0000

localhost#show vxlan address-table vlan 10
          Vxlan Mac Address Table
----------------------------------------------------------------------

VLAN  Mac Address     Type      Prt  VTEP             Moves   Last Move
----  -----------     ----      ---  ----             -----   ---------
  10  0c50.8584.0001  EVPN      Vx1  203.0.255.133    1       1:30:49 ago
Total Remote Mac Addresses for this criterion: 1

localhost#show mac address-table vlan 10
          Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports      Moves   Last Move
----    -----------       ----        -----      -----   ---------
  10    0c50.8584.0001    DYNAMIC     Vx1        1       1:31:17 ago
  10    0c74.3988.0001    DYNAMIC     Et2        1       1 day, 23:45:18 ago
Total Mac Addresses for this criterion: 2

          Multicast Mac Address Table
------------------------------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       ----        -----
Total Mac Addresses for this criterion: 0
```

### 使用Arista ESI LAG的桥接EVPN覆盖

**ESI-LAG**（以太网分段标识符 - 链路聚合）或**EVPN-LAG**是一种网络概念，使用**EVPN**（以太网虚拟专用网络）技术实现多归属，其中客户端设备（如接入交换机）可以通过多条链路连接到核心设备（如分布交换机），形成逻辑**LAG**接口。

#### 拓扑

让我们扩展上一个示例中的拓扑。**Host\_2**是启用了**LACP**的RouterOS设备，连接到两个Arista leaf，形成active‑active多归属设置。

![](img/evpn_eos_ros_2.jpg#gh-light-mode-only)
![](img/evpn_eos_ros_2_dark.png#gh-dark-mode-only)

#### 配置前提

有关设置underlay和EVPN覆盖的详细信息，请参阅上面的示例。本节重点介绍ESI LAG配置和验证。

#### 端口通道配置

假设underlay和overlay已配置并运行，继续在Arista交换机上进行端口通道配置：

**leaf\_2**和**leaf\_4**的配置完全相同

```
interface Port-Channel3
   switchport access vlan 10
   switchport trunk allowed vlan 10
   switchport mode trunk
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0333:3333
      route-target import 00:00:03:33:33:33
   lacp system-id 0000.0333.3333
!
interface Ethernet2
   channel-group 3 mode active
```

**ros\_host\_2**

```routeros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether2,ether3
/interface/vlan
add interface=bond1 mtu=1496 name=vlan10 vlan-id=10
/ip/address
add address=192.168.10.130/24 interface=vlan10
```

#### 验证设置

现在，如果我们查看EVPN路由，应该会看到一些新的路由类型。两台Arista交换机都在通告Type-1 AD路由和Type-4以太网分段（ES）路由，以发现多归属VTEP。

```routeros
[admin@gns3_spine1_ros] /routing/route>  print where afi=evpn dst-address~"(ad|es)"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.127:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.127  203.0.255.127  evpn        20     40  30
Ab [203.0.255.127:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.127  evpn        20     40  30

Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

```

如果我们检查两台Eos leaf，将看到指定转发器203.0.255.127（**eos\_leaf\_4**）被选中：

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.127
      Non-Designated forwarder: 203.0.255.134

```

让我们挂起从**host2**到**eos\_leaf\_4**的链路并观察结果：

```
eos_leaf_2#show bgp evpn instance vlan 10
EVPN instance: VLAN 10
  Route distinguisher: 203.0.255.134:1010
  Route target import: Route-Target-AS:1010:1010
  Route target export: Route-Target-AS:1010:1010
  Service interface: VLAN-based
  Local VXLAN IP address: 203.0.255.134
  VXLAN: enabled
  MPLS: disabled
  Local ethernet segment:
    ESI: 0000:0000:0000:0333:3333
      Type: 0 (administratively configured)
      Interface: Port-Channel3
      Mode: all-active
      State: up
      ES-Import RT: 00:00:03:33:33:33
      DF election algorithm: modulus
      Designated forwarder: 203.0.255.134

[admin@spine1_ros] /routing/route>  print interval=1 where dst-address~"ad|es"
Flags: A - ACTIVE; b - BGP
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE
   DST-ADDRESS                                                      GATEWAY        AFI   DISTANCE  SCOPE  TA
Ab [203.0.255.134:1]ad:4294967295|00:00:00:00:00:00:03:33:33:33     203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1]es:00:00:00:00:00:00:03:33:33:33|203.0.255.134  203.0.255.134  evpn        20     40  30
Ab [203.0.255.134:1010]ad:0|00:00:00:00:00:00:03:33:33:33           203.0.255.134  evpn        20     40  30

[admin@host_2] /interface/bonding> /ping 192.168.10.132 interval=500ms
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.132                             56  64 2ms90us
    1 192.168.10.132                             56  64 2ms172us
    2 192.168.10.132                             56  64 2ms503us
    3 192.168.10.132                                               timeout
    4 192.168.10.132                                               timeout
    5 192.168.10.132                                               timeout
    6 192.168.10.132                             56  64 2ms191us
    7 192.168.10.132                             56  64 2ms31us
```

**eos\_leaf\_2**成为转发器，**eos\_leaf\_4**撤销了ES和AD路由，流量切换到另一条LACP链路。