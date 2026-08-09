# RouterOS 配置重置

> 本页提供关于重置 MikroTik RouterOS 配置的全面指南，涵盖物理按钮方法和 GUI/CLI 命令。详细说明了每种重置操作的 LED 指示灯、备份加载器程序、旧型号上的跳线孔使用，以及用于无线网络访问的 WPS 功能。

# RouterOS 配置重置

## 如何重置配置

要将 RouterOS 重置为出厂默认设置（包括移除当前密码），请按照以下步骤操作：

1. 断开设备电源。
2. 按住重置按钮。

![重置按钮](https://manual.mikrotik.com/docs/getting-started/configuration-management/img/reset-button_01.png)

1. 在按住按钮的同时，重新连接设备电源。
2. 观察 LED 指示灯。其中一个 LED（通常是 USR/用户 LED）将开始闪烁。
3. 当 LED 开始闪烁时，松开重置按钮。

设备将以默认配置重新启动。

## 从 RouterOS 重置

如果您仍然可以访问设备，可以直接从 RouterOS 恢复默认配置：

- 在终端中运行以下命令：**`/system/reset-configuration`**

- 或者在 **[WinBox](../../management-tools/winbox)** 或 **[WebFig](../../management-tools/webfig)** 中导航至 **System → Reset Configuration**。

## 使用重置按钮

MikroTik 设备包含一个重置按钮，根据启动期间按住的时间长短，可以执行多种功能。

:::tip
观看官方 MikroTips 系列视频：[重置序列](https://youtu.be/6Unz92rABs8)。
:::

### 加载备份 RouterBOOT 加载器

在通电前按住重置按钮，约 3 秒后松开。这将加载备份的 RouterBOOT 加载器。

如果设备因 RouterBOOT 升级失败而无法启动，此功能非常有用。使用备份加载器启动后，您可以在 RouterBOARD 设置中强制使用备份加载器，或从 `.fwf` 文件重新安装 RouterBOOT。

### 重置 RouterOS 配置

按住重置按钮直到 LED 开始闪烁，然后松开。设备将把 RouterOS 配置重置为出厂默认设置。

### 启用 CAPs 模式

在 LED 开始闪烁后，继续按住按钮约 **5 秒**。当 LED 变为常亮时，松开按钮以启用 **[CAPs 模式](../../wireless/abgn/capsman)**。

**CAPs 模式** 也可以通过命令行启用：`/system/reset-configuration caps-mode=yes`

### 启动 Netinstall 模式

在设备通电时按住重置按钮。持续按住直到 LED 序列完成（通常为 闪烁 → 常亮 → 熄灭），然后松开。

设备将进入 Netinstall 模式，并开始在网络上搜索 Netinstall 服务器。

:::tip
观看官方 MikroTips 系列视频：[Netinstall](https://youtu.be/gzlLbIf3Dbk)。
:::

有关 Netinstall 的详细说明，请参阅 **[Netinstall 文档](../installation-and-upgrade/netinstall)**。

## 重置跳线方法

较旧的 RouterBOARD 型号还配有重置跳线孔。某些设备可能需要打开外壳。RB750/RB951/RB751 的跳线孔位于外壳的一个橡胶脚下。

使用金属螺丝刀短接重置跳线，然后启动板卡，直到配置被清除：

![](https://manual.mikrotik.com/docs/getting-started/configuration-management/img/reset_hole_01.jpg) ![](https://manual.mikrotik.com/docs/getting-started/configuration-management/img/reset_hole_02.jpg)

### 旧型号的跳线重置

下图显示了较旧 RouterBOARD（如 RB133C）上重置跳线的位置：

![](https://manual.mikrotik.com/docs/getting-started/configuration-management/img/jumper_set_01.jpg)

:::danger
配置重置后，不要忘记移除跳线，否则每次重启时配置都会被重置！
:::

### WPS

某些设备具有 WPS 按钮，或带有 WPS 功能的重置按钮，可用于简化无线客户端连接，无需手动输入密码。某些型号还支持设备之间的 WPS 同步。
有关 WPS 和重置按钮功能的特定型号信息，请参阅您设备的 [用户手册](../../../hardware)。