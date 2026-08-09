# 使用 MQTT 和 ThingsBoard 进行蓝牙标签追踪

> 本文档介绍了如何使用 MikroTik RouterOS 配合 MQTT 和 ThingsBoard 实现蓝牙标签追踪，详细说明了 KNOT 设备如何捕获蓝牙广播数据包、将其处理为 MQTT 消息，并在 ThingsBoard 中可视化以跨多个区域追踪资产移动。

# 使用 MQTT 和 ThingsBoard 进行蓝牙标签追踪

RouterOS 中的蓝牙接口实现允许设备捕获通过 37、38 和 39 广播信道广播的蓝牙广播数据包。更多信息请参阅[此处的指南](../index.md)。

蓝牙标签，例如 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 和 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out)，正是这样工作的。它们通过上述信道广播广播负载。要了解负载中存储了哪些信息，请务必查看此[链接](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-MikroTikPDUPayloadstructure)。标签可以配置（使用 [MikroTik Beacon Manager](https://help.mikrotik.com/docs/display/UM/MikroTik+Beacon+Manager) 应用）为自动广播负载，可以设置间隔和/或在检测到移动、倾斜或自由落体触发时广播。简而言之，标签会定期向周围所有蓝牙扫描器（如 [KNOT](https://mikrotik.com/product/knot)）“告知”（广播）关于自身的信息。

当标签广播负载且标签位于 KNOT 的蓝牙工作范围内时，KNOT 将捕获并在其“scanner”蓝牙接口部分显示该负载。显示效果如下：

```ros
/iot/bluetooth/scanners/advertisements/print
Columns: DEVICE, PDU-TYPE, TIME, ADDRESS-TYPE, ADDRESS, RSSI, LENGTH, DATA
#  DEVICE  PDU-TYPE        TIME                  ADDRESS-TYPE  ADDRESS            RSSI    LENGTH  DATA                                        
0  bt1     adv-noconn-ind  2023-03-07 12:11:57  public        DC:2C:6E:0F:C0:3D  -51dBm      22  15ff4f09010079100000ffff0000cf188a6b2b000064
1  bt1     adv-noconn-ind  2023-03-07 12:11:58  public        2C:C8:1B:4B:BB:0A  -49dBm      22  15ff4f090100168dfefffffffeffa51ae1362200005e 
```

上面的示例显示，KNOT 在其工作范围内看到两个蓝牙标签，MAC 地址分别为“DC:2C:6E:0F:C0:3D”和“2C:C8:1B:4B:BB:0A”，以及它们各自的负载（“DATA”字段）和信号强度（“RSSI”字段）。

:::info
在本地测试 KNOT 能处理多少负载时，我们取得了以下结果 → 使用 300 个标签（出厂设置），分散在 KNOT 周围，并使用蓝牙过滤器“keep-newest”（该过滤器会用最新的负载覆盖每个唯一 MAC 地址先前收到的负载，以便蓝牙列表始终为每个唯一标签的 MAC 地址显示 1 个负载），所有 300 个 MAC 地址在 30-40 秒后出现在 KNOT 的范围内。这里需要记住的是，所有 300 个标签同时在同一信道上广播会造成干扰（接收延迟）。当我们“清除”蓝牙负载列表时，列表每秒新增 20 条记录，大约 15 秒后，列表中有 250-290 个负载。再经过约 15 秒，列表显示了全部 300 个唯一标签负载。**您的 KNOT 实际能处理的标签数量在很大程度上取决于环境，因此最好在现场进行测试。**
:::

借助 RouterOS [脚本](../../../developer-guides/scripting/index.md)和[调度器](../../../system-information-and-utilities/scheduler.md)，我们可以让 KNOT 自动定期扫描负载列表，如果列表中发现特定负载或特定标签的 MAC 地址，我们可以让 KNOT 构建一条 MQTT 消息（基于上例中显示的信息），并通过 [MQTT](../../mqtt/index.md)、[电子邮件](../../../system-information-and-utilities/e-mail.md)或 [HTTP](../../../system-information-and-utilities/fetch.md) POST 发送到配置的服务器。脚本示例将在本指南后面展示。

正如标题所示，目标是实现一个**蓝牙标签追踪解决方案**，其思路非常简单。**当您有 2 个 KNOT**（KNOT-A 和 KNOT-B）在调度器上运行相同的脚本，**并且标签在它们的蓝牙工作范围之间移动时**，**服务器上的数据将指示**是 **KNOT-A 还是 KNOT-B 发送了**标签的**负载**。这将帮助您判断标签的邻近位置，即标签是在 KNOT-A 区域还是 KNOT-B 区域广播负载。

您需要一个服务器来存储和可视化数据。在本指南中，我们将展示一个名为 [ThingsBoard](https://thingsboard.io/) 的平台，以及如何使用 MQTT 协议与其通信。

ThingsBoard 提供云解决方案和不同的本地安装选项（在不同的操作系统上）。由于我们添加了[容器](../../../containers/index.md)功能，现在也可以在 RouterOS 中运行该平台。为此，您需要一个至少有 2 GB 可用 RAM 或 1 GB 可用 RAM 且负载极低的 RouterOS 设备，该设备需要支持扩展存储（例如，额外的 USB 端口），并且是 ARM64 或 AMD64 架构。可以考虑使用 [CHR](../../../getting-started/routeros-licensing/chr/index.md) 虚拟机，它可能是一个不错的选择。

### 设置要求

- 一个运行中的 ThingsBoard 服务器。
- 2 个或更多 [KNOT](https://mikrotik.com/product/knot)，能够通过以太网、Wi-Fi 或蜂窝连接访问服务器网络（所需设备数量取决于需要覆盖的区域大小）。
- 1 个或多个蓝牙 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 和/或 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 标签（取决于您需要追踪的资产数量 - 每个资产 1 个标签）。

## 场景说明

首先让我们看一个基本示例。我们有两个 KNOT（KNOT-A 和 KNOT-B）。我们在自己的环境中测试了蓝牙范围，并确认两个 KNOT 都能在 70 米距离内捕获标签。如果我们将 KNOT-A 和 KNOT-B 安装在相距 140 米的位置，它们的蓝牙范围将不会重叠或仅轻微重叠。当标签移动到 KNOT-A 范围内时 → 被监控标签的负载将出现在蓝牙扫描器列表下 → 脚本将按设定的计划启动 → 包含报告的 MQTT 消息将发送到服务器 → 最后，服务器将显示标签位于 KNOT-A 区域。当标签移动到 KNOT-B 范围内时，同样的事情发生，服务器将显示标签位于 KNOT-B 区域内。

实际的蓝牙工作距离可能因站点而异，因为许多不同因素会影响它，例如 2.4 GHz 干扰或周围使用的材料。例如，在视线无障碍且无干扰的情况下，KNOT 能够捕获标签广播负载的距离可达 180 米（KNOT — 约 180 米 — TG-BT5-OUT）。但您还必须记住，距离越远，传输过程中丢失的数据包就越多。在办公环境中，范围可能降至 30-100 米。

从逻辑上讲，如果蓝牙工作范围重叠且标签位于重叠区域内（同时处于 KNOT-A 和 KNOT-B 的蓝牙范围内），两个 KNOT 都将发送数据，服务器将显示该标签同时被两个设备报告。

**当然，会有两个或多个 KNOT 的蓝牙范围重叠的区域，您可以利用这一点**。基本上，您将获得信息，即标签当前位于特定 KNOT 区域之间的蓝牙范围边缘。换句话说，当资产移动到重叠区域时，您将在服务器上获得信息，表明资产位于两个 KNOT 工作范围之间的某个位置，这是有用的信息，**因为它提供了更高的精度**。

此外，**可以使用 [Tx power](https://help.mikrotik.com/docs/display/UM/MikroTik+Beacon+Manager+for+Android+devices#heading-TxPower) 参数降低标签的输出功率**。这意味着，即使标签的负载广播得太远，并被本不应看到这些负载的其他 KNOT（在更远的距离）捕获 → 您可以降低标签的输出功率，这将减少 KNOT 捕获它们的距离。这样，您可以“调整”接收“范围”，并避免“干扰”其他区域的信号。

我们准备的脚本还允许您设置过滤器（稍后展示），该过滤器将使 KNOT 忽略扫描器捕获的负载，除非信号强度（RSSI）强于指定值。在上面“[引言](../index.md)”部分显示的蓝牙扫描器示例打印中，我们可以看到 KNOT 看到一个标签的 **RSSI** 信号强度为 **-51 dBm**（MAC 地址为“**DC:2C:6E:0F:C0:3D**”的标签），另一个标签的 **RSSI** 信号强度为 **-49 dBm**（MAC 地址为“**2C:C8:1B:4B:BB:0A**”的标签）。因此，**如果我们**在脚本中应用过滤器以**忽略**所有信号强度（**RSSI**）**弱于 -50 dBm** 的负载，我们的 **KNOT 将报告只有标签“2C:C8:1B:4B:BB:0A”在蓝牙范围内**，因为其 RSSI 为 -49 dBm，而第二个标签（RSSI 为 -51 dBm）将被忽略。这本质上意味着这是“调整”接收“范围”的第二种方法。实际信号强度会因不同位置而异（如前所述，由于干扰和周围材料），因此需要在现场进行测试。

### 示例 #1

下面的拓扑中展示了一个用例：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-01.webp)

:::note
物体和蓝牙工作范围的比例仅作为示例展示，以帮助直观理解和想象拓扑结构！
:::

我们有一个仓库区域，**我们有 3 个资产**（托盘）需要追踪。**我们**还**有 3 个区域**：区域 **A**，存放新到达的托盘；区域 **B**，我们的资产被转移到此处进行检查；区域 **C**，资产在检查后被移动到此处。要实现蓝牙资产追踪，只需在每个区域安装 1 个 KNOT，每个资产安装 1 个标签。

如果 TAG 1 和 TAG 2（托盘）到达“到达”区域 A，KNOT A 将向服务器报告两个资产都在其蓝牙范围内。如果 TAG 3 被移动到区域 C，服务器将指示它在 KNOT C 的范围内。如果 TAG 1 和 TAG 2 向 B 区域移动，并停留在 A 和 B 区域之间的边缘，服务器将显示它们位于重叠区域（同时处于 KNOT-A 和 KNOT-B 的范围内）。如果标签移动到仓库中间，服务器将指示它们同时位于所有 3 个区域的重叠区域中。

#### 配置

在此示例中，我们将展示一个基本拓扑，使用两个 KNOT，我们只想知道标签是位于建筑物的一部分还是另一部分（是在区域 A 内还是区域 B 内）。

##### ThingsBoard 准备

请查看[此处](../../mqtt/mqtt-and-thingsboard-configuration.md)的指南，了解如何设置 ThingsBoard 和 RouterOS 以利用 MQTT 通信。

:::tip
为简单起见，此示例将展示[访问令牌](../../mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1)方案，但您也可以使用其他可用选项。对于生产环境，建议使用 SSL-MQTT，因为非 SSL-MQTT 容易被数据包捕获和检查。

要了解如何在通过[容器](../../../containers/index.md)运行的实例上实现 SSL-MQTT 通信，请查看[此处](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md)链接的指南（[启用 HTTPS 和 SSL MQTT](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md#enabling-https-and-ssl-mqtt) 部分）。
:::

在 ThingsBoard GUI 下创建 2 个 KNOT，并将它们设为“网关”。

转到“Devices”部分，点击“+”按钮和“Add new device”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-02.webp)

命名设备并勾选“Is gateway”选项：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-03.webp)

为您拥有的每个 KNOT 执行此操作：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-04.webp)

在您刚创建的设备下，在“Manage credentials”选项卡中为每个 KNOT 设置唯一的访问令牌（唯一凭据）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-05.webp)

##### RouterOS 配置

###### 准备

在继续之前，我们需要确认我们的蓝牙标签确实出现在 KNOT 的蓝牙范围内，并且 KNOT 能够检测到它。为此，您可以执行命令 `/iot/bluetooth/scanners/advertisements/print`：

```ros
/iot/bluetooth/scanners/advertisements/print
 # DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1        adv-noconn-ind  2023-03-08 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d   
 1 bt1        adv-noconn-ind  2023-03-08 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064   
 2 bt1        adv-noconn-ind  2023-03-08 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d   
 3 bt1        adv-noconn-ind  2023-03-08 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d   
```

或者您可以使用 [Webfig](../../../management-tools/webfig.md) 或 [Winbox](../../../management-tools/winbox.md) 在 IoT>Bluetooth>Advertising reports 选项卡下查看。

列表可能比较混乱。由于扫描器会捕获周围所有内容，列表中可能会出现随机负载。为帮助减少列表内容，您可以使用标签的 MAC 地址进行过滤 `/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D`：

```ros
/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D
 # DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1       adv-noconn-ind  2023-03-08 12:41:06 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f0901005ab20100fdfffdff4017e1c32c000064   
 1 bt1       adv-noconn-ind  2023-03-08 12:41:26 public       DC:2C:6E:0F:C0:3D        -40dBm         22 15ff4f090100349704000000fcff4017f5c32c000064   
 2 bt1       adv-noconn-ind  2023-03-08 12:41:36 public       DC:2C:6E:0F:C0:3D        -49dBm         22 15ff4f09010073fb0000000000003017ffc32c000064   
 3 bt1       adv-noconn-ind  2023-03-08 12:41:46 public       DC:2C:6E:0F:C0:3D        -43dBm         22 15ff4f090100b88cffffffffffff401709c42c000064   
```

要了解如何解读负载，请查看[此处](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-Scriptfordecoding)的指南。

###### MQTT broker

在每个 KNOT 上设置一个 MQTT broker。

对于 KNOT A：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=knot-A_access_token
```

其中：

- `name` 是您希望给 broker 的名称，此名称稍后将在脚本中使用。
- `address` 是 broker/ThingsBoard 服务器的 IP 地址。
- `port` 是 broker 监听的 TCP 端口 → 对于非 SSL，通常是 TCP 1883。
- `username` 由 MQTT broker 决定，在我们的案例中，它是在 ThingsBoard 管理门户中生成的“访问令牌”。

对于 KNOT B → 执行相同步骤。只需将 `username` 更改为为 KNOT B 设备（网关）生成的相应访问令牌。

###### 脚本

将下面显示的脚本导入到每个 KNOT。为此，只需复制下面显示的“代码”并将其粘贴到新的终端窗口中，然后按 <kbd>Enter</kbd>：

```ros
/system/script/add dont-require-permissions=no name=tracking owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="# Requ\
    ired packages: iot\r\
    \n\r\
    \n################################ Configuration ##############################\
    ##\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"tb\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"v1/gateway/telemetry\"\r\
    \n\r\
    \n# POSIX regex for filtering advertisement Bluetooth addresses. E.g. \"^BC:33:\
    AC\"\r\
    \n# would only include addresses which start with those 3 octets.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local addressRegex \"\"\r\
    \n\r\
    \n# POSIX regex for filtering Bluetooth advertisements based on their data. Sam\
    e\r\
    \n# usage as with 'addressRegex'.\r\
    \n:local advertisingDataRegex \"\"\r\
    \n\r\
    \n# Signal strength filter. E.g. -40 would only include Bluetooth advertisement\
    s\r\
    \n# whose signal strength is stronger than -40dBm.\r\
    \n# To disable this filter, set it to \"\"\r\
    \n:local rssiThreshold \"\"\r\
    \n\r\
    \n#Name the KNOT. Identity of the unit that will be sending the message. This n\
    ame will be reported to the MQTT broker.\r\
    \n:local gwName \"KNOT_A\"\r\
    \n\r\
    \n################################## Bluetooth ################################\
    ##\r\
    \n:put (\"[*] Gathering Bluetooth info...\")\r\
    \n\r\
    \n:global makeRecord do={\r\
    \n    :local jsonStr \"{\\\"ts\\\":\$ts,\\\"values\\\":{\\\"reporter\\\":\\\"\$\
    gwName\\\",\\\"rssi\\\":\$rssi}}\"\r\
    \n    :return \$jsonStr\r\
    \n}   \r\
    \n\r\
    \n# array of record strings collected for each advertising MAC address\r\
    \n:global macRecords [:toarray \"\"]\r\
    \n\r\
    \n# process advertisements and update macRecords\r\
    \n:local advertisements [/iot/bluetooth/scanners/advertisements/print detail as\
    -value where \\\r\
    \naddress ~ \$addressRegex and \\\r\
    \ndata ~ \$advertisingDataRegex and \\\r\
    \nrssi > \$rssiThreshold]\r\
    \n\r\
    \n/iot/bluetooth/scanners/advertisements/clear\r\
    \n\r\
    \n:foreach adv in=\$advertisements do={\r\
    \n:local address (\$adv->\"address\")\r\
    \n:local rssi (\$adv->\"rssi\")\r\
    \n:local epoch (\$adv->\"epoch\")\r\
    \n                \r\
    \n:local recordStr [\$makeRecord ts=\$epoch gwName=\$gwName rssi=\$rssi]\r\
    \n\r\
    \n:if ([:len (\$macRecords->\$address)] > 0) do={\r\
    \n:local str (\$macRecords->\$address)\r\
    \n:local newStr \"\$str,\$recordStr\"\r\
    \n:set (\$macRecords->\$address) \$newStr} else={:set (\$macRecords->\$address)\
    \_\$recordStr}}\r\
    \n\r\
    \n# TODO: add some logic to decide when we want to send data\r\
    \n:local sendData true\r\
    \n\r\
    \n:if (\$sendData) do={\r\
    \n:local jsonStr \"{\"\r\
    \n\r\
    \n:foreach addr,advRec in=\$macRecords do={\r\
    \n:set jsonStr \"\$jsonStr\\\"\$addr\\\":[\$advRec],\"}\r\
    \n\r\
    \n:local payloadlength\r\
    \n:set payloadlength [:len (\$jsonStr)]\r\
    \n:local remcom\r\
    \n:set remcom [:pick \$jsonStr 0 (\$payloadlength-1)]\r\
    \n:set jsonStr \"\$remcom}\"\r\
    \n:local message\r\
    \n:set message \"\$jsonStr\"\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Message structured: \$message\")\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\"\$broker\" topic=\"\$topic\" message=\$message}"
```

脚本应出现在“System>Scripts>Script List”选项卡下，名称为“tracking”，或者使用命令 `/system/script/print` 查看。

有一些脚本行需要您注意。

broker 名称配置行是您需要输入已设置的 MQTT broker 名称的地方：

>      :local broker "tb"

您需要输入 MQTT broker 使用的正确主题。有关更多详细信息，请查看 [ThingsBoard 文档](https://thingsboard.io/docs/reference/gateway-mqtt-api/)。默认情况下，主题应为：

>      :local topic "v1/gateway/telemetry"

MAC 地址过滤选项位于脚本本身内部。您可以输入 MAC 地址的所有 6 个八位字节（将过滤器应用于 1 个特定标签），也可以使用几个八位字节过滤列表，例如“^BC:33:AC”（应用过滤器，以便只处理以“BC:33:AC:...”开头的 MAC 地址）：

>     :local addressRegex "DC:2C:6E:0F:C0:3D"

负载内容/数据行。它允许您根据特定负载内容过滤列表，例如“[制造商数据](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-MikroTikPDUPayloadstructure)”。例如，“15ff4f09”将丢弃所有非 MikroTik 格式的负载：

>     :local advertisingDataRegex "15ff4f09"

RSSI 信号强度过滤选项。此过滤选项在“[场景说明](#scenario-explanation)”部分中提到。此过滤器允许您忽略任何 RSSI 弱于配置值的负载。例如，“-40”将只包括信号强度强于 -40dBm 的蓝牙广播：

>     :local rssiThreshold "-40"

KNOT 标识符行。您需要为每个唯一的 KNOT 更改它。例如，将您的第一个 KNOT 命名为 →  KNOT\_A，将您的第二个 KNOT 命名为 →  KNOT\_B：

> :local gwName "KNOT\_A"

脚本的其余部分无需更改/修改

脚本运行时如何工作？脚本使用应用的过滤器“检查”“Advertising reports”选项卡（负载列表选项卡），并构建一条 JSON 消息。JSON 消息的示例如下：

```
{
  "2C:C8:1B:4B:BB:0A": [
    {
      "ts": 1678967250600,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -47
      }
    }
  ],
  "DC:2C:6E:0F:C0:3D": [
    {
      "ts": 1678967247850,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -59
      }
    },
    {
      "ts": 1678967257849,
      "values": {
        "reporter": "KNOT_A",
        "rssi": -67
      }
    }
  ]
}
```

数据按照 [ThingsBoard 指南](https://thingsboard.io/docs/reference/gateway-mqtt-api/#telemetry-upload-api) 构建，其中 `2C:C8:1B:4B:BB:0A` 和 `DC:2C:6E:0F:C0:3D` 是出现在 KNOT 范围内的标签的 MAC 地址，`ts` 是标签广播的每个负载的 Unix 时间戳（毫秒），`reporter` 指示哪个特定的 KNOT 发送了消息，`rssi` 是标签广播的每个负载的信号强度（dBm）。

在“搜索”负载列表并构建 JSON 消息后，蓝牙接口负载列表被“清理”（或“刷新”），然后先前构建的 JSON 消息被发送到 ThingsBoard MQTT broker。

要运行脚本，请使用命令：

```ros
/system/script/run tracking
```

###### 调度器

为脚本应用调度器，以便 RouterOS 定期自动启动脚本：

```ros
/system/scheduler/add name=bluetoothscheduler interval=30s on-event="/system/script/run tracking"
```

您可以设置更短或更长的间隔。如果您想更频繁地发送数据，以使数据“更新鲜”→ 设置较短的时间间隔（10-15 秒）。如果您想减少消息发送频率 → 可以设置较长的时间间隔（30 分钟以上）。

使用脚本构建的 JSON 消息为每个收到的负载分配了一个 `ts` 值（时间戳）。这意味着**当脚本运行时**，例如，**每分钟**，使用 1 个标签，**标签每 10 秒广播** 1 个负载（即**每分钟 6 个负载**）→ ThingsBoard 数据（GUI）将每分钟更新一次，并且每分钟将出现 6 个新条目（每个条目将指示它是在前一个条目之后 10 秒收到的）。如果您每 15 分钟发送一次消息，使用 1 个每 10 秒广播一个负载的标签（即每 15 分钟 6\*15=90 个负载）→ ThingsBoard 数据（GUI）将每 15 分钟更新一次，但会出现 90 个条目。

#### ThingsBoard 数据可视化和结果验证

在您使用 `/system/script/run tracking` 或通过调度器运行脚本并刷新 GUI 门户后，JSON 消息中找到的所有 MAC 地址（标签）将在 ThingsBoard GUI 下成为新设备：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-06.webp)

为了帮助您可视化数据，您可以使用内置的[小部件](https://thingsboard.io/docs/user-guide/ui/widget-library/)或创建自己的小部件。

从设备列表中选择标签的 MAC 地址，转到“Latest telemetry”部分，检查“reporter”参数，然后点击“Show on widget”按钮：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-07.webp)

选择您希望使用的小部件，例如，在“Cards”包下的“Timeseries table”，然后点击“Add to dashboard”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-08.webp)

创建一个新的仪表板并随意命名。点击“Add”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-09.webp)

对出现在“Devices”选项卡下的其他标签执行相同步骤。在同一仪表板下为每个唯一标签创建新小部件。

将小部件的“Timewindow”从“Realtime-last minute”（默认使用）更改为“Realtime-current day”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-10.webp)

结果，如果两个标签都在 **KNOT A** **范围内**，仪表板将显示：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-11.webp)

如果它们移动到 **KNOT B 范围**，它将显示：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-12.webp)

如果标签移动到**重叠区域**，即两个范围内，两个报告者（KNOT\_A 和 KNOT\_B）应在几秒钟内出现，具体取决于调度器中使用的间隔：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-13.webp)

### 示例 #2

在第二个示例中，我们将展示另一个拓扑：

![](../img/knot_example_2.png)

我们有几个仓库、几辆公司送货车辆和 3 个需要追踪的资产。我们的资产是装载货物的托盘，我们的目标是了解：

- 资产（配备标签）当前位于哪个特定仓库（配备 KNOT），以及它在特定仓库内停留了多长时间。
- 资产（配备标签）是否在路上，在仓库之间运输，以及它在车辆（配备 KNOT）内停留了多长时间。
- **（可选）如果使用 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 标签**，这段时间内的温度是多少？您也可以/或者监控您可以从广播的[负载](https://help.mikrotik.com/docs/display/UM/MikroTik+Tag+advertisement+formats#heading-Example)中获取的其他参数，例如加速度。
- **（可选）** 获取 KNOT 的 GPS 位置。

要实现蓝牙资产追踪，只需在每个仓库安装 1 个 KNOT，每辆车安装 1 个 KNOT，每个资产安装 1 个标签。

我们可以看到 TAG 1 在车辆内，而这辆车刚刚停在仓库附近。KNOT 1 和 KNOT 4 都将向服务器报告资产在其范围内。这将告诉您资产已停放但尚未开始运输。

我们可以看到 TAG 2 正在仓库之间运输，并且只在 KNOT 5 的蓝牙范围内。在这种情况下，KNOT 5 将是唯一的报告者，服务器上显示的结果将意味着资产正在运输中。

我们可以看到 TAG 3 在仓库内。服务器将仅指示这一点。

服务器上的数据将显示 KNOT 发送的每个报告的时间戳，这将告诉您资产在特定设备的蓝牙范围内停留了多长时间。

#### 配置

在此示例中，我们将展示一个基本拓扑，包含 2 个仓库、1 辆在它们之间行驶的车辆/卡车，以及 1 个资产/托盘/标签。

##### ThingsBoard 准备

请查看[此处](../../mqtt/mqtt-and-thingsboard-configuration.md)的指南，了解如何设置 ThingsBoard 和 RouterOS 以利用 MQTT 通信。

:::tip
为简单起见，此示例将展示[访问令牌](../../mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1)方案，但您也可以使用其他可用选项。对于生产环境，建议使用 SSL-MQTT，因为非 SSL-MQTT 容易被数据包捕获和检查。

要了解如何在通过[容器](../../../containers/index.md)运行的实例上实现 SSL-MQTT 通信，请查看[此处](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md)链接的指南（[启用 HTTPS 和 SSL MQTT](../../../containers/user-guides/container-thingsboard-mqtt-http-server.md#enabling-https-and-ssl-mqtt) 部分）。
:::

在 ThingsBoard GUI 下创建 3 个 KNOT，并将它们设为“网关”。

转到“Devices”部分，点击“+”按钮和“Add new device”：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-02.webp)

命名设备并勾选“Is gateway”选项：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-14.webp)

为您拥有的每个 KNOT 执行此操作：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-15.webp)

在您刚创建的设备下，在“Manage credentials”选项卡中为每个 KNOT 设置唯一的访问令牌（唯一凭据）：

![](https://manual.mikrotik.com/docs/internet-of-things/bluetooth/user-guides/img/bluetooth-tag-tracking-mqtt-thingsboard-16.webp)

##### RouterOS 配置

###### 准备

在继续之前，我们需要确认我们的蓝牙标签确实出现在 KNOT 的蓝牙范围内，并且 KNOT 能够检测到它。为此，您可以执行命令 `/iot/bluetooth/scanners/advertisements/print`：

```ros
/iot/bluetooth/scanners/advertisements/print
 # DEVICE     PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0 bt1        adv-noconn-ind  2023-03-08 12:35:15 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100b0110100ffff00000019d68d2300005d   
 1 bt1        adv-noconn-ind  2023-03-08 12:35:16 public       DC:2C:6E:0F:C0:3D        -39dBm         22 15ff4f0901008f3cfcfffbfffaff301783c22c000064   
 2 bt1        adv-noconn-ind  2023-03-08 12:35:35 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f09010084d500000400ffff0319ea8d2300005d   
 3 bt1        adv-noconn-ind  2023-03-08 12:35:45 public       2C:C8:1B:4B:BB:0A        -50dBm         22 15ff4f090100e607faffffff03000319f48d2300005d   
```

或者您可以使用 [Webfig](../../../management-tools/webfig.md) 或 [Winbox](../../../management-tools/winbox.md) 在 IoT>Bluetooth>Advertising reports 选项卡下查看。

列表可能比较混乱。由于扫描器会捕获周围所有内容，列表中可能会出现随机负载。为帮助减少列表内容，您可以使用标签的 MAC 地址进行过滤 `/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D`：

```ros
/iot/bluetooth/scanners/advertisements/print where address=DC:2C:6E:0F:C0:3D
 # DEVICE    PDU-TYPE        TIME                 ADDRESS-TYPE ADDRESS                    RSSI     LENGTH DATA                                           
 0