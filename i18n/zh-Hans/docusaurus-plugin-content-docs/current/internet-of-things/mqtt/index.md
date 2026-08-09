# MQTT

> 本页面记录了 MikroTik RouterOS 中的 MQTT 集成，涵盖面向 Kaa 和 ThingsBoard 等 IoT 平台的发布者/订阅者工作流程。它解释了 MQTT 协议基础、RouterOS 作为 MQTT 代理/客户端的能力，并提供了 AWS/Azure 云平台的配置示例。

import DocCardList from '@theme/DocCardList';

# MQTT

本节涵盖 MQTT 集成示例。使用它可将 RouterOS MQTT 发布和订阅工作流程连接到 Kaa IoT 和 ThingsBoard 等 IoT 平台。

<DocCardList />

MQTT 是一种开放的 OASIS 和 ISO 标准轻量级发布-订阅网络协议，用于在设备之间传输消息。典型的 MQTT 通信拓扑包括：

- MQTT 发布者 → 向服务器发送信息的设备。
- MQTT 代理 → 存储数据的服务器。
- MQTT 订阅者 → 读取/监控服务器上发布数据的设备。

RouterOS 可以充当 MQTT 发布者和订阅者（从 **7.11beta2** 开始）。您还可以通过 [container](../../containers/index.md) 功能运行 MQTT 代理/服务器。有关 Mosquitto MQTT 代理配置，请访问 [此链接](../../containers/user-guides/container-mosquitto-mqtt-server.md)。

您可以在下方找到 MQTT 发布场景的应用示例：

a) [使用 AWS 云平台的 MQTT/HTTPS 示例](https://help.mikrotik.com/docs/pages/viewpage.action?pageId=63045633)

b) [使用 Azure 云平台的 MQTT 示例](https://help.mikrotik.com/docs/display/UM/MQTT+and+Azure+configuration)

c) [MQTT 和 ThingsBoard 配置](./mqtt-and-thingsboard-configuration.md)

请注意，AWS 和 Azure 示例（脚本）展示了发布蓝牙标签数据。目前，只有 [KNOT](https://mikrotik.com/product/knot) 内置了蓝牙芯片。

## 配置

**子菜单：** `/iot/mqtt`

***注意**：* 需要 **iot** 软件包。

IoT 软件包随 RouterOS 6.48.3 版本提供。您可以从我们的 [下载页面](https://mikrotik.com/download) - “Extra packages” 下获取。

| 属性 | 描述 |
| :-- | :-- |
| **brokers** | 已配置的 MQTT 代理列表。 |
| **connect** | 指定要连接的代理的命令。 |
| **disconnect** | 指定要断开连接的代理的命令。 |
| **publish** | 定义需要发布的 MQTT 消息的命令。 |
| **subscribe** | 定义要订阅的 MQTT 主题的命令。 |
| **subscriptions** | 已订阅主题和接收消息的列表。 |
| **unsubscribe** | 指定要取消订阅的主题的命令。 |

### 代理

**子菜单：** `/iot/mqtt/brokers`

要添加新的 MQTT 代理（或 MQTT 服务器），请运行以下命令：

```ros
/iot/mqtt/brokers/add
```

可配置属性如下所示：

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP\|主机名*; 默认：) | 代理的 IP 地址或主机名。 |
| **auto-connect** (*yes \| no*; 默认：**no**) | 启用后，当与 MQTT 代理的连接中断/被干扰时，RouterOS 将反复尝试重新建立连接。 |
| **certificate** (*字符串*; 默认：) | 用于 SSL 连接的 [证书存储中的证书](../../authentication-authorization-accounting/certificates.md)。 |
| **client-id** (*字符串*; 默认：) | 用于连接的唯一 ID。代理使用此 ID 来识别客户端。 |
| **keep-alive** (*整数：30..64800*; 默认：**60**) | 定义客户端应向 MQTT 代理“ping”以确认其“存活”的时间（以秒为单位）的参数，以确保连接持续进行。此值应根据 MQTT 代理设置进行配置。 |
| **name** (*字符串*; 默认：) | 代理的描述性名称。 |
| **parallel-scripts-limit**(*整数：3..1000;* 默认：off) | 定义此代理的 [on-message](#subscriptions) 功能允许同时运行的脚本数量的参数。在大量消息持续发布的情况下，可用于降低 CPU 使用率。 |
| **password** (*字符串*; 默认：) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 代理的密码（如果代理要求）。 |
| **port** (*整数：*0..4294967295**; 默认：**1883**) | 代理使用的网络端口。 |
| **ssl** (*yes \| no*; 默认：**no**) | 安全套接层配置。 |
| **username** (*字符串*; 默认：) | 代理的用户名（如果代理要求）。 |
| **will-message** (*字符串*; 默认：) | 配置遗嘱消息（LWT），该消息将在连接期间发送给代理。此消息将存储在代理上。除非 RouterOS 意外断开与代理的连接（未发送正确的“DISCONNECT”数据包），否则此消息不会被（代理）发布。 |
| **will-qos**(*整数*; 默认：) | 配置 LWT 消息的 QoS 值。 |
| **will-retain**(yes \| no; 默认：) | 配置是否保留 LWT 消息。 |
| **will-topic**(*字符串*; 默认：) | 配置 LWT 主题，**will-message** 应发布到该主题。 |

添加代理的示例：

```ros
/iot/mqtt/brokers/add name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60
```

结果：

```ros
/iot/mqtt/brokers/print
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no 
```

### 连接

**子菜单：** `/iot/mqtt/connect`

要连接到预先配置的 MQTT 代理，请发出命令：

```ros
/iot/mqtt/connect broker="broker"
```

如果连接成功，“**connected**”参数应更改为“**yes**”：

```ros
/iot/mqtt/brokers/print
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=yes
```

### 断开连接

**子菜单：** `/iot/mqtt/disconnect`

要断开与 MQTT 代理的连接，请发出命令：

```ros
/iot/mqtt/disconnect broker="broker"
```

要确认代理已断开连接，请发出以下命令，它应显示“**connected=no**”：

```ros
/iot/mqtt/brokers/print            
 0 name="broker" address="192.168.88.33" port=1883 ssl=no client-id="test-client" auto-connect=no keep-alive=60 connected=no 
```

### 发布

**子菜单：** `/iot/mqtt/publish`

Publish 菜单用于向 MQTT 代理发送 MQTT 消息。

| 属性 | 描述 |
| :-- | :-- |
| **broker** (*字符串*; 默认：) | 选择要发布消息的代理。 |
| **disconnect-after** (*yes \| no*; 默认：**no**) | 确保在发布消息发送后自动断开与代理的连接的参数。 |
| **force** (*yes \| no*; 默认：**yes**) | 如果设置为“yes”，当与代理的连接尚未建立（“**connected=no**”）且尝试发布消息时，RouterOS 将首先尝试与指定代理建立 MQTT 连接，然后发布消息。如果设置为“no”，除非连接已事先建立（“**connected=yes**”），否则 RouterOS 将无法发送消息。 |
| **message** (*字符串*; 默认：) | 您希望发布到代理的消息。 |
| **qos** (*整数：*0..2**; 默认：**0**) | 服务质量参数，由代理定义。qos=0 → 消息最多接收一次（消息发送...即发即忘）；qos=1 → 消息至少接收一次（消息持续发送，直到发布者收到代理的确认数据包 <code>PUBACK</code>）；qos=2 → 消息恰好接收一次（消息发送并进行四次握手以确保仅传递一次）； |
| **retain** (*yes \| no*; 默认：**no**) | 是否保留消息，或者如果没有人订阅该主题则丢弃它。此参数由代理定义。保留的消息保存在代理上，并由代理自动发送给新订阅者。 |
| **topic** (*字符串*; 默认：) | 主题，由代理定义。 |

发布消息的示例：

```ros
/iot/mqtt/publish message="test-message" broker="broker" topic="my/test/topic"
```

### 订阅

**子菜单：** `/iot/mqtt/subscribe`

:::info
请记住，如果您与代理有持续连接（连接处于“**connected=yes**”状态）并通过该代理订阅主题，则必须重新建立连接！
:::

此菜单用于订阅代理的 MQTT 主题。

| 属性 | 描述 |
| :-- | :-- |
| **broker** (*字符串*; 默认：) | 选择要订阅的代理。 |
| **force** (*yes \| no*; 默认：**yes**) | 如果设置为“yes”，当与代理的连接尚未建立（“**connected=no**”）且尝试订阅时，RouterOS 将首先尝试与指定代理建立 MQTT 连接，然后订阅主题。如果设置为“no”，除非连接已事先建立（“**connected=yes**”），否则 RouterOS 将无法订阅主题。 |
| **qos** (*整数：*0..2**; 默认：**0**) | 服务质量参数，由代理定义。 |
| **topic** (*字符串*; 默认：) | 要订阅的主题，由代理定义。 |

#### 订阅示例

```ros
/iot/mqtt/subscribe broker="broker" topic="my/test/topic"
```

也支持通配符（单级“**+**”和多级“**#**”）订阅（RouterOS **不允许发布**到通配符主题，**但允许订阅**它们）：

```ros
/iot/mqtt/subscribe broker="broker" topic="my/test/#"
/iot/mqtt/subscribe broker="broker" topic="my/test/+"
```

这意味着，如果您订阅了 `topic="my/test/#"`，您将能够接收发布到任何以通配符“#”之前的模式开头的主题的消息（例如，`"my/test/topic"`、`"my/test/topic/something"`）。

并且，如果您订阅了 `topic="my/test/+"`，您将能够接收发布到该主题 +1 级别的消息（例如，`"my/test/topic"`、`"my/test/something"`）。

### 订阅管理

**子菜单：** `/iot/mqtt/subscriptions`

本节用于管理已添加的订阅（之前通过 [Subscribe](./index.md#subscribe) 部分添加的）。

它具有与 [Subscribe](./index.md#subscribe) 部分相同的属性。

:::info
从 **v7.12beta9** 开始，此菜单允许您向订阅添加“**on-message**”设置。
:::

| 属性 | 描述 |
| :-- | :-- |
| **on-message** (*字符串*; 默认：) | 配置一个 [脚本](../../developer-guides/scripting/index.md)，该脚本将在订阅主题中收到新消息时自动启动/运行。 |

要检查已订阅的主题，请发出命令：

```ros
/iot/mqtt/subscriptions/print
0 broker=broker topic="my/test/topic" qos=0
```

在您按照上述 **Publish** 部分所示发布测试消息后：

```ros
/iot/mqtt/publish message="test-message" broker="broker" topic="my/test/topic"
```

您应该能够在以下位置检查收到的消息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=broker topic="my/test/topic" data="test-message" time=2023-05-22 16:57:00 
```

:::info
收到的消息列表限制为 1024 条，之后较旧的条目将被新条目覆盖。
:::

要清除存储的消息，请发出命令：

```ros
/iot/mqtt/subscriptions/recv/clear
```

要在订阅主题中出现任何新消息时运行 [脚本](../../developer-guides/scripting/index.md)（例如，一个基本的“log”脚本），您可以使用 `on-message` 功能：

```ros
/iot/mqtt/subscriptions/set on-message={:log info "Got data {$msgData} from topic {$msgTopic}"} broker=broker 0
```

脚本可以使用 **$msgData** 和 **$msgTopic** 变量。**$msgData** 定义已发布的 MQTT 消息，**$msgTopic** 定义消息发布到的 MQTT 主题。当新消息出现时，这两个变量会自动生成。

:::note

- **$msgData** 和 **$msgTopic** 变量在“**System>Script**”部分创建的脚本中使用时将不起作用，也就是说，它们不会在“/iot/mqtt/subscriptions/set **on-message=\{`/system/script/run` x}**”添加的脚本中起作用。这两个变量仅在“**on-message=\{}**”编写的脚本内部使用时才起作用，例如“**on-message=\{:log info "Got data \{$msgData} from topic \{$msgTopic}"}**”。
- 这同样适用于 [全局](../../developer-guides/scripting/index.md#scopes) 变量的使用。如果存在使用其他脚本“生成”的全局变量（出现在 System>Script>Environment 部分下的变量），它们将无法在“on-message”脚本中工作。

:::

在您向订阅主题发布新的 MQTT 消息后，应出现新的日志条目：

```ros
/log/print
10:19:15 script,info Got data {test-message} from topic {my/test/topic}
```

第二个示例展示了如何在特定消息（消息中的关键字）出现时运行脚本。要实现仅在 MQTT 消息具有特定内容或关键字时运行脚本的场景，我们可以利用 **if** [条件语句](../../developer-guides/scripting/index.md#conditional-statement)：

```ros
/iot/mqtt/subscriptions/set 0 on-message={:if ($msgData~"\\{\"test\":\"123\"\\}") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```

或者：

```ros
/iot/mqtt/subscriptions/set 0 on-message={:if ($msgData~"test") do={:log info "Got data {$msgData} from topic {$msgTopic}"}}
```

因此，在每次收到 MQTT 消息时，脚本将检查 if 条件是否为真。如果为真（如果 **$msgData** 包含 JSON 字符串 **\{"test":"123"}** 或如果 **$msgData** 包含字符串“**test**”），将生成日志条目。否则，不会发生任何事情。

也就是说，仅当您发布如下消息时，脚本才会运行：

```ros
/iot/mqtt/publish broker=broker topic="my/test/topic" message="{\"test\":\"123\"}"
```

当您从属于多个具有 `on-message` 配置的订阅的主题收到消息时，只会运行 **x1** 个 `on-message` 脚本。RouterOS 将使用以下逻辑/优先级选择要运行的 `on-message` 脚本：

1. 如果为订阅配置的主题是精确匹配 → 第一优先级。
2. 如果主题名称不是精确匹配（使用通配符）→ 第二优先级是单级通配符主题。
3. 如果主题不属于单级通配符类别 → 第三优先级是基于主题级别的多级通配符主题。

示例：

```ros
/iot/mqtt/subscriptions/print
 0 broker=broker topic="some/sort/of/topic" qos=0 on-message="/system/script/run script1" 

 1 broker=broker topic="some/#" qos=0 on-message="/system/script/run script2" 

 2 broker=broker topic="some/sort/of/+" qos=0 on-message="/system/script/run script3"  

 3 broker=broker topic="some/thing/#" qos=0 on-message="/system/script/run script4"   
```

当您将数据发布到 `some/sort/of/topic` 时，将启动 script1，因为主题是精确匹配。

当您将数据发布到 `some/sort/of/thing` 时，将启动 script3 → 因为它属于单级 1v1 通配符主题名称。

当您将数据发布到 `some/name` 时，将启动 script2 → 因为它属于多级通配符主题名称。

当您将数据发布到 `some/thing/else` 时，将启动 script4 → 因为它属于多级通配符主题名称（即使它也匹配 `some/#` 通配符，但它比 `some/thing/#` 条目更接近一级）。

### 取消订阅

**子菜单：** `/iot/mqtt/unsubscribe`

| 属性 | 描述 |
| :-- | :-- |
| **broker** (*字符串*; 默认：) | 选择要取消订阅的代理。 |
| **topic** (*字符串*; 默认：) | 选择要取消订阅的主题，由代理定义。 |

取消订阅代理和主题的示例如下所示：

```ros
/iot/mqtt/unsubscribe broker="broker" topic="my/test/topic"
```

## 使用脚本发布 RouterOS 统计信息

您还可以使用 [脚本](../../developer-guides/scripting/index.md) 来构建包含 RouterOS 统计信息的 MQTT 消息。然后，您可以应用 [调度器](../../system-information-and-utilities/scheduler.md) 在您希望的任何时间运行脚本。

例如，您可以运行类似 [mqttpublish.rsc](pathname:///assets/200573055_mqttpublish.rsc) 的脚本（将下面显示的 RouterOS 代码内容复制到新终端并按 <kbd>Enter</kbd>）：

```ros
/system/script/add dont-require-permissions=no name=mqttpublish owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#\
    \_Required packages: iot\r\
    \n\r\
    \n################################ Configuration #########################\
    #######\r\
    \n# Name of an existing MQTT broker that should be used for publishing\r\
    \n:local broker \"broker\"\r\
    \n\r\
    \n# MQTT topic where the message should be published\r\
    \n:local topic \"my/test/topic\"\r\
    \n\r\
    \n#################################### System ############################\
    #######\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load]\r\
    \n:local freeMemory [/system/resource/get free-memory]\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory)\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n\A0 \A0 [/system/package/find where name ~ \"^routeros\"]]\r\
    \n:local model [/system/routerboard/get value-name=model]\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number]\r\
    \n:local upTime [/system/resource/get uptime]\r\
    \n\r\
    \n#################################### MQTT ##############################\
    #######\r\
    \n:local message \\\r\
    \n\A0 \A0 \"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"cpu\\\":\$cpuLoad,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"umem\\\":\$usedMemory,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"fmem\\\":\$freeMemory,\\\r\
    \n\A0 \A0 \A0 \A0 \A0 \A0 \A0 \A0 \\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message to MQTT broker...\")\r\
    \n/iot/mqtt/publish broker=\$broker topic=\$topic message=\$message\r\
    \n:put (\"[*] Done\")"
```

该脚本从 RouterOS 收集数据（型号名称、序列号、RouterOS 版本、当前 CPU、已用内存、可用内存和运行时间），并以 JSON 格式将消息（数据）发布到代理：

```ros
/system/script/run mqttpublish
[*] Gathering system info...
[*] Total message size: 125 bytes
[*] Sending message to MQTT broker...

[*] Done
```

您可以订阅该主题以检查结果：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=broker topic="my/test/topic" data="{"model":"RB924i-2nD-BT5&BG77","sn":"E9C80EAEXXXX","ros":"7.9","cpu":13,"umem":47476736,
     "fmem":19632128,"uptime":"02:21:18"}" 
   time=2023-05-22 17:03:52 
```

不要忘记根据您的设置更改脚本的“Configuration”部分（主题和代理）。