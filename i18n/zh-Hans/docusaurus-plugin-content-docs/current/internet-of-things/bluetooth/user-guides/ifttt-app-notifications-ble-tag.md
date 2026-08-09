# BLE 标签出现在 KNOT 范围内时的 IFTTT 应用通知

> 我们的蓝牙标签和 KNOT 可用于物联网资产追踪的各种场景。

### 引言

我们的蓝牙标签和 KNOT 可用于物联网资产追踪的各种场景。

本指南将展示的场景是：当标签进入 KNOT 的蓝牙范围以及标签超出蓝牙工作范围时，在您的手机上接收通知。

该场景可借助 [IFTTT](https://ifttt.com/explore) 服务实现。IFTTT 会为您生成一个 URL。然后，您可以使用 RouterOS 中的 [/tool fetch](/docs/system-information-and-utilities/fetch) 向 IFTTT 生成的 URL 发送 HTTP/Web 请求，从而触发手机上的应用通知。

一旦 IFTTT 服务设置完成且 KNOT 已相应配置，您便可将蓝牙标签（[TG-BT5-IN](https://mikrotik.com/product/tg_bt5_in) 或 [OUT](https://mikrotik.com/product/tg_bt5_out) 型号）附着到任何您希望追踪的设备上。

假设您将标签附着到一台昂贵的机器上，或者仅仅是……您的钥匙上。然后，您安装并放置 KNOT，使标签处于 KNOT 的蓝牙范围内。接下来会发生什么，它是如何工作的？

KNOT 将按计划（以您选择的间隔）运行一个脚本。根据脚本中配置的标签 MAC 地址 → 脚本将检查最新收到的蓝牙数据包的时间（即最新数据包的接收时间）。具体情形如下：

- 数据包的接收时间在 **/system clock** 时间的 1 分钟以内（例如，**/system clock** 时间为 **16:02:00**，而标签的数据包在 **16:01:50** 被接收）→ 将触发“标签在范围内”通知，并发送到您的手机。
- 数据包的接收时间早于 **/system clock** 时间 1 分钟以上（例如，**/system clock** 时间为 **16:02:00**，而标签的数据包在 **16:00:50** 被接收）→ 将触发“标签不在范围内”通知，并发送到您的手机。

由于没有其他方法可以判断标签是否实际处于工作范围内，脚本使用“时间”参数来确认。因此，当数据包的接收时间不断刷新时 → 表示标签存在且 KNOT 成功接收数据包。当 KNOT 收到最后一个数据包后已过 1 分钟 → 表示 KNOT 在一整分钟内未收到标签的任何更新，从而确认标签不在范围内。

### IFTTT 设置

第一步是注册 IFTTT 账户或通过此[链接](https://ifttt.com/join)登录现有账户。

为您的手机下载 IFTTT 应用，您可以通过应用或浏览器配置后续步骤。

登录后，点击右上角的“Create”按钮：

![](../../img/image2022-8-8_11-52-18.webp)

这将带您进入小程序创建界面：

![](../../img/image2022-8-8_11-53-31.webp)

在“**If This**”字段中选择“**Add**”按钮。选择名为“**Webhooks**”的服务。然后，选择名为“**Receive a web request**”的选项。

输入一个“**Event Name**”，例如，`**{The_tag_IS_within_range}**`，然后选择“**Create trigger**”。这将带您返回：

![](../../img/image2022-8-8_11-59-39.webp)

在“**Then That**”字段中选择“**Add**”按钮，找到名为“**Notifications**”的操作。选择名为“**Send a notification from the IFTTT app**”的选项，并通过点击“**Create Action**”确认决定。

点击“**Continue**”并查看小程序。点击“**Finish**”。

现在，重复相同步骤创建第二个小程序，但对于第二个小程序，请输入另一个“**Event Name**”，例如，`**{The_tag_is_NOT_in_range}**`。

创建两个小程序后 → 检查为您生成的 Web 请求 URL。前往此[链接](https://ifttt.com/maker_webhooks)并点击“**Documentation**”按钮：

![](../../img/image2022-8-8_12-12-55.webp)

页面将显示您需要使用的 URL：

![](../../img/image2022-8-8_12-15-29.webp)

复制此 URL - 稍后您需要在脚本中使用它。

### 蓝牙标签配置

通过此[链接](/docs/internet-of-things/bluetooth/mikrotik-beacon-manager/)查看我们的标签配置指南（iOS 和 Android）。

在此特定用例中，KNOT 将检查收到的蓝牙数据包的时间，因此标签配置哪种数据包类型并不重要。

唯一重要的设置是“Advertisement interval”（广播间隔）。请确保此参数已配置。

或者，您可以**保持标签的默认设置不变**，无需更改任何内容。

### RouterOS 配置

:::info
请注意，需要 **iot** 软件包。您可以从我们的[下载页面](https://mikrotik.com/download)获取。
:::
确保您已配置互联网访问，以便 KNOT 能够访问 IFTTT Webhooks。

#### 蓝牙扫描器

导航至 **IoT>Bluetooth>Scanners**。如果扫描器被禁用，请确保启用它，然后编辑扫描器设置：

![](../../img/image2022-8-8_12-35-27.webp)

选择 **Filter duplicates**=**keep-newest**。

**keep-newest** 设置将确保“Advertising reports”部分仅保留最新的报告。扫描器捕获的新数据包（针对每个单独的 MAC 地址）将覆盖较旧的数据包。

#### 脚本

导航至 **System>Scripts** 菜单并在其中添加新脚本。

您可以复制下面的脚本。将以下脚本复制到“记事本”中，然后再次复制到脚本的“**Source:**”字段中。

```ros
#### 用户参数
:local addressRegex    "DC:2C:6E:91:D6:F3"
:local urlNotInRange   "https://maker.ifttt.com/trigger/{The_tag_is_NOT_in_range}/json/with/key/-xxxx"
:local urlInRange      "https://maker.ifttt.com/trigger/{The_tag_IS_within_range}/json/with/key/-xxxx"
:local missingInterval 60000

###时间

:local realtime [/system clock get time]
:local realdate [/system clock get date]
:local tonumtime [:tonum [:totime "$realdate $realtime"]];
:local gmt ([system/clock/print as-value]->"gmt-offset")

###使用当前 GMT 偏移 epoch 时间
:global tonumtimeoffset ($tonumtime-$gmt)

:global Epomili
:set Epomili ([$tonumtimeoffset]."000")

###蓝牙
:local adver
:local adver2
:local ts
:local clockmin

:set adver [/iot bluetooth scanners advertisements print detail as-value where address ~ $addressRegex]
:set adver2 ($adver->0)
:set ts ($adver2 -> "epoch")
:set clockmin ($Epomili-$missingInterval)

:local counterIN
:local counterOUT

:if ($ts&lt;=$clockmin) do={
    :set $counterIN 0;
    :if ($counterOUT=0 or $counterOUT=null) do={
        :set $counterOUT 0;
        /tool fetch http-method=get output=user url=$urlNotInRange;
        :set counterOUT ($counterOUT+1);
        :log info "IFTTT 通知 - 标签超出范围！"
    } else={
        :log info "标签超出范围！通知之前已发送！"
    }
} else={
    :set $counterOUT 0;
    :if ($counterIN=0 or $counterIN=null) do={
        :set $counterIN 0;
        /tool fetch http-method=get output=user url=$urlInRange;
        :set $counterIN ($counterIN+1);
        :log info "IFTTT 通知 - 标签在范围内！"
    } else={
        :log info "标签在范围内！通知之前已发送！"
    }
}
```

有 3 行需要特别注意（位于脚本的 **### 用户参数** 部分）。

1) MAC 地址行：

```
:local addressRegex "DC:2C:6E:91:D6:F3"
```

上述行中，您需要输入标签的 MAC 地址（您可以在标签的标签纸上找到 MAC 地址）。

1) 不在范围通知 URL 行：

```
:local urlNotInRange "https://maker.ifttt.com/trigger/{The_tag_is_NOT_in_range}/json/with/key/-xxxx"
```

该行中，您需要输入 IFTTT 服务为您生成的 URL。URL 应类似于 → `https://maker.ifttt.com/trigger/{event}/json/with/key/-xxxxx`。将 URL 中的 `{event}` 部分替换为在 IFTTT 门户创建小程序时选择的 `Event Name`，并将 URL 中的 -**xxxxx** 部分替换为 IFTTT 门户为您生成的密钥。

1) 在范围通知 URL 行：

```
:local urlInRange "https://maker.ifttt.com/trigger/{The_tag_IS_within_range}/json/with/key/-xxxx"
```

该行中，您需要输入 IFTTT 服务为您生成的 URL。URL 应类似于 → `https://maker.ifttt.com/trigger/{event}/json/with/key/-xxxxx`。将 URL 中的 `{event}` 部分替换为在 IFTTT 门户创建第二个小程序时选择的第二个 `Event Name`，并将 URL 中的 -**xxxxx** 部分替换为 IFTTT 门户为您生成的密钥。

为脚本命名，例如，**ifttt** 并保存（点击“Apply”和“OK”）。

**脚本将如何工作？**

我们为脚本应用一个调度器，脚本将按设定的间隔运行。调度器设置将在本指南后面部分展示。

脚本的 **###时间** 部分获取 **/system clock** 时间并计算“**epoch**”时间。当我们有了当前 **/system clock** 时间的“**epoch**”值后，我们可以从中减去 1 分钟。拥有“减去 1 分钟”的 epoch 时间值将帮助脚本将数据包的接收时间与之比较，以判断数据包是否延迟 1 分钟以上，或者是否在当前时间的 1 分钟间隔内。

如果标签移出范围（数据包早于 1 分钟）→ KNOT 将向 IFTTT Webhook 发送 HTTP post（使用“**Event Name**”表示其超出范围），并在 **System>Log** 中记录该事件。

如果标签的数据包被接收且不超过 1 分钟 → KNOT 将向 IFTTT Webhook 发送 HTTP post（使用“**Event Name**”表示其在范围内），并在 **System>Log** 中记录该事件。

“counter”参数将确保您不会在调度器每次运行脚本时收到重复通知，并确保您仅在标签进入范围时收到 1 次通知，在标签移出范围时收到 1 次通知。

#### 调度器

导航至 **System>Scheduler** 并在其中添加新的调度器。

为其命名，例如，**scheduler1**，并设置您希望 KNOT 检查数据包的间隔。

![](../../img/image2022-8-8_13-57-48.webp)

在“**On Event:**”字段中添加一行“/system script run **ifttt**”（其中 **ifttt** 是所创建脚本的名称），点击“**Apply**”和“**OK**”。

### 结果验证

确保您已在手机上登录 IFTTT 应用。

将标签放置在 KNOT 的蓝牙范围内，一旦调度器运行脚本，您应该会收到通知，如下所示：

![](../../img/image2022-8-8_14-15-3.webp)

将标签移出 KNOT 的范围（等待 1 分钟），您将收到另一条通知：

![](../../img/image2022-8-8_14-16-19.webp)