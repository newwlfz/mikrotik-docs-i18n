# Windows 版 Netinstall

> 本页介绍如何使用 Windows 上的 Netinstall 工具在 MikroTik 设备上安装或重新安装 RouterOS，涵盖先决条件、使用静态 IP 进行网络准备、以 Etherboot 模式启动设备、安装参数以及安装后步骤。

# Windows 版 Netinstall

本指南介绍如何使用 Windows 计算机上的 Netinstall 工具在 MikroTik 设备上安装 RouterOS。

## 先决条件

:::tip
在运行 netinstall 工具之前，请确保已在计算机的接口上设置静态 IP 地址。
:::

- 从 [下载](https://mikrotik.com/download) 页面下载 **Netinstall** 工具（Stable、Testing 或 Development 版本）。
- 从 [下载](https://mikrotik.com/download) 页面下载 RouterOS **系统包**，以及所有需要的或特定设备上必须使用的额外软件包（例如 wireless、wifi-qcom、container 等）。

:::tip
选择标记为 **LongTerm** 或 **Stable** 的 RouterOS 版本。选择适当的架构（ARM64、ARM、MIPSBE、TILE 等）。如果不确定，请下载适用于所有架构的 RouterOS 软件包 — Netinstall 将自动为您的设备选择正确的版本。
:::

该工具要求目标设备以 BOOTP 模式启动，以便被检测和访问。

### 可用操作和参数

| 控件/操作 | 描述 |
| :-- | :-- |
| **Net booting** | 启用、禁用和配置 Netinstall 内置 BOOTP 和 TFTP 服务器的 IP 寻址。这是使用 Netinstall 客户端对 MikroTik 设备进行网络启动所必需的。 |
| **Shutdown** | 关闭选定的以 Netinstall 模式启动的 MikroTik 设备。 |
| **Reboot** | 重新启动选定的以 Netinstall 模式启动的 MikroTik 设备。 |
| **Install** | 使用指定选项在选定的 MikroTik 设备上执行 RouterOS 安装。 |
| **Cancel** | 取消当前正在进行的安装。 |
| **Routers/Drives** | 显示可用于安装的设备。设备仅在以 Netinstall 模式启动后才会出现在此列表中。 |
| **Packages** | 允许选择包含 RouterOS 软件包文件的目录，并创建软件包集以供后续安装使用。 |

### Netinstall 参数

| 参数 | 描述 |
| :-- | :-- |
| **Auto Reboot** | 定义设备安装成功完成后执行的操作。 |
| **Software ID** | 显示当前设备的 Software ID。 |
| **Key** | 允许在安装期间指定并安装新的许可证密钥。默认情况下，Netinstall 会保留从设备检测到的许可证密钥。 |
| **Keep Old Configuration** | 指示 Netinstall 在安装后读取并恢复设备核心配置（/export; /users）。此选项不会保留用户文件、容器或类似数据。 |
| **Keep Branding** | 指示 Netinstall 在设备上存在 branding 软件包时予以保留。出厂安装的 branding 软件包无法丢弃，且始终会被保留。 |
| **Apply Default Config** | 如果启用，设备将在安装并重新启动后应用默认配置脚本。参见 `/system/default-configuration/script/print`。 |
| **Configure Script** | 允许在安装期间在设备上安装自定义默认配置脚本。这将替换 RouterOS 自带的默认配置脚本。参见 `/system/default-configuration/custom-script/print`。该脚本在 RouterOS 更新期间会被保留，并在后续配置重置后使用，直到设备使用新脚本重新安装或脚本被移除。从 RouterOS 7.10beta8 开始，该脚本可以使用只读变量 `$defconfPassword` 和 `$defconfWifiPassword` 访问出厂设置的密码。 |
| **Mode Script** | 指定一个一次性自定义脚本，该脚本在安装后设备首次启动时运行。使用此脚本在设备部署期间配置 **device‑mode**、**protected‑routerboot** 和其他设置。模式脚本在任何自定义或默认配置脚本之前执行。执行完成后，该脚本会自动从设备中移除。如果脚本修改了设备模式，设备将在执行后立即重新启动。**此功能需要 RouterOS 和 Netinstall 版本 7.22 或更新版本。** |
| **IP Address / Gateway / Baudrate** | Netinstall 会自动创建一个包含指定参数的 Configure 脚本，用于通过 IPv4 连接或串行控制台进行初始设备配置。此参数仅在安装到空配置时可用，即未指定其他配置选项时。 |

>Configure 和 Mode 脚本是[常规/导入文件](../../configuration-management/index.md#configuration-export-and-import)，接受有效的 MikroTik RouterOS CLI 命令。

## 准备计算机网络

1. 禁用计算机上的所有网络接口（WiFi、以太网、LTE 或任何其他连接），仅保留用于安装的以太网接口。Netinstall 仅支持一个活动接口。
    :::warning
    强烈建议停用所有其他网络接口，以确保 Netinstall 选择正确的网络接口。
    :::

2. 为以太网接口配置静态 IP 地址：

    - 打开 **开始** 并选择 **设置**。

    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_01.png)

    - 转到 **网络和 Internet** 并选择 **更改适配器选项**。

    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_02.png)
    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_02_2.png)

    - 右键单击 **以太网** 接口并选择 **属性**。

    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_03.png)

    - 选择 **Internet 协议版本 4 (TCP/IPv4)** 并单击 **属性**。

    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_04.png)

    - 勾选 **使用以下 IP 地址** 并配置：IP 地址 `192.168.88.1`，子网掩码 `255.255.255.0`。

    ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_05.png)

:::tip
Netinstall 也可以在本地网络上运行。在这种情况下，您可以跳过设置静态 IP 地址，但如果您不熟悉 Netinstall，强烈建议设置静态 IP 地址。
:::

## 启动 Netinstall

1. 将 Netinstall `.zip` 文件解压到方便的位置。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_06.png)
   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_07.png)

2. 确保以太网接口已连接，然后启动 `Netinstall.exe`。
   :::danger
   Netinstall 需要管理员权限。接受权限提示，Netinstall 才能正常工作。

   **提示：** 如果您严格按照本指南操作，您的计算机不应有 Internet 连接。Windows 10 可能会显示有关验证应用的警告 — 单击 **运行** 继续。
   :::

3. 在提示时允许 Netinstall 访问 **公用** 网络。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_08.png)

4. 配置 **Net booting** 设置：
   - 设置 **Client IP** 地址（必须是唯一的，且未被网络中任何其他设备使用，包括您的计算机）。
   - 使用与计算机静态 IP 相同子网但不同于计算机地址的 IP 地址。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_win10_09.png)

## 连接设备

1. 使用以太网电缆将设备直接连接到计算机（中间不要有其他设备）。
2. 将以太网电缆插入设备的 **Ether1** 端口或标记为 **BOOT** 的端口。
   :::danger
   某些计算机（尤其是 USB 以太网适配器）可能会产生额外的链路抖动，导致 Netinstall 无法检测到处于 Etherboot 模式的设备。如果发生这种情况，请在设备和计算机之间使用交换机，或使用基于 RouterOS 的路由器并设置为桥接模式。如果使用桥接模式的路由器，请禁用桥接接口上的任何 DHCP 客户端，并禁用 [Detect Internet](../../../diagnostics-monitoring-and-troubleshooting/detect-internet.md) 功能。

   Netinstall 使用 BOOTP 数据包，其端口号与 DHCP 数据包相同。如果使用交换机，请确保桥接端口未被其他网络设备阻塞。如果启用了 DHCP snooping，请在面向 Netinstall 计算机的桥接端口上启用 "trusted"。
   :::

3. 为设备上电并将其置于 Etherboot 模式。

## 安装 RouterOS

1. 等待设备出现在 Netinstall 中。

2. 选择设备并单击 **Browse**。导航到您的 RouterOS 软件包位置并按 **OK**。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_64_02.png)

3. **"Keep old configuration"** 过程会从路由器下载配置数据库，重新安装路由器（包括磁盘格式化），然后将配置上传回去。此过程仅适用于配置本身，不影响文件，包括 User Manager 数据库、Dude 数据库等数据库。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_64_041.png)

4. **"Keep branding"** 选项允许您保留设备已安装的 branding 软件包，而无需使用 Netinstall 重新安装。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_64_05.png)

   :::tip
   使用 **Configure script** 选项时，建议在配置执行之前引入[延迟](../../configuration-management/index.md#startup-delay)。
   :::

5. 选择所需的 RouterOS 软件包并按 **Install**。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_64_03.png)

6. 等待安装完成。根据 Netinstall 版本和设备的不同，可能需要手动重新启动。

   ![](https://manual.mikrotik.com/docs/getting-started/installation-and-upgrade/netinstall/img/netinstall_64_04.png)
   :::warning
   如果您下载了适用于多种架构的 RouterOS 软件包，Netinstall 在选中设备后只会显示适用于该设备的架构软件包。不支持的软件包不会出现在窗口中。

   如果安装未开始（进度条不移动或未显示状态），请尝试关闭并重新打开 Netinstall，或再次将设备置于 Etherboot 模式。如果问题仍然存在，请尝试在另一台计算机上使用 Netinstall。
   :::

## 安装后

使用 Netinstall 后，设备将重置为默认设置（除非您指定不应用默认配置或保留旧配置）。出于安全原因，某些设备在使用默认配置时无法通过 **Ether1** 端口访问。有关详细信息，请参见[默认配置](../../configuration-management/default-configurations.md)。

## 完成设置

您的设备现已准备就绪。根据需要配置设备，然后将其重新连接到网络。

[首次配置](../../first-time-configuration.md)

:::tip
正在寻找其他安装方法？请参阅 [**Linux**](./netinstall-linux.md) 或 [**Netinstall Package**](./netinstall-package.md) 说明。
:::