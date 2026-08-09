# The Things Stack

> 本页面向 MikroTik RouterOS 用户，指导如何将 LoRaWAN 网关注册到 The Things Stack，涵盖 UDP 与 LNS/CUPS 协议。内容涉及查找 Gateway EUI 值、配置服务器设置、生成认证密钥，以及导入根证书以实现与 TTN 服务器的安全通信。

# The Things Stack

[The Things Stack](https://console.cloud.thethings.network/) 是 The Things Network 的新版本。

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-01.webp)

选择您所在的区域，并使用 The Things Network 账户或其他凭据登录。

## 注册网关

登录后，导航至“Go to gateways”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-02.webp)

点击“**+ Register gateway**”按钮注册网关：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-03.webp)

在此处，网关可通过两种方式连接服务器：

- 使用 UDP 协议；

- 使用 LNS/CUPS 协议。

### UDP 场景

:::warning
[LNS/CUPS](/docs/internet-of-things/lora/user-guides/the-things-stack#lns-and-cups-scenario) 协议更为安全，我们建议优先使用！
:::
UDP 是服务器与网关之间通信的传统方法。

#### UDP 协议网关注册

填写空白字段。输入 **Gateway EUI**。确保选择了正确的频率计划。**不要**启用“**Require authenticated connection**”选项（该选项用于 LNS 和 CUPS）！

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-04.webp)

在 RouterOS 中，**Gateway EUI** 值可在“**IoT>LoRa>Devices>Gateway ID**”下找到：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-05.webp)

更多信息请参阅其[文档页面](https://www.thethingsindustries.com/docs/getting-started/)。

#### UDP 协议 RouterOS 配置

请仔细确认 LoRa 设备（在 RouterOS 中）已选择正确的 TTN 服务器，且服务器设置使用“UDP”协议：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-06.webp)

### LNS 和 CUPS 场景

[**LNS/CUPS**](https://www.thethingsindustries.com/docs/hardware/gateways/concepts/lora-basics-station/) 是现代协议。它们通过使用 TCP（TLS）提供更高的安全性，每个数据包都会被加密，并引入了基于证书的网关认证（以及其他新功能）。

#### LNS 和 CUPS 协议网关注册

填写空白字段。输入 **Gateway EUI**。确保选择了正确的频率计划。启用“**Require authenticated connection**”以及后续的（针对 LNS）“**Generate API key for LNS**”和（针对 CUPS）“**Generate API key for CUPS**”选项：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-07.webp)

在 RouterOS 中，**Gateway EUI** 值可在“**IoT>LoRa>Devices>Gateway ID**”下找到：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-05.webp)

点击“**Register gateway**”按钮后，系统会提示您下载密钥。请下载它们。

要查看 LNS 和 CUPS 密钥，请检查下载的文件。LNS 密钥也应显示在“**LoRa Basics Station LNS authentication Key**”字段下：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-08.webp)

更多信息请参阅其[文档页面](https://www.thethingsindustries.com/docs/getting-started/)。

#### LNS 协议 RouterOS 设置

确保选择了正确的 TTN 服务器，配置了正确的端口（TTN 期望 LNS 使用 8887 端口），选择了 LNS 协议，输入了 LNS 密钥（来自“**LoRa Basics Station LNS authentication Key**”字段），并启用了“**SSL**”复选框：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-09.webp)

如果您使用默认设置，网关内部的 [**builtin-trust-store**](/docs/authentication-authorization-accounting/certificates#settings) 应为 **lora** 服务启用，并且应已预装所需的 Root CA。**您可以跳到下一步**。

**可选地**，如果您已禁用 [**builtin-trust-store**](/docs/authentication-authorization-accounting/certificates#settings) 并希望手动上传证书，请下载并导入[根证书](https://www.thethingsindustries.com/docs/reference/root-certificates/)。

下载证书文件后，将其拖放到 RouterOS 文件菜单中并导入证书列表：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-10.webp)

这应使证书列表受信任：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-11.webp)

#### CUPS 协议 RouterOS 设置

确保选择了正确的 TTN 服务器，配置了正确的端口（TTN 期望 CUPS 使用 443 端口），选择了 CUPS 协议，输入了 CUPS 密钥（在网关注册步骤中从下载的 cups.key 文件中获取），并启用了“**SSL**”复选框：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-12.webp)

如果您使用默认设置，网关内部的 [**builtin-trust-store**](/docs/authentication-authorization-accounting/certificates#settings) 应为 **lora** 服务启用，并且应已预装所需的 Root CA。**您可以跳到下一步**。

**可选地**，如果您已禁用 [**builtin-trust-store**](/docs/authentication-authorization-accounting/certificates#settings) 并希望手动上传证书，请下载并导入[根证书](https://www.thethingsindustries.com/docs/reference/root-certificates/)。

下载证书文件后，将其拖放到 RouterOS 文件菜单中并导入证书列表：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-10.webp)

这应使证书列表受信任：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-11.webp)

### 网关注册验证

如果一切配置正确，在 RouterOS 中启用 LoRa 接口后（“**IoT>LoRa>Devices>Enable**”）：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-13.webp)

您应看到网关连接的“Live data”更新：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/the-things-stack-14.webp)

## 注册节点

在本节中，我们将演示如何将 MikroTik 的 **TG-LR** 标签（[**TG-LR82**](https://mikrotik.com/product/tg_lr82) 或 [**TG-LR92**](https://mikrotik.com/product/tg_lr92)）添加到门户。

相同原则适用于其他厂商的节点/传感器/标签。

### 创建应用程序

在 TTS 门户上，导航至“**Applications**”选项卡并点击“**add application**”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tts_appli_1.png)

输入您想要的 ID，为其命名，添加描述，然后创建它（“**Create application**”）：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tts_appli_2.png)

### 注册终端设备

在您刚创建的应用程序下，导航至“**End devices**”选项卡并点击“**+ Register end device**”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tts_device_1.png)

您可以选择“Select the end device in the LoRaWAN Device Repository”（并自动化该过程），也可以手动添加（“Enter end device specifics manually”）：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tts_device_2.png)

- 输入“**Frequency plan**”（例如，*Europe 863-870 MHz (SF9 for RX2 - recommended)*，具体取决于您的标签支持的频率）；
- “**LoRaWAN version**”（“*LoRaWAN Specification 1.0.4*”）；
- “**Regional Parameters version**”（“*RP002 Regional Parameters 1.0.4*”）。

找到包装内标签上印制的“**JoinEUI**”、“**DevEUI**”和“**AppKey**”，并继续提供配置信息：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tts_device_3.png)

- 输入标签上的“**JoinEUI**”，并“Confirm”确认；
- 输入标签上的“**DevEUI**”；
- 输入标签上的“**AppKey**”；
- 为您的标签设置 ID/名称；
- 点击“**Register end device**”。

### 启用解码器

:::info
如果跳过此步骤，TTS 门户将仅显示“原始十六进制”负载。
:::

为了使服务器以可读/可理解的格式显示标签数据，它首先需要能够“解码”接收到的负载。
您可以在新创建的标签选项下的“[Payload formatters](https://www.thethingsindustries.com/docs/integrations/payload-formatters/)”部分输入解码器脚本：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/payload_decoder.png)

- 选择“Custom Javascript formatter”；
- 将[提供的脚本 **tg-lrx2-2.0-ul-dec.js**](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide#quickstart-guide) 的内容复制/粘贴到“Formatter code”字段中，并“Save changes”保存更改。

### 标签开机

请参阅我们关于 [TG-LR 选项](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide) 的完整指南。

初始状态下，标签将处于“Shutdown”模式（休眠状态）。

要激活它，请参阅我们的[快速入门指南](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide#quickstart-guide)，只需将磁铁靠近干簧管约 1.5 秒，直到看到 LED 闪烁 2 次（之后移开磁铁）。

### 节点注册验证

节点一旦通电，应立即开始尝试[加入网络](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/)。

终端设备将发送“Join-request”数据包，并期望收到“Join-accept”作为回应。

在 RouterOS 中，您可以在“**IoT>LoRa>Traffic**”选项卡中查看该交互过程：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/joinreq_joinacpt.png)

最后，您应能够根据 TTS 日志确认注册成功：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tag_reg_verification.png)