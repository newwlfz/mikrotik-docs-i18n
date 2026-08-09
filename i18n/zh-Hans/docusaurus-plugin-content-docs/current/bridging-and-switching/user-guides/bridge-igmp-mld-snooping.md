# Bridge IGMP/MLD Snooping

> 本文档介绍 MikroTik RouterOS 桥接功能中的 IGMP/MLD Snooping，通过将组播流过滤到已订阅的端口，实现高效的组播流量转发。内容涵盖 IGMP/MLD 版本的配置选项、查询器检测、组播路由器状态以及用于管理组播数据库条目的监控工具。

# Bridge IGMP/MLD Snooping

---

IGMP（互联网组管理协议）和 MLD（组播监听发现）Snooping 是桥接功能，使桥接器能够被动监听 IGMP/MLD 网络通信，并利用这些信息为组播流量做出智能转发决策。默认情况下，桥接器会将所有组播流量泛洪到每个桥接端口，类似于广播流量的处理方式。这种默认行为可能不适用于某些应用，如组播视频流或 SDVoE（以太网软件定义视频）部署。IGMP/MLD Snooping 通过仅将组播流量转发到已订阅的客户端所在端口来解决此问题。请参阅下面的 IGMP/MLD 网络概念图。

RouterOS 桥接实现支持 IGMP 版本 1、2 和 3，以及 MLD 版本 1 和 2。该实现基于 RFC4541，各协议规范分别定义于 RFC1112（IGMPv1）、RFC2236（IGMPv2）、RFC3376（IGMPv3）、RFC2710（MLDv1）和 RFC3810（MLDv2）。

:::warning
IGMPv3 和 MLDv2 不支持源特定组播转发。
:::

![IGMP 配置示意图](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-igmp-mld-snooping-01.webp)

仅当启用 `igmp-snooping` 时，桥接器才会处理 IGMP/MLD 消息。此外，桥接器必须具有有效的 IPv6 地址才能处理 MLD 数据包。初始状态下，桥接器不限制任何组播流量，并泛洪所有组播数据包。一旦检测到 IGMP/MLD 查询器——通过接收 IGMP/MLD 查询消息（来自外部组播路由器或本地桥接接口且启用了 `multicast-querier`）——桥接器便开始限制未知 IP 组播流量，并仅从组播数据库（MDB）转发已知的组播流。IGMP 和 MLD 查询器检测独立运行；检测到 IGMP 查询器不会影响 IPv6 组播转发，反之亦然。查询器检测也不会限制非 IP 和链路本地组播组的转发，例如 224.0.0.0/24 和 ff02::1。

:::danger
配备 Marvell-98DX3236、Marvell-98DX224S 或 Marvell-98DX226S 交换芯片的 CRS3xx 系列设备，一旦检测到 IGMP 或 MLD 查询器，便无法区分非 IP、IPv4 和 IPv6 组播数据包。这意味着当检测到查询器时，交换机将停止转发所有未知组播流量（无论协议类型）。此限制不适用于某些链路本地组播地址范围，例如 224.0.0.0/24 或 ff02::1。
:::

## 配置选项

---

本节介绍 IGMP 和 MLD Snooping 的桥接配置选项。

**子菜单：** `/interface/bridge`

| 属性 | 描述 |
| :-- | :-- |
| **igmp-snooping** (*yes \| no*；默认：**no**) | 启用 IGMP 和 MLD Snooping。 |
| **igmp-version** (*2 \| 3*；默认：**2**) | 选择当桥接接口作为 IGMP 查询器时生成 IGMP 成员资格查询所使用的 IGMP 版本。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **last-member-interval** (*时间*；默认：**1s**) | 当桥接端口上的最后一个客户端取消订阅某个组播组，且桥接器作为活动查询器时，桥接器将发送特定于组的 IGMP/MLD 查询，以确保没有其他客户端仍处于订阅状态。此设置更改这些查询的响应时间。如果在特定时间段（`last-member-interval` \* `last-member-query-count`）内未收到成员资格报告，则该组播组将从组播数据库（MDB）中移除。如果桥接端口配置了 fast-leave，则组播组会立即被移除，无需发送任何查询。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **last-member-query-count** (*整数：0..4294967295*；默认：**2**) | 指定 IGMP/MLD Snooping 桥接器在停止转发特定组播流之前，`last-member-interval` 需要经过的次数。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **membership-interval** (*时间*；默认：**4m20s**) | 如果在桥接端口上未收到 IGMP/MLD 成员资格报告，组播数据库（MDB）中的条目被移除前的时间量。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **mld-version** (*1 \| 2*；默认：**1**) | 选择当桥接接口作为 MLD 查询器时生成 MLD 成员资格查询所使用的 MLD 版本。此属性仅在桥接器具有有效 IPv6 地址，且 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **multicast-querier** (*yes \| no*；默认：**no**) | 组播查询器生成周期性的 IGMP/MLD 通用成员资格查询，所有支持 IGMP/MLD 的设备都会以 IGMP/MLD 成员资格报告进行响应。通常，PIM（组播）路由器或 IGMP 代理会生成这些查询。通过使用此属性，可以使启用 IGMP/MLD Snooping 的桥接器生成 IGMP/MLD 通用成员资格查询。当二层网络中没有活动查询器（PIM 路由器或 IGMP 代理）时，应使用此属性。如果二层网络中没有组播查询器，组播数据库（MDB）将无法更新，学习到的条目会超时，IGMP/MLD Snooping 将无法正常工作。仅生成未打标签的 IGMP/MLD 通用成员资格查询，IGMP 查询使用桥接接口自身的 IPv4 地址作为源地址（参见 `querier-uses-bridge-address`），MLD 查询使用桥接接口的 IPv6 链路本地地址。如果检测到外部 IGMP/MLD 查询器（参见监控值 `igmp-querier` 和 `mld-querier`），桥接器将不会发送查询。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*；默认：**temporary-query**) | 组播路由器端口是连接组播路由器或查询器的端口。在此端口上，将发送未注册的组播流和 IGMP/MLD 成员资格报告。此设置更改桥接接口自身的组播路由器状态。此属性可用于将 IGMP/MLD 成员资格报告和组播流量发送到桥接接口，以进行进一步的组播路由或代理。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。<code>disabled</code> - 禁用桥接接口上的组播路由器状态。无论桥接接口上配置了什么，未注册的组播流和 IGMP/MLD 成员资格报告都不会发送到桥接接口。<code>permanent</code> - 启用桥接接口上的组播路由器状态。无论桥接接口上配置了什么，未注册的组播流和 IGMP/MLD 成员资格报告都会发送到桥接接口本身。<code>temporary-query</code> - 使用 IGMP/MLD 查询自动检测桥接接口上的组播路由器状态。 |
| **querier-interval** (*时间*；默认：**4m15s**) | 更改已检测到的查询器和组播路由器端口的超时时间。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **querier-uses-bridge-address** (*yes \| no*；默认：**yes**) | 启用后，桥接 IGMP 查询器使用桥接接口自身的 IPv4 地址作为 IGMP 查询数据包的源地址，而不是默认的 0.0.0.0。某些组播客户端认为来自 0.0.0.0 的查询无效且不响应，这可能导致 Snooping 表条目超时时组播流中断。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 且桥接接口已分配 IPv4 地址时生效。此设置仅适用于 IPv4（IGMP）。MLD 查询始终使用桥接接口的 IPv6 链路本地地址。 |
| **query-interval** (*时间*；默认：**2m5s**) | 更改当桥接接口作为 IGMP/MLD 查询器时发送 IGMP/MLD 通用成员资格查询的间隔。该间隔在发送最后一个启动查询后生效。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **query-response-interval** (*时间*；默认：**10s**) | 此设置更改当桥接器作为 IGMP/MLD 查询器时对通用 IGMP/MLD 查询的响应时间。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **startup-query-count** (*整数：0..4294967295*；默认：**2**) | 指定当桥接接口启用或活动查询器超时时，必须发送多少次通用 IGMP/MLD 查询。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |
| **startup-query-interval** (*时间*；默认：**31s250ms**) | 指定启动时通用 IGMP/MLD 查询之间的间隔。此属性仅在 `igmp-snooping` 和 `multicast-querier` 设置为 `yes` 时生效。 |

**子菜单：** `/interface/bridge/port`

| 属性 | 描述 |
| :-- | :-- |
| **fast-leave** (*yes \| no*；默认：**no**) | 在桥接端口上启用 IGMP/MLD 快速离开功能。当收到 IGMP/MLD 离开消息时，桥接器将停止向该桥接端口转发组播流量。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。 |
| **multicast-router** (*disabled \| permanent \| temporary-query*；默认：**temporary-query**) | 组播路由器端口是连接组播路由器或查询器的端口。在此端口上，将发送未注册的组播流和 IGMP/MLD 成员资格报告。此设置更改桥接端口的组播路由器状态。此属性可用于将 IGMP/MLD 成员资格报告和组播流发送到特定桥接端口，以进行进一步的组播路由或代理。此属性仅在 `igmp-snooping` 设置为 `yes` 时生效。<code>disabled</code> - 禁用桥接端口上的组播路由器状态。无论连接了什么，未注册的组播流和 IGMP/MLD 成员资格报告都不会发送到该桥接端口。<code>permanent</code> - 启用桥接端口上的组播路由器状态。无论连接了什么，未注册的组播流和 IGMP/MLD 成员资格报告都会发送到该桥接端口。<code>temporary-query</code> - 使用 IGMP/MLD 查询自动检测桥接端口上的组播路由器状态。 |
| **unknown-multicast-flood** (*yes \| no*；默认：**yes**) | 更改桥接端口上的组播泛洪选项。它仅控制出口流量。启用时，桥接器允许将组播数据包泛洪到指定桥接端口；禁用时，桥接器限制组播流量泛洪到指定桥接端口。此设置影响所有组播流量，包括非 IP、IPv4、IPv6 以及链路本地组播范围（例如 224.0.0.0/24 和 ff02::1）。请注意，当启用 `igmp-snooping` 并检测到 IGMP/MLD 查询器时，桥接器将自动限制未知 IP 组播的泛洪，因此此设置对于 IGMP/MLD Snooping 配置并非强制要求。将此设置与 `igmp-snooping` 一起使用时，桥接端口上允许的唯一组播流量是来自 MDB 表的已知组播。 |

**子菜单：** `/interface/bridge/mdb`

| 属性 | 描述 |
| :-- | :-- |
| **bridge** (*名称*；默认：) | MDB 条目将被分配到的桥接接口。 |
| **disabled** (*yes \| no*；默认：**no**) | 禁用或启用静态 MDB 条目。 |
| **group** (*ipv4 \| ipv6 地址*；默认：) | IPv4 或 IPv6 组播地址。无法为链路本地组播组 224.0.0.0/24 和 ff02::1 创建静态条目，因为这些数据包始终在所有端口和 VLAN 上泛洪。 |
| **ports** (*名称*；默认：) | 组播组将被转发到的桥接端口列表。 |
| **vid** (*整数：1..4094*；默认：) | 创建 MDB 条目的 VLAN ID，仅在启用 `vlan-filtering` 时适用。未指定 VLAN ID 时，条目将以共享 VLAN 模式工作，并动态应用于特定端口的所有已定义 VLAN ID。 |

## 监控与故障排除

---

本节介绍 IGMP/MLD Snooping 桥接的监控和故障排除选项。

要监控学习到的组播数据库（MDB）条目，请使用 `print` 命令。

**子菜单：** `/interface/bridge/mdb`

| 属性 | 描述 |
| :-- | :-- |
| **bridge** (*只读：*名称**) | 显示条目所属的桥接接口。 |
| **group** (*只读：* *ipv4 \| ipv6 地址*) | 显示组播组地址。 |
| **on-ports** (*只读：名称*) | 显示订阅了特定组播组的桥接端口。 |
| **vid** (*只读：整数*) | 显示组播组的 VLAN ID，仅在启用 `vlan-filtering` 时适用。 |

```ros
[admin@MikroTik] /interface/bridge/mdb/print 
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP              VID  ON-PORTS  BRIDGE 
 0 D ff02::2              1  bridge1   bridge1
 1 D ff02::6a             1  bridge1   bridge1
 2 D ff02::1:ff00:0       1  bridge1   bridge1
 3 D ff02::1:ff01:6a43    1  bridge1   bridge1
 4 D 229.1.1.1           10  ether2    bridge1
 5 D 229.2.2.2           10  ether3    bridge1
                             ether2           
 6 D ff02::2             10  ether5    bridge1
                             ether3           
                             ether2           
                             ether4            
```

要监控桥接接口的当前状态，请使用 `monitor` 命令。

**子菜单：** `/interface/bridge`

| 属性 | 描述 |
| :-- | :-- |
| **igmp-querier** (*none*\| *接口 & IPv4 地址*) | 显示检测到的 IGMP 查询器的桥接端口和源 IP 地址。仅显示检测到的外部 IGMP 查询器，本地桥接 IGMP 查询器（包括 IGMP 代理和 PIM）将不会显示。此监控值仅在启用 `igmp-snooping` 时出现。 |
| **mld-querier** (*none*\| *接口 & IPv6 地址*) | 显示检测到的 MLD 查询器的桥接端口和源 IPv6 地址。仅显示检测到的外部 MLD 查询器，本地桥接 MLD 查询器将不会显示。此监控值仅在启用 `igmp-snooping` 且桥接器具有有效 IPv6 地址时出现。 |
| **multicast-router** (*yes \| no*) | 显示是否在桥接接口上检测到组播路由器。此监控值仅在启用 `igmp-snooping` 时出现。 |

```ros
[admin@MikroTik] /interface/bridge/monitor bridge1
                  state: enabled
    current-mac-address: 64:D1:54:C7:3A:59
            root-bridge: yes
         root-bridge-id: 0x8000.64:D1:54:C7:3A:59
         root-path-cost: 0
              root-port: none
             port-count: 3
  designated-port-count: 3
           fast-forward: no
       multicast-router: no
           igmp-querier: ether2 192.168.10.10
            mld-querier: ether2 fe80::e68d:8cff:fe39:3824
```

要监控桥接端口的当前状态，请使用 `monitor` 命令。

**子菜单：** `/interface/bridge/port`

| 属性 | 描述 |
| :-- | :-- |
| **multicast-router** (*yes \| no*) | 显示是否在端口上检测到组播路由器。此监控值仅在启用 `igmp-snooping` 时出现。 |

```ros
[admin@MikroTik] > /interface/bridge/port/monitor [find]
              interface: ether2          ether3          ether4
                 status: in-bridge       in-bridge       in-bridge
            port-number: 1               2               3
                   role: designated-port designated-port designated-port
              edge-port: no              yes             yes
    edge-port-discovery: yes             yes             yes
    point-to-point-port: yes             yes             yes
           external-fdb: no              no              no
           sending-rstp: yes             yes             yes
               learning: yes             yes             yes
             forwarding: yes             yes             yes
       multicast-router: yes             no              no
       hw-offload-group: switch1         switch1         switch1
```

## 配置示例

---

下面介绍最常见的配置示例。部分示例使用了带 VLAN 过滤的桥接，因此请务必先了解过滤原理 - [桥接 VLAN 过滤](../index.md#bridge-vlan-filtering)、[桥接 VLAN 表](./bridge-vlan-table.md)。

### 基本 IGMP Snooping 配置

第一个示例仅包含一个 IGMP Snooping 桥接器、一个组播源设备和几个组播客户端设备。请参阅下面的网络方案。

![IGMP 基本设置示意图](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-igmp-mld-snooping-02.webp)

首先，创建一个启用 IGMP Snooping 的桥接接口。在此示例中，没有活动的 IGMP 查询器（没有组播路由器或代理），因此必须在同一桥接器上启用本地 IGMP 查询器。这可以通过 `multicast-querier` 设置完成。如果局域网中没有活动的 IGMP 查询器，未注册的 IP 组播将被泛洪，组播条目将始终从组播数据库中超时。

```ros
/interface/bridge
add igmp-snooping=yes multicast-querier=yes name=bridge1
```

然后将必要的接口添加为桥接端口。

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
```

基本 IGMP Snooping 配置已完成。使用 "`/interface/bridge/mdb/print"` 命令监控活动的组播组。如有必要，您可以在同一桥接接口上配置 IP 地址和 [DHCP 服务器](../../network-management/dhcp.md#configuration-examples)。

### 带 VLAN 的 IGMP Snooping 配置

第二个示例增加了一些复杂性。有两个 IGMP Snooping 桥接器，我们需要将组播流量隔离在不同的 VLAN 上。请参阅下面的网络方案。

![IGMP VLAN 设置示意图](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-igmp-mld-snooping-03.webp)

首先，在两台设备上创建桥接器，并将所需接口添加为桥接端口。要更改桥接端口的未打标签 VLAN，请使用 `pvid` 设置。Bridge1 将作为 IGMP 查询器。以下是 Bridge1 的配置命令：

```ros
/interface/bridge
add igmp-snooping=yes multicast-querier=yes name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 pvid=10
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
add bridge=bridge1 interface=sfp-sfpplus1 pvid=10
```

以及 Bridge2 的配置：

```ros
/interface/bridge
add igmp-snooping=yes name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether3 pvid=10
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
add bridge=bridge1 interface=sfp-sfpplus1 pvid=10
```

:::warning
桥接 IGMP 查询器实现只能发送未打标签的 IGMP 查询。如果需要发送带标签的 IGMP 查询或在多个 VLAN 中生成 IGMP 查询，您可以配置 VLAN 接口以及 [IGMP 代理](../../user-guides/routing-and-networking-protocols/multicast/igmp-proxy.md) 或 [PIM-SM](../../user-guides/routing-and-networking-protocols/multicast/pim-sm.md)。IGMP 代理的下游接口以及 PIM-SM 接口都可以作为 IGMP 查询器运行。
:::

确保为设备配置 [管理访问](../#management-access-configuration)。这在配置带 VLAN 过滤的桥接时至关重要。在此示例中，添加了一个带 IP 地址的 VLAN 99 接口到桥接器。此 VLAN 将在带标签的 sfp-sfpplus1 端口上被允许。以下是 Bridge1 的配置命令：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

以及 Bridge2 的配置：

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=MGMT network=192.168.99.0
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,sfp-sfpplus1 vlan-ids=99
```

添加桥接 VLAN 条目并指定带标签和未带标签的端口。VLAN 99 条目已在配置管理访问时创建；现在只需添加 VLAN 10 和 VLAN 20。以下是 Bridge1 的配置命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether2,ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

以及 Bridge2 的配置：

```ros
/interface/bridge/vlan
add bridge=bridge1 untagged=ether3,ether4,sfp-sfpplus1 vlan-ids=10
add bridge=bridge1 tagged=sfp-sfpplus1 untagged=ether5 vlan-ids=20
```

最后，启用 VLAN 过滤。以下是 Bridge1 和 Bridge2 的配置命令：

```ros
/interface/bridge/set [find name=bridge1] vlan-filtering=yes
```

此时，VLAN 和 IGMP Snooping 已配置完成，设备应能通过端口进行通信。但是，建议更进一步应用一些额外的过滤选项。在桥接端口上启用 `ingress-filtering` 和 `frame-types`。以下是 Bridge1 的配置命令：

```ros
/interface/bridge/port
set [find interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

以及 Bridge2 的配置：

```ros
/interface/bridge/port
set [find interface=ether3] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether4] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=ether5] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
set [find interface=sfp-sfpplus1] ingress-filtering=yes
```

### 静态 MDB 条目

自 RouterOS 7.7 版本起，可以为 IPv4 和 IPv6 组播组创建静态 MDB 条目。例如，要为 VLAN 10 上端口 ether2 和 ether3 的组播组 229.10.10.10 创建静态 MDB 条目，请使用以下命令：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=229.10.10.10 ports=ether2,ether3 vid=10
```

使用 `print` 命令验证结果：

```ros
[admin@MikroTik] > /interface/bridge/mdb/print where group=229.10.10.10
Columns: GROUP, VID, ON-PORTS, BRIDGE
 # GROUP         VID  ON-PORTS  BRIDGE 
12 229.10.10.10   10  ether2    bridge1
                      ether3   
```

如果某个 IPv6 组播组不需要被 Snooping，且希望在所有端口和 VLAN 上泛洪，可以在所有 VLAN 和端口（包括桥接接口本身）上创建静态 MDB 条目。使用以下命令为组播组 ff02::2 在所有 VLAN 和端口上创建静态 MDB 条目（根据您的具体设置修改 `ports` 设置）：

```ros
/interface/bridge/mdb
add bridge=bridge1 group=ff02::2 ports=bridge1,ether2,ether3,ether4,ether5

[admin@MikroTik] > /interface/bridge/mdb/print where group=ff02::2
Flags: D - DYNAMIC
Columns: GROUP, VID, ON-PORTS, BRIDGE
 #   GROUP    VID  ON-PORTS  BRIDGE 
 0   ff02::2                 bridge1
15 D ff02::2    1  bridge1   bridge1
16 D ff02::2   10  bridge1   bridge1
                   ether2           
                   ether3           
                   ether4           
                   ether5           
17 D ff02::2   20  bridge1   bridge1
                   ether2           
                   ether3           
18 D ff02::2   30  bridge1   bridge1
                   ether2           
                   ether3     
```