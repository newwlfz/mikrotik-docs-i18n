# MikroTik BLE 标签加速度计触发器的电子邮件通知

> 在本指南中，我们将逐步演示如何配置您的 KNOT，使其在检测到 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 或 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 标签报告的“触发”条件时发送电子邮件通知。

### 简介

在本指南中，我们将逐步演示如何配置您的 KNOT，使其在检测到 [TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 或 [TG-BT5-OUT](https://mikrotik.com/product/tg_bt5_out) 标签报告的“触发”条件时发送电子邮件通知。

两款标签均内置加速度计，能够检测自由落体、唤醒/移动以及倾斜状态。当标签设置为广播 [MikroTik 格式](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-tag-advertisement-formats) 的载荷，并且启用了加速度计触发器（使用 MikroTik Beacon Manager 应用程序）时，标签将在检测到触发条件时立即广播广告载荷/报告。

对于 [iOS](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices) 设备，触发器设置界面如下（处于禁用状态/默认设置）：

![](../../img/image2022-8-12_8-26-32.webp)

对于 [Android](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices) 设备，触发器设置界面如下（处于禁用状态/默认设置）：

![](../../img/image2022-8-12_8-29-6.webp)

要激活触发器检测，只需启用相应的“复选框”即可。

当标签广播蓝牙载荷后，载荷的第 21 个八位字节将指示检测到的具体触发类型。您可以在 **IoT>Bluetooth>Advertising reports** 选项卡下查看载荷：

![](../../img/image2022-8-12_9-24-4.webp)

根据上述截图，第 21 个八位字节为“04”，表示该载荷是在标签检测到自由落体状态时发送的（这些载荷是在我们“意外”掉落或抛出标签时广播的）。

一切配置完成后，将发生以下流程：

- KNOT 将按计划运行一个脚本。
- 该脚本将“读取/扫描” **IoT>Bluetooth>Advertising reports** 选项卡中显示的载荷。
- 如果存储/捕获的载荷第 21 个八位字节的值等于任何“触发”值，则将发送电子邮件通知。

换句话说，当 KNOT 扫描载荷并发现第 21 个八位字节指示触发器已被激活时，您将收到一封关于检测到触发器的电子邮件通知。

### TG-BT5 标签配置

在此具体示例中，我们需要将标签配置为以 **MikroTik 格式** 工作。在 MikroTik 格式中，每个载荷的第 21 个八位字节将指示其触发的原因。

您可以参考 [iOS](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-for-ios-devices) 和/或 [Android](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/mikrotik-beacon-manager-android-devices) 指南（**“Advertisement”/Beacon 设置** 部分）来了解如何启用触发器。

为了更容易“激活”触发器，我们还可以根据 iOS 和/或 Android 指南（**Free Fall Threshold 和 Duration** 部分）修改触发器的设置。为了测试目的，并且基本上为了更快地“触发”检测，我们可以将“**Free Fall Duration**”参数更改为“0”秒（这将确保所有轴上处于阈值范围内的任何加速度都会被立即检测为“自由落体”事件）。

### RouterOS 配置

:::info
需要 **iot** 软件包。您可以从我们的下载页面获取 - 位于“Extra packages”下。
:::
配置可以通过 4 个步骤完成：

- 启用扫描器（并且最好确认标签在检测到触发器时正在广播载荷）；
- 设置电子邮件服务器；
- 导入脚本（并根据需求修改几行脚本）；
- 设置调度器。

#### 蓝牙扫描器

转到 [IoT>Bluetooth>Scanners](/docs/internet-of-things/bluetooth/) 选项卡，确保其已启用：

![](../../img/image2022-8-12_9-39-30.webp)

转到 **Advertising reports** 选项卡，并使用 MAC 地址过滤选项过滤列表（您可以在 MikroTik 标签本身的标签上找到其 MAC 地址）。

尝试“触发”已配置的检测，并通过检查第 21 个八位字节的值进行确认。

在我们的示例中，我们为标签配置了“自由落体”检测，然后**将其掉落**。我们收到了标签报告“下落”状态的报告（第 21 个八位字节 = **04**）：

![](../../img/image2022-8-12_9-48-45.webp)

我们已经确认标签能够正确报告触发器。

#### 电子邮件

导航到 [Tools>Email](/docs/system-information-and-utilities/e-mail) 部分，并设置您选择的电子邮件服务器。

在本指南中，我们将使用所示的 **GMAIL** 示例。

![](../../img/image2022-8-12_10-5-40.webp)

尝试发送一封测试电子邮件，以确保配置正确。

#### 脚本

##### 选项 (a)

导航到 [System>Scripts](/docs/developer-guides/scripting/) 菜单，并在其中添加一个新脚本。

您可以复制下面的脚本。将以下脚本复制到“记事本”中，然后再次复制到脚本的“**Source:**”字段中。

```ros
## 在 "" 内输入标签的 MAC 地址
:local addressRegex "2C:C8:1B:E2:15:29"

#在 "" 内输入电子邮件的主题
:local emailsubject "RouterOS report!"

#在 "" 内输入电子邮件地址
:local emailaddress "YOUR_EMAIL@gmail.com"

#脚本：
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## 查找新的蓝牙广告
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # 自启动以来首次运行此脚本，需要初始化
    # 持久变量
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local obj "$[$flagStr $flags]"

    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

#消息结构：
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--标签报告的触发器！"

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"} else={:put "第21个八位字节未检测到触发器！"}
```

需要关注以下 3 行：

```
:local addressRegex "2C:C8:1B:E2:15:29"
```

此行用于输入您希望监控的标签的 MAC 地址；

```
:local emailsubject "RouterOS report!"
```

此行用于修改电子邮件的主题；

```
:local emailaddress "YOUR_EMAIL@gmail.com"
```

此行用于输入电子邮件地址，即您希望将报告发送到的地址。

您还可以使用以下行修改电子邮件的消息结构：

```ros
#消息结构：
:local message "$messageF
$messageT
$messageX
$messageY
$messageZ
$messageS
--标签报告的触发器！"
```

您可以随意命名脚本，例如 **triggernotification**。点击 **Apply** 和 **OK**。

:::info
另外，在本示例中，我们专门演示了电子邮件通知场景。**但是！** 如果您希望使用其他方法发送通知，只需修改下面这一行：

```
:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$message"}
```

您可以将该行中的 `do={/tool e-mail...` 部分修改为，例如 `do={/tool fetch...` 或 `do={/iot mqtt publish...`。这样，您就可以改为发送 HTTP POST 或 MQTT 发布消息。

如果您希望在检测到触发器时收到手机通知，您还可以利用 IFTTT 服务（向 IFTTT webhook 发送 HTTP POST），如我们的另一篇指南 [此处](/docs/internet-of-things/bluetooth/user-guides/ifttt-app-notifications-ble-tag) 所述。
:::
您可以通过命令“**/system script run triggernotification**”手动运行脚本，或者点击 **Script List** 部分下的“**Run Script**”按钮。

您应确保在手动启动脚本后收到电子邮件通知。

当脚本 **(a)** 启动时，RouterOS 将检查每个接收/存储的蓝牙载荷，如果在载荷列表中发现任何触发器，则将构建并发送一封电子邮件消息。该电子邮件消息将仅指示列表中检测到了哪些触发器，不包含其他附加信息。

##### 选项 (b)

```ros
## 在 "" 内输入标签的 MAC 地址
:local addressRegex "2C:C8:1B:E2:15:29"

## 用于根据数据过滤蓝牙广告的 POSIX 正则表达式。用法与 'addressRegex' 相同。
:local advertisingDataRegex ""

## 信号强度过滤器。例如，-40 将仅包含信号强度强于 -40dBm 的蓝牙广告。
## 要禁用此过滤器，请将其设置为 ""
:local rssiThreshold ""

#在 "" 内输入电子邮件的主题
:local emailsubject "RouterOS report!"

#在 "" 内输入电子邮件地址
:local emailaddress "YOUR_GMAIL@gmail.com"

#脚本：
################################## Bluetooth ##################################
:local flagStr do={
    :local str ""

    :if ($1 & 0x01) do={ :set $str " switch" }
    :if ($1 & 0x02) do={ :set $str "$str tilt" }
    :if ($1 & 0x04) do={ :set $str "$str free_fall" }
    :if ($1 & 0x08) do={ :set $str "$str impact_x" }
    :if ($1 & 0x10) do={ :set $str "$str impact_y" }
    :if ($1 & 0x20) do={ :set $str "$str impact_z" }

    :if ([:len $str] = 0) do={ :return "" }

    :return [:pick $str 1 [:len $str]]
}

:local triggernameF "free_fall"
:local triggernameT "tilt"
:local triggernameX "impact_x"
:local triggernameY "impact_y"
:local triggernameZ "impact_z"
:local triggernameS "switch"

## 查找新的蓝牙广告
:global btOldestAdvertisementTimestamp
:if ([:typeof $btOldestAdvertisementTimestamp] = "nothing") do={
    # 自启动以来首次运行此脚本，需要初始化
    # 持久变量
    :set $btOldestAdvertisementTimestamp 0
}
:local advertisements [/iot bluetooth scanners advertisements print detail \
    as-value where \
        epoch > $btOldestAdvertisementTimestamp and \
        address ~ $addressRegex and \
        data ~ $advertisingDataRegex and \
        rssi > $rssiThreshold
]
:local advCount 0
:local lastAdvTimestamp 0
:local triggerlist ""

:local triggerF
:local triggerT
:local triggerX
:local triggerY
:local triggerZ
:local triggerS

:local messageF ""
:local messageT ""
:local messageX ""
:local messageY ""
:local messageZ ""
:local messageS ""

:local 21st ""

:foreach adv in=$advertisements do={
    :local address ($adv->"address")
    :local rssi ($adv->"rssi")
    :local epoch ($adv->"epoch")
    :local rtime ($adv->"time")
    :local ad ($adv->"data")
    :local flags [:tonum "0x$[:pick $ad 40 42]"]
    :local fflags "$[$flagStr $flags]"
    :if ($fflags="") do={:set $fflags "none - periodically broadcasted payload"}

    :local obj "# $advCount:
                             time: $rtime
                             trigger: $fflags

"
    :set $advCount ($advCount + 1)
    :set $lastAdvTimestamp $epoch
    :set $triggerlist "$triggerlist$obj"

:set triggerF [:pick $triggerlist ([find $triggerlist "free_fall"]-0) ([find $triggerlist "free_fall"]+9)]
:if ($triggerF=$triggernameF) do={:set messageF "$triggernameF";:set 21st "not00";}
:set triggerT [:pick $triggerlist ([find $triggerlist "tilt"]-0) ([find $triggerlist "tilt"]+4)]
:if ($triggerT=$triggernameT) do={:set messageT "$triggernameT";:set 21st "not00";}
:set triggerX [:pick $triggerlist ([find $triggerlist "impact_x"]-0) ([find $triggerlist "impact_x"]+8)]
:if ($triggerX=$triggernameX) do={:set messageX "$triggernameX";:set 21st "not00";}
:set triggerY [:pick $triggerlist ([find $triggerlist "impact_y"]-0) ([find $triggerlist "impact_y"]+8)]
:if ($triggerY=$triggernameY) do={:set messageY "$triggernameY";:set 21st "not00";}
:set triggerZ [:pick $triggerlist ([find $triggerlist "impact_z"]-0) ([find $triggerlist "impact_z"]+8)]
:if ($triggerZ=$triggernameZ) do={:set messageZ "$triggernameZ";:set 21st "not00";}
:set triggerS [:pick $triggerlist ([find $triggerlist "switch"]-0) ([find $triggerlist "switch"]+6)]
:if ($triggerS=$triggernameS) do={:set messageS "$triggernameS";:set 21st "not00";}

}
:if ($advCount > 0) do={
    :set $btOldestAdvertisementTimestamp $lastAdvTimestamp
}

:if ($21st="not00") do={/tool e-mail send to=$emailaddress subject="$emailsubject" body="$triggerlist"} else={:put "第21个八位字节未检测到触发器！"}
```

当脚本 **(b)** 启动时，RouterOS 将检查每个接收/存储的蓝牙载荷，如果在载荷列表中发现任何触发器，则将构建并发送一封电子邮件消息。与脚本 **(a)** 相比，该电子邮件消息将包含更详细的信息。在这种情况下，消息将指示每个载荷的接收时间。

#### 调度器

要自动化该过程，请在 **System>Scheduler** 选项卡下添加一个新的调度器：

![](../../img/image2022-8-12_13-8-32.webp)

在“**On Event:**”字段中输入“**/system script run triggernotification**”，并设置您希望运行脚本以检查/扫描广告报告的**间隔**（例如，设置为 10 秒）。

点击 **Apply** 和 **OK**。

#### 结果验证

1) 确认标签正在广播广告报告，并且标签的触发器能够被检测到：

![](../../img/image2022-8-12_9-48-45.webp)

1) 确认您的电子邮件服务器配置正确，并且您能够从 KNOT (RouterOS) 发送电子邮件。

2) 在您手动运行脚本或将调度器应用于脚本后，应会发送一封电子邮件通知，如下所示：

     脚本 **(a)**：

![](../../img/image2022-8-29_15-15-9.webp)

     脚本 **(b)**：

![](../../img/image2022-8-29_15-18-39.webp)