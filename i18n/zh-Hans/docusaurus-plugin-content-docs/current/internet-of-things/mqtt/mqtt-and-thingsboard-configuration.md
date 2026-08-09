# MQTT 与 ThingsBoard 配置

> 本页指导 MikroTik RouterOS 用户完成将 MQTT 数据发布到 ThingsBoard 的配置，涵盖设备设置、认证场景（访问令牌、基本凭据、SSL/TLS）以及安全通信的证书管理。

# MQTT 与 ThingsBoard 配置

### 引言

您可以使用众多云服务之一来监控由 MQTT 发布者发送的信息，例如 [Thingsboard](https://thingsboard.io/)。本文将演示如何配置 Thingsboard 和 RouterOS，以使用 MQTT 协议发布数据。在此场景中，RouterOS 将充当网关，将数据从 RouterBoard 发布到 Thingsboard 服务器。而 Thingsboard 将充当 MQTT 代理（服务器，数据将被发布到此处）。

在继续设置之前，您需要：

- a) 在 Thingsboard 系统中创建一个账户。您可以通过此 [链接](https://thingsboard.cloud/signup) 完成注册。这将允许您在有限/测试时间内免费使用 ThingsBoard 云解决方案。
- b) 按照 [指南](https://thingsboard.io/docs/user-guide/install/installation-options/) 设置您自己的服务器。有一个社区版可以免费安装和使用。

:::warning
请考虑使用 **SSL MQTT（TCP 端口 8883 和证书）**，而不是非 SSL MQTT（TCP 端口 1883）。如果您使用非 SSL MQTT，客户端（MQTT 发布者）和服务器（MQTT 代理）之间的通信很容易被嗅探/抓包，这将危及认证数据（如客户端 ID、用户名和密码）。
:::

### Thingsboard 配置

:::info
在本指南中，我们将展示本地实例/服务器安装配置，但相同的原则也适用于云选项。
:::

通过浏览器访问登录页面并登录。进入“**设备**”菜单。

点击添加按钮“+”并选择“添加新设备”来创建新设备：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-01.webp)

输入设备名称并点击“添加”：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-02.webp)

默认情况下，新创建的设备会选用访问令牌认证。

#### 访问令牌场景

您可以通过点击已创建设备并进入“**管理凭据**”设置（在“**详细信息**”部分）来更改令牌：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-03.webp)

此令牌将用作 MQTT 发布者（在 RouterOS 设置中）的“用户名”。

更多信息请参阅此 [链接](https://thingsboard.io/docs/reference/mqtt-api/)。

#### MQTT 基本场景

您可以在特定设备的“**设备凭据**”部分更改凭据类型：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-04.webp)

MQTT 基本场景允许您指定 MQTT 认证的客户端 ID、用户名和密码。

更多信息请参阅此 [链接](https://thingsboard.io/docs/user-guide/basic-mqtt/)。

#### 单向 SSL 通信场景

:::warning
推荐使用的场景！

**重要提示：** 此类型的认证要求您使用服务器证书进行 SSL 通信。必须生成服务器证书并上传到 ThingsBoard 实例。

要生成服务器证书，请参考 [此指南](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) → 生成证书（例如，使用 OPENSSL 工具），将其安装/上传到正确的文件夹，并在 ThingsBoard 配置文件中启用 MQTT SSL。
:::

配置将与上面所示的 **访问令牌** 和 **MQTT 基本场景** 相同。因此请选择其中一种。

在这种情况下，唯一的区别在于设备和服务器之间的通信（您只需稍微更改 RouterOS 设置中的 MQTT 代理配置，稍后将展示）。

**使用此场景时，通信将被加密（使用 SSL）**。

#### X.509（双向 SSL 通信）场景

:::info
此类型的认证要求您使用服务器证书和客户端证书进行 SSL 通信。必须生成服务器证书并上传到 ThingsBoard 实例。

要生成服务器证书，请参考 [此指南](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) → 生成证书（例如，使用 OPENSSL 工具），将其安装/上传到正确的文件夹，并在 ThingsBoard 配置文件中启用 MQTT SSL。

要生成客户端证书，请参考 [此指南](https://thingsboard.io/docs/user-guide/certificates/)。
:::

您可以在特定设备的“**设备凭据**”部分更改凭据类型：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-05.webp)

X.509 场景使用客户端证书进行认证。

生成证书（例如，使用 OpenSSL）后，将 RSA 公钥复制到字段中并点击“保存”按钮。

### RouterOS 配置

***注意**：要配置 MQTT，请确保事先安装了 **iot** [软件包](../../getting-started/installation-and-upgrade/packages.md)。*

#### MQTT 代理

##### 访问令牌场景

按如下所示添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=access_token
```

- 将 `address` 更改为您的 ThingsBoard 服务器的实际 IP/域名地址。
- 将 `username` 更改为您在 ThingsBoard 设置中使用的访问令牌。

##### MQTT 基本场景

按如下所示添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x client-id=clientid password=password username=username
```

- 将 `address` 更改为您的 ThingsBoard 服务器的实际 IP/域名地址；
- 将 `username`、`password` 和 `client-id` 更改为您在 ThingsBoard 设置中使用的实际值。

##### 单向 SSL 通信场景

:::warning
推荐使用的场景！
:::

在此场景中，RouterOS 需要将服务器证书导入其系统。

将已安装到 ThingsBoard 的服务器证书拖放到路由器的“文件列表”菜单中：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-06.webp)

导入服务器证书：

```ros
/certificate/import file-name=mqttserver.pem passphrase=""
```

当使用 **SSL 单向通信** 和 **访问令牌场景** 时，按如下所示添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 username=access_token ssl=yes
```

- 将 `address` 更改为您的 ThingsBoard 服务器的实际 IP/域名地址。
- 将 `username` 更改为您在 ThingsBoard 设置中使用的访问令牌。
- 确保使用 `port=8883`（服务器监听的 MQTT SSL 端口）。
- 确保启用 `ssl=yes`。

当使用 **SSL 单向通信** 和 **MQTT 基本场景** 时，按如下所示添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 client-id=clientid password=password username=username ssl=yes
```

- 将 `address` 更改为您的 ThingsBoard 服务器的实际 IP/域名地址。
- 将 `username`、`password` 和 `client-id` 更改为您在 ThingsBoard 设置中使用的实际值。
- 确保使用 `port=8883`（服务器监听的 MQTT SSL 端口）。
- 确保启用 `ssl=yes`。

##### X.509（双向 SSL 通信）场景

将证书拖放到路由器的“文件/文件列表”菜单中 → *服务器证书、客户端证书及其私钥。*

逐一导入证书：

```ros
/certificate/import file-name=mqttserver.pem passphrase=""
/certificate/import file-name=cert.pem passphrase=""
/certificate/import file-name=key.pem passphrase=""
```

按如下所示添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 certificate=cert.pem_0 ssl=yes
```

- 将 `address` 更改为您的 ThingsBoard 服务器的实际 IP/域名地址。
- 将 `certificate` 选择为您导入的实际客户端证书名称。
- 确保使用 `port=8883`（服务器监听的 MQTT SSL 端口）。
- 确保启用 `ssl=yes`。

#### MQTT 发布

a) 使用静态值快速测试 MQTT 发布：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"cpu\":\"7\"}"
```

b) 为了将 RouterOS 中的相关数据发布到 Thingsboard，您可以使用下面显示的脚本作为参考。该脚本从 RouterOS 设备收集数据（型号名称、序列号、RouterOS 版本、当前 CPU、已用内存、空闲内存和运行时间），并以 JSON 格式将消息（数据）发布到代理：

```ros
# 所需软件包：iot
################################ 配置 ################################  
# 应使用的现有 MQTT 代理名称，用于发布  
:local broker "tb"
# 消息应发布到的 MQTT 主题  
:local topic "v1/devices/me/telemetry"
#################################### 系统 ###################################  
:put ("[\*] 正在收集系统信息...")  
:local cpuLoad [/system/resource/get cpu-load]  
:local freeMemory [/system/resource/get free-memory]  
:local usedMemory ([/system/resource/get total-memory] - $freeMemory)  
:local rosVersion [/system/package/get value-name=version \  
[/system/package/find where name ~ "^routeros"]]  
:local model [/system/routerboard/get value-name=model]  
:local serialNumber [/system/routerboard/get value-name=serial-number]  
:local upTime [/system/resource/get uptime]
#################################### MQTT #####################################  
:local message \  
"{\"model\":\"$model\",\  
\"sn\":\"$serialNumber\",\  
\"ros\":\"$rosVersion\",\  
\"cpu\":$cpuLoad,\  
\"umem\":$usedMemory,\  
\"fmem\":$freeMemory,\  
\"uptime\":\"$upTime\"}"
:log info "$message";  
:put ("[\*] 消息总大小：$[:len $message] 字节")  
:put ("[\*] 正在向 MQTT 代理发送消息...")  
/iot/mqtt/publish broker=$broker topic=$topic message=$message  
:put ("[\*] 完成")
```

应关注脚本中的 2 行。

```ros
:local broker "tb"
```

此行，您应在引号 "" 内指定代理名称。

```ros
:local topic "v1/devices/me/telemetry"
```

此行，您应在引号 "" 内指定正确的主题（请查阅 Thingsboard 的 [文档](https://thingsboard.io/docs/reference/mqtt-api/) 以了解需要使用的确切主题）。

脚本的其余配置取决于整体需求。

将上述脚本复制并粘贴到记事本中，然后再次复制。导航到 系统>脚本 菜单，在那里添加一个新脚本，并粘贴上面显示的脚本。例如，将其命名为 script1。

要运行该脚本，您可以使用命令行：

```ros
/system/script/run script1
```

### 验证

您可以在“**最新遥测**”部分查看设备的接收/发布数据：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/mqtt-and-thingsboard-configuration-07.webp)