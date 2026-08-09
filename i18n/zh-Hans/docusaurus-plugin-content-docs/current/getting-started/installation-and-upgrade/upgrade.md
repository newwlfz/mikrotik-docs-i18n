# 升级

> 本文档介绍 MikroTik 设备的 RouterOS 升级流程，涵盖通过发布链（长期版、稳定版、测试版、开发版）进行自动更新、通过 WinBox/WebFig/FTP 进行手动升级，以及引导加载程序升级建议。文中解释了版本编号约定、更新工作流程以及关键安全步骤的故障排除警告。

import DocCardList from '@theme/DocCardList';

# 升级

MikroTik 设备预装了 RouterOS，因此通常无需安装，除非是在裸机 x86 PC 或通过 CHR 镜像在虚拟机上安装 RouterOS。对于已安装设备的升级过程则非常简单。

## 版本编号

RouterOS 版本号使用句点分隔序列时按顺序编号；它*不*代表小数点，且序列*不*具有位置意义。例如，标识符 2.5 并非“二点五”或“距离版本三还有一半”；它是第二个第一级修订版的第五个第二级修订版。因此，v5.2 比 v5.18 旧，而 v5.18 更新。

RouterOS 版本通过多个“发布链”发布：长期版、稳定版、测试版和开发版。升级 RouterOS 时，您可以选择一个发布链来安装新软件包：

- **长期版**：发布频率低，仅包含最关键的错误修复。同一数字分支内的升级不包含新功能。当**稳定版**发布一段时间且足够稳定后，会被提升至长期分支，替换旧版本，旧版本随后移至存档。这会持续添加新功能。
- **稳定版**：每隔几个月发布，包含所有经过测试的新功能和修复。
- **测试版**：每隔几周发布，仅经过基本的内部测试，不应在生产环境中使用。
- **开发版**：按需发布。包含原始更改，可供软件爱好者测试新功能。

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-01.webp)</center>

**子菜单：** `/system/package/update`

### 命令

| 属性 | 描述 |
| :-- | :-- |
| **check-for-updates** | 检查 MikroTik 下载服务器上所选发布通道中是否有更新的 RouterOS 版本。|
| **download** | 下载最新的可用 RouterOS 软件包但不安装。需要手动重启才能应用更新。|
| **install** | 下载并安装最新的可用 RouterOS 软件包，随后自动重启。 |
| **cancel** | 取消待处理的更新下载或安装。 |

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **channel** (*long-term \| stable \| testing \| development*; 默认值：**stable**) | 检查新 RouterOS 版本时使用的发布通道。 |
| **mode** (*https \| http*; 默认值：**https**) | 连接 MikroTik 下载服务器时使用的协议。 |
| **check-certificate** (*yes \| no \| yes-without-crl*; 默认值：**yes**) | 是否验证服务器 SSL 证书。`yes-without-crl` 可用于跳过 CRL 验证。 |
| **ip-version** (*auto \| ipv4 \| ipv6*; 默认值：**auto**) | 连接 MikroTik 下载服务器时的 IP 版本偏好。 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **installed-version** (*string*) | 当前安装的 RouterOS 版本。 |
| **latest-version** (*string*) | 所选通道中可用的最新 RouterOS 版本。 |
| **status** (*string*) | 更新过程的当前状态（例如，`New version is available`）。 |

## 标准升级

软件包升级功能通过 HTTPS（自 v7.23 起）从路由器连接到 MikroTik 下载服务器，并检查所选发布通道中是否有更新的 RouterOS 版本。此菜单也可用于降级，只需将通道更改为提供较旧但更稳定版本的通道。请注意，该功能是从路由器（而非您的计算机）发起连接，因此路由器本身需要能够通过 HTTPS 连接到 MikroTik 服务器。请确保路由器前置的任何防火墙允许 TCP 端口 443。

在 QuickSet 或 System → Packages 菜单中点击 *Check for Updates* 按钮后，将打开 *Check for Updates* 窗口，显示当前更新日志或最新更新日志（如果存在更新版本）。如果有更新版本可用，将出现 *Download* 和 *Download&Install* 按钮。点击 *Download* 会下载最新版本（需要手动重启设备），而点击 *Download&Install* 则开始下载并在下载成功后自动重启设备。

提供的版本取决于所选的发布通道。并非所有版本都可用。使用 check-for-updates 方法时，无法一步从旧版本升级到最新版本。例如，如果运行的是 RouterOS v6.x，即使选择名为“Upgrade”的主版本升级通道，也只能看到 v7.12.1 作为可用版本。您必须先升级到该中间版本，然后才能在通道中看到更新的版本。此中间步骤也可以使用 check for updates 完成；只需在首次更新到中间版本后重复 check for updates 即可。

如果安装了自定义软件包，下载器会考虑这一点并下载所有必要的软件包。

:::warning
强烈建议在 RouterOS 更新后升级引导加载程序。要升级引导加载程序，请在 CLI 中执行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard.md#systemrouterboardupgrade) 命令，然后重启。或者，导航至 GUI 的 System → RouterBOARD 菜单，点击“Upgrade”按钮，然后重启设备。
:::

您可以通过在系统计划任务中运行脚本来自动化升级过程。此脚本查询 MikroTik 升级服务器以获取新版本。如果收到的响应显示“New version is available”，则脚本会发出以下升级命令。重要提示：如果您在较旧版本上首次运行此脚本，它将无法正常工作。它可能无法看到最新版本可用，如果您运行的是 v6.x，则必须先手动选择“Upgrade”通道以执行主版本升级到 v7.12.1 中间版本，之后更新的 v7 版本才会在升级通道中可见。

```ros
/system/package/update/check-for-updates
:delay 3s;
:if ( [/system/package/update get status] = "New version is available") do={ /system/package/update/install }
```

## 手动升级

您可以通过以下方式升级 RouterOS：

- WinBox – 将文件拖放到 Files 菜单。
- WebFig - 从 Files 菜单上传文件。
- FTP - 将文件上传到根目录。

:::warning
强烈建议在升级 RouterOS 后升级引导加载程序。要升级引导加载程序，请在 CLI 中执行 [`/system/routerboard/upgrade`](../../cli-reference/system/routerboard.md#systemrouterboardupgrade) 命令，然后重启。或者，导航至 GUI 的 System → RouterBOARD 菜单，点击“Upgrade”按钮，然后重启设备。

**警告：** RouterOS 无法通过串行电缆升级。只有 [RouterBOOT](./routerboot.md#simple-upgrade) 可以使用此方法升级。
:::

### 手动升级过程

- 访问 [www.mikrotik.com](http://www.mikrotik.com) 并前往 Software 页面，然后选择您安装 RouterOS 的系统的架构（系统架构可在 System → Resource 部分找到）。
- 下载 **routeros *(主)* ** 软件包以及设备上安装的额外软件包。
- 使用前述方法之一将软件包上传到设备。

如果您需要跳过某个特定软件包的升级，或者某个软件包文件不再可用，则使用 [`/system/package/update/install ignore-missing`](../../cli-reference/system/package/package.md#systempackageupdateinstall) 来跳过缺失的软件包。

#### 使用 WinBox

选择您的系统类型，并下载升级软件包。使用 WinBox 连接到您的路由器。用鼠标选择下载的文件，并将其拖到 Files 菜单。如果已存在某些文件，请确保将软件包放在根菜单中，而不是 hotspot 文件夹内！上传将开始。

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-02.webp)</center>

上传完成后 - 重启设备。新版本号将显示在 Winbox 标题和 Packages 菜单中。

#### 使用 S/FTP

- 打开您常用的 S/FTP 程序，选择软件包，并将其上传到您的路由器。
- 如果您愿意，可以检查文件是否成功传输到路由器（可选）。

```ros
[admin@MikroTik] >/file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                  TYPE       SIZE     CREATION-TIME       
0  routeros-7.9-arm.npk  package    13.0MiB  2023-05-18 16:16:18
1  pub                   directory           2022-11-04 11:22:19
2  ramdisk               directory           1970-01-01 03:00:24
```

- 重启您的路由器以开始升级过程。

```ros
[admin@MikroTik] >/system/reboot
Reboot, yes? [y/N]: y

```

- 重启后，您的路由器将是最新版本，您可以在以下菜单中查看：

```ros
/system/package/print

```

- 如果您的路由器未正确升级，请务必检查**日志**

```ros
/log/print without-paging

```

## RouterOS 本地升级

您可以通过在一台拥有所有必要软件包的设备上使用 [`/system/package/local-update`](../../cli-reference/system/package/package.md#systempackagelocal-update) 工具，升级本地网络中的一台或多台 MikroTik 路由器。以下是一个包含 3 台路由器的简单示例（相同方法适用于具有任意数量路由器的网络）：

- 将所需软件包放在主路由器的 Files 菜单下：

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-03.webp)</center>

**可选**，您可以在主设备之间设置镜像设备，如果不需要，请跳过此步骤：

- 选择 Local Package Sources 并启用 Mirror device。设置软件包所在的主服务器，10.155.136.50。Check Interval **最小** 设置可设为 00:07:12，设备将在此时间间隔内使用 Winbox 连接到主设备并检查软件包。  
  如果有新软件包可用，它将开始下载，请注意下载过程较慢，当使用大量文件时可能需要一些时间。如果发生某些故障，下载将在下次 Check 时恢复。

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-04.webp)</center>

- 将创建一个新的 `packs` 文件夹，镜像设备将在其中存储软件包：

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-05.webp)</center>

- 在将要更新的设备上添加新的软件包源，在此示例中，我们使用镜像设备 10.155.136.71：

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-06.webp)</center>

- 一旦您在 Local Update packages 选项卡中点击 **Refresh**，使用 Winbox 的设备将尝试连接到源并检查是否有新软件包。

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-07.webp)</center>

- 选择软件包并点击 **Download**，下载完成后，设备将需要重启以进行更新。

<center>![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/img/upgrade-08.webp)</center>

- 使用 `/system/package/local-update/refresh` 在您的脚本中自动化此过程。Fetch 工具可用于从我们的网页下载软件包，例如：

```ros
/tool/fetch url=https://download.mikrotik.com/routeros/7.16.1/routeros-7.16.1-arm.npk
```