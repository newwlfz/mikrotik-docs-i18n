# 蓝牙

> 本文档介绍 MikroTik RouterOS 的蓝牙 IoT 功能，涵盖蓝牙信道结构、广播数据包格式以及通过 `/iot/bluetooth` 子菜单进行的配置。文中解释了 PDU 类型、天线选择以及蓝牙芯片管理的设备命名，并说明了 iot 软件包或 USB 蓝牙适配器支持的要求。

import DocCardList from '@theme/DocCardList';

# 蓝牙

本节涵盖基于蓝牙的 IoT 示例。使用它来配置蓝牙标签跟踪，并将收集的数据与 MQTT 和 ThingsBoard 集成。

<DocCardList />

蓝牙是一种短距离无线技术，允许在特定的蓝牙信道上广播数据。

共有 40 个唯一频段（信道），每个频段间隔 2 MHz。信道 37、38 和 39 用于主要广播，0-36 用于数据传输。

在广播过程中，会广播 BLE 广播数据包。此数据包包含前导码、访问地址、PDU 和 CRC 字段。

前导码和访问地址字段帮助接收器检测帧。CRC 字段用于检查错误。PDU 由 PDU 头和 PDU 负载组成。PDU 定义了数据包本身。

PDU 头包含有关 PDU 类型的信息。根据类型，负载字段可能有所不同。

例如，当 PDU 类型为 ADV\_NOCONN\_IND 时 → PDU 负载由 "AdvA"（包含广播者地址信息的字段）和 "AdvData"（包含数据信息的字段）字段组成：

1 个八位组 = 1 字节 = 8 位

| 名称 | 长度 |
| :-- | :-- |
| 前导码 | 1 个八位组 |
| 访问地址 | 4 个八位组 |
| PDU | PDU 头 = 2 个八位组PDU 负载 = AdvA (6 个八位组) + AdvData (0...31 个八位组) |
| CRC | 3 个八位组 |

存在不同的 PDU 类型：

- ADV\_IND（负载由 AdvA [6个八位组] + AdvData [0-31 个八位组] 组成，用于可连接、可扫描的非定向广播）。
- ADV\_NOCONN\_IND（负载由 AdvA [6个八位组] + AdvData [0-31 个八位组] 组成，用于不可连接、不可扫描的非定向广播）。
- ADV\_SCAN\_IND（负载由 AdvA [6个八位组] + AdvData [0-31 个八位组] 组成，用于可扫描的非定向广播）。
- SCAN\_REQ（负载由 ScanA [6个八位组] + AdvA [6个八位组] 组成，其中 ScanA 字段包含扫描者地址，AdvA 包含广播者地址，用于请求 SCAN\_RSP 响应）。
- SCAN\_RSP（负载由 AdvA [6个八位组] + ScanRspData [0-31 个八位组] 组成，其中 ScanRspData 可以包含来自广播者主机的任何数据，用于响应 SCAN\_REQ 请求）。
- ADV\_DIRECT\_IND（负载由 AdvA [6个八位组] + TargetA [6个八位组] 组成，其中 TargetA 是 PDU 寻址的设备地址字段，用于可连接的定向广播）。
- 等等。

您可以在[此处](https://www.bluetooth.com/specifications/specs/core-specification/)（蓝牙规范）找到有关数据包结构的更多信息。

RouterOS 中蓝牙接口的主要应用是监控其他设备（例如 [蓝牙标签](https://help.mikrotik.com/docs/display/UM/TG-BT5-IN)）广播的蓝牙广播数据包（扫描器功能）或广播广播数据包（广播器功能）。

## 配置

**子菜单：** `/iot/bluetooth`

:::info
对于具有内置蓝牙芯片的设备（如 [KNOT](https://mikrotik.com/product/knot) 或 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4)），需要 **iot** 软件包。

如果您的设备是 ARM、ARM64 架构并且具有 USB 插槽，则 **iot-bt-extra** 软件包可以通过 USB 蓝牙适配器启用蓝牙功能。并非所有蓝牙适配器都经过测试。适配器必须支持 **LE 4.0+**。目前尚无“外设”列表。

**Iot** 软件包可从 RouterOS 版本 6.48.3 开始使用。**Iot-bt-extra 软件包** 可从 RouterOS 7.18 开始使用。您可以从我们的[下载页面](https://mikrotik.com/download)获取它们 - 位于“额外软件包”下。
:::

### 设备

在此菜单中，您可以检查和设置通用蓝牙芯片参数：

```ros
/iot/bluetooth/print
Columns: NAME, PUBLIC-ADDRESS, RANDOM-STATIC-ADDRESS, ANTENNA
  #  NAM  PUBLIC-ADDRESS     RANDOM-STATIC-ADD  ANTENNA 
  0  bt1  00:00:00:00:00:00  F4:4E:E8:04:77:3A  internal
/iot/bluetooth/set
```

***注意**：* 公共地址是 IEEE 注册的永久地址。此地址无法更改。在上面的“print”示例中，设备没有分配公共地址（所有八位组都设置为 0）。

可配置设置如下所示：

| 属性 | 描述 |
| :-- | :-- |
| **antenna** (*字符串*; 默认值：internal) | 选择使用内部还是外部蓝牙天线 |
| **name** (*字符串*; 默认值：) | 蓝牙芯片/接口的描述性名称 |
| **random-static-address** (*MAC 地址*; 默认值：) | 蓝牙芯片的用户可配置地址 |

您可以使用以下命令监控芯片统计信息：

```ros
/iot/bluetooth/print stats
Columns: NAME, RX-BYTES, TX-BYTES, RX-ERRORS, TX-ERRORS, RX-EVT, TX-CMD, RX-ACL, TX-ACL
  #  NAM  RX-BYTE  TX-  R  T  RX-EV  TX  R  T
  0  bt1  1857835  235  0  0  46677  45  0  0
```

### 广播器

在此菜单中，可以设置蓝牙芯片以广播广播数据包。您可以使用以下命令检查和设置广播器设置：

```ros
/iot/bluetooth/advertisers/print
Flags: X - DISABLED
Columns: DEVICE, MIN-INTERVAL, MAX-INTERVAL, OWN-ADDRESS-TYPE, CHANNEL-MAP, AD-SIZE
#   DEVICE  MIN-INTERVAL  MAX-INTERVAL  OWN-ADDRESS-TYPE  CHANNEL-MAP  AD-SIZE
0 X bt1     1280ms        2560ms        random-static              37        0
                                                                   38         
                                                                   39         
/iot/bluetooth/advertisers/set
```

可配置设置如下所示：

| 属性 | 描述 |
| :-- | :-- |
| **ad-structures** (*字符串*; 默认值：) | 为广播数据包选择预配置的结构。更多信息请参阅“AD 结构”部分。 |
| **channel-map** (*37 \| 38 \| 39*; 默认值：37, 38, 39) | 用于广播的信道。 |
| **disabled** (*是 \| 否*; 默认值：**是**) | 禁用或启用蓝牙芯片广播广播数据包的选项。 |
| **max-interval** (*整数:*20..10240;** 默认值：**2560** **ms**) | 广播广播数据包的最大间隔。 |
| **min-interval** (*整数:*20..10240;** 默认值：**1280 ms**) | 广播广播数据包的最小间隔。 |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; 默认值：**random-static**) | 将在广播数据包负载中使用的 MAC 地址：public → 使用 IEEE 注册的永久地址。random-static → 使用用户可配置的地址（将在下次重新上电时更改）。rpa-fallback-to-public → 使用可解析的随机私有地址 (RPA)，仅当接收方拥有我们的身份解析密钥 (IRK) 时才能解析。如果无法生成 RPA，则将改用公共地址。rpa-fallback-to-random → 与“rpa-fallback-to-public”相同，但如果无法生成 RPA，则将改用 random-static 地址。 |
| **phy** (*1M \| 2M \| CODED*; 默认值：**1M**) | 设置设备在广播期间使用的“物理层”：CODED → 最低速率 125 kbps = 更远距离；1M → 标准速率 1 Mbps = 平均距离；2M → 最高速率 2 Mbps = 短距离；**重要提示：** CODED 仅受 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4) 支持。 |
| **legacy** (*是 \| 否*) | 设置广播类型 → 扩展或传统。 当使用 `legacy=no` 时，AD 结构长度扩展至 191 字节。当使用 `legacy=yes` 时，AD 结构长度限制为 31 字节。 传统广播仅使用“主”蓝牙信道来广播负载。扩展广播同时使用“主”和“辅”信道。 |

***注意**：* 广播数据包将在每个 *min-interval* \<= **X** \<= *max-interval* 毫秒内广播。

### AD 结构

此部分允许您定义将由蓝牙芯片广播的广播数据包的负载。

目前仅支持 4 种类型：0x08 “缩短本地名称”；0x09 “完整本地名称”；0xFF “制造商特定数据”；“服务数据”

您可以使用以下命令检查和设置“AD 结构”设置：

```ros
/iot/bluetooth/advertisers/ad-structures/print
Columns: NAME, TYPE, DATA
#  NAME  TYPE              DATA
0  test  short-local-name  TEST
/iot/bluetooth/advertisers/ad-structures/set 
```

可配置属性如下所示：

| 属性 | 描述 |
| :-- | :-- |
| **data** (*字符串*; 默认值：) | 定义广播数据包负载的 AdvData 部分 |
| **name**(*字符串*; 默认值：) | AD 结构的描述性名称 |
| **type** (complete-local-name \| manufacturer-data \| short-local-name \| service-data; 默认值：) | 设置 AD 结构类型的选项：0x08 “缩短本地名称”（“文本”格式）0x09 “完整本地名称”（“文本”格式）0xFF “制造商特定数据”（“十六进制”格式）0x20 “服务数据 32 位”（“十六进制”格式） |

例如，如果选择了“缩短本地名称”类型，并且“data”字段配置为“TEST” → 负载的 AdvData 部分将如下所示：

05 08 54 45 53 54（十六进制格式）

，其中第一个八位组 (05) 表示后续字节数（5 字节），第二个八位组 (08) 表示类型（缩短本地名称）。第 3、4、5 和 6（等）个八位组是“数据”[54 (十六进制)=**T** (ASCII)，45 (十六进制)=**E** (ASCII)，53 (十六进制)=**S** (ASCII)，54 (十六进制)=**T** (ASCII)]。

“完整本地名称”类型同理。只有 AdvData 负载中的第二个八位组会不同，将设置为 09。

对于“制造商特定数据”类型，您需要以十六进制格式配置“data”字段。此类型的第二个八位组将设置为 FF。

### 连接

:::info
从 v**7.12beta9** 版本开始可用。
:::

目前仅支持 `central` 角色。不支持 `外设设备` 角色、`配对` 和 `加密` 选项。

可用部分包括：

| 部分 | 描述 |
| :-- | :-- |
| async-data | 用于查看已订阅的数据。 |
| characteristics | 用于查看设备支持的所有特征。 |
| connect | 用于连接到处于 `可连接` 状态的设备。 |
| disconnect | 用于断开与设备的连接。 |
| read | 用于读取特征值。 |
| write | 用于写入特征值。 |
| subscribe | 用于订阅特征值。 |
| unsubscribe | 用于取消订阅特征值。 |

为了连接到处于 `可连接` 状态的蓝牙设备，请使用以下命令（其中 `pdev` 是设备地址）：

```ros
/iot/bluetooth/connections/connect pdev=DC:2C:6E:0F:C0:3D
```

:::info
要连接到 TG-BT5-IN/OUT 标签，请确保通过将磁铁靠近磁簧开关将其置于 `可连接` 状态。
:::

查看已建立的连接：

```ros
/iot/bluetooth/connections/print
```

查看设备特征：

```ros
/iot/bluetooth/connections/characteristics/print
Columns: PDEV, NAME, UUID
 #  PDEV               NAME                              UUID                            
 0  DC:2C:6E:0F:C0:3D  Service Changed                   2a05                            
 1  DC:2C:6E:0F:C0:3D  Database Hash                     2b2a                            
 2  DC:2C:6E:0F:C0:3D  Client Supported Features         2b29                            
 3  DC:2C:6E:0F:C0:3D  Device Name                       2a00                            
 4  DC:2C:6E:0F:C0:3D  Appearance                        2a01                            
...
...
...
```

要读取特定特征，请指定 `pdev` 地址和 `uuid`：

```ros
/iot/bluetooth/connections/read pdev=DC:2C:6E:0F:C0:3D uuid=2a00
```

### 扫描器

在此菜单中，您可以设置蓝牙芯片的扫描器设置。禁用后，设备将无法再接收广播报告。启用后，您可以在“广播报告”选项卡中监控广播报告（稍后将在本指南中说明）。您可以使用以下命令检查和设置扫描器设置：

```ros
/iot/bluetooth/scanners/print
Flags: X - DISABLED
Columns: DEVICE, TYPE, INTERVAL, WINDOW, OWN-ADDRESS-TYPE, FILTER-POLICY, FILTER-DUPL
ICATES
#   DEVICE  TYPE     INTERVAL  WINDOW  OWN-ADDRESS-TYPE  FILTER-POLICY  FIL
0 X bt1     passive  10ms      10ms    random-static     default        off
/iot/bluetooth/scanners/set
```

可配置属性如下所示：

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*是 \| 否*; 默认值：**否**) | 禁用或启用蓝牙芯片接收广播报告的选项。 |
| **filter-duplicates** (keep-newest \| keep-oldest \| keep-unique \| off; 默认值：**off**) | 丢弃来自同一广播者的重复广播的选项：keep-newest → 保留最新的报告（丢弃最旧的）。将仅保留来自单个 AdvA 的最新 PDU。keep-oldest → 保留最旧的报告（丢弃最新的）。将仅保留来自单个 AdvA 的最旧 PDU。这种类型的 PDU 过滤发生在控制器级别，因此它是重复过滤最有效（在能量/带宽方面）的方法。keep-unique → 仅显示具有唯一负载的广播。这意味着，如果发现 1+ 个相同的负载 (AdvData)，则仅显示第一个负载，而“克隆”将被丢弃/忽略。off → 不丢弃重复项。将保留所有具有相同 AdvA 的 PDU。**重要提示：** 重复广播报告是从同一设备地址发送的广播报告。实际数据（负载的“AdvData”部分）可能会变化/不同，并且在确定重复广播报告时不被视为重要。这意味着，例如，如果蓝牙接口从同一标签接收到 10 个负载（一个接一个，间隔 1 秒）： 如果您使用“keep-oldest”设置 → 蓝牙接口将仅显示从该标签接收到的第一个负载（后续 9 个负载将被过滤掉）。如果您使用“keep-newest”设置 → 蓝牙接口将仅显示最后接收到的负载（每个后续负载将覆盖前一个负载）。 |
| **filter-policy** (default \| whitelist *\| no*; 默认值：**default**) | 设置过滤策略的选项（控制器级广播过滤）：default → 启用此策略时，扫描器将仅接受 ADV_IND、ADV_NOCONN_IND、ADV_SCAN_IND、SCAN_RSP 和 ADV_DIRECT_IND（其中 TargetA 是扫描器自身的蓝牙地址）PDU 类型。whitelist → 启用此策略时，扫描器将仅接受由广播者广播的 ADV_IND、ADV_NOCONN_IND、ADV_SCAN_IND、SCAN_RSP PDU 类型，该广播者的地址在“白名单”部分中配置，以及 ADV_DIRECT_IND 类型 PDU（其中 TargetA 是扫描器自身的蓝牙地址）。 |
| **interval** (*整数:3..10240*;** 默认值：**10 ms**) | 扫描器开始扫描下一个广播信道之前的时间。 |
| **own-address-type** (*public \| random-static \| rpa-fallback-to-public \| rpa-fallback-to-random*; 默认值：**random-static**) | 扫描请求中使用的地址类型（如果使用主动扫描类型）：public → 使用 IEEE 注册的永久地址。random-static → 使用用户可配置的地址（将在下次重新上电时更改）。rpa-fallback-to-public → 使用可解析的随机私有地址 (RPA)，只能使用我们的身份解析密钥 (IRK) 解析。如果无法生成 RPA，则将改用公共地址。rpa-fallback-to-random → 与“rpa-fallback-to-public”相同，但如果无法生成 RPA，则将改用 random-static 地址。 |
| **type** (*active \| passive;* 默认值：**passive**) | 定义扫描器的类型：active → 如果扫描器接收到可扫描的广播，则可以发送扫描请求。扫描器可以发送 SCAN_REQ 以获取 SCAN_RSP 响应。passive → 扫描器将仅侦听广播，不会发送任何数据（例如扫描请求）。 |
| **window** (*整数:3..10240;* 默认值：**10 ms**) | 扫描器在单个广播信道上花费的扫描时间。 |
| **phy** (*1M \| 2M \| CODED*; 默认值：**1M**) | 设置设备在扫描期间使用的“物理层”：CODED → 最低速率 125 kbps = 更远距离；1M → 标准速率 1 Mbps = 平均距离；2M → 最高速率 2 Mbps = 短距离；**重要提示：** CODED 仅受 [KNOT Embedded LTE](https://mikrotik.com/product/knot_embedded_lte4) 支持。 |

例如，如果扫描器间隔设置为 20ms，这意味着设备将在 20ms 后才开始扫描下一个信道。如果扫描器窗口设置为 10ms，这意味着设备将仅在该 10ms 窗口内扫描每个信道。这意味着它将扫描信道 37 持续 10ms（窗口时间），并在 10ms 后（20ms[间隔]-10ms[窗口]）开始扫描下一个信道。扫描信道 38 将花费 10ms，再过 10ms 后，设备将开始扫描信道 39。

扫描器将能够同时捕获“扩展”和“传统”广播类型。

### 广播报告

在此部分中，可以监控蓝牙广播报告（来自附近的广播者）。列表限制为 1024 个条目（如果列表满 1024 个条目，则每个新接收到的负载将覆盖“最旧”的负载）。您可以使用以下命令监控广播报告：

```ros
/iot/bluetooth/scanners/advertisements/print      
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI
 #  DEV  PDU-TYPE        TIME                  ADDRES  ADDRESS            RSSI  
 0  bt1  adv-noconn-ind  2021-07-28 09:30:56  public  2C:C8:1B:93:16:49  -24dBm
 1  bt1  adv-noconn-ind  2021-07-28 09:30:56  random  0B:16:17:9E:7B:EF  -60dBm
```

可以使用以下命令为报告设置过滤器：

```ros
/iot/bluetooth/scanners/advertisements/print where  
```

例如，要打印由特定蓝牙地址广播的报告，请使用以下命令：

```ros
/iot/bluetooth/scanners/advertisements/print where address=XX:XX:XX:XX:XX:XX
 # DEVICE    PDU-TYPE       TIME                 ADD... ADDRESS                    RSSI     LENGTH DATA    
79 bt1       adv-noconn-ind 2021-07-28 09:46:38 public XX:XX:XX:XX:XX:XX        -70dBm         30 02010...
80 bt1       adv-noconn-ind 2021-07-28 09:46:43 public XX:XX:XX:XX:XX:XX        -67dBm         30 02010...
81 bt1       adv-noconn-ind 2021-07-28 09:46:44 public XX:XX:XX:XX:XX:XX        -70dBm         28 1bff0...
82 bt1       adv-noconn-ind 2021-07-28 09:46:48 public XX:XX:XX:XX:XX:XX        -75dBm         30 02010...
```

要仅显示 RSSI 强于 -30 dBm 的广播报告，请使用以下命令：

```ros
/iot/bluetooth/scanners/advertisements/print where rssi > -30
 # DEVICE         PDU-TYPE       TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA       
307 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -24dBm         22 15ff4f09.>
308 bt1            adv-noconn-ind 2021-07-29 10:11:31 public       2C:C8:1B:93:16:49        -26dBm         22 15ff4f09.>
```

可能的过滤器（您可以借助以下参数过滤广播报告列表）：

| 过滤器 | 描述 |
| :-- | :-- |
| **address** | 蓝牙广播者地址 |
| **address-type** | 广播者地址类型（例如，public 或 random） |
| **data** | 十六进制格式的广播数据（AdvData 负载） |
| **device** | 蓝牙芯片/接口名称 |
| **epoch** | 自 Unix 纪元以来的毫秒数 |
| **filter-comment** | 匹配的白名单过滤器的注释 |
| **length** | 广播数据长度 |
| **pdu-type** | 广播 PDU 类型 |
| **rssi** | 信号强度 |
| **time** | 广播数据包接收时间 |

### 白名单

在此选项卡中，可以配置将在“扫描器”部分的过滤策略中使用的白名单。换句话说，这是一个指定将扫描哪些蓝牙地址（显示在“广播报告”中）的选项。

您可以使用以下命令查看白名单条目：

```ros
/iot/bluetooth/whitelist/print
Columns: DEVICE, ADDRESS-TYPE, ADDRESS
# DEVICE  ADDRESS-TYPE  ADDRESS    
0 bt1     any           *:*:*:*:*:*
```

您可以使用以下命令添加新的白名单条目：

```ros
/iot/bluetooth/whitelist/add
```

### 可配置属性

| 属性 | 描述 |
| :-- | :-- |
| **address** (*MAC 地址*; 默认值：) | 广播者地址 |
| **address-type** (*any \| public \| random*; 默认值：) | 广播者地址类型 |
| **comment**(*字符串*; 默认值：) | 白名单条目的简短描述 |
| **copy-from** | 复制条目的选项 - 更多信息请参阅 [控制台命令](../../developer-guides/scripting/index.md#common-commands) |
| **device** (*bt1*; 默认值：) | 选择蓝牙接口/芯片名称 |
| **disabled** (*是 \| 否*; 默认值：) | 禁用或启用条目的选项 |

:::info
在 **7.14beta8** 版本之前，只能添加 8 个白名单条目。
从 **7.14beta8** 版本开始，白名单不再限制为 8 个条目，并且地址字段支持星号通配符。
:::

例如，如果您想白名单所有以“DC:2C:...”八位组开头的 MAC 地址，请使用星号通配符添加条目：

```ros
/iot/bluetooth/whitelist/add address=DC:2C:*:*:*:*
```

星号通配符不能用在特定八位组之间，例如 `AA:*:*:BB:*:*`（这是无效条目）。

有效条目包括：

- `AA:BB:CC:DD:*:*`
- `AA:BB:CC:DD:EE:*`
- `AA:*:*:*:*:*`

### 外设设备

此部分显示解码后的 Eddystone TLM、Eddystone UID、iBeacon 和 MikroTik 蓝牙负载。如果“外设设备”捕获到其他信标类型，则不会对其进行解码。

您可以使用 `print detail` 命令查看解码列表：

```ros
/iot/bluetooth/peripheral-devices/print detail 
 0 address-type=public address=60:C0:BF:87:E2:1C name="60:C0:BF:87:E2:1C" persist=no 
   mtik-key="" rssi=-64 
   last-data="0201041BFFCD0960C0BF87E21C025B1F198B21AC62CDAE0045FAFEFE057D7B" 
   last-seen=2023-08-22 11:20:09 beacon-types="" 

 1 address-type=public address=DC:2C:6E:0F:C0:3D name="DC:2C:6E:0F:C0:3D" persist=no 
   mtik-key="" rssi=-47 
   last-data="0303AAFE1716AAFE00E5B2B98DE4C81C47C2B14E7500000000000000" 
   last-seen=2023-08-22 11:20:05 beacon-types=mikrotik,ibeacon,eddystone-uid 
   mtik-version=1 mtik-encrypted=no mtik-acc-x=-0.007G mtik-acc-y=-0.015G 
   mtik-acc-z=-0.007G mtik-temperature=23.808C mtik-battery=100% 
   mtik-uptime=14342160s mtik-flags="" 
   ibeacon-uuid="55555555-5555-5555-5555-222222222222" ibeacon-major=1280 
   ibeacon-minor=512 ibeacon-rssi-at-1m=-68dBm eddy-rssi-at-1m=-27dBm 
   eddy-namespace="b2b98de4c81c47c2b14e" eddy-instance="750000000000" 

 2 address-type=public address=DC:2C:6E:F6:54:7D name="DC:2C:6E:F6:54:7D" persist=no 
   mtik-key="" rssi=-74 
   last-data="0201060303AAFE1116AAFE20000B701549023532D802384F46" 
   last-seen=2023-08-22 11:20:13 beacon-types=eddystone-tlm eddy-version=0 
   eddy-battery-voltage=2.928V eddy-temperature=21.285C eddy-packet-count=37040856 
   eddy-uptime=3724474.2s 

 3 address-type=public address=DC:2C:6E:0F:C0:3E name="DC:2C:6E:0F:C0:3E" persist=no 
   mtik-key="" rssi=-72 last-data="15FF4F0901000214FFFF0200FDFF4F1774E00F000064" 
   last-seen=2023-08-22 11:20:06 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.003G mtik-acc-y=0.007G mtik-acc-z=-0.011G 
   mtik-temperature=23.308C mtik-battery=100% mtik-uptime=1040500s mtik-flags="" 

 4 address-type=public address=60:C0:BF:20:9A:50 name="60:C0:BF:20:9A:50" persist=no 
   mtik-key="" rssi=-66 
   last-data="0201041BFF4160C0BF209A50FFA4CA8906E48C0377DCFDD2DF7AF02FFC6AC5" 
   last-seen=2023-08-22 11:20:11 beacon-types="" 
```

您可以过滤列表，例如，根据设备的“address”（知道标签的 MAC 地址）：

```ros
/iot/bluetooth/peripheral-devices/print detail where address="DC:2C:6E:0F:C0:3E"
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-60 last-data="15FF4F090100669DFCFF0600FCFF6117F1E50F000064" 
   last-seen=2023-08-22 11:43:31 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=-0.015G mtik-acc-y=0.023G mtik-acc-z=-0.015G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1041905s mtik-flags=""

/iot/bluetooth/peripheral-devices/print value-list where address="DC:2C:6E:0F:C0:3E"
      address-type: public
           address: DC:2C:6E:0F:C0:3E
              name: my_tag
           persist: yes
          mtik-key: 
              rssi: -71
         last-data: 15FF4F0901002AC60400000004004F17D4E90F000064
         last-seen: 2023-08-22 12:00:06
      beacon-types: mikrotik
      mtik-version: 1
    mtik-encrypted: no
        mtik-acc-x: 0.015G
        mtik-acc-y: 0G
        mtik-acc-z: 0.015G
  mtik-temperature: 23.308C
      mtik-battery: 100%
       mtik-uptime: 1042900s
        mtik-flags: 
```

或者，例如，根据信标类型过滤列表：

```ros
/iot/bluetooth/peripheral-devices/print detail where beacon-types=mikrotik 
 0 address-type=public address=DC:2C:6E:0F:C0:3E name="my_tag" persist=yes 
   mtik-key="" rssi=-69 last-data="15FF4F0901000747020002000100611778E60F000064" 
   last-seen=2023-08-22 11:45:46 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0.007G mtik-acc-y=0.007G mtik-acc-z=0.003G 
   mtik-temperature=23.378C mtik-battery=100% mtik-uptime=1042040s mtik-flags="" 

 7 address-type=public address=2C:C8:1B:4B:BB:0A name="2C:C8:1B:4B:BB:0A" persist=no 
   mtik-key="" rssi=-44 last-data="15FF4F09010077090000FCFFFDFFD519BF9EFF00005B" 
   last-seen=2023-08-22 11:45:53 beacon-types=mikrotik mtik-version=1 
   mtik-encrypted=no mtik-acc-x=0G mtik-acc-y=-0.015G mtik-acc-z=-0.011G 
   mtik-temperature=25.832C mtik-battery=91% mtik-uptime=16752319s mtik-flags="" 
```

此外，您可以选择设置 `persist=yes`，这将确保设备/标签永远保留在列表中（因为停止广播负载的设备将在一分钟后超时并从列表中移除，直到新的负载开始在空中出现）：

```ros
/iot/bluetooth/peripheral-devices/set persist=yes address="DC:2C:6E:0F:C0:3E"
```

您还可以为设备设置名称，以便更容易在列表中找到它，使用以下命令：

```ros
/iot/bluetooth/peripheral-devices/set name="my_tag" address="DC:2C:6E:0F:C0:3E"
```

### 解码广播数据

在此菜单中，您可以解码静态 MikroTik、Eddystone TLM、Eddystone UID 和 iBeacon 负载。

要解码负载，只需将其输入到“data”字段中：

```ros
/iot/bluetooth/decode-ad data=0201060303AAFE1116AAFE20000B6E158402353AF20238576B 
             type: eddystone-tlm
          version: 0
  battery-voltage: 2.926V
      temperature: 21.515C
     packet-count: 37042930
           uptime: 3724682.7s

/iot/bluetooth/decode-ad data=15FF4F090100032E0100FFFF00004F17C1E80F000064      
         type: mikrotik
      version: 1
    encrypted: no
        acc-x: 0.003G
        acc-y: -0.003G
        acc-z: 0G
  temperature: 23.308C
       uptime: 1042625s
        flags: 
      battery: 100%
```