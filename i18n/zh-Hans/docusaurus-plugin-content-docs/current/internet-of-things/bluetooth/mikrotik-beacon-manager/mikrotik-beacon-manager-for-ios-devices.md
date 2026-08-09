# 适用于 iOS 设备的 MikroTik Beacon Manager

> MikroTik Beacon Manager 应用专为蓝牙标签（TG-BT5-XX）的配置而设计。由于标签是基于蓝牙的设备，因此在继续配置之前，您必须在手机上启用蓝牙。

##

## 概述

MikroTik Beacon Manager 应用专为蓝牙标签（TG-BT5-XX）的配置而设计。由于标签是基于蓝牙的设备，因此在继续配置之前，您必须在手机上启用蓝牙。

对于 iOS 设备，您可以通过以下[链接](https://apps.apple.com/id/app/mikrotik-beacon-manager/id1561796698)找到该应用。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/app_qr_ios.png)

## 我的设备

启动应用后看到的第一个屏幕是“我的设备”屏幕，其中显示所有附近的蓝牙标签。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_14-3-16.webp)

如果列表为空，则表示附近所有标签均处于出厂休眠模式。一旦标签进入广播或配置模式，它就会出现在列表中。要将标签从出厂休眠模式唤醒，请将磁铁放在标签上（激活干簧管）3-10 秒。

屏幕底部有 2 个选项——停留在“我的设备”选项卡，或在“设置”选项卡下修改应用设置。

## 设置

如果您选择修改应用的“设置”，您将看到以下屏幕：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_14-12-45.webp)

“设置”选项卡分为“发现”、“其他”和“关于”三个部分。

在“发现”部分，您可以启用“仅显示 MikroTik 数据包”复选框，这将确保“我的设备”列表中仅显示 MikroTik 设备。禁用时，所有蓝牙设备都会显示在“我的设备”列表中。

在“其他”部分，可以更改应用的语言（英语、俄语、拉脱维亚语和葡萄牙语）以及外观（系统、深色和浅色）。

“关于”部分仅显示应用的版本。

## 标签管理

当标签出现在列表中时，您可以点击它，进入标签的单独概览页面：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-6-9.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-6-25.webp)

您首先应该注意到的是信号强度指示（标签的 RSSI 信号——标签距离的远近）。当所有圆圈都被填满/完成时，表示信号强度约为 -60 RSSI。当只有 2 个圆圈被填满时，表示信号强度约为 -70 RSSI。当只有一个圆圈被填满时，表示信号强度为 -80 RSSI。当没有圆圈被填满时，表示信号强度为 -90 RSSI 或更低。

在信号强度指示下方，您可以查看标签的电池电量、温度和加速度。

:::info
TG-BT5-IN 型号没有温度传感器！
:::

在“传感器触发”字段中，您可以查看标签报告的触发事件（设备是否被倾斜、抛掷或跌落）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-16-10.webp)

在“显示名称”字段中，您可以更改标签的名称。

在“设备图标”字段中，您可以为标签分配一个图标。

如果您选择“移除设备”按钮 → 您可以取消配对设备并将其从设备列表中移除。

## 标签配置

为了访问标签的配置菜单，您需要将标签置于“配置模式”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-23-12.webp)

要进入设备配置，请将磁铁放在干簧管上，直到其 LED 停止闪烁。

成功进入配置模式后，“设置/齿轮”图标（右上角）将变为橙色，并且您应该在屏幕底部看到一条消息“配置模式已启用”，如下方截图所示：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-24-28.webp)

点击屏幕右上角的橙色“设置/齿轮”图标，您将进入标签的配置页面：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-33-20.webp)

此页面将要求您同步标签的时间和日期。

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-37-31.webp)

应用将在“设备状态”选项卡下显示标签的常规信息（如上图所示）。

:::info
TG-BT5-IN 型号没有温度传感器！
:::

设置可以在“配置”选项卡中进行修改：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-16-40.webp)

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-16-57.webp)

### “加速度计”设置

此部分允许您修改“功耗模式”、“测量”、“唤醒阈值和持续时间”、“自由落体阈值和持续时间”、“角度阈值”和“低噪声滤波器”设置。

#### 功耗模式

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-29_15-56-11.webp)

此菜单允许您在 2 种模式之间选择：“低功耗”和“高功耗”。在“低功耗”模式下，您将获得较低的精度，但功耗也较低。在“高功耗”模式下，您将获得较高的精度，但功耗也较高。

“比例因子”是一个测量范围（比例因子越低，精度越高，但请注意，较大的加速度峰值无法被测量）。

#### 测量

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-30_9-31-0.webp)

“数据速率”设置表示 1 秒窗口内的加速度测量次数（测量频率）。每秒发送的数据包越少 → 功耗越低。

“带宽滤波器”是数字滤波截止频率（高通滤波器带宽）。

如果带宽 = “x” Hz，则标签将滤除频率低于每秒 “x” 次的加速度变化。

例如，如果设备平放在桌子上，加速度将显示 0g（而不是 1g），即使存在地球重力 → （因为地球重力是恒定的——其变化频率为 0 Hz，小于 “x” Hz）它会被滤除。

#### 唤醒阈值和持续时间

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-33-8.webp)

“唤醒阈值”定义了一个唤醒区域/加速度范围。“唤醒持续时间”定义了加速度超过配置的唤醒阈值的时间。当任何轴（X、Y 或 Z）上的加速度超过阈值并持续配置的唤醒持续时间时，将生成唤醒事件（触发唤醒条件）。为了更好地理解“任何轴（X、Y 或 Z）上的加速度”的含义，想象一个三维笛卡尔坐标系，在原点（公共点）处放置标签的加速度计或标签本身：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/intagaxis.png) ![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/outtagaxis.png)

例如，唤醒阈值设置为 1.0g（这意味着 -1.0g 到 +1.0g 之间的任何加速度都属于配置的阈值/加速度范围），唤醒持续时间设置为 0.12 秒。因此，一旦设备被推/抛向任何轴（设备开始向任何方向移动），加速度超过配置的阈值（加速度> +1.0g 或加速度&lt; -1.0g）且持续时间超过 0.12 秒 → 唤醒条件被触发。

#### 自由落体阈值和持续时间

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-39-14.webp)

“自由落体阈值”定义了一个自由落体区域/加速度范围。“自由落体持续时间”定义了加速度将保持在配置的自由落体阈值内的时间。当所有 3 个轴（X、Y 和 Z）上的加速度都在自由落体区域/阈值内并持续配置的自由落体持续时间时，将生成自由落体事件（触发自由落体条件）。为了更好地理解“所有轴（X、Y 和 Z）上的加速度”的含义，请查看上面“唤醒阈值和持续时间”部分中的设备图片。

例如，自由落体阈值设置为 156.25g（这意味着 -156.25g 到 +156.25g 之间的任何加速度都属于配置的阈值/加速度范围），自由落体持续时间设置为 0.2 秒。因此，一旦设备处于自由落体状态，所有轴上的加速度都在配置的阈值内（-156.25g&lt;加速度&lt;+156.25g）且持续时间超过 0.2 秒 → 自由落体条件被触发。

#### 角度阈值

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-19-46.webp)

可在 50°...80° 之间变化。这是倾斜功能的阈值。当触发设置为例如 60° 且设备倾斜到该角度时——倾斜动作被触发并发送广播数据包。

#### 低噪声滤波器

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-30_11-55-41.webp)

启用或禁用低噪声滤波器的选项。低噪声滤波器用于降低测量中的噪声密度。启用此功能将略微增加功耗。

### “传输”设置

此部分允许您配置标签的“发射功率电平”。

#### 发射功率电平

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-30_11-56-42.webp)

以分贝毫瓦为单位的发射功率电平。可在 -28dBm...6dBm 之间变化。发射功率仅用于增加/减少标签的发射功率。

### “广播”设置

在广播模式下，标签通过蓝牙广播数据包广播关于自身的信息。信息取决于广播数据包类型（类型可以在设置中更改）。

目前，所有支持的类型如下：

MikroTik、[Eddystone-TLM](https://play.google.com/store/apps/details?id=com.mikrotik.android.bt5&hl=en_US&gl=US&pli=1)、[Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-uid) 和 [iBeacon](https://developer.apple.com/ibeacon/)。

Eddystone-TLM、Eddystone-UID 和 iBeacon 格式可以选择配置 4 个参数。MikroTik 格式可以选择配置一个额外的参数，称为“加密数据包”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2021-11-30_12-4-16.webp)

一旦启用“启用广播”复选框，您将能够配置以下参数：

| 属性 | 描述 |
| --- | --- |
| 广播间隔（20ms...10s 或禁用） | 标签广播一个广播数据包的间隔时间（以毫秒为单位） |
| 自由落体检测（开/关） | 当加速度计（标签）检测到自由落体触发时是否发送广播数据包 |
| 倾斜检测（开/关） | 当加速度计（标签）检测到倾斜触发时是否发送广播 |
| 冲击检测（开/关） | 当加速度计（标签）检测到冲击/唤醒触发时是否发送广播 |
| 加密数据包（开/关）——仅适用于 MikroTik 格式 | 是否在十六进制有效载荷中加密加速度、温度、运行时间、触发动作和电池百分比参数 |

- 当您仅配置了广播间隔而未启用任何触发时——广播数据包将根据设置的间隔时间（每 **x** 秒）进行广播。
- 当倾斜触发已启用且设备被倾斜时——广播数据包将立即发送。
- 当自由落体触发已启用且检测到自由落体时，一旦标签检测到自由落体条件——数据包即被发送。
- 当冲击触发已启用且设备被推/移动时——广播数据包将立即发送。
- 当加密参数已启用时，十六进制有效载荷数据（如加速度、温度、运行时间、触发动作和电池百分比）将使用私钥进行加密。此密钥仅由标签的所有者知晓（购买时获得）。

### “系统”设置

系统部分允许您重置标签的设置并将标签置于出厂休眠模式。

#### 重置设备

此选项将标签置于广播模式（以关闭设置）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-43-25.webp)

#### 出厂休眠

此选项将设备设置为出厂休眠模式：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/img/image2022-2-2_9-44-42.webp)