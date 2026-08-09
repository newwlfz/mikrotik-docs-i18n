# RMA 前检查清单

> 针对 MikroTik 硬件在提交保修申请前的诊断检查清单。在提交保修请求前，先排除常见的电源、启动、连接和 LTE 问题。

# RMA 前检查清单

在提交设备进行保修维修（RMA）之前，请依次完成以下检查。许多看似硬件的问题实际上是由电源、线缆、软件版本或配置引起的——这些问题无需将设备寄回即可解决。

## 电源与启动

| 症状 | 尝试方法 |
| :-- | :-- |
| 设备无法开机 | 使用其他兼容的电源适配器和/或 PoE 供电模块。 |
| 设备无法启动 | 加载备用 RouterBOOT：按住 **Reset** 按钮，给设备通电，持续按住 **Reset** 2–3 秒。如果设备能够启动，使用 `/system/routerboard/upgrade` 升级引导加载程序。如果仍然失败，使用 [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) 重新安装。 |
| 设备在负载下重启 | 尝试更换电源适配器。将 RouterOS 升级到最新的 Stable 版本。使用 `/system/reset-configuration` 重置配置。 |
| 设备在无负载时重启 | 将 RouterOS 升级到最新的 Stable 版本。使用 `/system/reset-configuration` 重置配置。 |

## 以太网与 SFP

| 症状 | 尝试方法 |
| :-- | :-- |
| 无法连接到设备 | 尝试其他端口——您可能正在使用默认配置中的 WAN 端口。检查线缆和端口是否有物理损坏。 |
| 无法进行 [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) | 确保使用直连以太网连接、处于同一子网，并关闭防火墙。尝试在 PC 和设备之间放置一台交换机。详细信息请参阅 [Netinstall 指南](../getting-started/installation-and-upgrade/netinstall/netinstall-windows.md)。 |
| 以太网端口无法建立链路 | 尝试更换以太网线缆。如果使用 PoE 供电，请尝试更换 PoE 供电模块。 |
| SFP / SFP+ / QSFP 端口无法建立链路或吞吐量低 | 确保链路两端兼容。使用正确的光缆类型（单模或多模）。验证 SFP 模块是否受支持。 |

## LTE

| 症状 | 尝试方法 |
| :-- | :-- |
| SIM 卡无法识别 | 尝试更换 SIM 卡。检查卡片方向，确保其完全插入或卡入卡槽。 |
| LTE 无法连接 | 验证 APN 是否正确。查阅您的服务提供商文档，确认所需的 APN 值。 |
| LTE 已连接但无数据传输 | 验证 APN 是否正确。确保路由和防火墙规则允许流量通过。 |
| LTE 接口缺失 | 确认设备为 LTE Kit 型号，且调制解调器已物理安装。 |
| LTE 调制解调器无法识别 | 安装最新的 RouterOS Stable 版本。 |

## 其他

| 症状 | 尝试方法 |
| :-- | :-- |
| LED 不工作 | 安装最新的 RouterOS Stable 版本并应用默认配置。 |
| 外壳弯曲或损坏 | 检查包装是否有损坏。运输造成的损坏应向运输公司报告。 |

:::info
如果上述步骤均无法解决问题，请联系 [MikroTik 支持](https://mikrotik.com/support)，并提供问题描述和 [支持输出文件（`supout.rif`）](../diagnostics-monitoring-and-troubleshooting/resource.md)。
:::