# 适用于 Linux 的 Netinstall

> 本文档介绍 netinstall-cli，即 MikroTik Netinstall 工具的 Linux 命令行版本，涵盖单台及多台设备重装的所有命令行选项、脚本与配置标志、网络选项，以及分步安装示例。

# 适用于 Linux 的 Netinstall

Netinstall 的 Linux 版本 `netinstall-cli` 是一款命令行工具，其功能与 Windows 版本几乎完全相同。

:::tip
在运行 netinstall 工具之前，请确保已在计算机的网卡接口上设置静态 IP 地址。

```bash
sudo ip addr add 192.168.88.2/24 dev <interface>
sudo ip link set <interface> up
```

:::

:::info
此工具需要 root 权限。您必须以 root 身份运行，或使用 `sudo` 来执行它。
:::

## netinstall-cli 命令行选项

`netinstall-cli` 命令语法如下：

```
netinstall-cli [-r] [-e] [-b] [-m [-o]] [-f] [-c] [-v] [--reboot] [--shutdown] [-k <keyfile>] [-s <userscript>] [-sm <modescript>] [--mac <mac address>] {-i <interface> | -a <client-ip>} [PACKAGE]+ 
```

## 常规选项

| 参数 | 说明 |
| :-- | :-- |
| **-r** | 重装设备并应用默认配置脚本。 |
| **-e** | 重装设备但不应用默认配置脚本，使设备保持空配置状态。 |
| **-b** | 丢弃设备当前安装的品牌包。若未指定，则保留品牌包。出厂预装的品牌包无法丢弃，将始终保留。 |
| **-f** | 忽略存储容量限制。默认情况下，netinstall-cli 会检查路由器的存储容量。若所选软件包总大小超过可用存储空间，将显示错误：**"Ignoring XX:XX:XX:XX:XX:XX, not enough space (override with -f)"** |
| **-c** | 允许在同一台计算机上同时运行多个 Netinstall 实例。 |
| **-v** | 启用详细输出模式。 |

### 多设备重装选项

| 参数 | 说明 |
| :-- | :-- |
| **-m** | 启用多设备重装。只要收到 BOOTP 请求，同一设备将被重复重装。 |
| **-o** | 限制每次 Netinstall 运行仅安装一次。工具会跟踪已成功安装设备的 MAC 地址，并在当前会话中忽略来自同一 MAC 地址的后续 BOOTP 请求。 |

**组合行为：**

- 未指定 `-m` 且未指定 `-o`：仅执行一次成功安装，然后 Netinstall 关闭。
- 仅指定 `-m`：启用多次重装；同一设备将反复重装。
- 仅指定 `-o`：与未指定标志相同；每次运行仅安装一次，然后关闭。
- 同时指定 `-m` 和 `-o`：启用多次重装，但每台设备在每次会话中仅安装一次。

### 脚本与配置选项

| 参数 | 说明 |
| :-- | :-- |
| **--reboot** | 重启选定的、已引导至 Netinstall 模式的 MikroTik 设备。 |
| **--shutdown** | 关闭选定的、已引导至 Netinstall 模式的 MikroTik 设备。 |
| **-k \<keyfile>** | 向设备提供 .KEY 格式的许可证密钥文件（可选）。 |
| **-s \<userscript>** | 允许在安装过程中向设备安装自定义默认配置脚本。此脚本将替换 RouterOS 自带的默认配置脚本。参见 `/system/default-configuration/custom-script/print`。该脚本在 RouterOS 更新期间会被保留，并在后续配置重置后继续使用，直到设备使用新脚本重新安装或该脚本被移除。 |
| **-sm \<modescript>** | 指定一个一次性自定义脚本，在设备安装后首次启动时执行。用于配置设备模式（device-mode）、受保护的路由器引导（protected-routerboot）及其他部署设置。模式脚本在任何自定义或默认配置脚本之前运行，并在执行后自动移除。若脚本修改了设备模式，设备将立即重启。**需要 RouterOS 和 Netinstall 版本 7.22 或更高版本。** |

### 网络选项

| 参数 | 说明 |
| :-- | :-- |
| **--mac \<mac address>** | 指定允许安装的 MAC 地址。提供后，所有其他 BOOTP 请求将被忽略。 |
| **-i \<interface>** | 指定用于安装的网络接口（可选，推荐使用）。 |
| **-a \<client-ip>** | 指定 Netinstall 服务器分配给设备的特定 IP 地址。除非使用 `-i` 参数（允许自动分配），否则此参数为必填项。 |

### 软件包选择

| 参数 | 说明 |
| :-- | :-- |
| **PACKAGES** | 指定要安装到设备上的 .NPK 格式 RouterOS 软件包列表。此参数为必填项。**系统软件包（system package）必须列在首位。** |

:::warning
**配置保留行为：**

当未指定 `-r` 或 `-e` 时，netinstall-cli 将重装 RouterOS 并保留当前配置。它会从路由器下载现有配置数据库，在重装过程中重新格式化磁盘，然后将配置上传回设备。这与 Netinstall 图形界面中的 **"Keep old configuration"（保留旧配置）** 选项一致。

注意：此过程仅适用于配置本身。用户管理器数据库、Dude 数据库及其他单独存储的数据文件不在保留范围内。
:::

## Linux Netinstall 示例

从 [MikroTik 下载页面](https://mikrotik.com/download) 下载该工具：

```bash
wget https://download.mikrotik.com/routeros/[VERSION]/netinstall-[VERSION].tar.gz
```

解压归档文件：

```bash
tar -xzf netinstall-[VERSION].tar.gz
```

配置网络接口（将 eth0 替换为您的接口名称）：

```bash
sudo ip link set eth0 down
sudo ip addr add 192.168.88.2/24 dev eth0
sudo ip link set eth0 up
```

运行安装。该工具需要 root 权限，请使用 sudo：

```bash
sudo ./netinstall-cli [-parameters] [address/interface] routeros-[architecture]-[package VERSION].npk
```

```bash
sudo ./netinstall-cli -i eth0 -v -e  routeros-7.23.1-arm64.npk wifi-qcom-7.23.1-arm64.npk container-7.23.1-arm64.npk 
Version: 7.24beta1(2026-05-26 11:17:51)
Will apply empty config
Waiting for Link-UP on eth0
Using client IP 192.168.88.3
Waiting for RouterBOARD...
Received a BOOTP request from 01:23:45:67:89:AA (arm64)
Assigned 192.168.88.3 to 01:23:45:67:89:AA
blksize 1452
Booting device 01:23:45:67:89:AA into setup mode
Formatting device 01:23:45:67:89:AA
Sending packages to device 01:23:45:67:89:AA
Packages sent to device 01:23:45:67:89:AA
Rebooting device 01:23:45:67:89:AA
Successfully finished installing device 01:23:45:67:89:AA
```

:::tip
正在寻找其他安装方法？请参阅 [**Windows**](./netinstall-windows.md) 或 [**Netinstall 软件包**](./netinstall-package.md) 的说明。
:::