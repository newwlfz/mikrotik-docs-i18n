# UPS

> UPS 监控功能适用于支持串行/USB 连接的 APC UPS 设备，能够实现优雅的断电处理，包括休眠和安全重启功能。该功能可监控电池状态、运行测试、记录电源变化，并需通过 ups.npk 软件包手动安装。

# UPS

### 概述

**子菜单:** `/system/ups`
**标准:**  `APC Smart Protocol`

UPS 监控功能适用于支持通过串行 RS232 或 USB 连接进行“智能”信号通信的 APC UPS 设备。UPS 监控服务不包含在默认软件包集中，因此需要通过 ups.npk 软件包手动下载并安装。该功能使网络管理员能够监控 UPS，并设置路由器以“优雅”方式处理任何断电情况，避免对路由器造成损坏或数据损坏。此功能的基本目的是确保路由器在长时间断电后能够重新上线。为此，路由器将监控 UPS，并在市电中断且 UPS 电池剩余电量低于 10% 时进入休眠模式。随后，路由器将继续监控 UPS（处于休眠模式时），并在市电恢复后自动重启。如果 UPS 电池耗尽且路由器完全断电，路由器将在市电恢复后重新启动并完全运行。

MikroTik RouterOS 上的 UPS 监控功能支持：

- 电源和电池故障时的休眠和安全重启
- UPS 电池测试和运行时间校准测试
- 监控 UPS 支持的所有“智能”模式状态信息
- 记录电源变化

### 连接 UPS 设备

串行 APC UPS（BackUPS Pro 或 SmartUPS）需要专用的串行电缆（除非使用 USB 连接）。如果 UPS 未附带电缆，可以向 APC 订购或自行制作。请参考以下接线图：

| 路由器端 (DB9f) | 信号 | 方向 | UPS 端 (DB9m) |
| --: | :-- | :-- | --: |
| 2 | 接收 | 输入 | 2 |
| 3 | 发送 | 输出 | 1 |
| 5 | 接地 |  | 4 |
| 7 | CTS | 输入 | 6 |

如果使用 RouterBOARD 设备，请确保将“RouterBOOT 设置键”设置为 *Delete* 键，而不是默认的 *任意键*。这是为了避免在 RouterBOARD 启动期间，UPS 设备向串行端口发送数据时意外打开设置菜单。可以在启动时的 RouterBOOT 选项中或通过 Winbox 中的 RouterBoard 设置进行配置：

```
选择启动时进入设置的按键：
 * 1 - 任意键
   2 - 仅 <Delete> 键
您的选择：

```

### 常规属性

| 属性 | 描述 |
| :-- | :-- |
| **alarm-setting** (*delayed \| immediate \| low-battery \| none*; 默认值：**immediate**) | UPS 声音报警设置：delayed - 报警延迟到电池供电事件发生时immediate - 电池供电事件发生后立即报警low-battery - 仅在电池电量低时报警none - 不报警 |
| **check-capabilities** (*yes \| no*; 默认值：**yes**) | 是否在读取信息前检查 UPS 的能力。禁用此选项可以修复某些 UPS 型号的兼容性问题。（适用于 RouterOS 6 版本，自 v6.17 起实现） |
| **min-runtime** (*time*; 默认值：**never**) | 最小剩余运行时间。市电故障后，路由器将监控剩余运行时间值。当该值达到 min-runtime 值时，路由器将进入休眠模式。  never - 当“电池电量低”信号发出（表示电池电量低于 10%）时，路由器将进入休眠模式0s - 只要电池提供足够的电压，路由器将继续工作 |
| **offline-time** (*time*; 默认值：**0s**) | 电池供电工作时间。路由器等待该时间后进入休眠模式，直到 UPS 报告市电恢复。  0s - 路由器将根据 min-runtime 设置进入休眠模式。在这种情况下，路由器将等待直到 UPS 报告电池电量低于 10% |
| **port** (*string*; 默认值：) | 路由器的通信端口。 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **load** (*percent*) | UPS 的输出负载，以额定功率（瓦特）的百分比表示。此测量的典型精度为最大值的 ±3%（最大为 105%） |
| **manufacture-date** (*string*) | UPS 的制造日期，格式为“mm/dd/yy”（月/日/年）。 |
| **model** (*string*) | 少于 32 个 ASCII 字符的字符串，包含 UPS 型号名称（UPS 正面的文字） |
| **nominal-battery-voltage** (*integer*) | UPS 的额定电池电压（这不是 UPS 的实际电池电压） |
| **offline-after** (*time*) | 路由器何时离线 |
| **serial** (*string*) | 至少 8 个字符的字符串，直接表示 UPS 出厂时设置的序列号。较新的 SmartUPS 型号具有 12 个字符的序列号 |
| **version** (*string*) | UPS 版本由三个字段组成：SKU 编号、固件修订版本、国家代码。国家代码可以是以下之一：I - 220/230/240 VacD - 115/120 VacA - 100 VacM - 208 VacJ - 200 Vac |

:::info
**注意：** 要启用 UPS 监控，串行端口必须可用。
:::

#### 示例

为 serial1 端口启用 UPS 监控：

```
[admin@MikroTik] /system/ups> add port=serial1 disabled=no
[admin@MikroTik] /system/ups> print
Flags: X - disabled, I - invalid
 0    name="ups" port=serial1 offline-time=5m min-runtime=5m
      alarm-setting=immediate model="SMART-UPS 1000" version="60.11.I"
      serial="QS0030311640" manufacture-date="07/18/00"
      nominal-battery-voltage=24V
[admin@MikroTik] /system/ups>

```

### 运行时间校准

**命令：**  `/system/ups/rtc/<id>`

rtc 命令使 UPS 开始运行时间校准，直到电池容量低于满容量的 25%。此命令校准返回的运行时间值。

:::info
**注意：** 测试仅在电池容量为 100% 时开始。
:::

### 监控

**命令：**  `/system/ups/monitor <id>`

| 属性 | 描述 |
| :-- | :-- |
| **battery-charge** () | UPS 的剩余电池容量，以充满电状态的百分比表示 |
| **battery-voltage** () | UPS 当前的电池电压。此测量的典型精度为最大值的 ±5%（取决于 UPS 的额定电池电压） |
| **frequency** () | 在线运行时，UPS 的内部工作频率与线路同步，偏差在标称 50 或 60 Hz 的 3 Hz 范围内。此测量的典型精度为满量程值 63 Hz 的 ±1% |
| **line-voltage** () | 在线市电电压 |
| **load** () | UPS 的输出负载，以额定功率（瓦特）的百分比表示。此测量的典型精度为最大值的 ±3%（最大为 105%） |
| **low-battery** (*yes \| no*) | 仅在 UPS 报告此状态时显示 |
| **on-battery** (*yes \| no*) | UPS 电池是否正在供电 |
| **on-line** (*yes \| no*) | 是否由外部市电（电力公司）供电 |
| **output-voltage** () | UPS 的输出电压 |
| **overloaded-output** (*yes \| no*) | 仅在 UPS 报告此状态时显示 |
| **replace-battery** (*yes \| no*) | 仅在 UPS 报告此状态时显示 |
| **runtime-calibration-running** (*yes \| no*) | 仅在 UPS 报告此状态时显示 |
| **runtime-left** (*time*) | UPS 的估计剩余运行时间（分钟）。您可以在 UPS 处于在线、旁路或电池供电模式下查询。UPS 的剩余运行时间回复基于可用电池容量和输出负载 |
| **smart-boost-mode** (*yes \| no*) | 仅在 UPS 报告此状态时显示 |
| **smart-ssdd-mode** () | 仅在 UPS 报告此状态时显示 |
| **transfer-cause** (*string*) | 最近一次切换到电池供电的原因（仅在设备处于电池供电时显示） |

#### 示例

市电供电时：

```
[admin@MikroTik] /system/ups> monitor 0
          on-line: yes
       on-battery: no
      RTC-running: no
     runtime-left: 20m
   battery-charge: 100%
  battery-voltage: 27V
     line-voltage: 226V
   output-voltage: 226V
             load: 45%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no

[admin@MikroTik] /system/ups>

```

电池供电时：

```
[admin@MikroTik] /system/ups> monitor 0
          on-line: no
       on-battery: yes
   transfer-cause: "Line voltage notch or spike"
      RTC-running: no
     runtime-left: 19m
    offline-after: 4m46s
   battery-charge: 94%
  battery-voltage: 24V
     line-voltage: 0V
   output-voltage: 228V
             load: 42%
      temperature: 39C
        frequency: 50Hz
  replace-battery: no
      smart-boost: no
       smart-trim: no
         overload: no
      low-battery: no

      [admin@MikroTik] /system/ups>

```