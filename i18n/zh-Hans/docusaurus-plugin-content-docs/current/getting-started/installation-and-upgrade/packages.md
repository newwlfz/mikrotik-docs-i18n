# 软件包

> RouterOS 将功能组织为带有 `.npk` 扩展名的软件包，包括核心的 routeros 捆绑包以及 Containers 或 The Dude 等可选附加组件。无线设备根据硬件不同需要特定的软件包，安装方法包括手动下载和直接从路由器更新。

# 软件包

## 概述

RouterOS 的功能被组织为软件包，这些软件包是带有 `.npk` 扩展名的文件。大多数功能都捆绑在 ***routeros*** 软件包中，而某些功能则作为单独的软件包提供。安装额外的 `.npk` 软件包可以启用特定功能，例如 Containers 或 The Dude。软件包文件仅由 MikroTik 提供，第三方无法创建。您可以从我们的下载页面下载额外的软件包，或者直接从您的路由器中添加。

## 最低要求

RouterOS 仅需系统软件包即可在最低限度下运行，但对于大多数设备，当您安装“routeros”捆绑软件包时，即可获得标准操作和功能。

对于无线设备，根据您使用的硬件，有多个无线软件包可用：

- 从 RouterOS 7.13 开始，基本家庭路由器的运行需要 ***routeros***（系统）软件包以及以下无线软件包之一：
  1. 802.11ax WiFi AP 需要无线电驱动程序，该驱动程序由 ***wifi-qcom*** 软件包提供（对于早于 7.13 的 RouterOS 版本，它被称为 *wifiwave2* 软件包）。
  2. 上一代 WiFi AP 需要 ***wireless*** 软件包。

有关使用哪个无线软件包的更多信息，请参阅 [无线手册](../../wireless/index.md)。

其他软件包是可选的，家庭路由器不需要。仅在您确定其用途时才安装它们。

## 安装软件包

### 手动下载

要手动下载并安装额外的软件包，请从 [MikroTik 下载](https://mikrotik.com/download) 页面下载所需的软件包，根据您在 System/Resources 菜单中找到的设备架构选择 RouterOS 部分。解压归档文件，并使用任何便捷的方法将所需的软件包上传到您的路由器，然后继续重启路由器。

### 直接从路由器下载

您可以通过使用 *System Packages* 部分直接从路由器下载并安装额外的软件包。

1. 执行 ***Check For Updates*** 命令后，可用的软件包将列在 *Packages* 列表中，但它们会显示为禁用状态。可用软件包列表来自 MikroTik 下载服务器。这些软件包是可用的，但尚未在您的路由器上（如标志 X（禁用）和 A（可用）所示）。
2. 要下载额外的软件包，首先选择该软件包并选择 ***Enable***。
3. 要使路由器下载该软件包，请选择 ***Apply Changes***，设备将要求重启。

| 软件包列表 | 使用“Check for updates”加载列表后 | 启用软件包 | 选择“Apply Changes” |
| :--- | :--- | :--- | :--- |
| [![](img/packages1.png)](img/packages1.png) | [![](img/packages2.png)](img/packages2.png) | [![](img/packages3.png)](img/packages3.png) | [![](img/packages4.png)](img/packages4.png) |

### 安装验证

为确保软件包安装成功，请在设备重启后检查“Log”部分。如果软件包安装成功，您将看到相关消息。如果存在冲突或某些要求未满足，将对此进行说明，以便您采取进一步措施进行纠正。

![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/packages-01.webp)日志条目中的成功信息![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/packages-02.webp)日志条目中的失败信息

### 系统软件包

| **软件包** | 描述 |
| :--- | :--- |
| **routeros-arm** (*arm*) | 适用于 arm 设备的系统软件包。 |
| **routeros-arm64** (*arm64*) | 适用于 arm64 设备的系统软件包。 |
| **routeros-mipsbe** (*mipsbe*) | 适用于 mipsbe 设备的系统软件包。 |
| **routeros-mmips** (*mmips*) | 适用于 mmips 设备的系统软件包。 |
| **routeros-smips** (*smips*) | 适用于 smips 设备的系统软件包。 |
| **routeros-tile** (*tile*) | 适用于 tile 设备的系统软件包。 |
| **routeros-ppc** (*ppc*) | 适用于 ppc 设备的系统软件包。 |
| **routeros** (*x86, CHR*) | 适用于 x86 安装和 CHR 环境的系统软件包。 |

### 额外软件包

| 软件包（支持的架构） | 描述 |
| :--- | :--- |
| **calea** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 针对美国“执法通信协助法案”特定用途的数据收集工具。 |
| **container** (*arm, arm64, x86, CHR*) | [Container](../../containers/index.md) Linux 容器实现，允许用户在 RouterOS 中运行容器化环境。 |
| **dude** (*arm, arm64, mmips, tile, x86, CHR*) | [Dude](../../management-tools/dude.md) 工具，用于监控网络环境。 |
| **extra-nic** (*arm64*) | ARM64 CPU 架构网络接口卡（NIC）支持，推荐用于非 MikroTik 板卡的 UEFI 安装。 |
| **gps** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [全球定位系统](../../mobile-networking/gps/index.md) 设备支持。 |
| **iot** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 启用：MQTTLoRa（适用于带有 LR8/9/2 miniPCIe 卡的设备）蓝牙（适用于带有蓝牙芯片的设备）GPIO（适用于带有 GPIO 引脚的设备）Modbus（适用于带有 RS485 端口的设备） |
| **iot-bt-extra** (*arm, arm64*) | 适用于 ARM 和 ARM64 设备的软件包，启用 USB 蓝牙适配器（必须支持 LE 4.0+）的使用。 ***注意：** 并非所有适配器都经过测试。我们无法事先保证特定适配器能够正常工作。 |
| **lora** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 用于 [LoRa](../../internet-of-things/lora/general-properties.md) 支持的虚拟软件包。LoRa 软件包不再是必需的，仅出于兼容性原因保留。LoRa 功能已移至 iot 软件包中。 |
| **lte** (*mipsbe*) | 仅适用于 SXT LTE (RBSXTLTE3-7) 的必需软件包，其中包含内置 LTE 接口的驱动程序。 |
| **rose-storage** (*arm, arm64, tile, x86, CHR*) | RouterOS 中的额外 [企业数据中心功能](../../storage/index.md)，支持磁盘监控、改进的格式化、RAID、rsync、iSCSI、NVMe over TCP、NFS 和改进的 SMB。 |
| **switch-marvell** (*arm64*) | CRS8xx 系列交换机所需的驱动程序软件包。 |
| **tr069-client** (*arm, arm64, mipsbe, mmips, smips, tile, ppc, x86, CHR*) | [TR069 客户端](../../management-tools/tr-069.md) 软件包。 |
| **ups** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [APC UPS 管理](../../system-information-and-utilities/ups.md) 接口。 |
| **user-manager** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | [MikroTik 用户管理器](../../authentication-authorization-accounting/user-manager.md) 服务器，用于控制 Hotspot 和其他服务用户。 |
| **wifi-mediatek** (*arm*) | 受支持的 MediaTek 无线硬件所需的 MediaTek WiFi 驱动程序。 |
| **wifi-qcom** (*arm, arm64*) | 802.11ax 接口所需的驱动程序软件包。在 7.13 中引入。[WiFi CAPsMAN](../../wireless/wifi/index.md#wifi-capsman) 支持随系统软件包提供。 |
| **wifi-qcom-ac** (*arm*) | 兼容的 802.11ac 接口的可选 [WiFi](../../wireless/wifi/index.md) 驱动程序软件包。在 7.13 中引入。 |
| **wifi-qcom-be** (*arm64*) | WiFi-7 802.11be 硬件所需的驱动程序软件包。 |
| **wireless** (*arm, arm64, mipsbe, mmips, tile, ppc, x86, CHR*) | 用于管理 WiFi（最高 802.11ac）和 60GHz 无线接口的实用程序和驱动程序。此软件包在 7.12 及更早版本中捆绑在 RouterOS 中。从 7.13 开始，它是一个单独的软件包。 **wireless** 软件包与 **wifi-qcom** 和 **wifi-qcom-ac** 软件包冲突 — 它们不能同时激活。 |
| **zerotier** (*arm, arm64*) | 启用 [ZeroTier](../../virtual-private-networks/zerotier.md) 功能。 |

## 自动安装

您还可以在通过 FTP 或 SFTP 将软件包上传到路由器后自动安装它们。软件包文件必须命名为带有 `*.auto.npk` 扩展名。文件上传后，路由器将自动重启以安装该软件包。这对于脚本编写和自动化非常有用。

文件名中的 `.auto.npk` 扩展名是自动安装软件包所必需的。

## 使用软件包

___

### 列出软件包

*zerotier* 软件包已禁用但已安装；*iot* 软件包在服务器上可用，但尚未下载到路由器并启用；*dude* 软件包已计划卸载。

```ros
/system/package/print 
Flags: X - DISABLED; A - AVAILABLE
Columns: NAME, VERSION, SCHEDULED, BUILD-TIME, SIZE
#    NAME            VERSION     SCHEDULED                      BUILD-TIME           SIZE  
0    wireless        7.24beta1                                  2026-05-26 10:47:52  1388.1KiB
1 X  container       7.24beta1                                  2026-05-26 10:47:52  1156.1KiB
2    routeros        7.24beta1                                  2026-05-26 10:47:52  11.0MiB  
3    zerotier        7.24beta1                                  2026-05-26 10:47:52  372.1KiB 
4 XA calea                                                                           20.1KiB  
5 XA gps                                                                             24.1KiB  
6 XA iot                                                                             788.1KiB 
7 XA openflow                                                                        76.1KiB  
8 XA tr069-client                                                                    120.1KiB 
9 XA ups                                                                             44.1KiB  
```

### 安装软件包

```ros
/system/package/enable gps,zerotier,container
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 

```

### 卸载软件包

```ros
/system/package/uninstall gps,container;
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]: 
```

### 禁用软件包

```ros
/system/package/disable container; 
/system/package/apply-changes
Apply scheduled changes and reboot device? [y/N]:
```

### 取消卸载或禁用操作

```ros
/system/package/unschedule container;
```

### 降级

```ros
/system/package/downgrade; /system/reboot;
Router will be rebooted. Continue? [y/N]: 
```