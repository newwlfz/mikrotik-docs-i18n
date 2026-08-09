# Netinstall

> 本页介绍 Netinstall，即 MikroTik 用于安装和重新安装 RouterOS 的实用工具，帮助您在 Windows、Linux 和 Netinstall 软件包方法之间进行选择，并描述使用 Etherboot 模式的常见设备安装工作流程。

# Netinstall

Netinstall 是一款用于在 MikroTik 设备上安装和重新安装 RouterOS 的实用工具。它可用于恢复无法访问的设备、执行全新安装，或在系统损坏或配置错误时重新安装 RouterOS。

该工具适用于 Windows（图形界面）和 Linux（命令行）。从 RouterOS 7.24beta1 开始，**Netinstall 软件包**可用于除 SMIPS 设备之外的所有 MikroTik 架构。

## 选择 Netinstall 方法

选择适合您环境的安装方法：

- [**Windows Netinstall**](./netinstall-windows.md) - 适用于 Windows 系统的图形界面。
- [**Linux Netinstall**](./netinstall-linux.md) - 适用于 Linux 系统的命令行工具。
- [**Netinstall 软件包**](./netinstall-package.md) - 一种 RouterOS 软件包，可直接在受支持的 MikroTik 设备上启用 Netinstall 功能。

您可以从 [MikroTik 下载页面](https://mikrotik.com/download) 下载 Netinstall 工具和 RouterOS 软件包。

:::danger
Netinstall 会重新格式化系统驱动器，这将擦除所有配置数据和用户文件。

Netinstall 不会移除 RouterOS 许可证密钥，也不会重置 RouterBOOT 设置。例如，重新安装期间 CPU 频率保持不变。
:::

## 使用 Netinstall 的设备安装工作流程

以下工作流程适用于所有 Netinstall 方法。

### 准备 Netinstall 主机

在与待重新安装设备位于同一 Layer 2 (L2) 网络网段的计算机或 MikroTik 路由器上启动 Netinstall。为获得最佳效果，请使用专用网络接口和简单的交换机或集线器，以避免 IP、DHCP 或 BOOTP 冲突。

### 将设备启动至 Etherboot 模式

Etherboot 模式是 MikroTik 设备上的一种特殊启动状态，允许您使用 Netinstall 重新安装 RouterOS。

有两种启动器选项可用：**常规启动器** 和 **备份启动器**。建议同时验证这两种选项，以防其中一种无法正常工作。

- **常规启动器：** 要使用串行控制台进入 Etherboot 模式，请按住 <kbd>Control</kbd>+<kbd>E</kbd>。或者，在设备通电并等待 1–2 秒后，按下 **Reset** 按钮。

- **备份启动器：** 关闭设备电源。按住 **Reset** 按钮，然后打开设备电源。等待 **LED** 序列（闪烁 → 常亮 → 熄灭），然后松开按钮。设备将启动至 **BOOTP** 模式，准备通过 Netinstall 重新安装 RouterOS。根据型号不同，这可能会通过 **USR、USER、System** 或 **ACT** LED，或 SFP 端口 LED 来指示。

### 安装设备

使用 Netinstall 安装带有所需软件包、参数和配置脚本的 RouterOS。

## 其他参考

- [RouterOS 配置管理](../../configuration-management/index.md)
- [RouterOS 软件包](../packages.md)
- [RouterBOOT 配置](../routerboot.md)
- [MikroTik 下载](https://mikrotik.com/download)