# VXLAN

> 本文档介绍 MikroTik RouterOS 的 VXLAN 实现，涵盖其在扩展 VLAN ID 方面的用途、VXLAN 接口和 VTEP 的配置选项，以及转发表监控。文中详细说明了 MTU、VNI、ARP 处理和多播组管理等设置，用于在 UDP 之上构建 Layer 2 覆盖网络。

# VXLAN

---

虚拟可扩展局域网（VXLAN）是一种隧道协议，旨在解决 IEEE 802.1Q 中 VLAN ID 数量有限（4096）的问题，该协议由 IETF RFC 7348 定义。通过 VXLAN，标识符的大小扩展至 24 位（16777216）。它在 Layer 3 网络上创建了 Layer 2 覆盖方案，并且该协议运行在 UDP 之上。RouterOS VXLAN 接口支持 IPv4 或 IPv6（自版本 7.6 起），但不支持双栈。

:::info
VXLAN 为 IPv4 增加 50 字节开销，为 IPv6 增加 70 字节开销。配置 VXLAN 时，建议通过相应配置 MTU 或限制以太网帧大小，确保封装后的以太网帧大小不超过底层网络的 MTU。
:::

只有同一 VXLAN 网段内的设备才能相互通信。每个 VXLAN 网段通过一个 24 位的网段 ID 来标识，称为 VXLAN 网络标识符（VNI）。与大多数隧道不同，VXLAN 是 1 对 N 的网络，而不仅仅是点对点。终止 VXLAN 隧道的端点称为 VXLAN 隧道端点（VTEP）。RouterOS 仅支持静态配置的远程 VTEP。当需要通过 VXLAN 发送单播流量时，设备可以类似于学习型网桥的方式动态学习其他端点的 IP 地址，并仅将流量转发到必要的 VTEP。对于需要泛洪（广播、未知单播和多播）到同一网段上所有 VTEP 的流量，VXLAN 可以使用多播或带头部复制（head-end replication）的单播，为每个远程 VTEP 发送一个副本。

## 配置选项

---

本节介绍 VXLAN 接口和 VTEP 的配置选项。

**子菜单：** `/interface/vxlan`

| 属性 | 描述 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*；默认值：**yes**) | 是否允许 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 处理。VXLAN 上的分片和泛洪数据包通过慢速路径重定向。对于使用 VRF 的 VXLAN 接口，Fast Path 被禁用。此设置自 RouterOS 版本 7.8 起可用。 |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*；默认值：**enabled**) | 地址解析协议设置。<code>disabled</code> - 接口将不使用 ARP<code>enabled</code> - 接口将使用 ARP<code>local-proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到同一接口<code>proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到其他接口<code>reply-only</code> - 接口将仅回复来自 IP/ARP 表中静态条目中匹配的 IP 地址/MAC 地址组合的请求。不会自动在 IP/ARP 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-timeout** (*auto \| integer*；默认值：**auto**) | 在从 IP 地址未收到数据包后，ARP 记录在 ARP 表中保留的时间。值 `auto` 等于 IP/Settings 中 `arp-timeout` 的值，默认为 30 秒。 |
| **bridge** (*name*；默认值：) | VXLAN 接口将作为从属端口添加到的 [bridge](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) 接口名称。 |
| **bridge-pvid** (*integer 1..4094;* 默认值：**1**) | 用于为动态桥接端口分配 PVID 参数。此属性仅在 bridge vlan-filtering 设置为 yes 时生效。 |
| **checksum**(*yes \| no*；默认值：**no**) | 该设置控制是否在传输的外部 VXLAN 数据包中计算 UDP 校验和：<code>no</code> - 在传输的外部数据包中，UDP 校验和设置为零。这也允许接收通过 IPv6 传输且 UDP 校验和为零的 VXLAN 数据包。<code>yes</code> - 在传输的外部数据包中计算 UDP 校验和。如果使用硬件卸载进行数据包传输，则忽略此设置，行为默认为发送 UDP 校验和为零的数据包。 |
| **comment** (*string*；默认值：) | 接口的简短描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 更改接口是否禁用。 |
| **dont-fragment**(*auto \| disabled \| enabled \| inherit*；默认值：**auto**) | 不分片（DF）标志控制数据包在通过网络发送前是否可以被分解成更小的数据包（称为分片）。配置 VXLAN 时，此设置决定外部 IPv4 报头上 DF 标志的存在，并可在封装数据包超过出接口 MTU 时控制数据包分片。此设置有三个选项：<code>auto</code> - 如果设备支持 VXLAN 卸载，dont-fragment 模式将作为 <code>enabled</code> 运行。如果不支持 VXLAN 卸载，它将使用 <code>inherit</code> 模式。<code>disabled</code> - 外部 IPv4 报头不设置 DF 标志，这意味着如果数据包太大而无法通过出接口发送，则可以进行分片。这也允许在 VXLAN 使用 IPv6 底层网络时进行数据包分片。在兼容设备上禁用硬件卸载。<code>enabled</code> - 外部 IPv4 报头始终设置 DF 标志，这意味着数据包不会被分片，如果超过出接口的 MTU，将被丢弃。这也避免了 VXLAN 使用 IPv6 底层网络时的数据包分片。<code>inherit</code> - 外部 IPv4 报头上的 DF 标志基于内部 IPv4 DF 标志。如果内部 IPv4 报头设置了 DF 标志，则外部 IPv4 报头也将设置它。如果数据包超过出接口的 MTU 且设置了 DF，它将被丢弃。如果内部数据包是非 IP 数据包，则外部 IPv4 报头不会设置 DF 标志，数据包可以被分片。如果内部数据包是 IPv6，则外部 IPv4 报头将始终设置 DF 标志，数据包不能被分片。请注意，当 VXLAN 使用 IPv6 底层网络时，此设置没有任何效果，并被视为与 <code>disabled</code> 相同。此设置自 RouterOS 版本 7.8 起可用。 |
| **group** (*IPv4 \| IPv6*；默认值：) | 指定后，可以使用多播组地址在 VTEP 之间转发广播、未知单播和多播流量。此属性需要指定 `interface` 设置。接口将使用 IGMP 或 MLD 加入指定的多播组，确保添加必要的 PIM 和 IGMP/MLD 配置。设置此属性时，`vteps-ip-version` 会自动更新为所使用的多播 IP 版本。在兼容设备上禁用硬件卸载。 |
| **hw** (*yes \| no*；默认值：**yes**) | 允许禁用硬件卸载，仅适用于支持 VXLAN 卸载的设备。 |
| **interface** (*name*；默认值：) | 用于多播转发的接口名称。此属性需要指定 `group` 设置。在兼容设备上禁用硬件卸载。 |
| **learning**(*yes \| no*；默认值：**yes**) | 该设置控制是否从接收到的数据包中动态学习内部源 MAC 地址和远程 VTEP IP/IPv6 地址。 |
| **local-address** (*IPv4 \| IPv6*；默认值：) | 指定 VXLAN 接口的本地源地址。如果未设置，将选择出接口的一个 IP 地址作为 VXLAN 数据包的源地址。设置此属性时，`vteps-ip-version` 会自动更新为所使用的本地 IP 版本。此设置自 RouterOS 版本 7.7 起可用。 |
| **mac-address** (*MAC*；默认值：) | 接口的静态 MAC 地址。未指定时，将分配一个随机生成的 MAC 地址。 |
| **max-fdb-size** (*integer: 1*..65535**；默认值：**4096**) | 限制 VXLAN 可以在转发表（FDB）中存储的最大 MAC 地址数量。 |
| **mtu** (*integer*；默认值：**1500**) | 对于最大传输单元，VXLAN 接口默认将 MTU 设置为 1500。`l2mtu` 将根据关联的 `interface` 自动设置（减去对应于 VXLAN 报头的 50 字节）。如果未指定接口，则使用 `l2mtu` 值 65535。`l2mtu` 不能更改。 |
| **name** (*text*；默认值：**vxlan1**) | 接口名称。 |
| **port** (*integer: 1*..65535**；默认值：**4789**) | 用于监听和向远程 VTEP 发送数据包的 UDP 端口号。 |
| **rem-csum** (*both \| none \| rx \| tx*；默认值：**none**) | 更改 VXLAN 接口的远程校验和卸载（RCO）设置。RCO 是一种省略封装数据报内部校验和的技术，允许网络驱动程序卸载外部校验和。但是，它涉及对封装协议的更改，接收方也必须支持。因此，默认情况下它是禁用的，此设置可用于确保与依赖此功能的系统的兼容性。RCO 在以下 Internet-Drafts 中有详细说明：  Remote checksum offload for VXLAN, draft-herbert-vxlan-rco-00. Remote checksum offload for encapsulation, draft-herbert-remotecsumoffload-00.  如果使用 [hardware offloading](./vxlan.md#hardware-offloaded-vxlan)，则忽略此设置，行为默认为 none。 |
| **ttl** (*auto \| integer: 0*..255**；默认值：**auto**) | 指定出站数据包中使用的 TTL 值。默认情况下，使用 `auto` 选项时 TTL 设置为 64。但是，如果 VXLAN 使用多播底层网络，则默认 TTL 设置为 1。如果多播网络涉及路由，则需要将 TTL 增加到更高的值。 |
| **vni** (*integer: 1..16777215*；默认值：) | VXLAN 网络标识符（VNI）。 |
| **vtep-vrf** (*name*；默认值：**main**) | 为 VXLAN 接口设置 VRF，VTEP 在该 VRF 上监听和建立连接。使用 `interface` 和多播 `group` 设置时不支持 VRF。同一 UDP `port` 不能同时在多个路由表中使用。当使用未设置为“main”的 VRF 时，在兼容设备上禁用硬件卸载。此设置自 RouterOS 版本 7.7 起可用。 |
| **vteps-ip-version** (*ipv4 \| ipv6*；默认值：**ipv4**) | 用于静态配置的 VTEP 的 IP 协议版本。RouterOS VXLAN 接口不支持双栈，任何配置了相反 IP 版本的远程 VTEP 将被忽略。当设置多播 `group` 或 `local-address` 属性时，`vteps-ip-version` 会自动更新为所使用的 IP 版本。使用 IPv6 会在兼容设备上禁用硬件卸载。此设置自 RouterOS 版本 7.6 起可用。 |

**子菜单：** `/interface/vxlan/vteps`

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*string*；默认值：) | 已配置 VTEP 的简短描述。 |
| **interface** (*name*；默认值：) | VXLAN 接口名称。 |
| **remote-ip** (*IPv4 \| IPv6*；默认值：) | 定义 VTEP 端点 IPv4 或 IPv6 地址，当 VXLAN 接口需要发送 BUM（广播、未知单播、多播）流量时使用。它不用作访问控制。 |

## 转发表

---

自 RouterOS 版本 7.9 起，可以监控从远程 VTEP 学习到的 MAC 地址。

**子菜单：** `/interface/vxlan/fdb`

| 属性 | 描述 |
| :-- | :-- |
| **interface** (*只读：*name**) | VXLAN 接口名称。 |
| **mac-address** (*只读：MAC 地址*) | MAC 地址。 |
| **remote-ip** (*只读：IPv4 \| IPv6 地址*) | 远程 VTEP 的 IPv4 或 IPv6 目的地址。 |

```ros
[admin@MikroTik] > /interface/vxlan/fdb/print          
 0 remote-ip=2001::2 mac-address=56:FF:AA:1A:72:33 interface=vxlan1 

 1 remote-ip=2002::2 mac-address=AE:EC:C4:12:8B:B9 interface=vxlan1 

 2 remote-ip=192.168.10.20 mac-address=FE:AF:58:31:A7:B6 interface=vxlan2
```

## 配置示例

---

此配置示例在两个静态配置的 VTEP 端点之间创建单个 VXLAN 隧道。

首先，在两台路由器上创建 VXLAN 接口。

```ros
/interface/vxlan
add name=vxlan1 port=4789 vni=10
```

然后，在两台路由器上配置具有相应 IPv4 目的地址的 VTEP。两台设备都应具有指向目的地址的活动路由。

```ros
# Router1
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.10.10

# Router2
/interface/vxlan/vteps
add interface=vxlan1 remote-ip=192.168.20.20
```

配置完成。可以将 VXLAN 接口与其他以太网接口一起加入 bridge。

## 硬件卸载的 VXLAN

---

从 RouterOS 版本 7.18 开始，引入了对硬件卸载 VXLAN 的初步支持。这使得卸载的 VXLAN 数据平面成为可能，支持封装和解封装，并允许在 vlan-filtering bridge 内进行静态的一对一 VLAN 到 VXLAN 映射。有关兼容设备列表，请参阅 [L3HW Device Support](./l3-hardware-offloading.md#l3hw-device-support) 文档。

目前，一些已知功能尚未实现。

### 底层网络（路由封装后的 VXLAN 数据包）

1. 不支持通过 ECMP 使用 VTEP。

2. 不支持通过 bond、bridge、VLAN 接口使用 VTEP（仅支持独立的路由以太网接口）。

3. 不支持通过多播使用 VTEP。

4. VTEP 不能在 VRF 内运行。

5. 不支持 IPv6 的 VTEP。

### 覆盖网络（以太网和 VXLAN 之间的转发）

1. 不支持在不同 VXLAN VNI 之间进行路由。

2. VTEP 是隔离的，没有机制来控制它们之间的“水平分割”。

3. 桥接的 VXLAN 接口不支持 IGMP 侦听。启用侦听时，VXLAN 上的 MDB 条目不会被卸载，并且多播流量在以太网和 VXLAN 之间会受到限制。

4. MLAG 不支持桥接的 VXLAN 接口。

### 基本配置示例

在此示例中，使用静态路由来访问远程 VTEP，但也可以使用 OSPF 或 BGP 等动态路由协议。上行接口具有更高的 MTU 以支持大数据包和 VXLAN 封装。以下是网络拓扑概述：

**sfp-sfpplus1** - 上行（底层）接口  
**sfp-sfpplus3** - 用于未标记 VLAN 10 的桥接端口  
**sfp-sfpplus4** - 用于未标记 VLAN 20 的桥接端口  
**vxlan-10010** - 用于未标记 VLAN 10 的覆盖端口  
**vxlan-10020** - 用于未标记 VLAN 20 的覆盖端口

```routeros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] l2mtu=9500 mtu=9500
/interface/vxlan
add bridge=bridge1 bridge-pvid=10 local-address=192.168.1.1 name=vxlan-10010 vni=10010
add bridge=bridge1 bridge-pvid=20 local-address=192.168.1.1 name=vxlan-10020 vni=10020
/interface/bridge/port
add bridge=bridge1 interface=sfp-sfpplus3 pvid=10
add bridge=bridge1 interface=sfp-sfpplus4 pvid=20
/interface/vxlan/vteps
add interface=vxlan-10010 remote-ip=192.168.1.2
add interface=vxlan-10020 remote-ip=192.168.1.2
/ip/address
add address=192.168.1.1 interface=lo network=192.168.1.1
add address=192.168.10.10/24 interface=sfp-sfpplus1 network=192.168.10.0
/ip/route
add dst-address=192.168.1.2 gateway=192.168.10.20
/interface/ethernet/switch
set 0 l3-hw-offloading=yes
```