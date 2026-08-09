# 配置室外CPE到AP的Wi-Fi链路

> 使用MikroTik RouterOS的`wifi-qcom`软件包配置室外CPE到AP的Wi-Fi链路指南，涵盖频率选择、国家法规、AP模式设置、安全性以及长距离连接的距离考量。

# 配置室外CPE到AP的Wi-Fi链路

**软件包：** `wifi-qcom`

众所周知，室内接入点的Wi-Fi覆盖范围是有限的。这主要受当地法规的影响，这些法规限制了设备的输出功率（取决于所使用的频率信道）。典型的室内Wi-Fi连接是在AP（接入点）和客户端（站点）设备（如智能手机、笔记本电脑等）之间建立的。

室内AP通常配备全向天线（允许信号以AP为中心的“甜甜圈”形状广播），其天线增益相对较低。对于室内和短距离室外安装，这是一种理想的天线。使用带有全向天线的简单家用AP，在“理想”的无干扰视距环境下，您可以实现约±100米的距离，而在建筑物内部，这一距离会进一步缩短。

但是！如果您增加AP的天线增益，并将信号“定向”到更小的角度指向特定目的地（而不是以360°广播信号），您就可以实现更远距离的连接（如果站点设备位于定向角度范围内）。这就是室外长距离AP和CPE发挥作用的地方。它们允许建立跨越数公里距离的Wi-Fi连接。

长距离连接要求您有一台以“AP”模式运行的设备，以及一台以“station”模式运行的客户端设备。多个站点可以连接到单个AP。

:::info
本指南适用于运行`wifi-qcom`软件包/驱动程序的802.11 AX设备。
:::

## AP设置

### 频率选择

如引言所述，当地主管部门监管Wi-Fi设备的输出功率。不同国家/地区的不同频率范围可以有不同的允许功率。您可以使用以下命令检查适用于您所在国家/地区配置的限制：

```ros
/interface/wifi/radio/reg-info country=Latvia 0           
  ranges: 2402-2482/20dBm/40MHz            
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs       
          5735-5875/14dBm/80MHz 
```

根据该表，我们可以看到（使用“Latvia”国家/地区配置）我们能获得的最大功率是信道`5490-5730`上的`30 dBm`。

此表中显示的“dBm”代表“允许的EIRP”（EIRP=发射功率+天线增益）。为了不违反任何法规和“法律”，设备的天线增益越高，设置的发射功率就越低（如果设备具有内置天线，这将**自动**发生），以匹配允许的“EIRP”值。

另请注意，最高“EIRP”信道可能是“DFS”信道（这意味着如果在信道上检测到雷达，广播将停止）。这一点需要牢记！

根据这些信息，从表中可以看出，明智的做法是避免使用`5735-5875`范围，因为它仅允许`14 dBm`。

信道上允许的“EIRP”越多 = 可用的输出功率越大 = 信号越强 = 您可以获得的距离越远。

:::note
请注意，有一个名为“Superchannel”的国家/地区配置。在此配置中，对输出功率没有软件限制。此模式只能在受控环境中使用，或者如果您有特殊许可在您的地区使用它。您可以将其与直接在设置中“降低”发射功率值相结合，以获得“自定义”功率输出。
:::

在频率方面，另外请记住，信道宽度越低，干扰越少，您可以获得的距离越远。这意味着，对于更长的距离，请使用20 MHz。

### WiFi接口配置

要配置AP模式，请运行以下命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=ap .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here channel.width=20mhz
```

- `channel.frequency` → 选择AP运行所在的频率信道。如果您想使用“自动”信道选择，可以跳过此项。
- `configuration.country` → 应用国家/地区配置，以便设备遵循输出功率法规。
- `.mode=ap` → 将WiFi接口设置为在“接入点”模式下运行。
- `.ssid=input_your_SSID_here` → 配置AP将广播的SSID名称。
- `security.authentication-types=wpa2-psk` → 指定要支持的身份验证类型。
- `.passphrase=input_your_password_here` → 设置SSID的密码。

:::warning
如果您的链路超过2公里，则必须额外配置一个“distance”参数。此设置不适用于`wifi-qcom-ac`驱动程序。
:::

- `configuration.distance=distance_in_km` → 以公里为单位设置最大链路距离。该值应反映到距离设备最远的AP或站点的距离。未配置的值允许使用2公里的链路。
- `channel.width=20mhz` → 设置信道宽度。信道宽度越低，距离越远（干扰越少）。

### 其他需要考虑的设置

#### 场景 #1

如果您的拓扑中已有DHCP服务器负责向网络提供IP地址，并且您希望将AP安装在其后面：

![](https://manual.mikrotik.com/docs/wireless/wifi/img/configuring-outdoor-cpe-to-ap-links-01.webp)

1. 确保AP已添加[桥接接口](../../bridging-and-switching/index.md#example)，并且所有以太网和WiFi端口[都是其一部分](../../bridging-and-switching/index.md#example-1)。
2. 在该桥上设置[DHCP客户端](../../network-management/dhcp.md#dhcp-client)，或者静态添加[IP地址](../../getting-started/networking-fundamentals/index.md#address-configuration)和[默认路由](../../user-guides/routing-and-networking-protocols/routing-decision.md#default-route)。
3. 如有需要，更改[接口列表成员](../../system-information-and-utilities/interface-lists.md)角色。

#### 场景 #2

如果您希望AP本身充当站点的DHCP服务器：

![](https://manual.mikrotik.com/docs/wireless/wifi/img/configuring-outdoor-cpe-to-ap-links-02.webp)

1. 将以太网端口配置为上行链路/WAN端口，即为以太网接口设置[DHCP客户端](../../network-management/dhcp.md#dhcp-client)或[静态IP](../../getting-started/networking-fundamentals/index.md#address-configuration)，设置默认[路由](../../user-guides/routing-and-networking-protocols/routing-decision.md)，并在[接口列表](../../system-information-and-utilities/interface-lists.md)设置中将该端口归类为“WAN”端口。
2. 在WiFi接口（或WiFi端口所属的桥接接口）之上设置[DHCP服务器](../../network-management/dhcp.md#dhcp-server)，并向该接口添加相应的[IP地址](../../getting-started/networking-fundamentals/index.md#address-configuration)。

## 站点设置

### WiFi接口配置

要配置站点模式，请运行以下命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5500 configuration.country=Latvia .mode=station .ssid=input_your_SSID_here security.authentication-types=wpa2-psk .passphrase=input_your_password_here
```

- `channel.frequency` → 选择AP使用的频率信道。如果您想使用“自动”信道选择，可以跳过此项。
- `configuration.country` → 应用国家/地区配置，以便设备遵循输出功率法规。
- `.mode=station` → 将WiFi接口设置为在“站点”模式下运行。
- `.ssid=input_your_SSID_here` → 输入AP正在广播的SSID名称。
- `security.authentication-types=wpa2-psk` → 指定要支持的身份验证类型。
- `.passphrase=input_your_password_here` → 设置AP期望的密码。

:::warning
如果您的链路超过2公里，则必须额外配置一个“distance”参数。此参数不适用于`wifi-qcom-ac`驱动程序。
:::

- `configuration.distance=distance_in_km` → 以公里为单位设置最大链路距离。该值应反映到距离设备最远的AP或站点的距离。未配置的值允许使用2公里的链路。

### 其他需要考虑的设置

#### 场景 #1

站点WiFi接口被归类为“WAN”接口的场景，这允许站点的客户端隐藏在[NAT](../../firewall-and-quality-of-service/firewall/nat.md)后面。这是大多数CPE设备上应用的出厂配置。

此类拓扑的示例：

![](https://manual.mikrotik.com/docs/wireless/wifi/img/configuring-outdoor-cpe-to-ap-links-03.webp)

这种类型的设置要求CPE具备：

1. WiFi接口在[接口列表成员](../../system-information-and-utilities/interface-lists.md)菜单中被归类为“WAN”端口。
2. 在“其他/以太网”接口上运行[DHCP服务器](../../network-management/dhcp.md#dhcp-server)（建议确保AP的DHCP服务器和站点的DHCP服务器网络不使用相同的子网，因为这可能导致第3层/路由问题）。
3. 将[DHCP客户端](../../network-management/dhcp.md#dhcp-client)或[静态IP](../../getting-started/networking-fundamentals/index.md#address-configuration)应用于WiFi接口，并配置[默认路由](../../user-guides/routing-and-networking-protocols/routing-decision.md)。
4. 在WiFi设置中配置[`mode=station`](../user-guides/wireless-station-modes.md#mode-station)。

#### 场景 #2

可以桥接站点端口的场景，以便CPE本身和所有CPE的客户端从AP获取DHCP地址。

此类拓扑的示例：

![](https://manual.mikrotik.com/docs/wireless/wifi/img/configuring-outdoor-cpe-to-ap-links-04.webp)

这种类型的设置要求CPE具备：

1. 所有端口（WiFi和以太网）都添加到同一个[桥接接口](../../bridging-and-switching/index.md#example)中。
2. 桥接接口在[接口列表成员](../../system-information-and-utilities/interface-lists.md)菜单中被归类为“LAN”接口。
3. 禁用[DHCP服务器](../../network-management/dhcp.md#dhcp-server)。
4. 将[DHCP客户端](../../network-management/dhcp.md#dhcp-client)或[静态IP](../../getting-started/networking-fundamentals/index.md#address-configuration)应用于桥接接口。
5. 在WiFi设置中配置[`mode=station-bridge`](../user-guides/wireless-station-modes.md#mode-station-bridge)：

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=station-bridge
```

## 验证

连接成功后，AP和站点都应在“注册”表中显示一个新条目：

```ros
/interface/wifi/registration-table/print
Flags: A - AUTHORIZED
Columns: INTERFACE, SSID, MAC-ADDRESS, UPTIME, LAST-ACTIVITY, SIGNAL, AUTH-TYPE, BAND
#   INTERFACE  SSID        MAC-ADDRESS        UPTIME    LAST-ACTIVITY  SIGNAL  AUTH-TYPE  BAND   
0 A wifi1      input_SSID  XX:YY:ZZ:AA:30:6E  6h24m21s  0ms            -72     wpa2-psk   5ghz-ax
```

您还可以通过CPE使用“scan”命令检查它是否正确看到/识别AP：

```ros
/interface/wifi/scan [find where name=wifi1]
Flags: A - ACTIVE
Columns: ADDRESS, SSID, CHANNEL, SECURITY, SIGNAL, STA-COUNT
  ADDRESS            SSID               CHANNEL           SECURITY                              SIGNAL  STA-COUNT
A XX:YY:ZZ:AA:F4:28  SSID_Y             5620/ax           WPA2-PSK/WPA3-PSK                     -60             0
A XX:YY:ZZ:BB:0B:DA  SSID_X             5745/ax/Ce        WPA3-PSK                              -68             0
A XX:YY:ZZ:CC:0B:DA  input_SSID         5745/ax/Ce        WPA2-PSK                              -68             0
A XX:YY:ZZ:DD:0B:DA                     5745/ax/Ce        WPA2-PSK                              -68             0
```