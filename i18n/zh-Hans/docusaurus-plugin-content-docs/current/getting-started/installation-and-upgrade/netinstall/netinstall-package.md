# Netinstall 软件包

> 本文档介绍 RouterOS Netinstall 软件包，该软件包允许从另一台运行 RouterOS 7.24beta1 或更高版本的路由器远程重新安装 MikroTik 设备上的 RouterOS，涵盖前提条件、/tool/netinstall 菜单和参数、缓存以及 Preboot Etherboot 恢复用例。

# Netinstall 软件包

**Netinstall 软件包** 是一个附加软件包，适用于所有运行 RouterOS 7.24beta1 及以上版本的设备，并支持除 SMIPS 之外的所有架构。

该软件包允许从另一台运行 RouterOS 的 MikroTik 设备远程重新安装 RouterOS。

## 前提条件

- RouterOS 版本 7.24beta1 及更高版本。
- 已启用 Netinstall 软件包。
- 目标 MikroTik 硬件路由器与正在重新安装的设备连接到同一 L2 网段。

:::warning
默认情况下，**Netinstall 软件包** 会在根目录下创建一个 `NetinstallCache` 目录。在带有 `flash` 目录的设备上，Netinstall 相关文件存储在 RAM 中。在没有 `flash` 目录的设备上，这些文件存储在设备的持久化存储中。

请确保 **Netinstall** 服务器设备具有足够的可用存储空间或 RAM。

您还可以在 **Netinstall → Settings** 中配置外部存储设备作为 `NetinstallCache/` 目录。
:::

> 从 `Files` 菜单中物理删除的文件，如果当前已缓存，将被自动重新下载。要删除缓存文件，请从 `Netinstall Cache` 菜单中移除它们。
> 如果文件在设备重启前已下载，则会被删除。

## 安装工作流程

1. 安装并启用 Netinstall 软件包。**Netinstall 软件包** 可在 WinBox、WebFig GUI 和 CLI 中使用，位于 **Tools** 菜单下，或在 CLI 中通过 `/tools/netinstall` 访问。

2. 配置 Netinstall 接口。添加新的 **Netinstall** 接口，设置所需参数，并将连接到该接口的设备以 BOOTP 模式运行。

3. 下载或选择所需的 RouterOS 软件包。**Netinstall 软件包** 会自动为目标设备架构安装相应的 **System** 软件包。

4. 将目标设备启动到 Etherboot 模式。

5. 安装 RouterOS。

:::tip
如果未设置 **Version** 参数，**Netinstall 软件包** 将安装 **Netinstall 服务器** 上当前在 `Check for Updates` 频道中选择的最新 RouterOS 版本。
:::

附加软件包必须显式选择。

## 通用配置选项

| 参数 | 描述 |
| :-- | :-- |
| **Settings** | 允许设置 `NetinstallCache/` 路径目录。参见 [前提条件警告信息](#前提条件)。示例：`/tool/netinstall/settings/set cache-directory=...` |

## Netinstall 参数

| 参数 | 描述 |
| :-- | :-- |
| **allow-etherboot** (yes / no ; 默认值：**yes**) | 允许所选接口上的 BOOTP 请求。如果设置为 no，将忽略该设备。 |
| **allow-flashfig** (yes / no ; 默认值：**yes**) | 启用 [FlashFig](../../../management-tools/flashfig.md) 功能 |
| **apply-default-configuration** (yes / no ; 默认值：**no**) | 如果启用，设备将在安装并重启后应用默认配置脚本。参见 `/system/default-configuration/script/print`。 |
| **auto-reboot** (none / reboot / shutdown ; 默认值：**reboot**) | 定义设备安装成功完成后执行的操作。 |
| **etherboot-image** | 允许选择先前缓存的软件包进行安装。 |
| **etherboot-image-arch** | 指定 etherboot 镜像所需的 CPU 架构。所有其他架构的请求将被忽略。如果未指定，将使用检测到的架构。 |
| **extra-packages** | 允许添加与 `system` 软件包一起安装的附加软件包。`routeros` 软件包将默认安装。 |
| **install-once** (yes / no ; 默认值：**yes**) | 限制每次 Netinstall 运行仅安装一次。该工具会跟踪成功安装设备的 **MAC 地址**，并在当前会话中忽略来自同一 **MAC 地址** 的后续 **BOOTP** 请求。 |
| **interface** | 指定 **Netinstall 服务器** 的网络接口。 |
| **ip-range** | 自定义用于 netinstall 过程的 **BOOTP** IP 范围。 |
| **keep-old-configuration** (yes / no ; 默认值：**yes**) | 指示 Netinstall 在安装后读取并恢复设备核心配置（/export；/users）。此选项不会保留用户文件、容器或类似数据。 |
| **mac-address** | 指定允许安装的 MAC 地址。提供后，所有其他 BOOTP 请求将被忽略。 |
| **mode-file** | 类似于 `Mode script`。指定一个一次性自定义脚本，该脚本在设备安装后首次启动时运行。使用此脚本在设备部署期间配置设备模式、protected-routerboot 和其他设置。模式脚本在任何自定义或默认配置脚本之前执行。完成后，脚本会自动从设备中移除。如果脚本修改了设备模式，设备将在执行后立即重启。 |
| **place-before** | 在现有规则之前插入规则 |
| **remove-branding** (yes / no ; 默认值：**no**) | 丢弃设备上当前安装的 branding 软件包。如果未指定，则保留 branding 软件包。出厂安装的 branding 软件包无法丢弃，且始终保留。 |
| **script-file** | 允许在安装期间在设备上安装自定义默认配置脚本。这将替换 RouterOS 提供的默认配置脚本。参见 `/system/default-configuration/custom-script/print`。该脚本在 RouterOS 更新期间保留，并在后续配置重置后使用，直到设备使用新脚本重新安装或脚本被移除。 |
| **version** | 指定要安装的 RouterOS 版本。如果未设置 **Version** 参数，**Netinstall** 将安装 **Netinstall 服务器** 上当前在 `Check for Updates` 频道中选择的最新 RouterOS 版本。 |
| **wait** (yes / no ; 默认值：**no**) | 保持设备处于 etherboot 状态，并等待用户命令开始安装。 |

## 缓存

可用操作 - GUI 和 CLI 均支持 `Add`。

| 参数 | 描述 |
| :-- | :-- |
| **arch** | 必填参数。指定要下载的必要文件的 CPU 架构。 |
| **packages** | 允许添加要下载到 `NetinstallCache/` 目录的附加软件包列表。 |
| **version** | 指定要下载的 RouterOS 版本软件包。如果未设置 **Version** 参数，**Netinstall** 将下载 **Netinstall 服务器** 上当前在 `Check for Updates` 频道中选择的最新 RouterOS 版本。 |

## 设备

**Netinstall Devices** 菜单显示已 netinstall 设备列表及其状态。

可用操作：

- `Clear` 清空列表。
- `Install` 菜单。如果使用 `Install` 菜单选择了附加参数，则所有先前设置的设置将被覆盖。

可用的 `install` 参数：`auto-reboot`、`extra-packages`、`numbers`、`version`。

```bash
/tool/netinstall/devices> install auto-reboot=reboot extra-packages=user-manager version=7.24beta1
```

| 参数 | 描述 |
| :-- | :-- |
| **auto-reboot** (none / reboot / shutdown ; 默认值：**reboot**) | 定义设备安装成功完成后执行的操作。 |
| **extra-packages** | 允许添加与 `system` 软件包一起安装的附加软件包。`routeros` 软件包将默认安装。 |
| **numbers** | 允许选择列表中哪些设备需要重新安装 RouterOS。 |
| **version** | 指定要下载的 RouterOS 版本软件包。如果未设置 **Version** 参数，**Netinstall** 将安装接口主设置中选择的 **版本**，或者如果未指定，则下载 **Netinstall 服务器** 上当前在 `Check for Updates` 频道中选择的最新 RouterOS 版本。 |

## 使用场景

**Netinstall 软件包** 可用于 [Preboot Etherboot](../../../hardware/routerboard.md#preboot-etherboot) 场景，即当一台安装了 Netinstall 软件包的 MikroTik 路由器专门用于远程恢复目的时。
设置 Netinstall 服务器的 `preboot-etherboot-server=ip_address`，并在目标设备出现任何问题时远程重新安装 RouterOS。
使用 `preboot-etherboot-server` 时，请在 Netinstall 服务器上配置适当的 **IP 范围** 以处理 Etherboot 请求。

:::danger
请记住禁用或严格过滤所创建的规则，以免在每次重启时意外重新安装系统。
:::

### Netinstall 软件包示例

```bash
[admin@MikroTik] /tool/netinstall/add interface=bridge1 keep-old-configuration=no apply-default-configuration=yes auto-reboot=reboot mac-address=01:23:45:67:89:BB extra-packages=wifi-qcom,container version=7.23.1 ip-range=192.168.88.10-192.168.88.20
```

验证缓存的软件包：

```bash
[admin@MikroTik] /tool/netinstall/cache/print 
Columns: PATH, URL, STATUS
#  PATH                                               URL                                                                                STATUS    
0  NetinstallCache/container-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/container-7.23.1-arm64.npk  downloaded
1  NetinstallCache/linux.arm64                 https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64        downloaded
2  NetinstallCache/linux.arm64-uefi            https://upgrade.mikrotik.com/routeros/7.23.1/netinstk/linux.arm64-uefi   downloaded
3  NetinstallCache/wifi-qcom-7.23.1-arm64.npk  https://upgrade.mikrotik.com/routeros/7.23.1/wifi-qcom-7.23.1-arm64.npk  downloaded
```

安装后检查设备状态：

```bash
[admin@MikroTik] /tool/netinstall/devices/print 
Flags: N - NETINSTALL
Columns: MAC-ADDRESS, INTERFACE, STATE, LAST-STATE-UPDATE, EXTRA-PACKAGES, VERSION, ARCH, MODEL, LAST-STATE, AUTO-REBOOT
#   MAC-ADDRESS        INTERFACE  STATE    LAST-STATE-UPDATE  EXTRA-PACKAGES  VERSION    ARCH   MODEL       LAST-STATE        AUTO-REBOOT
0 N 01:23:45:67:89:BB  bridge1    done     58s                container       7.23.1     arm64   L009UiGS   bootp reply sent  reboot     
                                                              wifi-qcom 
```

:::tip
正在寻找其他安装方法？请参阅 [**Windows**](./netinstall-windows.md) 或 [**Linux**](./netinstall-linux.md) 说明。
:::