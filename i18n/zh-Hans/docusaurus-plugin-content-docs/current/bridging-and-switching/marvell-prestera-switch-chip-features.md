# Marvell Prestera 交换芯片特性

> 搭载 Marvell Prestera 交换芯片的 MikroTik 设备提供高性能的第二层和第三层功能，包括高级转发、路由卸载、VLAN 支持、QoS、镜像以及用于精确时间同步的 PTP 功能。

import WideTable from '@site/src/components/WideTable';

# Marvell Prestera 交换芯片特性

---

部分 MikroTik 设备采用了高性能且功能丰富的 Marvell Prestera 以太网交换芯片。这些设备可应用于各种以太网场景，包括非管理型交换机、二层管理型交换机、运营商级交换机、VLAN 间路由器以及有线统一数据包处理器。

:::warning
本文仅适用于搭载 Marvell Prestera 交换芯片的 MikroTik 设备，不适用于 [CRS1xx/CRS2xx 系列交换机](./crs1xx-and-2xx-series-switches.md)。
:::

### 功能特性

<WideTable>

| 功能 | 描述 |
| :-- | :-- |
| **转发** | 可配置端口用于交换或路由完整的无阻塞线速交换大型单播 FDB 用于二层单播转发基于 IVL 工作的转发数据库巨型帧支持IGMP/MLD Snooping 支持DHCP Snooping 支持，支持自定义 Option 82（Circuit ID、Remote ID）DHCPv6 Snooping 支持，支持自定义 Option 18（Interface ID）和 Option 37（Remote ID）RA Guard 支持 |
| **路由** | 三层硬件卸载：IPv4、IPv6 单播路由支持在 Ethernet、Bridge、Bonding 和 VLAN 接口上ECMP黑洞卸载的 Fasttrack 连接 <sup>1</sup>卸载的 Fasttrack 连接 NAT <sup>1</sup>硬件卸载的 VRF <sup>1</sup>多 MTU 配置文件**重要提示：** 1. 仅适用于[特定交换机型号](./l3-hardware-offloading.md#l3hw-device-support) |
| **生成树协议** | STPRSTPMSTP边缘端口、BPDU Guard、Root Guard |
| **镜像** | 多种镜像类型：基于端口的镜像基于 VLAN 的镜像基于 MAC 的镜像远程交换端口分析器（RSPAN） |
| **VLAN** | 完全兼容 IEEE802.1Q 和 IEEE802.1ad VLAN4k 个活动 VLAN灵活的 VLAN 分配：基于端口的 VLAN基于协议的 VLAN基于 MAC 的 VLANVLAN 过滤入口 VLAN 转换多 VLAN 注册协议（MVRP） |
| **链路聚合** | 支持 802.3ad（LACP）、balance-xor 和 active-backup 模式每个聚合接口最多 8 个成员端口硬件自动故障转移和负载均衡MLAG |
| **服务质量（QoS）** | 每个端口八个输出队列DSCP 和 802.1p PCP 映射基于端口的二层和三层信任设置基于端口和队列的出口速率限制基于 ACL 规则的策略 QoS严格优先级（SP）和整形赤字加权轮询（SDWRR）队列增强传输选择（ETS）调度加权随机早期检测（WRED） <sup>1</sup>显式拥塞通知（ECN） <sup>1</sup>基于优先级的流控（PFC） <sup>1</sup>资源分配控制（基于队列、共享池和多播），具备全面的监控能力兼容 Dante 环境兼容融合以太网上的远程直接内存访问（RoCE）环境 <sup>1</sup>入口流量限制（基于端口或通过 ACL 规则）流量风暴控制**重要提示：** 1. 仅适用于[特定交换机型号](./quality-of-service.md#qos-device-support) |
| **端口隔离** | 适用于私有 VLAN 实现 |
| **访问控制列表** | 入口 ACL 表基于端口、L2、L3、L4 协议头字段的分类ACL 操作包括过滤、转发和修改协议头字段 |
| **PTP** | 两步普通时钟和边界时钟。硬件时间戳，确保纳秒（ns）级别的时钟同步。IPv4 和二层（L2）多播传输模式。端到端（E2E）和点到点（P2P）延迟机制。IEEE 1588-2008（PTPv2）。配置文件支持：802.1AS：音频视频桥接（AVB）和时间敏感网络（TSN）的定时与同步。AES67：高性能音频-over-IP 互操作性。G.8275.1：PTP 感知网络中的频率和相位同步。SMPTE：专业广播环境中的音视频同步。**重要提示：** PTP 支持取决于硬件，请参考[支持的设备](../system-information-and-utilities/precision-time-protocol.md#supported-devices)列表。 |

:::info
有关 L3 硬件卸载功能支持及硬件限制，请参阅 [功能支持](./l3-hardware-offloading.md#l3hw-device-support) 用户手册。
:::

:::note
有关 QoS 硬件卸载功能支持及硬件限制，请参阅 [服务质量（QoS）](./quality-of-service.md) 用户手册。
:::

</WideTable>

### 型号

下表说明了 Cloud Router Switch 型号与 CCR 路由器之间的主要区别。

<WideTable>

|  |  |  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型号** | **交换芯片** | **CPU** | **内存大小** | **以太网** | **[PoE 输出](../hardware/poe-out.mdx)** | **ACL 规则数** | **单播 FDB 条目** | **巨型帧（字节）** |
| **CRS318-1Fi-15Fr-2S-OUT (netPower 15FR)** | Marvell-98DX224S | ARM 双核 800MHz | 256 MB | 16x 10/100M 以太网  2x 1G SFP | 1x 被动 | 128 | 最多 16K | 10218 |
| **CRS318-16P-2S+OUT (netPower 16P)** | Marvell-98DX226S | ARM 双核 800MHz | 256 MB | 16x 10/100/1000M 以太网  2x 10G SFP+ | 16x 802.3af/at | 128 | 最多 16K | 10218 |
| **CRS310-1G-5S-4S+ (netFiber 9/IN)** | Marvell-98DX226S | ARM 双核 800MHz | 256 MB | 1x 10/100/1000M 以太网  5x 1G SFP  4x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS310-8G+2S+IN** | Marvell-98DX226S | ARM 双核 800MHz | 256 MB | 8x 2.5G 以太网  2x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS320-8P-8B-4S+RM** | Marvell-98DX226S | ARM 双核 800MHz | 256 MB | 16x 10/100/1000M 以太网  4x 10G SFP+ | 8x 802.3af/at  8x 802.3bt | 128 | 最多 16K | 10218 |
| **CRS304-4XG-IN** | Marvell-98DX2528 | ARM64 双核 1200MHz | 512 MB | 4x 1/2.5/5/10G 以太网 |  | 128 | 最多 16K | 10218 |
| **CRS326-24G-2S+ (RM/IN)** | Marvell-98DX3236 | ARM 双核 800MHz | 512 MB | 24x 10/100/1000M 以太网  2x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS328-24P-4S+RM** | Marvell-98DX3236 | ARM 单核 800MHz | 512 MB | 24x 10/100/1000M 以太网  4x 10G SFP+ | 24x 802.3af/at | 128 | 最多 16K | 10218 |
| **CRS328-4C-20S-4S+RM** | Marvell-98DX3236 | ARM 双核 800MHz | 512 MB | 20x 1G SFP  4x 1G combo  4x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS305-1G-4S+IN** | Marvell-98DX3236 | ARM 双核 800MHz | 512 MB | 1x 10/100/1000M 以太网  4x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS305-1G-4S+OUT (FiberBox Plus)** | Marvell-98DX226S | ARM 双核 800MHz | 256 MB | 1x 10/100/1000M 以太网  4x 10G SFP+ |  | 128 | 最多 16K | 10218 |
| **CRS309-1G-8S+IN** | Marvell-98DX8208 | ARM 双核 800MHz | 512 MB | 1x 10/100/1000M 以太网  8x 10G SFP+ |  | 1024 | 最多 32K | 10218 |
| **CRS317-1G-16S+RM** | Marvell-98DX8216 | ARM 双核 800MHz | 1 GB | 1x 10/100/1000M 以太网  16x 10G SFP+ |  | 1024 | 最多 128K | 10218 |
| **CRS312-4C+8XG-RM** | Marvell-98DX8212 | MIPSBE 单核 650MHz | 64 MB | 4x 10G combo  8x 1/2.5/5/10G 以太网 |  | 512 | 最多 32K | 10218 |
| **CRS326-24S+2Q+RM** | Marvell-98DX8332 | MIPSBE 单核 650MHz | 128 MB | 24x 10G SFP+  2x 40G QSFP+ |  | 256 | 最多 32K | 10218 |
| **CRS326-4C+20G+2Q+RM** | Marvell-98DX8332 | MIPSBE 单核 650MHz | 128 MB | 4x 2.5G 以太网/10G SFP+ combo  20x 2.5G 以太网  2x 40G QSFP+ |  | 256 | 最多 32K | 10218 |
| **CRS354-48G-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 单核 650MHz | 128 MB | 48x 10/100/1000M 以太网  4x 10G SFP+  2x 40G QSFP+ |  | 170 | 最多 32K | 10218 |
| **CRS354-48P-4S+2Q+RM** | Marvell-98DX3257 | MIPSBE 单核 650MHz | 128 MB | 48x 10/100/1000M 以太网  4x 10G SFP+  2x 40G QSFP+ | 48x 802.3af/at | 170 | 最多 32K | 10218 |
| **CRS418-8P-8G-2S+RM**  **CRS418-8P-8G-2S+5axQ2axQ-RM** | Marvell-98DX226S | ARM64 四核 2208MHz | 1 GB | 16x 10/100/1000M 以太网  2x 10G SFP+ | 8x 802.3af/at | 128 | 最多 16K | 10218 |
| **CRS504-4XQ (IN/OUT)** | Marvell-98DX4310 | MIPSBE 单核 650MHz | 64 MB | 4x 100G QSFP28 |  | 1024 | 最多 128K | 10218 |
| **CRS510-8XS-2XQ-IN** | Marvell-98DX4310 | MIPSBE 单核 650MHz | 128 MB | 8x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最多 128K | 10218 |
| **CRS518-16XS-2XQ-RM** | Marvell-98DX8525 | MIPSBE 单核 650MHz | 64 MB | 16x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最多 128K | 10218 |
| **CRS520-4XS-16XQ-RM** | Marvell-98CX8410 | ARM64 四核 2000MHz | 4 GB | 4x 25G SFP28  16x 100G QSFP28 |  | 682 | 最多 256K | 9570 |
| **CRS812-8DS-2DQ-2DDQ-RM** | Marvell-98DX7335 | ARM64 四核 2000MHz | 4 GB | 8x 50G SFP56  2x 200G QSFP56  2x 400G QSFP56-DD |  | 1365 | 最多 128K | 9570 |
| **CRS804-4DDQ-hRM** | Marvell-98DX7335 | ARM64 四核 2000MHz | 4 GB | 4x 400G QSFP56-DD |  | 1365 | 最多 128K | 9570 |
| **CCR2116-12G-4S+** | Marvell-98DX3255 | ARM64 十六核 2000MHz | 16 GB | 12x 10/100/1000M 以太网  4x 10G SFP+ |  | 512 | 最多 32K | 9570 |
| **CCR2216-1G-12XS-2XQ** | Marvell-98DX8525 | ARM64 十六核 2000MHz | 16 GB | 12x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最多 128K | 9570 |
| **RDS2216-2XG-4S+4XS-2XQ** | Marvell-98DX4310 | ARM64 十六核 2000MHz | 32 GB | 2x 1/2.5/5/10G 以太网  4x 10G SFP+  4x 25G SFP28  2x 100G QSFP28 |  | 1024 | 最多 128K | 9570 |

</WideTable>

### 缩写

- FDB - 转发数据库（Forwarding Database）。
- MDB - 多播数据库（Multicast Database）。
- SVL - 共享 VLAN 学习（Shared VLAN Learning）。
- IVL - 独立 VLAN 学习（Independent VLAN Learning）。
- PVID - 端口 VLAN ID（Port VLAN ID）。
- ACL - 访问控制列表（Access Control List）。
- CVID - 客户 VLAN ID（Customer VLAN ID）。
- SVID - 服务 VLAN ID（Service VLAN ID）。

## 端口交换

---

要设置端口交换，请查看 [桥接硬件卸载](index.md#bridge-hardware-offloading) 页面。

:::danger
目前，只能创建一个启用硬件卸载的桥接。使用 `hw=yes/no` 参数选择哪个桥接将使用硬件卸载。
:::

:::warning
桥接的 STP/RSTP/MSTP、IGMP Snooping 和 VLAN 过滤设置不影响硬件卸载。自 RouterOS v6.42 起，Bonding 接口也支持硬件卸载。
:::

## VLAN

---

自 RouterOS 6.41 版本起，桥接提供 VLAN 感知的二层转发以及桥内 VLAN 标签修改功能。这一系列功能使桥接操作更类似于传统以太网交换机，并且与桥接隧道式 VLAN 接口的配置相比，能够克服生成树兼容性问题。强烈建议配置桥接 VLAN 过滤以符合 STP（802.1D）、RSTP（802.1w）标准，并且在 RouterOS 中启用 MSTP（802.1s）支持是强制性的。

### VLAN 过滤

详细的架构概念和配置步骤请参阅主要的 [桥接 VLAN 过滤](index.md#bridge-vlan-filtering) 部分。

#### 支持的 VLAN 实现方式

根据您的网络设计，您可以实现多种硬件卸载的 VLAN 拓扑：

- **基于端口的 VLAN：** 请参阅 [桥接 VLAN 过滤](index.md#bridge-vlan-filtering) 部分中的分步配置指南。
- **基于协议的 VLAN：** 通过交换机规则表配置，以映射特定的网络协议。
- **基于 MAC 的 VLAN：** 将特定的源 MAC 地址映射到指定的 VLAN ID。

---

### 基于 MAC 的 VLAN 配置

:::warning 硬件与转发限制

- **规则容量：** 此功能使用硬件交换机规则表。请参阅 [交换芯片型号容量表](./marvell-prestera-switch-chip-features.md#models) 以确认您的特定设备支持多少条规则。
- **CPU 转发限制：** 基于 MAC 的 VLAN 严格适用于硬件端口之间交换的流量。如果数据包被路由或转发到 CPU，则将强制执行桥接端口的默认 `pvid`，而不是 ACL 规则中定义的 `new-vlan-id` 操作。
- **DHCP 冲突：** 如果在桥接上启用了 `dhcp-snooping=yes`，基于 MAC 的 VLAN 匹配将无法处理 DHCP 数据包。
:::

#### 配置示例

通过创建启用硬件卸载的桥接来启用端口交换：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在桥接 VLAN 表中添加 VLAN 并指定端口：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=200,300,400
```

添加基于 MAC 地址分配 VLAN ID 的交换机规则：

```ros
/interface/ethernet/switch/rule
add switch=switch1 ports=ether7 src-mac-address=A4:12:6D:77:94:43/FF:FF:FF:FF:FF:FF new-vlan-id=200
add switch=switch1 ports=ether7 src-mac-address=84:37:62:DF:04:20/FF:FF:FF:FF:FF:FF new-vlan-id=300
add switch=switch1 ports=ether7 src-mac-address=E7:16:34:A1:CD:18/FF:FF:FF:FF:FF:FF new-vlan-id=400
```

#### 基于协议的 VLAN

:::warning

- 基于协议的 VLAN 功能使用交换机规则表，请参阅[此表](./marvell-prestera-switch-chip-features.md#models)了解每个设备支持多少条规则。
- 基于协议的 VLAN 仅在交换机端口之间正常工作，不适用于交换机端口与 CPU 之间的通信。当数据包被转发到 CPU 时，将始终使用桥接端口的 `pvid` 属性，而不是 ACL 规则中的 `new-vlan-id`。
- 当启用 DHCP Snooping 时，基于协议的 VLAN 将不适用于 DHCP 数据包。

:::

通过创建启用硬件卸载的桥接来启用端口交换：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

在桥接 VLAN 表中添加 VLAN 并指定端口：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 untagged=ether6 vlan-ids=200
add bridge=bridge1 tagged=ether2 untagged=ether7 vlan-ids=300
add bridge=bridge1 tagged=ether2 untagged=ether8 vlan-ids=400
```

添加基于 MAC 协议分配 VLAN ID 的交换机规则：

```ros
/interface/ethernet/switch/rule
add mac-protocol=ip new-vlan-id=200 ports=ether6 switch=switch1
add mac-protocol=ipx new-vlan-id=300 ports=ether7 switch=switch1
add mac-protocol=0x80F3 new-vlan-id=400 ports=ether8 switch=switch1
```

#### VLAN 隧道（Q-in-Q）

自 RouterOS v6.43 起，可以同时使用运营商桥接（IEEE 802.1ad）和标签堆叠 VLAN 过滤以及硬件卸载。配置方法在 [桥接 VLAN 隧道（Q-in-Q）](vlan.md#q-in-q) 部分中描述。

:::danger
搭载 Marvell-98DX3257 交换芯片的设备（例如 CRS354 系列）不支持在 1Gbps 以太网接口上对其他 VLAN 类型（`0x88a8` 和 `0x9100`）进行 VLAN 过滤。
:::

### 入口 VLAN 转换

可以使用 ACL 规则在入口端口上将某个 VLAN ID 转换为不同的 VLAN ID。在此示例中，我们创建两条 ACL 规则，允许双向通信。可以通过以下步骤完成。

创建一个新的桥接并添加端口，启用硬件卸载：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=no
/interface/bridge/port
add interface=ether1 bridge=bridge1 hw=yes
add interface=ether2 bridge=bridge1 hw=yes
```

添加 ACL 规则以在每个方向转换 VLAN ID：

```ros
/interface/ethernet/switch/rule
add new-dst-ports=ether2 new-vlan-id=20 ports=ether1 switch=switch1 vlan-id=10
add new-dst-ports=ether1 new-vlan-id=10 ports=ether2 switch=switch1 vlan-id=20
```

将两个 VLAN ID 添加到桥接 VLAN 表：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=ether2 vlan-ids=20
```

启用桥接 VLAN 过滤：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
双向通信仅限于两个交换机端口之间。在多个端口之间转换 VLAN ID 可能导致流量泛洪或同一 VLAN 端口之间的错误转发。

**注意：** 启用 `vlan-filtering` 将过滤发往 CPU 的流量。在启用 VLAN 过滤之前，您应确保已设置[管理端口](index.md#management-access-configuration)。
:::

## (R/M)STP

---

搭载 Marvell Prestera 交换芯片的 MikroTik 设备能够在硬件层面运行 STP、RSTP 和 MSTP。有关更详细的信息，请查看[生成树协议](./user-guides/spanning-tree-protocol.md)手册页面，相关的配置/监控选项请参阅[桥接与交换](./)页面。

## Bonding

---

搭载 Marvell Prestera 交换芯片的 MikroTik 设备支持 Bonding 接口的硬件卸载。只有 `802.3ad`（LACP）、`balance-xor`（静态 LAG）和 `active-backup` 聚合模式支持硬件卸载；其他聚合模式将使用 CPU 资源。您可以在 [Bonding 接口](../high-availability-solutions/bonding.md) 部分找到有关聚合接口的更多信息。

要创建硬件卸载的 Bonding 接口，必须使用受支持的聚合模式创建聚合接口：

```ros
/interface/bonding
add mode=802.3ad name=bond1 slaves=ether1,ether2
```

该接口可以与其他接口一起添加到桥接中：

```ros
/interface/bridge
add name=bridge
/interface/bridge/port
add bridge=bridge interface=bond1 hw=yes
add bridge=bridge interface=ether3 hw=yes
add bridge=bridge interface=ether4 hw=yes
```

:::warning
不要将已在聚合中的接口添加到桥接，RouterOS 不允许将已经是聚合从属端口的接口添加到桥接。
:::

通过检查“H”标志确保聚合接口已启用硬件卸载：

```text
/interface/bridge/port/print 
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                                 BRIDGE                                 HW
 0   H bond1                                     bridge                                 yes
 1   H ether3                                    bridge                                 yes
 2   H ether4                                    bridge                                 yes
```

:::warning
对于硬件卸载的 Bonding 接口，内置交换芯片将始终使用二层+三层+四层作为传输哈希策略；手动更改传输哈希策略将不会生效。
:::

### 配置示例 - 带 Bonding 的 VLAN

本部分将展示如何配置多台交换机以使用 Bonding 接口和基于端口的 VLAN，同时还将展示一个包含 DHCP 服务器、VLAN 间路由、管理 IP 和无效 VLAN 过滤配置的工作示例。

对于此网络拓扑，我们将使用两台 CRS326-24G-2S+、一台 CRS317-1G-16S+ 和一台 CCR1072-1G-8S+。

![CRS3xx VLANs with Bonds](https://manual.mikrotik.com/docs/bridging-and-switching/img/marvell-prestera-switch-chip-features-01.webp)

在此设置中，SwitchA 和 SwitchC 将把来自 ether1-ether8 端口的所有流量标记为 VLAN ID 10，ether9-ether16 标记为 VLAN ID 20，ether17-ether24 标记为 VLAN ID 30。只有当用户从 SwitchA 或 SwitchB 的 ether1 使用带 VLAN ID 99 的标记流量连接时，才能进行管理。从路由器使用带 VLAN ID 99 的标记流量也可以连接到所有设备。此设置中的 SFP+ 端口将用作 VLAN  trunk 端口，同时处于聚合中以创建 LAG 接口。

#### 配置 Bonding

当需要更大带宽时，使用 Bonding 接口。这是通过创建链路聚合组来实现的，该组还为交换机提供硬件自动故障转移和负载均衡。通过将两个 10Gbps 接口添加到聚合中，可以将理论带宽限制提高到 20Gbps。确保所有聚合接口都连接到相同的速率。

:::info
使用硬件卸载桥接时，交换机使用内置交换芯片聚合流量，无需使用 CPU 资源。
:::

要在 SwitchA 和 SwitchB 之间以及 SwitchC 和 SwitchB 之间创建 20Gbps 的 Bonding 接口（使用 sfp-sfpplus1 和 sfp-sfpplus2），请在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
```

要在 SwitchB 和路由器之间创建 40Gbps 的 Bonding 接口，并在 SwitchA 和 SwitchC 之间创建 20Gbps 的 Bonding 接口，请在 **SwitchB** 上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2 slaves=sfp-sfpplus1,sfp-sfpplus2
add mode=802.3ad name=bond_3-4 slaves=sfp-sfpplus3,sfp-sfpplus4
add mode=802.3ad name=bond_5-6-7-8 slaves=sfp-sfpplus5,sfp-sfpplus6,sfp-sfpplus7,sfp-sfpplus8
```

在我们的案例中，路由器需要一个基于软件的 Bonding 接口。请在**路由器**上使用以下命令：

```ros
/interface/bonding
add mode=802.3ad name=bond_1-2-3-4 slaves=sfp-sfpplus1,sfp-sfpplus2,sfp-sfpplus3,sfp-sfpplus4
```

:::info
接口聚合不会创建具有更大链路速度的接口。接口聚合创建一个虚拟接口，可以在多个接口上负载均衡流量。更多详细信息请参阅 [LAG 接口与负载均衡](./user-guides/layer2-misconfiguration.md#lag-interfaces-and-load-balancing) 页面。
:::

#### 配置端口交换

此设置中的所有交换机都要求所有使用的端口一起交换。对于聚合，您应将聚合接口添加为桥接端口，而不是单独的聚合端口。请在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=ether1 pvid=10
add bridge=bridge interface=ether2 pvid=10
add bridge=bridge interface=ether3 pvid=10
add bridge=bridge interface=ether4 pvid=10
add bridge=bridge interface=ether5 pvid=10
add bridge=bridge interface=ether6 pvid=10
add bridge=bridge interface=ether7 pvid=10
add bridge=bridge interface=ether8 pvid=10
add bridge=bridge interface=ether9 pvid=20
add bridge=bridge interface=ether10 pvid=20
add bridge=bridge interface=ether11 pvid=20
add bridge=bridge interface=ether12 pvid=20
add bridge=bridge interface=ether13 pvid=20
add bridge=bridge interface=ether14 pvid=20
add bridge=bridge interface=ether15 pvid=20
add bridge=bridge interface=ether16 pvid=20
add bridge=bridge interface=ether17 pvid=30
add bridge=bridge interface=ether18 pvid=30
add bridge=bridge interface=ether19 pvid=30
add bridge=bridge interface=ether20 pvid=30
add bridge=bridge interface=ether21 pvid=30
add bridge=bridge interface=ether22 pvid=30
add bridge=bridge interface=ether23 pvid=30
add bridge=bridge interface=ether24 pvid=30
add bridge=bridge interface=bond_1-2
```

通过在 **SwitchB** 上使用以下命令，将所有聚合接口添加到 SwitchB 上的单个桥接：

```ros
/interface/bridge
add name=bridge vlan-filtering=no
/interface/bridge/port
add bridge=bridge interface=bond_1-2
add bridge=bridge interface=bond_3-4
add bridge=bridge interface=bond_5-6-7-8
```

#### 配置管理 IP

创建管理接口并为其分配 IP 地址以保持对交换机的访问是非常有用的。这在更新交换机时也非常有用，因为启用无效 VLAN 过滤后，发往交换机的此类流量将被阻止。

在 **SwitchA**、**SwitchB** 和 **SwitchC** 上创建可路由的 VLAN 接口：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
```

路由器需要在聚合接口上创建可路由的 VLAN 接口。使用以下命令在**路由器**上创建 VLAN 接口：

```ros
/interface/vlan
add interface=bond_1-2-3-4 name=MGMT vlan-id=99
```

在本指南中，我们将为每个设备使用以下地址：

| 设备 | 地址 |
| :-- | :-- |
| 路由器 | 192.168.99.1 |
| SwitchA | 192.168.99.2 |
| SwitchB | 192.168.99.3 |
| SwitchC | 192.168.99.4 |

为每个交换机设备在 VLAN 接口上添加 IP 地址（将 X 更改为相应的数字）：

```ros
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

不要忘记在交换机设备上添加默认网关并指定 DNS 服务器：

```ros
/ip/route
add gateway=192.168.99.1
/ip/dns
set servers=192.168.99.1
```

在**路由器**上添加 IP 地址：

```ros
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

#### 配置无效 VLAN 过滤

由于 SwitchA 和 SwitchC 上的大多数端口将是接入端口，您可以设置所有端口仅接受特定类型的数据包，在这种情况下，我们希望 SwitchA 和 SwitchC 仅接受未标记的数据包。请在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-untagged-and-priority-tagged
```

SwitchA 和 SwitchC 上的帧类型有一个例外。在此设置中，需要从 ether1 和聚合接口进行管理访问。它们要求能够转发标记流量。请在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/port
set [find where interface=ether1] frame-types=admit-all
set [find where interface=bond_1-2] frame-types=admit-only-vlan-tagged
```

在 SwitchB 上，只应转发标记的数据包，请在 **SwitchB** 上使用以下命令：

```ros
/interface/bridge/port
set [ find ] frame-types=admit-only-vlan-tagged
```

可选步骤是在桥接接口上设置 `frame-types=admit-only-vlan-tagged` 以禁用默认的未标记 VLAN 1（`pvid=1`）。我们在桥接上使用标记的 VLAN 进行管理访问，因此无需在桥接上接受未标记的流量。请在 **SwitchA**、**SwitchB** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/set [find name=bridge] frame-types=admit-only-vlan-tagged
```

需要设置桥接 VLAN 表。在此网络设置中，我们需要允许 ether1-ether8 上的 VLAN 10、ether9-ether16 上的 VLAN 20、ether17-ether24 上的 VLAN 30、bond\_1-2 上的 VLAN 10,20,30,99，以及 SwitchA 和 SwitchC 上 ether1 的特殊情况以允许 VLAN 99 的转发。请在 **SwitchA** 和 **SwitchC** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2 vlan-ids=10
add bridge=bridge tagged=bond_1-2 vlan-ids=20
add bridge=bridge tagged=bond_1-2 vlan-ids=30
add bridge=bridge tagged=bridge,bond_1-2,ether1 vlan-ids=99
```

:::warning
`frame-types` 设置为 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的桥接端口将自动作为 `pvid` VLAN 的未标记端口添加。
:::

同样，需要为 SwitchB 设置桥接 VLAN 表。请在 **SwitchB** 上使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=bond_1-2,bond_3-4,bond_5-6-7-8 vlan-ids=10,20,30
add bridge=