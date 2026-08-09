# WinBox

> WinBox 是一款用于通过 Wine 在 Linux/macOS 上管理 MikroTik RouterOS 的 GUI 工具，通过 AES128-CBC-SHA 加密和 ECSRP 认证提供安全连接。它提供简单和高级两种模式用于连接路由器，并支持邻居发现功能来发现附近设备，同时避免不兼容的协议。

# WinBox

## 概述

:::info
**适用于 Linux 和 macOS 的原生 WinBox 测试版**现已在 [MikroTik 下载页面](https://mikrotik.com/download) 上提供！

:::

WinBox 是一款小型实用工具，允许通过快速简单的 GUI 管理 MikroTik RouterOS。它是一个原生的 Win32/Win64 二进制文件，但可以通过 Wine 在 **Linux** 和 **macOS (OSX)** 上运行。所有 WinBox 界面功能尽可能与控制台功能保持一致，因此手册中没有单独的 WinBox 章节。某些高级和系统关键配置无法通过 WinBox 完成，例如更改接口的 MAC 地址。

从 WinBox v3.14 开始，使用以下安全功能：

- WinBox.exe 使用由 SIA Mikrotīkls (MikroTik) 颁发的扩展验证证书进行签名。
- WinBox 使用 ECSRP 进行密钥交换和认证（需要新版本的 WinBox）。
- 双方验证对方知道密码（不可能进行中间人攻击）。
- RoMON 模式下的 WinBox 要求代理为最新版本，才能连接到最新版本的路由器。
- WinBox 使用 AES128-CBC-SHA 作为加密算法（需要 WinBox 3.14 或更高版本）。

## 启动 WinBox

WinBox 加载器可以从 [MikroTik 下载页面](https://www.mikrotik.com/download) 下载。下载 WinBox.exe 后，双击它，WinBox 加载器窗口将弹出。WinBox 加载器有两种模式：默认启用的简单模式和高级模式。

### 简单模式

当您首次打开 WinBox 加载器时，将使用简单模式布局：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-01.webp)

要连接到路由器，请输入路由器的 IP 或 MAC 地址，指定用户名和密码（如果有），然后点击 **Connect** 按钮。您也可以在 IP 地址后输入端口号，用冒号分隔，例如 192.168.88.1:9999。端口可以在 RouterOS **services** 菜单中更改。

:::warning
建议尽可能使用 IP 地址。MAC 会话使用网络广播，并非 100% 可靠。

:::

您也可以使用邻居发现来列出可用的路由器。使用 **Neighbors** 选项卡：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-02.webp)

从发现的路由器列表中，您可以点击 IP 或 MAC 地址列来连接到该路由器。如果您点击 IP 地址，则将使用 IP 进行连接；但如果您点击 MAC 地址，则将使用 MAC 地址连接到路由器。

:::info
邻居发现也会显示与 WinBox 不兼容的设备，例如 Cisco 路由器或任何其他使用 CDP（Cisco 发现协议）的设备。如果您尝试连接到 SwOS 设备，则连接将通过 Web 浏览器建立。

:::

#### 按钮/复选框和其他字段

- **Connect** - 连接到路由器。
- **Connect To RoMON** - 连接到 [RoMON](./romon.md) 代理。
- **Add/set** - 保存/编辑 **Managed** 选项卡中任何已保存的路由器条目。
- **Open In New Window** - 保持加载器在后台打开，并为每个连接的设备打开新窗口。
- **Connect To:** - 目标路由器的 IP 或 MAC 地址。
- **Login** - 用于认证的用户名。
- **Password** - 用于认证的密码。
- **Keep Password** - 如果未选中，密码不会保存到列表中。

#### 菜单项

- **File**
  - **New** - 在指定位置创建新的托管路由器列表
  - **Open** - 打开托管路由器列表文件
  - **Save As** - 将当前托管路由器列表保存到文件
  - **Exit** - 退出 WinBox 加载器

- **Tools**
  - **Advanced Mode** - 启用/禁用高级模式视图
  - **Import** - 导入已保存的会话文件
  - **Export** - 导出已保存的会话文件
  - **Move Session Folder** - 更改会话文件的存储路径
  - **Clear cache** - 清除 WinBox 缓存
  - **Check For Updates** - 检查 WinBox 加载器的更新

### 高级模式

当通过 *Tools → Advanced Mode* 启用 **高级模式** 时，将显示额外的 WinBox 加载器参数：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-03.webp)

#### 按钮/复选框和其他字段

按钮/复选框

- **Browse** - 浏览文件目录以查找特定会话。
- **Keep Password** - 如果未选中，密码不会保存到列表中。
- **Secure mode** - 如果选中，WinBox 将使用 DH-2048 进行密钥交换，并使用修改和加固的 RC4-drop3072 加密来保护会话。
- **Autosave session** - 自动保存已连接设备的会话。

字段：

- **Session** - 已保存的路由器会话。
- **Note** - 分配给已保存路由器条目的备注。
- **Group** - 分配给已保存路由器条目的组。
- **RoMON Agent** - 从可用设备列表中选择 RoMON 代理。

:::danger
托管路由器列表已加密，但如果没有为其设置主密码，**仍然**可以被另一个 WinBox 加载！

:::

### 命令行

可以使用命令行自动传递连接目标、用户、密码和会话（WinBox 4 的“工作区”）参数：

```
winbox.exe [<connect-to> [<login> [<password>]] <session|workspace>]

```

例如（无密码）：

```
winbox.exe 10.5.101.1 admin "" "<own>"

```

这将使用用户“admin”无密码连接到路由器 10.5.101.1，并使用会话|工作区“```<own>```”。

可以使用命令行自动传递连接目标、用户和密码参数，通过 RoMON 连接到路由器。在这种情况下，RoMON 代理必须保存在托管路由器列表中，以便 WinBox 知道该设备的用户和密码：

```
winbox.exe --romon [<romon-agent> [<connect-to> [<login> [<password>]]] <session|workspace>]

```

例如（无密码）：

```
winbox.exe --romon 10.5.101.1 D4:CA:6D:E1:B5:7D admin "" "<own>"

```

将通过 10.5.101.1 的 RoMON 代理，使用用户“admin”无密码连接到路由器 D4:CA:6D:E1:B5:7D，并应用名为“```<own>```”的会话|工作区。

### IPv6 连接

WinBox 支持 IPv6 连接。要连接到路由器的 IPv6 地址，必须像 Web 浏览器连接到 IPv6 服务器时一样，将其放在方括号中。示例：

[db8::1]

当连接到链路本地地址时，必须在 % 后输入接口索引：

[0:a00:27ff:fe70::e88c%2]

当需要将 WinBox 连接到非默认端口时，端口号设置在方括号之后：

WinBox 邻居发现能够发现启用 IPv6 的路由器。每个启用 IPv6 的路由器有两个条目，一个条目带有 IPv4 地址，另一个带有 IPv6 链路本地地址。您可以轻松选择要连接的地址。

### 在 macOS 上运行 WinBox

从 macOS 10.15 Catalina 开始，Apple 已移除对 32 位应用程序的支持，这意味着在此操作系统中不再可能使用常规 Wine 和常规 WinBox。Wine 已为 macOS 提供了 64 位版本，MikroTik 也发布了特殊的 [WinBox64.exe](https://mt.lv/winbox64) 版本。

要运行 WinBox64，需要执行以下步骤：

1. 从 [Wine macOS builds page](https://github.com/Gcenx/macOS_Wine_builds/releases) 安装最新的 Wine（wine-devel-7.X-osx64.tar.xz），并确保您已从 MikroTik 下载页面下载了 [WinBox64.exe 可执行文件](https://mt.lv/winbox64)。
2. 使用“打开方式”> Wine64.app 启动 WinBox64.exe。

### 在 Linux 上运行 WinBox

可以通过使用 Wine 仿真软件在 Linux 上运行 WinBox。确保已安装 Microsoft 字体包，否则可能会出现显示扭曲。

## 界面概览

WinBox 界面设计为对大多数用户直观易用。界面由以下部分组成：

- 顶部的主工具栏，用户可以在其中添加各种信息字段，如 CPU 和内存使用情况。
- 左侧的菜单栏 - 所有可用菜单和子菜单的列表。此列表根据安装的软件包而变化。例如，如果禁用了 IPv6 软件包，则 **IPv6** 菜单及其所有子菜单将不会显示。
- 工作区 - 所有菜单窗口打开的区域。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-04.webp)

标题栏显示信息以标识 WinBox 会话与哪个路由器打开。信息按以下格式显示：

```
[username]@[Router's IP or MAC] ( [RouterID] ) - WinBox [ROS version] on [RB model] ([platform])

```

从上面的截图可以看出，用户 **krisjanis** 已通过 IPv4/IPv6 地址 **[fe80::4e5e:cff:fef6:c0ab%3]** 登录到路由器。路由器 ID 为 **3C18-Krisjanis\_GW**，当前安装的 RouterOS 版本为 **v6.36rc6**，RouterBoard 为 **CCR1036-12G-4S**，平台为 **tile**。

在主工具栏的左侧是：

- **Undo**
- **Redo**
- **Safe Mode**
- 当前加载的会话

有关安全模式和撤销已执行操作的更多信息，请阅读 [本文](../getting-started/configuration-management/index.md)。

右侧是：

- 指示 WinBox 会话是否使用加密的指示器。
- 显示为绿色条的 WinBox 流量指示器。
- 自定义信息字段，用户可以通过右键单击工具栏并从列表中选择可用的信息字段来添加。

## 工作区和子窗口

WinBox 具有 MDI 界面，这意味着所有菜单配置（子）窗口都附加到主（父）WinBox 窗口，并显示在工作区中。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-05.webp)

子窗口不能拖出工作区。请注意上图中的 **Interface** 窗口被拖出可见工作区，底部出现了水平滚动条。如果任何窗口超出可见工作区边界，将出现垂直和/或水平滚动条。

### 子窗口菜单栏

每个子窗口都有自己的工具栏。大多数窗口具有相同的工具栏按钮集：

- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-06.webp) **Add** - 向列表中添加新项目。
- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-07.webp) **Remove** - 从列表中删除选定的项目。
- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-enable.png) **Enable** - 启用选定的项目（与控制台中的 **enable** 命令相同）。
- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-disable.png) **Disable** - 禁用选定的项目（与控制台中的 **disable** 命令相同）。
- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-comment.png) **Comment** - 添加或编辑注释。
- ![](https://manual.mikrotik.com/docs/management-tools/img/winbox-sort.png)  **Sort** - 允许您根据各种参数对项目进行排序。 [对显示的项目进行排序](#sorting-out-displayed-items)

几乎所有窗口的工具栏右侧都有一个快速搜索输入字段。在此字段中输入的任何文本都会在所有项目中搜索并高亮显示，如下面的截图所示。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-08.webp)

请注意，在快速查找输入字段旁边的右侧有一个下拉框。对于当前打开的（IP Route）窗口，此下拉框允许按路由表快速排序项目。例如，如果选择了 **main**，则只会列出主路由表中的路由。
所有防火墙窗口也有类似的下拉框，用于按链快速排序规则。

### 对显示的项目进行排序

几乎每个窗口都有一个 **Sort** 按钮。点击此按钮时，会出现多个选项，如下面的截图所示。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-09.webp)

该示例展示了如何快速筛选出 10.0.0.0/8 范围内的路由：

1. 按下 **Sort** 按钮。
2. 从第一个下拉框中选择 **Dst.Address**。
3. 从第二个下拉框中选择 **in**。“in”表示过滤器将检查 DST 地址值是否在指定网络范围内。
4. 输入要比较值的网络（在我们的示例中输入“10.0.0.0/8”）。
5. 这些按钮用于向过滤器堆栈中添加或移除另一个过滤器。
6. 按下 **Filter** 按钮以应用我们的过滤器。

从截图中可以看出，WinBox 只筛选出了 10.0.0.0/8 范围内的路由。

比较运算符（截图中的数字 **3**）可能因窗口而异。例如，“IP Route”窗口只有两个：**is** 和 **in**。其他窗口可能有“is not”、“contains”、“contains not”等运算符。

WinBox 允许构建过滤器堆栈。例如，如果需要按目标地址和网关进行过滤，则：

- 按照上述示例设置第一个过滤器。
- 按下 **[+]** 按钮在堆栈中添加另一个过滤器栏。
- 设置第二个过滤器以按网关过滤。
- 按下 **Filter** 按钮以应用过滤器。

您也可以通过按下 **[-]** 按钮从堆栈中移除不必要的过滤器。

### 自定义显示的列列表

默认情况下，WinBox 显示最常用的参数。然而，有时需要查看其他参数，例如“BGP AS Path”或其他 BGP 属性，以监控路由是否正确选择。

WinBox 允许您为每个单独的窗口自定义显示的列。例如，要添加 BGP AS path 列：

- 点击列标题右侧的小箭头按钮（**1**）或右键单击路由列表。
- 从弹出的菜单中移动到 **Show Columns**（**2**），并从子菜单中选择所需的列，在我们的案例中点击 **BGP AS Path**（**3**）。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-10.webp)

对窗口布局所做的更改会被保存，下次打开 WinBox 时会应用相同的列顺序和大小。

#### 详细模式

也可以启用 **Detail mode**。在此模式下，所有参数都显示在列中，第一列是参数名称，第二列是参数值。

要启用详细模式，请右键单击项目列表，并从弹出菜单中选择 **Detail mode**

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-11.webp)

#### 类别视图

可以按类别列出项目。在此模式下，所有项目将按字母顺序或其他类别分组。例如，如果按名称排序，项目可以按字母顺序分类；项目也可以按类型分类，如下面的截图所示。

要启用类别视图，请右键单击项目列表，并从弹出菜单中选择 **Show Categories**。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-12.webp)

### 拖放

可以使用 WinBox 的拖放功能向路由器上传和从路由器下载文件。您也可以通过右键单击文件并选择“Download”来下载文件。

:::info
如果 WinBox 在 Linux 上使用 wine4 运行，拖放功能可以正常工作。两个 WinBox 窗口之间的拖放可能会失败。

:::

### 流量监控

WinBox 可以用作实时监控每个接口、队列或防火墙规则流量的工具。下面的截图显示了以太网流量监控图。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-13.webp)

### 项目复制

这展示了在 WinBox 中复制项目是多么容易。在此示例中，我们将使用 COPY 按钮将动态 PPPoE 服务器接口转换为静态接口。

此图像显示了初始状态。如您所见，DR 指示“D”表示动态：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-14.webp)

双击接口并点击 COPY：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-15.webp)

将出现一个新的接口窗口，并自动创建一个新名称（在本例中为 pppoe-in1）。

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-16.webp)

在此 Down/Up 事件之后，此接口将变为静态：

![](https://manual.mikrotik.com/docs/management-tools/img/winbox-17.webp)

## 传输设置

- 托管路由器传输 - 在 File 菜单中，使用 Save As 和 Open 功能将托管路由器列表保存到文件，并在新工作站上重新打开。

- 路由器会话传输 - 在 Tools 菜单中，使用 Export 和 Import 功能将现有会话保存到文件，并在新工作站上重新导入。

## WinBox v3 键盘快捷键

| 快捷键 | 描述 |
| :-- | :-- |
| **Ctrl** + **F** | 查找 |
| **Ctrl** + **G** | 查找下一个 |
| <kbd>F3</kbd> | 查找 / 查找下一个 |
| **Ctrl** + **M** | 添加或编辑注释 |
| **Ctrl** + **E** 或 **Num+** | 启用选定的设置 |
| **Ctrl**+ **D** 或 **Num-** | 禁用选定的设置 |
| **Ctrl** + **+** | 放大 WinBox |
| **Ctrl**+ **-** | 缩小 WinBox |
| <kbd>Tab</kbd> | 选择下一个控件 |
| <kbd>Tab</kbd>+<kbd>Shift</kbd> | 选择上一个控件 |
| <kbd>Space</kbd> | 选择聚焦的控件 |
| <kbd>F4</kbd> 或 **Esc** | 关闭窗口 |
| <kbd>F6</kbd> | 聚焦上一个窗口 |
| <kbd>F6</kbd>+<kbd>Shift</kbd> | 聚焦下一个窗口 |
| <kbd>Insert</kbd> | 向列表中添加新条目 |
| <kbd>Delete</kbd> | 从列表中删除条目 |

## WinBox v4 键盘快捷键

| 快捷键 | 描述 |
| :-- | :-- |
| **Ctrl** + **E** 或 **Num+** | 启用选定的设置 |
| **Ctrl**+ **D** 或 **Num-** | 禁用选定的设置 |
| **Ctrl/CMD** + **+** | 放大 WinBox |
| **Ctrl/CMD** + **-** | 缩小 WinBox |
| **Ctrl/CMD**+ **0** | 重置缩放 |
| **Ctrl** + **Tab** | 选择下一个选项卡 |
| **Ctrl** + **Shift** + **Tab** | 选择上一个选项卡 |
| **Tab** | 选择下一个控件 |
| **Shift** + **Tab** | 选择上一个控件 |
| **Space** | 选择聚焦的控件 |
| **Ctrl + F4** 或 **Alt**/**Cmd + W** | 关闭窗口 |
| **Alt** + **A**/ **Cmd** + **Shift** + **S** | 聚焦上一个窗口 |
| **Alt**/**Cmd** + **S** | 聚焦下一个窗口 |
| **Delete** | 从列表中删除条目 |
| **Alt**/**Cmd**+ **Opt** + **F** | 全局菜单搜索 |
| **Alt**/**Cmd** + **T** | 打开新的终端窗口 |

## 故障排除

##### WinBox 无法连接到路由器的 IP 地址，设备未显示在邻居列表中

确保 Windows 防火墙设置为允许 WinBox 连接通过 Windows 防火墙中的专用和/或公用网络接口。可以在 *Control Panel\System and Security\Windows Defender Firewall\Allowed applications* 中更改。或者禁用 Windows 防火墙。

##### 连接到路由器的 MAC 地址时出现错误 '(port 20561) timed out'

如果文件和打印共享被禁用，Windows (7/8) 不允许 MAC 连接。

##### 我无法在 WinBox IPv4 邻居列表中找到我的设备，或者 MAC 连接失败并显示“ERROR could not connect to XX-XX-XX-XX-XX-XX”

大多数网络驱动程序不会启用 IP 协议栈，除非您的主机设备具有 IP 配置。请在您的主机设备上设置 IPv4 配置。

*有时设备会因缓存而被发现，但 MAC 连接仍会失败并显示“ERROR: could not connect to XX:XX:XX:XX:XX:XX”。*

:::warning
WinBox MAC 地址连接要求 MTU 值设置为 1500，且不分片。其他值可能导致性能不佳 - 可能会发生连接丢失。

:::