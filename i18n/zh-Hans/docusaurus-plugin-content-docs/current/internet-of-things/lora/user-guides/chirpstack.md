# ChirpStack

> 本页面向 MikroTik RouterOS 用户介绍如何将 LoRaWAN 网关注册到 ChirpStack 开源服务器。

# ChirpStack

[ChirpStack](https://www.chirpstack.io/) 是一款开源 LoRaWAN 服务器，您可以在本地安装部署。

服务器启动并运行后，登录 ChirpStack 管理门户。

## 网关注册

### 注册网关

导航至“租户>网关”部分，点击“添加网关”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_reg_gw.png)

为设备命名，并输入“网关 ID”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_reg_gw_2.png)

在 RouterOS 中，**网关 EUI** 值可在“**IoT>LoRa>设备>网关 ID**”下找到：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack-01.webp)

### 连接网关

网关可通过 **UDP** 或 **LNS** 协议连接。有关两种协议的详细配置方法，请参阅 ChirpStack 文档。

在 RouterOS 中，添加一个新服务器，指向 ChirpStack 的 IP/域名。若使用 UDP：

```ros
/iot lora servers
add address=10.x.x.x name=Chirpstack protocol=UDP
```

若使用 LNS：

```ros
/iot lora servers
add address=10.x.x.x name=Chirpstack port=3001 protocol=LNS ssl=no
```

:::info
端口、地址和 SSL 选项可能因 ChirpStack 自身的配置方式而有所不同。
:::

确保接口已禁用（否则将无法应用任何更改）：

```ros
/iot lora disable [find]
```

将服务器附加到接口：

```ros
/iot lora set servers=Chirpstack [find]
```

启用接口：

```ros
/iot lora enable [find]
```

### 网关注册验证

在 RouterOS 中，您可以通过日志确认网关已连接：

```ros
/log print where topics ~"lora"
```

您应看到“forwarder is ready”消息：

```
 2026-06-15 14:31:09 lora,info [FWD] gateway-0 forwarder started
 2026-06-15 14:31:22 lora,info [FWD] gateway-0 forwarder is ready
 2026-06-15 14:31:41 lora,debug [FWD] gateway-0, Rx, Freq 868.100, CRC Error
 2026-06-15 14:32:10 lora,debug [FWD] gateway-0, Rx, Freq 867.100, CRC Error
```

在 ChirpStack 门户中，可在“网关”仪表板（“租户>网关”部分）下查看状态：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_reg_gw3.png)

## 节点注册

### 创建设备配置文件

添加新的[“设备配置文件”](https://www.chirpstack.io/docs/chirpstack/use/device-profiles.html)：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_device_profile.png)

根据您的节点/传感器所支持的参数，配置“*区域*”、“*MAC 版本*”、“*区域参数修订版*”、“*ADR 算法*”及其他设置。
可选地，您可以启用不同的类别（如 Class B）。

MikroTik **TG-LR** 标签的信息可在[此处](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide)找到。

添加“负载编解码器”：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_device_profile2.png)

- 选择“JavaScript 函数”；
- 将[提供的脚本 **tg-lrx2-2.0-ul-dec.js**](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide#quickstart-guide) 的内容复制/粘贴到“编解码器函数”字段，然后点击“提交”。

### 创建应用

添加新的[“应用”](https://www.chirpstack.io/docs/chirpstack/use/applications.html)：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_appli.png)

### 创建设备

如果您使用的是 **TG-LR** MikroTik 标签，请在包装内的标签上找到“**JoinEUI**”、“**DevEUI**”和“**AppKey**”。如果您使用的是其他厂商的传感器，请通过制造商了解这些信息。

在之前创建的“应用”下添加新的[“设备”](https://www.chirpstack.io/docs/chirpstack/use/devices.html)：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_device.png)

输入“**设备 EUI**”、“**加入 EUI**”，选择之前创建的“设备配置文件”，然后点击“提交”。

最后：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_device2.png)

输入“**应用密钥**”并点击“提交”。

### 开启标签电源

请查阅我们关于 [TG-LR 选项](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide) 的完整指南。

标签初始处于“关机”模式（休眠状态）。

要激活它，请查阅我们的[快速入门指南](/docs/internet-of-things/lora/user-guides/tg-lr-setup-guide#quickstart-guide)，只需将磁铁靠近簧片开关约 1.5 秒，直到看到 2 次 LED 闪烁（之后移开磁铁）。

:::info
使用其他厂商的传感器时，请了解如何激活它。
:::

### 节点注册验证

节点通电后，应立即开始尝试加入网络。

终端设备将发送“Join-request”数据包，并期望收到“Join-accept”作为回应。

在 RouterOS 中，您可以在“**IoT>LoRa>流量**”选项卡中查看该交互过程：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/joinreq_joinacpt.png)

在门户中，您应能通过“LoRaWAN 帧”选项卡确认注册状态：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/chirpstack_verification.png)