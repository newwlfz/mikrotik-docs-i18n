# Modbus

> :::warning
目前，仅 [KNOT](https://mikrotik.com/product/knot)、[KNOT LR8G kit](https://mikrotik.com/product/knot_lr8g_kit) 和 [KNOT LR9G kit](https://mikrotik.com/product/knot_lr9g_kit) 支持 Modbus 协议（具有 RS-485 端口）。
:::
在 IoT 架构中广泛使用的协议之一称为 Modbus。

### 引言

:::warning
目前，仅 [KNOT](https://mikrotik.com/product/knot)、[KNOT LR8G kit](https://mikrotik.com/product/knot_lr8g_kit) 和 [KNOT LR9G kit](https://mikrotik.com/product/knot_lr9g_kit) 支持 Modbus 协议（具有 RS-485 端口）。
:::
在 IoT 架构中广泛使用的协议之一称为 Modbus。

![](https://manual.mikrotik.com/docs/internet-of-things/img/image2021-3-30_10-57-11.webp)

您可以通过此链接找到有关此协议的更多信息。

支持 Modbus 的设备应连接到 RS485 端口。设备支持两线连接（A+/B-）（2 针端子排）。

![](https://manual.mikrotik.com/docs/internet-of-things/img/image2021-3-22_15-40-37.webp)

需要注意的是，两个引脚不应接反。将“A”和“B”连接颠倒（极性错误）将导致通信失败。

另一个需要记住的是 Modbus 电缆距离。如果电缆长度小于 50 米，则不应有问题。如果使用 50 米以上的电缆，则应在电缆末端安装 120 欧姆终端电阻。

KNOT 支持：

- **Modbus TCP 服务器场景**，允许您使用第三方 Modbus 客户端通过 Modbus TCP/IP 连接（TCP 端口 502）向 KNOT 的 IP 地址发送功能码命令。您可以使用任何 Modbus 客户端软件（互联网上有很多），也可以轻松地用 Python 编写/配置。在这种情况下，KNOT 将 Modbus TCP/IP 请求“转换/桥接”为 Modbus RTU。
- **Modbus RTU 控制器场景**（仅从 v**7.10** 开始可用），允许您直接从 RouterOS 命令行通过 Modbus/RTU 发送功能码命令。

#### Modbus TCP 数据包结构

您可以通过此[链接](https://en.wikipedia.org/wiki/Modbus)找到有关 Modbus 数据包结构的更多信息。

查询数据包由事务标识符、协议、长度、单元标识符、功能码和功能参数字段组成，最大大小为 260 字节。

- 事务标识符 - 从 0 到 65535 的整数，用于标识对特定查询的应答；
- 协议 - 0x0000 表示 Modbus；
- 长度 - 表示长度字段之后将跟多少字节；
- 单元标识符 - 通常称为“设备地址”，0x00-0xff。特定系统中的每个终端设备应具有唯一的 ID；
- 功能码 - 描述将调用哪个功能。每个设备都有多个寄存器，这些功能用于与寄存器交互。代码由标准定义，但制造商也可以实现具有特定代码的自己的功能；
- 功能参数/数据 - 通常指定寄存器地址、数据长度以及在使用“写入”功能时要写入的数据。
默认单元标识符、功能码和参数可在特定产品的数据手册中找到。应答消息的结构类似，也应在产品数据手册中进行描述。

### 配置

**子菜单：** `/iot modbus`

一旦电路板连接到 Modbus 设备，请检查“modbus”端口配置（如果连接的 Modbus 设备期望其他值，则可以更改波特率）：

```ros
[admin@MikroTik] > /port print
Columns: DEVICE, NAME, CHANNELS, USED-BY, BAUD-RATE
# DEVICE  NAME    CHANNELS  USED-BY  BAUD-RATE
0         modbus         1  modbus        9600
1 1-1     modem          4                9600
```

默认情况下，名为“*modbus*”的端口分配给 Modbus 服务，但服务本身是禁用的。为了激活“Modbus”服务，您需要发出如下所示的命令：

```ros
[admin@MikroTik] > /iot modbus print       
                disabled: yes
           hardware-port: modbus
                tcp-port: 502
                 timeout: 1000ms
  disable-security-rules: yes
[admin@MikroTik] > /iot modbus set disabled=no
```

此外，当您希望允许 Modbus 客户端使用 TCP(502)/IP 协议与 Modbus 服务器通信时，您需要确保设备的 IP+502 TCP 端口是可访问的。从 LAN 访问，由于没有防火墙规则限制此类访问，因此应该从一开始就允许。从外部访问（如果“从”设备从 WAN 侧连接）- 默认情况下不允许。您可以在手册中找到有关如何配置防火墙的信息。不建议为所有人保持公共/WAN 访问可用，如果确实需要此类访问，您应该指定允许的公共“客户端”的源 IP 地址（借助防火墙规则中的 **src-address** 参数）。否则，您将为所有人打开 Modbus 端口以供探测。

| 属性 | 说明 |
| --- | --- |
| **disabled** (yes \| no; 默认值：yes) | 启用或禁用 Modbus 功能。 |
| **hardware-port** (*字符串列表*; 默认值：modbus) | 为服务分配一个端口。使用默认的“modbus”端口。 |
| **tcp-port** (*整数：0..4294967295*; 默认值：502) | 指定设备将用于 Modbus TCP 通信的 TCP 端口。 |
| **timeout** (*整数：0..1000*; 默认值：1000) | 指定超时值，以毫秒为单位。发送 Modbus 请求并接收应答所允许的最长时间。如果请求和应答之间的时间超过配置的值，则返回“失败”。 |
| **disable-security-rules** (yes \| no; 默认值：yes) | 启用或禁用安全规则功能。 |
| **interframe-gap** (*整数*; 默认值：0) | Modbus 是“半双工”的 → 一次只能打开 Tx 或 Rx 窗口。根据标准，在 Tx 之后，必须跟随 3.5 个字符（对于不同的波特率而不同）的静默间隔。但是，并非所有 Modbus 从站设备都遵循该规则，它们可能更早或更晚开始 Tx 回传。这可能导致信息位丢失和通信失败。此参数可用于“从”设备不遵循标准规则的情况。`interframe-gap=0` 表示 `~4 ms` 的 3.5 字符间隔。 |
| **rx-switch-offset** (整数;) | 定义 Modbus 窗口（引脚方向）从 Tx 切换到 Rx 的速度。 |

### 通过 Modbus RTU 发送功能码命令

仅从 v**7.10** 开始可用。这适用于“**Modbus RTU**”场景。此功能允许直接从 RouterOS 发送功能码命令（支持所有功能码）。对于“Modbus TCP”场景，您必须使用第三方软件来发送功能码命令。

**子菜单：** `/iot modbus transceive`

| 属性 | 说明 |
| --- | --- |
| **address** (*整数：0..255*; 默认值：) | 指定设备地址或单元标识符。 |
| **function** (*整数：0..255*; 默认值：) | 指定功能码。例如：function=3 → 读保持寄存器功能码；function=6 → 写单个保持寄存器功能码。 |
| **data** (*字符串，最大长度 504*; 默认值：) | 输入数据字符串，通常指定寄存器地址和要发送的数据。例如：data=20000001 数据字符串长度为 4 字节。“0x2000”是对寄存器的命令（2 字节长），“0x0001”（2 字节长）是设备地址。有关需要发送的确切数据字符串，请参阅 Modbus 设备的规格说明。 |
| **values** (*整数：0..4294967295*; 默认值：) | 发送数据的另一种方式（请参阅上面的 **data** 参数）。在这种情况下，每个指定的值代表数据负载/字符串的 1 个字节。例如：values=32,0,0,1 等同于 data=20000001 的输出。32(十进制)=0x20(十六进制)，0(十进制)=0x00(十六进制)，0(十进制)=0x00(十六进制)，1(十进制)=0x01(十六进制) → 0x20000001。 |

使用“transceive”功能发送功能码 3 命令的示例：

```ros
/iot modbus transceive address=1 function=3 data=20000001 
   address: 1
  function: 3
      data: 01030164
    values: 100
      time: apr/27/2023 14:05:15
    status: ok
```

从上面的输出中，我们可以看出连接的 Modbus 设备回复了值“100”或数据“01030164”（01→ 地址；03→ 功能码；01→ 字节数；64（十六进制转十进制=100）→ 应答）。

### 通过 Modbus TCP 发送功能码“3”命令

专门针对功能码 3（这不适用于任何其他功能码），您可以使用附加选项，如下所示：

```ros
[admin@device] > {:local output [/iot modbus read-holding-registers slave-id=0x03 num-regs=0x1 reg-addr=0x0 as-value once];:put [($output->"values")]}
2349
[admin@device] > {:local output [/iot modbus read-holding-registers slave-id=0x03 num-regs=0x5 reg-addr=0x0 as-value once];:put [($output->"values")]}
2353;3;500;75;38
```

可以变化的参数是“reg-addr”（数据字符串中的地址）、“num-regs”（数据字符串中对寄存器的命令/寄存器数量）和“slave-id”（设备地址或单元标识符）。所有这些都取决于 MODBUS 连接的设备支持哪些值。

### Modbus 安全

从 v**7.12** 开始可用。

**子菜单：** `/iot modbus security-rules`

Modbus 安全功能允许您设置特定规则，以限制或允许访问 Modbus 连接的设备。**这仅适用于 Modbus TCP 通信**（这些规则不适用于 Modbus RTU 通信）。这使得可以允许特定的 IP 范围/网络访问特定的功能码命令。

要启用该功能，请输入命令：

```ros
/iot modbus set disable-security-rules=no
```

启用该功能后，添加规则本身。例如：

```ros
/iot modbus security-rules add ip-range=0.0.0.0/0 allowed-function-codes=3,6
```

上述规则将允许任何可能的 IP 地址向 Modbus 连接的设备发送功能码 3 和 6 命令。其他所有内容均受限制。

| 属性 | 说明 |
| --- | --- |
| **ip-range** (*地址/掩码*; 默认值：) | 指定将被允许发送功能码命令的 IP 地址范围（或网络）。 |
| **allowed-function-codes** (*整数：0..4294967295*; 默认值：) | 指定仅可从配置的 ip-range 访问的功能码。 |