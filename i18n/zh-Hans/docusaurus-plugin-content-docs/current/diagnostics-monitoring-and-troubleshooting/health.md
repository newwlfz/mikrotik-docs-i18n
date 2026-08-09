# 健康状态

> 本页介绍 MikroTik RouterOS 硬件健康监控功能，详细说明受支持设备的温度、电压、风扇转速及 CPU 状态等指标。内容包括 CLI 示例、设备限制警告，以及基于 PoE-out 负载或温度阈值的风扇控制参数。

# 健康状态

支持监控功能的硬件将显示不同的硬件状态信息，如温度、电压、电流、风扇转速等。

以 CCR1072-1G-8S+ 设备为例：

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
 #  NAME                VALUE  TYPE
 0  power-consumption   50.8   W   
 1  cpu-temperature     43     C   
 2  fan1-speed          5654   RPM 
 3  fan2-speed          5825   RPM 
 4  fan3-speed          5800   RPM 
 5  fan4-speed          5750   RPM 
 6  board-temperature1  29     C   
 7  board-temperature2  28     C   
 8  psu1-voltage        0      V   
 9  psu2-voltage        12.1   V   
10  psu1-current        0      A   
11  psu2-current        4.2    A
```

:::info
有关 RouterBOARD 产品的功能可用性，请查看 [mikrotik.com](https://mikrotik.com/products)
:::

在 [CCR2004-16G-2S+PC](https://mikrotik.com/product/ccr2004_16g_2s_pc) 设备上（通过控制台、WinBox 或 SNMP）进行密集型健康监控会导致显著的 CPU 负载。

### 电压

支持电压监控的路由器将显示供电电压值。在 CLI/WinBox 中显示单位为伏特。在脚本/API/SNMP 中，该值以 dV 为单位，或显示为 CLI/WinBox 中的数值。

**注意：** 具有 PEXT 和 PoE 电源输入的路由器使用 PEXT 进行校准，因此通过 PoE 显示的电压值可能因额外的以太网保护链路而低于输入电压。

```ros
[admin@MikroTik] > /system/health/print 
Columns: NAME, VALUE, TYPE
#  NAME         VALUE  TYPE
0  voltage      23.8   V   
1  temperature  39     C 
```

:::warning
如果旧版 CRS112、CRS210 和 CRS109 设备通过 PoE 供电，健康状态仅在电压不超过 26.7V 时显示正确值。若使用更高电压，健康状态将恒定显示 16V。
:::

### 温度

支持温度监控的路由器将显示温度读数。在 CLI/WinBox 中显示单位为摄氏度。通过脚本/API/SNMP 获取时，该值为 CLI/WinBox 显示值乘以 10。根据设备不同，存在多种温度传感器，可能包括：cpu-temperature、pcb-temperature、sfp-temperature。您可以在 [mikrotik.com](https://mikrotik.com/products) 的规格说明中找到设备测试环境温度范围。测试环境温度范围是指设备可物理放置的环境温度，**并非**系统健康监控器报告的温度！

### 风扇控制与行为

**子菜单：** `/system/health`

通过此菜单，用户可以在 TILE 架构 [设备](https://mikrotik.com/download) 上控制风扇行为。

:::info
自 6.45.5 版本起，风扇稳定性得到改进。
:::

影响风扇行为的有三个参数：PoE-out 功耗、SFP 温度和 CPU 温度。一旦任一参数超过最佳值，风扇即会启动。

#### PoE-out 功耗

如果设备具有 PoE-out 功能，风扇转速将按以下方式变化：

| PoE-out 负载 | 最大风扇转速的百分比 |
| :-- | :-- |
| 0%..24% | 风扇转速 0% |
| 25%..46% | 风扇转速 25% |
| 47%..70% | 风扇转速 50% |
| 71%..92% | 风扇转速 75% |
| 93%.. | 风扇转速 100% |

对于配备 **PWM** 风扇的设备，转速将在 9%..88% 范围内线性增减（注意：低于 100W 时风扇转速为 0）

#### 有限的手动风扇控制选项

:::info
自 RouterOS 7.9 版本起，为 CRS3xx、CRS5xx 和 CCR2xxx 设备添加了有限的手动风扇控制选项。

自 RouterOS 7.14 版本起，CCR1036-8G-2S+-r2、CCR1036-12G-4S-r2 和 CCR1016-12S-1S+-r2 设备支持有限的手动风扇控制。
:::

可通过系统健康状态的设置部分来调整风扇行为：

```
/system/health/settings/set 
```

可用属性如下所述：

| 属性 | 描述 |
| :-- | :-- |
| **fan-full-speed-temp** (*整数* *[-273..65];* 默认值：**65**) | 设置温度值，达到该值时风扇转速将提升至最大可能转速。读取 CPU、PHY、SWITCH 和 SFP 的温度，并根据温度最高的组件调整风扇转速。 |
| **fan-target-temp** (*整数* *[-273..65];* 默认值：**58**) | 设置最热组件的目标温度。基于此设置，调整风扇行为以将温度维持在目标范围内。 |
| **fan-min-speed-percent** (*整数* *[0..100];* 默认值：**取决于 FAN 控制器**) | 设置风扇转速的最小百分比，防止风扇转速低于此值。**\*注意：** 默认值可能因 FAN 控制器芯片和/或特定型号要求而异。自 RouterOS 7.14 版本起，默认值设置为 **12**，而所有先前版本的默认值为 **0**。 |
| **fan-control-interval** (*整数* *[5..30];* 默认值：**30**) | 设置实际温度数据读取间隔，以从 CPU、PHY、SWITCH 和 SFP 获取温度值。**\*注意：** 此设置直接影响 CPU 使用率。 |
| **cpu-overtemp-check** *(是 \| 否; 默认值：否)* | 启用/禁用 CPU 过温监控。*(适用于 ARM/ARM64 设备)* |
| **cpu-overtemp-threshold** *(整数 [0..105]; 默认值：105)* | 触发过温保护前的最高温度。 |
| **cpu-overtemp-startup-delay** *(时间; 默认值：1m)* | 启动后启用过温监控前的延迟时间。 |

#### 风扇控制简要说明

如果至少一个内部测量（CPU、SFP、Switch、Board 等）温度超过 **fan-target-temp**，风扇将开始旋转。温度越高，风扇转速越快。对于配备 PWM 风扇的设备，当内部测量温度超过 **fan-target-temp** 时，风扇将线性增加转速，以尽可能将温度维持在 **fan-target-temp**，并在温度达到或超过 **fan-full-speed-temp** 时达到最大转速。对于配备 DC 风扇的设备，当内部测量温度超过 **fan-target-temp** 时，风扇将开始旋转，但默认以较高的最小转速运行。如果 **fan-min-speed-percent** 设置为 **0%**，这可能导致设备冷却到风扇完全停止的程度；而使用默认值 **12%** 时，风扇永远不会完全停止，从而减少可能出现的噪音和开关峰值。随后温度可能缓慢上升至 **fan-target-temp**，风扇将再次启动。目前有一个例外：S+RJ10 模块在触发风扇前有 65°C 的温度阈值。由于该阈值较高，风扇将以更高的初始转速启动以冷却设备。上述所有功能均与 **fan-control-interval** 参数值直接相关，因为它决定了 FAN 控制器监控所有传感器数据并触发风扇控制变化的频率。

:::warning
PWM 和 DC 风扇对风扇控制的响应不同。PWM 风扇会线性增减转速，而 DC 风扇仅有少数几个可用的转速档位。
所有读数均为近似值，可能并非 100% 精确。其目的是告知用户可能/即将发生的故障。
:::