# Fail-over PtP GUI 示例

> 本指南演示了如何使用 MikroTik RouterOS GUI 在 60GHz 无线网桥和绑定 5GHz 接口之间配置自动故障切换，包括网桥设置、无线模式选择和安全配置文件创建，以实现无缝冗余。

# Fail-over PtP GUI 示例

### 概述

本示例展示了如何在 GUI 中配置 60GHz 设备与 5GHz 链路之间的自动故障切换（绑定）。  
当 60GHz 无线连接丢失时，系统将自动使用绑定接口。  
本示例从空配置状态开始，使用 [[WinBox](https://mikrotik.com/download)] 工具进行操作。

### 连接设备

配置重置后，仅支持 MAC-telnet 连接。在 WinBox 主界面中，点击“Neighbours”，选择设备的 MAC 地址，然后点击“Connect”：

1. 选择正确的设备 **MAC 地址**。
2. 默认登录名为“**admin**”，未设置密码。
3. 点击 **Connect**。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-01.webp)

### 配置网桥

添加新网桥：

1. 打开 Bridge 子菜单；
2. 点击“+”添加新网桥；
3. 应用更改。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-02.webp)

*后续步骤中需要将接口成员分配给该网桥。这将允许流量无需路由即可从 Ethernet 传递到 W60G 接口。*

### 设置 60GHz 无线连接

之前解释的所有步骤对于 **bridge** 和 **station** 设备均相同。配置无线接口时需使用不同的模式。

配置 **bridge** 设备如下：

1. 打开 Interface 菜单；
2. 双击 wlan60-1 接口；
3. 点击 Wireless 子菜单，将模式设置为 **bridge**（对于 PtmP 则为 **ap-bridge**）；
4. 设置 SSID、密码和区域；
5. 在“Put Stations In Bridge”下选择之前创建的网桥；
6. 应用更改；
7. 点击 Enable 开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-03.webp)

配置 **station** 设备如下：

1. 打开 Interface 菜单；
2. 双击 wlan60-1 接口；
3. 点击 Wireless 子菜单，将模式设置为 **station bridge**；
4. 设置 SSID 和密码；
5. 应用更改；
6. 点击 Enable 开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-04.webp)

### 设置 5GHz 无线连接

#### 为设备选择安全配置文件

1. 选择 **Wireless** 菜单；
2. 选择 **Security Profiles** 子菜单；
3. 点击“+”添加新配置文件；
4. 选择 **名称**、**模式**、**认证类型** 和安全密码；
5. **应用** 配置。

**![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-05.webp)**

#### 对于 bridge 设备

1. 打开 **Interfaces** 菜单；
2. 双击 **wlan1** 接口；
3. 点击 **Wireless** 子菜单，将模式设置为 **bridge**（对于 PtmP 则为 **ap-bridge**）；
4. 设置 **SSID**、**密码** 和 **国家**；
5. 点击 **Advanced Mode**；

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-06.webp)

1. 选择您的 **安全配置文件**；
2. **应用** 更改；
3. 点击 **enable** 开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-07.webp)

#### 对于 station 设备

1. 打开 **Interfaces** 菜单；
2. 双击 **wlan1** 接口；
3. 打开 **Wireless** 子菜单，将模式设置为 **station-bridge**；
4. 设置 **SSID**、**密码** 和 **国家**；
5. 打开 **高级** 模式（与 bridge 设备类似\*）；
6. 选择 **安全配置文件**；
7. **应用** 更改；
8. 点击 **enable** 开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-08.webp)

*如果一切配置正确，运行（R）标志应如截图所示出现：*  
![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-09.webp)

### 配置绑定

*配置绑定并分配从属接口，在本设置中选择内置的 wlan1 接口，但在其他类型的设置中也可以是以太网接口。*

#### 对于 bridge 设备

1. 点击 **Bonding** 子菜单；
2. 点击“+”添加新成员；
3. 将接口成员（**wlan1** 和 **wlan60-station-1**）作为 **Slaves** 添加到 **bonding** 接口；
4. 将接口成员 **wlan60-station-1** 添加为 **Primary** 接口；
5. 选择模式为 **active backup**；
6. **应用** 配置。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-10.webp)

#### 对于 station 设备

1. 点击 **Bonding** 子菜单；
2. 点击“+”添加新成员；
3. 将接口成员（**wlan1** 和 **wlan60-1**）作为 **Slaves** 添加到 **bonding** 接口；
4. 将接口成员 **wlan60-1** 添加为 **Primary** 接口；
5. 选择模式为 **active backup**；
6. **应用** 配置。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-11.webp)

### 配置网桥

*配置包含绑定接口的网桥设置对于 active-backup 在所用设备上正常工作至关重要（本例中 bridge 和 station 设备设置相同）：*

1. 点击 **Bridge** 子菜单；
2. 点击“+”添加新成员；
3. 将接口成员添加为 **ether1**，网桥成员添加为 **bridge1**；
4. **应用** 配置；

*![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-12.webp)*

1. 点击 **Bridge** 子菜单；
2. 点击“+”添加新成员；
3. 将接口成员添加为 **bonding1**，网桥成员添加为 **bridge1**；
4. **应用** 配置。

*![](https://manual.mikrotik.com/docs/wireless/w60g/img/fail-over-ptp-gui-example-13.webp)*

### 附加配置

接口从灰色状态启用后将变为活动状态。

完成上述所有步骤后，链路应建立成功。建议在两台设备上设置管理员密码。