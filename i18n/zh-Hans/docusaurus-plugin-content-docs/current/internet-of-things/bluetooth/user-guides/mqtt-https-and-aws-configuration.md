# MQTT/HTTPS 与 AWS 配置

> 使用 MQTT over HTTPS 将 MikroTik 蓝牙标签数据转发至 Amazon AWS，涵盖 AWS 账户设置、证书及 Broker 配置。

### 引言

监控蓝牙标签广播信息的可选方案之一是使用云系统，例如 AWS（Amazon Web Services）。本文将演示如何配置 AWS 与 RouterOS，以通过 MQTT 和 HTTPS 协议发布数据。在此场景中，RouterOS 将作为网关，将 BLEtag 广播的数据发布至云端（AWS）；而 AWS 则充当 MQTT Broker 和 MQTT 订阅者（即数据展示/接收的服务器）。

在开始配置之前，您需要在 AWS 系统中创建账户。有关如何创建账户的更多信息，请参阅此[链接](https://repost.aws/knowledge-center/create-and-activate-aws-account)。

创建账户后，请确保在 **您的用户名>My account** 下完成支付卡验证，否则账户将无法激活。

进入 **Services>Internet of Things>IoT Core**。

在 **Test** 部分，您可以使用内置的 MQTT 测试客户端来测试主题的发布与订阅。您可以通过 **Subscribe to a topic** 和 **Publish to a topic** 选项卡来检查这两个过程。MQTT 测试客户端部分也可以显示 HTTPS 发布的内容。

### AWS IoT 配置

:::info
本节展示的配置适用于 MQTT 发布/订阅场景，但您也可以使用相同的 AWS 设置来测试 HTTPS 发布。
:::

#### Things（设备）

步骤 1：导航至 **Manage>Things**。这是配置开始的菜单（Things 菜单代表设备或逻辑实体）。

**

![](../../img/image2021-3-31_11-20-55.webp)

**

点击 **Create>Create a single thing>** 选择名称 **>Next>Create certificate。**

步骤 2：下载 "AmazonRootCA1.pem" 证书（AWS 的 Root CA）、"xxxx.cert.pem" 证书（"thing" 的证书）和 "xxxx.private.key" 密钥（私钥）——其中 "xxxx" 部分对于每个新创建的证书都是唯一的。

![](../../img/image2021-3-31_11-40-45.webp)

步骤 3：您可以选择完成设置（选择 **Done**）或设置策略（选择 **Attach a policy**）。您需要为创建的 "thing" 添加策略，但如果您使用的是新账户，可能没有可选的策略。不必担心，您可以稍后手动创建。

还有两个重要的菜单——**Secure>Certificates** 和 **Secure>Policies**。

#### Certificates（证书）

在 **Certificates** 菜单中，您可以创建证书、激活证书并将其附加到策略。"Things" 配置应该已经创建了证书。只需确保证书处于"已激活"状态。为此，请选择证书，点击 "**Actions**"，然后点击 "**Activate**"。

![](../../img/image2021-3-31_11-41-18.webp)

#### Policies（策略）

![](../../img/image2021-3-31_11-45-14.webp)

步骤 1：创建新策略。点击 "**Create**" 并输入策略名称。在 "**Create a policy**" 选项卡中，您可以设置 "actions"。本示例将使用 4 个操作（`iot:Publish`、`iot:Receive`、`iot:Subscribe` 和 `iot:Connect`）。有关策略及示例的更多信息，请参阅此[链接](https://docs.aws.amazon.com/iot/latest/developerguide/example-iot-policies.html)。

步骤 2：导航至 "**Add statements**" 部分。在 "**Action**" 字段中，选择 **iot:Publish** 和 **iot:Receive** 操作，并用逗号 "," 分隔。在 "**Resource ARN**" 字段中，将文本 "`replaceWithATopic`" 替换为实际相关的主题（例如 "`my/test/topic`"）。在 "**Effect**" 复选框中勾选 "**Allow**"。

![](../../img/image2021-3-31_11-48-20.webp)

步骤 3：点击 "**Add statement**" 添加新语句。选择 **iot:Subscribe** 为语句添加操作，并将 "**Resource ARN**" 字段中的文本 "`replaceWithATopicFilter`" 替换为实际相关的主题（例如 "`my/test/topic`"）。在 "**Effect**" 复选框中勾选 "**Allow**"。

![](../../img/image2021-3-31_11-51-18.webp)

步骤 4：添加最后一条语句并设置 **iot:Connect** 操作。仅将 "`replaceWithAClientId`" 部分替换为适当的客户端 ID（例如 "`test-client`"），并勾选 "**Allow**" 复选框。要完成设置，请点击 "**Create**"。

步骤 5：您需要将证书附加到新创建的策略。为此，请前往 **Secure>Certificates**，选择证书，点击 "**Actions**" 和 "**Attach policy**"。

![](../../img/image2021-3-31_11-56-52.webp)

选择策略并点击 "**Attach**"。

![](../../img/image2021-3-31_11-57-29.webp)

至此，AWS 设置完成。

#### Endpoint 地址（Broker 地址）

您可以在 "**Settings**" 部分（Settings>Device data endpoint）找到 **Endpoint** 地址。该地址应配置为 RouterOS 设置中的 Broker IP/FQDN 地址。

![](../../img/image2021-3-31_12-0-54.webp)

### RouterOS 配置

:::info
要配置 MQTT，请确保事先安装 **iot** 软件包。
:::
在我们的示例中，我们使用 [KNOT](https://mikrotik.com/product/knot) 作为网关，并使用一个（专为 KNOT 创建的）脚本发布数据。在您的具体应用场景中，您可以使用任何 RouterOS 设备（已安装 iot 软件包）来发布您需要的任何数据。

#### Certificates（证书）

由于 AWS 使用 SSL 连接，我们需要之前下载的证书和密钥。

进入 "Files" 菜单，将 *AmazonRootCA1.pem*、*xxxx.cert.pem.crt* 和 *xxxx.private.pem.crt* 添加到 "File list"。

![](../../img/image2021-3-24_16-11-43.webp)

进入 System>Certificates 并导入所有 3 个文件（通过 "Import" 按钮——逐个导入）：

![](../../img/image2021-3-24_16-4-55.webp)

确保两个证书均受信任（T），且 "xxxx.certificate.pem.crt" 带有私钥（K）。

#### MQTT Broker

导航至 IoT>MQTT 并添加新的 broker（"+" 按钮）。

![](../../img/image2021-4-27_9-9-32.webp)

在 "Name" 字段中为 broker 命名（例如，**AWS**）。

在 "Address" 字段中输入/粘贴 AWS 地址（您可以在 AWS 设置的 "**Settings>Device data endpoint**" - **Endpoint address** 中找到）。

在 "Port" 字段中配置 broker 使用的端口，并通过 SSL 复选框启用 SSL（在此情况下，AWS 使用 **8883**，并且由于我们使用证书，需要**启用 SSL**）。

在此场景中，"Username" 和 "Password" 字段不是必需的（取决于 broker 的配置——跳过这两个字段）。

在 "Client Id" 字段中设置客户端 ID（这是在 AWS 策略中配置的 ID——在本示例中为 **`test-client`**）。

由于使用了 SSL，必须在 "Certificate" 字段中选择证书（选择 ***xxxx.certificate.pem.crt***）。

点击 "Apply" 和 "OK" 完成 broker 设置。

#### 使用脚本进行 MQTT 发布

为了将蓝牙标签（在我们的示例中为 TG-BT5-IN）的数据发布到 AWS，我们将使用脚本。脚本示例如下所示。

每个以符号 `#` 开头的行都是说明性的，描述该行下方将要配置的参数。请更改引号 `""` 内的参数以适用于您的具体情况。

```ros
## Required packages: iot

################################ Configuration ################################
## Name of an existing MQTT broker that should be used for publishing
:local broker "AWS"

## MQTT topic where the message should be published
:local topic "my/test/topic"

## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
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
## Remove semicolons from MAC/Bluetooth addresses
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
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"clientId\":\"$[/iot mqtt brokers get value-name=client-id \
            [/iot mqtt brokers find name=$broker]]\",\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
:put ("[*] Sending message to MQTT broker...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] Done")
```

需要关注 2 行脚本。

```
:local broker "AWS"
```

此行中，您应在引号 `""` 内指定 broker 的名称（在我们的示例中为 **AWS**）。

```
:local topic "my/test/topic"
```

此行中，您应在引号 `""` 内指定正确的主题。该主题在 AWS 策略中配置（在我们的示例中为 **my/test/topic**）。

脚本的其余配置取决于整体需求。脚本说明了具体配置了哪些参数用于发布。

导航至 System>Scripts，在那里添加一个新脚本，并粘贴上面显示的脚本（例如，将其命名为 script1）。

要运行脚本，您可以使用命令行：

```
/system script run script1
```

#### 使用脚本进行 HTTPS 发布

另一种可用于将数据从网关发布到云端的协议是 HTTPS。这可以通过 [fetch 工具](/docs/system-information-and-utilities/fetch) 实现。在 RouterOS 7.1beta6 版本之前，fetch 没有选择客户端证书进行身份验证的选项（意味着不支持使用客户端证书进行 HTTPS 发布），而在 7.1beta6 中新增了一项功能，启用了此设置/支持。使用 CURL 和 Python 的 HTTPS 发布示例（以及其他有用信息）请参阅 [AWS HTTPS 手册](https://docs.aws.amazon.com/iot/latest/developerguide/http.html)。

为了将蓝牙标签（在我们的示例中为 TG-BT5-IN）的数据发布到 AWS，我们将使用脚本。脚本示例如下所示。

每个以符号 `#` 开头的行都是说明性的，描述该行下方将要配置的参数。请更改引号 `""` 内的参数以适用于您的具体情况。

```ros
################################ Configuration ################################
## Interface whose MAC should be used as 'Locator ID'
:local locatorIface "ether1"

## POSIX regex for filtering advertisement Bluetooth addresses. E.g. "^BC:33:AC"
## would only include addresses which start with those 3 octets.
## To disable this filter, set it to ""
:local addressRegex ""

## POSIX regex for filtering Bluetooth advertisements based on their data. Same
## usage as with 'addressRegex'.
:local advertisingDataRegex ""

## Signal strength filter. E.g. -40 would only include Bluetooth advertisements
## whose signal strength is stronger than -40dBm.
## To disable this filter, set it to ""
:local rssiThreshold "-40"

#################################### System ###################################
:put ("[*] Gathering system info...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## Health is a bit iffy since '/system health' does not have 'find' in ROS6
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## Bluetooth ##################################
:put ("[*] Gathering Bluetooth info...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # First time this script has been run since booting, need to initialize
    # persistent variables
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
## Remove semicolons from MAC/Bluetooth addresses
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
    :local obj "\
        {\
            \"id\":\"$[$minimizeMac address=$address]\",\
            \"ts\":$ts,\
            \"rssi\":$rssi,\
            \"ed\":{\
                \"ad\":\"$ad\"\
            }\
        }"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $ts
    # Ensure that the last object is not terminated by a comma
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] Found $advCount new advertisements \
    (processing time: $[([/system clock get time] - $btProcessingStart)])")

#################################### MQTT #####################################
:local message \
    "{\
        \"t\":0,\
        \"v\":1,\
        \"OldestAdvertisementTimestamp\":$btOldestAdvertisementTimestamp,\
        \"locs\":[{\
            \"id\":\"$[$minimizeMac address=$ifaceMac]\",\
            \"tags\":[$advJson],\
            \"ed\":{\
                \"model\":\"$model\",\
                \"sn\":\"$serialNumber\",\
                \"ros\":\"$rosVersion\",\
                \"cpu\":$cpuLoad,\
                \"umem\":$usedMemory,\
                \"fmem\":$freeMemory,\
                \"psu\":$supplyVoltage,\
                \"temp\":$boardTemp\
            }\
        }]\
    }"
:log info "$message";
:put ("[*] Total message size: $[:len $message] bytes")
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"

:put ("[*] Done")
```

需要关注 1 行脚本：

```
/tool fetch certificate=f79dda4ec5-certificate.pem.crt.txt_0 http-method=post output=user http-header-field="Content-Type:application/json" http-data=$message url="https://xxxxxx.iot.us-east-2.amazonaws.com:8443/topics/my/test/topic"
```

请根据您的具体情况更改证书名称和 URL：

`url="https://xxxx:8443/topics/yyyy"`，其中 "xxxx" 是 AWS endpoint 地址，"yyyy" 是在 AWS 策略中配置的主题——步骤 2 和 3（在我们的示例中为 my/test/topic）。

脚本的其余配置取决于整体需求。脚本说明了具体配置了哪些参数用于发布。

导航至 System>Scripts，在那里添加一个新脚本，并粘贴上面显示的脚本（例如，将其命名为 script2）。

要运行脚本，您可以使用命令行：

`/system script run script2`

### 验证

要验证 AWS 是否收到数据，请返回 AWS 门户。导航至 **Test** 页面。使用 **Subscribe to a topic** 选项。在 **Topic filter** 字段中输入在 AWS 策略中配置的主题（在我们的示例中为 **my/test/topic**），然后点击 **Subscribe**。在下方，您应该会看到 **Subscriptions** 部分，数据将显示在那里。运行脚本（在 RouterOS 中），您应该会在 "**Subscriptions**" 选项卡中看到收集到的数据。

![](../../img/image2021-3-31_12-47-14.webp)

同一页面/选项卡也应显示 HTTPS 发布的数据包。