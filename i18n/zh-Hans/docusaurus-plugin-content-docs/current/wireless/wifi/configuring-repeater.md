# 配置无线中继器

> 本指南介绍如何使用 MikroTik RouterOS 的 wifi-qcom 软件包配置无线中继器，详细说明双频接口（2.4 GHz 和 5 GHz）的设置步骤、SSID 管理、安全设置，以及漫游行为和距离限制等故障排除注意事项。

# 配置无线中继器

**软件包：** `wifi-qcom`

:::info
本指南适用于运行 `wifi-qcom` 软件包/驱动程序的 802.11 AX 设备。
:::

WiFi 覆盖范围是有限的。AP（广播 Wi-Fi 网络的设备）运行在 2.4 和/或 5 GHz 频率上。5 GHz 网络可提供更好的吞吐量，但覆盖范围较小。2.4 GHz 网络可确保更好的覆盖范围，但吞吐量较低。

室内 AP 通常配备全向天线（允许以 AP 为中心 360° 的“甜甜圈”形状广播信号）。对于室内和短距离室外安装，这是一种理想的天线。使用带有全向天线的简单家用 AP，在“理想”的无干扰视距环境中，您可以实现约 ±100 米的距离，而在建筑物内部，这一距离会进一步缩短。混凝土、管道、金属、水……以及各种其他不同材料都会影响室内 WiFi。有些物体会吸收信号，有些会偏转信号，有些会衍射信号，还有些会散射信号。

考虑到这一点，单个 AP/路由器并不总能覆盖所需的距离范围，因此需要安装额外的 AP。

为了获得最佳吞吐量，每个 AP 都应通过以太网线连接到主网络。但是！由于种种原因（最可能的原因是美观问题），并不总能将网线从 AP 连接到主路由器。

这时，“**中继器**”或“**扩展器**”就能派上用场。

扩展器/中继器的作用是作为“客户端”或“工作站”与主路由器建立 Wi-Fi 连接，将此连接用作上行链路连接，同时广播扩展器自身的 WiFi 网络。

:::info
**吞吐量！**

当设备用作扩展器时，您获得的吞吐量至少会减少一半。

一半的资源用于维持与路由器的持续连接，而另一半则用于重传。这会使总空中传输时间加倍。

此外！由于您将扩展器安装在距离主路由器一定距离的位置……随着距离的增加，WiFi 吞吐量会进一步降低。
:::

:::info
**漫游！**

如果您从路由器设置中复制 SSID 名称，并配置扩展器广播相同的 SSID 名称 → 漫游将完全由客户端决定。

漫游是指您的客户端设备在使用相同 WiFi 名称的不同 AP 之间切换的过程。有一些标准可以帮助“加速”和“平滑”切换过程（如 802.11 r/k/v），但遗憾的是，它们无法在此设置中使用，因此“漫游”或“不漫游”的决定完全取决于客户端。不同厂商实现了不同的算法来决定客户端设备应如何以及何时切换。

请记住这一点！某些具有良好算法（决策能力）的设备将正常漫游，而其他设备可能会一直连接到信号较差的远端 AP。
:::

## 中继器设置

:::info
**使用哪个频率？**

双频路由器和接入点从一开始就应该有两个 Wi-Fi 接口 → wifi1 和 wifi2，分别代表 5 GHz 和 2.4 GHz 频率。对于中继器设置，其中一个接口需要转换为**工作站**接口（将作为另一个网络的客户端），而另一个则应设置为 **ap** 模式（允许设备广播自己的网络）。

如果我们使用 2.4 GHz 作为**工作站**接口，将增加中继器的安装距离，但也会降低可获得的吞吐量。如果我们使用 5 GHz 作为**工作站**接口，则会缩小覆盖范围但增加吞吐量。
:::

:::warning
由于我们将更改 Wi-Fi 和端口相关配置，建议通过以太网端口/网线使用 MAC 地址连接到设备设置。您可以使用 [Winbox](../../management-tools/winbox.md) 的“邻居”选项卡，然后双击列表中设备的 MAC 地址。这样，在后续更改接口相关设置时，您不会失去访问权限。
:::

在我们的示例中，我们希望使用 wifi2（2.4 GHz）作为“工作站”接口，同时让 wifi1（5 GHz）广播中继器自身的 SSID（并且也可能通过 2.4 GHz 重新广播路由器的 SSID）：

![](https://manual.mikrotik.com/docs/wireless/wifi/img/configuring-repeater-01.webp)

整体配置：

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
/interface/list
add comment=defconf name=WAN
add comment=defconf name=LAN
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
/interface/list/member
add comment=defconf interface=bridge list=LAN
/ip/dhcp-client
add interface=bridge
```

### 2.4 GHz 接口配置

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=station-bridge .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=station-bridge` → 选择[工作站模式](../user-guides/wireless-station-modes.md)。

:::info
**使用哪种工作站模式？**

对于 **MikroTik Wi-Fi 6 AX**（使用 `wifi-qcom` 软件包/驱动程序的路由器）到 **MikroTik Wi-Fi 6 AX**（使用 `wifi-qcom` 软件包/驱动程序的中继器/工作站）的连接，请使用 **`station-bridge`** 模式。

对于**第三方厂商**或 **MikroTik 传统 WiFi 5 AC 及以下**（路由器）到 **Wi-Fi 6 AX**（中继器）的连接，请使用 **`station-pseudobridge`** 模式。

`station-pseudobridge` 的作用类似于“网络地址转换”，但使用的是 MAC 地址。使用此模式时，如果有多个设备连接到中继器并访问互联网，路由器将看到所有这些尝试都来自单个 MAC 地址。基本上，所有客户端设备都将隐藏在一个 MAC 地址后面，这可能会导致网络问题。不建议使用此模式，但在这种情况下，没有其他选择。

此外，在传统 MikroTik 设备上使用 `station-pseudobridge` 时，请确保传统设备已通过命令 `/interface/bridge/set protocol-mode=none` 在其桥接端口上禁用 [RSTP](../../bridging-and-switching/user-guides/spanning-tree-protocol.md)。否则，RSTP 可能导致 DHCP 客户端功能出现问题，以及通过桥接端口传递 IP 地址时出现问题。
:::

- `configuration.country=Latvia` → 选择您的实际国家/地区，以免违反任何法规（您所在国家/地区的“法律”）。不同的国家/地区配置文件在不同频率范围内具有不同的允许输出功率。
- `ssid=router.ssid.2` → 这是路由器广播的 2.4 GHz SSID 网络名称（中继器应连接到的网络）。
- `security.authentication-types=wpa2-psk` → 选择主路由器使用的认证类型。
- `passphrase=router.password` → 配置主路由器网络的密码。这是路由器设置中配置的密码。

### 5 GHz 接口配置

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 将接口配置为“接入点”模式。
- `configuration.country=Latvia` → 选择您的实际国家/地区，以免违反任何法规（您所在国家/地区的“法律”）。不同的国家/地区配置文件在不同频率范围内具有不同的允许输出功率。
- `ssid=router.ssid.5` → 配置中继器需要重新广播的无线网络名称（SSID）。它可以与主路由器使用的网络名称相同，也可以是不同的名称。对于测试，最好使用“唯一”名称，以便区分网络。要实现“客户端漫游”，请使用与路由器设置完全相同的 WiFi 名称。
- `security.authentication-types=wpa2-psk` → 选择要使用的认证类型。要实现“客户端漫游”，请使用与路由器设置完全相同的认证类型。
- `passphrase=router.password` → 设置中继器 WiFi 网络的密码。要实现“客户端漫游”，请使用与路由器设置完全相同的密码。

### 可选步骤 - 添加虚拟接口

如果您希望扩展器使用两个频率重新广播无线网络（例如，`wifi2` 保留用于 `mode=station-bridge`，而您只剩下 `wifi1` 用于 `mode=ap`），请在 `station` 接口之上创建虚拟接口：

```ros
/interface/wifi
add configuration.mode=ap .ssid=router.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 确保其作为“接入点”接口运行。
- `ssid=router.ssid.2` → 配置中继器需要重新广播的无线网络名称（SSID）。要实现“客户端漫游”，请使用与路由器设置完全相同的 WiFi 名称。
- `master-interface=wifi2` → 指定“虚拟”接口所基于的接口（指定在其之上创建哪个接口）。选择用作 `station` 接口的接口。
- `name=wifi3` → 为虚拟接口命名。
- `security.authentication-types=wpa2-psk` → 选择要使用的认证类型。要实现“客户端漫游”，请使用与路由器设置完全相同的认证类型。
- `passphrase=router.password` → 设置中继器 WiFi 网络的密码。要实现“客户端漫游”，请使用与路由器设置完全相同的密码。

:::info
虚拟接口将使用与 `station` 接口连接到路由器时完全相同的频率信道。此接口的 Wi-Fi 频率信道无法更改。
:::

### 桥接和列表

[桥接所有端口](../../bridging-and-switching/index.md#example-1)（以太网、Wi-Fi 和虚拟 Wi-Fi 接口）：

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

并确保桥接接口被列为“LAN”接口（`/interface list member add comment=defconf interface=bridge list=LAN`），以便防火墙规则不会阻止对扩展器管理的访问：

```ros
/interface/list/member
add comment=defconf interface=bridge list=LAN
```

当然，前提是您在主路由器上添加了适当的防火墙和访问限制。否则，请进行限制。

### DHCP

```ros
/ip/dhcp-client
add interface=bridge
```

在桥接接口上应用 [DHCP 客户端](../../network-management/dhcp.md#configuration-examples)，以便中继器本身及其所有连接的客户端从主路由器获取 IP 地址。

禁用 [DHCP 服务器](../../network-management/dhcp.md#dhcp-server)功能。

### 地址

如果您的路由器网络使用相同的子网，请移除/禁用默认配置中桥接接口分配的 [IP 地址](../../getting-started/networking-fundamentals/index.md#address-configuration)，以免与网关 IP 产生“冲突”。