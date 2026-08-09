# 精确时间协议

> MikroTik RouterOS 文档介绍了精确时间协议（PTP），用于在网络中实现亚微秒级时钟同步，支持 IEEE 1588-2008 标准，具备硬件时间戳功能，并提供多种配置文件选项，包括 802.1AS、AES67、G.8275.1 和 SMPTE，适用于特定行业。

# 精确时间协议

精确时间协议（PTP）由电气与电子工程师协会（IEEE）制定，是一种用于在局域网中同步时钟的协议。在电信、金融和工业自动化等对精确计时至关重要的行业和应用中，该协议不可或缺。PTP 通常可确保亚微秒级的时间精度，在满足硬件要求时，甚至可实现纳秒级的精度。MikroTik 对 PTP 的实现支持 IEEE 1588-2008（PTPv2），并具备硬件时间戳功能，确保同步精度在纳秒级范围内。有关 MikroTik PTP 功能的更多详细信息，请参阅以下列表。

- 两步普通时钟和边界时钟。
- 硬件时间戳，确保时钟同步精度在纳秒（ns）级范围内。
- IPv4 和二层（L2）组播传输模式。
- 端到端（E2E）和点对点（P2P）延迟机制。
- IEEE 1588-2008（PTPv2）。
- 支持以下配置文件：
  - 802.1AS：用于音频视频桥接（AVB）和时间敏感网络（TSN）的定时与同步，基于 IEEE 802.1AS-2020 标准。
  - AES67：高性能音频-over-IP 互操作性。
  - G.8275.1：PTP 感知网络中的频率和相位同步。
  - SMPTE：专业广播环境中的音频/视频同步。

:::info
MikroTik PTP 支持依赖于硬件；请参阅[支持的设备](./precision-time-protocol.md#supported-devices)列表。
:::

## 常规属性

**子菜单：** `/system/ptp`

| 属性 | 描述 |
| :-- | :-- |
| **port** | 用于添加、移除或查看已分配端口的子菜单。 |
| **status** | 显示 PTP 端口、其状态以及从端口延迟的子菜单。 |
| **comment** (*字符串*；默认值：) | PTP 配置文件的简短描述。 |
| **name** (*字符串*；默认值：) | PTP 配置文件的名称。 |
| **domain** (默认值：**auto**) | 用于区分不同 PTP 实例的标识符。每个 PTP 配置文件定义其允许的域范围和默认值： • 802.1AS 范围：0–127，默认值：0（auto） • AES67 范围：0–127，默认值：0（auto） • G.8275.1 范围：24–43，默认值：24（auto） • SMPTE 范围：0–127，默认值：127（auto） • 默认 范围：0–127，默认值：0（auto） 注意：- “auto” 选择配置文件的默认域值。 |
| **delay-mode** (*auto \| e2e \| p2p*；默认值：**auto**) | auto - 根据所使用的配置文件自动选择延迟模式。e2e - 使用延迟请求-响应机制。p2p - 使用对等延迟机制。 |
| **priority1** (*整数 [0..255]*；auto；默认值：**auto**) | 参与主时钟选举的参数。 |
| **priority2** (*整数 [0..255]*；auto；默认值：**auto**) | 参与备用主时钟选举的参数。 |
| **profile**(*802.1as; aes67; g8275.1; smpte; default;* 默认值：**default**) | 每个配置文件都带有其预定义的 PTP 运行参数和选项的自动值：802.1as 是 PTP 针对音频视频桥接和时间敏感网络的适配。默认（auto）值：priority1=246，priority2=248，transport=l2-non-forwardable，delay-mode=p2p。aes67 配置文件用于高性能音频-over-IP 互操作性。默认（auto）值：priority1=128，priority2=128，domain=0，transport=ipv4，delay-mode=e2e。g8275.1 配置文件用于完全 PTP 感知网络中的频率和相位同步。默认（auto）值：priority1=128，priority2=128，domain=24，transport=l2-non-forwardable，delay-mode=e2e。smpte 配置文件用于专业广播环境中音频/视频设备的同步。默认（auto）值：priority1=128，priority2=128，domain=127，transport=ipv4，delay-mode=e2e。default 配置文件，即 PTPv2 默认配置，比其他配置文件提供更多的配置选项。默认（auto）值：priority1=128，priority2=128，domain=0，transport=ipv4，delay-mode=e2e。 |
| **transport** (*auto; ipv4; l2-forwardable; l2-non-forwardable;* 默认值：**auto**) | 要使用的传输协议：auto - 根据所使用的 PTP 配置文件自动选择传输模式。ipv4 - 使用 IPv4 组播地址 224.0.1.129 用于 PTP 主要消息，224.0.0.107 用于 PTP 对等延迟消息。l2-forwardable - 使用组播 MAC 地址 <code>01-1B-19-00-00-00</code>，该地址可通过不支持 PTP 的网络设备转发。l2-non-forwardable - 使用组播 MAC 地址 <code>01-80-C2-00-00-0E</code>，确保 PTP 消息不会通过不支持 PTP 的网络设备转发。 |

## 配置

在 MikroTik 设备上配置精确时间协议（PTP）是一个直接的过程。主要步骤包括创建 PTP 配置文件并将相关端口分配给该配置文件以进行 PTP 操作。

#### 创建 PTP 配置文件

要创建 PTP 配置文件，请使用以下命令。在此示例中，我们使用 802.1as 配置文件，但您可以根据需要选择其他可用配置文件：

```ros
/system/ptp/add name=ptp1 profile=802.1as
```

要验证配置文件是否已成功创建，请执行：

```routeros
/system/ptp/print
```

输出将显示已创建的配置文件及其当前设置：

```routeros
 Flags: I - inactive, X - disabled 
 0   name="ptp1" priority1=auto priority2=auto delay-mode=auto transport=auto profile=802.1as domain=auto  
```

:::note
默认情况下，每个配置文件的参数均设置为“auto”，即根据所选配置文件自动选择适当的值。在进行手动调整之前，请验证设置是否符合相关标准（例如 ITU-T G.8275.1、IEEE 802.1as、SMPTE、AES67）。
:::

#### 将端口分配给 PTP 配置文件

作为最后一步，分配将参与 PTP 的端口。例如，让我们添加几个 sfp28 接口。SFP28-12 连接到主时钟，而 SFP28-1 和 SFP28-2 连接到普通时钟/从时钟：

```ros
/system/ptp/port/add interface=sfp28-1 ptp=ptp1
/system/ptp/port/add interface=sfp28-2 ptp=ptp1
/system/ptp/port/add interface=sfp28-12 ptp=ptp1
```

#### 在 VLAN 端口上配置 PTP

当 PTP 端口同时也是边界时钟设备上 VLAN 的一部分时，您必须在[桥接 VLAN 表](../bridging-and-switching/user-guides/bridge-vlan-table.md)中为每个包含 PTP 端口的条目添加一个桥接接口作为未标记端口。

这是必要的，因为桥接接口作为通往 CPU 的桥接端口。因此，它必须与 PTP 端口一起包含在 VLAN 表中，以确保数据包能够正确地从物理端口接收，并通过桥接转发到 CPU。让我们继续之前的配置以使其更清晰：

```routeros
# 创建一个新的桥接接口
/interface/bridge/add name=bridge1

# 分配将作为此桥接一部分的端口
/interface/bridge/port/add bridge=bridge1 interface=sfp28-1 pvid=10
/interface/bridge/port/add bridge=bridge1 interface=sfp28-2 pvid=20

# 为桥接 VLAN 表创建新条目
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=10 untagged=bridge1,sfp28-1
/interface/bridge/vlan/add bridge=bridge1 vlan-ids=20 untagged=bridge1,sfp28-2
```

:::note
这适用于 IPv4 和 L2-forwardable（01-1B-19-00-00-00）传输模式。唯一的例外是 L2-non-forwardable（01-80-C2-00-00-0E），在这种情况下，无需在桥接 VLAN 表中添加桥接接口作为未标记端口。

要查看每个配置文件的默认（auto）传输模式值，请参阅[“常规属性](./precision-time-protocol.md#general-properties)”部分。
:::

#### 使用 IGMP 侦听的 PTP

如果您的桥接上启用了 IGMP 侦听，并且 VLAN 按照前一个示例配置，则必须为每个包含使用 **IPv4**（224.0.1.129）作为传输模式的 PTP 端口的 VLAN 手动添加静态组播数据库（MDB）条目。这可确保 PTP 组播流量的正确转发。

```routeros
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=10
/interface/bridge/mdb/add group=224.0.1.129 bridge=bridge1 ports=bridge1 vid=20
```

:::note
仅在启用 IGMP 侦听且同时配置 VLAN 时，才需要在 PTP 设置中添加静态 MDB 条目。
:::

## 监控

要监控 PTP 配置文件的状态和性能，请使用以下命令：

```ros
/system/ptp/monitor 0
```

输出将提供有关配置文件运行状态的详细信息：

```routeros
name: ptp1
clock-id: 64:D1:54:FF:FE:EB:AD:C7
priority1: 246
priority2: 248
i-am-gm: no
gm-clock-id: 64:D1:54:FF:FE:EB:AE:C3
gm-priority1: 100
gm-priority2: 248
master-clock-id: 64:D1:54:FF:FE:EB:AE:C3
slave-port: ether1
freq-drift: 2690 ppb
offset: 3 ns
hw-offset: -889419842 ns
slave-port-delay: 306 ns
```

此信息包括关键细节，如时钟 ID、优先级值和定时偏移，这些对于监控 PTP 设置的精度和同步至关重要。

#### 监控属性

| 属性 | 描述 |
| :-- | :-- |
| **clock-id:** | 本地时钟标识符，用于在 PTP 网络中唯一标识时钟。 |
| **priority1:** | 用于主时钟选举的优先级参数。数值越低表示优先级越高。 |
| **priority2:** | 用于备用主时钟选举的优先级参数。数值越低表示优先级越高。 |
| **i-am-gm:** yes \| no | 指示设备是否为主时钟（`yes`）或不是（`no`）。 |
| **gm-clock-id:** | 主时钟的标识符。这是提供主要时间源的时钟。 |
| **gm-priority1:** | 从从设备角度看到的主时钟的 `priority1` 值。 |
| **gm-priority2:** | 从从设备角度看到的主时钟的 `priority2` 值。 |
| **master-clock-id:** | PTP 通信路径中主时钟的标识符。根据网络拓扑，这可能是主时钟或边界时钟。 |
| **slave-port:** | 设备上连接到主时钟或主时钟的端口。 |
| **freq-drift:** | 主时钟和从时钟之间的频率漂移，以十亿分率（ppb）为单位。这表示从时钟频率与主时钟频率的偏差程度。 |
| **offset:** | 主时钟和从时钟之间的时间差，以纳秒（ns）为单位。这反映了同步精度。 |
| **hw-offset:** | 与硬件时钟的偏移差。 |
| **slave-port-delay:** | 数据包在两个设备之间传输的时间延迟，以纳秒（ns）为单位。此延迟可能受网络中使用的线缆和收发器质量的影响。 |
| **name**  | PTP 配置文件的名称。 |

## 支持的设备

- **CRS326-24G-2S+：** 仅在千兆以太网端口上支持。
- **CRS328-24P-4S+：** 仅在千兆以太网端口上支持。
- **CRS317-1G-16S+：** 在所有端口上支持。
- **CRS326-24S+2Q+：** 在 SFP+ 和 QSFP+ 接口上支持。
- **CRS312-4C+8XG：** 在所有端口上支持。
- **CRS318-16P-2S+：** 仅在千兆以太网端口上支持。
- **CRS318-1Fi-15Fr-2S：** 仅在 100M 以太网端口上支持。

### RouterOS 7.16 及更高版本中新增的 PTP 支持

- **CCR2116-12G-4S+：** 在所有端口上支持。
- **CCR2216-1G-12XS-2XQ：** 在所有端口上支持。
- **CRS518-16XS-2XQ：** 在所有端口上支持。
- **CRS504-4XQ：** 在所有端口上支持。
- **CRS510-8XS-2XQ：** 在所有端口上支持。
- **CRS520-4XS-16XQ：** 在所有端口上支持。

### RouterOS 7.17 及更高版本中新增的 PTP 支持

- **CRS320-8P-8B-4S+RM：** 仅在千兆以太网端口上支持。
- **CRS326-4C+20G+2Q+：** 在所有端口上支持。

### RouterOS 7.20 及更高版本中新增的 PTP 支持

- **RDS2216-2XG-4S+4XS-2XQ：** 在所有端口上支持。

:::info
本节未列出的设备不支持精确时间协议。
:::
:::info
任何设备上的 MGMT（管理）端口均不支持 PTP。“所有端口”指所有数据接口，不包括 MGMT 端口。
:::