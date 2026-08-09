# RouterOS 中的 MTU

> 本页介绍 MikroTik RouterOS 中的最大传输单元（MTU）配置，阐述其对网络效率与兼容性的重要性。内容涵盖不同类型的 MTU，包括二层/L3 MTU 及全帧 MTU，并详细说明各 RouterBoard 型号所支持的数值。

# RouterOS 中的 MTU

## 引言

最大传输单元（MTU）必须由管理员进行配置，以确保预期的服务和应用能够在网络中成功部署。换言之，管理员负责配置 MTU 值，使数据包大小不超过网络设备的处理能力。

最初，引入 MTU 是由于当时较高的错误率和较低的通信速度。数据流的分片允许通过仅重传损坏的分片来纠正错误，而无需重传整个数据流。此外，在调制解调器等低速连接上，传输大分片可能耗时过长，因此只有较小的分片才能实现通信。

如今，错误率已大幅降低，通信速度也显著提升。这为增大 MTU 值提供了机会。增大 MTU 可减少协议开销并降低 CPU 利用率，这主要得益于中断次数的减少。因此，出现了一些非标准帧大小：

- **Giant** 或 **Jumbo** 帧——超过标准（IEEE）以太网 MTU 的帧。
- **Baby Giant** 或 **Baby Jumbo** 帧——略大于标准（IEEE）以太网 MTU 的帧。

如今，以太网接口支持高于标准的物理 MTU 值已很常见，但这并非理所当然。还必须考虑其他网络设备的能力。例如，如果两台 RouterBoard 的以太网接口支持物理 MTU 1526，并通过以太网交换机相连，则交换机也必须支持转发这些大型以太网帧，应用才能正常运行。

## 最大传输单元

|  |  |
| :-- | :-- |
| ![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-01.webp)  |  MikroTik RouterOS 识别多种类型的 MTU：IP/三层/L3 MTU、MPLS/二层.5/L2.5 MTU、MAC/二层/L2 MTU、全帧 MTU |

### 全帧 MTU

全帧 MTU 表示特定接口实际传输的帧大小。帧校验序列（FCS）不包含在此值中，因为帧到达目的地后，以太网驱动程序会将其移除。

### MAC/二层/L2 MTU

L2MTU 表示该接口可发送的不含 MAC 头部的最大帧大小。

在 RouterOS 中，可在 `/interface` 菜单中查看 L2MTU 值。所有与 RouterBoard 相关的以太网接口、VLAN、Bridge、VPLS 及无线接口均支持 L2MTU。其中部分接口支持配置 L2MTU 值。其他以太网接口仅在芯片组与 RouterBoard 以太网相同的情况下才可能显示 L2MTU。

这将使用户能够检查所需配置是否可行。用户可以利用额外的字节来承载 VLAN 和 MPLS 标签，或直接增大接口 MTU 以避免不必要的分片。

下表显示了 MikroTik RouterBoard 支持的 *max-l2mtu*（可在 `/interface/print` 菜单中作为只读选项 "max-l2mtu" 的值查看）：

|  |  |
| :-- | :-- |
| **型号名称** | **MTU 描述** |
| **RB SXT 系列、RB LHG、RB LDF、PL6411-2nD、PL7411-2nD、RB711 系列、wAP R-2nD、RB912R-2nD-LTm (LtAP mini)、RB Metal 系列、RB SXT Lite 系列、RB Groove 系列、Cube Lite60、LHG Lite60** | ether1:2028 |
| **RB SXT G 系列、RB DynaDish、wAP ac、RB QRT 系列、RB711G 系列、RB911G、RB912UAG** | ether1:4076 |
| **RB OmniTik 系列、RB750、RB750UP、RB751U-2HnD、RB951-2n** | ether1:4076；ether2-ether5:2028 |
| **RB OmniTik ac 系列、RB750GL、RB750Gr2** | ether1-ether5:4074 |
| **RB mAP、RB mAP lite、RB cAP、RB wAP** | ether1-ether2:2028 |
| **RB750r2、RB750P-PBr2、RB750UPr2、RB941-2nD、RB951Ui/RB952Ui 系列** | ether1-ether5:2028 |
| **RB750Gr3** | ether1-ether5:2026 |
| **RB751G-2HnD、RB951G-2HnD** | ether1-ether5:4074 |
| **RB962UiGS、RB960PGS** | ether1-ether5:4074；sfp1:4076 |
| **RB LHGG 系列** | ether1:9214 |
| **LHG XL 52 ac** | ether1:9214；sfp1:9214 |
| **RB1100Hx2、RB1100AHx2** | ether1-ether10:9498；ether11:9500；ether12-ether13:9116 |
| **RB4011iGS+ 系列** | ether1-ether10:9578；sfp-sfpplus1:9982 |
| **CCR1009 系列** | ether1-ether4:10224；ether5-ether8:10226；sfp1:10226；sfp-sfpplus1:10226 |
| **CCR1016 系列** | ether1-ether12:10226；sfp1-sfp12:10226；sfp-sfpplus1:10226 |
| **CCR1036 系列** | ether1-ether12:10226；sfp1-sfp4:10226；sfp-sfpplus1-sfp-sfpplus2:10226 |
| **CCR1072 系列** | ether1:9116；sfp-sfpplus1-sfp-sfpplus8:10226 |
| **CCR2004-1G-12S+2XS** | ether1:9586；sfp-sfpplus1-sfp-sfpplus12:9578；sfp28-1 - sfp28-2:9578 |
| **CCR2004-16G-2S+** | ether1-ether16:9582；sfp-sfpplus1-sfp-sfpplus2:9586 |
| **CCR2116-12G-4S+** | ether1-ether12:9570；ether13:9586；sfp-sfpplus1-sfp-sfpplus4:9570 |
| **CCR2216-1G-12XS-2XQ** | ether1:9586；sfp28-1 - sfp28-12:9570；qsfp28-1-1 - qsfp28-2-4:9570 |
| **CRS109-8G-1S** | ether1-ether8:4064；sfp1:4064 |
| **CRS125-24G-1S** | ether1-ether24:4064；sfp1:4064 |
| **CRS112-8G-4S、CRS112-8P-4S** | ether1-ether8:9204；sfp9-sfp12:9204 |
| **CRS106-1C-5S** | sfp1-sfp5:9204；combo1:9204 |
| **CRS210-8G-2S+** | ether1-ether8:9204；sfp-sfpplus1:9204；sfpplus2:9204 |
| **CRS212-1G-10S-1S+** | ether1:9204；sfp1-sfp10:9204；sfpplus1:9204 |
| **CRS226-24G-2S+** | ether1-ether24:9204；sfp-sfpplus1:9204；sfpplus2:9204 |
| **CRS326-24G-2S+、CSS326-24G-2S+** | ether1-ether24:10218；sfp-sfpplus1:10218；sfpplus2:10218 |
| **CRS317-1G-16S+** | ether1:10218；sfp-sfpplus1-sfp-sfpplus16:10218 |
| **CRS328-24P-4S+** | ether1-ether24:10218；sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS328-4C-20S-4S+** | combo1-combo4:10218；sfp1-sfp20:10218；sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS305-1G-4S+** | ether1:10218；sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS304-4XG** | ether1-ether4:10218；ether5:9676 |
| **CRS309-1G-8S+** | ether1:10218；sfp-sfpplus1-sfp-sfpplus8:10218 |
| **netFiber 9/IN (CRS310-1G-5S-4S+)** | sfp1-sfp5:10218；sfp-sfpplus1-sfp-sfpplus4:10218 |
| **CRS310-8G+2S+IN** | ether1-ether8:10218；sfp-sfpplus1-sfp-sfpplus2:10218 |
| **CRS312-4C+8XG** | combo1-combo4:10218；ether1-ether8:10218；ether9:2028 |
| **netPower 15FR (CRS318-1Fi-15Fr-2S)** | ether1-ether16:10218；sfp1-sfp2:10218 |
| **netPower 16P (CRS318-16P-2S+)** | ether1-ether16:10218；sfp-sfpplus1-sfp-sfpplus2:10218 |
| **CRS326-4C+20G+2Q+** | combo1-combo4:10218；ether1-ether20:10218；qsfpplus1-1-qsfpplus2-4:10218；ether21:2028 |
| **CRS326-24S+2Q+** | sfp-sfpplus1-sfp-sfpplus24:10218；qsfpplus1-1-qsfpplus2-4:10218；ether1:2028 |
| **CRS354-48G-4S+2Q+、CRS354-48P-4S+2Q+** | sfp-sfpplus1-sfp-sfpplus4:10218；qsfpplus1-1-qsfpplus2-4:10218；ether1-ether48:10218；ether49:2028 |
| **CRS418-8P-8G-2S+RM** | ether1-ether16:10218；ether17:9018；sfp-sfpplus1-sfp-sfpplus2: 10218 |
| **CRS504-4XQ-IN** | ether1:2028；qsfp28-1-1 - qsfp28-4-4:10218 |
| **CRS510-8XS-2XQ-IN** | ether1:2028；sfp28-1 - sfp28-8:10218；qsfp28-1-1 - qsfp28-2-4:10218 |
| **CRS518-16XS-2XQ** | ether1:2028；sfp28-1 - sfp28-16:10218；qsfp28-1-1 - qsfp28-2-4:10218 |
| **CRS812-8DS-2DQ-2DDQ-RM** | ether1-ether2:9586；qsfp56-1-1 - qsfp56-2-4:9570；qsfp56-dd-1-1 - qsfp56-dd-2-8:9570；sfp56-1 - sfp56-8:9570 |
| **CSS610-8G-2S+、CSS610-8P-2S+** | ether1-ether8:10218；sfp-sfpplus1-sfp-sfpplus2:10218 |
| **D52G-5HacD2HnD (hAP ac²)** | ether1-ether5:9124 |
| **C52iG-5HaxD2HaxD (hAP ax[^2])** | ether1-ether5:9214 |
| **C53UiG+5HPaxD2HPaxD (hAP ax[^3])** | ether1-ether5:9214 |
| **L41G-2axD (hAP ax lite)** | ether1-ether4:2026 |
| **cAP ac** | ether1-ether2:9124 |
| **GPEN21** | ether1-ether2:10222；sfp1: 10222 |
| **wAP60G、LHG60G** | ether1:9124 |
| **RB260GS 系列、CSS106-5G-1S、CSS106-1G-4P-1S** | ether1-ether5:9198；sfp1:9198 |
| **RBFTC11** | ether1:4046；sfp1:4046 |
| **RBM33G** | ether1-ether3:2026 |
| **RBM11G** | ether1:2026 |
| **RB760iGS** | ether1-ether5:2026；sfp1:2026 |
| **E50UG** | ether1:2048；ether2-ether5:2026 |
| **RB411 系列** | ether1:1526 |
| **RB433 系列、RB450、RB493 系列** | ether1:1526；ether2-ether3:1522 |
| **RB450Gx4** | ether1-ether5:9214 |
| **RB411GL** | ether1:1520 |
| **RB433GL、RB435G、RB450G、RB493G** | ether1-ether3:1520 |
| **RB800** | ether1-ether2:9500；ether3:9116 |
| **RB850Gx2** | ether1-ether5:1580 |
| **RB921UAGS、RB922UAGS** | ether1:4076；sfp1:4076 |
| **D23UGS-5HPacD2HnD (NetMetal ac²)** | ether1:9214；sfp1:9214 |
| **L23UGSR-5HaxD2HaxD (NetMetal ax)** | ether1:8158；sfp1:8158 |
| **RB953GS** | ether1-ether2:4074；sfp1:4074；sfp2:4076 |
| **RB2011 系列** | ether1-ether5:4074；ether6-ether10:2028；sfp1:4074 |
| **RB3011 系列** | ether1-ether5:8156；ether6-ether10:8156；sfp1:8158 |
| **RB5009 系列** | ether1-ether8: 9796；sfp-sfpplus1: 9796 |
| **L009 系列** | ether1: 8158；ether2-ether8: 8154；sfp1: 8154 |
| **RB44Ge** | ether1-ether4:9116 |

RouterOS 中的所有无线接口（包括 Nstreme2）均支持 2290 字节的 L2MTU。

:::danger
L2MTU 配置更改会触发所有接口重新加载（链路断开/链路恢复），这是必要的内部处理过程所致。
建议谨慎配置 L2MTU，并注意这可能导致已连接设备出现短暂中断。

:::

### MPLS/二层.5/L2.5 MTU

MPLS MTU 在 `/mpls/interface` 菜单中配置，用于指定可通过特定接口发送的最大数据包大小（包括 MPLS 标签）。

请确保 MPLS MTU 值小于或等于 L2MTU。MPLS MTU 对数据包的影响因 MPLS 路由器所执行的操作而异。由于 MPLS MTU 对 MPLS 交换数据包的影响，强烈建议在构成 MPLS 云的所有路由器上配置相同的 MPLS MTU 值。这一要求意味着，参与 MPLS 云的所有接口必须配置为参与接口中最小的 MPLS MTU 值；因此，在选择所用硬件时必须仔细考量。

### MPLS 交换

当包含 MPLS 标签的数据包超过所配置的 MPLS MTU 时，路由器会尝试确定 MPLS 帧内承载的协议类型：

- **IP 数据包**：如果封装的数据包是 IP 数据包，MPLS 会生成 ICMP "需要分片" 错误消息。此行为与标准 IP 协议处理方式一致。请注意，此 ICMP 错误不会直接路由回数据包发送方；相反，它会沿标签交换路径（LSP）向末端交换，使出口路由器能够将其路由回源地址。

- **非 IP 数据包**：如果封装的数据包不是 IP 数据包，MPLS 会直接丢弃它，因为路由器无法解析数据包内容。此行为对于 VPLS 等 MPLS 应用尤为重要，因为通过 MPLS 网络传输的帧不是 IP 数据包，而是封装的以太网帧。如果 LSP 上任何接口配置的 MPLS MTU 小于入口路由器准备的数据包大小，这些帧将被静默丢弃。

#### IP 入口

当路由器首次为 IP 数据包压入标签，且包含 MPLS 标签后的数据包大小超过 MPLS MTU 时，路由器的行为与接口 MTU 被超出时相同。它要么将数据包分片为附加标签后不超过 MPLS MTU 的分片（如果 IP 不分片标志未设置），要么生成 ICMP 需要分片错误并发送回发送方。

#### VPLS 入口

当路由器封装以太网帧以通过 VPLS 伪线转发时，它会检查数据包大小（包括 VPLS 控制字（4 字节）及所需的标签（通常为 2 个标签，增加 8 字节））是否超过出接口的 MPLS MTU。如果超过，VPLS 会对数据包进行分片，以符合出接口的 MPLS MTU。数据包将在 VPLS 伪线的出口点进行重组。

## 配置示例

在这些示例中，我们将观察通过以太网接口进入和离开路由器的帧。

### 简单路由

下图显示了简单路由时的数据包 MTU 大小，数据包大小未被修改。

![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-02.webp)

### 带 VLAN 封装的简单路由

每个 VLAN 标签长度为 4 字节。VLAN 标签由路由器添加。L2-MTU 增加 4 字节。

![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-03.webp)

### 带标签的简单 MPLS

当 MPLS 作为 IP 路由的简单替代方案使用时，每个数据包仅附加一个标签，因此数据包大小增加 4 字节。我们这里讨论的是带有两个 MPLS 标签的情况。为了能够无分片地转发标准大小（1500 字节）的 IP 数据包，对于两个 MPLS 标签，MPLS MTU 必须至少设置为 1508。

![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-04.webp)

### VPLS 隧道

当远端端点未直接连接时，会存在两个 MPLS 标签。一个 MPLS 标签用于到达远端端点；第二个标签用于标识 VPLS 隧道。

![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-05.webp)

## 高级配置示例

在此示例中，我们将更详细地了解所有类以太网接口（包括 Bridge、VLAN 和 VPLS 接口）所需的 L2MTU。

在此配置中，我们将有 3 台路由器：

- Q-in-Q 路由器——此路由器将接收标准 1500 字节的以太网帧，并为数据包添加两个 VLAN 标签。然后，数据包将通过以太网网络发送至第二台路由器。

- VPLS 路由器——此路由器将移除外层 VLAN 标签，并将带有剩余 VLAN 标签的数据包桥接到 VPLS 隧道。VPLS 隧道将通过 MPLS 网络将数据包传输至第三台路由器。

- MPLS 边缘路由器——将移除 VPLS 和 VLAN 标签，并将数据包桥接到客户端以太网网络。

![](https://manual.mikrotik.com/docs/hardware/img/mtu-in-routeros-06.webp)