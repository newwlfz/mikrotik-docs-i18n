# Wi-Fi 6 / 7 (802.11ax/be)

> 本页介绍 RouterOS 中的 WiFi 配置菜单，涵盖受密码保护及 OWE 过渡模式接入点的基本设置。文中解释了配置配置文件（Profiles）、安全设置，并包含重置配置的示例。

# Wi-Fi 6 / 7 (802.11ax/be)

本章节涵盖 MikroTik **Wi-Fi 6 / 6E / 7 (802.11ax/be)** 设备，所有这些设备均通过共享的 **`/interface/wifi`** 菜单进行配置。设备所需的驱动包取决于其无线芯片组和标准。同一菜单也适用于运行 **`wifi-qcom-ac`** 驱动包的 **Wi-Fi 5 (802.11ac)** 设备。

:::tip[我的设备适用此章节吗？]
此菜单（及本手册）适用于所有运行以下驱动包之一的设备：

| 驱动包 | 设备 | 示例 |
| :-- | :-- | :-- |
| `wifi-qcom` | Wi-Fi 6 / 6E (Qualcomm) | wAP ax, cAP ax, hAP ax¬≥ |
| `wifi-qcom-be` | Wi-Fi 7 (Qualcomm) | hAP be3 media |
| `wifi-mediatek` | Wi-Fi 6 / 7 (MediaTek) | hAP ax S, hAP be lite |
| `wifi-qcom-ac` | Wi-Fi 5 / 802.11ac (Qualcomm) | 参见 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) |

标准通常编码在型号名称中——**ax** 代表 Wi-Fi 6，**be** 代表 Wi-Fi 7。对于 `wifi-qcom-ac` 设备，请参阅 [Wi-Fi 5 (802.11ac)](../wifi-ac/index.md) 以确认您的设备应使用此菜单还是传统的 `/interface/wireless` 菜单。

如果您的设备使用传统的 `/interface/wireless` 菜单，请参阅 [802.11 a/b/g/n](../abgn/index.md)。
:::

:::note
在 RouterOS 7.13 之前的版本中，此菜单是名为 `wifiwave2` 的独立软件包的一部分。
:::

## 快速入门

刚接触这些设备？请从面向任务的指南开始，然后使用本页下方的属性参考了解各项设置：

- [配置独立接入点](./configuring-standalone-access-point.md)
- [配置中继器](./configuring-repeater.md)
- [配置室外 CPE 到 AP 链路](./configuring-outdoor-cpe-to-ap-links.md)
- [WiFi6 的互操作 (802.11u / Hotspot 2.0)](./interworking-for-wifi6.md)
- [使用 WiFi CAPsMAN 进行集中管理](./capsman.md)

## WiFi 术语

在继续之前，让我们熟悉一下对理解此菜单操作至关重要的术语。这些术语将在本文中反复使用。

- **Profile（配置文件）** - 指在以下 WiFi 子菜单之一下创建的配置预设：**aaa**、**channel**、**security**、**datapath** 或 **interworking**。
- **Configuration profile（配置配置文件）** - 在 `/interface/wifi/configuration` 下定义的配置预设，它可以引用各种配置文件。
- **Station（工作站）** - 无线客户端。

## 基本配置

完全配置兼容设备的最简单方法是通过 `/interface/wifi/network` 菜单，它将 SSID、安全、数据路径和无线电设置捆绑到一个配置实体中。或者，也可以按接口应用设置，如下方示例所示。

### 网络 (Network)

网络配置适用于其 `labels`（标签）匹配的 WiFi 接口。如果未指定 `labels`，则网络配置将应用于所有接口。

有关网络配置使用的示例，请参见下文：

```ros
# 创建一个包含 SSID、安全和数据路径设置的网络预设，该预设将应用于所有可用接口
/interface/wifi/network
add ssid=MikroTik mode=ap security.authentication-types=wpa2-psk,wpa3-psk security.passphrase="strong_password" datapath.bridge=bridge1 disabled=no

# 创建一个网络无线电预设，该预设将应用于整个无线电。
/interface/wifi/network/radio
add configuration.country=Latvia
```

启用多链路操作 (MLO) 的示例：

```ros
/interface/wifi/network
add datapath.bridge=bridge1 disabled=no mlo=yes mode=ap security.authentication-types=wpa3-psk ssid="MikroTik" security.passphrase="strong_password"
```

| 属性 | 描述 |
| :-- | :-- |
| **mlo** (*no* \| *yes; 默认值: **yes***) | 为 Wi-Fi 7 启用多链路操作。 |
| **labels** (*逗号分隔的字符串*) | 在匹配任何提供的标签的无线电上启用网络配置。 |
| **ssid** (*字符串*) | 无线网络名称 (ESSID)。 |
| **mode** (*ap* \| *station* \| *station-bridge* \| *station-pseudobridge*; 默认值: **ap***) | 接口操作模式。 |
| **disabled** (*no* \| *yes; 默认值: **no***) | 网络是否被禁用。 |

所有安全、认证和加密参数（密码短语、WPA3/SAE、EAP 等）共享 [安全属性](#security-properties) 中描述的相同属性。数据路径参数（桥接、VLAN、客户端隔离、流量处理）遵循 [数据路径属性](#datapath-properties)。

#### 网络无线电属性

`/interface/wifi/network/radio` 下的每无线电设置：

| 属性 | 描述 |
| :-- | :-- |
| **labels** (*对象*) | 将无线电配置与具有给定标签的物理无线电匹配。 |
| **extra-labels** (*多字符串*) | 用于匹配的附加标签，扩展主要的 `labels` 字段。 |
| **disabled** (*no* \| *yes; 默认值: **no***) | 无线电条目是否被禁用。 |

无线电参数（国家/地区、频段、频率、宽度、链、功率等）使用 [信道属性](#channel-properties) 和 [配置属性](#configuration-properties) 中描述的相同属性。

### 基本密码保护 AP

直接的按接口设置适用于所有设备，并且在 `/interface/wifi/network` 菜单不可用或需要按接口覆盖时，此方法仍完全受支持。

```ros
/interface/wifi
set wifi1 disabled=no configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types=wpa2-psk,wpa3-psk security.passphrase=8-63_characters
```

### 带 OWE 过渡模式的开放 AP

机会性无线加密 (OWE) 允许创建无需知晓密码即可连接，但仍提供流量加密和管理帧保护优势的无线网络。这是对常规开放接入点的改进。

然而，由于网络不能同时加密和不加密，需要两个独立的接口配置来为不支持 OWE 的旧设备提供连接，并为支持 OWE 的设备提供 OWE 的优势。

此配置称为 OWE 过渡模式。

```ros
/interface/wifi
add master-interface=wifi1 name=wifi1_owe configuration.ssid=MikroTik_OWE security.authentication-types=owe security.owe-transition-interface=wifi1 configuration.hide-ssid=yes
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik security.authentication-types="" security.owe-transition-interface=wifi1_owe
enable wifi1,wifi1_owe
```

通过这种设置，AP 将广播两个 SSID → 可见的 `MikroTik` SSID（应为“未加密”访问，供不支持 OWE 的旧设备使用），以及隐藏的 `MikroTik_OWE` SSID（应为“OWE”安全，即无密码但加密）。客户端设备不会在（客户端的 WiFi 列表中）看到隐藏的 `MikroTik_OWE` SSID，但是，可见 `MikroTik` SSID 的信标帧将使用“OWE 过渡模式”参数（在信标帧中）通告指向隐藏 `MikroTik_OWE` 网络的链接。因此，客户端设备应优先通过 `owe-transition-interface` 设置连接到“OWE”网络。

支持 OWE 的客户端设备将优先选择 OWE 接口。如果您在注册表中没有看到任何与常规开放 AP 关联的设备，您可能希望从运行过渡模式设置转向使用单个 OWE 加密接口：

```ros
/interface/wifi
set wifi1 configuration.country=Latvia configuration.ssid=MikroTik_OWE security.authentication-types=owe
```

:::info
802.11r（快速漫游）不适用于 OWE 网络。
:::

### 重置配置

WiFi 接口配置可以使用 'reset' 命令重置。

```ros
/interface/wifi/reset wifi1
```

物理接口 MAC 地址可以通过 'reset-mac-address' 命令重置为默认值。

```ros
/interface/wifi/reset-mac-address wifi1
```

## 配置配置文件 (Configuration Profiles)

新增的 WiFi 功能之一是配置配置文件。您可以创建各种预设，并根据需要分配给接口。WiFi 的配置设置根据本页末尾找到的参数部分分组为 **配置文件** - **aaa**、**channel**、**configuration**、**datapath**、**interworking** 和 **security**，然后可以分配给接口。**配置配置文件** 可以包含其他配置文件以及来自其他类别的单独参数。

这种可选的灵活性旨在允许每个用户以对他们最有意义的方式安排其配置，但这也意味着每个参数可能在配置的不同部分被赋予不同的值。

以下优先级决定使用哪个值：

1. 接口设置中的值。
2. 分配给接口的配置文件中的值。
3. 分配给接口的配置配置文件中的值。
4. 分配给配置配置文件（该配置文件又分配给接口）的配置文件中的值。

如果您在任何时候不确定接口将使用哪个参数值，可以执行 "/interface/wifi/print detail" 命令。print 命令将显示接口将拥有的所有值，包括继承的值。

要仅查看直接在接口上配置的值，而不显示继承的值，请使用 "/interface/wifi/print config"。

有关配置配置文件使用的示例，请参见下文（双频家用 AP 示例）：

```ros
# 创建一个安全配置文件，该文件对两个接口通用
/interface/wifi/security
add name=common-auth authentication-types=wpa2-psk,wpa3-psk passphrase="diceware makes good passwords" wps=disable
# 创建一个通用配置配置文件并将安全配置文件链接到它
/interface/wifi/configuration
add name=common-conf ssid=MikroTik country=Latvia security=common-auth
# 为每个频段创建单独的信道配置
/interface/wifi/channel
add name=ch-2ghz frequency=2412,2432,2472 width=20mhz
add name=ch-5ghz frequency=5180,5260,5500 width=20/40/80mhz
# 为每个接口分配通用配置文件以及特定频段的信道配置文件，如果接口上出现“no supported channels”消息，请确保正确的（信道）配置应用于每个接口。
set wifi1 channel=ch-5ghz configuration=common-conf disabled=no
set wifi2 channel=ch-2ghz configuration=common-conf disabled=no

#"print detail" 将显示接口将使用的所有值，包括继承的值
[admin@c52i] > /interface/wifi/print detail 
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-5ghz 
        channel.frequency=5180,5260,5500 .width=20/40/80mhz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap .ssid="MikroTik" .country=Latvia 
        security.authentication-types=wpa2-psk,wpa3-psk .passphrase="diceware makes good passwords" .wps=disable 
        channel=ch-2ghz 
        channel.frequency=2412,2432,2472 .width=20mhz 
#使用 "print detail config" 将仅显示直接在接口上配置的值
[admin@c52i] > /interface/wifi/print detail config  
Flags: M - master; D - dynamic; B - bound; X - disabled, I - inactive, R - running 
 0 M B  default-name="wifi1" name="wifi1" l2mtu=1560 mac-address=18:FD:74:AF:F4:28 arp-timeout=auto radio-mac=18:FD:74:AF:F4:28 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-5ghz 

 1 M B  default-name="wifi2" name="wifi2" l2mtu=1560 mac-address=18:FD:74:AF:F4:29 arp-timeout=auto radio-mac=18:FD:74:AF:F4:29 configuration=common-conf 
        configuration.mode=ap 
        channel=ch-2ghz 
```

:::info
`print detail` 和 `print detail config` 也可以在 `/interface/wifi/configuration` 上使用，其工作方式与在 `/interface/wifi/` 菜单中相同。
:::

## 访问列表 (Access List)

访问列表提供了多种过滤和管理无线连接的方式。

RouterOS 将检查每个新连接，看其参数是否与访问列表中的任何规则指定的参数匹配。

规则按其在列表中出现的顺序进行检查。仅将第一个匹配规则中指定的管理操作应用于每个连接。

已被访问列表规则接受的连接将被定期检查，以确认它们是否仍在允许的**时间、日期**和**信号范围**内。如果不在，它们将被终止。

:::warning
编写拒绝客户端的访问列表规则时要小心。在被 AP 反复拒绝后，客户端设备可能会开始避开它。在没有先为接口配置 pvid 值的情况下，访问列表无法为 wifi-qcom-ac 接口的客户端设置 VLAN ID。
:::

访问列表有两种参数 - [过滤](#access-list) 和 [动作](#access-list)。过滤属性仅用于匹配客户端，即访问列表规则应应用于的客户端。动作参数可以更改该特定客户端的连接参数，并可能使用访问列表规则中指定的参数覆盖其默认连接参数。

### MAC 地址认证

通过 **query-radius** 动作实现，MAC 地址认证是一种使用 RADIUS 服务器实现客户端 MAC 地址集中白名单的方法。

当客户端设备尝试与配置为执行 MAC 地址认证的 AP 关联时，AP 将向 RADIUS 服务器发送访问请求消息，其中包含设备的 MAC 地址作为用户名和空密码。如果 RADIUS 服务器对此类请求回复 access-accept，则 AP 继续进行为接口配置的任何常规认证过程（密码短语或 EAP 认证）。

### 访问规则示例

仅在工作时间内接受来自附近设备到访客网络的连接：

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled 
 0   signal-range=-60..0 allow-signal-out-of-range=5m ssid-regexp="MikroTik Guest" time=7h-19h days=mon,tue,wed,thu,fri action=accept

 1   ssid-regexp="MikroTik Guest" action=reject 
```

拒绝来自本地管理（'匿名'/'随机化'）MAC 地址的连接：

```ros
/interface/wifi/access-list/print detail
Flags: X - disabled
 0   mac-address=02:00:00:00:00:00 mac-address-mask=02:00:00:00:00:00 action=reject
```

为特定客户端分配不同的密码短语可能很有用，如果您需要为客户端提供无线访问，但不想共享您的无线密码，或者不想创建单独的 SSID。当匹配的客户端连接到该网络时，访问列表将使该客户端使用不同的密码，而不是使用接口配置中定义的密码。只需确保特定客户端不会先被更通用的访问列表规则匹配。

或者拒绝所有未知 MAC 地址，可以作为最终规则添加到访问列表的末尾。- 如果您只想允许网络上的特定客户端，请确保在访问列表的末尾也添加一条拒绝规则，因为默认情况下没有隐式拒绝规则。

```ros
/interface/wifi/access-list
add action=accept disabled=no mac-address=22:F9:70:E5:D2:8E interface=wifi1 passphrase=StrongPassword
```

## 频率扫描 (Frequency scan)

`/interface/wifi/frequency-scan wifi1` 命令提供有关可用信道上射频状况的信息，可通过运行 frequency-scan 命令获取。用于估算频谱使用情况，有助于找到不那么拥挤的频率。

![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-scan.png)

:::info
运行频率扫描将断开所有已连接的客户端，或者如果接口处于 station 模式，它将断开与 AP 的连接。
:::

## 扫描命令 (Scan command)

`/interface/wifi/scan` 命令将扫描接入点并打印有关其检测到的任何 AP 的信息。它不显示每个信道的频率使用情况，但会揭示所有正在传输的接入点。您可以使用“connect”按钮发起与特定 AP 的连接。

scan 命令接受与 frequency-scan 命令相同的所有参数。
![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-scan-command.png)

## 嗅探器 (Sniffer)

sniffer 命令在无线接口上启用监听模式。这将接口转变为所有 WiFi 传输的被动接收器。
该命令持续打印有关接收数据包的信息，并可将它们本地保存到 pcap 文件或使用 TZSP 协议进行流式传输。

嗅探器将在所选接口配置的任何信道上运行。

![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-sniffer.png)

## 频谱扫描 (Spectral scan)

频谱扫描可以扫描您的 wifi 接口支持的频率，并直接在控制台中绘制它们。

:::info
频谱扫描仅由 wifi-qcom 驱动支持；wifi-qcom-ac 驱动不支持。
:::

```ros
/interface/wifi/spectral-scan <wifiinterface name> range=
```

![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-spectral-scan.png)

此命令持续监控频谱数据。此命令使用与 `spectral-history` 相同的数据源，并共享许多参数。

要使用频谱扫描，您必须使用 `range=` 属性。

每行显示一个频谱图桶——频率、幅度 (dBm)、峰值和字符图形条。条形图使用 ':' 字符显示功率值，使用 '.' 字符显示平均峰值保持。

`data` - min/max/avg，默认使用 avg 作为数据。在大多数情况下应使用平均值，但在某些情况下，“min”可用于检查是否存在具有恒定信号输出的频率。Max 表示扫描间隔期间检测到的最强信号，类似于峰值。
`duration` - 在指定时间后终止命令。默认为无限期；
`freeze-frame-interval` - 更新命令输出的时间间隔
`interval` - 更新主要数据值（非峰值）的频率间隔
`peak-mode` - avg/max/disabled - 峰值反映 peak-hold-duration 期间的最强信号。默认使用“avg”。它是 peak-hold-duration 期间最大值的平均值。如果使用“max”，则将显示最高值，直到下一次“peak-hold-duration”更新。
`peak-hold-duration` - 更改 peak-mode 使用的峰值保持持续时间，默认为 5 秒。
`range` - 扫描特定范围，必需；
`resolution` - 频谱扫描的频率步长
`show-interference` - yes/no

可能分类的干扰类型：

- 微波炉 (`MWO`)。
- 连续波 (`CW`)。
- WLAN（宽带）(`WIFI`)。
- 无绳电话 2.4 (`CORDLESS24`)。
- 无绳电话 5 (`CORDLESS5`)。
- 蓝牙 (`BLUETOOTH`)。
- 跳频扩频 (`FHSS`)。

## 频谱历史 (Spectral history)

```ros
/interface/wifi/spectral-history <wifi interface name> range=
```

![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-spectral-history.png)

绘制频谱图。落入不同范围的功率值将打印为具有相同前景和背景颜色的不同字符，因此可以复制和粘贴此命令的终端输出。

`data` - min/max/avg，默认使用 avg 作为数据。在大多数情况下应使用平均值，但在某些情况下，“min”可用于检查是否存在具有恒定信号输出的频率。Max 将显示检测到的最强信号，而不是平均信号。
`interv` - 更新数据值的频率间隔；
`interval` - 打印频谱图行的间隔；
`duration` - 在指定时间后终止命令。默认为无限期；
`range` - 扫描特定范围，必需；
`resolution` - 频率步长；
`show-interference` - yes/no

可能分类的干扰类型：

- 微波炉 (`O`)。
- 连续波 (`C`)。
- WLAN（宽带）(`W`)。
- 无绳电话 2.4 (`T`)。
- 无绳电话 5 (`T`)。
- 蓝牙 (`BB`)。
- 跳频扩频 (`F`)。

## WPS

### WPS 客户端

wps-client 命令能够从启用 WPS 的 AP 获取认证信息。

```ros
/interface/wifi/wps-client/wifi1
```

### WPS 服务器

可以通过运行以下命令使 AP 接受客户端设备 2 分钟的 WPS 认证。

```ros
/interface/wifi/wps-push-button wifi1
```

## 无线电 (Radios)

可以通过运行 `/interface/wifi/radio/print detail` 命令获取有关每个无线电能力的信息。查看接口支持哪些频段以及可以选择哪些信道非常有用。应用于接口的国家/地区配置文件将影响结果。

```ros
/interface/wifi/radio/print detail 
Flags: L - local 
 0 L radio-mac=48:A9:8A:0B:F7:4A phy-id=0 tx-chains=0,1 rx-chains=0,1 
     bands=5ghz-a:20mhz,5ghz-n:20mhz,20/40mhz,5ghz-ac:20mhz,20/40mhz,20/40/80mhz,5ghz-ax:20mhz,
      20/40mhz,20/40/80mhz 
     ciphers=tkip,ccmp,gcmp,ccmp-256,gcmp-256,cmac,gmac,cmac-256,gmac-256 countries=all 
     5g-channels=5180,5200,5220,5240,5260,5280,5300,5320,5500,5520,5540,5560,5580,5600,5620,5640,5660,
            5680,5700,5720,5745,5765,5785,5805,5825 
     max-vlans=128 max-interfaces=16 max-station-interfaces=3 max-peers=120 hw-type="QCA6018" 
     hw-caps=sniffer interface=wifi1 current-country=Latvia 
     current-channels=5180/a,5180/n,5180/n/Ce,5180/ac,5180/ac/Ce,5180/ac/Ceee,5180/ax,5180/ax/Ce,
                 5180/ax/Ceee,5200/a,5200/n,5200/n/eC,5200/ac,5200/ac/eC,5200/ac/eCee,5200/ax...
                 ...5680/n/eC,5680/ac,5680/ac/eC,5680/ax,5680/ax/eC,5700/a,5700/n,5700/ac,5700/ax 
     current-gopclasses=115,116,128,117,118,119,120,121,122,123 current-max-reg-power=30 
```

虽然无线电信息提供了有关支持的信道宽度的信息，但也可以从产品页面推断出此信息。为此，您需要检查以下参数：**链数**、**最大数据速率**。一旦知道这些参数，您需要检查调制和编码方案 (MCS) 表，例如：[https://mcsindex.com/](https://mcsindex.com/)。

如果我们以 hAP ax <sup>2</sup> 为例，我们可以看到链数为 2，MCS 表中的最大数据速率为 1200 - 1201。在 MCS 表中，我们需要找到 2 个空间流（链）的条目以及相应的数据速率，在这种情况下，这向我们表明 80MHz 是支持的最大信道宽度。

## 注册表 (Registration table)

`/interface/wifi/registration-table/` 显示已连接的无线客户端列表及其详细信息。

![](https://manual.mikrotik.com/docs/wireless/wifi/img/wifi-reg-table.png)

### 去认证 (De-authentication)

可以通过从注册表中移除无线对等体来手动去认证（强制重新关联）。

```ros
/interface/wifi/registration-table/remove [find where mac-address=02:01:02:03:04:05]
```

## WiFi CAPsMAN

用于新 WiFi 菜单的 CAPsMAN（受控接入点系统管理器）允许您从中央控制器将无线设置应用于许多 MikroTik WiFi AP。请参阅专门页面：[WiFi CAPsMAN](./capsman.md)。

## 高级示例

[使用 User Manager v5 的企业无线安全](../user-guides/enterprise-wireless-security-user.md)

## 替换 'wireless' 软件包

一些 MikroTik Wi-Fi 5 AP 的接口由 'wireless' 菜单管理，可以通过用 'wifi-qcom-ac' 软件包替换 'wireless' 软件包，使其接口与 'wifi' 菜单兼容。

为此，需要先卸载 'wireless' 软件包，然后安装 'wifi-qcom-**ac**'。

:::info
请注意，“wifi-qcom-ac”驱动程序占用资源要多得多。使用新软件包时，可用 RAM 会减少，这一点需要牢记。
:::

### 兼容性

wifi-qcom-**ac** 软件包包含适用于 IPQ4018/4019 和 QCA9984 无线电的替代驱动程序，使其与 WiFi 配置菜单兼容。有关可能的 wifi-qcom-ac/wifi-qcom/wireless 软件包组合，请参阅[此处](../index.md)的软件包类型部分。

根据经验，该软件包与具有 ARM CPU 的 802.11ac 产品兼容。它与我们任何具有 MIPS CPU 的 802.11ac 产品**不**兼容。

| 兼容性 | 设备 |
| :-- | :-- |
| 兼容 | Audience, Audience LTE kit, Chateau (所有 D53 变体), hAP ac<sup>2</sup>, hAP ac<sup>3</sup>, cAP ac, cAP XL ac, LDF 5 ac, LHG XL 5 ac, LHG XL 52 ac, NetMetal ac<sup>2</sup>, mANTBox 52 15s, wAP ac (RBwAPG-5HacD2HnD), SXTsq 5 ac |
| 不兼容 | RB4011iGS+5HacQ2HnD-IN (不支持 2.4GHz 接口), Cube 60Pro ac (不支持 60GHz 接口), wAP ac (RBwAPG-5HacT2HnD) 以及**所有其他具有 MIPSBE CPU 的设备** |

### 优势

- WPA3 认证和 OWE（机会性无线加密）。
- 802.11w 标准管理帧保护。
- 802.11r/k/v。
- MU-MIMO 和波束成形。
- IPQ4019 接口在 2.4GHz 频段的最大数据速率为 400Mb/s。

:::info
这些优势同时适用于 wifi-qcom 和 wifi-qcom-ac 软件包。
:::

### 丢失的功能

使用与 'wifi' 管理接口兼容的驱动程序运行 802.11ac 产品时，会丢失以下显著功能：

- Nstreme 和 Nv2 无线协议。
- 无线设置中的 VLAN 配置（每接口 VLAN 可以在桥接设置中配置）。
- 与 'wireless' 软件包中实现的 station-bridging 的兼容性。Station-bridge 仅在同一类型的驱动程序之间工作。WiFi 到 WiFi，以及 [Wireless](../index.md) 到 Wireless。

## 属性参考

### AAA 属性

此类别中的属性配置接入点与 AAA (RADIUS) 服务器的交互。

下表中的某些参数将 *format-string* 作为其值。在 *format-string* 中，某些字符按以下方式解释：

| 字符 | 解释 |
| :-- | :-- |
| a | 构成客户端设备 MAC 地址的十六进制字符（小写） |
| A | 构成客户端设备 MAC 地址的十六进制字符（大写） |
| i | 构成 AP 接口 MAC 地址的十六进制字符（小写） |
| I (大写 'i') | 构成 AP 接口 MAC 地址的十六进制字符（大写） |
| N | AP 接口的完整名称（例如 'wifi1'） |
| S | 完整的 SSID |

所有其他字符均按原样使用，不做任何解释。有关示例，请参阅默认值。

| 属性 | 描述 |
| :-- | :-- |
| **called-format** (*format-string*; *默认值: **II-II-II-II-II-II:S**)* | AP 发送给 RADIUS 服务器的消息中 Called-Station-Id RADIUS 属性值的格式。 |
| **calling-format** (*format-string*; *默认值: **AA:AA:AA:AA:AA:AA**)* | AP 发送给 RADIUS 服务器的消息中 Calling-Station-Id RADIUS 属性值的格式。 |
| **interim-update** (*时间间隔; 默认值: ****5m****)* | 向 RADIUS 服务器发送流量计费临时更新的间隔。 |
| **mac-caching** (*时间间隔;* *默认值: **disabled**)* | 启用 MAC 地址认证时，缓存 RADIUS 服务器回复的时间长度。这解决了由于 RADIUS 服务器回复延迟相对较高而导致客户端设备认证超时的问题。 |
| **name** (*字符串*; *默认值: **no**)* | AAA 配置文件的唯一名称。 |
| **nas-identifier** (*字符串*) | AP 发送给 RADIUS 服务器的消息中 NAS-Identifier 属性的值。默认为设备的主机名 (/system/identity)。 |
| **password-format** (*format-string*) | 执行 MAC 地址认证时，用于计算 AP 发送给 RADIUS 服务器的消息中 User-Password 属性值的格式。默认值：""（空字符串）。 |
| **username-format** (*format-string*; *默认值: **AA:AA:AA:AA:AA:AA**)* | 执行 MAC 地址认证时，AP 发送给 RADIUS 服务器的消息中 User-Name 属性值的格式。 |

### 信道属性

此类别中的属性指定所需的无线电信道。

| 属性 | 描述 |
| :-- | :-- |
| **band** (*2ghz-g* \| *2ghz-n* \| *2ghz-ax*\| *2ghz-be* \| *5ghz-a* \| *5ghz-ac* \| *5ghz-an* \| *5ghz-ax* \| *5ghz-be*\| *6ghz-ax* \| *6ghz-be*) | AP 将使用的频段和无线标准。默认为支持的最新标准。**请注意，频段支持受无线电能力限制。**  |
| **deprioritize-unii-3-4** (*no* \| *yes*) | 是否为控制频率为 5720 或 5825-5885 MHz 的信道分配较低优先级。这些信道不受某些客户端设备支持，使得自动选择它们不理想。在 ETSI 监管域中默认为 'yes'，在其他地方默认为 'no'。  |
| **frequency** (*数字或数字范围列表*) | 对于处于 AP 模式的接口，指定选择控制信道中心频率时要考虑的频率（以 MHz 为单位）。 对于处于 station 模式的接口，指定扫描 AP 的频率。  保持未设置（默认）以考虑无线电支持且适用监管配置文件允许的所有频率。  参数可以包含 1 个或多个逗号分隔的十进制数值，或可选地使用语法 RangeBeginning-RangeEnd:RangeStep 表示的数字范围。 有效 channel.frequency 值的示例： 24122412,2432,24725180-5240:20,5500-5580:20 |
| **preamble-puncturing** (*no* \| yes; 默认值: **no***) |  在此接口上为 DFS/radar 启用 puncturing 支持（仅限 802.11be）。  设置后，当检测到雷达信号时，接入点可以仅禁用（“puncture”）宽 80/160 MHz 信道中受影响的 20 MHz 部分，而不是切换整个信道。  对于 80 MHz 信道，可以 puncture 一个 20 MHz 子信道。  对于 160 MHz 信道，可以 puncture 一个 20 MHz 子信道或一个 40 MHz 块。    当前的 puncturing 状态可以在该接口的 `/interface/wifi/monitor` 输出中观察到，其中被 puncture 的子信道用字母 `o` 标记。  |
| **reselect-interval** (*时间间隔; 默认值: **disabled***) | 指定接口应运行“重新扫描信道可用性”并选择最合适信道使用的间隔。指定间隔将允许系统动态且随机地选择此间隔。这有助于避免许多 AP 同时扫描网络、选择相同信道并倾向于同时使用它的情况。reselect-interval 使用后台扫描。  reselect 过程将考虑信道中的网络数量、信道使用情况以及与相邻信道中网络的重叠来选择最合适的信道。它可以与定义的频率列表一起使用，或者不设置 `frequency` - 使用所有支持的频率。  示例： 01:00..01:30 → 将信道的重新扫描设置为每 1 小时 + 最多 30 分钟的随机时间运行一次。第一次，它可能在“1 小时 15 分钟”后运行重新扫描，稍后可能是“1 小时 1 秒”，然后可能是“1 小时 29 分钟 59 秒”……随机地，重新扫描将在每 1 小时到 1 小时 30 分钟之间发生。 |
| **reselect-time** (*时间间隔; 默认值: **disabled***) | 指定接口应运行“重新扫描信道可用性”并选择最合适信道使用的时钟时间。指定时钟时间将允许系统动态且随机地选择此时间。这有助于避免许多 AP 同时扫描网络、选择相同信道并倾向于同时使用它的情况。reselect-time 使用后台扫描。  reselect 过程将考虑信道中的网络数量、信道使用情况以及与相邻信道中网络的重叠来选择最合适的信道。它可以与定义的频率列表一起使用，或者不设置 `frequency` - 使用所有支持的频率。  示例： 01:00..01:30 → 将信道的重新扫描设置为每晚在系统时钟时间 01:00 AM 和 01:30 AM 之间随机运行一次。14:00..14:30 → 将信道的重新扫描设置为每天（中午之后）在系统时钟时间 14:00:00 和 14:30:00（或下午 2 点到 2 点 30 分）之间随机运行一次。 |
| **secondary-frequency** (*整数列表* \| *默认值: **disabled***) | 对于分离的 80+80MHz 信道，指定次要 80MHz 段允许的中心频率。  对于 320MHz 信道，指定允许的 320MHz 信道中心。  未设置（默认）时，不限制信道选择。  例如： 'width=20/40/80+80mhz frequency=518