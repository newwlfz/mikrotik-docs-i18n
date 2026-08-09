# PoE-Out

> 本页介绍如何在至少配备一个 PoE-Out 接口的 MikroTik 设备上使用 PoE-Out（以太网供电）功能。MikroTik 设备采用 RJ45 模式 B 引脚排列进行电力传输，通过引脚 4 和 5（+）以及引脚 7 和 8（-）提供 PoE 供电。

import WideTable from '@site/src/components/WideTable';

# PoE-Out

## 概述

本页介绍如何在至少配备一个 PoE-Out 接口的 MikroTik 设备上使用 PoE-Out（以太网供电）功能。MikroTik 设备采用 RJ45 模式 B 引脚排列进行电力传输，通过引脚 4 和 5（+）以及引脚 7 和 8（-）提供 PoE 供电。

:::info
通过 PoE-Out 为其他设备供电时，建议使用最低 18V 的输入电压，除非设备支持多种输出电压（例如，CRS112-8P-4S-IN、CRS328-24P-4S+RM、CRS354-48P-4S+2Q+RM）。

:::

## MikroTik 支持的 PoE-Out 标准

MikroTik 设备可以支持以下部分或全部 PoE 标准：

- **无源 PoE-Out 最高 30 V** - PoE 标准，无需在 PSE（供电设备）和 PD（受电设备）之间进行协商。PoE-Out 使用与提供给 PSE 相同的电压。适用于支持输入电压最高 30 V 的设备的 PoE-Out 标准。（例如 [hEX PoE lite](https://mikrotik.com/product/RB750UPr2)、[RB3011UiAS-RM](https://mikrotik.com/product/RB3011UiAS-RM)、[RB2011iL-IN](https://mikrotik.com/product/RB2011iL-IN)。）

- **无源 PoE-Out 最高 57 V** - 工作原理与低电压（最高 30 V）PoE-Out 相同，但也能通过 PoE 端口提供高电压。输出电压取决于连接到 PSE 的电源。可以为兼容 af/at 的设备供电，这些设备接受通过 4、5（+）和 7、8（-）引脚供电，并且不需要 PoE 协商。（例如 [cAP ac](https://mikrotik.com/product/cap_ac)、[hAP ac](https://mikrotik.com/product/RB962UiGS-5HacT2HnT)、[wsAP ac lite](https://mikrotik.com/product/wsap_ac_lite)。）

- **IEEE 标准 802.3af/at** - 也称为 PoE（802.3af，Type 1）和 PoE+（802.3at，Type 2），这些 IEEE 标准旨在确保供应商之间的兼容性。支持这些标准的 MikroTik PSE 可以为 Type 1 和 Type 2 PD 供电。支持 af/at 标准的 MikroTik 设备也可以为接受无源 PoE-In 的设备供电。（例如 [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm)、[CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm)。）
- **IEEE 标准 802.3bt** - 802.3bt 标准，也称为 PoE++，扩展了早期的 PoE 标准，并引入了“Type 3”（Class 5-6）和“Type 4”（Class 7-8）。该标准使用千兆以太网电缆中的所有四对线来传输电力，因此得名 4PPoE/802.3bt（“4对线以太网供电”）。802.3bt 供电与 PoE-Out 及设备自身供电隔离。（例如 [CRS320-8P-8B-4S+RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm)）

每个 PoE-Out 实现都支持过载和短路检测。

:::info
如果设备的规格页面在“PoE-OUT”部分下标明其能够提供 **`低电压 PoE-Out 电流限制`**，则表示该设备支持 **无源 PoE-Out 最高 30 V**。如果还标明 **`高电压 PoE-Out 电流限制`**，则表示该设备还支持 **无源 PoE-Out 最高 57 V**。

根据上述章节，**无源 PoE-Out 最高 57 V** 也能够为不需要 PoE 协商的 af/at 兼容设备供电。对于 MikroTik PD，这应该没有问题。但是，第三方 PD 可能由于无协商而自行分配较低的 PoE Class，这可能导致 PD 请求的功率减少（这反过来，例如，可能导致 PD 的无线电输出功率降低、外设被禁用等）。不同的 PD 可能有不同的行为。

:::

## 如何选择您的 PoE PSE

此表可帮助您选择最适合您需求的 PSE 设备。

<WideTable>

| 设备名称 | PoE-Out 端口数 | 无源 PoE | 802.3af/at | 802.3bt | 电源输入 | 每端口最大输出 |  | 最大输出功率，W |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
|  |  |  |  |  |  | 输入 18-30V，mA | 输入 30-57V，mA |  |
| **CSS610-8P-2S+IN** | 8 | + | + | - | 交流 & 直流 48-57 V | 1000 | 625 | 140 |
| **CRS328-24P-4S+RM** | 24 | + | + | - | 交流 | 1000 | 450 | 450 |
| **CRS354-48P-4S+2Q+RM** | 48 | + | + | - | 交流 | 1000 | 570 | 700 |
| **CRS112-8P-4S-IN** | 8 | + | + | - | 直流 18-30V & 直流 30-57V | 1000 | 450 | 150 |
| **netPower 16P** | 16 | + | + | - | 直流 18-30V & 直流 30-57V | 1100 | 600 | 160 |
| **RB5009UPr+S+** | 8 | + | + | - | 直流 18-30V 或 直流 30-57V | 900 | 440 | 130 |
| **hEX PoE** | 4 | + | + | - | 直流 18-30V 或 直流 30-57V | 1000 | 450 | 102 |
| **PowerBox Pro** | 4 | + | + | - | 直流 18-30V 或 直流 30-57V | 1000 | 450 | 102 |
| **OmniTIK 5 PoE ac** | 4 | + | + | - | 直流 18-30V 或 直流 30-57V | 1000 | 450 | 102 |
| **hEX PoE lite** | 4 | + | - | - | 直流 18-30V | 1000 |    - | 60 |
| **PowerBox** | 4 | + | - | - | 直流 18-30V | 1000 |  | 60 |
| **RB260GSP** | 4 | + | - | - | 直流 18-30V | 1000 |  | 60 |
| **OmniTIK 5 PoE** | 4 | + | - | - | 直流 18-30V | 1000 |  | 60 |
| **CRS320-8P-8B-4S+RM** | 16 | + | + | + | 交流 | - | 560 (af/at) / 1667 (bt) | 963 |

</WideTable>

## PoE-Out 配置

所有带有 PoE-Out 接口的 MikroTik 设备都支持 PoE 配置。可以从 RouterOS 和 SwOS 界面编辑配置。

### RouterOS

**子菜单：** `/interface/ethernet/poe`

#### 用法

RouterOS 提供了通过 Winbox、Webfig 和 CLI 配置 PoE-Out 的选项。使用 CLI 的基本命令是

| 属性 | 描述 |
| :-- | :-- |
| **print** () | 打印 PoE-Out 相关设置。 |
| **export** () | 导出显示在 `/interface/ethernet` 菜单下。 |
| **monitor** (*string\| interface*) | 显示指定端口或所有端口的 poe-out-status，使用 `/interface/ethernet/poe/monitor [find]` 命令。 |
| **power-cycle** (*duration:0..1m \|*; 默认值：**5s**) | 在指定时间段内禁用 PoE-Out 电源。 |

#### 全局设置

**子菜单：** `/interface/ethernet/poe/settings`

某些 MikroTik PoE-Out 设备支持全局 PoE 设置

| 属性 | 描述 |
| :-- | :-- |
| **ether1-poe-in-long-cable** (*yes \| no*) | 设置为“yes”将禁用所有 poe-out 端口上的短路检测。这是一个潜在危险的设置，应谨慎使用。此功能禁用严格的输入/输出电流监控（短路检测），以允许在长以太网电缆上使用 PoE-Out 和/或避免不正确的短路检测。它也可能影响使用直流连接器供电的 PSE 上的 PoE-Out 行为。 |
| **psuX-max-power** | 指定 PSU 可以消耗的最大功率（瓦特）。**默认值 - 96W**  psu1 - RB5009UPr+S+IN = 直流插座 | RB5009UPr+S+OUT - 2-PIN  psu2 - RB5009UPr+S+IN = 2-PIN 端子 | RB5009UPr+S+OUT - 不可用  此命令专为 RB5009UPr+S+ 设计，以确保电源单元（PSU）的安全和最佳性能。它允许用户设置 PSU 的最大功率限制，防止可能危及系统稳定性和寿命的潜在过载。 |
| **routerboard-max-self-power** | 指定设备为自身供电保留的功率。 |
| **poe-out-limit-power** | PoE-Out 预算限制。 |
| **psuX-poe-out-max-power** | 每个 PSU 的 PoE-Out 限制（瓦特）。 |

#### 端口设置

PoE-Out 可以在菜单下配置。每个端口可以独立控制。

| 属性 | 描述 |
| :-- | :-- |
| **name** () | 接口名称。 |
| **poe-out** (*auto-on \| forced-on \| off*; 默认值：**auto-on**) | 指定 PoE-Out 状态。auto-on - 电路板将尝试检测是否可以向端口供电。为了供电，电阻应在 3kΩ 到 26.5kΩ 范围内。forced-on - 移除检测范围。因此，将通过 B（备用）线对向 PD 供电，以太网供电将始终开启。forced-on-a - 与 forced-on 相同，但将通过 A（主）线对而非 B 线对向 PD 供电。（仅适用于支持 802.3bt PoE-Out 的 PSE）forced-on-bt - 移除检测范围。将通过所有 4 个电源线对向 PD 供电，以太网供电将始终开启。（仅适用于支持 802.3bt PoE-Out 的 PSE）off - 此端口的所有检测和电源均关闭。**重要提示：** **注意：** 无论选择的 PoE-Out 状态如何，短路和过载保护始终开启。     |
| **poe-priority** (*integer:0..99 \| any*; 默认值：**10**) | poe-priority 指定 PoE-Out 端口的重要性，当达到总 PoE-Out 限制时，端口优先级最低的接口将首先被断电。最高优先级为 0，最低优先级为 99。如果有两个或更多端口具有相同优先级，则端口号最小的端口将具有更高优先级。每 6 秒检查一次端口，看是否有可能在因端口优先级而关闭后重新提供 PoE-Out。 |
| **poe-voltage** (*auto \| low \| high*; 默认值：**auto**) | 允许我们在 PoE-Out 端口上手动切换两种电压输出的功能。它仅在具有可切换电压模式的 PSE 上生效（[CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm)、[netPower 16P](https://mikrotik.com/product/netpower_16p)、[CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm)）。 |
| **poe-lldp-enabled***( yes / no;* 默认值：**no**) | [链路层发现协议](https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol "Link Layer Discovery Protocol")（LLDP）是一种用于管理设备的二层以太网协议。LLDP 允许在 PSE 和 PD 之间交换信息。从 RouterOS 7.15 版本开始，此设置已被 [邻居发现](../system-information-and-utilities/neighbor-discovery.md#discovery-configuration) 的 `lldp-poe-power` 属性所取代。 |

#### 电源周期设置

RouterOS 提供了使用 ping 监控 PD 的功能，并在主机无响应时对 PoE-Out 端口执行电源周期操作。可以在 `/interface/ethernet/poe` 菜单下启用 power-cycle-ping 功能。

| 属性 | 描述 |
| :-- | :-- |
| **power-cycle-ping-enabled** (*yes \| no*; 默认值：**no**) | 启用 ping 看门狗，如果主机未响应 ICMP 或 MAC-Telnet 数据包，则对端口执行电源周期操作。 |
| **power-cycle-ping-address** (*IPv4 \| IPv6 \| MAC*; 默认值：) | 将被监控的地址。从 RouterOS 6.46beta16 开始，如果配置了 IP 地址，则需要有一条指向 PD 的活动路由，因此请确保 PSE 可以到达 PD。如果指定了 MAC 地址，PSE 将仅从指定的以太网接口发送 MAC-Telnet ping 请求。当配置 [桥接 vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) 或某种 [VLAN 交换](../bridging-and-switching/user-guides/basic-vlan-switching.md) 时，建议使用 IP 地址来监控您的 PD。 |
| **power-cycle-ping-timeout** (*time:0..1h \|*; 默认值：**5s**) | 如果主机在超过超时时间段内未响应，则 PoE-Out 端口将关闭 5 秒。 |
| **power-cycle-interval** (*time\| any*; 默认值：) | 在指定间隔之间禁用 PoE-Out 电源 5 秒。与 power-cycle-ping 功能无关。 |

如果启用了 power-cycle，`/interface/ethernet/poe/monitor` 将显示主机的实际状态以及将执行电源周期的时间 [PoE-Out 监控](#poe-out-monitoring)。

:::info
power-cycle-host-alive: YES/NO（显示被监控的主机是否可达）
power-cycle-after: TIME（显示端口将被电源周期操作的时间）

:::

### SwOS

SwOS 界面提供基本的 PoE-Out 配置和监控选项，更多详细信息请参阅 [SwOS PoE](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=76415036#CRS3xxandCSS32624G2S+seriesManual-PoE) 用户手册。

## PoE-Out 监控

### RouterOS

**子菜单：** `/interface/ethernet/poe/monitor`

| 属性 | 描述 |
| :-- | :-- |
| **name** () | 接口名称。 |
| **poe-out** () | 显示 PoE-Out 状态。 |
| **poe-out-status** () | 显示端口当前的 PoE-Out 状态。powered-on - 电源已施加到端口，PoE-Out 正常运行。waiting-for-load - PSE 尝试检测是否可以向端口供电。为了供电，电阻应在 3kΩ 到 26.5kΩ 范围内；short-circuit - 在 PoE-Out 端口上检测到短路，电源关闭，仅进行低电压检测。这也可能意味着连接的设备不支持 PoE。overload - 超过 PoE-Out 电流限制，PoE-Out 端口上的电源关闭。有关端口限制，请参阅每个型号的规格。voltage-too-low - 无法使用 PSE 提供的电压为 PD 供电。voltage-too-high - 检测到连接的设备是 PoE-In 设备，但 PSE 的输出电压高于 PD 支持的范围；current-too-low - current-too-low 表示 PD 消耗的电流（&lt;10mA）低于正常 PoE-Out 设备应消耗的电流。voltage_on_poe-in - 显示 PoE-Out 端口上当前存在的电压。此状态表示 PoE-Out 端口检测到意外的电压输入，可能发生在两种情况下：外部电源 – 另一个设备正在向端口供电（PoE-In 电压）。内部故障 – 端口上的 PoE-Out 电路可能已损坏。PD 接收到的电压过低，无法正常供电（例如，Vmin =>30V，但提供 24V）；PD 使用第二个电源，其电压高于 PSE，因此所有电流都来自第二个直流电源，而不是 PSE PoE-Out 端口。 off - 此端口的所有检测和电源均关闭；power_reset - PSE 控制器正在重置电源，例如，在执行电源周期命令或 ping 失败时（power-cycle-ping）；controller_init - PSE 控制器初始化；controller_upgrade - PSE 控制器正在升级；controller_error - PSE 控制器无响应。 |
| **poe-out-voltage** () | 显示施加到 PD 的 PoE 电压。 |
| **poe-out-current** () | 显示 PD 消耗的端口电流（mA）。 |
| **poe-out-power** () | 显示 PD 功耗。 |
| **poe-out-power-pair()** | 显示 PSE 通过哪个电源线对向 PD 供电。（**a** = 1,2(+) 3,6(-) ; **b** = 4,5(+) 7,8(-) ; **bt** = 所有 4 对线）。 |

如果使用了 `power-cycle-ping` 功能，`/interface/ethernet/poe/monitor [find]` 将显示附加字段：

### SNMP

可以使用 SNMP 协议监控 PoE-Out 值。这需要在 PSE 上启用 [SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md)。

SNMP OID 表：

- 1.3.6.1.4.1.14988.1.1.15.1.1.1 - 接口 ID
- 1.3.6.1.4.1.14988.1.1.15.1.1.2 - 接口名称
- 1.3.6.1.4.1.14988.1.1.15.1.1.4 - 电压（dV，分伏）
- 1.3.6.1.4.1.14988.1.1.15.1.1.5 - 电流（mA）
- 1.3.6.1.4.1.14988.1.1.15.1.1.6 - 功耗（dW，分瓦）

也可以从 RouterOS 请求 SNMP 值，例如，`snmp-walk` 将打印所有可用 PoE-Out 端口的当前 mA：

:::info
`/tool/snmp-walk` address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5

:::

要获取非常具体的 OID 值，请使用 `snmp-get` 工具（显示 ether3 接口上的当前 mA）：

:::info
tool snmp-get address=10.155.149.252 oid=1.3.6.1.4.1.14988.1.1.15.1.1.5.3

:::

## PoE-Out 通知

### PoE-Out LED

##### 具有固定电压输出的型号

PoE-Out LED 行为可能因型号而异，但大多数型号会通过一个额外的 LED 指示 PoE-Out 状态。具有单一电压输出的设备将点亮：

- 红色 LED - PoE-Out 端口状态为 **powered-on**（自动或强制开启模式）。
- 红色 LED 闪烁 - PoE-Out 端口状态为 **short-circuit**。

##### 具有可选电压输出的型号

具有多种电压选项的型号可以指示附加信息：

- 绿色三角形 LED - PoE-Out 端口状态为 **powered-on**，PD 使用低电压。
- 红色三角形 LED - PoE-Out 端口状态为 **powered-on**，PD 使用高电压。
- 绿色 LED 闪烁 - 低电压的 PoE-Out 端口状态为 **short-circuit** 或 **overload**。
- 红色 LED 闪烁 - 高电压的 PoE-Out 端口状态为 **short-circuit** 或 **overload**。

##### 特定型号的 LED 行为

- [CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[netPower 16P](https://mikrotik.com/product/netpower_16p) - 所有 PoE LED 闪烁：某个端口插入了错误电压的 PSU。
- [CRS320-8P-8B-4S+RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm) - 紫色 LED - PoE-Out 端口状态为 powered-on，PD 使用高电压（802.3bt）。紫色三角形 LED 闪烁 - PoE-Out 端口状态为短路或过载。

### PoE-Out 日志

默认情况下，PoE-Out 事件 [日志](../diagnostics-monitoring-and-troubleshooting/log/index.md) 已启用，并使用“warning”和“info”主题通知用户 PoE-Out 状态更改。每次 PoE-Out 状态更改都会添加日志条目。重要日志将使用“warning”主题添加，信息性日志将使用“info”主题添加。当启用 PoE LLDP 时，设备日志中会提供 LLDP 状态更新，例如：

:::info
`06:56:50 poe-out,debug ether4 LLDP TLV 25.0W request denied : hw-limit`

:::

#### 可能的拒绝原因

:::info

- budget - 请求的功率超过 PSE 总预算。
- hw-limit - 请求的功率超过硬件支持的范围（PSU 会影响此值）。
- low-voltage - 对低电压端口发出了 LLDP 请求。
- off - 端口已关闭。
- class-limit - LLDP 请求的功率超过 Class 所能提供的范围。
- cmd-failed - RouterOS 无法向控制器发出请求。

:::

为避免在 PD 因 current-too-low 而未通电时产生不必要的日志，RouterOS 将过滤此类事件，并每 512 个 current-too-low 事件添加一条日志。

#### 必要时可以禁用日志

:::info
`/system/logging/set [find topics~"info"]` topics=info,!poe-out
`/system/logging/set [find topics~"warning"]` topics=warning,!poe-out

:::

### GUI/CLI 中的 PoE-Out 警告

为了通知用户重要的 PoE-Out 相关问题，将在 Winbox / WebFig 和 CLI 界面字段中显示消息：

:::info
1 RS ;;; poe-out status: overload  
ether1 ether 1500 1588 9204 64:D1:54:61:D5:E0

:::

WebFig 和 Winbox 将在接口下通知用户：

![](https://manual.mikrotik.com/docs/hardware/img/poe-out-01.webp)

## 工作原理

### PoE-Out 模式

#### auto-on 模式

如果在 PoE-Out 接口上选择了 auto-on，则端口按以下严格顺序运行：

- 低电压 PSE 检查连接端口上的电阻。如果检测到的电阻范围在（3kΩ 和 26.5kΩ）之间，则打开电源。
- 施加电源后，PSE 持续检查是否达到过载限制或检测到短路。
- 如果拔掉电缆，端口将返回到检测状态，并保持关闭状态，直到检测到合适的 PD。

#### forced-on 模式

如果选择了 forced-on，则端口按以下严格顺序运行：

- PSE 禁用端口上的电阻检查，并根据 **poe-out()** 状态在引脚上施加电源，即使没有连接电缆。
- 施加电源后，PSE 仍会持续检查是否检测到过载或短路。
- 拔掉电缆后，端口上的电源仍保持启用状态。

#### off 模式

如果使用 off 模式，端口上的 PoE-Out 将关闭，不进行任何检测，接口将表现得像一个简单的以太网端口。

### PoE-Out 限制

检查 PoE-Out 规格以了解硬件限制非常重要，因为不同型号可能有所不同。

#### PoE-Out 端口限制

PoE-Out 端口受特定电压下支持的最大安培值限制，通常最大电流对于低电压设备（最高 30 V）和高电压设备（31 至 57 V）会有所不同。

#### PoE-Out 总限制

PSE 也有一个不能超过的总 PoE-Out 电流限制，即使单个端口限制允许。

#### PoE-Out 极性

大多数\*\* MikroTik PSE 使用相同的 PoE-Out 引脚极性 [模式 B](https://en.wikipedia.org/wiki/Power_over_Ethernet#Pinouts) 4、5（+）和 7、8（-），但是其他供应商可能在 PD 上使用相反的极性或 [模式 A](https://en.wikipedia.org/wiki/Power_over_Ethernet#Pinouts) 引脚排列。反极性将需要使用交叉电缆，但模式 A PD 将需要模式 B 到模式 A 的转换器。

:::note
**\*\* 例外：** [CRS320-8P-8B-4S+-RM](https://mikrotik.com/product/crs320_8p_8b_4s_rm) 同时使用模式 A 和模式 B 极性。

:::

:::warning
**注意：** 具有高输入浪涌电流的无源 PD 可能导致 PSE 上的过流保护。确保 PD 规格支持从 PSE 供电（不仅仅是从无源电源注入器）。

:::

### 安全性

PSE 具有以下安全功能：

##### PoE-Out 兼容性检测

auto-on 模式被认为是安全的。它将检查端口上的电阻是否在允许的范围内，然后才在接口上启用 PoE 输出。范围是 3kΩ 到 26.5kΩ。

##### 过载保护

当 PoE-Out 端口通电时，会持续检查是否过载。如果检测到过载，端口上的 PoE-Out 将关闭，以避免损坏 PD 或 PSE。

几秒钟后，PoE Out 功能将再次开启，以检查环境是否已改变，PD 是否可以再次供电。这对于未连接到主电源的配置（太阳能装置、因主电源故障而依靠电池运行的设备）非常重要，这样当电压下降时 - 将检测到过载并关闭连接的设备。一段时间后，当电压水平恢复到通常的工作值时 - 连接的设备可以再次通电。

##### 短路检测

当 PoE-Out 端口启用电源时，PSE 会持续检查短路。如果检测到短路，所有端口的电源都将关闭，以确保 PD 和 PSE 不会受到额外损坏。PSE 将继续检查 PoE-Out 端口，直到环境恢复正常。

:::warning
**警告：** 确保没有连接不具有 3kΩ 到 26.5kΩ 电阻范围的非标准不兼容 PD，以免 PSE 尝试对其施加电源。

:::

### 特定型号功能

具有独立 8 端口部分的 PSE（[CRS112-8P-4S-IN](https://mikrotik.com/product/crs112_8p_4s_in)、[CRS328-24P-4S+RM](https://mikrotik.com/product/crs328_24p_4s_rm)、[netPower 16P](https://mikrotik.com/product/netpower_16p)、[CRS354-48P-4S+2Q+RM](https://mikrotik.com/product/crs354_48p_4s_2q_rm)）允许 PoE-Out 独立于 RouterOS 工作；这意味着您可以重启/升级 RouterOS，而 PD 不会重启。

:::info
注意：[CRS328-24P-4S+](https://mikrotik.com/product/crs328_24p_4s_rm)、[netPower 16P](https://mikrotik.com/product/netpower_16p) 的 Poe-Out 优先级在每个 8 端口部分独立工作！

:::

## PoE Out 示例

RouterOS 允许我们在 PoE-Out 端口上定义优先级，因此如果您的安装将超过功率预算，PSE 将禁用优先级最低的不太重要的 PD。

*0* 优先级是最高优先级，*99* - 最低优先级

### 设置优先级

如何从 CLI 设置优先级的示例：

:::info
`/interface/ethernet/poe/set` ether2 poe-priority=10
`/interface/ethernet/poe/set` ether3 poe-priority=13
`/interface/ethernet/poe/set` ether4 poe-priority=11
`/interface/ethernet/poe/set` ether5 poe-priority=14

:::

当功率预算超过总 PoE-Out 限制时会发生什么 - 首先，如果检测到过载，ether5 将被关闭（最低优先级），然后进行重新检查，如果仍然检测到总限制过载，则按优先级关闭下一个端口，在此示例中，ether3 将被关闭。这两个端口将每隔几秒检查一次，以确定是否可以重新为这些端口开启 PoE-Out。重新上电将按照断电的相反顺序进行。

### 相同优先级

如果所有或部分端口具有相同的 poe-priority，则端口号最小的端口将具有更高优先级

:::info
`/interface/ethernet/poe/set` ether2 poe-priority=10
`/interface/ethernet/poe/set` ether3 poe-priority=10
`/interface/ethernet/poe/set` ether4 poe-priority=10
`/interface/ethernet/poe/set` ether5 poe-priority=10

:::

在此示例中，如果达到总 PoE-Out 限制，ether5 将首先被关闭，然后是 ether4，然后是 ether3，因为所有这些端口都具有相同的 poe 优先级。

### 监控 PoE-Out

可以使用命令 `/interface/ethernet/poe/monitor <interface>` 监控 PoE-Out 端口

:::info

```
[admin@MikroTik] > /interface/ethernet/poe/monitor ether9  
                name: ether9      
             poe-out: auto-on     
      poe-out-status: powered-on  
     poe-out-voltage: 54.2V       
     poe-out-current: 449mA       
       poe-out-power: 24.3W       
  poe-out-power-pair: b       
```

:::

### 电源周期 Ping

使用 power-cycle-ping 功能监控连接的 PD：

:::info
`/interface/ethernet/poe/set` ether1 power-cycle-ping-enabled=yes power-cycle-ping-address=192.168.88.10 power-cycle-ping-timeout=30s

:::

在此示例中，连接到 ether1 的 PD 将使用 power-cycle-ping 功能持续监控，该功能将发送 ICMP ping 请求并等待回复。如果 IP 地址为 192.168.88.10 的 PD 超过 30 秒未响应，PoE-Out 端口将关闭 5 秒。

## 故障排除

如果 PD 无法启动或在由您的 PSE 供电时意外重启，建议首先检查：

- **PD 支持的输入电压** - PSE 输出电压必须在 PD 支持的范围内。否则，PD 与 PSE 不兼容，将无法启动。请查阅 PD 数据表。
- **PD 支持的输入 PoE-in 标准** - 某些 PD 即使支持高达 57 V 的 PoE-in，也不支持 af/at 标准，请查阅 PD 数据表。
- **PD 被 PSE 重启：**
  - 检查 PD 是否超过 PSE 的 PoE-Out 端口限制和总 PoE-Out 端口限制，请查阅 PSE 数据表。
  - 检查电压限制是否未降至支持值以下（可能由线路上的电压降引起）。
  - 检查您是否使用了正确的电源，PSU 的输出功率应计算如下：

    ```
    (PSE 最大功耗) + (所有 PD 最大功耗) + 10%)
    ```

  - 检查您是否使用了高质量的以太网电缆，尤其是在使用 PoE 的情况下。
- **检查 RouterOS 版本** - 某些 PoE 相关功能可能会随 RouterOS 更新，请确保您运行的是最新的 [RouterOS 版本](https://mikrotik.com/download)。
- **PD 无法启动：**
  - 在某些情况下，即使 PD 支持无源 PoE，并且功耗不超过指定的 PSE 端口限制，也可能无法启动。这可能是由浪涌电流触发 PSE 上的过流保护引起的。确保 PD 规格支持从 PSE 供电（不仅仅是从无源电源注入器）。
  - 极性 - 具有相反或不同引脚排列的设备可能无法从所有 PSE 启动。请查阅 PD 数据表。
  - 电阻不兼容 - PD 电阻应在 3kΩ 到 26.5kΩ 范围内（对于无源 PoE），在 af/at 上应在 23.75kΩ 到 26.25kΩ 范围内。

## 旧版

### PoE-Out 控制器升级

运行 RouterOS 5.x 的 PoE-Out 设备也可能包含旧的 PoE-Out 控制器固件；升级到 RouterOS 6.x 将自动更新 PoE-Out 固件。1.x 和 2.x PoE-Out 控制器固件之间的更改将导致更高的最大端口限制（0.5A 到 1A）（如果硬件支持），并且还将提供一些额外的可监控数据，并允许使用 PoE-Out 优先级。

所有随 RouterOS 6.x 一起提供的 MikroTik 设备都已经支持最新的 PoE-Out 固件。