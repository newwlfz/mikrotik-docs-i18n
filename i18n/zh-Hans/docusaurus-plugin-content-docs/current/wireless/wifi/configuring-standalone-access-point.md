# 配置独立接入点

> 本指南提供使用 MikroTik RouterOS 的 wifi-qcom 包配置独立接入点（AP）的说明，详细介绍了 2.4/5 GHz 网络的设置步骤、天线选择及桥接配置，同时警告在无 CAPSMAN 管理的情况下漫游功能的局限性。

# 配置独立接入点

**软件包：** `wifi-qcom`

:::info
本指南适用于运行 `wifi-qcom` 包/驱动程序的 802.11 AX 设备。
:::

Wi-Fi 设备可以扮演不同的角色。几乎每个家庭都拥有的最常见设备称为 Wi-Fi 路由器。典型的 Wi-Fi 路由器通常具有 WAN 端口（用于 ISP 连接）、LAN 端口（用于本地 PC、有线打印机等）和 WLAN 网络（Wi-Fi 网络）。路由器也被称为“网关”和“防火墙”，因为它们充当本地网络客户端通往互联网的“门户”（这些设备将 LAN 连接的客户端“隐藏”在它们身后并加以保护）。

:::info
路由器是一种防火墙/网关设备，ISP 电缆连接到它，并且受[防火墙保护](../../firewall-and-quality-of-service/firewall/index.md)，同时启用了 [DHCP 服务器](../../network-management/dhcp.md#dhcp-server)功能（为通过无线和有线方式连接的 LAN 客户端提供 IP 地址）。
:::

Wi-Fi 设备的另一种角色称为“接入点”或简称“AP”。这些设备通常通过以太网连接（连接到路由器的 LAN 端口）连接到主“路由器/网关/防火墙”；它们不受防火墙保护，并且未启用 DHCP 服务器功能（它们不提供 IP 地址）。AP 将其所有 Wi-Fi 和 LAN 接口/端口桥接在一起，因此 AP 从路由器连接“获取”IP 地址，并将其“传递”给连接到 AP 的客户端（充当“二层”桥接/交换机）。

:::info
接入点是“桥接”设备，通过以太网电缆连接到路由器；它们不受[防火墙保护](../../firewall-and-quality-of-service/firewall/index.md)，并且已禁用 [DHCP 服务器](../../network-management/dhcp.md#dhcp-server)功能（它们将来自路由器的 DHCP 请求“桥接”到 AP 的客户端）。
:::

换句话说，**Wi-Fi 路由器** **就是** **具有附加功能的 AP**。

AP（广播 Wi-Fi 网络的设备）运行在 2.4 和/或 5 GHz 频率上。5 GHz 网络可实现更好的吞吐量，但覆盖范围较小。2.4 GHz 网络确保更好的覆盖范围，但吞吐量较低。

室内 AP 通常配备全向天线（允许以“甜甜圈”形状在 AP 周围 360° 广播信号）。对于室内和短距离室外安装，这是理想的天线选择。使用带有全向天线的简单家用 AP，在“理想”的无干扰视距设置下，您可以实现最长约 ±100 米的距离，但在建筑物内部，该距离会大大缩短。混凝土、管道、金属、水……以及各种其他不同材料都会影响室内 Wi-Fi。有些物品会吸收信号，有些会偏转信号，有些会衍射信号，还有些会散射信号。

考虑到这一点，单个 AP/路由器并不总能覆盖所需的范围，需要安装额外的 AP，这意味着如果您家中有 Wi-Fi 信号差或完全无信号的区域，请考虑在问题区域附近安装新的 AP。

:::warning
**本指南适用于**“基本”或所谓的**“独立”AP 设置**。如果您拥有第三方厂商的 Wi-Fi 路由器（非 MikroTik）、旧款 Wi-Fi 5（AC）MikroTik 路由器，或者您之前的设置完全没有 Wi-Fi AP，则可以使用本指南。

**对于由 `wifi-qcom` 包/驱动程序 AP 组成的设置，请使用 [CAPSMAN 管理](./capsman.md)**，因为它支持 802.11 r/k/v 漫游标准，可平滑客户端的切换过程。
:::

:::note
**非 802.11 r/k/v 漫游！**

在“独立”AP 设置中，如果您只是从路由器设置中复制 SSID 名称并配置 AP 广播相同的 SSID 名称 → 漫游将完全取决于客户端。

漫游是指您的客户端设备在使用相同 Wi-Fi 名称的不同 AP 之间切换。有一些标准可以帮助“加速”和“平滑”切换过程（如 802.11 r/k/v），但不幸的是，它们不能在此设置中使用（因为没有“管理器”设备），因此“漫游”或“不漫游”的决定完全由客户端决定。不同厂商实现了不同的算法来决定您的客户端设备应如何以及何时切换。

请记住这一点！一些具有良好算法（决策制定）的设备将正确漫游，而其他设备可能会坚持使用信号较差的（最远的）AP。
:::

我们的大多数（如果不是全部）MikroTik Wi-Fi 设备都预配置为[“路由器”角色](../../getting-started/first-time-configuration.md)。本指南将向您展示如何将它们转变为独立 AP 角色设备（二层桥接 AP）。

## 接入点设置

:::warning
因为我们将更改 Wi-Fi 和端口相关配置，建议通过以太网端口/电缆使用 MAC 地址连接到设备的设置。您可以使用 [Winbox](../../management-tools/winbox.md) 的“邻居”选项卡，然后双击列表中设备的 MAC 地址。这样，在稍后更改接口相关设置时，您不会失去访问权限。
:::

整体配置：

```ros
/interface/wifi
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
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
set [ find default-name=wifi2 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.2 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 将接口配置为“接入点”模式。
- `configuration.country=Latvia` → 选择您的实际国家/地区，以免违反任何法规（您所在国家的“法律”）。不同的国家/地区配置文件在不同频率范围内允许不同的输出功率。
- `ssid=router.ssid.2` → 配置 AP 需要广播的无线网络名称（SSID）。它可以与主路由器使用的网络名称相同，也可以是不同的名称。为了测试，最好使用“唯一”名称，以便区分网络。要实现“客户端漫游”，请使用与路由器设置中完全相同的 Wi-Fi 名称。
- `security.authentication-types=wpa2-psk` → 选择要使用的认证类型。要实现“客户端漫游”，请使用与路由器设置中完全相同的认证类型。
- `passphrase=router.password` → 设置 AP 的 Wi-Fi 网络密码。要实现“客户端漫游”，请使用与路由器设置中完全相同的密码。

### 5 GHz 接口配置

```ros
/interface/wifi
set [ find default-name=wifi1 ] configuration.mode=ap configuration.country=Latvia .ssid=router.ssid.5 disabled=no security.authentication-types=wpa2-psk .passphrase=router.password
```

- `configuration.mode=ap` → 将接口配置为“接入点”模式。
- `configuration.country=Latvia` → 选择您的实际国家/地区，以免违反任何法规（您所在国家的“法律”）。不同的国家/地区配置文件在不同频率范围内允许不同的输出功率。
- `ssid=router.ssid.5` → 配置 AP 需要广播的无线网络名称（SSID）。它可以与主路由器使用的网络名称相同，也可以是不同的名称。为了测试，最好使用“唯一”名称，以便区分网络。要实现“客户端漫游”，请使用与路由器设置中完全相同的 Wi-Fi 名称。
- `security.authentication-types=wpa2-psk` → 选择要使用的认证类型。要实现“客户端漫游”，请使用与路由器设置中完全相同的认证类型。
- `passphrase=router.password` → 设置 AP 的 Wi-Fi 网络密码。要实现“客户端漫游”，请使用与路由器设置中完全相同的密码。

#### **增加 5 GHz 覆盖范围**

当地主管部门监管 Wi-Fi 设备的输出功率。不同国家/地区的不同频率范围可能允许不同的功率。您可以使用以下命令检查适用于您国家/地区配置文件的限制：

```ros
/interface/wifi/radio/reg-info country=Latvia 0      
  ranges: 2402-2482/20dBm/40MHz   
          5170-5250/23dBm/160MHz/indoor    
          5250-5330/23dBm/160MHz/indoor/dfs
          5490-5730/30dBm/160MHz/dfs     
          5735-5875/14dBm/80MHz 
```

根据该表，我们可以看到（使用“Latvia”国家/地区配置文件）我们可以在 `5490-5730` 信道上获得最大功率 `30 dBm`。

此表中显示的“dBm”表示“允许的 EIRP”（EIRP = 发射功率 + 天线增益）。为了不违反任何法规和“法律”，设备的天线增益越高，设置的发射功率就越低（如果设备具有内置天线，这将**自动**发生），以匹配允许的“EIRP”值。

另请注意，最高“EIRP”信道可能是“DFS”信道（意味着如果在信道上检测到雷达，广播将停止）。这一点需要牢记！

根据这些信息，从表中可以看出，明智的做法是避免使用 `5735-5875` 范围，因为它仅允许 `14 dBm`。

信道上允许的“EIRP”越多 = 可用的输出功率越多 = 信号越强 = 您可以获得的距离越大。

:::info
请注意，有一个名为 `Superchannel` 的国家/地区配置文件。在此配置文件中，输出功率没有软件限制。此模式只能在受控环境中使用，或者如果您在所在地区获得特殊许可。您可以将其与直接在设置中“降低”发射功率值相结合，以获得“自定义”功率输出。
:::

要设置信道或范围，请运行命令：

```ros
/interface/wifi
set [ find default-name=wifi1 ] channel.frequency=5490-5730
```

### 可选步骤 - 添加虚拟接口

如果您想创建额外的网络（额外的 SSID 名称），您可以在另一个接口之上创建 `virtual` 接口：

```ros
/interface/wifi
add configuration.mode=ap .ssid=guest.ssid.2 disabled=no master-interface=wifi2 name=wifi3 security.authentication-types=wpa2-psk .passphrase=guest.password
```

- `configuration.mode=ap` → 确保它将充当“接入点”接口。
- `ssid=guest.ssid.2` → 配置 AP 需要广播的无线网络名称（SSID）。要实现“客户端漫游”，请使用与路由器设置中完全相同的 Wi-Fi 名称。
- `master-interface=wifi2` → 指定“虚拟”接口所基于的接口（指定在其之上创建该接口的接口）。
- `name=wifi3` → 为虚拟接口命名。
- `security.authentication-types=wpa2-psk` → 选择要使用的认证类型。要实现“客户端漫游”，请使用与路由器设置中完全相同的认证类型。
- `passphrase=guest.password` → 设置 AP 的 Wi-Fi 网络密码。要实现“客户端漫游”，请使用与路由器设置中完全相同的密码。

:::info
虚拟接口将使用与 `master` 接口完全相同的频率信道。此接口的 Wi-Fi 频率信道无法更改。
:::

### 桥接和列表

[桥接所有端口](../../bridging-and-switching/index.md#example-1)：

```ros
/interface/bridge
add auto-mac=no comment=defconf name=bridge
/interface/bridge/port
add interface=all bridge=bridge 
```

并确保桥接被列为“LAN”接口（`/interface list member add comment=defconf interface=bridge list=LAN`），以便防火墙规则不会阻止对 AP 管理的访问：

```ros
/interface/list/member
add comment=defconf interface=bridge list=LAN
```

当然，前提是您在主路由器上添加了适当的防火墙和访问限制。否则，请加以限制。

### DHCP

```ros
/ip/dhcp-client
add interface=bridge
```

在桥接接口之上应用 [DHCP 客户端](../../network-management/dhcp.md#configuration-examples)，以便 AP 本身及其所有连接的客户端从主路由器获取 IP 地址。

禁用 [DHCP 服务器](../../network-management/dhcp.md#dhcp-server)功能。

### 地址

如果您的路由器网络使用相同的子网，请移除/禁用默认配置中桥接分配的 [IP 地址](../../getting-started/networking-fundamentals/index.md#address-configuration)，以免与网关 IP 产生“冲突”。