# 串行控制台

> 串行控制台与终端工具支持通过串行端口实现设备直接通信，适用于初始配置或恢复配置，最多可管理132台设备。本页说明用于硬件流控制的零调制解调器（null-modem）线缆配置，包括无握手、部分握手及全握手等选项。

# 串行控制台

串行控制台和串行终端是用于与通过串行端口互联的设备及其他系统进行通信的工具。串行终端可用于监控和配置多种设备——包括调制解调器、网络设备（含MikroTik路由器），以及任何可连接至串行（异步）端口的设备。

串行控制台功能用于配置直接访问的配置设施（显示器/键盘和串行端口），这些设施主要用于初始配置或恢复配置。连接两台主机（如两台PC或两台路由器，而非调制解调器）需要专用的零调制解调器线缆。请注意，从另一台计算机访问串行控制台需要终端仿真程序（例如Windows上的HyperTerminal或Linux上的minicom）。路由器串行端口的默认设置为115200比特/秒（x86平台默认9600比特/秒）、8个数据位、1个停止位、无校验、硬件（RTS/CTS）流控。

多位客户描述了串行终端（管理侧）功能可能适用的场景：

- 在山顶，MikroTik无线设备与无法通过带内方式（通过IP网络telnet）管理的设备（包括交换机和Cisco路由器）并排安装。
- 通过串行端口监控气象报告设备。
- 连接需要通过串行连接进行监控和管理的高速微波调制解调器。

借助MikroTik的串行终端功能，最多可监控和管理132台（甚至更多）设备。

## 串行控制台连接

设备间的串行通信采用RS232标准。这是计算机世界中最古老且应用最广泛的通信方式之一，曾用于与调制解调器或其他外围设备（DTE/DCE）通信。在现代应用中，串行通信主要用于DTE/DTE通信（数据终端设备），例如使用零调制解调器线缆。零调制解调器线缆有多种类型，其中部分可能完全不适用于RouterBoard。

### 无握手零调制解调器线缆

此线缆完全不使用握手引脚：

| 侧1（DB9母头） | 侧2（DB9母头） | 功能 |
| --: | --: | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 5 | 5 | GND |

该线缆仅允许在交叉连接的Rx/Tx线上传输数据。此类线缆无法实现硬件流控，唯一可行的流控方式是使用XOFF和XON字符的软件流控。

### 带环回握手的零调制解调器线缆

第一种线缆的问题在于：当连接到启用了硬件流控的设备时，软件在检测调制解调器信号线时可能发生挂起。

带环回握手的零调制解调器线缆解决了此问题；其主要目的是让定义完善的软件误以为存在握手能力：

| 侧1（DB9母头） | 侧2（DB9母头） | 功能 |
| :-- | :-- | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 5 | 5 | GND |
| 1+4+6 | - | DTR → CD + DSR |
| - | 1+4+6 | DTR → CD + DSR |
| 7+8 | - | RTS → CTS |
| - | 7+8 | RTS → CTS |

此线缆无法实现硬件流控。此外，如果远端软件未向DTR输出发送自身的就绪信号，通信将发生挂起。

### 部分握手零调制解调器线缆

此线缆适用于启用流控且与DTE/DCE通信中流控的原始使用方式不冲突的场景。

不建议将此类线缆与RouterOS配合使用。

| 侧1（DB9母头） | 侧2（DB9母头） | 功能 |
| :-- | :-- | :-- |
| 1 | 7+8 | RTS2 → CTS2 + CD1 |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 4 | 6 | DTR → DSR |
| 5 | 5 | GND |
| 6 | 4 | DSR ← DTR |
| 7+8 | 1 | RTS1 → CTS1 + CD2 |

### 全握手零调制解调器线缆

适用于特殊软件，不应与RouterOS配合使用。

| 侧1（DB9母头） | 侧2（DB9母头） | 功能 |
| --: | --: | :-- |
| 2 | 3 | Rx ← Tx |
| 3 | 2 | Tx → Rx |
| 4 | 6 | DTR → DSR |
| 5 | 5 | GND |
| 6 | 4 | DSR ← DTR |
| 7 | 8 | RTS → CTS |
| 8 | 7 | CTS ← RTS |

### 零调制解调器线缆兼容性

以下汇总表可帮助您为应用场景选择合适的线缆。

|  | 无握手 | 环回握手 | 部分握手 | 全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 端口功能受限的RouterBoard | Y | Y | N\* | N |
| 功能完整的RouterBoard | Y | Y | Y | N |

\* - 仅在禁用硬件流控时可能可用

|  | 无握手 | 环回握手 | 部分握手 | 全握手 |
| :-- | :-- | :-- | :-- | :-- |
| 仅软件流控 | Y | Y\* | Y\*\* | Y\*\* |
| 低速DTE/DCE兼容硬件流控 | N | Y | Y\* | N |
| 高速DTE/DCE兼容硬件流控 | N | Y | Y\*\* | N |
| 使用特殊软件的高速通信 | N | N | Y\* | Y |

\* - 可作为替代方案使用

\*\* - 可用但不推荐

### RJ45类型串行端口

此类端口用于RouterBOARD 2011、3011、4011、CCR1072、CCR1036 r2、CCR2xxx及CRS系列设备，有时称为“Cisco风格”串行端口。

#### RJ45转DB9线缆引脚定义

![](https://manual.mikrotik.com/docs/management-tools/img/serial-console-01.webp)

| 信号 | 控制台端口（DTE）RJ-45 | RJ-45卷曲线 RJ-45引脚 | 适配器DB-9引脚 | 适配器DB-25引脚 | 信号 |
| :-- | --: | --: | --: | --: | :-- |
| RTS | 1 | 8 | 8 | 5 | CTS |
| DTR | 2 | 7 | 6 | 6 | DSR |
| TxD | 3 | 6 | 2 | 3 | RxD |
| 接地 | 4 | 5 | 5 | 7 | 接地 |
| 接地 | 5 | 4 | 5 | 7 | 接地 |
| RxD | 6 | 3 | 3 | 2 | TxD |
| DSR | 7 | 2 | 4 | 20 | DTR |
| CTS | 8 | 1 | 7 | 4 | RTS |

### RB M33G附加串行排针

对于RBM33G，可在GPIO引脚U3\_RXD、GND、U3\_TXD和3V3上连接附加串行排针。

### CCR串行排针

Cloud Core Router系列设备的PCB板上带有串行排针，标记为J402或100。

以下是该连接器的引脚定义：

![](https://manual.mikrotik.com/docs/management-tools/img/serial-console-02.webp)

## 串行终端使用

RouterOS允许通过`/system/serial-terminal`命令与连接到路由器串行端口的设备及其他系统进行通信。所有键盘输入将转发至串行端口，端口接收的所有数据将输出至所连接的设备。

首先，您需要有一个空闲的串行端口。如果设备只有一个串行端口（如所有RouterBoard、WRAP/ALIX板卡等），您需要禁用该系统控制台在该串行端口上的使用，才能将其用作连接其他设备（交换机、调制解调器等）的**串行终端**：

```ros
/system/console/disable 0
```

请务必仅禁用控制台而非删除，因为如果实际删除，RouterOS将在下次重启后重新创建控制台。

:::danger
**请注意以下重要事项！请花时间理解这些限制，以避免在RouterBoard的串行端口上连接设备时出现异常情况：**

- 按上述方式重新配置RouterBoard上的Serial0端口后，您将失去对RouterOS的串行控制台访问权限。这意味着，如果之后无法通过网络访问RouterBoard，您甚至可能需要重置其全部配置才能重新获得访问权限。
- 重启RouterBoard时，引导加载程序（RouterBOOT）将始终使用串行控制台（RouterBoard上的Serial0）发送启动消息并提供RouterBOOT菜单访问权限。

  串行端口向所连接设备输出的文本可能会干扰设备运行。此外，在标准配置下，按**任意**键即可进入RouterBOOT菜单。因此，如果您的串行设备在启动期间向RouterBoard的串行端口发送任何字符，RouterBoard将进入RouterBOOT菜单，并且**不会**启动RouterOS，除非您手动干预！

  您可以重新配置RouterBOOT，使其仅在收到<kbd>Delete</kbd>字符时才进入RouterBOOT菜单——使用此设置可降低重启时路由器卡死的风险！

  或者，如果使用较新版本，可使用[“静默启动”](../getting-started/installation-and-upgrade/routerboot.md)功能来抑制串行接口上的所有输出，包括取消启动音。

:::

接下来，您需要根据所连接设备的串行端口设置来配置您的串行端口。使用以下命令可将串行端口设置为19200波特率8N1。具体需要使用的设置取决于您连接的设备：

```ros
/port/set serial0 baud-rate=19200 data-bits=8 parity=none stop-bits=1
```

您也可以尝试让RouterOS自动检测所需波特率，设置如下：

```ros
/port/set serial0 baud-rate=auto
```

如果尚未连接设备，现在可以连接了。通常，您需要使用[零调制解调器线缆](#serial-console-connections)（与以太网交叉线类似）。现在一切就绪：

```ros
/system/serial-terminal serial0
```

这将使您能够访问连接到Serial0端口的设备。*<kbd>Control</kbd>+<kbd>A</kbd>*是前缀键，按下后将进入一个小型“菜单”。如果需要向远端设备发送*<kbd>Control</kbd>+<kbd>A</kbd>*字符，请连续按两次*<kbd>Control</kbd>+<kbd>A</kbd>*。

如需退出与串行设备的连接，请按*<kbd>Control</kbd>+<kbd>A</kbd>*，然后按***Q***。这将返回RouterOS控制台。

:::danger
请勿以错误速率连接设备，并避免转储二进制数据。
:::

## 特殊登录

特殊登录功能可用于通过打开telnet/ssh会话直接访问通过串行线缆连接的另一台设备（例如交换机），无需先登录RouterOS。

本演示将使用两台RouterBoard和一台PC。

![](https://manual.mikrotik.com/docs/management-tools/img/serial-console-03.webp)

路由器R1和R2通过串行线缆连接，PC通过以太网连接到R1。假设我们希望从PC通过串行线缆访问路由器R2。为此，您需要在R1上设置串行接口代理，可通过名为**特殊登录**的功能实现。

:::info
默认情况下，控制台绑定到串行端口。
:::

第一步是解除控制台与串行的绑定，只需在`/system/console`菜单中禁用相应条目：

```ros
[admin@MikroTik] /system/console> print
Flags: X - disabled, U - used, F - free
 #   PORT                                                                    TERM
 0 X serial0                                                                 vt102
```

下一步是添加新用户（本例中为*serial*），并将其绑定到串行端口：

```ros
[admin@MikroTik] > /user/add name=serial group=full
[admin@MikroTik] > /special-login/add user=serial port=serial0 disabled=no
[admin@MikroTik] > /special-login/print
Flags: X - disabled
 #   USER                                                                    PORT
 0   serial                                                                  serial0
```

现在我们可以从PC访问R2了。

```ros
maris@bumba:/$ ssh serial@10.1.101.146

[Ctrl-A is the prefix key]
R2 4.0beta4
R2 Login:

[admin@R2] >
```

要退出特殊登录模式，请按<kbd>Ctrl</kbd>+<kbd>A</kbd>，然后按Q：

```ros
[admin@MikroTik] >
[Q - quit connection]      [B - send break]
[A - send Ctrl-A prefix]   [R - autoconfigure rate]

Connection to 10.1.101.146 closed.
```

:::danger
路由器重启且串行线缆连接后，路由器可能卡在引导加载程序主菜单。
:::

要解决此问题，您需要将引导加载程序主菜单的访问键从`<任意键>`更改为`<Delete>`：

- 进入引导加载程序菜单。
- 按'k'选择启动键选项。
- 按'2'将键更改为`<Delete>`。

```
What do you want to configure?
d - boot delay
k - boot key
s - serial console
n - silent boot
o - boot device
u - cpu mode
f - cpu frequency
r - reset booter configuration
e - format nand
g - upgrade firmware
i - board info
p - boot protocol
b - booter options
t - call debug code
l - erase license
x - exit setup
your choice: k - boot key

Select key which will enter setup on boot:
 * 1 - any key
   2 - <Delete> key only

your choice: 2

```