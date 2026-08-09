# 通用属性

> 本文档介绍了在 MikroTik RouterOS 上设置 LoRaWAN 网关的配置，包括天线增益、信道规划、服务器连接和流量转发规则。它解释了如何启用网关、选择频段、配置 LBT 协议，以及如何通过 `/iot/lora` 和 `/iot/lora/channels` 等子菜单管理信道。

# 通用属性

任何带有支持 LTE 调制解调器的 miniPCI-e 插槽的 RouterBOARD，都可以通过安装 **R11e-LR8** 或 **R11e-LR9** 网卡用作 LoRaWAN 网关。支持 UDP 和 LNS（从 **v7.12rc1** 测试版开始）协议。

:::info
为了使用 LoRa 功能，需要安装 IoT 软件包。您可以在[下载](https://mikrotik.com/download)页面的附加软件包存档中找到适用于您设备架构的软件包。

**重要提示：** 从 **v7.11**（稳定版）开始，LoRa 功能已移至[下载](https://mikrotik.com/download)页面附加软件包下的 **IoT 软件包** 中。单独的 Lora 软件包仍可下载。

使用 IoT 软件包时，LoRa 功能将移至 `/iot/lora` 子菜单。使用 LoRa 软件包时，LoRa 功能可通过 `/lora` 子菜单使用。

LoRa 软件包不再是必需的，仅出于兼容性原因保留。

**注意：** ***注意**：* RouterOS 不支持第三方 LoRaWAN 网关网卡。
:::

## 属性

此菜单用于将设置应用于 LoRa 接口。

**子菜单：** `/iot/lora`

| 属性 | 描述 |
| :-- | :-- |
| **antenna-gain** (*整数 [-128..127]*; 默认值：**0**) | 天线增益，单位为 dBi。此值应等于 `setup-antenna-gain` 减去 `cable-loss`。使用 6.5 dBi 天线时，配置值为 6.5（不考虑线缆损耗）。网关的输出功率由服务器决定。网关将通过从 `server_value`（下行消息中接收到的值）中减去 `antenna-gain` 设置来计算其实际输出功率。 |
| **channel-plan** (*2.4-ghz \| as-923 \| as-923-2 \| as-923-3 \| as-923-4 \| au-915 \| au-915-1 \| au-915-2 \| custom \| eu-868 \| in-865 \| kr-920 \| ru-864 \| ru-864-mid \| us-915 \| us-915-1 \| us-915-2 \| us-915-3 \| us-915-4 \| us-915-5 \| us-915-6 \| us-915-7 \| us-915-8*; 默认值：**eu-868**) | 适用于不同地区的频率规划。 |
| **disabled** (*yes \| no*; 默认值：**yes**) | LoRaWAN 网关是否禁用。 |
| **forward** (*crc-validation \| dev-addr-validation \| proprietary-traffic*; 默认值：**crc-validation**) | 定义应转发哪些类型的数据包到网络服务器：crc-validation - 转发具有正确 CRC 的有效数据包。dev-addr-validation - 检查数据包的 DevAddr 是否与 NetID 对应，如果不匹配则丢弃数据包。具体流程如下：1) 从接收到的 LoRa 数据包中“获取”Dev. Addr 值；2) 将 Dev. Addr 与“有效”的 Net ID 列表进行“比较”；3) 如果 Dev. Addr 没有对应的 Net ID，则不转发数据包；4) 如果 Net ID 有效，Dev. Addr 范围有效，则转发数据包。proprietary-traffic - 检查 LoRa 数据包的内容，如果帧的“类型”是“proprietary”，则不转发该数据包。 |
| **gateway-id**(字符串) | 向服务器注册网关时使用的网关 ID 或网关 EUI。 |
| **lbt-enabled** (*yes \| no*; 默认值：**no**) | 网关是否应使用 LBT（先听后说）协议。 |
| **listen-time** (*整数 [0us..4294967295us]*; 默认值：**5000us**) | 在 TX 之前跟踪 RSSI 的时间（微秒）（当 **lbt-enabled=yes** 时使用）。 |
| **name** (*字符串*; 默认值：) | LoRaWAN 网关的名称。 |
| **network** (*private \| public*; 默认值：**public**) | 通信是否应使用同步字（network=private）或不使用（network=public）。 |
| **rssi-threshold** (*整数 [-32,768 .. 32,767]*; 默认值：**-65dBm**) | 用于确定转发器是否可以使用特定信道通信的 RSSI 值。如果 RSSI 值低于 **rssi-threshold**，则可以使用该信道（当 **lbt-enabled=yes** 时使用）。 |
| **servers** (*字符串列表*; 默认值：) | 来自 `/iot/lora/servers` 部分的服务器名称。 |
| **src-address** (*IP*; 默认值：) | 如有必要，指定上行数据包的源地址（地址应与 RB 上配置的地址匹配）。 |
| **spoof-gps** (*bool \| lat \| long \| alt*; 默认值：) | 设置自定义 GPS 位置。使用 `lat`、`long`、`alt` 指定纬度、经度和海拔值。 |

:::info
一旦选择了服务器并使用 `/iot/lora/enable [find]` 命令启用了 LoRa 接口，设备将开始作为 LoRaWAN 网关运行。它将开始将来自 [`/iot/lora/traffic`](./general-properties.md#traffic) 选项卡的 LoRa 负载转发到配置的服务器。
:::

## 信道

此部分用于修改与信道/频率相关的设置。

**子菜单：** `/iot/lora/channels`

| 属性 | 描述 |
| :-- | :-- |
| **bandwidth** (*200\_kHz \| 400\_kHz \| 62.5\_kHz \| 125\_kHz \| 250\_kHz \| 500\_kHz*; 默认值：**125\_kHz**) | 特定信道的带宽，使用任何信道规划预设时预定义，但当信道规划设置为自定义时可以手动更改。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 禁用或启用信道。 |
| **freq-off** (*整数* [-400000..400000]; 默认值：) | 信道频率相对于无线电中心频率的偏移，可以调整信道频率以避免信道重叠。 |
| **radio** (*radio0 \| radio1*; 默认值：) | 定义哪个无线电使用所选信道。 |
| **spread-factor** (*SF5 \| SF6 \| SF7 \| SF8 \| SF9 \| SF10 \| SF11 \| SF12*; 默认值：) | 定义 type=LoRa 信道的扩频因子。较低的扩频因子意味着较高的数据速率。 |

要查看当前信道，请执行命令 `/iot/lora/channels/print`：

```ros
/iot/lora/channels/print
Columns: NAME, TYPE, RADIO, FREQ-OFF, BANDWIDTH, FREQ, SPREAD-FACTOR, DATARATE
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1                         
1 gateway-0  MSF   radio1  -200000   125_kHz    868.3                         
2 gateway-0  MSF   radio1  0         125_kHz    868.5                         
3 gateway-0  MSF   radio0  -400000   125_kHz    867.1                         
4 gateway-0  MSF   radio0  -200000   125_kHz    867.3                         
5 gateway-0  MSF   radio0  0         125_kHz    867.5                         
6 gateway-0  MSF   radio0  200000    125_kHz    867.7                         
7 gateway-0  MSF   radio0  400000    125_kHz    867.9                         
8 gateway-0  LoRa  radio1  -200000   250_kHz    868.3  SF7                    
9 gateway-0  FSK   radio1  300000    125_kHz    868.8                    50000
```

信道是使用 `freq-off` 和无线电的 `center-freq` 频率创建的。要查看**无线电**的中心频率，请使用命令 `/iot/lora/radios/print`。

要了解每个信道的频率是如何计算的，请参考以下示例：

```ros
# NAME       TYPE  RADIO   FREQ-OFF  BANDWIDTH  FREQ   SPREAD-FACTOR  DATARATE
0 gateway-0  MSF   radio1  -400000   125_kHz    868.1                         
```

选择 `radio1` 用于信道 #0，其配置的 `center-freq=868500000`（868500000 Hz 或 868.5 MHz）。

通过使用频率偏移 `freq-off=-400000`（-400000 Hz 或 -0.4 MHz），我们将信道 #0 定义为 `868500000-400000=868100000` Hz 或 868.1 MHz。

:::info
要配置自定义信道，请使用以下命令选择“custom”信道配置文件：

```ros
/iot/lora/set [find] channel-plan=custom
```

:::

## Join EUI

网关将把接收到的每一个 LoRaWAN 负载转发到服务器。这包括邻近 LoRaWAN 节点的负载。转发所有内容可能并不理想，例如，这会增加使用的数据量（并直接影响 ISP 套餐费用）。

Join EUI 菜单允许您指定网关应转发（如果是“白名单”）或应阻止（如果是“黑名单”）的 JOIN EUI 黑名单或白名单范围。添加范围后，请确保将其应用到[服务器](./general-properties.md#servers)设置。

过滤器的工作原理如下：

1) 默认情况下，允许所有内容（除非添加了白名单/黑名单过滤器）；

2) **如果添加了“黑名单”过滤器范围**，并且附近出现与黑名单范围匹配的 JOIN EUI 数据包 → **它将被丢弃**；

3) **如果添加了“白名单”过滤器范围，则其优先级高于“黑名单”过滤器**。这意味着如果“黑名单”和“白名单”都匹配同一个 JOIN EUI，则“白名单”优先，数据包将被转发。

您可以通过 RouterOS GUI 找到节点使用的 Join EUI。转到“LoRa”部分和“Traffic”子菜单（仅可通过图形界面使用）。为 LoRaWAN 节点上电后，节点应发送一个“Join-request”数据包。双击它以检查：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/img/general-properties-01.webp)

**子菜单：** `/iot/lora/joineui`

| 属性 | 描述 |
| :-- | :-- |
| **joineuis** (*字符串*; 默认值：) | 定义 Join EUI 的范围。 |
| **logging**(*yes \| no*; 默认值：no) | 为过滤器功能启用额外的日志记录。 |
| **name** (*字符串*; 默认值：) | 定义范围的名称。 |
| **type** (blacklist \| whitelist; 默认值：whitelist) | 定义过滤器的类型：blacklist（如果范围匹配，则阻止/丢弃数据包）whitelist（如果范围匹配，则转发数据包） |

Join EUI 的示例格式如下 **E0 E1 E2 01 02 03 04 05**。它由 8 个十六进制格式的八位字节组成。

要添加一个**阻止所有内容**的范围，请添加如下过滤器：

```ros
/iot/lora/joineui/add name=block_all joineuis=0000000000000000-ffffffffffffffff type=blacklist logging=yes
```

要允许特定的单个 Join EUI，请添加如下过滤器：

```ros
/iot/lora/joineui/add name=allow_my_node joineuis=E0E1E20102030405-E0E1E20102030405 type=whitelist logging=yes
```

禁用 LoRa 接口：

```ros
/iot/lora/disable [find where ]
```

将两个范围应用到您正在使用的 LoRa 服务器，然后重新启用接口：

```ros
/iot/lora/servers/set joineui=block_all,allow_my_node [find where address ~ "eu1.cloud.thethings.network"]
/iot/lora/enable [find where ]
```

结果，我们将只允许“JOIN EUI=**E0 E1 E2 01 02 03 04 05**”节点的负载被转发，而所有其他可能的 JOIN EUI 都将被黑名单规则丢弃。

## 网络 ID

网关将把接收到的每一个 LoRaWAN 负载转发到服务器。这包括邻近 LoRaWAN 节点的负载。转发所有内容可能并不理想，例如，这会增加使用的数据量（并直接影响 ISP 套餐费用）。

NetID 菜单允许您指定网关应转发（如果是“白名单”）或应阻止（如果是“黑名单”）的 NetID 黑名单或白名单范围。添加列表后，请确保将其应用到[服务器](./general-properties.md#servers)设置。

过滤器的工作原理如下：

1) 默认情况下，允许所有内容（除非添加了白名单/黑名单过滤器）；

2) **如果添加了“黑名单”过滤器范围**，并且数据包的 NetID 与黑名单范围匹配 → **它将被丢弃**；

3) **如果添加了“白名单”过滤器范围，则其优先级高于“黑名单”过滤器**。这意味着如果“黑名单”和“白名单”都匹配同一个 NetID，则“白名单”优先，数据包将被转发。

NetID 定义了 LoRaWAN 联盟分配给不同运营商/服务器的设备地址（DevAddr）范围。大多数范围的列表可以在 [TTN 指南](https://www.thethingsnetwork.org/docs/lorawan/prefix-assignments/) 中找到。

DevAddr 由 LoRaWAN 服务器在与服务器通信后分配给 LoRaWAN 节点。例如，[TTN](https://www.thethingsnetwork.org/) 将为您的节点分配一个 26000000 - 27FFFFFF 范围内的地址。您可以在 LoRaWAN 服务器仪表板下找到它，或者使用 RouterOS GUI，在“Traffic”子菜单（在“join-request”和“join-accept”通信发生后）的 Dev Addr 列/字段中找到。

假设 TTN 为您的节点分配了 **26 1B D8 D1** Dev Addr。根据 [TTN 指南](https://www.thethingsnetwork.org/docs/lorawan/prefix-assignments/)，它属于 26000000 - 27FFFFFF DevAddr 范围，并且属于 **000013 NetID**。

**子菜单：** `/iot/lora/netid`

| 属性 | 描述 |
| :-- | :-- |
| **netids** (*字符串*; 默认值：) | 定义 NetID |
| **logging**(*yes \| no*; 默认值：no) | 为过滤器功能启用额外的日志记录。 |
| **name** (*字符串*; 默认值：) | 定义 ID 的名称。 |
| **type** (blacklist \| whitelist; 默认值：whitelist) | 定义过滤器的类型：blacklist（如果范围匹配，则阻止/丢弃数据包）whitelist（如果范围匹配，则转发数据包） |

要添加一个允许特定 NetID（在此示例中为 **000013** NetID，属于 TTN）的过滤器，请使用命令：

```ros
/iot/lora/netid/add name=allow_TTN netids=000013-000013 type=whitelist
```

要阻止所有其他 NetID，请使用 `type=blacklist`：

```ros
/iot/lora/netid/add name=block_all netids=000000-ffffff type=blacklist
```

禁用 LoRa 接口：

```ros
/iot/lora/disable [find where ]
```

将两个范围应用到您正在使用的 LoRa 服务器，然后重新启用接口：

```ros
/iot/lora/servers/set netid=block_all,allow_TTN [find where address ~ "eu1.cloud.thethings.network"]
/iot/lora/enable [find where ]
```

## 服务器

此部分用于添加新服务器或修改当前服务器设置。

**子菜单：** `/iot/lora/servers`

有几个预定义的服务器可以使用（使用它们需要创建一个 [The Things Network](https://thethingsnetwork.org) 帐户）：

```ros
[admin@MikroTik] /iot/lora/servers/print
Columns: NAME, UP-PORT, DOWN-PORT, ADDRESS
#  NAME              UP-PORT  DOWN-PORT  ADDRESS                                     
0  TTS Cloud (eu1)      1700       1700  eu1.cloud.thethings.industries         
1  TTS Cloud (nam1)     1700       1700  nam1.cloud.thethings.industries        
2  TTS Cloud (au1)      1700       1700  au1.cloud.thethings.industries         
3  TTN V3 (eu1)         1700       1700  eu1.cloud.thethings.network            
4  TTN V3 (nam1)        1700       1700  nam1.cloud.thethings.network           
5  TTN V3 (au1)         1700       1700  au1.cloud.thethings.network          
```

也可以添加自定义服务器。如果第一个服务器不更改数据包的“DevAddress”部分，并且所有服务器都能解码数据包，则可以同时向多个服务器转发数据。

| 属性 | 描述 |
| :-- | :-- |
| **address** (*域名或 IP 地址*; 默认值：) | 定义 LoRaWAN 网络服务器地址。 |
| **name** (*字符串*; 默认值：) | 定义服务器名称。 |
| **protocol** (*UDP \| LNS \| CUPS*; 默认值：**UDP**) | 指定与 LoRaWAN 服务器通信时使用 UDP、LNS 还是 CUPS 协议。 |
| **down-port** (*整数 [0..65535]*; 默认值：**1700**) | 选择 UDP 协议时使用的参数。定义与 LoRaWAN 网络服务器下行链路通信（从服务器到节点）的端口。大多数已知的开源服务器默认使用端口 1700，但如果同一台机器上配置了多个服务器，则可能会更改。 |
| **up-port** (*整数 [0..65535]*; 默认值：**1700**) | 选择 UDP 协议时使用的参数。定义与 LoRaWAN 网络服务器上行链路通信（从节点到服务器）的端口。大多数已知的开源服务器默认使用端口 1700，但如果同一台机器上配置了多个服务器，则可能会更改。 |
| **netid**(*字符串列表*; 默认值：) | 选择 UDP 协议时使用的参数。应用过滤器，仅发送与配置的网络 ID（Net ID）过滤器匹配的 LoRaWAN 负载。 |
| **joineui** (*字符串列表*; 默认值：) | 选择 UDP 协议时使用的参数。应用过滤器，仅发送与配置的 Join EUI 过滤器匹配的 LoRaWAN 负载。 |
| **port** (*整数 [0..65535]*; 默认值：**8887**) | 选择 LNS 或 CUPS 协议时使用的参数。对于 LNS，定义 WSS（WebSocket）端口；对于 CUPS，定义 HTTPS 端口。 |
| **key** (*字符串*; 默认值：) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 选择 LNS 或 CUPS 协议时使用的参数。指定 LoRa Basics Station LNS 认证密钥或 CUPS API 密钥（均在服务器上生成）。 |
| **ssl** (*yes 或 no*; 默认值：no) | 选择 LNS 或 CUPS 协议时使用的参数。指定是否使用 SSL（如果服务器支持 TLS 服务器认证）。选择此选项时，必须在[证书](../../authentication-authorization-accounting/certificates.md)菜单下上传根 SSL 证书。 |
| **certificate** (*字符串列表*; 默认值：**none**) | 选择 LNS 或 CUPS 协议时使用的参数。选择客户端[证书存储中的证书](../../authentication-authorization-accounting/certificates.md)（如果服务器等待 TLS 客户端认证）。如果服务器不需要 TLS 客户端认证，请使用默认的“**none**”设置。 |
| **interval**(*整数 [0..65535]*; 默认值：) | 选择 CUPS 协议时使用的参数。指定 LoRa Basics Station 查询 CUPS 服务器以获取配置更新/更改的时间间隔。 |

有几个预配置的 The Things 默认服务器。如果您删除了一个并想恢复默认服务器，可以使用命令：

```ros
/iot/lora/servers/reset-servers
```

:::warning
请注意，重置服务器将同时删除所有先前配置的服务器，因此请务必事先“保存”它们。
:::

## 流量

此部分显示由周围节点广播的 LoRa 负载。

**子菜单：** `/iot/lora/traffic`

| 属性 | 描述 |
| :-- | :-- |
| **options** | 允许为流量选项卡配置附加选项：crc-errors (yes \| no) → 设置为“no”以丢弃具有“crc error”状态的数据包，使其不显示在流量选项卡中；pckt-limit (10...1024) → 限制流量选项卡的日志列表。 |
| **clear** | 清空列表（删除所有条目）。 |

要查看列表，请使用 `print` 命令：

```ros
[admin@MikroTik] /iot/lora/traffic/print
Columns: TIME, GWID, MSGTYPE, DEVADDR, MVER, FCNT, CRC, TYPE, JOINEUI, DEVEUI
 #  TIME                             GWID  MSGTYPE                DEVADDR      MVER         FCNT  CRC    TY  JOINEUI                  DEVEUI                 
 0  2024-11-08 13:33:28  xxxxxxxxxxxxxxxx  Unconfirmed Data Up    6C B9 XX XX  LoRaWAN R1  59434  Error  Rx                                                  
 1  2024-11-08 13:33:50  xxxxxxxxxxxxxxxx  Rejoin-request                      LoRaWAN R1         Error  Rx                           50 62 9F FE XX XX XX XX
 2  2024-11-08 13:34:09  xxxxxxxxxxxxxxxx  Unconfirmed Data Down  5E 00 XX XX  RFU         41736  Error  Rx                                                  
 3  2024-11-08 13:34:15  xxxxxxxxxxxxxxxx  Rejoin-request                      RFU                Error  Rx                           D9 C2 BD 4B XX XX XX XX
 4  2024-11-08 13:34:55  xxxxxxxxxxxxxxxx  Join-request                        LoRaWAN R1         Error  Rx  A1 AE B1 8A XX XX XX XX  F4 62 81 BE XX XX XX XX
```

要清空列表（删除所有条目），请执行 `clear` 命令：

```ros
[admin@MikroTik] /iot/lora/traffic/clear
```

Traffic 选项卡显示“LoRa”负载。一旦使用 `/iot/lora/enable [find]` 命令启用 LoRa 接口，列表中的所有负载都将转换为 TCP/UDP 数据包（取决于您使用的是 UDP 1700 还是 LNS/CUPS 协议）并转发到配置的服务器。

如果您不想使用 LoRaWAN 拓扑，并且希望将“原始”LoRa 负载转发到您自己的服务器，您可以使用 [MQTT](../mqtt/index.md) 或 [Fetch](../../system-information-and-utilities/fetch.md) 按您选择的时间间隔运行脚本以持续发送数据。

一个关于如何将流量负载转换为名为“traffic”的变量的基本示例（脚本的第一步）：

```ros
[admin@MikroTik] > :global traffic;:set traffic [/iot/lora/traffic/print as-value ];put $traffic 
.id=*4f;band=125 kHz;coderate=?/?;counter=890652548;crc=Error;datarate=SF 7;freqhz=868300;gwid=50313xxxxxx;ifcha
in=1;mod=LoRa;msgtype=Proprietary;mver=RFU;rfchain=1;rssi=-116.00;rxcrc=3809;size=213;snr=-12.00;snrmax=-8.25;snrmin=
-14.25;time=2024-11-08 14:39:45;type=Rx
```

## 调试

如果连接出现问题，请确保启用日志：

```ros
/system/logging/add topics=debug,lora
```

这将启用调试日志，并帮助您定位潜在问题所在。可以使用以下命令查看日志：

```ros
/log/print
```

成功的连接如下所示：

```ros
 13:50:33 lora,info gateway-0 forwarder started
 13:50:38 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/router-info
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network discovered
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network disconnected
 13:50:39 lora,info [LNS] connecting to wss://eu1.cloud.thethings.network:8887/traffic/eui-xxxx
 13:50:39 lora,info [LNS] eu1.cloud.thethings.network configured
 13:50:52 lora,info gateway-0 forwarder is ready
```

更多日志信息可以在我们的[日志](../../diagnostics-monitoring-and-troubleshooting/log/index.md)指南中找到。