# FlashFig

> FlashFig 是一款 Windows 实用工具，用于通过 Layer-2 网络在数秒内向 MikroTik RouterBOARD 快速批量传输 RouterOS 配置。它支持闪存启动模式以实现自动化配置，并提供了在旧型号上启用该模式及使用脚本的详细说明。

# FlashFig

### 描述

FlashFig 是一款基于 Windows 的实用工具，专为 MikroTik RouterBOARD 的高批量配置而设计。它旨在供 MikroTik 分销商、互联网服务提供商以及其他需要快速向多台设备部署 RouterOS 配置的组织使用。

当 RouterBOARD 处于闪存启动模式并在包含 FlashFig 的 Layer-2 广播域中通电时，该应用程序会在约三秒内将目标 RouterOS 配置文件传输到设备。因此，只需将每台 RouterBOARD 连接到同一 Layer-2 网络并为启用 FlashFig 的设备供电，即可同时配置一批路由器。

FlashFig 实用工具可从 MikroTik [下载](https://mikrotik.com/download) 页面获取。

自 2010 年 3 月起生产的所有 RouterBOARD 设备默认启用 FlashFig 模式。对于旧型号，可通过 [RouterBOARD](../hardware/routerboard.md#settings) 设置或 RouterOS 控制台命令将 *boot-device* 设置为 `flash-boot` 或 `flash-boot-once-then-nand` 来激活 FlashFig：*`/system/routerboard/settings/set boot-device=flash-boot-once-then-nand`* 或 *`/system/routerboard/settings/set boot-device=flash-boot`*。

:::info
从 RouterOS/RouterBOOT **v7.16** 开始，每次从软件发起系统重置后，闪存启动模式将像出厂时一样被启用。当您使用重置按钮重置路由器时，也会启动相同的模式（需要引导加载程序版本 v7.16 或更高）。
请注意，如果您在路由器通电前按住重置按钮，则会使用备份引导程序。备份引导程序固件（出厂时安装）也必须为 v7.16 或更高版本。
:::

全新 RouterBOARD 上的 FlashFig 模式仅在首次成功用户登录或 FlashFig 尝试成功后才在后续启动中禁用，以避免日后发生不必要的重新配置。要在同一台路由器上第二次使用 FlashFig，您需要在 [RouterBOARD](../hardware/routerboard.md#settings) 设置中启用 **flash-boot**（此设置将在成功配置更改或任何用户登录设备后恢复为 NAND）。

如果稍后使用 RouterOS *reset-configuration* 命令（或使用重置按钮进行配置重置），则会加载 FlashFig 配置。要永久覆盖，请使用 Netinstall 过程并勾选 *Apply default configuration*，或在基于 Linux 的命令行中使用 *-r* 标志。

从 RouterOS/FlashFig 7.22 开始，可以使用 Mode 脚本配置 **device-mode** 和 **protected-routerboot** 及其他设置。Mode 脚本在任何自定义或默认配置脚本之前执行。执行完成后，脚本会自动从设备中移除。如果脚本修改了设备模式，设备将在执行后立即重启。

您可以在 MikroTik YouTube 频道上观看 FlashFig [视频教程](https://www.youtube.com/watch?v=gticPeOdN54)。

### FlashFig 示例

这是一个逐步示例，演示如何使用 FlashFig 流程将选定的 MikroTik RouterOS 配置应用到“出厂全新”的 RouterBOARD。

##### 要求

Windows 计算机必须配备以下端口并包含以下文件：

- 一个可用的以太网端口。
- 有效的 *Config* 和/或 *Mode* 脚本文件，包含类似于 [导出/导入文件](../getting-started/configuration-management/index.md#configuration-export-and-import) 的 MikroTik RouterOS 配置。除了有效的 MikroTik RouterOS CLI 命令外，还可以通过使用只读变量 *$defconfPassword* 和 *$defconfWifiPassword* 重新应用出厂密码；
- 始终使用 [下载](https://mikrotik.com/download) 页面提供的最新 FlashFig 程序。
- RouterBOARD 必须处于闪存启动模式。如果这是首次启动，则无需进行任何操作。

:::info
请注意文本编辑器对 CR/LF 字符的处理方式，并在通过 FlashFig 应用之前，测试配置在相同版本的 RouterOS 上正常应用时没有错误，因为运行时错误将不可见！
:::

##### 预配置

###### Windows 计算机

- 运行 FlashFig。
- 准备 *Config* 和/或 *Mode* 脚本 **.rsc** 文件。*Config* 和/或 *Mode* 脚本文件是 [常规/导入文件](../getting-started/configuration-management/index.md#configuration-export-and-import)，它接受有效的 MikroTik RouterOS CLI 命令。您可以使用任何文本编辑器程序（记事本、Notepad++、文本编辑器、TextEdit、Microsoft Word、OpenOffice Writer）创建 .rsc 文件。

![](img/editor_1.png)

- 分配 **Boot Client Address**，该地址应位于 *与计算机以太网接口配置相同的子网内*。

![](img/flashfig_1.png)

- **浏览** 选择 *Config* 和/或 *Mode* 脚本 **.rsc** 文件

![](img/flashfig_2.png)

- 高亮 *Config* 脚本文件并 **选择 Config**，高亮 *Mode* 脚本文件并 **选择 Mode**。

![](img/flashfig_3.png)

- 激活 FlashFig 服务器。现在它已准备好进行 FlashFig。注意：任何在网络上通电且 boot-device 配置为 **flash-boot** 或 **flash-boot-once-then-nand** 的 RouterBOARD 都将被 FlashFig。

![](img/flashfig_4.png)

##### RouterBOARD

- 每台 RouterBOARD 出厂时默认启用 FlashFig 模式，这意味着 RouterBOARD **无需配置**。

- 如果您的路由器未启用 FlashFig，请使用 WinBox/控制台访问 RouterBOARD，并将 [boot-device](../hardware/routerboard.md#settings) 更改为 *flash-boot* 或 *flash-boot-once-then-nand*：

```ros
/system/routerboard/settings/set boot-device=flash-boot
```

或者使用更推荐的单次启动闪存启动选项：

```ros
/system/routerboard/settings/set boot-device=flash-boot-once-then-nand
```

您的路由器现已准备好进行 FlashFig。

##### 连接

将 RouterBOARD 的 ***Boot*** 端口和 FlashFig 计算机连接到同一局域网。

##### 运行 FlashFig

- 为 RouterBOARD 接通电源。
- 检查 FlashFig 程序的状态。

![](img/flashfig_5.png)

消息日志显示“Flashfigged”，RouterBOARD 应反复发出字符“/”的莫尔斯电码声音（“\_..\_.”并闪烁 LED）——现在可以安全地拔掉电源/关闭路由器：

- FlashFig **配置**已应用到 RouterBOARD，并且它**已准备好**以新配置投入生产使用。

### 故障排除

#### FlashFig 找不到路由器

如果 PC 和路由器之间存在其他设备（路由器/交换机），请确保该设备：

- DHCP 服务器已禁用。
- 如果使用的端口位于桥接中，请将桥接 *protocol-mode* 设置为 *none*。
- 所用端口的 HW-offload 已禁用。

#### FlashFig 找到路由器，但未进行刷写（无 TFTP 请求）

确保运行 FlashFig 的计算机只有一个活动的网络接口。

#### FlashFig 完成，但配置未应用

如果所有过程均成功，但 .rsc 文件中的 RouterOS 配置未应用，请向 \*.rsc 配置文件添加 [启动延迟](../getting-started/configuration-management/index.md#startup-delay)。原因可能是配置脚本在所有接口启动之前执行。

#### 闪存空间不足，忽略

FlashFig 配置文件的最大大小为 4000 字节，否则程序将返回上述错误。