# 将TG-BT5-OUT标签的温度读数发送至ThingsBoard

> 我们的 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 蓝牙标签型号内置温度传感器。这意味着它可用于测量周围环境温度。

### 引言

我们的 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 蓝牙标签型号内置温度传感器。这意味着它可用于测量周围环境温度。

温度值被“写入”到标签通过蓝牙广播信道广播的广播负载中。根据您对标签的配置方式，标签可以定期广播负载，或在检测到触发事件时广播负载。您可以在[链接章节](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/)中找到有关标签配置选项的更多信息。

您可以使用我们的 [KNOT](https://mikrotik.com/product/knot) 型号在 **IoT>Bluetooth>Advertising reports** 标签页下查看/显示负载：

![](../../img/image2022-8-24_10-6-47.webp)

负载将显示在“Advertisement (hex)”字段中，格式为**十六进制**。

当标签配置为MikroTik格式时，负载的第14和第15个八位组表示广播时刻“感知”到的温度（以**有符号16位整数[二进制补码] 8.8定点格式**表示的环境温度，单位为摄氏度）。

以下为MikroTik格式负载的示例：

| 15ff4f09010032a500000000ffff `5019` bd5954000061 |
| --- |

请注意，负载中的所有多字节值均为小端序。因此，如果第14和第15个八位组表示温度为“**50 19**”→ 您需要交换八位组位置，变为0x**1950**。

正温度：

我们捕获到的温度为0x**1950**（十六进制）→ **6480**（十进制）。要获取实际温度值，请将结果除以256 → 6480/256=**25.31 C**。

负温度：

我们捕获到的温度为0x**FE80**（十六进制）。请记住，**使用的是二进制补码格式** → **-384**（有符号二进制补码的十进制值）。要获取实际温度值，请将结果除以256 → -384/256=**-1.5 C**。

基于以上知识，我们可以利用RouterOS脚本从接收到的负载中构建消息，并将其发送至MQTT/HTTP服务器。建议由服务器负责将数据从**十六进制**格式转换为**十进制**格式。**但是！** 如果您愿意增加RouterOS设备的负载，您可以使用RouterOS脚本执行**十六进制**值到**十进制**格式的转换（这会增加设备负载并可能影响RouterOS性能 → 我们建议在服务器上进行值转换，而非在RouterOS上）。在本指南中，我们将通过MQTT发布至[ThingsBoard](https://thingsboard.io/)来实现目标。

### ThingsBoard服务器与MQTT配置

您需要有一个运行中的ThingsBoard服务器。您可以通过[链接](https://thingsboard.io/docs/installation/)找到有关如何设置服务器的有用信息。您可以将服务器本地安装到一台机器上，或使用其云解决方案。

服务器准备就绪后，您需要对其进行配置以接收MQTT消息。请按照[ThingsBoard配置](/docs/internet-of-things/mqtt/mqtt-and-thingsboard-configuration)链接设置您的“设备”。

### RouterOS配置

请查看[此链接](/docs/internet-of-things/mqtt/mqtt-and-thingsboard-configuration)，了解如何根据ThingsBoard服务器使用的设备凭据设置MQTT代理。

设置好代理后，请确认蓝牙标签正在广播信息，如上图**IoT>Bluetooth>Advertising reports**标签页所示。

#### 脚本

将以下脚本粘贴到（**System>Scripts>Add**下）：

```ros
## 所需软件包：iot

################################ 配置 ################################
## 用于发布的现有MQTT代理名称
 :local broker "tb"

## 消息发布的目标MQTT主题
 :local topic "v1/devices/me/telemetry"

 # 其MAC地址应作为“定位器ID”的接口
:local locatorIface "ether1"

## 用于过滤广播蓝牙地址的POSIX正则表达式。例如“^BC:33:AC”
## 将仅包含以这三个八位组开头的地址。
## 要禁用此过滤器，请将其设置为“”
:local addressRegex "2C:C8:1B:4B:BB:0A"

## 用于根据数据过滤蓝牙广播的POSIX正则表达式。用法
## 与'addressRegex'相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如-40将仅包含信号强度强于-40dBm的蓝牙广播。
## 要禁用此过滤器，请将其设置为“”
:local rssiThreshold ""

####以下行用于将数据从十六进制转换为十进制###

    :global invertU16 do={
        :local inverted 0
        :for idx from=0 to=15 step=1 do={
            :local mask (1 &lt;&lt; $idx)
            :if ($1 & $mask = 0) do={
                :set $inverted ($inverted | $mask)
            }
        }
        return $inverted
    }

    :global le16ToHost do={
        :local lsb [:pick $1 0 2]
        :local msb [:pick $1 2 4]

        :return [:tonum "0x$msb$lsb"]
    }
    :local from88 do={
        :global invertU16
        :global le16ToHost
        :local num [$le16ToHost $1]

        # 处理负数
        :if ($num & 0x8000) do={
            :set num (-1 * ([$invertU16 $num] + 1))
        }

        # 从8.8格式转换。由于不支持浮点数，按1000缩放
        :return (($num * 125) / 32)
    }

################################## 蓝牙 ##################################
:put ("[*] 正在收集蓝牙信息...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # 自启动以来首次运行此脚本，需要初始化
    # 持久变量
    :set $btOldestAdvertisementTimestamp 0
}
:local btProcessingStart [/system clock get time]
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advJson ""
:local advCount 0
:local advSeparator ""
:local lastAdvTimestamp 0
## 从MAC/蓝牙地址中移除分号
:local minimizeMac do={
    :local minimized
    :local lastIdx ([:len $address] - 1)
    :for idx from=0 to=$lastIdx step=1 do={
        :local char [:pick $address $idx]
        :if ($char != ":") do={
            :set $minimized "$minimized$char"
        }
    }
    :return $minimized
}

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local ts ($adv->"epoch")
    :local rssi ($adv->"rssi")
    :local ad ($adv->"data")
    :local tempf [:pick ($adv->"data") 28 32]

#以下行将以十六进制格式设置温度，例如“0x1950”
    :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])

#以下行将以十进制格式设置温度，例如“25313”。该行以“#”注释，因此如果您希望使用它代替十六进制格式值，请注释上面一行并取消注释下面一行 > 从下面一行移除“#”并在上面一行添加“#”。

##    :local temp [$from88 [:pick $ad 28 32]]

    :local obj "{\
        \
           \"ts\":$ts,\
           \"values\":{\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"rssi\":\"$rssi\",\
            \"temp\":\"$temp\",\
            \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # 确保最后一个对象不以逗号结尾
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","}
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] 发现 $advCount 条新广播 \
    (处理时间: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "[$advJson]"
:log info "$message";
:put ("[*] 消息总大小: $[:len $message] 字节")
:put ("[*] 正在向MQTT代理发送消息...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] 完成")
```

**更改您为MQTT代理选择的代理名称**（在引号内，在我们的示例中，我们将其命名为 **tb**）：

```
 :local broker "tb"
```

ThingsBoard使用的默认主题为（您无需更改）：

```
 :local topic "v1/devices/me/telemetry"
```

**更改您希望监控的标签的MAC地址**（在我们的示例中，MAC地址为 **2C:C8:1B:4B:BB:0A**）：

```
:local addressRegex "2C:C8:1B:4B:BB:0A"
```

以下行将获取负载的第14和第15个八位组，并将值从“ABCD”“重新构建”为“CDAB”（根据我们**引言**部分的示例，从“**5019**”变为“**1950**”）→ 基本上构建包含**十六进制**格式温度的消息：

```
    :local tempf [:pick ($adv->"data") 28 32]
    :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])
```

您的第二个选项是使用RouterOS将温度从**十六进制**转换为**十进制**格式（如果您希望保留十六进制格式，请忽略此步骤）。这可以通过“注释”（添加`#`）上一行（或完全删除）并“取消注释”（移除`#`）下一行来实现，如下所示：

```
#  :local temp ([:pick $tempf 2 4].[:pick $tempf 0 2])
    :local temp [$from88 [:pick $ad 28 32]]
```

由于不支持浮点数 → 小数点后的所有计算都将“四舍五入”为整数。这就是脚本将温度**按1000缩放**（乘以**1000**）的原因，因此温度将显示为“**25546**”（表示25.546 C）。您可以添加额外的脚本设置小数点（但请记住，额外的操作会增加设备负载），您也可以在服务器端执行此操作。

我们发布的MQTT消息在以下部分构建（您无需更改）：

```
    :local obj "{\
        \
           \"ts\":$ts,\
           \"values\":{\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"rssi\":\"$rssi\",\
            \"temp\":\"$temp\",\
            \"ad\":\"$ad\"\
            }\
        }"
```

按照上述示例构建的消息将以JSON格式显示（我们唯一需要关注的实际值是“时间戳”→“ts”和“温度”→“temp”，因此您可以随意移除其他参数）。如果温度以**十六进制**格式计算，消息将如下所示：

```
[
  {
    "ts": 1661333913375,
    "values": {
      "id": "2CC81B4BBB0A",
      "rssi": "-43",
      "temp": "1939",
      "ad": "15ff4f0901002de0ffff010000003919877c54000061"
    }
  }
]
```

如果温度以**十进制**格式计算，消息将如下所示：

```
[
  {
    "ts": 1661333913375,
    "values": {
      "id": "2CC81B4BBB0A",
      "rssi": "-43",
      "temp": "25222",
      "ad": "15ff4f0901002de0ffff010000003919877c54000061"
    }
  }
]
```

保存脚本并运行：

```ros
[admin@MikroTik] > system script run name_of_the_script
[*] 正在收集系统信息...
[*] 正在收集蓝牙信息...
[*] 发现 1 条新广播 (处理时间: 00:00:00)
[*] 消息总大小: 134 字节
[*] 正在向MQTT代理发送消息...

[*] 完成
[admin@MikroTik] > 
```

#### 调度器

为脚本应用调度器，以所需间隔运行。**请注意！** 如果您设置了调度器以例如每2分钟运行脚本，则意味着在2分钟间隔内接收到的每个负载（由标签广播）都将被“构建”到MQTT消息中。您很可能不需要每2-5秒了解标签的温度，因此您可以更改构建的MQTT消息以仅发布最新温度读数，或者只需将**IoT>Bluetooth>Scanners**设置中的**Filter duplicates**更改为“**keep-newest**”（这样，蓝牙扫描器将覆盖来自每个单独标签MAC地址的每个新报告），脚本将仅发布脚本运行时“扫描”到的1个负载。

#### 结果

您可以在为ThingsBoard创建的设备下的**Latest telemetry**部分验证结果（在我们的示例中，我们将“设备”命名为 **KNOT**）：

![](../../img/image-2022-9-30_10-43-31.webp)

结果是MQTT发布成功！从上面的截图可以看出，**temp**参数为**十六进制**格式。

**但是！** 我们希望以**十进制**格式显示温度（**temp**参数），并且希望数据更易于理解。

此外，如果我们以**十进制**格式发布温度，我们希望设置小数点。

这就是[Widgets](https://thingsboard.io/docs/reference/widgets/widget-library/)发挥作用的地方。

### ThingsBoard Widgets

在**Latest telemetry**部分收到值后，您可以将其显示在[**Widget**](https://thingsboard.io/docs/reference/widgets/widget-library/)上。

Widget中使用的Javascript应能够将数据从十六进制格式转换为十进制格式。

选择您希望在Widget中显示的值（在我们的示例中为 **temp**），然后点击“**Show on widget**”按钮：

![](../../img/image-2022-9-30_10-45-21.webp)

您可以在弹出的窗口中浏览Widgets：

![](../../img/image-2022-9-30_10-47-43.webp)

点击“**Add to dashboard**”按钮：

![](../../img/image-2022-9-30_10-48-48.webp)

选择创建新仪表板或选择您已预先安装/预先制作的现有仪表板。点击“**Add**”。

通过勾选“**Open dashboard**”复选框，您将被重定向到仪表板菜单，或者您可以手动前往。

我们还添加了第二个表格，因此我们的测试仪表板如下所示：

![](../../img/image-2022-9-30_10-50-41.webp)

#### 如果我们以十六进制格式发布数据

两个表格都将以**十六进制格式**显示值为“17f9”（原始值，如同我们从KNOT发送的一样 → 表格的javascript尚未将其转换为十进制值）。

由于我们标签负载中的值采用有符号8.8定点格式（请记住二进制补码格式），我们需要添加额外的javascript代码来将数据“转换”为十进制值。

进入“**Edit**”模式并点击“**Edit widget**”按钮：

![](../../img/image-2022-9-30_10-51-59.webp)

点击“**edit**”按钮编辑参数 **temp**：

![](../../img/image2022-8-24_14-23-30.webp)

在弹出窗口“**Data key configuration**”中，启用“**Use data post-processing function**”复选框并输入以下代码：

![](../../img/image-2022-9-30_10-54-5.webp)

代码：

```
function f(p){

this.p = p;

}

f.prototype.calculate = function(mes){

let intValue = parseInt(mes, 16);

let sign = 1;

if(intValue & 0x8000) {

intValue = (~intValue + 1) & 0xFFFF;

sign = -1;

}

intValue = sign * intValue / Math.pow(2, this.p);

return intValue;

}

let res = new f(8);

return (res.calculate(value));
```

保存并应用更改。

对第二个/第一个表格执行相同步骤。

#### 如果我们以十进制格式发布数据

您将看到如下结果：

![](../../img/image-2022-9-27_11-48-5.webp)

执行与上述示例完全相同的步骤，但对于此场景，**将结果除以“1000”**：

![](../../img/image-2022-9-27_11-51-16.webp)

保存并应用更改。

#### 验证

最终结果应如下所示：

![](../../img/image2022-8-24_14-29-27.webp)

现在两个表格均显示**十进制温度**。
:::info
您也可以在将遥测数据保存到ThingsBoard之前对其进行转换。使用此场景，每次打开仪表板时都不会进行后处理。

以下指南可作为转换数据的通用方法：[Transformation nodes](https://thingsboard.io/docs/user-guide/rule-engine-2-0/transformation-nodes/)。
:::