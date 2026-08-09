# Ethernet

> MikroTik RouterOS 支持从 10Mbps 到 100Gbps 的各种以太网接口，包括铜缆和光纤选项，并配备 combo 接口。它能够控制链路速度、双工模式、自动协商，以及通过手动 advertise 设置来精确指定链路模式的 SFP/QSFP 接口配置。

# Ethernet

MikroTik RouterOS 支持多种类型的以太网接口 - 从 10Mbps 到 10Gbps 的铜质双绞线以太网，1Gbps、10Gbps、25Gbps 的 SFP/SFP+/SFP28 接口，以及 40Gbps、100Gbps、200Gbps、400Gbps 的 QSFP+/QSFP28/QSFP56/QSFP56-DD 接口。某些 RouterBoard 设备配备了 combo 接口，该接口同时包含两种接口类型（例如，双绞线以太网和 SFP/SFP+ 接口），允许选择最合适的选项或创建物理链路故障切换。通过 RouterOS，可以控制不同的以太网相关属性，如链路速度、自动协商、双工模式等，监控收发器诊断信息，并查看广泛的以太网相关统计信息。

:::info
有关 MikroTik SFP 和 QSFP 类型接口及其兼容性的更多信息，请参阅 [有线接口兼容性](./mikrotik-wired-interface-compatibility.mdx) 页面。
:::

## 自动协商和强制链路模式

自动协商是一种通信方法和一系列步骤，由通过双绞线电缆连接的以太网设备采用。它使这些设备能够就关键的传输设置达成一致，包括速度、双工模式和流量控制。在此过程中，连接的设备首先交换关于这些设置的能力信息。之后，它们共同选择双方都能有效支持的最佳传输模式。

然而，在 RouterOS 中，自动协商在 SFP/QSFP 端口上的行为与标准 RJ45 以太网端口不同。对于 SFP/QSFP 接口，协商过程不涉及通告能力的交换（不共享通告位）。相反，RouterOS 尝试使用每一侧支持的最高模式来建立链路。要成功连接，两个设备必须通告相同的最高公共模式。

## 例如

- 设备 A 通告 `10G-baseCR` 和 `25G-baseCR`。
- 设备 B 仅通告 `10G-baseCR`。

在这种情况下，链路将无法建立，因为设备 A 优先选择 25G，而设备 B 仅通告 10G。

## 为确保链路成功

- 设备 A 和设备 B 必须具有相同的最高通告模式。
  因此，如果设备 B 通告 `25G-baseCR`，并且设备 A 也将 `25G-baseCR` 作为其最高通告，则链路将建立。

总之，在配置 SFP/QSFP 接口时，请确保两端支持的最高模式匹配，以确保正确建立链路。

### Advertise

在 RouterOS 7.12 版本之前，当启用自动协商时，接口会尝试猜测另一端接口的最大可用速度（使得 advertise 设置不适用于 SFP/QSFP 接口）。

在 RouterOS 7.12 版本之后，您现在可以手动设置 advertise 位来指定您想要使用的所需链路模式。速度参数也已修订以提供更清晰的表示，因为以前的值过于模糊。此外，全双工设置已被移除，因为新的链路模式已经包含了双工选项（见下表）。

| 链路模式（用于 advertise 和 speed 属性） | 描述 |
| :-- | :-- |
| 10M-baseT-half | 10M 双绞线半双工 |
| 10M-baseT-full | 10M 双绞线全双工 |
| 100M-baseT-half | 100M 双绞线半双工 |
| 100M-baseT-full | 100M 双绞线全双工 |
| 100M-baseFX-full | 100M 光纤 |
| 1G-baseT-half | 1G 双绞线半双工 |
| 1G-baseT-full | 1G 双绞线全双工 |
| 1G-baseX | 1G 光纤 |
| 2.5G-baseT | 2.5G 双绞线全双工 |
| 2.5G-baseX | 2.5G 光纤 |
| 5G-baseT | 5G 双绞线全双工 |
| 10G-baseT | 10G 双绞线全双工 |
| 10G-baseSR-LR | 10G 光纤 |
| 10G-baseCR | 10G 双轴铜缆 |
| 40G-baseSR4-LR4 | 4x10G 光纤 |
| 40G-baseCR4 | 4x10G 双轴铜缆 |
| 25G-baseSR-LR | 25G 光纤 |
| 25G-baseCR | 25G 双轴铜缆 |
| 50G-baseSR2-LR2 | 2x25G 光纤 |
| 50G-baseCR2 | 2x25G 双轴铜缆 |
| 100G-baseSR4-LR4 | 4x25G 光纤 |
| 100G-baseCR4 | 4x25G 双轴铜缆 |
| 50G-baseSR-LR | 50G 光纤 |
| 50G-baseCR | 50G 双轴铜缆 |
| 100G-baseSR2-LR2 | 2x50G 光纤 |
| 100G-baseCR2 | 2x50G 双轴铜缆 |
| 200G-baseSR4-LR4 | 4x50G 光纤 |
| 200G-baseCR4 | 4x50G 双轴铜缆 |
| 400G-baseSR8-LR8 | 8x50G 光纤 |
| 400G-baseCR8 | 8x50G 双轴铜缆 |

:::info
**链路模式命名方案**

**传输速率**：第一个数字后跟 'M' 或 'G'（例如，10M、100M、1G）表示以兆比特或吉比特每秒为单位的数据传输速率。

**接口类型**："base" 后的符号表示接口类型：

- **T**：代表双绞线布线，后跟双工模式（半双工或全双工）。
- **SR-LR**：代表“短距离”和“长距离”光模块，包括 LRM、ER、ZR 等其他变体。这些链路模式应与光模块一起使用。
- **CR**：代表双轴铜缆，用于直接连接电缆（DAC）。对于 1Gbps DAC，适当的链路模式是 1G-baseX。
- **FX:** 代表通过光纤电缆的快速以太网。这也包括 LX - 长波长标准。

**线路数量**：

- **SR2-LR2/CR2**：表示两条线路。
- **SR4-LR4/CR4**：表示四条线路。
- **SR8-LR8/CR8:** 表示八条线路。

:::

在手动配置接口的 advertise 位之前，首先通过执行命令 `/interface/ethernet/monitor` 并检查“supported”列表来确定支持哪些位。您还可以在“sfp-supported”字段下查看收发器支持的 advertise 位。此外，“advertising”将显示 RouterOS 自动设置的位。该列表是通过比较接口和收发器上可用的最大链路模式值并选择匹配项生成的。

```ros
[admin@MikroTik] > /interface/ethernet/monitor qsfp28-1-1
                      name: qsfp28-1-1
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full,
                            1G-baseX,2.5G-baseT,2.5G-baseX,5G-baseT,10G-baseT,10G-baseSR-LR,10G-baseCR,40G-baseSR4-LR4,
                            40G-baseCR4,25G-baseSR-LR,25G-baseCR,50G-baseSR2-LR2,50G-baseCR2,100G-baseSR4-LR4,100G-baseCR4
             sfp-supported: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
               advertising: 10G-baseSR-LR,25G-baseSR-LR,100G-baseSR4-LR4
... 
```

手动设置 advertise 设置的一个应用场景是 QSFP 下的所有子接口。整体配置过程从最顶层的启用端口开始。如果选择的模式有效且受支持，则将应用该模式。如果该特定链路模式需要多条通道，则下一个接口的 advertise 和 speed 配置将被忽略，但该接口应保持 **启用** 状态。下一个可用的空闲通道或端口遵循类似的过程。

```ros
/interface/ethernet
set [ find default-name=qsfp28-1-1 ] advertise=50G-baseCR2
set [ find default-name=qsfp28-1-3 ] advertise=25G-baseCR
set [ find default-name=qsfp28-1-4 ] advertise=25G-baseCR
```

:::warning
**注意**：多通道接口链路模式（50G-baseCR2、50G-baseSR2-LR2）不能配置在单通道接口（SFP28/SFP56）上。

IEEE 802.3az 高能效以太网（EEE）功能在我们所有产品上均已禁用。没有选项可以手动启用或禁用 EEE 设置。
:::

### 以太网 LED 行为

#### 绿色 LED（链路/速度）

- 亮（常亮）– 最大速率

#### 黄色/琥珀色 LED（活动/速度）

- 亮（常亮）- 链路已建立。
- 灭 – 无链路。
- 闪烁 – 正在传输数据。

### 强制模式

在连接 DAC 电缆或光模块后，如果日志记录中出现警告消息，例如：

```ros
10:20:47 interface,warning sfp-sfpplus1 module auto-initialization failed, try forced-mode
```

这可能表示连接的电缆或模块具有损坏或错误的 EEPROM 校验和，导致自动连接配置失败。此功能在 RouterOS 7.12 版本中引入，可能会影响一些过去因错误地假设模块/电缆属性而工作的链路，这可能导致与链路连接和设备功能相关的各种问题。

在这种情况下，您可以尝试手动设置链路模式，这可能有助于建立可用的链路。提供以下强制端口设置示例：

- 对于 DAC 电缆和 1G/10G/25G 的连接速度。

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseCR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseCR
```

:::info
注意：选择接口速度设置时，请注意您的 DAC 电缆支持哪些速率（检查电缆规格数据）
:::

- 对于光模块和 1G/10G/25G 的连接速度。

```ros
/interface/ethernet
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=1G-baseX
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=10G-baseSR-LR
set [ find default-name=sfp-sfpplus1 ] auto-negotiation=no speed=25G-baseSR-LR
```

:::warning
注意：选择接口速度设置时，请注意您的光模块支持哪些速率（检查模块规格数据）

具有错误 EEPROM 校验和的模块不会向以太网监视器输出任何 EEPROM 信息，这也意味着此类模块的 SFP DDM 监视器无法工作。
:::

### FEC

FEC（前向纠错）是一种数字信号处理方法，通过在发送端向数据添加信息（奇偶校验位）来改善 SFP28、QSFP+ 和 QSFP28 链路的误码率。接收端随后使用此信息来检测和纠正传输过程中可能引入的错误。

为确保链路成功，链路两端应使用相同的 *fec-mode*。RouterOS 默认使用禁用 *fec-mode* 的设置，但可以更改为 *fec74*（也称为 FC-FEC）或 *fec91*（也称为 RS-FEC）。有关 FEC 模式选项的更多信息，请参阅 [属性](./ethernet.md#properties) 描述。下表显示了链路模式和支持的 FEC 模式：

| 链路模式（用于 advertise 和 speed 属性） | 支持的 FEC 模式 |
| :-- | :-- |
| 40G-baseSR4-LR4 | fec74 |
| 40G-baseCR4 | fec74 |
| 25G-baseSR-LR | fec74, fec91\* |
| 25G-baseCR | fec74, fec91\* |
| 50G-baseSR2-LR2 | fec74, fec91 |
| 50G-baseCR2 | fec74, fec91 |
| 100G-baseSR4-LR4 | fec91 |
| 100G-baseCR4 | fec91 |
| 50G-baseSR-LR | fec91 (必需) |
| 50G-baseCR | fec91 (必需) |
| 100G-baseSR2-LR2 | fec91 (必需) |
| 100G-baseCR2 | fec91 (必需) |
| 200G-baseSR4-LR4 | fec91 (必需) |
| 200G-baseCR4 | fec91 (必需) |
| 400G-baseSR8-LR8 | fec91 (必需) |
| 400G-baseCR8 | fec91 (必需) |

:::warning
**注意**：CCR2004-1G-2XS-PCIe 设备在 SFP28 接口上不支持 fec91。
:::

## 属性

**子菜单：** `/interface/ethernet`

本节介绍以太网接口的配置选项。

| 属性 | 描述 |
| :-- | :-- |
| **advertise** (自 RouterOS v7.12 起: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4;* 默认值: )  (旧版 RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*; 默认值: ) | 通告的链路模式，仅在启用自动协商时适用。通告高于接口实际支持速度的速度可能导致未定义行为。允许多个选项。 |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*; 默认值: **enabled**) | 地址解析协议模式：disabled - 接口将不使用 ARPenabled - 接口将使用 ARPlocal-proxy-arp - 路由器在接口上执行代理 ARP，并将回复发送到同一接口proxy-arp - 路由器在接口上执行代理 ARP，并将回复发送到其他接口reply-only - 接口将仅回复来自 ARP 表中作为静态条目输入的匹配 IP 地址/MAC 地址组合的请求。不会自动在 ARP 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-timeout** (*auto \| integer*; 默认值: **auto**) | 在从 IP 地址未收到数据包后，ARP 记录在 ARP 表中保留的时间。值 `auto` 等于 IP/设置中的 `arp-timeout` 值，默认为 30 秒。 |
| **auto-negotiation** (*yes \| no*; 默认值: **yes**) | 启用后，接口“通告”其最大能力以实现最佳连接。注意1：不应仅在一端禁用自动协商，否则以太网接口可能无法正常工作。注意2：千兆以太网和 NBASE-T 以太网链路在禁用自动协商时无法工作。 |
| **bandwidth** (*integer/integer*; 默认值: **unlimited/unlimited**) | 设置接口将处理的最大 rx/tx 带宽（kbps）。所有 Atheros [交换芯片](../bridging-and-switching/switch-chip-features.md) 端口均支持 TX 限制。仅 Atheros8327/QCA8337 交换芯片端口支持 RX 限制。 |
| **cable-setting** (*default \| short \| standard*; 默认值: **default**) | 更改电缆长度设置（仅适用于 NS DP83815/6 网卡） |
| **combo-mode** (*auto \| copper \| sfp*; 默认值: **auto**) | 选择自动模式时，首先连接的端口将建立链路。如果此链路失败，另一个端口将尝试建立新链路。重启时，两个端口中的任何一个都可以运行，这取决于哪个端口将首先成功建立链路。选择 sfp 模式时，接口将仅通过 SFP/SFP+ 笼工作。选择 copper 模式时，接口将仅通过 RJ45 以太网端口工作。 |
| **comment** (*string*; 默认值: ) | 项目的描述性名称 |
| **disable-running-check** (*yes \| no*; 默认值: **yes**) | 禁用运行检查。如果此值设置为 'no'，路由器将自动检测 NIC 是否连接到网络中的设备。默认值为 'yes'，因为较旧的 NIC 不支持它。（仅与 CHR 和 x86 相关） |
| **fec-mode**(*auto \| fec74 \| fec91 \| off;* 默认值: **auto**) | 更改 SFP28、QSFP+ 和 QSFP28 接口的前向纠错（FEC）模式。链路两端应使用相同的模式，否则 FEC 不匹配可能导致链路无法工作甚至虚假链路启动。**建议启用 FEC，尤其是在 CRS3xx、CRS5xx 系列交换机之间创建链路时。某些光模块可能依赖 MAC 中的 FEC 功能。** auto - 与 off 相同fec74 - 启用 IEEE 802.3 第 74 条 FEC（又名 FC-FEC），可用于 25Gbps、40Gbps 和 50Gbps 链路模式fec91 - 启用 IEEE 802.3 第 91 条 FEC（又名 RS-FEC），可用于 25Gbps、50Gbps、100Gbps、200Gbps 和 400Gbps 链路模式off - 禁用 FEC。 |
| **tx-flow-control** (*on \| off \| auto*; 默认值: **off**) | 设置为 on 时，端口将向上游设备生成暂停帧以暂时停止数据包传输。仅当路由器的某个输出接口拥塞且无法再传输数据包时，才会生成暂停帧。**auto** 与 **on** 相同，除非 auto-negotiation=yes 时，流量控制状态通过考虑另一端通告的内容来解决。 |
| **rx-flow-control** (*on \| off \| auto*; 默认值: **off**) | 设置为 on 时，端口将处理接收到的暂停帧并在需要时暂停传输。**auto** 与 **on** 相同，除非 auto-negotiation=yes 时，流量控制状态通过考虑另一端通告的内容来解决。 |
| **full-duplex** (*yes \| no*; 默认值: **yes**) | 定义数据传输是否同时双向进行，仅在禁用自动协商时适用。自 RouterOS v7.12 起，此设置已被新的速度链路模式取代。 |
| **l2mtu** (*integer [0..65536]*; 默认值: ) | 二层最大传输单元。[阅读更多](../hardware/mtu-in-routeros.md)。 |
| **mac-address** (*MAC*; 默认值: ) | 接口的媒体访问控制编号。 |
| **mdix-enable** (*yes \| no*; 默认值: **yes**) | 是否为端口启用 MDI/X 自动交叉线缆校正功能（特定于硬件，例如 RB500 上的 ether1 可以设置为 yes/no。在其他硬件上固定为 'yes'。） |
| **mtu** (*integer [0..65536]*; 默认值: **1500**) | 三层最大传输单元 |
| **name** (*string*; 默认值: ) | 接口名称 |
| **orig-mac-address** (*只读: MAC*; 默认值: ) | 接口的原始媒体访问控制编号。 |
| **passthrough-interface** (*interface*; 默认值: ) | 在 CCR2004-1G-2XS-PCIe 设备上设置接口为直通模式。默认情况下，PCIe 接口将显示为四个虚拟以太网接口。两个接口以直通模式连接到 25G SFP28 笼。其余两个虚拟 Ethernet-PCIe 接口与千兆以太网端口桥接以进行管理访问。 |
| **poe-out** (*auto-on \| forced-on \| off*; 默认值: **off**) | PoE 输出设置。[`阅读更多`](../hardware/poe-out.mdx)。 |
| **poe-priority** (*integer [0..99]*; 默认值: ) | PoE 输出设置。[`阅读更多`](../hardware/poe-out.mdx)。 |
| **sfp-shutdown-temperature** (*integer*; 默认值: **95** \| **80**) | 检测到 SFP 模块温度过高时，接口将暂时关闭的温度（摄氏度）（v6.48 引入）。SFP/SFP+/SFP28 接口的默认值为 95，QSFP+/QSFP28 接口的默认值为 80（v7.6 引入）。 |
| **sfp-rate-select**(*high \| low*; 默认值: **high**) | 允许控制 SFP 端口的速率选择引脚。 |
| **speed** (自 RouterOS v7.12 起: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4;* 默认值: )  (旧版 RouterOS: *10Mbps \| 10Gbps \| 100Mbps \| 1Gbps \| 2.5Gbps \| 5Gbps \| 25Gbps \| 40Gbps \| 100Gbps*; 默认值: ) | 设置接口数据传输速度，仅在禁用自动协商时生效。设置高于接口实际支持速度的速度可能导致未定义行为。仅允许单个选项。 |

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **running** (*yes \| no*) | 接口是否正在运行。请注意，某些接口没有运行检查，它们总是报告为“running”。 |
| **slave** (*yes \| no*) | 接口是否配置为另一个接口的从属接口（例如 [Bonding](../high-availability-solutions/bonding.md) 或 [Bridge](../bridging-and-switching/index.md)） |
| **switch** (*integer*) | 交换芯片接口所属的 ID。 |

## 菜单特定命令

| 属性 | 描述 |
| :-- | :-- |
| **blink** (*[id, name]*) | 闪烁以太网 LED |
| **monitor** (*[id, name]*) | 监视以太网状态。[阅读更多](./ethernet.md#monitor)。 |
| **reset-counters** (*[id, name]*) | 重置统计计数器。[阅读更多](./ethernet.md#stats)。 |
| **reset-mac-address** (*[id, name]*) | 将 MAC 地址重置为制造商默认值。 |
| **cable-test** (*string*) | 显示检测到的电缆对问题。[`阅读更多`](./ethernet.md#detect-cable-problems)。 |

## 监视器

要打印当前链路速率和其他以太网相关属性，或查看收发器的详细诊断信息，请使用 `/interface/ethernet/monitor` 命令。提供的信息可能因不同的接口类型（例如，双绞线以太网或 SFP 接口）或不同的收发器（例如，SFP 和 QSFP）而异。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **advertising** (自 RouterOS v7.12 起: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*) (旧版 RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*) | 通告的链路模式仅在启用自动协商时适用 |
| **auto-negotiation** (*disabled \| done \| failed \| incomplete*) | 当前自动协商状态：disabled - 协商已禁用done - 协商已完成failed - 协商失败incomplete - 协商尚未完成 |
| **default-cable-settings** (*short \| standard*) | 默认电缆长度设置（仅适用于 NS DP83815/6 网卡）short - 支持短电缆standard - 支持标准电缆 |
| **fec** (*fec74 \| fec91 \| off*) | 当前 FEC 模式。 |
| **full-duplex** (*yes \| no*) | 数据传输是否同时双向进行 |
| **link-partner-advertising** (自 RouterOS v7.12 起: *10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4*) (旧版 RouterOS: *10M-full \| 10M-half \| 100M-full \| 100M-half \| 1000M-full \| 1000M-half \| 2500M-full \| 5000M-full \| 10000M-full*) | 链路伙伴通告的链路模式仅在启用自动协商时适用 |
| **rate** (*10Mbps \| 100Mbps \| 1Gbps \| 2.5Gbps \| 5Gbps \| 10Gbps \| 25Gbps \| 40Gbps \| 50Gbps \| 100Gbps \| 200Gbps \| 400Gbps*) | 连接的实际数据速率。 |
| **status** (*link-ok \| no-link \| unknown*) | 接口的当前链路状态link-ok - 网卡已连接到网络no-link - 网卡未连接到网络unknown - 无法识别连接（如果网卡不报告连接状态） |
| **tx-flow-control** (*yes \| no*) | 是否使用 TX 流量控制 |
| **rx-flow-control** (*yes \| no*) | 是否使用 RX 流量控制 |
| **combo-state** (*copper \| sfp*) | combo 接口使用的 combo 模式 |
| **sfp-module-present** (*yes \| no*) | 收发器是否在笼中 |
| **sfp-rx-loss** (*yes \| no*) | 接收器信号是否丢失 |
| **sfp-tx-fault** (*yes \| no*) | 收发器发射器是否处于故障状态 |
| **sfp-type** (*SFP/SFP+/SFP28/SFP56 \| DWDM-SFP/SFP+ \| QSFP \| QSFP+ \| QSFP28/QSFP56 \| QSFPDD*) | 使用的收发器类型 |
| **sfp-cmis-revision** *(string)* | 收发器 CMIS 修订号 |
| **sfp-connector-type** (*SC \| LC \| optical-pigtail \| copper-pigtail \| multifiber-parallel-optic-1x12 \| multifiber-parallel-optic-1x16 \| no-separable-connector \| RJ45*) | 使用的收发器连接器类型 |
| **sfp-link-length-9um** (*m*) | 收发器支持的单模 9/125um 光纤链路长度 |
| **sfp-link-length-sm** *(km)* | 收发器支持的单模光纤链路长度 |
| **sfp-link-length-om3** *(m)* | 收发器支持的多模 (OM3) 链路长度 |
| **sfp-link-length-om4** *(m)* | 收发器支持的多模 (OM4) 链路长度 |
| **sfp-link-length-om5** *(m)* | 收发器支持的多模 (OM5) 链路长度 |
| **sfp-link-length-om2** *(m)* | 收发器支持的多模 50/125um 光纤 (OM2) 链路长度 |
| **sfp-link-length-om1** *(m)* | 收发器支持的多模 62.5/125um 光纤 (OM1) 链路长度 |
| **sfp-link-length-copper** *(m)* | 铜缆收发器支持的链路长度 |
| **sfp-vendor-name** (*string*) | 收发器制造商 |
| **sfp-vendor-part-number** (*string*) | 收发器部件号 |
| **sfp-vendor-revision** (*string*) | 收发器修订号 |
| **sfp-vendor-serial** (*string*) | 收发器序列号 |
| **sfp-manufacturing-date** (*date*) | 收发器制造日期 |
| **sfp-power-class** *(string)* | 收发器功率等级 |
| **sfp-max-power** *(W)* | 收发器最大功耗 |
| **sfp-wavelength** (*nm*) | 收发器发射器光信号波长 |
| **sfp-temperature***(C)* | 收发器温度 |
| **sfp-supply-voltage** *(V)* | 收发器电源电压 |
| **sfp-tx-bias-current** *(mA)* | 收发器 Tx 偏置电流 |
| **sfp-tx-power** *(dBm)* | 收发器发射光功率 |
| **sfp-rx-power** *(dBm)* | 收发器接收光功率 |
| **sfp-supported**(*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*) | 模块支持的链路模式。此属性仅适用于某些设备。 |
| **supported** (*10M-baseT-half \| 10M-baseT-full\| 100M-baseT-half \| 100M-baseT-full \| 1G-baseT-half \| 1G-baseT-full \| 1G-baseX \| 2.5G-baseT \| 2.5G-baseX \| 5G-baseT \| 10G-baseT \| 10G-baseSR-LR \| 10G-baseCR \| 40G-baseSR4-LR4 \| 40G-baseCR4 \| 25G-baseSR-LR \| 25G-baseCR \| 50G-baseSR2-LR2 \| 50G-baseCR2 \| 100G-baseSR4-LR4 \| 100G-baseCR4 \| 50G-baseSR-LR \| 50G-baseCR \| 100G-baseSR2-LR2 \| 100G-baseCR2 \| 200G-baseSR4-LR4 \| 200G-baseCR4 \| 400G-baseSR8-LR8 \| 400G-baseCR8*) | 显示支持的接口硬件链路模式能力。 |
| **eeprom-checksum** *(good \| bad)* | EEPROM 校验和是否正确 |
| **eeprom** *(十六进制转储)* | 收发器的原始 EEPROM |

以太网状态输出示例：

```ros
[admin@MikroTik] > /interface/ethernet/monitor ether2 
                      name: ether2
                    status: link-ok
          auto-negotiation: done
                      rate: 1Gbps
               full-duplex: yes
           tx-flow-control: no
           rx-flow-control: no
                 supported: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
               advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
  link-partner-advertising: 10M-baseT-half,10M-baseT-full,100M-baseT-half,100M-baseT-full,1G-baseT-half,1G-baseT-full
```

SFP 状态输出示例：

```ros
[admin@MikroTik] > /interface/ethernet/monitor sfp3
                      name: sfp3
                    status: link-ok
          auto-negotiation: done
                       rate: 1Gbps
                full-duplex: yes
            tx-flow-control: no
          