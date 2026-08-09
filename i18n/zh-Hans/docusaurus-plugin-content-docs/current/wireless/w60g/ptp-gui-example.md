# PtP GUI 示例

> 本指南演示了如何使用 WinBox 在两台 MikroTik W60G 设备之间配置透明无线桥接，涵盖接口设置、桥接创建、桥接与站点角色的无线模式配置，以及额外的安全建议。

# PtP GUI 示例

### 概述

本示例展示了如何在图形界面中，从一台 W60G 设备到另一台设备配置透明无线桥接。

示例从空配置状态开始，使用 [[WinBox](https://mikrotik.com/download)] 工具进行操作。

### 连接设备

配置重置后，仅支持 MAC-telnet 连接。在 WinBox 主界面中，点击“邻居”按钮，选择设备的 MAC 地址，然后点击“连接”：

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-01.webp)

### 配置桥接

添加新的桥接，并为其分配桥接成员。这将允许流量无需路由即可从以太网接口传递到 W60G 接口：

1. 打开“桥接”子菜单；
2. 点击“+”添加新的桥接；
3. 应用更改。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-02.webp)

将接口成员（ether1 和 wlan60-1）添加到新创建的桥接中：

1. 点击“端口”子菜单；
2. 使用“+”添加新成员；
3. 选择正确的接口；
4. 应用设置。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-03.webp)

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-04.webp)

### 设置无线连接

之前所有步骤对**桥接**和**站点**设备均相同。配置无线接口时需使用不同的模式。

按以下步骤配置**桥接**设备：

1. 打开“接口”菜单；
2. 双击 wlan60-1 接口；
3. 点击“无线”子菜单，将模式设置为 **bridge**；
4. 设置 SSID、密码和区域；
5. 在“将站点放入桥接”下选择之前创建的桥接；
6. 应用更改；
7. 点击“启用”开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-05.webp)

按以下步骤配置**站点**设备：

1. 打开“接口”菜单；
2. 双击 wlan60-1 接口；
3. 点击“无线”子菜单，将模式设置为 **station bridge**；
4. 设置 SSID 和密码；
5. 应用更改；
6. 点击“启用”开始传输。

![](https://manual.mikrotik.com/docs/wireless/w60g/img/ptp-gui-example-06.webp)

### 额外配置

接口从灰色状态启用后，将变为活动状态。

完成上述所有步骤后，链路应建立。建议在两台设备上设置管理员密码。

要创建点对多点设置：在桥接设备上必须设置 ap-bridge，站点设备上设置 station-bridge。