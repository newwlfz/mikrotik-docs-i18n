# MQTT 与 Azure 配置

> 将 MikroTik MQTT 数据发布到 Microsoft Azure IoT，涵盖 Azure 账户设置、设备凭据及 MQTT 代理配置。

### 简介

您可以使用多种云服务来监控 MQTT 发布者发送的信息，Microsoft [Azure](https://azure.microsoft.com/en-us) 便是其中之一。本文将演示如何配置 Azure 和 RouterOS，以使用 MQTT 协议发布数据。在此场景中，RouterOS 将充当网关，把 BLEtag 广播的数据发布到云端（Azure）。而 Azure 则充当 MQTT 代理和 MQTT 订阅者（服务器，数据将在此处发布/显示）。

在继续设置之前，您需要在 Azure 系统中创建一个账户。您可以点击此 [链接](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=azurefreeaccount) 了解更多相关信息。

Azure 提供了许多不同的选项和服务，其中许多选项/服务都有价格表。您可以点击 [链接](https://www.azure.cn/en-us/pricing/) 了解更多定价信息。

### Azure 配置

一旦您完成了订阅设置（Azure 门户 > 所有服务 > 订阅），您将需要配置一个资源组、一个 IoT 中心、一个证书和一个设备。

#### 资源组

转到“所有服务”>“资源组”并创建一个。

![](../../img/azure_resources.png)

将您的 IoT 中心链接到之前创建的资源组。不要忘记检查/设置“网络”（网络连接）和“管理”（[订阅层级](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-scaling)）选项卡。

您可以点击 [此处](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub) 了解更多信息。

#### IoT 中心

导航到“所有服务”>“IoT 中心”并创建一个。

![](../../img/azure_iothub.png)

将您的 IoT 中心链接到之前创建的资源组。不要忘记检查/设置“网络”（网络连接）和“管理”（订阅层级）选项卡。

您可以点击此处了解更多信息。

#### 证书

在本示例中，我们将重点介绍 [X.509 CA 签名](https://learn.microsoft.com/en-us/azure/iot-edge/how-to-authenticate-downstream-device?view=iotedge-2020-11#x509-ca-signed-authentication) 身份验证。

您可以使用 [Microsoft 提供的脚本](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows) 或 [open SSL](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows) 来生成测试证书。

生成 RootCA 后，转到 IoT 中心 > 证书，并在那里添加证书：

![](../../img/image2021-6-1_9-46-36.webp)

成功添加 RootCA 后，您需要 [证明所有权](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows)（验证它）。

如果您使用脚本，[教程（步骤 3）](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-3---prove-possession) 中对此有详细描述和演示；如果您使用 open ssl，请参阅 [教程（步骤 7）](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-7---demonstrate-proof-of-possession)。

证书成功验证后，您需要创建设备证书（如果您使用 open ssl，请点击此 [链接](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub)）。

#### 设备

导航到您的 IoT 中心 > IoT 设备，并添加一个新设备：

![](../../img/image2021-6-1_10-1-41.webp)

请注意“设备 ID”字段。设备 ID 应与设备证书的“公用名”匹配。

选择 `身份验证类型=X.509 CA 签名` 并保存设置。

您现在可以生成最后一个必需的证书 - [设备证书](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-4---create-a-new-device)（如果您使用 open ssl，请点击此 [链接](https://learn.microsoft.com/en-us/azure/iot-hub/tutorial-x509-test-certs?tabs=windows#step-8---create-a-device-in-your-iot-hub)）。

至此，Azure 部分的配置已完成。

### RouterOS 配置

:::info
为了配置 MQTT，请确保事先安装了 **iot** 软件包。
:::
在我们的示例中，我们使用 [KNOT](https://mikrotik.com/product/knot) 作为网关，并使用一个（专门为 KNOT 创建的）脚本来发布数据。在您的特定应用场景中，您可以使用任何 RouterOS 设备（安装了 iot 软件包）来发布您需要的任何数据。

#### 证书

由于我们使用 SSL 连接，因此需要之前生成的设备证书及其私钥。我们还将使用 [Baltimore CyberTrust 根证书](https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-certificate-authority-details?tabs=root-and-subordinate-cas-list)。

转到“文件”菜单，并在其中添加以下证书 - *Baltimore CyberTrust 根证书、之前生成的设备证书及其私钥*。

![](../../img/image2021-6-1_10-34-22.webp)

转到 系统 > 证书，并导入所有 3 个文件（通过“导入”按钮 - 逐个导入）：

![](../../img/image2021-6-1_10-36-54.webp)

:::info
*请仔细检查“公用名”是否与在 Azure 门户上为设备配置的设备 ID 匹配。在我们的示例中，设备 ID 是“testor”，它与“公用名”字段匹配。*
:::
确保两个证书都受信任（T），并且私钥（K）已添加到设备证书中。

#### MQTT 代理

导航到 IoT > MQTT，并添加一个新代理（“+”按钮）：

![](../../img/image2021-6-1_10-44-13.webp)

- 在“名称”字段中为代理命名（例如，**Azure**）。
- 在“地址”字段中输入/粘贴 Azure 主机名地址（您可以在 IoT 中心 > 概述 菜单中找到主机名）：

![](../../img/image2021-6-1_10-24-10.webp)

- 在“端口”字段中配置代理使用的端口，并通过 SSL 复选框启用 SSL（在这种情况下，Azure 使用 **8883** 端口，并且由于我们使用证书，因此需要 **启用 SSL**）。
- “用户名”字段应按以下方式配置 - `{iothubhostname}/{device_id}/?api-version=2018-06-30`，其中 `{iothubhostname}` 是您的 IoT 中心的主机名，`{device_id}` 是在 Azure 门户上设置的设备 ID（与证书的“公用名”相同，在我们的示例中为“testor”）。
- 在此场景中，“密码”字段不是必需的（此配置取决于代理的设置 - 请跳过此字段）。
- “客户端 ID”应与设备的 ID 相同（在我们的示例中为 **testor**）。
- 由于使用了 SSL，必须在“证书”字段中选择证书（选择设备证书）。

您可以点击 [此处](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#using-the-mqtt-protocol-directly-as-a-device) 了解更多关于所需设置的信息。

点击“应用”和“确定”以完成代理的设置。

#### 使用脚本发布 MQTT

为了将数据从蓝牙标签（在我们的示例中为 TG-BT5-IN）发布到 Azure，我们将使用脚本。脚本示例如下所示。

每个以符号 `#` 开头的行都是说明性的，它描述了该行下方将要配置的参数。请更改引号 `""` 内的参数以适用于您的特定情况。

```ros
## 所需软件包：iot

################################ 配置 ################################
## 用于发布的现有 MQTT 代理名称
:local broker "Azure"

## 消息应发布到的 MQTT 主题
:local topic "devices/testor/messages/events/"

## 其 MAC 地址应用作“定位器 ID”的接口
:local locatorIface "ether1"

## 用于过滤广播蓝牙地址的 POSIX 正则表达式。例如 "^BC:33:AC"
## 将只包含以这三个八位字节开头的地址。
## 要禁用此过滤器，请将其设置为 ""
:local addressRegex ""

## 用于根据数据过滤蓝牙广播的 POSIX 正则表达式。用法与 'addressRegex' 相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将只包含信号强度强于 -40dBm 的蓝牙广播。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold "-40"

#################################### 系统 ###################################
:put ("[*] 正在收集系统信息...")
:local ifaceMac [/interface get [/interface find name=$locatorIface] mac-address]
:local cpuLoad [/system resource get cpu-load]
:local freeMemory [/system resource get free-memory]
:local usedMemory ([/system resource get total-memory] - $freeMemory)
:local rosVersion [/system package get value-name=version \
    [/system package find where name ~ "^routeros"]]
:local model [/system routerboard get value-name=model]
:local serialNumber [/system routerboard get value-name=serial-number]
## 健康状态有点不确定，因为 '/system health' 在 ROS6 中没有 'find'
:local health [/system health print as-value]
:local supplyVoltage 0
:local boardTemp 0
:foreach entry in=$health do={
    :if ($entry->"name" = "voltage") do={:set $supplyVoltage ($entry->"value")}
    :if ($entry->"name" = "board-temperature1") do={:set $boardTemp ($entry->"value")}
}

################################## 蓝牙 ##################################
:put ("[*] 正在收集蓝牙信息...")
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # 自启动以来首次运行此脚本，需要初始化持久变量
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
## 从 MAC/蓝牙地址中移除分号
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
    # 确保最后一个对象不以逗号结尾
    :set $advJson "$advJson$advSeparator$obj"
    :if ($advSeparator = "") do={
        :set $advSeparator ","
    }
}

:set $btOldestAdvertisementTimestamp $lastAdvTimestamp
:put ("[*] 找到 $advCount 个新广播 \
    (处理时间: $[([/system clock get time] - $btProcessingStart)])")

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
:put ("[*] 总消息大小: $[:len $message] 字节")
:put ("[*] 正在发送消息到 MQTT 代理...")
/iot mqtt publish broker=$broker topic=$topic message=$message
:put ("[*] 完成")
```

需要注意 2 行脚本：

```
:local broker "Azure"
```

此行中，您应在引号 `""` 内指定代理的名称（在我们的示例中为 **Azure**）。

```
:local topic "devices/testor/messages/events/"
```

此行中，您应在引号 `""` 内指定正确的主题。Azure 默认使用 `devices/{device_id}/messages/events/` 主题进行发布（如 [此处](https://learn.microsoft.com/en-us/azure/iot-hub/iot-mqtt-connect-to-iot-hub#for-azure-iot-tools) 手册所述）。不要忘记将 `{device_id}` 部分更改为您在 Azure 门户上配置的“设备 ID”。

脚本的其余配置取决于整体需求。脚本解释了具体配置了哪些参数用于发布。

导航到 系统 > 脚本，在那里添加一个新脚本，并粘贴上面显示的脚本（例如，将其命名为 script1）。

要运行脚本，您可以使用命令行：

```
/system script run script1
```

### 验证

在 Azure 门户上查看接收/发布的消息有多种不同的方式。请查阅 Azure 教程以了解您可用的选项。

在我们的示例中，我们将使用 [Visual Studio Code 程序](https://code.visualstudio.com/) 来验证结果。

下载该程序并将其连接到您的 [IoT 中心](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)。

添加 IoT 中心后，您可以开始监控端点：

![](../../img/image2021-6-14_10-47-6.webp)

您可以在“输出”部分查看发布的消息，如下面的截图所示：

![](../../img/image2021-6-1_11-39-43.webp)