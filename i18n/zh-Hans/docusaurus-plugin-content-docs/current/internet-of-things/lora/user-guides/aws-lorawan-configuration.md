# AWS LoRaWAN 配置

> 本页面指导用户如何在 MikroTik RouterOS 上配置 AWS LoRaWAN 集成，涵盖在 AWS IoT Core 中注册网关、生成并导入证书，以及为 LNS 连接设置服务器。

# AWS LoRaWAN 配置

:::info
此场景将从 RouterOS 版本 **7.14beta8** 开始支持。
:::

在继续设置之前，您需要在 AWS 系统中创建一个账户。您可以点击此[链接](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)了解更多相关信息。

登录后，请在门户中进入 **Services>IoT Core** 部分。

## AWS - 注册网关

第一步是注册 LoRaWAN 网关。

导航至 [Gateways](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/wireless/gateways) 部分（位于 [LPWAN devices](https://eu-central-1.console.aws.amazon.com/iot/home?region=eu-central-1#/wireless/landing) 下）。

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-01.webp)

点击“**Add gateway**”按钮。

### 步骤 1 - 添加网关

- 输入网关的 EUI。
- 选择设备的频段。
- 如有需要，配置可选字段。

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-02.webp)

再次点击“**Add gateway**”完成此步骤。

在 RouterOS 设置中，可以在 **IoT>LoRa>Devices** 标签页下查看网关的 EUI 和频率计划：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-03.webp)

### 步骤 2 - 配置您的网关

- 生成网关证书（“**Create certificate**”按钮），并下载证书文件和私钥文件（“**Download certificate files**”按钮）。
- 复制 CUPS 和 LNS 端点，并下载服务器信任证书（“**Download server trust certificates**”按钮）。
- 添加建议的网关权限。

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-04.webp)

点击“**Submit**”完成此步骤。

您将被重定向到显示新创建网关的页面。

## RouterOS - 连接网关

### 上传和导入证书

:::info
默认情况下，**lora** 服务在[证书 **trust-store**](/docs/authentication-authorization-accounting/certificates) 中是受信任的，并且内置存储已包含所需的 AWS Root 证书。
以下步骤展示了如果您希望手动操作，如何获取和安装 AWS Root 证书。

如果在[证书 **trust-store**](/docs/authentication-authorization-accounting/certificates) 中启用了 **lora** 服务，请跳过导入 AWS Root CA。您仍然需要导入唯一的设备证书。
:::

在继续设置之前，您需要下载 [Amazon Root CA](https://www.amazontrust.com/repository/) 并将其与网关证书文件及其密钥一起上传到 RouterOS 文件列表菜单中：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-05.webp)

文件上传后，请逐一导入证书（在 **System>Certificates** 下）：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-06.webp)

请确保先上传网关证书，然后再上传其密钥（以便网关证书同时具有 K-key 和 T-trusted 标志）。最终，您应该成功导入所有 3 个文件，如下所示：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-07.webp)

### 服务器配置

#### LNS 场景

导航至 **IoT>LoRa>Servers** 标签页并添加新服务器：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-08.webp)

- 为服务器命名。
- 输入 LNS 端点地址（不含 `wss://` 和 `:443`）。
- 选择 LNS 协议。
- 将端口更改为“443”。
- 启用 SSL 复选框。
- 选择网关证书。

确保在 **IoT>LoRa>Devices** 标签页下应用新配置的服务器：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-09.webp)

然后，**启用** LoRa 接口。

#### CUPS 场景

导航至 **IoT>LoRa>Servers** 标签页并添加新服务器：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-10.webp)

- 为服务器命名。
- 输入 CUPS 端点地址（不含 `https://` 和 `:443`）。
- 选择 CUPS 协议。
- 将端口更改为“443”。
- 启用 SSL 复选框。
- 选择网关证书。

确保在 **IoT>LoRa>Devices** 标签页下应用新配置的服务器：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-11.webp)

然后，**启用** LoRa 接口。

### 连接验证

如果一切配置正确，您应该在 AWS 门户上看到“connected”状态：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/aws-lorawan-configuration-12.webp)