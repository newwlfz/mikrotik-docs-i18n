# 手动网络设置（无默认配置）

> 如何手动设置一台没有默认配置的 MikroTik 路由器：重置至干净状态、创建桥接、分配 LAN IP 地址，并通过 CLI 或 WinBox/WebFig 配置 DHCP 服务器。

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# 手动网络设置（无默认配置）

大多数 MikroTik 路由器出厂时带有[默认配置](./configuration-management/default-configurations)，该配置已提供桥接、LAN IP 地址、DHCP 服务器和基本防火墙。如果您保留默认配置，则可以跳过本页内容。

仅当您的设备**没有默认配置**，或您已将其重置为干净状态时，才需按照以下步骤操作。

## 从干净配置开始

1. 将网线连接到路由器的 **ether1** 端口。
2. 将您的计算机连接到其他任意 **Ethernet** 端口。
3. 打开 WinBox，使用邻居发现功能定位路由器。详细说明请参阅 [WinBox 文章](../management-tools/winbox)。
4. 选择路由器的 MAC 地址，点击 **Connect**。

要完全从干净配置开始，请运行以下命令：

```ros
/system/reset-configuration no-defaults=yes skip-backup=yes
```

路由器将重启，且不包含任何默认设置、防火墙规则或服务配置。

或者通过 WinBox 操作：

![](https://manual.mikrotik.com/docs/getting-started/img/reset-config-to-default_01.png)

## 创建桥接并分配 IP 地址

由于 MAC 连接有时可能不稳定，第一步是启用 IP 连接。这涉及三个主要任务：

- 创建桥接接口并分配桥接端口
- 为桥接接口分配 IP 地址
- 配置 DHCP 服务器

<Tabs>
<TabItem value="cli" label="CLI" default>

创建桥接接口，将所需的以太网端口添加为桥接端口，并为桥接分配 IP 地址：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add interface=ether2 bridge=bridge1
/ip/address/add address=192.168.88.1/24 interface=bridge1
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

1. 打开 **Bridge** 窗口，确保选中 **Bridge** 选项卡。
   - 点击 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按钮以打开新对话框。您可以输入自定义桥接名称，或保留默认的 **bridge1**，然后点击 <kbd>**OK**</kbd> 继续。

     ![](https://manual.mikrotik.com/docs/getting-started/img/add_bridge.png)
2. 切换到 **Ports** 选项卡，点击 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按钮以打开另一个对话框。
   - 选择 **ether2** 作为接口，**bridge1** 作为桥接，然后点击 <kbd>**OK**</kbd>。对要添加到桥接的每个额外端口重复此步骤。

     ![](https://manual.mikrotik.com/docs/getting-started/img/add_bridge_port.png)
   - 您可以关闭桥接对话框。
3. 进入 **IP** 菜单，导航至 **Address** 对话框。
   - 点击 <kbd>**New**</kbd> 或 <kbd>**+**</kbd> 按钮以打开新对话框。
   - 输入 IP 地址 **`192.168.88.1/24`**，并从下拉列表中选择接口 **bridge1**。

     ![](https://manual.mikrotik.com/docs/getting-started/img/ip_addr_add.png)
   - 点击 <kbd>**OK**</kbd> 确认设置。

</TabItem>
</Tabs>

## 设置 DHCP 服务器

<Tabs>
<TabItem value="cli" label="CLI" default>

为简化和加快此过程，请运行设置命令。大多数配置选项会自动确定，您只需按 <kbd>Enter</kbd> 接受每个值即可：

```ros
[admin@MikroTik] > ip dhcp-server/ setup [enter]
选择运行 DHCP 服务器的接口 

dhcp server interface: bridge1 [enter]
选择 DHCP 地址的网络 

dhcp address space: 192.168.88.0/24 [enter]
选择给定网络的网关 

gateway for dhcp network: 192.168.88.1 [enter]
选择 DHCP 服务器分配的 IP 地址池 

addresses to give out: 192.168.88.2-192.168.88.254 [enter]
选择 DNS 服务器 

dns servers: 192.168.88.1 [enter]               
选择租约时间 

lease time: 1800 [enter]
```

</TabItem>
<TabItem value="winbox" label="WinBox / WebFig">

DHCP 服务器设置向导也可在 [WinBox](../management-tools/winbox) 和 [WebFig](../management-tools/webfig) 中使用：

- 导航至 **IP → DHCP Server** 窗口，确保选中 **DHCP** 选项卡。
- 点击 <kbd>**DHCP Setup**</kbd> 按钮以打开新对话框。

  ![](https://manual.mikrotik.com/docs/getting-started/img/dhcp_setup_01.png)

- 选择 **bridge1** 作为 **DHCP Server Interface**，然后点击 <kbd>**Next**</kbd>。
- 按照向导完成设置。

</TabItem>
</Tabs>

完成以上步骤后，连接的 PC 应能自动获取动态 IP 地址。然后您可以关闭 WinBox，并使用 IP 地址 **`192.168.88.1`** 重新连接到路由器。

当 IP 连接正常后，请继续参阅[配置互联网连接](./first-time-configuration.md#configuring-the-internet-connection-wan)及首次配置指南的其余部分。