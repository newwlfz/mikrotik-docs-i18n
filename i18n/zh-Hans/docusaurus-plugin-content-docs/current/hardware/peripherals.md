# 外设

> 本文介绍 RouterBOARD 硬件设备支持的附加外设。

import WideTable from '@site/src/components/WideTable';

# 外设

本文介绍 RouterBOARD 硬件设备支持的附加外设。

## 蜂窝调制解调器

RouterOS v7 支持以下蜂窝调制解调器：

- MikroTik 调制解调器。
- 按设备类别/类型支持的第三方调制解调器：
  - MBIM 类 USB 接口
  - USB-CDC 类 USB 接口
  - RNDIS 类型 USB 接口
- 具有额外支持的第三方调制解调器（请参阅下方调制解调器表格）。

## 请注意

- 并非所有调制解调器都列在支持的调制解调器表格中。某些调制解调器即使未列出也可能正常工作，因为调制解调器制造商经常重复使用相同的硬件 ID，反之亦然。
- 定制、本地化或锁定单元可能存在兼容性问题。
- 第三方调制解调器可能需要在与 RouterOS 配合使用前进行配置调整。
- 对于安装在支持 PCIe/USB2.0 的 mini-PCIe 插槽中、带有 USB3.0 接口的 mini-PCIe 调制解调器，必须将 USB 速度限制为 USB2.0，或者隔离 mini-PCIe 共享的 PCIe/USB3.0 引脚。请参阅表格下方的图片。

## 蜂窝调制解调器

| 型号 | vendor-id | device-id | 已测试的 RouterOS 版本 | 备注 | 格式 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Alcatel IK40 |  |  | v6.41RC11 | LTE 接口，调制解调器只能通过调制解调器的配置网页进行配置。 | USB |
| Alcatel IK41 |  |  | v6.48 | 免配置 LTE 接口 | USB |
| Android usb tethering interface |  |  | v6.7 | 某些设置会被忽略。 | USB |
| AnyData ADU-E630WH |  |  | v6 | （又名 "USB Wireless HSDPA/UMTS 2.1GHz GSM/GPRS/EGPRS 900/17000MHz/CDMA 1x EVDO Rev.A"） | USB |
| Anteniti 3372h-153 |  |  | 7.12 |  | USB |
| BandRich C501 |  |  | v5.25 和 v6.0 |  | USB |
| Cinterion LTE Modem | 0x1e2d | 0x0061 | v7.14 及更高版本 | LTE 接口，某些设置会被忽略。SMS 功能不完整。 | MiniPCI-e |
| D-link DWM-157 | 0x2001 | 0x7d02 | v6.xx | 可用！数据通道：2，信息通道：3，调制解调器初始化：AT+CFUN=1，vendor-id="0x2001" device-id="0x7d02" 来自调制解调器的一些信息：> H/W Ver.: B1, F/W Ver.: 2.0.1eu, revision: +CGMR: MOLY.WR8.W1231.DC.WG.MP.V3, 2013/04/09 02:08 不同的硬件版本可能无法与 RouterOS 配合使用 | USB |
| D-link DWM-222 |  |  | 请参阅备注 | 存在多个具有相同营销名称的调制解调器版本：H/W ver: A1 - 从 RoS v6.38 起作为免配置 LTE 接口支持。调制解调器固件版本从 "2.1.4EU" 开始。H/W ver: A3 - 使用调制解调器固件提供的 RNDIS 接口作为免配置 LTE 工作（仅限 RouterOS v7） | USB |
| Dell DW5821e |  |  | v7.4beta4 及更高版本 | MBIM 驱动。版本：T77W968.F1.0.0.5.2.VZ.013 044 | M.2 |
| Dell DW5821e-eSIM | 0x413c | 0x81e0 | 7.11 及更高版本 | MBIM 驱动。固件：T77W968.F1.0.0.5.2.GC.013。已添加 "at-chat" 支持 | M.2 |
| DELL T99W175 | 0x05c6 | 0x90d5 | 7.16 及更高版本 | MBIM 驱动。固件：T99W175.F0.1.0.0.9.GC.004。已添加 "at-chat" 支持 | M.2 |
| Dell Wireless 5530 HSPA |  |  | v6.1 及更高版本 | 数据通道 0，信息通道 0，初始化：AT+CFUN=1（需要通过命令 AT\*ENAP=1,1 手动更改配置文件） | MiniPCI-e |
| Ericsson F5521gw |  |  | v6.x 及更高版本 |  | MiniPCI-e |
| Fibocom FM150-AE/FM150-NA | 0x2cb7 | 0x0111 | v7.1beta5 | MBIM 驱动。版本：89603.1000.00.01.01.03 | M.2 |
| Fibocom NL-952-EAU |  |  | v7.1beta5 | MBIM 驱动。版本：19600.7000.00.04.01.05 | M.2 |
| 基于 Marvell PXA1802 的调制解调器 | 0x1286 | 0x4e31 | v7.2.2 |  | mini-PCIe |
| Huawei E153 |  |  | v6.31 及更高版本 |  | USB |
| Huawei E171 |  |  | v6.xx | 可用！ppp 接口，vendorid=0x12d1 deviceid=0x140c | USB |
| Huawei e3131 |  |  | v6.xx 及更高版本 | ppp 接口 | USB |
| Huawei E3372h, E5576h, E8372h | 0x12d1 | 0x14db | v6.8 | 适用于 vendor-id="0x12d1" device-id="0x14db" 调制解调器的免配置 LTE 接口。带有 -320 和 -608 后缀的型号无法与 RouterOS v6 配合使用，请改用 v7。带有 -325 后缀的型号仅适用于 arm cpu | USB |
| Huawei E3276-150 |  |  | v6.xx | ppp 接口 | USB |
| Huawei E3351 |  |  | v6.24 及更高版本 |  | USB |
| Huawei E3531 |  |  | v6.24 或 6.40RC25 | 此调制解调器有不同的版本，E3531-6 从版本 6.40RC25 起作为 ppp 工作，mbim 仅从 RouterOS V7 开始支持 | USB |
| Huawei e398 |  |  | v6.xx 及更高版本 | ppp 接口 | USB |
| Huawei E5377 |  |  | v6.36.1 | MIFI 单元。不支持串口，但可通过 LTE 接口上的 IP 工作 | USB |
| Huawei E5673s-609 |  |  | v6.xx | LTE 接口 | USB |
| Huawei K5160 |  |  | v6.37  v7.0beta6 | v6 和 v7 - 免配置 LTE 接口。v7 - 默认将尝试在 MBIM 模式下使用调制解调器 | USB |
| Huawei K5161 |  |  | v6.47 | 免配置 LTE 接口 | USB |
| Huawei ME909s-120 |  |  | v6.28 | 推荐的调制解调器固件版本 11.617.24.00.00。要将 LTE 接口 IP 子网掩码减小到 /32，请使用 at-chat 命令配置调制解调器：`/interface/lte/at-chat [find]` input="AT^CUSTFEATURE=3,1" | MiniPCI-e |
| Huawei ME909u-521 |  |  | v6.11 |  | MiniPCI-e |
| Huawei MU609 |  |  | v6.11 |  | MiniPCI-e |
| Huawei MU709s-2 |  |  | v6.28 |  | MiniPCI-e |
| Huawei MS2372h-517 |  |  | v7.12beta3 | ppp/串行接口 | USB |
| Jaton MT421e |  |  | v6.40RC32 | 带以太网模拟的 LTE 接口（无法配置），LTE 支持频段 42/43 | MiniPCI-e |
| Netgear Unite Explore 815S |  |  | v6.41 | MIFI 单元。不支持串口，但可通过 LTE 接口上的 IP 工作。 | USB |
| Novatel USB730L |  |  | v6.41RC6 | LTE 接口 | USB |
| Olivetti Olicard 500 |  |  | v6.41RC11 | ppp 接口 | USB |
| Quectel EC20/EC21 |  |  | v6.xx | ppp 接口 | MiniPCI-e |
| Quectel BG77 | 0x2c7c | 0x0700 | v6.47 | 串行/PPP 接口，单 AT/调制解调器通道 | OEM 模块 |
| Quectel BG95-M3 |  |  | v6.47 | 串行/PPP 接口，单 AT/调制解调器通道。无法在 wAP R ac 板上工作。 | mini-PCIe |
| Quectel BG96 |  |  | v6.45 | 串行/PPP 接口，2x AT/调制解调器通道 | mini-PCIe |
| Quectel EC25-EU | 0x2c7c | 0x0125 | v6.42 | ppp/LTE 接口。RouterOS v6 CDC-ECM 模式 - LTE 接口接收调制解调器内部网络中的地址。RouterOS v7 MBIM 模式 - LTE 接口使用 APN IP 地址。 | MiniPCI-e |
| Quectel EG25-G | 0x2c7c | 0x0125 | 6.48.3 | RouterOS v6 CDC-ECM 模式 - LTE 接口接收调制解调器内部网络中的地址。RouterOS v7 MBIM 模式 - LTE 接口使用 APN IP 地址。在某些板上可能需要禁用 SIM 热插拔检测：```/interface/lte/set [find] modem-init="AT+QSIMDET=0,1"``` | MiniPCI-e |
| Quectel EM12-G | 0x2c7c | 0x0512 | v7.1beta5 | MBIM 驱动 | m.2 |
| Quectel EP06 |  |  | v6.42 | ppp/LTE 接口 | MiniPCI-e |
| Quectel RG255C-GL |  |  | v7.18 | 通过 at-chat 提供基本支持，最低固件版本：RG255CGLABR01A04M4G\_A0.004.A0.004。调制解调器组合：`at+qcfg="usbnet",0` | mini-PCIe |
| Quectel RM500Q-GL | 0x2c7c | 0x0800 | v7.1beta6 | MBIM 驱动 | m.2 |
| Quectel RM500Q-AE | 0x2c7c | 0x0800 | v7.1beta6 | MBIM 驱动 | m.2 |
| Quectel RM502Q-AE | 0x2c7c | 0x0800 | v7.1beta5 | MBIM 驱动 | m.2 |
| Quectel RM510Q-GL | 0x2c7c | 0x0800 | 7.9 | MBIM 驱动 | m.2 |
| Quectel UC15 |  |  | v6.xx | 可用，ppp 接口 | MiniPCI-e |
| Quectel UC20 |  |  | v6.xx | 可用，ppp 接口 | MiniPCI-e |
| R11e-4G | 0x2cd2 | 0x0003 | v6.42 | LTE 接口。支持多 APN 透传。 | MiniPCI-e |
| R11e-LTE6 | 0x2cd2 | 0x0004 | v6.39.2 | LTE 接口。支持多 APN 透传。 | MiniPCI-e |
| R11e-LTE | 0x2cd2 | 0x0001 | v6.39.2 | LTE 接口。支持多 APN 透传。 | MiniPCI-e |
| Sierra Netgear AirCard 320U |  |  | 6.41 | 客户使用固件 03.05.23 测试了该调制解调器 | USB |
| Sierra wireless MC73xx |  |  | v6.xx(ppp) v7.xx (LTE) | 可用！PPP 接口。从 v7.xx 开始，它将支持调制解调器切换到暴露 MBIM 接口的 LTE 接口。MC7304 已使用固件 SWI9X15C\_05.05.67.00 测试 | MiniPCI-e |
| Sierra Wireless MC7430 |  |  | v6.xx 及更高版本 | 数据通道 2，信息通道 2，调制解调器初始化：AT+CGATT=0，拨号命令：AT+CGATT=1;D\*99#，还需要隔离 3.0 引脚（引脚：23,25,27,31,33） | MiniPCI-e |
| Sierra Wireless MC74xx |  |  | v7.1 | 对具有 MBIM 接口/USB 组合的调制解调器的基本功能支持 | mini-PCIe |
| Sierra Wireless MC7455 |  |  | v7.3beta37 | MBIM 模式，扩展支持 USB 组合：1009 - diag,modem,mbim100D - diag,nmea,modem,mbim | mini-PCIe |
| Sierra Wireless MC7710/MC7700/MC7750 |  |  | v5.25, v6.0 和 6.40RC43 | 如果调制解调器使用固件 3.5，则应升级到 3.5.23.2 固件版本，以便在 RouterOS 中再次正常工作。 | MiniPCI-e |
| SIMcom SIM5360 |  |  | v6.xx | 可用！使用 PPP 接口，vendor-id="0x05c6" device-id="0x9000" | MiniPCI-e / USB w/ converter |
| SIMcom SIM7100 | 0x1e0e | 0x9001 | v6.xx(ppp) v7.xx (LTE) | 可用！PPP 接口。从 v7.xx 开始，它将支持 LTE 接口。 | MiniPCI-e / USB w/ converter |
| SIMCom SIM8202G-M.2 |  |  | v7.11 | 支持 MBIM 驱动：AT+CUSBCFG=usbid,1e0e,901e | m.2 |
| SXT LTE |  |  | v6 | LTE 接口。旧版 SXT LTE | 内置 |
| Tele2.ru LTE-D402 |  |  | v6.47 | 免配置 LTE 接口 |  |
| Telecom NZ T-Stick ZTE MF-181 |  |  | v6.0rc13 | 数据通道=2，信息通道=2，APN internet.telecom.co.nz，电话号码=\*99#。已在 CCR1016-12G 上测试数据和短信均正常 | USB |
| Telit FN980m |  |  | v7.5 | AT#USBCFG=2 | m.2 |
| Telit LE910 | 0x1bc7 | 0x1201 | v6.xx | ppp 接口 | MiniPCI-e |
| Telit LE910C1 |  |  | v6.46 | 无法从 RouterOS 配置 | MiniPCI-e |
| Telit LM940 |  |  | v6.44 | 某些情况下 LTE 接口需要隔离 3.0 引脚（引脚：23,25,27,29,31,33） | MiniPCI-e |
| Telit LM960 |  |  | v6.46 | 某些情况下 LTE 接口需要隔离 3.0 引脚（引脚：23,25,27,29,31,33） | MiniPCI-e |
| TPS (Turning Point Solution) GCT450 |  |  | v6.48 | 免配置 LTE 接口 | MiniPCI-e |
| Vodafone (Huawei) K4203 |  |  | v7.xx | 在 ROS v6 中不支持，但由于此调制解调器支持 MBIM 驱动，在 ROS v7 中可能支持。 | USB |
| Vodafone K4201-Z |  |  | v6.8 | 某些设置会被忽略。LTE 接口。 | USB |
| Vodafone K4305 |  |  | v6.7 | 某些设置会被忽略。 | USB |
| Vodafone K5160 |  |  | v6.37 | 某些设置会被忽略。 | USB |
| Yota LU150 |  |  | v5.22 和 v6.4 | 某些设置会被忽略。 | USB |
| Yota wifi modem |  |  | v6.7 | 某些设置会被忽略。 | USB |
| Yota WLTUBA-107 |  |  | v6.0 | 某些设置会被忽略。 | USB |
| ZTE 821D |  |  | v6.x | 设置信息通道 = 1，数据通道 = 3，拨号命令=ATDT | USB |
| ZTE AC5730 |  |  | v6.x |  | USB |
| ZTE ME3630-E |  |  | v6.40RC26 | ppp 和 LTE 接口 | MiniPCI-e |
| ZTE MF110 |  |  | v6.28 及更高版本 | 设置信息通道 = 2，数据通道 = 2，拨号命令=ATM1L3DT | USB |
| ZTE MF823 |  |  | v6.8 | 某些设置会被忽略。某些设备需要进入 FACTORY 模式才能更改操作状态。 | USB |
| ZTE MF825A |  |  | v6.xx | 某些设置会被忽略。 | USB |
| ZTE MF827 |  |  | v6.8 | 某些设置会被忽略。 | USB |
| ZTE MF832S |  |  | v7.10 | 免配置支持，可能需要使用 at-chat 或调制解调器初始化字符串设置某些设置 | USB |
| ZTE MF833U1 | 0x19d2 | 0x1405 | v7.20.6 | 免配置 LTE 接口 | USB |
| ZTE MF90 |  |  | v6.44beta32 及更高版本 | LTE 接口 | USB |

:::warning
并非所有调制解调器都已列出。本地化和锁定单元可能存在兼容性问题。

:::

对于某些支持 USB3.0 的调制解调器，在某些情况下需要隔离 USB3.0 引脚以确保正确初始化：

![](https://manual.mikrotik.com/docs/hardware/img/peripherals-01.webp)

## SFP 模块

<WideTable>

| 品牌 | 型号 | 速率 | 连接器/线缆类型 | 波长 | 测试设备 | 可用/不可用 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| MikroTik | S-85DLC05D | 1,25G | 双 LC，多模 | 850nm | \*查看：[SFP/SFP+ 兼容性参考表](../wired-connections/mikrotik-wired-interface-compatibility.mdx) | 原生支持 |
| MikroTik | S-31DLC20D | 1,25G | 双 LC，单模 | 1310nm | \*查看：[SFP/SFP+ 兼容性参考表](../wired-connections/mikrotik-wired-interface-compatibility.mdx) | 原生支持 |
| MikroTik | S-35LC20D | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1550nm | \*查看：[SFP/SFP+ 兼容性参考表](../wired-connections/mikrotik-wired-interface-compatibility.mdx) | 原生支持 |
| MikroTik | S-53LC20D | 1,25G | BiDi LC，单模 | Tx:1550nm/Rx:1310nm | \*查看：[SFP/SFP+ 兼容性参考表](../wired-connections/mikrotik-wired-interface-compatibility.mdx) | 原生支持 |
| MikroTik | S-RJ01 | 1000/100/10 | RJ45，Cat5/Cat6 | 不适用 | \*查看：[SFP/SFP+ 兼容性参考表](../wired-connections/mikrotik-wired-interface-compatibility.mdx) | 原生支持 |
| Axiom | AXG91632 | 1000BASE-LX | 双 LC | 1310nm | CRS125-24G-1S-RM | 可用！ |
| Finisar | FCLF-8521-3 | 10/100/1000 | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| Finisar | FCLF-8521-3-MD | 10/100/1000 | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| Finisar | FTRJ8519P1BNL-B1 | 10/100/1000 1.25 Gb/s 1000Base-SX 以太网 | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| Finisar | FTLF8519P2BNL | 10/100/1000 1.25 Gb/s 1000Base-SX 以太网 | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| Finisar | FTRJ1319P1BTL | 1.25Gb/s 1000Base-LX 以太网 | 双 LC，单模 | 1310nm | CCR1009-8G-1S-1S+ 和 CCR1009-7G-1C-1S+ | 可用！ |
| Unica | SFP-1.25G-T | 1000M | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| Dell | FTLX8571D3BCL | 1,25G | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| Unica | GP-3124-L2CD-C | 1,25G | 双 LC，多模 | 1310nm | RB2011LS-IN | 可用！ |
| Cisco | GLC-T | 1.25G | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| Cisco | GLC-SX-MM | 1000BASE-SX SFP 收发器模块，用于多模光纤，1.25G | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| Cisco | SFP-GE-L | 1000BASE-LX/LH SFP 收发器模块，用于单模光纤，1.25G | 双 LC，单模 | 1300nm | 多种 MT 硬件 | 可用！ |
| 6COM | 6C-SFP-T | 10/100/1000 | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| 6COM | 6C-WDM-0210BSD | 1,25G | BiDi SC，单模 | Tx:1550nm/Rx:1310nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-WDM-0210ASD | 1,25G | BiDi SC，单模 | Tx:1310nm/Rx:1550nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-SFP-0310D | 1,25G | 双 LC，多模 | 1310nm | RB2011LS-IN | 可用！ |
| 6COM | 6C-SFP-0301D | 1,25G | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| Ingellen | INSP-T(10/100/1000) | 10/100/1000 | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| Ingellen | INSPL-53-BX | 1,25G | BiDi LC，多模 | 1550/1310 | RB2011LS-IN | 可用！ |
| Ingellen | INSPL-35-BX | 1,25G | BiDi LC，多模 | 1310/1550 | RB2011LS-IN | 可用！ |
| Ingellen | INSP-LX-SM | 1,25G | 双 LC，单模 | 1310nm | RB2011LS-IN | 可用！ |
| Ingellen | INSP-SX-MM | 1,25G | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGT-R1T4-05I1 | 10/100/1000 | RJ45，Cat6 | 不适用 | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-37А4-0531 | 1,25G | BiDi LC，多模 | Tx:1550nm/Rx:1310nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-16А4-0531 | 1,25G | BiDi LC，多模 | Tx:1310nm/Rx:1550nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-1354-0531 | 1,25G | 双 LC，多模 | 1310nm | RB2011LS-IN | 可用！ |
| AXCEN | AXGD-5854-0511 | 1,25G | 双 LC，多模 | 850nm | RB2011LS-IN | 可用！ |
| TP-Link | TL-SM311LS | 1,25G | 双 LC，单模 | 1310nm | RB2011LS-IN | 可用！ |
| TP-Link | TL-SM311LM | 1,25G | 双 LC，多模 | 850nm | CCR1036 12G-4S | 可用！ |
| OPTIC | OPTIC-SFP-3524S-02-SC | 1,25G | BiDi SC，单模 | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-5324S-02-SC | 1,25G | BiDi SC，单模 | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-S1203-L3302-LC | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1550nm | RB2011UAS-RM, RB260GS | 可用！ |
| OPTIC | OPTIC-SFP-S1205-L3302-LC | 1,25G | BiDi LC，单模 | Tx:1550nm/Rx:1310nm | RB2011UAS-RM, RB260GS | 可用！ |
| ROBOFiber | SFP-7120-55 | 1,25G | 双 LC，单模 | 1550nm | CCR1036-12G-4S, RB2011 | 可用！ |
| ROBOFiber | SFP-7120-WA | 1,25G | BiDi LC，多模 | Tx:1490nm/Rx:1550nm | CCR, RB2011 | 可用！ |
| ROBOFiber | SFP-7120-WB | 1,25G | BiDi LC，多模 | Tx:1550nm/Rx:1490nm | CCR, RB2011 | 可用！ |
| Enguity | SFP-3647603KM.b1310 XT | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1550nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647603KM.b1550 XT | 1,25G | BiDi LC，单模 | Tx:1550nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647610KM.b1490 XT | 1,25G | BiDi LC，单模 | Tx:1490nm/Rx:1550nm | CCR, RB2011, RB260GS | 可用！ |
| Enguity | SFP-3647610KM.b1550 XT | 1,25G | BiDi LC，单模 | Tx:1550nm/Rx:1490nm | CCR, RB2011, RB260GS | 可用！ |
| AdvOptics MSA | GLC-SX-MM | 1,25G | BiDi LC，多模 | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| AdvOptics MSA | GLC-ZX-SM | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1310nm | CCR, RB2011, RB260GS | 可用！ |
| Proline | GLC-BX-D20-PRO | 1,25G | BiDi LC，单模 | Tx:1490nm/Rx:1310nm | CRS125 | 可用！ |
| Proline | GLC-BX-D40-PRO | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1490nm | CRS125 | 可用！ |
| Foundry Networks | E1MG-BXU-AC | 1,25G | BiDi LC，单模 | Tx:1310nm/Rx:1490nm | RB3011UiAS, hAP ac | 可用！ |
| Avago | SFBR-5799APZ | 1,25G | 双 LC，多模 | 850nm | CRS326, CRS112 | 在 1Gbps 模式下可用！ |
| Eltex | NTU-SFP-100 | 1,25G | SC | 不适用 | RB4011iGS+ | 可用！ |

</WideTable>

## SFP+ 模块

<WideTable>

| 品牌 | 型号 | 距离 | 速率 | 连接器/线缆类型 | 波长 | 测试设备 | 可用/不可用 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| MikroTik | S+85DLC03D | 300m | 10G | 双 LC，多模 | 850nm | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+31DLC10D | 10km | 10G | 双 LC，单模 | 1310nm | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+23LC10D | 10km | 10G | BiDi LC，单模 | Tx:1270nm/Rx:1330nm | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+32LC10D | 10km | 10G | BiDi LC，单模 | Tx:1330nm/Rx:1270nm | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+DA0001 | 1m | 10G | Twinax 铜缆 | 不适用 | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+DA0003 | 3m | 10G | Twinax 铜缆 | 不适用 | 所有带 SFP/SFP+ 接口的 MikroTik 产品 | 原生支持 |
| MikroTik | S+RJ10 | 因链路速率而异。详情请查看宣传册 | 10G/5G/2.5G/1G/100M/10M | RJ45 - Cat5E/Cat6/Cat7 | 不适用 | 所有带 SFP+ 接口的 MikroTik 产品 | 原生支持 |
| Atop | APSP55B30CDL40 | 40km | 10G | 双 LC，单模 | 1550nm | 带 SFP+ 接口的 CRS 系列、CCR 系列设备 | 不可用！ |
| Cisco | SFP-10G-LR | 10km | 10G | 双 LC，单模 | 1310nm | RB2011LS-IN | 可用！ |
| Dell (Finisar) | FTLX8571D3BCL | 300m | 10G | 双 LC，多模 | 850nm | 大多数 SFP/SFP+ MikroTik 产品 | 可用！ |
| Juniper (Finisar) | FTLX8571D3BCL-J1 | 300m | 10G | 双 LC，多模 | 850nm | 大多数 SFP/SFP+ MikroTik 产品 | 可用！ |
| Intel (Finisar) | FTLX8571D3BCV-IT | 300m | 10G | 双 LC，多模 | 850nm | 大多数 SFP/SFP+ MikroTik 产品 | 可用！ |
| OEM (Juniper?) | EX-SFP-10GE-SR-OEM | 300m | 10G | 双 LC，多模 | 850nm | 大多数 SFP/SFP+ MikroTik 产品 | 可用！ |
| Fiberstore | SFP-10G31-40 | 40km | 10G | 双 LC，单模 | 1310nm | 带 SFP+ 接口的 CRS 系列、CCR 系列设备 | 可用！ |
| Fiberstore | SFP-10G55-40 | 40km | 10G | 双 LC，单模 | 1310nm | 带 SFP+ 接口的 CRS 系列、CCR 系列设备 | 可用！ |
| Fiberstore | SFP-10G32-40 | 40km | 10G | BiDi LC，单模 | Tx:1330nm/Rx:1270nm | 带 SFP+ 接口的 CRS 系列、CCR 系列设备 | 可用！ |
| Fiberstore | SFP-10G23-40 | 40km | 10G | BiDi LC，单模 | Tx:1270nm/Rx:1330nm | 带 SFP+ 接口的 CRS