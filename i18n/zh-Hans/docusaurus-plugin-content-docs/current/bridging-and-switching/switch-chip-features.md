# 交换芯片特性

> 本页介绍 MikroTik RouterOS 交换芯片特性，详细说明各型号支持的端口交换和端口镜像等功能，以及带宽控制和 VLAN 配置方面的限制。

# 交换芯片特性

---

Routerboard 上有多种类型的交换芯片，它们具有不同的功能集。

:::info
Cloud Router Switch (CRS) 系列设备内置了高度先进的交换芯片。它们支持多种多样的功能。对于采用 Marvell Prestera 交换芯片的 MikroTik 设备（例如 CRS3xx），请参阅 [Marvell Prestera 交换芯片特性](./marvell-prestera-switch-chip-features.md) 手册。有关 CRS1xx/CRS2xx 系列设备交换芯片功能的更多详细信息，请查看 [CRS1xx/CRS2xx 系列交换机](./crs1xx-and-2xx-series-switches.md) 手册。
:::

| 交换芯片 | 端口交换 | 端口镜像 | TX 限速¹ | RX 限速¹ | 主机表 | VLAN 表² | 规则表 |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| 88E6393X | ✓ | ✓ | ✓ | ✓ | 最多 16K | 最多 4K | 最多 256 条规则 |
| 88E6191X, 88E6190 | ✓ | ✓ | ✓ | ✓ | 最多 16K | 最多 4K | ✗ |
| MT7621, MT7531, RTL8367 | ✓ | ✓ | ✓ | ✓ | 最多 2K | 最多 4K | ✗ |
| EN7523 | ✓ | ✓ | ✓ | ✓ | 最多 1K | 最多 4K | ✗ |
| QCA8337, Atheros8327 | ✓ | ✓ | ✓ | ✓ | 最多 2K | 最多 4K | 最多 92 条规则 |
| Atheros8316 | ✓ | ✓ | ✓ | ✗ | 最多 2K | 最多 4K | 最多 32 条规则 |
| Atheros8227 | ✓ | ✓ | ✓ | ✗ | 最多 1K | 最多 4K | ✗ |
| Atheros7240 | ✓ | ✓ | ✓ | ✗ | 最多 2K | 16 | ✗ |
| ICPlus175D | ✓ | ✓ | ✗ | ✗ | 最多 2K | ✗ | ✗ |
| IPQ-PPE | ✓ | ✗ | ✗ | ✗ | 最多 2K | ✗ | ✗ |
| PIPE 98PX1012, QCA8386 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

1. 对于 RTL8367, 88E6393X, 88E6191X, 88E6190, MT7621, MT7531 和 EN7523，Tx/Rx 速率限制可以通过 `/interface/ethernet/switch/port` 菜单中的 `egress-rate` 和 `ingress-rate` 属性更改。对于 QCA8337, Atheros8327, Atheros8316, Atheros8227 和 Atheros7240，Tx/Rx 速率限制可以通过 `/interface/ethernet` 菜单中的 `bandwidth` 属性更改，更多详情请参阅 [以太网手册](../wired-connections/ethernet.md)。
2. 对于 88E6393X, 88E6191X, 88E6190, MT7621, MT7531, EN7523, RTL8367 交换芯片，VLAN 表通过 [桥接 VLAN 硬件过滤](index.md#bridge-vlan-filtering) 使用 `/interface/bridge` 菜单配置。对于其他支持 VLAN 表的交换机，请参阅 [VLAN 表](./switch-chip-features.md#vlan-table) 并使用 `/interface/ethernet/switch/vlan` 菜单配置 VLAN 表。

| RouterBoard | 交换芯片描述 |
| :-- | :-- |
| **MA53UG+HbeH (hAP be³ Media)** | QCA8386 (ether2-ether5) |
| **C52iG-5HaxD2HaxD-TC (hAP ax²), C53UiG+5HPaxD2HPaxD (hAP ax³), Chateau ax 系列** | IPQ-PPE (ether1-ether5) |
| **cAPGi-5HaxD2HaxD (cAP ax)** | IPQ-PPE (ether1-ether2) |
| **L009 系列** | 88E6190 (ether2-ether8, sfp1) |
| **RB5009 系列** | 88E6393X (ether1-ether8, sfp-sfpplus1) |
| **CCR2004-16G-2S+** | 88E6191X (ether1-ether8); 88E6191X (ether9-ether16); |
| **RB4011iGS+** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); |
| **RB1100AHx4** | RTL8367 (ether1-ether5); RTL8367 (ether6-ether10); RTL8367 (ether11-ether13) |
| **L41G-2axD (hAP ax lite)** | MT7531 (ether1-ether4) |
| **RB750Gr3 (hEX), RB760iGS (hEX S)** | MT7621 (ether1-ether5) |
| **E50UG (hEX Refresh)** | EN7523 (ether2-ether5) |
| **RBM33G** | MT7621 (ether1-ether3) |
| **RB3011 系列** | QCA8337 (ether1-ether5); QCA8337 (ether6-ether10) |
| **RB OmniTik ac 系列** | QCA8337 (ether1-ether5) |
| **RBwsAP-5Hac2nD (wsAP ac lite)** | Atheros8227 (ether1-ether3) |
| **RB941-2nD (hAP lite)** | Atheros8227 (ether1-ether4) |
| **RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB750r2 (hEX lite); RB750UPr2 (hEX PoE lite); RB750P-PBr2 (PowerBox); RB750P r2; RBOmniTikU-5HnDr2 (OmniTIK 5); RBOmniTikUPA-5HnDr2 (OmniTIK 5 PoE)** | Atheros8227 (ether1-ether5) |
| **RB750Gr2 (hEX); RB962UiGS-5HacT2HnT (hAP ac); RB960PGS (hEX PoE); RB960PGS-PB (PowerBox Pro)** | QCA8337 (ether1-ether5) |
| **RB953GS** | Atheros8327 (ether1-ether3+sfp1) |
| **RB850Gx2** | Atheros8327 (ether1-ether5) 其中 ether1 可选 |
| **RB2011 系列** | Atheros8327 (ether1-ether5+sfp1); Atheros8227 (ether6-ether10) |
| **RB750GL; RB751G-2HnD; RB951G-2HnD; RBD52G-5HacD2HnD (hAP ac²), RBD53iG-5HacD2HnD (hAP ac³), RBD53GR-5HacD2HnD&R11e-LTE6 (hAP ac³ LTE6 kit), RBD53G-5HacD2HnD-TC&EG12-EA (Chateau LTE12)** | Atheros8327 (ether1-ether5) |
| **RBcAPGi-5acD2nD (cAP ac), RBwAPGR-5HacD2HnD (wAP R ac 和 wAP ac LTE 系列), RBwAPG-5HacD2HnD (wAP ac), RBD25G-5HPacQD2HPnD (Audience), RBD25GR-5HPacQD2HPnD&R11e-LTE6 (Audience LTE6 kit),** | Atheros8327 (ether1-ether2) |
| **RBD22UGS-5HPacD2HnD (mANTBox 52 15s)** | Atheros8327 (ether1-sfp1) |
| **RB1100AH** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **RB1100AHx2** | Atheros8327 (ether1-ether5); Atheros8327 (ether6-ether10) |
| **CCR1009-8G-1S-1S+; CCR1009-8G-1S** | Atheros8327 (ether1-ether4) |
| **RB493G** | Atheros8316 (ether1+ether6-ether9); Atheros8316 (ether2-ether5) |
| **RB435G** | Atheros8316 (ether1-ether3) 其中 ether1 可选 |
| **RB450G** | Atheros8316 (ether1-ether5) 其中 ether1 可选 |
| **RB450Gx4** | Atheros8327 (ether1-ether5) |
| **RB433GL** | Atheros8327 (ether1-ether3) |
| **RB750G** | Atheros8316 (ether1-ether5) |
| **RB1200** | Atheros8316 (ether1-ether5) |
| **RB1100** | Atheros8316 (ether1-ether5); Atheros8316 (ether6-ether10) |
| **DISC Lite5** | Atheros8227 (ether1) |
| **RBmAP2nD** | Atheros8227 (ether1-ether2) |
| **RBmAP2n** | Atheros7240 (ether1-ether2) |
| **RB750** | Atheros7240 (ether2-ether5) |
| **RB750UP** | Atheros7240 (ether2-ether5) |
| **RB751U-2HnD** | Atheros7240 (ether2-ether5) |
| **RB951-2n** | Atheros7240 (ether2-ether5) |
| **RB951Ui-2HnD** | Atheros8227 (ether1-ether5) |
| **RB433 系列** | ICPlus175D (ether2-ether3); 旧型号使用 ICPlus175C |
| **RB450** | ICPlus175D (ether2-ether5); 旧型号使用 ICPlus175C |
| **RB493 系列** | ICPlus178C (ether2-ether9) |
| **RB816** | ICPlus178C (ether1-ether16) |

命令行配置位于 switch 菜单下。此菜单包含系统中所有交换芯片的列表以及一些子菜单。

```ros
[admin@MikroTik] > /interface/ethernet/switch/print 
Flags: I - invalid 
 #   NAME         TYPE             MIRROR-SOURCE       MIRROR-TARGET       SWITCH-ALL-PORTS
 0   switch1      Atheros-8327     none                none               
 1   switch2      Atheros-8227     none                none               
```

根据交换机类型的不同，可用的配置功能也会有所不同。

## 功能

---

### 端口交换

要在非 CRS 系列设备上设置端口交换，请查看 [桥接硬件卸载](index.md#bridge-hardware-offloading) 页面。

:::warning
RouterOS v6.41 及更新版本中的端口交换是使用桥接配置完成的。在 RouterOS v6.41 之前，端口交换是使用 master-port 属性完成的。
:::

#### 全部端口交换功能

RB450G/RB435G/RB850Gx2 设备上的 Ether1 端口具有一项功能，允许将其从默认交换组中移除/添加。此设置可在 `/interface/ethernet/switch` 菜单中找到。默认情况下，ether1 端口将包含在交换组中。

![Switch 4](https://manual.mikrotik.com/docs/bridging-and-switching/img/switch-chip-features-01.webp)

| 属性 | 描述 |
| :-- | :-- |
| **switch-all-ports** (no*\| yes*; 默认值: **yes**) | 仅在 RB450G/RB435G/RB850Gx2 设备上更改 ether1 交换组。<code>yes</code> - ether1 是交换机的一部分，支持交换分组以及所有其他高级 Atheros8316/Atheros8327 功能，包括扩展统计信息（<code>`/interface/ethernet/print` stats</code>）。<code>no</code> - ether1 不是交换机的一部分，实际上使其成为一个独立的以太网端口，从而在桥接和路由模式下提高其到其他端口的吞吐量，但移除了此端口上的交换功能。 |

### 端口镜像

端口镜像允许交换机复制进出某个端口（`mirror-source`）的所有流量，并将这些复制的帧发送到另一个端口（`mirror-target`）。此功能可用于轻松设置一个“分路”设备，接收进出某个特定端口的所有流量。请注意，`mirror-source` 和 `mirror-target` 端口必须属于同一交换机（请参阅 `/interface/ethernet` 菜单中哪个端口属于哪个交换机）。此外，mirror-target 可以具有特殊的 `cpu` 值，这意味着镜像的数据包应发送到交换芯片的 CPU 端口。端口镜像独立于已设置或未设置的交换组进行。

**子菜单:** `/interface/ethernet/switch`

| 属性 | 描述 |
| :-- | :-- |
| **mirror-source** (*name \| none*; 默认值: **none**) | 选择单个镜像源端口。入站和出站流量将被发送到 `mirror-target` 端口。请注意，`mirror-target` 端口必须属于同一交换机（请参阅 `/interface/ethernet` 菜单中哪个端口属于哪个交换机）。 |
| **mirror-target** (*name \| none \| cpu*; 默认值: **none**) | 选择单个镜像目标端口。来自 `mirror-source` 和 `mirror`（请参阅规则和主机表中的属性）的镜像数据包将被发送到所选端口。 |
| **mirror-egress-target** (*name \| none*; 默认值: **none**) | 选择单个镜像出站目标端口，仅在 **88E6393X**、**88E6191X** 和 **88E6190** 交换芯片上可用。来自 `mirror-egress`（请参阅端口菜单中的属性）的镜像数据包将被发送到所选端口。 |

**子菜单:** `/interface/ethernet/switch/rule`

| 属性 | 描述 |
| :-- | :-- |
| **mirror** (*no \| yes*; 默认值: **no**) | 是否将数据包副本发送到 `mirror-target` 端口。 |
| **mirror-ports** (*name*; 默认值: ) | 选择多个镜像目标端口，仅在 **88E6393X** 交换芯片上可用。ACL 规则中匹配的数据包将被复制并发送到所选端口。 |

**子菜单:** `/interface/ethernet/switch/host`

| 属性 | 描述 |
| :-- | :-- |
| **mirror** (*no \| yes*; 默认值: **no**) | 是否将具有匹配 MAC 目的地址（对于 CRS3xx 系列交换机为匹配目的或源地址）的帧副本发送到 `mirror-target` 端口。 |

**子菜单:** `/interface/ethernet/switch/port`

| 属性 | 描述 |
| :-- | :-- |
| **mirror-egress** (*no \| yes*; 默认值: **no**) | 是否将出站数据包副本发送到 `mirror-egress-target` 端口，仅在 **88E6393X**、**88E6191X** 和 **88E6190** 交换芯片上可用。 |
| **mirror-ingress** (*no \| yes*; 默认值: **no**) | 是否将入站数据包副本发送到 `mirror-ingress-target` 端口，仅在 **88E6393X**、**88E6191X** 和 **88E6190** 交换芯片上可用。 |
| **mirror-ingress-target** (*name \| none*; 默认值: **none**) | 选择单个镜像入站目标端口，仅在 **88E6393X**、**88E6191X** 和 **88E6190** 交换芯片上可用。来自 `mirror-ingress` 的镜像数据包将被发送到所选端口。 |

端口镜像配置示例：

```ros
/interface/ethernet/switch
set switch1 mirror-source=ether2 mirror-target=ether3
```

:::danger
如果您将 mirror-source 设置为具有至少两个交换芯片的设备上的一个以太网端口，并且这些 mirror-source 端口位于单个桥接中，而两个交换芯片的 mirror-target 都设置为将数据包发送到 CPU，则会导致环路，这可能使您的设备无法访问。
:::

### 端口设置

此菜单下的属性用于为支持 VLAN 表的交换芯片配置 VLAN 交换和过滤选项。这些属性仅适用于支持 VLAN 表的交换芯片。请检查 [交换芯片特性](./switch-chip-features.md) 表以确认您的设备支持此功能。

:::danger
入站流量被视为发送**进**某个端口的流量；该端口有时称为**入站端口**。出站流量被视为发送**出**某个端口的流量；该端口有时称为**出站端口**。区分它们对于正确设置 VLAN 过滤非常重要，因为某些属性仅适用于入站或出站流量。
:::

| 属性 | 描述 |
| :-- | :-- |
| **vlan-mode** (*check \| disabled \| fallback \| secure*; 默认值: **disabled**) | 更改针对入站流量在 [VLAN 表](./switch-chip-features.md#vlan-table) 中的 VLAN 查找机制。<code>disabled</code> - 完全禁用对入站流量的 VLAN 表检查。在入站端口上设置时不会丢弃任何流量。<code>fallback</code> - 检查入站流量的带标签流量是否在 VLAN 表中，并转发所有未标记流量。如果入站流量带标签且在 VLAN 表中未找到相应 VLAN ID 的出站端口，则丢弃流量。如果在 VLAN 表中未找到 VLAN ID，则转发流量。用于仅允许特定端口上的已知 VLAN。<code>check</code> - 检查入站流量的带标签流量是否在 VLAN 表中，并丢弃所有未标记流量。如果入站流量带标签且在 VLAN 表中未找到相应 VLAN ID 的出站端口，则丢弃流量。<code>secure</code> - 检查入站流量的带标签流量是否在 VLAN 表中，并丢弃所有未标记流量。入站和出站端口都必须在 VLAN 表中找到相应的 VLAN ID，否则丢弃流量。 |
| **vlan-header** (*add-if-missing \| always-strip \| leave-as-is*; 默认值: **leave-as-is**) | 设置端口对出站流量执行的操作。<code>add-if-missing</code> - 在出站流量上添加 VLAN 标签，并使用入站端口的 default-vlan-id。应用于 trunk 端口。<code>always-strip</code> - 在出站流量上移除 VLAN 标签。应用于 access 端口。<code>leave-as-is</code> - 不在出站流量上添加或移除 VLAN 标签。应用于 hybrid 端口。 |
| **default-vlan-id** (*auto \| integer: 0..4095*; 默认值: **auto**) | 在端口上的所有未标记入站流量上添加具有指定 VLAN ID 的 VLAN 标签。应与端口上的 vlan-header 设置为 `always-strip` 一起使用，以将端口配置为 access 端口。对于 hybrid 端口，default-vlan-id 用于标记未标记流量。如果两个端口具有相同的 default-vlan-id，则不添加 VLAN 标签，因为交换芯片假定流量在 access 端口之间转发。 |

:::warning
在 **QCA8337** 和 **Atheros8327** 交换芯片上，应使用默认的 `vlan-header=leave-as-is` 属性。交换芯片将通过使用 `default-vlan-id` 属性来确定哪些端口是 access 端口。`default-vlan-id` 应仅在 access/hybrid 端口上使用，以指定未标记入站流量分配给哪个 VLAN。
:::

### VLAN 表

VLAN 表为具有特定 802.1Q 标签的数据包指定了某些转发规则。这些规则的优先级高于使用 [桥接硬件卸载](index.md#bridge-hardware-offloading) 功能配置的交换组。基本上，该表包含将特定 VLAN 标签 ID 映射到一个或多个端口组的条目。带有 VLAN 标签的数据包通过相应表条目中设置的一个或多个端口离开交换芯片。控制如何处理带 VLAN 标签的数据包的确切逻辑由 `vlan-mode` 参数控制，该参数可在每个交换机端口上更改。

基于 VLAN ID 的转发会考虑动态学习或手动添加到主机表中的 MAC 地址。QCA8337 和 Atheros8327 交换芯片还支持独立 VLAN 学习（IVL），该学习基于 MAC 地址和 VLAN ID 两者进行，从而允许同一 MAC 在多个 VLAN 中使用。

没有 VLAN 标签的数据包被视为具有端口 `default-vlan-id` 的 VLAN 标签。如果配置了 `vlan-mode=check` 或 `vlan=mode=secure`，要转发没有 VLAN 标签的数据包，您必须根据 `default-vlan-id` 向 VLAN 表添加具有相同 VLAN ID 的条目。

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*no \| yes*; 默认值: **no**) | 启用或禁用交换机 VLAN 条目。 |
| **independent-learning** (no*\| yes*; 默认值: **yes**) | 是否使用共享 VLAN 学习（SVL）或独立 VLAN 学习（IVL）。 |
| **ports** (*name*; 默认值: **none**) | 相应 VLAN 的接口成员列表。此设置接受逗号分隔的值。例如：`ports=ether1,ether2`。 |
| **switch** (*name*; 默认值: **none**) | 相应 VLAN 条目所针对的交换机名称。 |
| **vlan-id** (*integer: 0..4095*; 默认值:) | 特定交换机端口配置的 VLAN ID。 |

:::warning
具有 **MT7621**、**MT7531**、**EN7523, RTL8367**、**88E6393X**、**88E6191X**、**88E6190** 交换芯片的设备在 RouterOS v7 中支持 [硬件卸载的 vlan-filtering](index.md#bridge-vlan-filtering)。`/interface/ethernet/switch` 菜单上的 VLAN 相关配置不可用。
:::

#### VLAN 转发

`vlan-mode` 和 `vlan-header` 以及 VLAN 表可用于配置 VLAN 标记、去标记和过滤。多种组合是可能的，每种组合实现不同的结果。下表列出了对于每种 VLAN 模式，当在入站端口上接收到特定流量时，将通过出站端口发送何种类型的流量。

**注意：**

- **L** - `vlan-header` 设置为 `leave-as-is`
- **S** - `vlan-header` 设置为 `always-strip`
- **A** - `vlan-header` 设置为 `add-if-missing`
- **U** - 发送未标记流量
- **T** - 发送带标签流量，标签已存在于入站端口上
- **TA** - 发送带标签流量，标签在入站端口上添加
- **DI** - 由于 vlan-mode 中选择的模式，流量在入站端口被丢弃
- **DE** - 由于在 VLAN 表中未找到出站端口，流量在出站端口被丢弃
- **VID 匹配** - 入站流量的 VLAN 标签中的 VLAN ID 存在于 VLAN 表中
- **端口匹配** - 入站端口存在于 VLAN 表中相应的 VLAN ID 下

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = disabled* | 出站端口不在 VLAN 表中 |  |  | 出站端口在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未标记流量 | U | U | TA | U | U | TA |
| 带标签流量；无 VID 匹配 | T | U | T |  |  |  |
| 带标签流量；VID 匹配；无端口匹配 | T | U | T | T | U | T |
| 带标签流量；VID 匹配；端口匹配 | T | U | T | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = fallback* | 出站端口不在 VLAN 表中 |  |  | 出站端口在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未标记流量 | U | U | TA | U | U | TA |
| 带标签流量；无 VID 匹配 | T | U | T |  |  |  |
| 带标签流量；VID 匹配；无端口匹配 | DE | DE | DE | T | U | T |
| 带标签流量；VID 匹配；端口匹配 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = check* | 出站端口不在 VLAN 表中 |  |  | 出站端口在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未标记流量 |  |  |  |  |  |  |
| 带标签流量；无 VID 匹配 | DI | DI | DI |  |  |  |
| 带标签流量；VID 匹配；无端口匹配 | DE | DE | DE | T | U | T |
| 带标签流量；VID 匹配；端口匹配 | DE | DE | DE | T | U | T |

|  |  |  |  |  |  |  |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| *VLAN 模式 = secure* | 出站端口不在 VLAN 表中 |  |  | 出站端口在 VLAN 表中 |  |  |
|  | L | S | A | L | S | A |
| 未标记流量 |  |  |  |  |  |  |
| 带标签流量；无 VID 匹配 | DI | DI | DI |  |  |  |
| 带标签流量；VID 匹配；无端口匹配 | DI | DI | DI | DI | DI | DI |
| 带标签流量；VID 匹配；端口匹配 | DE | DE | DE | T | U | T |

:::warning
上表适用于更高级的配置，并用于再次检查您对每个 VLAN 相关属性将如何处理数据包的理解。
:::

### 主机表

主机表表示交换芯片内部的 MAC 地址到端口的映射。它可以包含两种条目：动态和静态。动态条目会自动添加。这也称为学习过程：当交换芯片从某个端口接收到数据包时，它会将数据包的源 MAC 地址和接收数据包的端口添加到主机表中，因此当具有相同目的 MAC 地址的数据包到达时，它知道应将数据包转发到哪个端口。如果目的 MAC 地址不在主机表中（所谓的未知单播流量），则它将数据包转发到组中的所有端口。动态条目大约需要 5 分钟超时。学习仅在配置为交换组一部分的端口上启用，因此如果您未设置端口交换，则不会看到动态条目。此外，您可以添加静态条目，如果已存在具有相同 MAC 地址的动态条目，则静态条目将接管动态条目。由于端口交换是使用具有硬件卸载的桥接配置的，因此在一个表（桥接主机或交换机主机）上创建的任何静态条目将作为动态条目出现在另一个表中。在交换机主机表上添加静态条目将提供对通过以下参数控制的更多功能的访问：

| 属性 | 描述 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; 默认值: **no**) | 是否将具有匹配 MAC 目的地址（对于 CRS3xx 系列交换机为匹配目的或源地址）的帧副本发送到交换机 CPU 端口。 |
| **drop** (*no \| yes*; 默认值: **no**) | 是否丢弃在特定端口上接收到的具有匹配 MAC 源地址的帧（对于 CRS3xx 系列交换机为匹配目的或源地址）。 |
| **mac-address** (*MAC;* 默认值: **00:00:00:00:00:00**) | 主机的 MAC 地址。 |
| **mirror** (*no \| yes*; 默认值: **no**) | 是否将具有匹配 MAC 目的地址（对于 CRS3xx 系列交换机为匹配目的或源地址）的帧副本发送到 `mirror-target` 端口。 |
| **ports** (*name*; 默认值: **none**) | 接口名称，静态 MAC 地址可以映射到多个端口，包括交换机 CPU 端口。 |
| **redirect-to-cpu** (*no \| yes*; 默认值: **no**) | 是否将具有匹配 MAC 目的地址（对于 CRS3xx 系列交换机为匹配目的或源地址）的帧重定向到交换机 CPU 端口。 |
| **share-vlan-learned**(*no \| yes*; 默认值: **no**) | 静态主机 MAC 地址查找是否使用共享 VLAN 学习（SVL）或独立 VLAN 学习（IVL）。SVL 模式用于不支持 IVL 或 IVL 被禁用（independent-learning=no）的 VLAN 条目。 |
| **switch** (*name*; 默认值: **none**) | MAC 地址将被分配到的交换机名称。 |
| **vlan-id** (*integer: 0..4095*; 默认值:) | 静态添加的 MAC 地址条目的 VLAN ID。 |

:::warning
每个交换芯片可以存储的 MAC 地址数量有限，请参阅介绍表中的特定主机表大小。一旦主机表已满，可以采用不同的技术来应对这种情况，例如，交换机可以移除较旧的条目以腾出空间给更新的 MAC 地址（用于 QCA-8337 和 Atheros-8327 交换芯片），另一种选择是简单地忽略新的 MAC 地址，并且仅在超时过后才移除条目（用于 Atheros8316、Atheros8227、Atheros-7240、ICPlus175D 和 Realtek-RTL8367 交换芯片），最后一种选择是前两种的组合 - 只允许更新一定数量的条目，并保持其他主机部分完整直到超时（用于 MediaTek-MT7621、MT7531、EN7523 交换芯片）。这些技术无法通过配置更改。
:::

:::warning
对于 Atheros8316、Atheros8227 和 Atheros-7240 交换芯片，当交换组上至少有一个硬件卸载的桥接端口处于活动状态时，switch-cpu 端口将始终参与主机学习过程。这将导致 switch-cpu 端口从非硬件卸载接口学习 MAC 地址。当单个桥接包含硬件卸载和非硬件卸载接口时，这可能导致数据包丢失。此外，当在同一交换组上使用重复的 MAC 地址时，无论主机是否位于不同的逻辑网络上，都可能出现数据包丢失。建议仅在所有桥接端口都可以使用硬件卸载时才使用硬件卸载，或者当一个或多个桥接端口无法配置硬件卸载时，在所有交换机端口上保持禁用。
:::

:::note
**QCA-8337** 和 **Atheros-8327** 交换芯片在创建具有 `forward-reserved-addresses=no` 和 `protocol-mode=stp/rstp` 的硬件卸载桥接时，会自动将保留的多播 MAC 地址（01:80:C2:00:00:0x）添加到主机表。这些 MAC 不应由 802.1Q 兼容的桥接器转发，并且它们对于 R/STP 的正确操作至关重要。由于交换机的主机表条目数量有限，这些 MAC 地址仅分配给 VLAN 1。
:::

:::info
为确保具有这些目的 MAC 地址的数据包被正确处理：

- 交换机端口应设置为默认 VLAN 1（`default-vlan-id=auto` 或 `default-vlan-id=1`）。
- 如果显式配置了 VLAN 1，则必须使用独立 VLAN 学习（`independent-learning=yes`）。

:::

### 规则表

规则表是一个非常强大的工具，允许基于 L2、L3 和 L4 协议头字段条件进行线速数据包过滤、转发和 VLAN 标记。该菜单包含一个有序的规则列表，就像在 `/ip/firewall/filter` 中一样，因此每个数据包都会检查 ACL 规则，直到找到匹配项。如果多个规则可以匹配，则只会触发第一条规则。没有任何操作参数的规则是接受数据包的规则。

每条规则包含一个条件部分和一个操作部分。操作部分由以下参数控制：

| 属性 | 描述 |
| :-- | :-- |
| **copy-to-cpu** (*no \| yes*; 默认值: **no**) | 是否将数据包副本发送到交换机 CPU 端口。 |
| **mirror** (*no \| yes*; 默认值: **no**) | 是否将数据包副本发送到 `mirror-target` 端口。 |
| **new-dst-ports** (*name*; 默认值: **none**) | 按指定更改目的端口，允许多个端口，包括交换机 CPU 端口。空设置将丢弃数据包。当不使用该参数时，数据包将被接受。 |
| **new-vlan-id** (*integer: 0..4095*) | 将 VLAN ID 更改为指定值，或者如果不存在 VLAN 标签则添加新的 VLAN 标签（该属性仅适用于 **Atheros8316** 和 **88E6393X** 交换芯片（**注意**：对于 88E6393X 交换芯片，还需要 vlan-filtering=yes））。 |
| **new-vlan-priority** (*integer: 0..7*) | 更改 VLAN 优先级字段（优先级代码点；该属性仅适用于 **Atheros8327**、**QCA8337** 和 **Atheros8316** 交换芯片）。 |
| **rate** (*integer: 0..4294967295*) | 为匹配的流量设置入站流量限制（每秒位数），并且只能应用于前 32 个规则槽位（该属性仅适用于 **Atheros8327/QCA8337** 交换芯片）。 |
| **redirect-to-cpu** (*no \| yes*; 默认值: **no**) | 将匹配数据包的目的端口更改为交换机 CPU。 |

条件部分由其余参数控制：

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*no \| yes*; 默认值: **no**) | 启用或禁用交换机规则。 |
| **dscp** (*integer: 0..63*) | 匹配数据包的 DSCP 字段。 |
| **dst-address** (*IP 地址/掩码*) | 匹配目的 IP 地址和掩码。 |
| **dst-address6** (*IPv6 地址/掩码*) | 匹配目的 IPv6 地址和掩码。 |
| **dst-mac-address** (*MAC 地址/掩码*) | 匹配目的 MAC 地址和掩码。 |
|