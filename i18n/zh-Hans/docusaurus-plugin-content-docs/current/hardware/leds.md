# LED 指示灯

> RouterOS 允许在支持的设备上自定义 LED 指示灯行为，用于显示无线信号强度、接口流量活动及其他状态指示。用户可以为特定功能（如无线信号强度、以太网活动或调制解调器信号）配置单个 LED，但需注意硬件限制。

# LED 指示灯

## 概述

**子菜单：** `/system/leds`

RouterOS 允许用户按照自己的意愿配置每个 LED 指示灯的活动。可以配置 LED 显示无线信号强度、在接口流量活动时闪烁，以及许多其他选项。

例如，Groove 上的默认 LED 配置

```ros
[admin@MikroTik] /system/leds> print 
Flags: X - disabled 
# TYPE INTERFACE LEDS 
0 wireless-signal-strength led1 
led2 
led3 
led4 
led5 
1 interface-activity ether1 user-led 

```

:::warning
并非所有主板都具备支持此功能所需的硬件能力。

:::

:::warning
RB Groove 使用五个 LED 显示无线信号强度，一个 LED 用于以太网活动监控。

:::

## 属性说明

| 属性 | 说明 |
| :-- | :-- |
| **disabled** (*yes \| no*; 默认值：**no**) | 项目是否被禁用 |
| **interface** (*string*; 默认值：) | 用于 LED 状态的接口名称。仅当 **type** 为接口特定类型时适用。 |
| **modem-signal-treshold** (*integer [-113..-51]*; 默认值：) | 当类型为 **modem-signal** 时适用 |
| **leds** (*list of leds*; 默认值：) | 用于状态报告的 LED 名称列表。例如，无线信号强度需要多个 LED。 |
| **type** (*align-down \| align-left \| align-right \| align-up \| ap-cap \| fan-fault \| flash-access \| interface-activity \| interface-receive \| interface-speed \| interface-speed-1G \| interface-speed-25G \| interface-speed-100G \| interface-status \| interface-transmit \| modem-signal \| modem-technology \| off \| on \| poe-fault \| poe-out \| wireless-signal-strength \| wireless-status*; 默认值：) | 状态类型：align-down - 当 w60g 设备需要向下调整以获得最佳信号质量时点亮 LEDalign-left - 当 w60g 设备需要向左调整时点亮 LEDalign-right - 当 w60g 设备需要向右调整时点亮 LEDalign-up - 当 w60g 设备需要向上调整时点亮 LEDap-cap - 在 CAP 使用 CAPsMAN 初始化时闪烁，连接成功后常亮fan-fault - 当设备任一受控风扇停止工作时点亮 LEDflash-access - 在闪存访问时闪烁 LEDinterface-activity - 在接口（流量）活动时闪烁 LEDinterface-receive - 在接口接收流量时闪烁 LEDinterface-speed - 当接口工作在 10Gbit 速率时点亮 LEDinterface-speed-1G - 当接口工作在 1Gbit 速率时点亮 LEDinterface-speed-25G - 当接口工作在 25Gbit 速率时点亮 LEDinterface-speed-100G - 当接口工作在 100Gbit 速率时点亮 LEDinterface-status - 在接口状态变化时点亮 LEDinterface-transmit - 在接口发送流量时闪烁 LEDmodem-signal - 在 3G 调制解调器信号（USB 或 miniPCIe）时闪烁 LEDmodem-technology - 按照调制解调器技术代次顺序点亮 LED：GSM；3G；LTE；仅当 LTE 激活时单个 LED 点亮。off - 关闭 LEDon - 点亮 LEDpoe-fault - 当 PoE 输出预算接近最大支持限制时点亮 LEDpoe-out - 当接口 PoE 输出开启时点亮 LEDwireless-signal-strength - 点亮 LED 显示无线信号（需要多个 LED）wireless-status - 在无线状态变化时点亮 LED。 |

## LED 设置

全局设置存储在 LED 设置菜单中。

**子菜单：** `/system/leds/setting`

| 属性 | 说明 |
| :-- | :-- |
| **all-leds-off** (*after-1h \| after-1min \| immediate \| never*; 默认值：**never**) | 是否以及何时可以关闭路由器的所有 LED |

列出的设备支持关闭其 LED（LED 暗色模式）；然而，由于设备设计因素，某些 LED 仍然无法关闭。

### **室内设备**

| RouterBoard | LED 说明 |
| :-- | :-- |
| **CRS305-1G-4S+; CRS309-1G-8S+** | 关闭除以太网 LED 和电源 LED 外的所有 LED |
| **RB5009UG+S+IN; RB5009UPr+S+** | 关闭所有 LED |
| **L009UiGS-RM; L009UiGS-2HaxD-IN** | 关闭 PWR、USR 和 Ether1 LED |
| **L41G-2axD; L41G-2axD&FG621-EA (hAP ax lite 系列)** | 关闭除以太网 LED 外的所有 LED |
| **RB760iGS (hEX S)** | 关闭电源 LED 和 SFP LED |
| **E50UG** | 关闭除 Ethernet1 LED 外的所有 LED |
| **RB924i-2nD-BT5&BG77; RB924iR-2nD-BT5&BG77 (KNOT 系列)** | 关闭所有 LED |
| **RB951Ui-2HnD** | 关闭除电源 LED 外的所有 LED |
| **RB951Ui-2nD (hAP); RB952Ui-5ac2nD (hAP ac lite); RB952Ui-5ac2nD-TC (hAP ac lite TC)** | 关闭除电源 LED 外的所有 LED |
| **RB962UiGS-5HacT2HnT (hAP ac)** | 关闭除 Port5 PoE LED 外的所有 LED |
| **RBcAP2n; RBcAP2nD (cAP)** | 关闭所有 LED |
| **RBcAPGi-5acD2nD (cAP ac); RBcAPGi-5acD2nD-XL (cAP XL ac)** | 关闭所有 LED |
| **cAPGi-5HaxD2HaxD (cAP ax)** | 关闭除以太网 LED 外的所有 LED |
| **RBD25G/RB25GR-5HPacQD2HPnD (Audience)** | 关闭除以太网 LED 外的所有 LED |
| **RBD52G-5HacD2HnD-TC (hAP ac^2)** | 关闭所有 LED |
| **RBD53iG-5HacD2HnD (hAP ac^3)** | 关闭所有 LED |
| **RBD53G-5HacD2HnD-TC (Chateau 系列)** | 关闭所有 LED |
| **RBwsAP5Hac2nD (wsAP ac lite)** | 关闭所有 LED |
| **C52iG-5HaxD2HaxD-TC (hAP ax^2)** | 关闭除以太网 LED 外的所有 LED |
| **C53UiG+5HPaxD2HPaxD (hAP ax^3)** | 关闭除以太网 LED 外的所有 LED |
| **S53UG+5HaxD2HaxD-TC (Chateau ax 系列)** | 关闭除以太网 LED 外的所有 LED |

### **无线系统**

| RouterBoard | LED 说明 |
| :-- | :-- |
| **CME22-2n-BG77 (CME Gateway)** | 关闭所有 LED |
| **CubeG-5ac60ay (Cube 60Pro ac); CubeG-5ac60ay-SA (CubeSA 60Pro ac)** | 关闭所有 LED |
| **CubeG-5ac60ad (Cube 60G ac)** | 关闭所有 LED |
| **RB912R-2nD-LTm (ltAP mini / ltAP mini LTE kit)** | 关闭所有 LED |
| **RB912UAG-6HPnD (BaseBox 6)** | 关闭所有 LED |
| **RBD23UGS-5HPacD2HnD (NetMetal ac^2)** | 关闭所有 LED |
| **L11UG-5HaxD; L11UG-5HaxD-NB (NetBox 5 ax)** | 关闭所有 LED |
| **L22UGS-5HaxD2HaxD-15S (mANTBox ax 15s)** | 关闭所有 LED |
| **L23UGSR-5HaxD2HaxD; L23UGSR-5HaxD2HaxD-NM (NetMetal ax)** | 关闭所有 LED |
| **RBLDF-2nD (LDF 2); RBLDF-5nD (LDF 5); RBLHGR** | 关闭所有 LED |
| **RBLDFG-5acD (LDF 5 ac)** | 关闭除以太网 LED 外的所有 LED |
| **RBLHG2nD (LHG 2); RBLHG2nD-XL (LHG XL 2)** | 关闭所有 LED |
| **RBLHG5nD (LHG 5); RBLHG5HPnD (LHG HP5); RBLHG5HPnD-XL (LHG XL HP5)** | 关闭所有 LED |
| **RBLHGG-5acD (LHG 5 ac); RBLHGG-5acD-XL (LHG XL 5 ac); RBLHGG-5HPacD2HPnD (LHG XL 52 ac); RBSXTsqG-5acD (SXTsq 5 ac)** | 关闭除以太网 LED 外的所有 LED |
| **RBLHGG-60ad (Wireless Wire Dish)** | 关闭所有 LED |
| **LHGGM&EG18-EA (LHG LTE18 kit); ATLGM&EG18-EA (ATL LTE18 kit)** | 关闭所有 LED |
| **RBLtAP-2HnD (LtAP)** | 关闭除以太网 LED 外的所有 LED |
| **RBSXTsq-60ad (SXTsq Lite60); RBCube-60ad (Cube Lite60)** | 关闭所有 LED |
| **RBwAPG-60ad (Wireless Wire)** | 关闭所有 LED |
| **RBwAPGR-5HacD2HnD (wAP ac)** | 关闭除以太网 LED 外的所有 LED |

## 示例

### 基本示例

通过 CLI 命令控制 LED，用于脚本编写：

```ros
# 向 leds 菜单添加类型为 "on" 或 "off" 的 LED 条目
/system/leds/add leds=led1 type=off
# 控制 LED
/system/leds/set [find where leds="led1"] type=on
或
/system/leds/set [find where leds="led1"] type=off

```

在 RB951 上启用 User ACT LED 以显示当前 CAP 状态

```ros
/system/leds
add leds=user-led type=ap-cap
```

### 调制解调器信号强度示例

整个调制解调器信号强度范围为 [-113..-51]，modem-signal-threshold 将最弱信号限制提高到 -91，因此 LED 指示的信号范围为 [-91..-51]。该范围根据为 modem-signal LED 触发配置的 LED 数量等分为若干部分。当信号高于 -91 时第一个 LED 点亮，当信号达到 -51 时最后一个 LED 点亮。

```ros
/system/leds
add interface=lte1 leds=led1,led2,led3,led4,led5 modem-signal-treshold=-91 type=modem-signal

```

### 调制解调器接入技术示例

这些 LED 触发示例按照调制解调器技术代次顺序点亮 LED：GSM；3G；LTE。

- 1 个 LED：当 LTE 激活时 led1 点亮。

```ros
/system/leds/add interface=lte1 leds=led1 type=modem-technology
```

- 2 个 LED：led1 - 3G；led2 - LTE；

```ros
/system/leds
add interface=lte1 leds=led1,led2 type=modem-technology

```

- 3 个 LED：led1 - GSM；led2 - 3G；led3 - LTE

```ros
/system/leds/add interface=lte1 leds=led1,led2,led3 type=modem-technology
```