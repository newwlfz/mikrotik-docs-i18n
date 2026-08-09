# 首次配置

> 本页面为首次使用 MikroTik RouterOS 配置的用户提供分步指南，涵盖前置条件、连接设置以及 DHCP、NAT 和防火墙等关键概念。指南同时包含 WinBox 图形界面和 CLI 命令行两种方法，适用于新手和高级用户。

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 首次配置

## 开始之前

### 前置条件

在开始配置过程之前，请确保您具备以下条件：

- 一台 MikroTik 路由器
- 一台带有以太网口的电脑（推荐）。如果路由器提供无线接入点，也支持通过 WiFi 进行配置
- 一根以太网线
- 来自 ISP 的可用互联网连接
- 30–60 分钟不被打扰的时间

### 关键概念

- **默认配置：** 出厂预装设置，可能需要根据您的网络需求进行调整
- **Bridge（桥接）：** 一种虚拟接口，将多个物理端口合并为一个网络段
- **DHCP：** 一种自动为网络中的设备分配 IP 地址的协议
- **NAT：** 网络地址转换，允许多台设备共享一个公网 IP 地址
- **防火墙：** 一组用于控制和过滤网络流量以实现安全目的的规则

### 选择您的配置方法

本指南介绍如何使用以下任一方式配置 RouterOS：

- 使用 [WinBox](../management-tools/winbox) 或 [WebFig](../management-tools/webfig) 的图形界面
- 命令行界面（CLI）

如何选择：

- **新手用户：** 建议按照 WinBox 操作说明进行
- **高级用户：** 可以使用代码块中显示的 CLI 命令

:::tip
在完成每个主要配置部分后，建议创建一份设置备份。

**CLI 方法：**

```
/export file=backup-step3
```

**WinBox 方法：**

1. 打开 **Files** 菜单
2. 点击 **Backup**
3. 输入一个描述性名称（例如：`after-internet-setup`）

如果出现问题，您可以从 **Files** 菜单中选择备份并点击 **Restore** 来恢复配置。
:::

## 访问路由器

大多数 MikroTik 路由器出厂时带有默认配置，可立即访问。然而，一些专业设备（如 CCR 系列）可能出厂时仅带有最小化配置或没有默认配置。在这种情况下，请先手动设置网络——参见 [手动网络设置](./manual-network-setup.md)。

### 第 1 步：物理连接

1. 将以太网线从您的电脑连接到路由器的任意以太网端口（**ether1 除外**）。
2. 将 ISP 线缆连接到 **ether1**（通常用作 WAN 接口）。
3. 给路由器上电，等待约一分钟使其完全启动。

```
Internet ─── [ISP] ─── [ether1] MikroTik Router [ether2-ether5] ─── [Switch / Devices]

                                                 │

                                          [WiFi Clients]
```

### 第 2 步：下载 WinBox

如果您还没有 WinBox：

**[下载 WinBox](https://mt.lv/winbox)** 适用于您的操作系统：

可用软件包：

- **Windows：** ZIP 压缩包（包含 `WinBox.exe`）
- **Linux：** ZIP 压缩包（包含可执行二进制文件）
- **macOS：** DMG 软件包

1. 解压或打开下载的软件包。
2. 启动 WinBox：
   - Windows：运行 `WinBox.exe`
   - Linux：使二进制文件可执行并运行
   - macOS：打开 `.dmg` 并启动 WinBox

无需安装。更多详情，请参阅 [WinBox 手册](../management-tools/winbox)。

### 第 3 步：使用邻居发现查找您的路由器

1. 打开 WinBox。
2. 在 **Select from** 下拉菜单中，选择 **Neighbors**。
3. 您的路由器应出现在 **Neighbors** 列表中。
4. 双击路由器条目进行连接：
   - 如果 IP 地址不可达或显示 `0.0.0.0`，请优先使用 **MAC 地址**。
5. 提示时，输入登录凭据：
   - **用户名：** `admin`
   - **密码：** 留空，或使用设备标签上打印的密码（如适用）

### 第 4 步：保护路由器

路由器可访问后，请立即保护其免受未授权访问和基本攻击。请先执行以下操作：

1. **设置管理员密码。** 空密码允许对路由器进行无限制访问。
2. **验证防火墙已启用。** 大多数 MikroTik 设备出厂时带有默认防火墙配置，可阻止最常见的外部攻击。不要禁用现有规则；仅在需要时添加新规则。
3. **禁用来自互联网的直接管理访问。** 这对于没有默认防火墙的设备尤为重要。如果需要远程访问，请使用安全方法，如 **WireGuard** 或 **IPsec**，而不是直接暴露管理端口。

### 用户密码管理

使用强密码保护您的 MikroTik 路由器至关重要。请使用满足以下条件的密码：

- 至少 12 个字符长
- 包含大写和小写字母、数字和符号
- 避免使用字典单词或简单模式

使用 CLI 设置管理员密码：

```ros
/user set 0 password="Your_Super_Strong_Password_123!@#$%^&*"
```

或以交互方式更改：

```ros
[admin@MikroTik] > /password 
old-password: ********
new-password: ****************************
confirm-new-password: ****************************
```

:::danger
请记住您的密码。如果丢失，将无法恢复。您需要重置路由器或重新安装 RouterOS。
:::

您也可以在 `/user` 菜单中管理用户：

```ros
/user/add name=myname password=mypassword group=full
/user/remove admin
```

:::tip
最佳实践是创建一个具有强密码的新管理员用户，验证其可用后，再禁用或删除默认的 **admin** 账户。
:::

## 了解默认配置

当您首次连接到 MikroTik 路由器时，可能会看到关于 [默认配置](./configuration-management/default-configurations) 的提示。以下是您需要了解的内容：

- **对于初学者：** 建议保留默认配置，因为它提供了基本的安全性和基本功能。
- **默认设置包括：** 基本防火墙、DHCP 服务器和默认无线安全设置（如适用）。
- **您可以安全地自定义它**，同时保留默认结构作为基础。

![默认配置提示](https://manual.mikrotik.com/docs/getting-started/img/winbox-first-boot-prompt_01.png)

:::danger
移除默认配置将删除所有内置安全规则和服务。仅建议计划手动配置路由器的高级用户执行此操作。
:::

如果您的设备**没有默认配置**，或者您将其重置为干净状态，则必须手动设置 bridge、LAN IP 地址和 DHCP 服务器——在继续之前请参阅 **[手动网络设置](./manual-network-setup.md)**。

## 配置互联网连接（WAN）

要赋予路由器互联网访问权限，您需要知道您的 ISP 使用哪种连接类型。请咨询您的 ISP，或使用以下描述：

- **DHCP / 动态 IP** — 大多数电缆调制解调器和部分光纤连接。即插即用，自动获取互联网。
- **静态 IP** — 企业连接或部分住宅光纤。您的 ISP 为您提供了特定的 IP 地址、网关和 DNS 服务器。
- **PPPoE** — DSL 连接或部分光纤提供商。您的 ISP 为您提供了连接所需的用户名和密码。

:::tip
**不确定？** 从 DHCP 开始——它适用于约 80% 的家庭连接。
:::

### DHCP / 动态 IP（最常见）

这是家庭用户最简单、最常见的设置。在公网接口上配置 DHCP 客户端，自动从 ISP 获取 IP 地址、DNS 服务器、NTP 服务器和默认路由。

```ros
/ip/dhcp-client/add disabled=no interface=ether1
```

添加客户端后，验证分配的地址并确认状态显示为 "bound"：

```ros
[admin@MikroTik] > ip dhcp-client print
Columns: INTERFACE, USE-PEER-DNS, ADD-DEFAULT-ROUTE, STATUS, ADDRESS
# INTERFACE  USE-PEER-DNS  ADD-DEFAULT-ROUTE  STATUS  ADDRESS        
0 ether1     yes           yes                bound   1.2.3.100/24
```

### 静态 IP

如果您的 ISP 提供了不会更改的特定网络设置，请使用此方法。您的 ISP 提供三个参数：

- IP 地址：**`1.2.3.100/24`**
- 网关：**`1.2.3.1`**
- DNS 服务器：**`8.8.8.8`**

将 IP 地址添加到 WAN 接口，使用网关创建默认路由，并设置 DNS 服务器：

```ros
/ip/address/add address=1.2.3.100/24 interface=ether1
/ip/route/add gateway=1.2.3.1
/ip/dns/set servers=8.8.8.8
```

### PPPoE

如果您的 ISP 提供了登录凭据（常见于 DSL 提供商），请使用此方法。PPPoE 提供动态 IP 地址，并可自动配置 DNS 服务器和默认路由。

<Tabs>
<TabItem value="cli" label="CLI" default>

```ros
/interface/pppoe-client
add disabled=no interface=ether1 user=me password=123 \
  add-default-route=yes use-peer-dns=yes
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

1. 打开 **PPP** 窗口并导航到 **Interface** 选项卡。
2. 点击 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按钮添加新接口。
3. 从下拉列表中选择 **PPPoE Client**。
4. 输入连接名称并选择 **ether1** 作为接口。

   ![](https://manual.mikrotik.com/docs/getting-started/img/pppoe_client_01.png)
5. 转到 **Dial Out** 选项卡，输入您的 ISP 提供的用户名和密码。
6. 根据 ISP 要求配置任何其他参数。
7. 点击 <kbd>**OK**</kbd> 保存设置。

   ![](https://manual.mikrotik.com/docs/getting-started/img/pppoe_client_02.png)

</TabItem>
</Tabs>

:::warning
配置后，WAN 接口变为 **pppoe-out1** 而不是 **ether1**。后续所有与 WAN 相关的配置请使用此接口。
:::

## 验证互联网连接

配置 WAN 连接后，确认路由器本身可以访问互联网。首先通过 ping 一个已知的公网 IP 地址来测试 IP 连通性——Google 的公共 DNS 服务器 `8.8.8.8`：

```ros
[admin@MikroTik] > /ping 8.8.8.8
  SEQ HOST                                     SIZE TTL TIME       STATUS             
    0 8.8.8.8                                    56  55 14ms399us 
    1 8.8.8.8                                    56  55 18ms534us 
    2 8.8.8.8                                    56  55 14ms384us 
```

然后通过 ping 域名验证 DNS 解析是否正常：

```ros
[admin@MikroTik] > /ping google.com
  SEQ HOST                                     SIZE TTL TIME       STATUS             
    0 142.250.74.14                              56  55 14ms475us 
    1 142.250.74.14                              56  55 14ms308us 
    2 142.250.74.14                              56  55 14ms238us
```

如果 IP ping 成功但域名 ping 失败，说明连接正常但 DNS 配置不正确。如果两者都成功，则路由器自身的互联网连接完全正常。如果任一失败，请参阅 [故障排除](#troubleshooting) 部分。

路由器后面的本地设备仍需要有效的 NAT 规则才能访问互联网——请参阅下一部分。

## NAT 配置

:::note
如果您保留了**默认配置**，则已在 WAN 接口上设置了源 NAT（masquerade）规则，因此本地设备已经可以访问互联网——您可以跳过此部分。以下步骤仅适用于您的路由器**没有默认配置**或您正在构建自定义设置的情况。
:::

要使本地设备访问互联网，路由器必须将其出站数据包的私有源地址转换为其自身的公网 IP 地址。私有地址无法在互联网上路由，因此没有此转换，远程主机将无法回复您的本地设备。这通过在 WAN 接口上设置源 NAT（masquerade）规则来实现：

```ros
/ip/firewall/nat
add chain=srcnat out-interface=ether1 action=masquerade
```

:::danger
如果公网接口是 PPPoE、LTE 或其他类型，'out-interface' 应设置为该接口。
:::

或者，可以使用接口列表实现更灵活的配置。

首先，创建一个名为 WAN 的接口列表，并将所有外部接口添加到其中：

```ros
/interface list add name=WAN
/interface list member add list=WAN interface=ether1
```

然后在 NAT 规则中使用接口列表：

```ros
/ip/firewall/nat
add chain=srcnat out-interface-list=WAN ipsec-policy=out,none action=masquerade
```

此设置的另一个好处是，默认情况下，路由器后面的客户端无法从互联网直接访问，这有助于保护它们免受未经请求的入站流量攻击。

### 端口转发

某些客户端设备可能需要从互联网直接访问特定端口。例如，IP 地址为 192.168.88.254 的客户端设备必须可通过远程桌面协议（RDP）访问。

经过快速搜索，您可以发现 RDP 运行在 TCP 端口 3389 上。现在您可以添加目标 NAT 规则，将 RDP 流量重定向到客户端 PC。

```ros
/ip/firewall/nat/add chain=dstnat action=dst-nat protocol=tcp dst-port=3389 to-addresses=192.168.88.254 to-ports=3389
```

:::tip
如果您设置了严格的防火墙规则，则必须在防火墙过滤器的 forward 链中允许 RDP 协议。
:::

## 设置无线 / WiFi

如何配置无线取决于您的 RouterOS 版本和驱动程序：

- **现代 WiFi** (`/interface wifi`) — 使用新 WiFi 协议栈的 RouterOS v7 设备。
- **传统无线** (`/interface wireless`) — RouterOS v6 和较旧的 v7 软件包。

本指南展示一个基本的安全接入点（SSID + WPA2/WPA3 密码）。有关高级主题——Wi-Fi 6/7、MLD / 多链路、多无线电、CAPsMAN、中继器以及按设备系列指导——请参阅 [无线](../wireless/index.md) 部分。

:::note
以下示例假设：国家 = `Latvia`，SSID = `MikroTik-12345`，在支持的地方启用 WPA2/WPA3，禁用 WPS。
:::

<Tabs>
<TabItem value="wifi" label="现代 WiFi (/interface wifi)" default>

创建安全配置文件：

```ros
/interface wifi security
add name=myProfile authentication-types=wpa2-psk,wpa3-psk \
  passphrase="YOUR_STRONG_PASSWORD"
```

配置无线电：

```ros
/interface wifi
set [ find default-name=wifi1 ] configuration.country=Latvia \
  .mode=ap .ssid="MikroTik-12345" .hide-ssid=no \
  channel.width=20mhz disabled=no \
  security=myProfile security.wps=disable

set [ find default-name=wifi2 ] configuration.country=Latvia \
  .mode=ap .ssid="MikroTik-12345" .hide-ssid=no \
  channel.width=20mhz disabled=no \
  security=myProfile security.wps=disable
```

![](https://manual.mikrotik.com/docs/getting-started/img/wireless-setup_03.png)

</TabItem>
<TabItem value="legacy" label="传统无线 (/interface wireless)">

创建安全配置文件：

```ros
/interface/wireless/security-profiles
add name="myProfile" authentication-types=wpa2-psk mode=dynamic-keys \
wpa2-pre-shared-key="YOUR_STRONG_PASSWORD"
```

配置无线电：

```ros
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n channel-width=20/40mhz-Ce distance=indoors \
  mode=ap-bridge ssid=MikroTik-12345 wireless-protocol=802.11 \
  security-profile=myProfile frequency-mode=regulatory-domain \
  country=latvia antenna-gain=3

set [ find default-name=wlan2 ] band=5ghz-a/n/ac channel-width=20/40mhz-Ce distance=indoors \
  mode=ap-bridge ssid=MikroTik-12345 wireless-protocol=802.11 \
  security-profile=myProfile frequency-mode=regulatory-domain \
  country=latvia antenna-gain=3
```

<video controls width="600">
  <source src="/videos/wireless-setup_video.mp4" type="video/mp4" />
</video>

</TabItem>
</Tabs>

### 将无线接口添加到 bridge

每个应提供 LAN 访问的无线接口都必须添加到 bridge 中。如果未添加，无线客户端将无法获取 DHCP 地址、访问 LAN 设备或访问互联网——即使 WiFi 连接成功。

:::note
如果您保留了**默认配置**，无线接口通常已在 bridge 中，因此可以跳过此步骤。此步骤主要适用于手动设置，其中 bridge 创建为 `bridge1`。
:::

```ros
/interface bridge port
add interface=wifi1 bridge=bridge1
add interface=wifi2 bridge=bridge1
```

对于传统无线，请改用 `wlanN` 接口名称（例如 `wlan1`、`wlan2`）。

## 配置完成

此时，路由器应：

- 为本地设备提供互联网访问
- 使用 DHCP 自动分配 IP 地址
- 保护设备免受来自互联网的未经请求的访问
- 提供无线连接（如适用）

您现在可以继续学习更高级的主题，如 VPN、VLAN、路由、监控和网络管理。

## 下一步：保护您的路由器

您的路由器现已上线。在投入生产使用之前，请加固其安全性以防止未授权访问：设置强密码和唯一用户名，保留默认防火墙规则，限制管理服务，并禁用任何您不使用的功能。

请参阅 **[保护您的路由器](./securing-your-router.md)** 获取完整的加固检查清单，包括公网接口的防火墙规则、MAC 访问和邻居发现限制、服务端口加固以及 SSH 强加密。

## 故障排除

RouterOS 具有各种内置故障排除工具，如 ping、traceroute、torch、数据包嗅探器、带宽测试等。

我们在本文中已经使用了 ping 工具来 [验证互联网连接](#verify-internet-connectivity)。

### ping 失败时的故障排除

ping 工具的问题在于它只显示目的地**不可达**，但没有更详细的信息。让我们回顾一下基本错误。

您无法从连接到 MikroTik 设备的电脑访问 [www.google.com](https://www.google.com)：

![](https://manual.mikrotik.com/docs/getting-started/img/troubleshoot-if-ping-fail.jpg)

:::tip
如果您不确定如何精确配置您的网关设备，请联系 MikroTik 官方 [顾问](https://mikrotik.com/consultants) 获取配置支持。
:::