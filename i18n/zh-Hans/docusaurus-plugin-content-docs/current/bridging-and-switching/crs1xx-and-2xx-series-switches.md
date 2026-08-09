# CRS1xx 和 2xx 系列交换机

> 本页介绍 MikroTik RouterOS CRS1xx 和 2xx 系列交换机，重点介绍其高性能特性，包括二层/三层交换、VLAN 支持、QoS 工具、镜像功能以及端口隔离选项。文中详细说明了型号差异、技术规格（如 CPU 速度和巨型帧大小），并提供了 VLAN 相关术语的缩写。

# CRS1xx 和 2xx 系列交换机

---

Cloud Router Switch 系列是高度集成的交换机，配备高性能 MIPS CPU 和功能丰富的数据包处理器。CRS 交换机可应用于各种以太网场景，包括非管理型交换机、二层管理型交换机、运营商级交换机以及无线/有线统一数据包处理。参见 [Cloud Router Switch](./user-guides/crs1xx-2xx-series-switches-examples.md) 配置示例。

:::danger
本文适用于 CRS1xx 和 CRS2xx 系列交换机，不适用于采用 Marvell Prestera 交换芯片的 MikroTik 设备（例如 CRS3xx）。对于采用 Marvell Prestera 交换芯片的 MikroTik 设备，请参阅 [Marvell Prestera 交换芯片特性](./marvell-prestera-switch-chip-features.md) 手册。
:::

| 特性 | 描述 |
| :-- | :-- |
| **转发** | 可配置端口用于交换或路由完全非阻塞线速交换单播 FDB 中最多 16k 条 MAC 条目，用于二层单播转发组播 FDB 中最多 1k 条 MAC 条目，用于组播转发保留 FDB 中最多 256 条 MAC 条目，用于控制和管理目的所有转发数据库均支持 IVL 和 SVL可配置的基于端口的 MAC 学习限制巨型帧支持（CRS1xx/2xx：9204 字节；CRS125/CRS109：4064 字节）IGMP Snooping 支持 |
| **镜像** | 多种镜像类型：基于端口的镜像基于 VLAN 的镜像基于 MAC 的镜像2 个独立的镜像分析端口 |
| **VLAN** | 完全兼容 IEEE802.1Q 和 IEEE802.1ad VLAN4k 个活动 VLAN灵活的 VLAN 分配：基于端口的 VLAN基于协议的 VLAN基于 MAC 的 VLAN任意到任意的 VLAN 转换和交换1：1 VLAN 交换 - VLAN 到端口映射VLAN 过滤 |
| **端口隔离与泄漏** | 适用于私有 VLAN 实现3 种端口配置文件类型：混杂、隔离和公共最多 28 个公共配置文件泄漏配置文件允许绕过出口 VLAN 过滤 |
| **链路聚合** | 支持静态链路聚合组最多 8 个端口聚合组每个端口聚合组最多 8 个成员端口硬件自动故障转移和负载均衡 |
| **服务质量（QoS）** | 灵活的 QoS 分类和分配：基于端口基于 MAC基于 VLAN基于协议基于 PCP/DEI基于 DSCP基于 ACLQoS 标记和重映射，用于服务提供商和客户网络之间的 QoS 域转换根据配置的优先级覆盖每个 QoS 分配 |
| **整形与调度** | 每个物理端口 8 个队列按端口、按队列、按队列组进行整形 |
| **访问控制列表** | 入口和出口 ACL 表最多 128 条 ACL 规则（受 RouterOS 限制）基于端口、L2、L3、L4 协议头字段的分类ACL 操作包括过滤、转发和修改协议头字段 |

## Cloud Router Switch 型号

---

下表说明了 Cloud Router Switch 各型号之间的主要区别。

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **型号** | **交换芯片** | **CPU** | **无线** | **SFP+ 端口** | **访问控制列表** | **巨型帧（字节）** |
| **CRS105-5S-FB** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS106-1C-5S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS112-8G-4S** | QCA-8511 | 400MHz | - | - | + | 9204 |
| **CRS210-8G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS212-1G-10S-1S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS226-24G-2S+** | QCA-8519 | 400MHz | - | + | + | 9204 |
| **CRS125-24G-1S** | QCA-8513L | 600MHz | - | - | - | 4064 |
| **CRS125-24G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |
| **CRS109-8G-1S-2HnD** | QCA-8513L | 600MHz | + | - | - | 4064 |

## 缩写与解释

---

CVID - 客户 VLAN ID：IEEE 802.1ad 帧的内层 VLAN 标签 ID

SVID - 服务 VLAN ID：IEEE 802.1ad 帧的外层 VLAN 标签 ID

IVL - 独立 VLAN 学习 - 学习/查找基于 MAC 地址和 VLAN ID。

SVL - 共享 VLAN 学习 - 学习/查找基于 MAC 地址 - 而非 VLAN ID。

TPID - 标签协议标识符

PCP - 优先级代码点：一个 3 位字段，指 IEEE 802.1p 优先级

DEI - 丢弃合格指示符

DSCP - 差异化服务代码点

丢弃优先级 - 一个内部 CRS 交换机 QoS 属性，用于数据包入队或丢弃。

## 端口交换

---

要在 CRS1xx/2xx 系列交换机上设置端口交换，请查看 [桥接硬件卸载](index.md#bridge-hardware-offloading) 页面。

:::warning
当创建硬件卸载桥接并添加交换端口组时，CRS 交换机会创建动态保留 VLAN 条目（VLAN4091；VLAN4090；VLAN4089；等）。这些 VLAN 是内部操作所必需的，其优先级低于用户配置的 VLAN。
:::

### 多个交换机组

CRS1xx/2xx 系列交换机允许您使用多个启用硬件卸载的桥接；这使您可以轻松隔离多个交换机组。这可以通过简单地创建多个桥接并启用硬件卸载来实现。

:::warning
多硬件卸载桥接配置被设计为一种快速简单的端口隔离解决方案，但它限制了 CRS 交换芯片支持的部分 VLAN 功能。对于高级配置，请在 CRS 交换芯片内使用一个桥接用于所有端口，配置 VLAN，并使用端口隔离配置文件来隔离端口组。
:::

:::danger
CRS1xx/2xx 系列交换机可以运行多个启用 (R)STP 的硬件卸载桥接，但不推荐这样做，因为该设备并非设计用于在硬件级别运行多个 (R)STP 实例。要隔离多个交换机组并启用 (R)STP，您应该使用端口隔离配置文件配置来隔离端口组。
:::

## 全局设置

---

CRS 交换芯片可通过 `/interface/ethernet/switch` 控制台菜单进行配置。

**子菜单：** `/interface/ethernet/switch`

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串值*; 默认值：**switch1**) | 交换机名称。 |
| **bridge-type** (*customer-vid-used-as-lookup-vid \| service-vid-used-as-lookup-vid*; 默认值：**customer-vid-used-as-lookup-vid**) | 桥接类型定义哪个 VLAN 标签用作查找 VID。查找 VID 作为所有基于 VLAN 的查找的 VLAN 键。 |
| **mac-level-isolation** (*yes \| no*; 默认值：**yes**) | 全局启用或禁用 MAC 层隔离。启用后，交换机将检查源和目标 MAC 地址条目及其在单播转发表中的 `isolation-profile`。默认情况下，交换机会学习 MAC 地址并将其放入 `promiscuous` 隔离配置文件。创建静态单播条目时可以使用其他隔离配置文件。如果源或目标 MAC 地址位于 `promiscuous` 隔离配置文件中，则数据包被转发。如果源和目标 MAC 地址都位于相同的 `community1` 或 `community2` 隔离配置文件中，则数据包被转发。当源和目标 MAC 地址隔离配置文件为 `isolated`，或源和目标 MAC 地址隔离配置文件来自不同的社区（例如，源 MAC 地址是 `community1`，目标 MAC 地址是 `community2`）时，数据包被丢弃。当 MAC 层隔离被全局禁用时，隔离被绕过。 |
| **use-svid-in-one2one-vlan-lookup** (*yes \| no*; 默认值：**no**) | 是否在 1：1 VLAN 交换查找中使用服务 VLAN ID。 |
| **use-cvid-in-one2one-vlan-lookup** (*yes \| no*; 默认值：**yes**) | 是否在 1：1 VLAN 交换查找中使用客户 VLAN ID。 |
| **multicast-lookup-mode** (*dst-ip-and-vid-for-ipv4 \| dst-mac-and-vid-always*; 默认值：**dst-ip-and-vid-for-ipv4**) | IPv4 组播桥接的查找模式。dst-mac-and-vid-always - 对于所有数据包类型，查找键是目标 MAC 和 VLAN ID。dst-ip-and-vid-for-ipv4 - 对于 IPv4 数据包，查找键是目标 IP 和 VLAN ID。对于其他数据包类型，查找键是目标 MAC 和 VLAN ID。 |
| **unicast-fdb-timeout** (*时间间隔*; 默认值：**5m**) | 单播 FDB 条目的超时时间。 |
| **override-existing-when-ufdb-full** (*yes \| no*; 默认值：**no**) | 当 UFDB 已满时，启用或禁用覆盖老化值最低的现有条目。 |

| 属性 | 描述 |
| :-- | :-- |
| **drop-if-no-vlan-assignment-on-ports** (*端口*; 默认值：**none**) | 如果未应用基于 MAC、基于协议的 VLAN 分配或入口 VLAN 转换，则丢弃帧的端口。 |
| **drop-if-invalid-or-src-port- -not-member-of-vlan-on-ports** (*端口*; 默认值：**none**) | 丢弃无效和其他端口 VLAN ID 帧的端口。 |
| **unknown-vlan-lookup-mode** (*ivl \| svl*; 默认值：**svl**) | 对具有无效 VLAN 的数据包的查找和学习模式。 |
| **forward-unknown-vlan** (*yes \| no*; 默认值：**yes**) | 是否允许转发不在 VLAN 表中的 VLAN。 |

| 属性 | 描述 |
| :-- | :-- |
| **bypass-vlan-ingress-filter-for** (*协议*; 默认值：**none**) | 被排除在入口 VLAN 过滤之外的协议。如果这些协议具有无效 VLAN，则不会被丢弃。（arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1） |
| **bypass-ingress-port-policing-for** (*协议*; 默认值：**none**) | 被排除在入口端口策略之外的协议。（arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1） |
| **bypass-l2-security-check-filter-for** (*协议*; 默认值：**none**) | 被排除在策略规则安全检查之外的协议。（arp, dhcpv4, dhcpv6, eapol, igmp, mld, nd, pppoe-discovery, ripv1） |

| 属性 | 描述 |
| :-- | :-- |
| **ingress-mirror0** (*端口 \| 聚合组,格式*; 默认值：**none,modified**) | 第一个入口镜像分析端口或聚合组及镜像格式：analyzer-configured - 数据包与发往目的地的数据包相同。VLAN 格式根据分析端口的 VLAN 配置进行修改。modified - 数据包与发往目的地的数据包相同。VLAN 格式根据出口端口的 VLAN 配置进行修改。original - 流量镜像时对原始传入数据包格式不做任何更改。但服务 VLAN 标签在边缘端口被剥离。 |
| **ingress-mirror1** (*端口 \| 聚合组,格式*; 默认值：**none,modified**) | 第二个入口镜像分析端口或聚合组及镜像格式：analyzer-configured - 数据包与发往目的地的数据包相同。VLAN 格式根据分析端口的 VLAN 配置进行修改。modified - 数据包与发往目的地的数据包相同。VLAN 格式根据出口端口的 VLAN 配置进行修改。original - 流量镜像时对原始传入数据包格式不做任何更改。但服务 VLAN 标签在边缘端口被剥离。 |
| **ingress-mirror-ratio** (*1/32768..1/1*; 默认值：**1/1**) | 入口镜像数据包占所有数据包的比例。 |
| **egress-mirror0** (*端口 \| 聚合组,格式*; 默认值：**none,modified**) | 第一个出口镜像分析端口或聚合组及镜像格式：analyzer-configured - 数据包与发往目的地的数据包相同。VLAN 格式根据分析端口的 VLAN 配置进行修改。modified - 数据包与发往目的地的数据包相同。VLAN 格式根据出口端口的 VLAN 配置进行修改。original - 流量镜像时对原始传入数据包格式不做任何更改。但服务 VLAN 标签在边缘端口被剥离。 |
| **egress-mirror1** (*端口 \| 聚合组,格式*; 默认值：**none,modified**) | 第二个出口镜像分析端口或聚合组及镜像格式：analyzer-configured - 数据包与发往目的地的数据包相同。VLAN 格式根据分析端口的 VLAN 配置进行修改。modified - 数据包与发往目的地的数据包相同。VLAN 格式根据出口端口的 VLAN 配置进行修改。original - 流量镜像时对原始传入数据包格式不做任何更改。但服务 VLAN 标签在边缘端口被剥离。 |
| **egress-mirror-ratio** (*1/32768..1/1*; 默认值：**1/1**) | 出口镜像数据包占所有数据包的比例。 |
| **mirror-egress-if-ingress-mirrored** (*yes \| no*; 默认值：**no**) | 当一个数据包同时应用入口和出口镜像时，如果此设置被禁用，则仅对数据包执行入口镜像。如果此设置启用，则应用两种镜像类型。 |
| **mirror-tx-on-mirror-port** (*yes \| no*; 默认值：**no**) |  |
| **mirrored-packet-qos-priority** (*0..7*; 默认值：**0**) | 镜像数据包中重新标记的优先级。 |
| **mirrored-packet-drop-precedence** (*drop \| green \| red \| yellow*; 默认值：**green**) | 镜像数据包中重新标记的丢弃优先级。此 QoS 属性用于镜像数据包的入队或丢弃。 |
| **fdb-uses** (*mirror0 \| mirror1*; 默认值：**mirror0**) | 用于基于 FDB 的镜像的分析端口。 |
| **vlan-uses** (*mirror0 \| mirror1*; 默认值：**mirror0**) | 用于基于 VLAN 的镜像的分析端口。 |

## 端口设置

---

**子菜单：** `/interface/ethernet/switch/port`

| 属性 | 描述 |
| :-- | :-- |
| **vlan-type** (*edge-port \| network-port*; 默认值：**network-port**) | 端口 VLAN 类型指定 VLAN ID 是否用于 UFDB 学习。网络端口在 UFDB 中学习 VLAN ID，边缘端口不学习 - VLAN 0。这仅在 IVL 学习模式下可观察到。 |
| **isolation-leakage-profile-override** (*yes \| no*; 默认值：**!isolation-leakage-profile-override**) **isolation-leakage-profile** (*0..31*;) | 用于端口隔离/泄漏配置的自定义端口配置文件。端口级隔离配置文件 0。上行链路端口 - 允许该端口与设备中的所有端口通信。端口级隔离配置文件 1。隔离端口 - 允许该端口仅与上行链路端口通信。端口级隔离配置文件 2 - 31。公共端口 - 允许相同公共端口和上行链路端口之间的通信。 |
| **learn-override** (*yes \| no*; 默认值：**!learn-override**) **learn-limit** (*1..1023*; 默认值：**!learn-limit**) | 启用或禁用 MAC 地址学习并设置端口上的 MAC 限制。当设置 !learn-override 和 !learn-limit 时，MAC 学习限制默认禁用。自 RouterOS v6.42 起，属性 learn-override 被 `/interface/bridge/port` 菜单下的 learn 取代。 |
| **drop-when-ufdb-entry-src-drop** (*yes \| no*; 默认值：**yes**) | 当 UFDB 条目具有操作 src-drop 时，启用或禁用丢弃数据包。 |
| **allow-unicast-loopback** (*yes \| no*; 默认值：**no**) | 端口上的单播环回。启用后，对于已知单播数据包，当源端口和目标端口相同时，允许发送回。 |
| **allow-multicast-loopback** (*yes \| no*; 默认值：**no**) | 端口上的组播环回。启用后，对于已注册的组播或广播数据包，当源端口和目标端口相同时，允许发送回。 |
| **action-on-static-station-move** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; 默认值：**forward**) | 当 UFDB 已包含具有此类 MAC 但端口不同的静态条目时，对数据包执行的操作。 |
| **drop-dynamic-mac-move** (*yes \| no*; 默认值：**no**) | 如果 MAC 已在另一个端口上学习，则阻止 MAC 重新学习，直到 UFDB 超时。 |

| 属性 | 描述 |
| :-- | :-- |
| **allow-fdb-based-vlan-translate** (*yes \| no*; 默认值：**no**) | 在端口上启用或禁用基于 MAC 的 VLAN 转换。 |
| **allow-mac-based-service-vlan-assignment-for** (*all-frames \| none \|* *tagged-frame-only \| untagged-and-priority-tagged-frame-only*; 默认值：**none**) | 应用基于 MAC 的服务 VLAN 转换的帧类型。 |
| **allow-mac-based-customer-vlan-assignment-for** (*all-frames \| none \|* *tagged-frame-only \| untagged-and-priority-tagged-frame-only*; 默认值：**none**) | 应用基于 MAC 的客户 VLAN 转换的帧类型。 |
| **default-customer-pcp** (*0..7*; 默认值：**0**) | 端口的默认客户 PCP。 |
| **default-service-pcp** (*0..7*; 默认值：**0**) | 端口的默认服务 PCP。 |
| **pcp-propagation-for-initial-pcp** (*yes \| no*; 默认值：**no**) | 启用或禁用入口处初始 PCP 分配的 PCP 传播。如果端口 vlan-type 是边缘端口，则服务 PCP 从客户 PCP 复制。如果端口 vlan-type 是网络端口，则客户 PCP 从服务 PCP 复制。 |
| **filter-untagged-frame** (*yes \| no*; 默认值：**no**) | 是否过滤端口上的未标记帧。 |
| **filter-priority-tagged-frame** (*yes \| no*; 默认值：**no**) | 是否过滤端口上带优先级的标记帧。 |
| **filter-tagged-frame** (*yes \| no*; 默认值：**no**) | 是否过滤端口上的标记帧。 |

| 属性 | 描述 |
| :-- | :-- |
| **egress-vlan-tag-table-lookup-key** (*according-to-bridge-type \| egress-vid*; 默认值：**egress-vid**) | 出口 VLAN 表（VLAN 标记）查找：egress-vid - 当配置边缘端口时，查找 VLAN ID 为 CVID；当配置网络端口时，查找 VLAN ID 为 SVID。according-to-bridge-type - 当配置客户 VLAN 桥接时，查找 VLAN ID 为 CVID；当配置服务 VLAN 桥接时，查找 VLAN ID 为 SVID。在服务 VLAN 桥接中，边缘端口的客户标签不被修改。 |
| **egress-vlan-mode** (*tagged \| unmodified \| untagged*; 默认值：**unmodified**) | 端口上的出口 VLAN 标记操作。 |
| **egress-pcp-propagation** (*yes \| no*; 默认值：**no**) | 启用或禁用出口 PCP 传播。如果端口 vlan-type 是边缘端口，则服务 PCP 从客户 PCP 复制。如果端口 vlan-type 是网络端口，则客户 PCP 从服务 PCP 复制。 |

| 属性 | 描述 |
| :-- | :-- |
| **ingress-mirror-to** (*mirror0 \| mirror1 \| none*; 默认值：**none**) | 用于基于端口的入口镜像的分析端口。 |
| **ingress-mirroring-according-to-vlan** (*yes \| no*; 默认值：**no**) |  |
| **egress-mirror-to** (*mirror0 \| mirror1 \| none*; 默认值：**none**) | 用于基于端口的出口镜像的分析端口。 |

| 属性 | 描述 |
| :-- | :-- |
| **qos-scheme-precedence** (*da-based \| dscp-based \| ingress-acl-based \| pcp-based \| protocol-based \| sa-based \| vlan-based*; 默认值：**pcp-based, sa-based, da-based, dscp-based, protocol-based, vlan-based**) | 指定在端口入口处应用的 QoS 分配方案。da-baseddscp-basedingress-acl-basedpcp-basedprotocol-basedsa-basedvlan-based |
| **pcp-or-dscp-based-qos-change-dei** (*yes \| no*; 默认值：**no**) | 在端口上启用或禁用基于 PCP 或 DSCP 的 DEI 更改。 |
| **pcp-or-dscp-based-qos-change-pcp** (*yes \| no*; 默认值：**no**) | 在端口上启用或禁用基于 PCP 或 DSCP 的 PCP 更改。 |
| **pcp-or-dscp-based-qos-change-dscp** (*yes \| no*; 默认值：**no**) | 在端口上启用或禁用基于 PCP 或 DSCP 的 DSCP 更改。 |
| **dscp-based-qos-dscp-to-dscp-mapping** (*yes \| no*; 默认值：**yes**) | 在端口上启用或禁用 DSCP 到内部 DSCP 的映射。 |
| **pcp-based-qos-drop-precedence-mapping** (*PCP/DEI范围:丢弃优先级*; 默认值：**0-15:green**) | PCP/DEI 到丢弃优先级（drop \| green \| red \| yellow）映射的丢弃优先级新值。允许多个映射，用逗号分隔，例如 "0-7:yellow,8-15:red"。 |
| **pcp-based-qos-dscp-mapping** (*PCP/DEI范围:DEI*; 默认值：**0-15:0**) | PCP/DEI 到 DSCP（0..63）映射的 DSCP 新值。允许多个映射，用逗号分隔，例如 "0-7:25,8-15:50"。 |
| **pcp-based-qos-dei-mapping** (*PCP/DEI范围:DEI*; 默认值：**0-15:0**) | PCP/DEI 到 DEI（0..1）映射的 DEI 新值。允许多个映射，用逗号分隔，例如 "0-7:0,8-15:1"。 |
| **pcp-based-qos-pcp-mapping** (*PCP/DEI范围:DEI*; 默认值：**0-15:0**) | PCP/DEI 到 PCP（0..7）映射的 PCP 新值。允许多个映射，用逗号分隔，例如 "0-7:3,8-15:4"。 |
| **pcp-based-qos-priority-mapping** (*PCP/DEI范围:DEI*; 默认值：**0-15:0**) | PCP/DEI 到优先级（0..15）映射的内部优先级新值。允许多个映射，用逗号分隔，例如 "0-7:5,8-15:15"。 |

| 属性 | 描述 |
| :-- | :-- |
| **priority-to-queue** (*优先级范围:队列*; 默认值：**0-15:0,1:1,2:2,3:3**) | 每个端口的内部优先级（0..15）到队列（0..7）的映射。 |
| **per-queue-scheduling** (*调度类型:权重*; 默认值：**wrr-group0:1,wrr-group0:2,wrr-group0:4,wrr-group0:8,wrr-group0:16,wrr-group0:32,** **wrr-group0:64,wrr-group0:128**) | 设置端口对每个队列组使用严格或加权轮询策略进行流量整形；每个队列用逗号分隔。 |

| 属性 | 描述 |
| :-- | :-- |
| **ingress-customer-tpid-override** (*yes \| no*; 默认值：**!ingress-customer-tpid-override**) **ingress-customer-tpid** (*0..10000*; 默认值：**0x8100**) | 入口客户 TPID 覆盖允许接受具有自定义客户标签 TPID 的特定帧。默认值适用于 802.1Q 帧的标签。 |
| **egress-customer-tpid-override** (*yes \| no*; 默认值：**!egress-customer-tpid-override**) **egress-customer-tpid** (*0..10000*; 默认值：**0x8100**) | 出口客户 TPID 覆盖允许对带有客户标签的出口帧进行自定义标识。默认值适用于 802.1Q 帧的标签。 |
| **ingress-service-tpid-override** (*yes \| no*; 默认值：**!ingress-service-tpid-override**) **ingress-service-tpid** (*0..10000*; 默认值：**0x88A8**) | 入口服务 TPID 覆盖允许接受具有自定义服务标签 TPID 的特定帧。默认值适用于 802.1AD 帧的服务标签。 |
| **egress-service-tpid-override** (*yes \| no*; 默认值：**!egress-service-tpid-override**) **egress-service-tpid** (*0..10000*; 默认值：**0x88A8**) | 出口服务 TPID 覆盖允许对带有服务标签的出口帧进行自定义标识。默认值适用于 802.1AD 帧的服务标签。 |

| 属性 | 描述 |
| :-- | :-- |
| **custom-drop-counter-includes** (*计数器*; 默认值：**none**) | 自定义包含以计数交换机端口 custom-drop-packet 计数器的丢弃数据包。device-loopbackfdb-hash-violationexceeded-port-learn-limitationdynamic-station-movestatic-station-moveufdb-source-drophost-source-dropunknown-hostingress-vlan-filtered |
| **queue-custom-drop-counter0-includes** (*计数器*; 默认值：**none**) | 自定义包含以计数交换机端口 tx-queue-custom0-drop-packet 和 tx-queue-custom0-drop-byte 计数器的丢弃数据包和字节。redyellowgreenqueue0...queue7 |
| **queue-custom-drop-counter1-includes** (*计数器*; 默认值：**none**) | 自定义包含以计数交换机端口 tx-queue-custom1-drop-packet 和 tx-queue-custom1-drop-byte 计数器的丢弃数据包和字节。redyellowgreenqueue0...queue7 |
| **policy-drop-counter-includes** (*计数器*; 默认值：**none**) | 自定义包含以计数交换机端口 policy-drop-packet 计数器的丢弃数据包。ingress-policingingress-aclegress-policingegress-acl |

## 转发数据库

---

### 单播 FDB

单播转发数据库支持最多 16K 条 MAC 条目。

**子菜单：** `/interface/ethernet/switch/unicast-fdb`

| 属性 | 描述 |
| :-- | :-- |
| **action** (*操作*; 默认值：**forward**) | UFDB 条目的操作：dst-drop - 当数据包的目标 MAC 与条目匹配时，数据包被丢弃。dst-redirect-to-cpu - 当数据包的目标 MAC 与条目匹配时，数据包被重定向到 CPU。forward - 数据包被转发。src-and-dst-drop - 当数据包的源 MAC 或目标 MAC 与条目匹配时，数据包被丢弃。src-and-dst-redirect-to-cpu - 当数据包的源 MAC 或目标 MAC 与条目匹配时，数据包被重定向到 CPU。src-drop - 当数据包的源 MAC 与条目匹配时，数据包被丢弃。src-redirect-to-cpu - 当数据包的源 MAC 与条目匹配时，数据包被重定向到 CPU。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 启用或禁用单播 FDB 条目。 |
| **isolation-profile** (*community1 \| community2 \| isolated \| promiscuous*; 默认值：**promiscuous**) | MAC 层隔离配置文件。 |
| **mac-address** (*MAC 地址*) | 当目标 MAC 或源 MAC 与条目匹配时，操作命令应用于数据包。 |
| **mirror** (*yes \| no*; 默认值：**no**) | 启用或禁用基于源 MAC 或目标 MAC 的镜像。 |
| **port** (*端口*) | 单播 FDB 条目的匹配端口。 |
| **qos-group** (*none*; 默认值：**none**) | 从 QoS 组菜单定义的 QoS 组。 |
| **svl** (*yes \| no*; 默认值：**no**) | 单播 FDB 学习模式：共享 VLAN 学习（svl） - 学习/查找基于 MAC 地址 - 而非 VLAN ID。独立 VLAN 学习（ivl） - 学习/查找基于 MAC 地址和 VLAN ID。 |
| **vlan-id** (*0..4095*) | 单播 FDB 查找/学习 VLAN ID。 |

### 组播 FDB

CRS125 交换芯片支持 MFDB 中最多 1024 个条目用于组播转发。对于每个组播数据包，在 MFDB 中执行目标 MAC 或目标 IP 查找。MFDB 条目不会自动学习，只能配置。

**子菜单：** `/interface/ethernet/switch/multicast-fdb`

| 属性 | 描述 |
| :-- | :-- |
| **address** (*X.X.X.X \| XX:XX:XX:XX:XX:XX*) | 匹配组播数据包的 IP 地址或 MAC 地址。 |
| **bypass-vlan-filter** (*yes \| no*; 默认值：**no**) | 允许匹配的组播数据包绕过 VLAN 过滤。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 启用或禁用组播 FDB 条目。 |
| **ports** (*端口*) | 组播流量的成员端口。 |
| **qos-group** (*none*; 默认值：**none**) | 从 QoS 组菜单定义的 QoS 组。 |
| **svl** (*yes \| no*; 默认值：**no**) | 组播 FDB 学习模式：共享 VLAN 学习（svl） - 学习/查找基于 MAC 地址 - 而非 VLAN ID。独立 VLAN 学习（ivl） - 学习/查找基于 MAC 地址和 VLAN ID。 |
| **vlan-id** (*0..4095*; 默认值：**0**) | 组播 FDB 查找 VLAN ID。如果 VLAN 学习模式为 IVL，则 VLAN ID 为查找 ID，否则 VLAN ID = 0。 |

### 保留 FDB

Cloud Router Switch 支持 256 个 RFDB 条目。每个 RFDB 条目可以存储一个带有特定命令的二层单播或组播 MAC 地址。

**子菜单：** `/interface/ethernet/switch/reserved-fdb`

| 属性 | 描述 |
| :-- | :-- |
| **action** (*copy-to-cpu \| drop \| forward \| redirect-to-cpu*; 默认值：**forward**) | RFDB 条目的操作：copy-to-cpu - 当数据包的目标 MAC 与条目匹配时，数据包被复制到 CPU。drop - 当数据包的目标 MAC 与条目匹配时，数据包被丢弃。forward - 当数据包的目标 MAC 与条目匹配时，数据包被转发。redirect-to-cpu - 当数据包的目标 MAC 与条目匹配时，数据包被重定向到 CPU。 |
| **bypass-ingress-port-policing** (*yes \| no*; 默认值：**no**) | 允许匹配的数据包绕过入口端口策略器。 |
| **bypass-ingress-vlan-filter** (*yes \| no*; 默认值：**no**) | 允许匹配的数据包绕过 VLAN 过滤。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 启用或禁用保留 FDB 条目。 |
| **mac-address** (*MAC 地址*; 默认值：**00:00:00:00:00:00**) | 保留 FDB 条目的匹配 MAC 地址。 |
| **qos-group** (*none*; 默认值：**none**) | 从 QoS 组菜单定义的 QoS 组。 |

## VLAN

---

### VLAN 表

VLAN 表支持 4096 个 VLAN 条目，用于存储 VLAN 成员信息以及其他 VLAN 信息，如 QoS、隔离、强制 VLAN、学习和镜像。

**子菜单：** `/interface/ethernet/switch/vlan`

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*yes \| no*; 默认值：**no**) | 指示 VLAN 条目是否被禁用。只有启用的条目才会应用于查找过程和转发决策。 |
| **flood** (*yes \| no*; 默认值：**no**) | 启用或禁用每个 VLAN 的强制 VLAN 泛洪。如果启用该功能，则忽略 UFDB 或 MFDB 中目标 MAC 查找的结果，并强制数据包在 VLAN 中泛洪。 |
| **ingress-mirror** (*yes \| no*; 默认值：**no**) | 启用每个 VLAN 的入口镜像以支持