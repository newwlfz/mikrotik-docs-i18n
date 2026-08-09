# 适用于 Android 设备的 MikroTik Beacon Manager

> MikroTik Beacon Manager 应用专为蓝牙标签（TG-BT5-XX）的配置而设计。由于标签是基于蓝牙的设备，因此在继续配置之前，您必须在手机上启用蓝牙。

##

## 概述

MikroTik Beacon Manager 应用专为蓝牙标签（TG-BT5-XX）的配置而设计。由于标签是基于蓝牙的设备，因此在继续配置之前，您必须在手机上启用蓝牙。

对于 Android 设备，您可以通过以下[链接](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)找到该应用。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/app_qr.png)

## Beacon Manager 屏幕

启动应用后看到的第一个屏幕是“MikroTik Beacon Manager”屏幕，其中会显示所有附近的蓝牙标签。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-10_8-16-34.webp)

如果列表为空，则表示附近所有标签均处于出厂休眠模式。一旦标签进入广播或配置模式，它就会显示在列表中。要将标签从出厂休眠模式唤醒，请将磁铁放在标签上方（激活干簧管）3-10 秒。

:::info
如果您确定手机范围内有标签，但列表未捕获到任何标签 → 请尝试在手机的 GPS 设置中开启“位置=ON”。
:::
屏幕右上角有 3 个按钮：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-10_8-17-49.webp)

### 二维码读取器

“二维码读取器”按钮，允许您通过二维码添加标签（MAC 地址用作标签的 ID）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-13-39.webp)

#### NFC 支持

:::info
此部分仅适用于 TG-BT5-OUT 型号
:::

您还可以使用 NFC 查找标签（类似于二维码读取器功能）（MAC 地址用作标签的 ID）。

您只需在手机设置中启用 NFC 并打开 MikroTik Beacon Manager 应用即可。

当您看到初始屏幕（标签列表）时，将标签靠近手机的 NFC 天线，系统将为您提供打开设备设置的选项：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-6-34.webp)

如果您按下“YES”，您将被重定向到如下所示的页面。在菜单中，您可以选择从列表中删除设备，或通过“Configure”按钮进入配置模式。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-15-48.webp)

### 排序方式

“Order by”按钮，允许您更改设备列表的顺序，或通过勾选“Show only MikroTik beacons”复选框来仅显示 MikroTik 信标：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-17-41.webp)

### 设置与批量配置

“⋮”选项卡分为两个子选项卡——“Settings”和“Batch Configuration”。

#### 设置

此选项卡中的第一个选项是设置“Discovery refresh interval”，即扫描附近标签的时间间隔。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-18-17.webp)

第二个选项是启用或禁用“Save triggers”设置。启用后，应用会将检测到的触发器保存在数据库中。您可以在“Sensor Triggers”菜单中查看触发器（“Sensor Triggers”菜单在本指南的“**Tag Management**”部分中显示）。如果禁用此选项，则应用关闭后“Sensor Triggers”数据将立即被清除。

最后，“App version”字段显示当前应用的版本/构建号。

#### 批量配置

此选项允许您使用相同的设置对多个标签进行批量配置。

为此，您需要从其中一个标签导出配置文件。标签配置的导出和导入在本指南的“**Tag Configuration**”部分中显示。

保存配置文件后，只需按下“Batch Configuration”按钮，它将带您进入文件菜单，您需要在此选择文件。选择配置文件（您希望应用于多个设备的文件），应用将显示包含所有附近检测到的标签的屏幕：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-16-53.webp)

最后一步是将这些标签置于配置模式（将磁铁放在标签上方 5-10 秒）。设备进入配置模式后，您将看到“Uploading configuration”消息。当配置成功应用后，消息将变为“Configuration updated”。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-17-19.webp)

## 标签管理

当标签出现在列表中时，您可以点击其 MAC 地址，系统将显示以下选项：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-40-36.webp)

通过“SAVE”按钮“保存”标签，或通过“CONFIG ONLY”按钮立即进入标签的配置菜单。

首先，我们将更详细地解释“SAVE”选项。标签的配置菜单将在后面的“**Tag Configuration**”部分中说明。

当您点击之前保存的标签时，您将看到以下菜单：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-9_10-39-56.webp)

您首先应该注意到的是信号强度指示（标签的 RSSI 信号——标签的距离）。当所有圆圈均为绿色时，表示信号强度约为 -60 RSSI。当只有 2 个圆圈为绿色时，表示信号强度约为 -70 RSSI。当只有一个圆圈为绿色时，表示信号强度为 -80 RSSI。当没有圆圈为绿色时，表示信号强度为 -90 RSSI 或更低。

在信号强度指示器下方，您有 2 个选项——进入标签的配置菜单（“Configure”按钮）或删除设备（“Delete”按钮）。

在“Name/Display Name”字段中，您可以更改标签的名称：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-42-16.webp)

在“Sensors”字段中，您可以查看标签的电池电量或温度。

:::info
TG-BT5-IN 型号没有温度传感器
:::

在“Sensor Triggers”字段中，您可以查看标签报告的触发器：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-44-46.webp)

## 标签配置

要访问标签的配置菜单，您需要按下“CONFIG ONLY”按钮或“Configure”按钮，如下所示：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-45-49.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-46-7.webp)

紧接着，您需要将磁铁放在干簧管上 5-10 秒：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-47-1.webp)

经过短暂的启动时间后，设备应处于配置模式：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_10-33-30.webp)

应用将在“Status”选项卡中显示标签的常规信息（如上方截图所示）。

配置可以在“Settings”选项卡中进行修改：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_10-34-13.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_10-34-50.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_10-35-5.webp)

### 写保护

此菜单允许您使用 6 位符号长度的密码锁定标签的设置：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-2-12.webp)

一旦设置密码，就无法移除密码保护（您只能编辑它）。

下次尝试配置标签时，您将收到“write protected”通知，您可以选择保持在“READ-ONLY”模式（允许您浏览/读取设置，但限制进行配置更改）或通过输入已配置的密码来“UNLOCK”设置：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-1-51.webp)

### 信标设置

在广播模式下，标签会在蓝牙广播包中广播关于自身的信息。信息取决于广播包类型（类型可以在设置中更改）。

目前，所有支持的类型包括：

DeviceName、MikroTik、[Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)、[Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) 和 [iBeacon](https://developer.apple.com/ibeacon/)。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-16-54.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-17-4.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-17-16.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-9-8_12-17-23.webp)

| 属性 | 描述 |
| --- | --- |
| **广播间隔** (20ms...24h 或禁用) | 标签广播广播包的时间间隔（以毫秒为单位）。当仅配置了广播间隔而未启用任何触发器时 → 广播包将根据设定的间隔时间（每 **x** 秒）进行广播。 |
| **自由落体检测** (开/关) | 当标签检测到自由落体触发器时是否发送广播包。当启用自由落体触发器并检测到自由落体状态时 → 发送数据包。 |
| **倾斜检测** (开/关) | 当标签检测到倾斜触发器时是否发送广播。当启用倾斜触发器且设备发生倾斜时 → 立即广播广播包。 |
| **冲击检测** (开/关) | 当标签检测到冲击/唤醒触发器时是否发送广播。当启用冲击触发器且设备被推动/移动时 → 发送广播包。 |
| **加密** (开/关) - 仅适用于 MikroTik 格式 | 是否使用“AES”密钥加密广播的十六进制负载。当启用“Encrypt”参数时，十六进制负载数据（加速度、温度、运行时间、触发动作和电池百分比）将使用私钥进行加密。该密钥仅标签所有者知晓（购买时获得）。 |
| **命名空间** - 仅适用于 Eddystone-UID 格式 | 设置一个唯一的 10 字节长的信标命名空间 ID。 |
| **实例** - 仅适用于 Eddystone-UID 格式 | 设置一个唯一的 6 字节长的信标实例 ID。 |
| **UUID** - 仅适用于 iBeacon 格式 | 设置一个通用唯一标识符 (UUID)，格式如下：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx |
| **Major** - 仅适用于 iBeacon 格式 | 设置一个 16 位整数次要标识符，格式为十六进制或十进制数字（从 0 到 65 535）。 |
| **Minor** - 仅适用于 iBeacon 格式 | 设置一个 16 位整数次要标识符，格式为十六进制或十进制数字（从 0 到 65 535）。 |

### 广播属性

| 属性 | 描述 |
| --- | --- |
| **可连接广播** (开/关) | 启用可连接广播。 |
| **信道 37** (开/关) | 在特定信道上启用广播。 |
| **信道 38** (开/关) | 在特定信道上启用广播。 |
| **信道 39** (开/关) | 在特定信道上启用广播。 |

### 预估电池寿命

此部分显示预估电池寿命：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-52-0.webp)

预估电池寿命在很大程度上取决于发送的广播包数量（配置为发送的数量）。应用会计算每天预计广播的数据包数量、标签将活跃多长时间，以及平均每日功耗的估算值。

### 加速度计设置

加速度计可以完全关闭，也可以通过“Use Accelerometer”切换按钮重新开启。

此部分允许您更改下方截图中显示的参数：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_11-47-16.webp)

#### 模式与数据速率

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-53-8.webp)

此菜单允许您在 2 种模式之间选择：“Low power”和“High power”。在“Low power”模式下，精度较低，但功耗也较低。在“High power”模式下，精度较高，但功耗也较高。

“Data Rate”设置表示 1 秒窗口内的加速度测量次数（测量频率）。每秒发送的数据包越少 → 功耗越低。

#### 满量程

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2022-11-14_11-57-58.webp)

可在 (2g...16g) 之间变化。这是用于计算唤醒阈值的测量范围。满量程定义了加速度计能够测量的加速度范围（范围越大，测量加速度的精度越低）。

#### 带宽滤波器

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-53-53.webp)

是数字滤波截止频率（高通滤波器带宽）。

如果带宽 = “x” Hz，则标签将滤除频率低于每秒 “x” 次的加速度变化。

例如，如果设备平放在桌子上，加速度将显示 0g（而不是 1g），即使地球重力存在 → （因为地球重力是恒定的——其变化频率为 0 Hz，小于 “x” Hz）它会被滤除。

#### 唤醒阈值与持续时间

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-54-18.webp)

“Wakeup Threshold”定义了唤醒区域/加速度范围。“Wakeup Duration”定义了加速度超过配置的唤醒阈值的持续时间。当任一轴（X、Y 或 Z）上的加速度超过配置的唤醒持续时间内的阈值时，将生成唤醒事件（触发唤醒条件）。为了更好地理解“任一轴（X、Y 或 Z）上的加速度”的含义，想象一个 3-D 笛卡尔坐标系，在原点（公共点）处放置标签的加速度计或标签本身：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/intagaxis.png) ![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/outtagaxis.png)

例如，唤醒阈值设置为 1.0g（这意味着 -1.0g 到 +1.0g 之间的任何加速度都属于配置的阈值/加速度范围），唤醒持续时间设置为 0.12s。因此，一旦设备被推动/抛向任何轴（设备开始向任何方向移动），且加速度超过配置的阈值（加速度> +1.0g 或加速度&lt; -1.0g）持续超过 0.12s → 唤醒条件被触发。

#### 自由落体阈值与持续时间

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-54-38.webp)

“Free Fall Threshold”定义了自由落体区域/加速度范围。“Free Fall Duration”定义了加速度将保持在配置的自由落体阈值内的时间。当所有 3 个轴（X、Y 和 Z）上的加速度在配置的自由落体持续时间内处于自由落体区域/阈值内时，将生成自由落体事件（触发自由落体条件）。为了更好地理解“所有轴（X、Y 和 Z）上的加速度”的含义，请查看上方“Wakeup Threshold and Duration”部分中的设备照片。

例如，自由落体阈值设置为 156.25g（这意味着 -156.25g 到 +156.25g 之间的任何加速度都属于配置的阈值/加速度范围），自由落体持续时间设置为 0.2s。因此，一旦设备处于自由落体状态，且所有轴上的加速度在配置的阈值内（-156.25g&lt;加速度&lt;+156.25g）持续超过 0.2s → 自由落体条件被触发。

#### 角度阈值

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-55-18.webp)

可在 50°...80° 之间变化。这是倾斜功能的阈值。例如，当阈值设置为 60° 且设备倾斜该角度时 - 倾斜动作被触发并发送广播包。

#### 低噪声滤波器

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-57-32.webp)

启用或禁用低噪声滤波器的选项。低噪声滤波器用于降低测量中的噪声密度。启用此功能将略微增加功耗。

#### 温度偏移

:::info
TG-BT5-IN 型号没有温度传感器！
:::

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-57-5.webp)

可在 -10°C...+10°C 之间变化。应用于原始温度测量的偏移量，单位为百分之一摄氏度。

#### 发射功率

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_13-58-19.webp)

以分贝毫瓦为单位的发射功率电平。可在 -28dBm...6dBm 之间变化。Tx Power 仅用于增加/减少标签的发射功率。

### 数据日志

:::info
此部分仅适用于 TG-BT5-OUT 型号。
:::

此部分允许您配置/查看日志（仅可通过应用访问）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-0-8.webp)

#### 配置日志记录

在“Configure logging”菜单中，您可以设置日志记录选项：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-9-24.webp)

您可以选择设置“Periodic logging interval (s)”（或禁用它）。启用后，数据日志将每 “x” 秒自动保存一次：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-5-45.webp)

另一个选项是启用“Log Triggers”（周期性日志记录和触发器日志记录可以同时使用）。使用日志触发器时 - 每当检测到倾斜、自由落体和/或冲击动作时，将保存日志。

例如，当启用倾斜触发器且标签检测到该触发器时 - 将记录该消息。

您可以在“Field config”部分设置要记录的参数：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-9_15-5-2.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-9_15-5-25.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-9_15-5-53.webp)

您可以选择记录 3 个参数：1) 电池电量；2) 温度；3) 加速度。

如果您对某个参数不感兴趣，可以禁用它，也可以为其设置阈值。

如果您只对电池电量低于 40% 时的记录感兴趣，您可以设置最小=0% 到最大=40% 的阈值，这样，电池电量（电池电量百分比）将仅在其处于配置范围内时显示在日志中。其他 2 个参数适用相同的原则。

#### 数据日志

记录的日志消息将显示在“Data Logs”选项卡中：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-10-30.webp)

您可以通过“Export as .csv”按钮将日志导出为 .csv 文件：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-10-58.webp)

### 系统

在“System”选项卡中，您可以同步时间、查看系统日志、将标签置于出厂休眠模式以及升级固件：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-6-30_14-24-6.webp)

#### Unix 时间

使用此设置，您可以同步标签的当前时间和日期：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-13-23.webp)

#### 日志

查看系统日志的菜单：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-14-10.webp)

#### 出厂休眠

此选项可以为标签启动出厂休眠模式：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-14-52.webp)

#### 固件升级

此菜单允许您升级标签的固件版本：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-15-20.webp)

##### 自动升级

点击“Download and install”并等待设备重启。

##### 手动升级

要手动下载标签的固件文件，请导航至 https://download.mikrotik.com/firmware/bt-tag/latest。它将允许您下载“latest”文件，该文件可以在记事本或任何其他文本编辑器中打开。文件内容将指示最新的可用 TG-BT5-XX 版本：

```
2.3.1 1638358509
1326c554c18340a41e79fd88abbea193dc53b99931eddecd018e33cff577f6d3 bt-tag_HT_app_2.3.1-0rr.gbl
9dc21eb980e8bd36732ec4db8e4b03a8177885fccdbbd87122f7d9bf76410b8b bt-tag_HT_apploader_3.2.3-0rr.gbl
9e4f30d9006f24063ac96d0fb1181d135929d86d0e243d3b3985cc5e43d6b448 bt-tag_IN_app_2.3.1-0rr.gbl
e03fa2987b874463e9a5c686303f4d75fef0c0f8d89dde14f8c4b04be4838a93 bt-tag_IN_apploader_3.2.3-0rr.gbl
54e959dd9cc1da3a5408b5dc7c797c52ae1a1685122e14d966cbe433ec1d1b3c bt-tag_OUT_app_2.3.1-0rr.gbl
e0bc2e8a1a9de6a1974c201a48cfea2276465414e07efc07816400abca91aa14 bt-tag_OUT_apploader_3.2.3-0rr.gbl
5257a1b06cb8d57d06ae10ef2c87abf0df0a3ab8a9ac7f9229a9a421b8a0c0fc bt-tag_HT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_HT_apploader_3.2.3-000.gbl
0f6603d97df5fc4b3f260b410628b3c62fb2562f26e85e44b6cdfdf1b58d04f8 bt-tag_IN_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_IN_apploader_3.2.3-000.gbl
3235db7bb9a9cca0d5e59ae774c3cd004be4e58b44c1ae40e6e3bb84feb077a6 bt-tag_OUT_app_2.3.1-000.gbl
caf3e333721852077945c8a766db32ee5e478f1e7844dcb3e0e3d700dbab009f bt-tag_OUT_apploader_3.2.3-000.gbl
```

使用应用仔细核对当前标签的固件版本：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-1-31_14-6-50.webp)

例如，已知标签是 **TG-BT5-IN** 型号且当前版本为 **1.6.1-000**，我们可以得出结论，最新版本是“bt-tag_IN_app_2.3.1-000.gbl”。

请注意，对于大多数标签，固件版本将是 1.6.1-**0rr**（而不是 1.6.1-**000**）。您需要使用 x.x.x-**0rr** 文件。

要下载实际的固件文件，请将链接中的“latest”部分更改为“bt-tag_IN_app_2.3.1-000.gbl”。

因此，如果您的当前版本是，例如，“1.6.1-000”（TG-BT5-IN 标签），则可以使用以下链接下载固件：

https://download.mikrotik.com/firmware/bt-tag/bt-tag_IN_app_2.3.1-000.gbl

如果您的当前版本是，例如，“1.6.1-0rr”（TG-BT5-OUT 标签），则可以使用以下链接下载固件：

https://download.mikrotik.com/firmware/bt-tag/bt-tag_OUT_app_2.3.1-0rr.gbl

##### 升级设置

:::warning
**如果标签更新时遇到问题，标签停留在 OTA/更新模式 → 请尝试启用“Reliable write”！**

当标签“卡在”OTA/升级模式时，可能发生两种情况：
a) Beacon Manager 标签列表仍会显示该标签，但不会有任何指示表明该标签“可配置”。您仍然可以点击列表中的标签（即使没有“齿轮”图标），并在不激活磁簧开关的情况下浏览其设置；

b) 标签可能会从可管理标签列表中消失。在这种情况下，请尝试使用二维码读取器功能手动添加标签，并批准“configuration”。
:::

要进入附加的升级设置菜单，请点击“Upgrade settings”按钮：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-8-9_13-9-47.webp)

这将允许您更改“Reliable write”配置：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image-2023-8-9_13-11-7.webp)

启用后，该复选框允许您使蓝牙升级过程“更慢”但“更可靠”（其中手机和标签之间会进行额外的交换和验证步骤）。

### 导入/导出

在屏幕的右上角，您可以选择导入/导出当前设置：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-7-7_14-15-43.webp)

如果您按下导出按钮，应用将打开手机的文件菜单，您可以在其中命名配置文件并保存。

如果您按下导入按钮，应用将打开手机的文件菜单，您可以在其中选择配置文件并应用它。