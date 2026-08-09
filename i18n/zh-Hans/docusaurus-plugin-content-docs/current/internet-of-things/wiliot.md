# Wiliot

> Wiliot 是一家物联网公司，提供无需电池的蓝牙标签，用于广播遥测数据。这需要支持蓝牙的 MikroTik RouterOS 设备以网关和桥接模式运行。本文档指导用户将 MikroTik 板卡注册为 Wiliot 网关，包括 API 令牌设置和 MQTT 连接建立。

# Wiliot

**[Wiliot](https://www.wiliot.com/company)** 是一家以 [IoT Pixels](https://www.wiliot.com/product/iot-pixels)（标签）等解决方案而闻名的**物联网**公司。Pixel 的一大优势在于它是一种无需电池、标签大小的（紧凑型）蓝牙“标签”（可广播带有遥测数据的蓝牙信标）。

- 要为 IoT Pixel 供电，您需要一个桥接（“激励器”）设备。它通过无线电波提供“能量”，并从一定距离外为 IoT Pixel 供电。
- 要将 IoT Pixel 的数据转发到服务器（“仪表盘”），您需要一个网关设备。它通过 TCP/IP 连接与服务器建立连接，并转发包含传感器数据（如温度）的标签负载。

这两种操作模式可以由单个设备执行，也可以由不同的设备分别执行。

RouterOS 允许在支持蓝牙的设备上使用 Wiliot `gateway` 和 `bridge` 模式。

Wiliot `gateway` 模式负责与 MQTT 服务器建立连接（通过 API 注册网关、获取所需的令牌和凭据，并授权设备）。它还负责通过已建立的 MQTT 连接转发其捕获的 Pixel 蓝牙负载，以及通过蓝牙广播中继它可能从订阅的 MQTT 主题接收到的附加命令。

Wiliot `bridge` 模式负责在特定频率上提供能量，并保持 IoT Pixels 的供电。

:::warning
`bridge` 模式尚未实现。
:::

## 分步指南

分步指南需要两个快速步骤：

1. 注册设备并激活 MikroTik 板卡；
2. 设置 IoT Pixels。

### 步骤 #1，网关注册

#### 在 Wiliot 门户网站上

- 登录 Wiliot 注册页面 → [https://deployment-tool.wiliot.com](https://deployment-tool.wiliot.com)

![](https://manual.mikrotik.com/docs/internet-of-things/img/wiliot-01.webp)

- 选择“Gateway Registration”（网关注册）。
- 选择“Manual input”（手动输入）（屏幕右上角）。
- 输入“Gateway ID”（网关 ID）。

您可以从 RouterOS 设置中复制“Gateway ID”（`gateway-id` 字段）：

```routeros
[admin@MikroTik] > /iot wiliot configuration print
                  status: inactive                
              gateway-id: XXXXXXXXX          
                    type: mikrotik-knot-embedded
                   owner: xxxx              
               spoof-gps: xx                   
                     lat: xx                    
                    long: xx                    
  token-refresh-handicap: 3600                  
                  server: Wiliot US East        
                 scanner: bt1                   
              advertiser: bt1                   
                   wi-fi: none                  
                features: gateway  
```

- 新网关应出现在平台的“pre-registered”（预注册）状态中 → [https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)

#### 在 RouterOS 中

:::info
您可以使用不同的工具来浏览设置。建议的管理方式是使用 [Winbox](../management-tools/winbox.md) 软件。[点击此链接下载该工具](https://mikrotik.com/download/winbox) 并运行它。使用“以太网”线缆将您的 PC 连接到从 ether2+ 开始的任何端口（避免使用 ether1，因为在大多数情况下，它被配置为 WAN 端口并受防火墙限制，而其余端口是 LAN 端口，具有开放访问权限并启用了 DHCP 服务器），或使用 Wi-Fi 连接（如果板卡有 Wi-Fi 芯片）。

在 Winbox 中，导航到“Neighbors”（邻居）选项卡（从下拉菜单中选择：Neighbors），找到您的 MikroTik 板卡的 MAC 地址（印在设备标签上），点击 MAC 地址，输入登录凭据（也印在标签上），然后“连接”到它。

从这里，您可以使用“GUI”或“CLI”命令。**本指南展示的是“CLI”命令示例**，您可以通过从 Winbox 选项打开“New Terminal”（新终端）来运行这些命令。但是，GUI 中也提供了完全相同的部分和选项卡。例如，如果命令显示为“**`/iot/wiliot/enable`**”，请转到 **IoT→ Wiliot** 选项卡并点击“**enable**”按钮。
:::

- 启用“wiliot”功能。

```routeros
[admin@MikroTik] > /iot/wiliot/enable
```

- 确认设备成功获取了令牌、已获得授权并连接到 MQTT 服务器，状态为“**active**”（`status: active`）。

```routeros
[admin@MikroTik] > /iot/wiliot/configuration/print
                  status: active                  
              gateway-id: XXXXXXXXX           
                    type: mikrotik-knot-embedded
                   owner: xxxx              
  token-refresh-handicap: 3600                  
                  server: Wiliot US East        
                 scanner: bt1                   
              advertiser: bt1                   
                   wi-fi: none                  
                features: gateway               
```

 网关状态应在 Wiliot 平台上从“pre-registered”（预注册）更改为“approved”（已批准）（或/和“online”（在线））→ [https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)

### 步骤 #2，添加 IoT Pixel（标签）

#### 在 Wiliot 门户网站上

- 登录 Wiliot 平台并导航到“Category”（类别）选项卡 → [https://platform.wiliot.com/categories](https://platform.wiliot.com/categories)。添加一个新的“Category”（类别）（“Add new”（添加新类别））。为其命名并选择所需的类别类型。
- 导航到“Pixels”选项卡 → [https://platform.wiliot.com/edge/pixels](https://platform.wiliot.com/edge/pixels)。检查您的标签的“ID”。标签应已分配到您的账户。
- 转到“Assets”（资产）选项卡 → [https://platform.wiliot.com/assets](https://platform.wiliot.com/assets)。创建一个新资产（“Add New”（添加新资产））。选择/将资产链接到之前创建的“Category”（类别），输入“Asset ID”（资产 ID）（或生成一个随机 ID），并从列表中选择像素的 ID。
- 点击创建的“asset”（资产）条目（一旦标签被供电且网关就绪），您将能够看到标签的读数（温度等）。

## RouterOS 设置

**子菜单：** `/iot/wiliot`

***注意***：**需要** **iot** 软件包。

| 属性 | 描述 |
| :-- | :-- |
| **configuration** | 常规 Wiliot 网关/桥接设置。 |
| **servers** | MQTT 服务器配置。 |
| **bluetooth traffic** | 蓝牙流量菜单。 |
| **mqtt traffic** | MQTT 流量菜单。 |

### 配置（常规选项）

要启用配置，请使用命令：

```routeros
/iot/wiliot/enable
```

要禁用它：

```routeros
/iot/wiliot/disable
```

要清除（清除）MQTT 连接/认证数据（仅在“禁用”时可用）：

```routeros
/iot/wiliot/disable
/iot/wiliot/clear
```

:::info
“清除”配置后，您将必须删除网关（[https://platform.wiliot.com/edge/gateways](https://platform.wiliot.com/edge/gateways)）并重新注册网关（[https://deployment-tool.wiliot.com/](https://deployment-tool.wiliot.com/)）。
:::

配置属性可以使用“set”命令应用（仅在“禁用”时可用）：

```routeros
/iot/wiliot/set
```

示例：

```routeros
/iot/wiliot/set features=gateway
```

| 属性 | 描述 |
| :-- | :-- |
| **advertiser**（默认值：bt1） | 选择将用于广播（中继从 MQTT 服务器获得的命令）的蓝牙接口。 |
| **scanner**（默认值：bt1） | 选择将用于扫描（捕获 Pixel 负载）的蓝牙接口。 |
| **spoof-gps**（*yes \| no*；默认值：no） | 选择是否使用手动 GPS 坐标，这些坐标将传递给服务器。 |
| **lat**（默认值：） | 使用“spoof-gps”时，设置在与服务器连接期间要包含的 GPS 纬度值。 |
| **long**（默认值：） | 使用“spoof-gps”时，设置在与服务器连接期间要包含的 GPS 经度值。 |
| **features**（*gateway \| bridge*；默认值：） | 为设备选择角色：gateway。在此模式下，设备与服务器建立 MQTT 连接，并将扫描器捕获的 IoT Pixel 信标转发到服务器。它还会将从订阅主题接收到的命令广播给附近的桥接设备。bridge。在此模式下，设备为周围的 IoT Pixels 供电（为其上电）。**注意：** `bridge` 模式尚未实现。 |
| **server**（默认值：） | 设置 MQTT 连接的服务器。 |

### 服务器

要更改 MQTT 服务器设置：

| 属性 | 描述 |
| :-- | :-- |
| **address**（默认值：） | MQTT 服务器的 IP/域名地址。 |
| **certificate**（默认值：） | 如果服务器要求，指定要用于 SSL MQTT 连接的[证书存储中的证书](../authentication-authorization-accounting/certificates.md)。 |
| **name**（默认值：） | 服务器名称。 |
| **port**（默认值：） | MQTT 服务器使用的 TCP 端口。 |
| **ssl**（yes \| no；默认值：） | 启用与服务器的 SSL 通信。 |

### 蓝牙流量

显示附近的 IoT Pixel 原始数据：

```routeros
/iot/wiliot/bluetooth-traffic/print 
Columns: TIME, ADDRESS, RSSI, PAYLOAD
 #  TIME        ADDRESS            RSSI    PAYLOAD                                                                                     
 0  2026-01-07  E9:B7:32:XX:XX:XX  -34dBm  1E 16 C6 FC 03 00 7C 7B 3C 22 0E D8 54 38 B0 03 E0 DA 8C 06 36 B4 CF AC 8A D6 76 54 BD FC B9
    14:23:26                                                                                                                           
 1  2026-01-07  E9:B7:32:XX:XX:XX  -41dBm  1E 16 C6 FC 03 00 3C DB 7D 72 BF A0 C1 62 9C 5F B6 D5 90 00 C1 62 BF 68 EC E5 64 02 63 F9 C3
    14:23:26                                                                                                                           
 2  2026-01-07  E9:B7:32:XX:XX:XX  -42dBm  1E 16 C6 FC 03 00 3C A8 3B 27 17 25 BC 6D 01 F5 49 E1 98 03 CA 3C 64 04 30 B2 E1 86 FC 80 CB
    14:23:28                                                                                                                           
 3  2026-01-07  E9:B7:32:XX:XX:XX  -33dBm  1E 16 C6 FC 03 00 3C F5 AF 22 CC E2 60 FA BC 4E 57 F7 8C 01 80 6A 21 EF 82 CB 62 2A 16 5A 3F
    14:23:29                                                                                                                           
 4  2026-01-07  E9:B7:32:XX:XX:XX  -33dBm  1E 16 C6 FC 03 00 3C FC AC 9A 1B 9A BD 2C DE B7 02 FF 7C 03 C7 28 BD AB 20 1B 91 89 B9 ED 88
```

### MQTT 流量

显示 MQTT 流量：

```routeros
/iot/wiliot/mqtt-traffic/print
   time: 2026-03-02                                                                                                                      >
         07:37:43                                                                                                                        >
  topic: update/mikrotik/XXXXXXXXXXX                                                                                                     >
   data: {"txPacket":"1E16C6FC0000ED070C3443B7D39DE2CE08993D7F40B2F56B822096AA19CD00","txMaxRetries":8,"txMaxDurationMs":700,"action":0} >
```

### 调试

您可以使用以下命令启用“wiliot”调试日志记录：

```routeros
/system/logging
add topics=wiliot
```

结果，您应该在日志中看到更详细的条目（`/log/print` 命令）：

```routeros
 2026-02-12 12:04:54 wiliot,debug [CFG] authorizing...
 2026-02-12 12:04:54 wiliot,debug [CFG] authorization complete
 2026-02-12 12:04:54 wiliot,debug [CFG] registering...
 2026-02-12 12:04:55 wiliot,debug [CFG] registration complete
 2026-02-12 12:04:55 wiliot,debug [CFG] polling for token...
 2026-02-12 12:04:55 wiliot,debug [CFG] token obtained
 2026-02-12 12:04:55 wiliot,debug [CFG] ownerId
 2026-02-12 12:04:55 wiliot,debug [CFG] authorization complete
 2026-02-12 12:04:55 wiliot,debug [CFG] updating MQTT credentials
 2026-02-12 12:04:56 wiliot,debug [CFG] MQTT credentials updated
 2026-02-12 12:04:56 wiliot,debug [CFG] connecting to MQTT server
  2026-02-12 12:04:56 wiliot,debug [CFG] subscribing to BLE advertisements
 2026-02-12 12:04:56 wiliot,debug [CFG] active
```

### 证书

Wiliot 功能使用 [/tool/fetch](../system-information-and-utilities/fetch.md) 发起 HTTP 请求，并使用 [/mqtt](./mqtt/index.md) 建立 MQTT 连接。HTTP 和 MQTT 都需要 SSL 证书。RouterOS 有一个“内置信任库”，其中从一开始就包含所有必需的证书。

**[默认情况下](../authentication-authorization-accounting/certificates.md#settings)，**“**all**”服务应被允许使用内置证书库**，因此您无需执行任何操作。但是，如果您决定限制这一点（如果您决定不允许“all”服务访问“store”），则要使“wiliot”正常工作，您需要启用“wiliot”、“mqtt”和“fetch”服务（或禁用 builtin-trust-store 并手动上传证书）：

```routeros
[admin@MikroTik] > /certificate/settings/print
  builtin-trust-store: fetch                    
                       mqtt                      
                       wiliot                     
         crl-download: no    
              crl-use: no    
            crl-store: ram 
```