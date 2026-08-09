# W60G

> 本文档介绍 MikroTik RouterOS W60G 无线接口配置，涵盖 60GHz 点对点/点对多点链路设置、ARP/MAC 设置、加密及站点管理，并提供详细的统计信息监控。

import DocCardList from '@theme/DocCardList';

# W60G

本章节涵盖 60 GHz 无线示例与指导。使用它来配置 W60G 点对点及点对多点链路、故障切换及与距离相关的设置。

<DocCardList />

### 概述

**软件包：** `system`,`wireless`

802.11ad 实现，能够在无线网络上提供千兆以太网速度。

通过透明的 AES 加密 60GHz 无线链路扩展您的千兆网络，无需处理常见的有线或无线网络问题。

### 通用接口属性

**子菜单：** `/interface/w60g`

:::warning
Wireless Wire 套件设备出厂时已预配置为配对连接状态。手动配置为可选操作。
:::

| 属性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | [`了解更多 >>`](../../network-management/arp.md#arp-modes) |
| **arp-timeout** (*auto \| integer*; 默认值：**auto**) | ARP 超时时间，指在未从 IP 地址接收到数据包后，ARP 记录在 ARP 表中保留的时间。值 **auto** 等同于 `/ip/settings` 中 **arp-timeout** 的值，默认为 30 秒 |
| **comment** (*string*; 默认值：) | 接口的简短描述 |
| **disabled** (*yes \| no*; 默认值：**yes**) | 接口是否被禁用 |
| **frequency** (*58320 \| 60480 \| 62640 \| 64800 \| 66000 \| auto*; 默认值：**auto**) | 通信所使用的频率（仅在桥接设备上生效） |
| **isolate-stations** (*yes \| no*; 默认值：**yes**) | 不允许已连接的客户端之间进行通信（自 RouterOS 6.41 起） |
| **l2mtu** (*integer [0..7882]*; 默认值：**1600**) | 二层最大传输单元 |
| **mac-address** (*MAC*; 默认值：) | 无线接口的 MAC 地址 |
| **mdmg-fix** (*yes \| no*; 默认值：**no**) | 实验性功能，仅在 wAP60Gx3 设备上有效，在某些情况下可提供更好的点对多点稳定性 |
| **mode** (*ap-bridge \| bridge \| sniff \| station-bridge*; 默认值：**bridge**) | 操作模式 |
| **mtu** (*integer [32..8192]*; 默认值：**1500**) | 三层最大传输单元 |
| **name** (*string*; 默认值：**wlan60-1**) | 接口名称 |
| **password** (*string*; 默认值：**随机生成**) *[敏感参数](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于 AES 加密的密码 |
| **put-stations-in-bridge** (; 默认值：) | 将新建的站点设备接口放入此桥接 |
| **region** (*asia \| australia \| canada \| china \| eu \| japan \| no-region-set \| usa*; 默认值：**no-region-set**) | 用于限制频率使用的参数 |
| **scan-list** (*58320,60480,62640,64800,66000*; 默认值：**58320,60480,62640,64800**) | 在站点模式下限制频率连接性的扫描列表 |
| **ssid** (*string (0..32 字符)*; 默认值：**[系统标识](../../system-information-and-utilities/identity.md) 的值**) | SSID（服务集标识符）是标识无线网络的名称 |
| **tx-sector** (*integer [0..63] \| auto*; 默认值：**auto**) | 禁用波束成形并锁定到选定的辐射方向图 |

**子菜单：** `/interface/w60g/print/stats`

提供关于波束成形事件及一些调试信息的更详细信息：

```ros
/interface w60g print stats name: wlan60-1 
beamforming-event: 310 
tx-io-msdu: 0 
tx-sw-msdu: 154 663
tx-fw-msdu: 102 
tx-ppdu: 220 147 
tx-ppdu-from-q: 40 327 
tx-mpdu-new: 154 663 
tx-mpdu-total: 184 759 
tx-mpdu-retry: 30 096 
rx-ppdu: 166 636 
rx-mpdu-crc-err: 4 817 
rx-mpdu-crc-ok: 285 649
```

站点接口属性：

:::warning
ap-bridge 设备需要 License 级别 4  [(点击了解更多)](../../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels) 才能支持超过一个已连接客户端
:::

已连接的客户端被视为独立的接口，成功连接后会创建一个新的站点接口。

更新后默认配置仍然有效——新建的站点接口会被移动到默认桥接中。

**子菜单：** `/interface/w60g/station`

| 属性 | 描述 |
| :-- | :-- |
| **parent** (*string*; 默认值：**wlan60-\***) | 父接口名称 |
| **put-in-bridge** (*none \| parent \| bridge-name*; 默认值：**parent**) | 将站点设备接口添加到指定的桥接 |
| **remote-address** (*MAC*; 默认值：**匹配桥接接口 MAC**) | 站点所连接的桥接接口的 MAC 地址 |

### 扫描

**子菜单：** `/interface/w60g/scan`

```ros
/interface w60g scan wlan60-1
```

扫描命令用于搜索并显示 W60G 接口支持的频率范围内可用的 AP。

使用扫描命令时，接口操作将被禁用（扫描期间无线链路会断开）。

目前无法进行后台扫描。

### 监控

**子菜单：** `/interface/w60g/monitor`

```ros
/interface w60g monitor wlan60-1 
connected: yes frequency: 58320 
remote-address: 04:D6:AA:AA:AA:AA 
mcs: 8 
phy-rate: 2.3Gbps 
signal: 80 rssi: -68 
tx-sector: 28 
tx-sector-info: center 
distance: 160.9m
```

监控命令显示活动连接的当前状态。距离测量工具可提供非常精确的距离测量。"tx-sector-info"（测试阶段功能）提供当前使用的波束成形方向图信息，并显示指向中心的方向——即理论最高功率输出点。

### 对准

**子菜单：** `/interface/w60g/align`

```ros
/interface w60g align wlan60-1 
connected: yes 
frequency: 58320 
remote-address: 04:D6:AA:AA:AA:AB 
tx-mcs: 6 
tx-phy-rate: 1540.0Mbps 
signal: 70 
rssi: -62 
10s-average-rssi: -63.1 
tx-sector: 62 
tx-sector-info: left 19 degrees, up 26.6 degrees 
rx-sector: 96 
distance: 220.88m 
tx-packet-error-rate: 5%
```

在对准模式下，两个设备之间的帧交换更加频繁，信号质量信息的显示也更加频繁。使用 "rssi"、"10s-average-rssi" 和 "tx-sector-info" 值进行更精确的链路对准。当设备进入对准模式时——链路会中断几秒钟。

### 嗅探

嗅探模式允许捕获附近的 802.11ad 帧。要使用嗅探模式，需要使用相同的频率，并将接口操作模式设置为 sniff：

```ros
/interface w60g set wlan60-1 mode=sniff
```

现在该接口可用于 [工具/数据包嗅探器](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 进行数据包捕获。嗅探模式不能与常规接口工作模式同时使用。

### 点对多点设置示例

所有 MikroTik 设备都可以相互连接。目前有四种不同版本的 wAP60G 设备可用：

- Wireless Wire 套件
- wAP 60G
- SXTsq60 Lite60
- wAP 60G AP

以及

- Wireless Wire Dish

在硬件方面，wAP 设备是相同的，但存在一些软件限制：

**wAP 60G AP** 专为在 PtMP（点对多点）设置中作为接入点使用而设计，但也可以用作 PtP（点对点）或作为站点设备。它已配备 level4 许可证，以支持多个已连接客户端。更多信息请参阅 [RouterOS 许可证级别](../../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels)。

**Wireless Wire 套件**、**Wireless Wire Dish**、**SXTsq Lite60** 和 **wAP60G** 设备配备 level3 许可证。Wireless Wire Dish 由于其窄辐射方向图，应仅用作客户端设备。

需要升级许可证才能解锁接入点模式下同时连接多个客户端的支持，但设备可以作为常规站点设备连接到接入点。

:::warning
配置前，请确保设备运行最新的软件版本：[如何升级](../../getting-started/installation-and-upgrade/upgrade.md)
:::

透明无线链路的最小配置是匹配 SSID、正确的模式（bridge || station-bridge）以及将无线和以太网接口放入同一个桥接中。

在当前示例中，我们将查看一个使用场景，其中 **wAP60G AP** 用作接入点，**wAP60G** 和 **Wireless Wire 套件** 设备用作站点设备，形成一个 4 单元网络。

:::warning
建议更改默认 IP 地址，以避免设备连接问题
:::

**wAP60G AP** 单元出厂时预配置了 WISP Bridge [默认配置](../../getting-started/configuration-management/default-configurations.md)。

SSID 以及无线和以太网接口之间的桥接已配置完成。建议设置无线密码并更改 SSID。如果设备已被重置，您也可以设置正确的模式并启用接口。

执行上述所有步骤的单行命令：

```ros
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=ap-bridge
```

**Wireless Wire 和 wAP60G** 单元出厂时预配置了 PTP Bridge 默认配置。

Wireless Wire 设备已具有随机生成的匹配 SSID 和无线密码。

桥接设备（Bridge 或支持一个已连接客户端的接入点设备）需要将无线模式更改为 station-bridge。

可用于将设备设置为客户端模式的单行命令：

```ros
/interface w60g set wlan60-1 password="put_your_safe_password_here" ssid="put_your_new_ssid_here" disabled=no mode=station-bridge
```

如果从空配置开始配置（重置且无默认配置）：

需要创建一个包含无线和以太网接口的新桥接，并添加一个 IP 地址以便于访问。

```ros
{ /interface bridge 
add name=bridge1 
/interface bridge port 
add bridge=bridge1 interface=ether1 
add bridge=bridge1 interface=wlan60-1 
/ip address add address=192.168.88.1/24 interface=bridge1 
}
```

对于接入点，添加此行以确保所有已连接的站点都将被放入同一个桥接中。

```ros
/interface w60g set wlan60-1 put-stations-in-bridge=bridge1
```

每个客户端设备成功连接后，接入点设备上会出现一个新条目，位于：

```ros
/interface w60g station print
```

```ros
Flags: X - disabled, R - running 

0 name="wlan60-station-1" parent=wlan60-1 remote-address=AA:AA:AA:AA:AA:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AB arp=enabled arp-timeout=auto put-in-bridge=parent 

1 name="wlan60-station-2" parent=wlan60-1 remote-address=AA:AA:AA:AA:AB:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AC arp=enabled arp-timeout=auto put-in-bridge=parent 

2 name="wlan60-station-3" parent=wlan60-1 remote-address=AA:AA:AA:AA:AC:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AD arp=enabled arp-timeout=auto put-in-bridge=parent 

3 name="wlan60-station-4" parent=wlan60-1 remote-address=AA:AA:AA:AA:AD:AA mtu=1500 mac-address=AA:AA:AA:AA:AA:AE arp=enabled arp-timeout=auto put-in-bridge=parent 
```

可以为每个客户端应用单独的设置（队列、VLAN、防火墙规则等），提供更大的配置灵活性。

要限制同一桥接中客户端之间的通信，可以在接入点设备上使用 isolate-stations 选项：

```ros
/interface w60g set wlan60-1 isolate-stations=yes
```

### 点对点 GUI 配置示例

[点对点 GUI 配置示例](./ptp-gui-example.md)

### 故障排除与建议

MikroTik 60GHz 解决方案的功能包括对 ATPC（自适应发射功率控制）的支持

##### 物理特性

802.11ad 标准中使用的无线频率的大气衰减非常高。在部署链路之前应考虑这一点。

Wireless Wire 套件已在长达 200 米的距离上进行了测试。

Wireless Wire Dish 套件在长达 2500 米的距离上进行了测试。为了稳定性和全速可用性，建议该套件用于长达 1500 米的距离。

wAP60G 设备配备相控阵 60° 波束成形天线，可以帮助信号在短距离内绕过障碍物找到路径，但在较远距离上保持视线清晰仍然至关重要。

LHG60G 设备的单一辐射方向图小于 1 度（水平和垂直方向）。所有方向图组合起来在水平和垂直平面上提供接近 3 度的覆盖。每种情况下的最佳方向图通过波束成形算法计算得出。波束宽度和方向取决于所使用的预定义校准扇区。

##### 设备射频特性

60 GHz 设备

| **设备** | **单一天线方向图宽度及全跨度（度）** | **EIRP** | **发射功率** | **中心扇区\*** |
| :-- | :-- | :-- | :-- | :-- |
| wAP 60G | 单一方向图 15-20 度，水平面全跨度 60 度，垂直面 30 度 | < 40 dBm |  | 27,28,35,36 |
| wAP 60G AP | 单一方向图 15-20 度，水平面全跨度 60 度，垂直面 30 度 | < 40 dBm |  | 27,28,35,36 |
| Wireless Wire | 单一方向图 15-20 度，水平面全跨度 60 度，垂直面 30 度 | < 40 dBm |  | 27,28,35,36 |
| wAP 60Gx3 AP | 单一方向图 15-20 度，水平面全跨度 180 度，垂直面 30 度 | < 40 dBm |  | 27,28,35,36 |
| SXTsq Lite 60 | 单一方向图 15-20 度，水平面全跨度 60 度，垂直面 30 度 | < 40 dBm |  | 27,28,35,36 |
| Cube Lite 60 | 单一方向图 4-8 度，水平面全跨度 12 度，垂直面 12 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| Cube 60G ac | 单一方向图 4-8 度，水平面全跨度 12 度，垂直面 12 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| Cube 60Pro ac | 单一方向图 4-8 度，水平面全跨度 11 度，垂直面 11 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| CubeSA 60Pro ac | 单一方向图 15 度，水平面全跨度 60 度，垂直面 30 度 | < 40 dBm | < 10 dBm | 27,28,35,36 |
| LHG Lite 60 | 单一方向图 < 1 度，水平面全跨度 3 度，垂直面 3 度 | < 55 dBm | < 10 dBm | 27,28,35,36 |
| LHG 60G | 单一方向图 {`< 1`} 度，水平面全跨度 3 度，垂直面 3 度 | {`< 55`} dBm | {`< 10`} dBm | 27,28,35,36 |
| Wireless Wire Dish | 单一方向图 {`< 1`} 度，水平面全跨度 3 度，垂直面 3 度 | {`< 55`} dBm | {`< 10`} dBm | 27,28,35,36 |
| Wireless Wire nRAY | 单一方向图 {`< 1`} 度，水平面全跨度 3 度，垂直面 3 度 | {`< 55`} dBm 或 EU 区域 {`<40`} dBm | {`< 10`} dBm | 31 |

**\*中心扇区是波束成形阵列的校准中心**

##### 区域

MikroTik 802.11ad 设备支持频率范围：57240 MHz - 67080 MHz，如果使用 "region" 参数，可以限制频率和信道使用。

| **区域** | **较低频率** | **较高频率** | **可用信道** |
| :-- | :-- | :-- | :-- |
| 美国 | 57.24 GHz | 70.20 GHz | 1, 2, 3, 4, 5, 6 |
| 加拿大 | 57.24 GHz | 63.72 GHz | 1, 2, 3 |
| 亚洲 | 57.24 GHz | 63.72 GHz | 1, 2, 3 |
| 欧盟 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 日本 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 澳大利亚 | 57.24 GHz | 65.88 GHz | 1, 2, 3, 4 |
| 中国 | 59.40 GHz | 63.72 GHz | 2, 3 |

##### 连接问题

为了连接设备，它们需要在直接可见范围内，客户端设备上的 "scan-list" 需要包含 AP 设备上使用的 "frequency"。LHG60 设备在较远距离上需要非常精确的对准才能获得最佳性能。

##### 用于监控的 SNMP OID

从 RouterOS>=6.42rc6 开始，增加了对 W60G 接口监控的 SNMP 支持。
对于主接口：

```
1.3.6.1.4.1.14988.1.1.1.8.1.2.1  integer  模式
1.3.6.1.4.1.14988.1.1.1.8.1.3.1  string   SSID
1.3.6.1.4.1.14988.1.1.1.8.1.4.1  integer  连接状态
1.3.6.1.4.1.14988.1.1.1.8.1.5.1  string   远程 MAC
1.3.6.1.4.1.14988.1.1.1.8.1.6.1  integer  频率
1.3.6.1.4.1.14988.1.1.1.8.1.7.1  integer  MCS
1.3.6.1.4.1.14988.1.1.1.8.1.8.1  integer  信号质量
1.3.6.1.4.1.14988.1.1.1.8.1.9.1  integer  tx-sector
1.3.6.1.4.1.14988.1.1.1.8.1.11.1 string   扇区信息
1.3.6.1.4.1.14988.1.1.1.8.1.12.1 integer  RSSI
1.3.6.1.4.1.14988.1.1.1.8.1.13.1 gauge32  PHY 速率
```

站点接口将在不同的表下编号：

```
1.3.6.1.4.1.14988.1.1.1.9.1.2.(interfaceID) = integer 连接状态
1.3.6.1.4.1.14988.1.1.1.9.1.3.(interfaceID) = Hex-STRING mac-address
1.3.6.1.4.1.14988.1.1.1.9.1.4.(interfaceID) = INTEGER: MCS 
1.3.6.1.4.1.14988.1.1.1.9.1.5.(interfaceID) = INTEGER: 信号质量指数
1.3.6.1.4.1.14988.1.1.1.9.1.6.(interfaceID) = INTEGER: tx-sector
1.3.6.1.4.1.14988.1.1.1.9.1.8.(interfaceID) = Gauge32: 数据速率 [Mbps]
1.3.6.1.4.1.14988.1.1.1.9.1.9.(interfaceID) = INTEGER: RSSI
1.3.6.1.4.1.14988.1.1.1.9.1.10.(interfaceID) = INTEGER: 距离 [cm]
```

InterfaceID 从 3 开始，每个已连接站点递增 +1。有关 SNMP 功能和 MIB 文件的更多信息，请参阅 [SNMP 手册](../../diagnostics-monitoring-and-troubleshooting/snmp.md)

##### Wireless Wire 套件的配置重置

重置按钮与其他设备上的功能相同，详细说明请参阅 [此处](../../getting-started/configuration-management/routeros-configuration-reset.md)

**启动时按住按钮 5 秒（USR LED 开始闪烁）** - 重置为密码保护状态。

**启动时按住按钮 10 秒（USR LED 闪烁后变为常亮）** - 完全移除配置。

:::warning
完全移除配置后，只能通过 [mac-telnet](../../management-tools/mac-server.md) 连接建立会话。
:::