# HTTPS 发布与 Azure 配置

> 本文将演示如何配置 [Azure](https://azure.microsoft.com/en-us) 和 RouterOS，以通过 HTTPS 协议发布数据。在此场景中，RouterOS 将充当网关，将 BLEtag 广播的数据发布到云端（Azure）。

### 简介

本文将演示如何配置 [Azure](https://azure.microsoft.com/en-us) 和 RouterOS，以通过 HTTPS 协议发布数据。在此场景中，RouterOS 将充当网关，将 BLEtag 广播的数据发布到云端（Azure）。

在继续设置之前，您需要在 Azure 系统中创建一个账户。您可以点击此 [链接](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account?icid=azurefreeaccount) 了解更多相关信息。

Azure 提供了许多不同的选项和服务，其中许多选项/服务都有价格表。您可以点击 [链接](https://www.azure.cn/en-us/pricing/) 了解更多定价信息。

### Azure 配置

一旦您完成了订阅设置（Azure 门户 > 所有服务 > 订阅），您将需要配置一个资源组、一个 IoT 中心、一个设备，并生成一个 SAS 令牌。

#### 资源组

前往“所有服务”>“资源组”并创建一个。

![](../../img/azure_resources.png)

您可以点击 [链接](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal) 查看更详细的指南。

成功配置资源组后，您需要创建一个 IoT 中心。

#### IoT 中心

导航至“所有服务”>“IoT 中心”并创建一个。

![](../../img/azure_iothub.png)

将您的 IoT 中心链接到之前创建的资源组。不要忘记检查/设置“网络”（网络连接）和“管理”（[订阅层级](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-scaling)）选项卡。

您可以点击 [此处](https://learn.microsoft.com/en-us/azure/iot-hub/iot-concepts-and-iot-hub) 了解更多信息。

#### 设备

导航至您的 IoT 中心 >“IoT 设备”并添加一个新设备：

![](../../img/image2021-6-17_14-36-45.webp)

选择 `身份验证类型=对称密钥` 并保存设置。

#### SAS 令牌

在我们的示例中，我们将使用 [Visual Studio Code](https://code.visualstudio.com/) 程序来生成 [SAS 令牌](https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview)。

简单来说，下载该程序并将其连接到您的 [IoT 中心](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-toolkit)。

完成后，当之前配置的设备名称出现在您的 IoT 中心中时 - 右键单击设备名称并生成令牌，如下方截图所示：

![](../../img/image2021-6-17_15-4-15.webp)

系统将要求您输入令牌的过期时间（以小时为单位），然后按“回车”确认设置。

此步骤之后，令牌应生成在“输出”字段中：

![](../../img/image2021-6-17_15-7-52.webp)

复制该令牌，因为它将在后续的 HTTPS 发布脚本中使用。

至此，Azure 部分的配置已完成。

### RouterOS 配置

在本指南中，我们使用 [KNOT](https://mikrotik.com/product/knot) 作为网关，并使用一个（专门为 KNOT 创建的）脚本来发布数据。在您的特定应用场景中，您可以使用任何 RouterOS 设备来发布您需要的任何数据。

#### 使用脚本进行 HTTPS 发布

HTTPS 发布可以使用 [fetch 工具](/docs/system-information-and-utilities/fetch) 实现。为了将蓝牙标签（在我们的示例中为 TG-BT5-XX）的数据发布到 Azure，我们将使用脚本。脚本示例如下所示。

每个以符号 `#` 开头的行都是说明性的，它描述了将在该行下方配置的参数。请更改引号 `""` 内的参数以适用于您的特定情况。

```ros
################################ 配置 ################################
## 其 MAC 地址应作为“定位器 ID”使用的接口
:local locatorIface "ether1"

## 用于过滤广播蓝牙地址的 POSIX 正则表达式。例如 "^BC:33:AC"
## 将仅包含以这三个八位字节开头的地址。
## 要禁用此过滤器，请将其设置为 ""
:local addressRegex ""

## 用于根据数据过滤蓝牙广播的 POSIX 正则表达式。用法与
## 'addressRegex' 相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将仅包含信号强度强于 -40dBm 的蓝牙广播。
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

:if ($advCount > 0) do={

    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp

}

:put ("[*] 找到 $advCount 个新广播 \
    (处理时间: $[([/system clock get time] - $btProcessingStart)])")

#################################### 消息 #####################################
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
:put ("[*] 总消息大小: $[:len $message] 字节")
/tool fetch http-method=post output=user http-header-field="authorization:{sas_token}" http-data=$message url="https://{iot_hub_name}.azure-devices.net/devices/{device_id}/messages/events\?api-version=2020-03-13"

:put ("[*] 完成")
```

需要注意 1 行脚本：

```ros
/tool fetch http-method=post output=user http-header-field="authorization:{sas_token}" http-data=$message url="https://{iot_hub_name}.azure-devices.net/devices/{device_id}/messages/events\?api-version=2020-03-13"
```

将 HTTP 头中的 `{sas_token}` 更改为在 SAS 令牌部分生成的令牌。

将 URL 中的 `{iot_hub_name}` 和 `{device_id}` 更改为在 Azure 门户上配置的实际 IoT 中心名称和设备 ID。

脚本的其余配置取决于整体需求。脚本解释了具体配置了哪些参数用于发布。

导航至“系统”>“脚本”，在那里添加一个新脚本，并粘贴上面显示的脚本（例如，将其命名为 script1）。

要运行该脚本，您可以使用命令行：

```ros
/system script run script1
```

### 验证

在 Azure 门户上查看接收/发布的消息有很多不同的方法。请查看 Azure 教程以了解您可用的选项。

我们将使用 [Visual Studio Code](https://code.visualstudio.com/) 程序来验证结果。

打开您的 IoT 中心并开始监控端点（设备）：

![](../../img/image2021-6-17_15-25-28.webp)

您可以在“输出”部分查看发布的消息，如下方截图所示。只需运行脚本并检查收到的消息：

![](../../img/image2021-6-17_15-31-11.webp)