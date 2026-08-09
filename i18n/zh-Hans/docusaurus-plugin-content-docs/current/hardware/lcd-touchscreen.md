# LCD 触摸屏

> 本文档介绍了 MikroTik RouterOS 上的 LCD 触摸屏功能，涵盖背光超时、配色方案和屏幕默认设置等配置选项。同时说明了校准流程、截图捕获、接口监控设置以及用于网络统计的基于页面的图形显示。

# LCD 触摸屏

## 概述

RouterBOARD 2011U 和 CCR 系列设备配备电阻式触摸屏，可快速访问设备统计信息和进行简单配置。触摸屏需要施加压力才能识别触摸；因此，轻扫、快速或短促的点击可能无法被识别（与手机上常见的电容式触摸屏不同）。如果您用手指操作屏幕有困难，也可以尝试使用触控笔或笔的末端。

## 配置

**子菜单：** `/lcd`

该子菜单提供 LCD 触摸屏的配置选项。

| 属性 | 描述 |
| :-- | :-- |
| **backlight-timeout** (*时间间隔：5m..2h \| never*；默认值：**30m**) | 指定 LCD 触摸屏背光关闭前的无操作持续时间。设置为 "never" 可保持背光常亮。 |
| **color-scheme** (*dark \| light*；默认值：取决于 RouterBoard 型号) | 设置 LCD 显示器的配色方案，可选择深色或浅色背景。 |
| **default-screen** (*informative-slideshow\|interface\|log\|main-menu\|stat-slideshow\|stats\|stats-all*；默认值：**main-menu**) | 定义路由器启动后 LCD 上显示的默认屏幕。 |
| **enabled** (*yes \| no*；默认值：**yes**) | 启用或禁用 LCD 触摸屏。禁用后，触摸屏停止工作，统计信息收集将重置，LCD 程序将关闭。 |
| **read-only-mode** (*yes \| no*；默认值：**yes**) | 启用或禁用只读模式。启用后，允许更改配置的菜单将从 LCD 界面中隐藏。 |
| **time-interval** (*min \| hour \| daily \| weekly*；默认值：**min**) | 设置 Stats 屏幕中显示的接口统计信息的时间间隔。 |
| **touch-screen** (*enabled \| disabled*；默认值：**enabled**) | 启用或禁用触摸屏输入功能。 |

### 可用功能

LCD 触摸屏支持以下功能：

- **backlight** - 打开或关闭 LCD 背光。LCD 程序继续运行。
- **recalibrate** - 启动 LCD 触摸屏校准过程。
- **show** - 指定 LCD 上显示的屏幕。
- **take-screenshot** - 创建当前 LCD 屏幕的截图。

### LCD 触摸屏校准

LCD 触摸屏在首次使用前需要进行校准。校准成功后，校准数据将存储在路由器上。如果不存在校准数据，校准过程将自动启动。

在校准或重新校准期间，您必须触摸屏幕上显示的四个点。其中三个点用于计算校准变量，而第四个点用于验证校准是否成功。如果校准失败，校准变量将不会被保存。触摸第四个点后，将显示校准结果消息。

### 拍摄 LCD 截图

take-screenshot 功能将当前 LCD 屏幕捕获为 BMP 图像，并使用指定的文件名保存到文件列表中。没有文件名的截图不会被保存。如果指定名称的文件已存在，它将被覆盖。

示例：

```ros
[admin@MikroTik] /lcd/take-screenshot file-name=screen-1
Screenshot taken
[admin@MikroTik] >
```

## LCD 接口

**子菜单：** `/lcd/interface`

Interfaces 子菜单配置各个接口统计信息在 Stat Slideshow 中的显示方式。最多可以将 10 个额外的（非物理）接口添加到 LCD 以进行监控。

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*yes | no*；默认值：**no**) | 控制接口是否出现在 Stat Slideshow 轮播中 |
| **max-speed** (*integer | auto*；默认值：) | 设置用于计算 All Interface 图形和 Interface 屏幕中带宽使用量的最大接口速度。"auto" 值只能分配给物理接口。 |
| **timeout** (*时间间隔：1s..1m*；默认值：**10s**) | 指定幻灯片放映期间每个接口幻灯片的显示时长 |

- **display** - 在 Stats 屏幕中显示接口。

### 所有接口图形屏幕

**子菜单：** `/lcd/interface/pages`

Page 是一个可以包含最多 12 个接口条形图的屏幕。该子菜单允许配置页面中显示哪些接口。最多可以向 All Interface Graph Screen 添加 5 个页面，每个页面最多 12 个接口。要将接口添加到页面，必须首先在 `/lcd/interface` 子菜单下添加该接口。

| 属性 | 描述 |
| :-- | :-- |
| **interfaces** (接口名称；默认值：) | 屏幕上显示的接口。必须至少包含 1 个接口。 |

## LCD 信息屏幕

**子菜单：** `/lcd/screen`

Screens 菜单允许您配置 Informative Slideshow 中每个幻灯片的显示时间。

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*yes | no*；默认值：**no**) | 定义项目在 Informative Slideshow 中是被忽略还是使用 |
| **timeout** (*时间间隔：1s..1m*；默认值：**10s**) | 每个信息幻灯片的显示时长 |

## LCD PIN 码

**子菜单：** `/lcd/pin`

![](https://manual.mikrotik.com/docs/hardware/img/lcd-touchscreen-01.webp)

PIN 码保护 LCD 屏幕上的敏感菜单。当只读模式被禁用且您尝试添加 IP 地址、重置或重启路由器时，将要求输入 PIN 码。默认 PIN 码为 **1234**。

| 属性 | 描述 |
| :-- | :-- |
| **pin-number** (*数字*；默认值：**1234**) | PIN 保护代码 |
| **hide-pin-number** (*yes | no*；默认值：**no**) | 是否在 LCD 屏幕上显示输入的数字或用星号隐藏 |

## LCD 屏幕/模式

自 v6.0 起，LCD 具有菜单结构。菜单屏幕由用于导航菜单的按钮组成。如果内容超出实际显示范围，屏幕右侧将显示滚动条。如果有更多选项可用，可以向上或向下拖动屏幕以访问。每个菜单屏幕顶部都有一个 "Back" 按钮，可跳转到上一个屏幕。

### 启动

![](https://manual.mikrotik.com/docs/hardware/img/lcd-touchscreen-02.webp)

如果路由器具有默认配置 - 用户名为 "admin" 且无密码，则 LCD 上会出现警告。此屏幕显示分配给接口的 IP 地址，可用于连接路由器。否则，启动后将显示主菜单屏幕。

### 接口

Interfaces 菜单显示所有以太网和无线接口。带宽使用情况显示方式类似于 All interface graph 屏幕。在 Interfaces 屏幕中，您可以选择特定接口进行查看。以下选项可用：

- Info（仅限物理接口）- 显示接口信息的菜单。
- Registration Table（仅限无线）- 显示无线接口的所有已注册客户端及其各自信号强度的菜单。
- Addresses - 列出分配给接口的所有地址的菜单。
- Stats - 允许您跳转到 "Stats" 屏幕中所选接口的菜单。您可以直接选择显示带宽或数据包。

|  |  |  |  |
| :-- | :-- | :-- | :-- |
| ![](https://manual.mikrotik.com/docs/hardware/img/lcd-info.jpg)  Info  | ![](https://manual.mikrotik.com/docs/hardware/img/lcd-registration-table.jpg)  Registration Table  | ![](https://manual.mikrotik.com/docs/hardware/img/lcd-addresses.jpg)  Addresses  | ![](https://manual.mikrotik.com/docs/hardware/img/lcd-stats.jpg)  Stats 选择  |

### 统计信息

Stats 屏幕显示 RX 和 TX 的单个接口图形。数值从右到左更新（从最新到最旧）。显示的信息：RX/TX 速率和数据包。

![](https://manual.mikrotik.com/docs/hardware/img/lcd-touchscreen-03.webp)

接口名称显示在右上角；如果太长，将被截断（最后几个字符被切掉）。右上角显示数值的时间间隔。可用的时间值如下：

- **Min (分钟)** - 显示最后一分钟的数值。单位 = 秒。垂直线分隔前 30 秒。总数值：30 + 24。
- **Hour (小时)** - 显示最后几小时的数值。单位 = 5 分钟。垂直线分隔 1 小时。总数值：12 + 12 + 3。
- **Daily (每日)** - 显示最后几天的数值。单位 = 小时。垂直线分隔 1 天。总数值：12 + 12 + 3。
- **Weekly (每周)** - 显示最后几周的数值。单位 = 天。垂直线分隔 1 周。总数值：7 + 7 + 4。

## 手势

- 点击 - 用手指轻触触摸屏而不大幅移动。
  - 如果点击落在屏幕右上角（屏幕高度 1/4 的方形区域），信息时间间隔将更改：Min -> Hour -> Daily -> Weekly -> Min...
  - 否则，点击将循环切换图形信息：rate -> packets -> rate...
- 滑动/拖动 - 按住手指的同时，向任意方向移动。拖动期间更改应高亮显示。
  - 向上 - 转到主菜单。
  - 向下 - 选择 All Interface graph 屏幕。
  - 向左 - 下一个接口。
  - 向右 - 上一个接口。

### 所有接口图形屏幕

![](https://manual.mikrotik.com/docs/hardware/img/lcd-touchscreen-04.webp)

All interface graph 屏幕显示所有接口的 RX/TX 带宽使用情况。最大值计算方式如下 - 对于以太网接口，为协商速率或设定速度。对于无线接口，则根据使用的频段、信道宽度和链数使用理论值计算。此屏幕的目标是查看单个接口的数值之间的相互关系。

## 手势

- 滑动/拖动：
  - 向上 - 返回（到 Stats 屏幕）。
  - 向左 - 下一页。
  - 向右 - 上一页。

### 统计幻灯片放映

Stat Slideshow 屏幕类似于 "Stats" 屏幕，但接口在超时后切换。幻灯片放映的设置存储在 RouterOS 子菜单 `/lcd/interface` 中。

### 信息幻灯片放映

`/lcd/screen` 子菜单的 Informative Slideshow 屏幕循环显示包含各种系统信息的屏幕：

- 总流量。
- 总数据包。
- 资源。
- 系统。
- 健康状态。
- 日期和时间。

|  |  |  |
| :-- | :-- | :-- |
| ![](https://manual.mikrotik.com/docs/hardware/img/lcd-system.jpg)  System  | ![](https://manual.mikrotik.com/docs/hardware/img/lcd-resources.jpg)  Resources  | ![](https://manual.mikrotik.com/docs/hardware/img/lcd-health.jpg)  Health  |

### 日志

![](https://manual.mikrotik.com/docs/hardware/img/lcd-touchscreen-05.webp)
Log 屏幕显示最后 5 条日志条目，其中 log action=echo。

### 重启和重置配置

这些屏幕仅在只读模式被禁用时可用。要访问任何屏幕，必须输入 PIN 码。如果 PIN 认证成功，用户必须按 "Yes" 按钮确认所需操作，或按 "No" 取消。