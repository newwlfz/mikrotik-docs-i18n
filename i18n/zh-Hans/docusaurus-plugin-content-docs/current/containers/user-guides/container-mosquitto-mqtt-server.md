# Container - mosquitto MQTT 服务器

> 本页介绍如何使用 MikroTik RouterOS 容器运行 eclipse-mosquitto MQTT 服务器，用于物联网应用，详细说明容器设置步骤，包括网络、环境变量和挂载，并附带 SSL 支持警告。

# Container - mosquitto MQTT 服务器

## 简介

RouterOS 引入容器功能后，可以在路由器内部运行各种类型的服务器，用于处理各类任务。这对于希望减少网络中设备数量的用户尤其重要。与其在单独的设备/机器上运行服务器，为何不直接在路由器内部运行呢？

在本指南中，我们将演示如何安装一个名为 [eclipse-mosquitto](https://mosquitto.org/) 的基础 MQTT 代理（或者说，服务器）。MQTT 协议是一种非常流行的选择，尤其是在物联网拓扑中。它是一种开放的 OASIS 和 ISO 标准轻量级发布/订阅网络协议，用于在设备之间传输消息。典型的拓扑结构包括一个 MQTT 发布者（发送信息的设备）、一个 MQTT 代理（存储数据的服务器）和一个 MQTT 订阅者（监听服务器上发布数据的设备）。

RouterOS 支持 [MQTT 发布、订阅](../../internet-of-things/mqtt/index.md) 功能，现在，我们也可以运行 MQTT 代理。

我们将使用的镜像可以通过以下 hub.docker [链接](https://hub.docker.com/_/eclipse-mosquitto) 找到。

## 摘要

在进行配置之前，请务必先学习我们的 [container](../) 指南。请务必查看 [免责声明](../#disclaimer) 和 [要求](../#requirements) 部分，以了解所有风险以及您可能需要采取的步骤。

您可以通过以下 [链接](https://hub.docker.com/_/eclipse-mosquitto/tags) 找到支持的架构。

在指南发布时，**eclipse-mosquitto** 镜像可用于 ARM32、ARM64 和 AMD64（CHR 和 x86）设备。在此示例中，我们将在 ARM32 架构设备 → [RB1100AHx4](https://mikrotik.com/product/rb1100ahx4) 上运行它。

:::warning

将展示**非常基础**且**快速**的配置。请务必查看 [mosquitto 文档](https://mosquitto.org/documentation/) 页面，了解您可以实施的更多选项和设置。如果您想将其用于生产环境，请**务必尽可能加强安全性**：

- [防火墙](../../firewall-and-quality-of-service/firewall/index.md)，以便仅允许来自您信任的 IP 地址访问容器；
- 从 mosquitto 代理/服务器端提高安全性 → 使用强密码、非标准端口等；
- 使用 SSL MQTT。

:::

## 容器配置

**子菜单：** `/container`

***注意***：需要 **container** 软件包。

### 容器模式

启用容器模式：

```ros
/system/device-mode/update container=yes
```

您需要按复位按钮确认设备模式，或者如果在 X86 上使用容器，则需要进行冷重启。

### 网络设置

为容器添加 veth 接口：

```ros
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```

为容器创建网桥并将 veth 添加到其中：

```ros
/interface/bridge/add name=msqt
/ip/address/add address=172.19.0.1/24 interface=msqt
/interface/bridge/port/add bridge=msqt interface=veth2
```

如果 NAT 是必需的（可选），为测试目的转发 TCP 1883 端口以用于非 SSL MQTT（其中 192.168.88.1 是设备的 LAN IP 地址）：

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.19.0.2 to-ports=1883
```

### 环境变量和挂载

根据 eclipse-mosquitto docker hub 的要求，为配置文件定义一个挂载。我们将挂载整个文件夹，而不仅仅是配置文件，因为对于 SSL MQTT，我们还需要将证书上传到该文件夹中：

```ros
/container/mounts/add list=msqt_config src=/mosquitto_mounted dst=/mosquitto/config
```

### 获取镜像

为了简化配置，我们将从外部库获取镜像，但您也可以通过 [.tar](../#option-b-import-image-from-pc) 文件导入。

在此示例中，我们将使用设备自身的存储空间。RB1100AHx4 拥有 128 MB 磁盘空间，基本的 mosquitto 安装不应占用超过约 15 MB。

确保正确设置“Registry URL”，限制 RAM 使用量（如有必要），并为镜像设置目录：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```

### 拉取镜像

```ros
/container/add remote-image=library/eclipse-mosquitto:latest interface=veth2 root-dir=mosquitto mountlists=msqt_config logging=yes
```

运行命令后，RouterOS 应开始“解压”软件包。检查“文件系统”中是否有新创建的文件夹，并使用 `/container/print` 命令监控容器状态。

### 设置 mosquitto 配置文件

要获取 **mosquitto.conf** 文件，我们需要使用 SFTP（基于 SSH 的文件传输）协议，因此请确保 SSH [服务](../../system-information-and-utilities/services.md) 已启用。您也可以使用 FTP。

打开您的命令终端（Windows 用户以管理员身份打开“CMD”，Linux 用户打开“Linux Shell 或命令终端”），并导航到您想要下载配置文件的目录。例如，到您“桌面”上的“Container”文件夹：

```powershell
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\Container

C:\Users\Administrator\Desktop\Container>
```

启动到设备 IP 地址的 SFTP 会话：

```powershell
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:lfxxs+xMrXlvP7hiHi9ZAEZlPi6/c5US+r6J7ljhkaA.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
Warning: Permanently added '192.168.88.1' (RSA) to the list of known hosts.
Connected to 192.168.88.1.
sftp>
```

转到 mosquitto 配置文件文件夹（使用 `dir` 或 `ls` 命令查看当前文件夹内容，使用 `cd` 命令转到您选择的文件夹）。默认情况下，配置从“/mosquitto/config/mosquitto.conf”加载，因此，导航到那里并使用 `get` 命令下载它：

```powershell
sftp> cd mosquitto/mosquitto/config
sftp> dir
mosquitto.conf
sftp> get mosquitto.conf
Fetching /mosquitto/mosquitto/config/mosquitto.conf to mosquitto.conf
/mosquitto/mosquitto/config/mosquitto.conf
```

使用您喜欢的文本编辑器（记事本或其他）打开“**mosquitto.conf**”，并仅用下面显示的两行覆盖它：

:::warning

在本节中，我们将为测试目的配置一个基本的非 SSL MQTT 设置。除非您确定已实施所需的安全/限制措施，否则非 SSL MQTT 对于生产环境是不安全的。

对于生产环境，在 MQTT 流量可能被捕获/嗅探的拓扑中，和/或在 MQTT 流量直接通过互联网（而非本地）路由的拓扑中，请使用 SSL MQTT。查看 [SSL MQTT 部分](./container-mosquitto-mqtt-server.md#ssl-mqtt) 了解更多信息。

:::

```text
listener 1883
allow_anonymous true
```

- 第一行，**listener 1883**，将使安装监听指定端口上的传入网络连接。
- 第二行，**allow\_anonymous true**，决定是否允许未提供用户名的客户端连接。

使用相同的 **mosquitto.conf** 文件名覆盖该文件。

创建您自己的自定义配置文件后，将其上传到挂载的目录/文件夹“**mosquitto\_mounted**”中。如果您尚未运行容器，则不会有“**mosquitto\_mounted**”文件夹，您可以手动创建。如果您确实运行了它（`/container/start 0`），它应该已自动创建：

```powershell
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
```

从编辑后的 mosquitto.conf 文件所在目录使用 SFTP，并将其 `put` 到挂载目录中：

```powershell
C:\Users\Administrator\Desktop\Container>dir
 Directory of C:\Users\Administrator\Desktop\Container

02/03/2023  12:09 PM    <DIR>          .
02/03/2023  12:09 PM    <DIR>          ..
02/03/2023  12:09 PM            40,449 mosquitto.conf
               1 File(s)         40,449 bytes
               2 Dir(s)  76,166,430,720 bytes free

C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> dir
mosquitto           mosquitto_mounted   pub                 pull                skins
sftp> cd mosquitto_mounted
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    40.5KB/s   00:00
```

重启容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

在再次启动之前，请确保等待容器停止（使用 `/container/print` 命令后应显示 `status=stopped`）。

### 启动容器

在您确认容器已添加并且使用 `/container/print` 后状态已变为 `status=stopped` → 您可以启动它：

```ros
/container/start 0
```

如果您已启用容器日志记录，您将在 [日志](../../diagnostics-monitoring-and-troubleshooting/log/index.md) 部分看到类似这样的内容：

```text
 12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 starting
 12:12:46 container,info,debug 1707214366: Config loaded from /mosquitto/config/mosquitto.conf.
 12:12:46 container,info,debug 1707214366: Opening ipv4 listen socket on port 1883.
 12:12:46 container,info,debug 1707214366: Opening ipv6 listen socket on port 1883.
 12:12:46 container,info,debug 1707214366: mosquitto version 2.0.18 running
```

## MQTT 发布和订阅

**子菜单：** `/iot/mqtt`

***注意***：需要 **iot** 软件包。

添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=mosquitto username=test address=172.19.0.2
```

订阅 MQTT 代理和所需主题：

```ros
/iot/mqtt/subscribe broker=mosquitto topic=test/topic
```

发布静态 MQTT 消息：

```ros
/iot/mqtt/publish broker="mosquitto" topic="test/topic" message="{\"test\":\"123\"}"
```

检查订阅以获取接收到的消息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=mosquitto topic="test/topic" data="{"test":"123"}" 
   time=2023-07-12 10:01:40 
```

您也可以检查容器日志（如果已启用），以确认 mosquitto 正在运行：

```text
 12:47:28 container,info,debug 1675421248: New connection from 172.19.0.1:42240 on port 1883.
 12:47:28 container,info,debug 1675421248: New client connected from 172.19.0.1:42240 as MTD8580EC793C4 (p2, c1, k60, u'test').
 12:47:38 container,info,debug 1675421258: Client MTD8580EC793C4 disconnected.
```

## SSL MQTT

在生产环境中使用**非 SSL MQTT** **是不安全的**。攻击者可以轻松地[捕获/嗅探](../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md)代理和发布者之间的数据包交换，从而获取用户凭据和其他敏感信息。

为了提高安全性，请使用 SSL MQTT。

第一步是生成证书。在此示例中，我们将使用一个简单的 Root CA 方案（无需设备/客户端证书）。

请使用官方的 [mosquitto-tls 用户指南](https://mosquitto.org/man/mosquitto-tls-7.html) 获取分步说明。

### 服务器配置

您应该已经生成了 ca.crt（证书颁发机构文件）、server.crt（服务器证书）和 server.key（服务器密钥）：

```powershell
C:\Users\Administrator\Desktop\Container>dir
 Directory of C:\Users\Administrator\Desktop\Container

07/12/2023  10:58 AM    <DIR>          .
07/12/2023  10:58 AM    <DIR>          ..
07/12/2023  10:56 AM             1,322 ca.crt
07/12/2023  10:56 AM             1,854 ca.key
07/12/2023  09:57 AM                35 mosquitto.conf
07/12/2023  10:58 AM             1,164 server.crt
07/12/2023  10:57 AM               960 server.csr
07/12/2023  10:56 AM             1,704 server.key
               6 File(s)          7,039 bytes
               2 Dir(s)  52,401,184,768 bytes free
```

使用您喜欢的文本编辑器（记事本或其他）打开挂载的“**mosquitto.conf**”，并仅用下面显示的行覆盖它：

```text
tls_version tlsv1.2
port 8883
allow_anonymous true
cafile /mosquitto/config/ca.crt
keyfile /mosquitto/config/server.key
certfile /mosquitto/config/server.crt
```

- **tls\_version** 行设置最低 TLS 版本。
- **port 8883** 将使安装监听指定端口上的传入网络连接。
- **allow\_anonymous true** 决定是否允许未提供用户名的客户端连接。

:::warning

我们使用基本的 SSL 配置进行测试。**allow\_anonymous true** 对于生产环境来说不是一个安全的设置。

:::

- **cafile /mosquitto/config/ca.crt** 行指定 CA 证书文件的路径。
- **keyfile /mosquitto/config/server.key** 行指定服务器密钥文件的路径。
- **certfile /mosquitto/config/server.crt** 行指定服务器证书文件的路径。

将证书文件和更新后的、支持 SSL 的 mosquitto.conf 文件上传到挂载的文件夹“**mosquitto\_mounted**”中：

```powershell
C:\Users\Administrator\Desktop\Container>sftp admin@192.168.88.1
Connected to 192.168.88.1.
sftp> cd mosquitto_mounted
sftp> dir
mosquitto.conf
sftp> put ca.crt
Uploading ca.crt to /mosquitto_mounted/ca.crt
ca.crt                                                                                100% 1322   323.0KB/s   00:00
sftp> put server.crt
Uploading server.crt to /mosquitto_mounted/server.crt
server.crt                                                                            100% 1164   227.3KB/s   00:00
sftp> put server.key
Uploading server.key to /mosquitto_mounted/server.key
server.key                                                                            100% 1704   415.7KB/s   00:00
sftp> dir
ca.crt           mosquitto.conf   server.crt       server.key
sftp> put mosquitto.conf
Uploading mosquitto.conf to /mosquitto_mounted/mosquitto.conf
mosquitto.conf                                                                        100%  162    32.2KB/s   00:00
```

重启容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

使用日志确认代理正在监听 8883 端口：

```text
 11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 starting
 11:20:41 container,info,debug 1689160841: Config loaded from /mosquitto/config/mosquitto.conf.
 11:20:41 container,info,debug 1689160841: Opening ipv4 listen socket on port 8883.
 11:20:41 container,info,debug 1689160841: Opening ipv6 listen socket on port 8883.
 11:20:41 container,info,debug 1689160841: mosquitto version 2.0.15 running
 11:22:24 system,info,account user admin logged in from 10.5.217.34 via local
```

### 测试连接

将 CA 证书（**ca.crt**）上传到 RouterOS 设备的“文件列表”中：

```ros
/file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME                TYPE             SIZE  CREATION-TIME      
0  skins               directory              1970-01-01 03:00:02
1  pub                 directory              2023-01-04 11:05:04
2  disk7               disk                   2023-07-12 09:52:07
3  mosquitto           container store        2023-07-12 09:52:09
4  mosquitto_mounted   container store        2023-07-25 16:38:37
5  pull                directory              2023-07-12 09:52:09
6  ca.crt              .crt file        1322  2023-07-12 11:28:23
```

导入证书：

```ros
/certificate/import file-name=ca.crt passphrase=""
```

为 SSL 连接添加 MQTT 代理：

```ros
/iot/mqtt/brokers/add name=mosquittoSSL username=test address=172.19.0.2 port=8883 ssl=yes
```

订阅 MQTT 代理和所需主题：

```ros
/iot/mqtt/subscribe broker=mosquittoSSL topic=test/topic
```

发布静态 MQTT 消息：

```ros
/iot/mqtt/publish broker="mosquittoSSL" topic="test/topic" message="{\"test\":\"123\"}"
```

检查订阅以获取接收到的消息：

```ros
/iot/mqtt/subscriptions/recv/print
 0 broker=mosquittoSSL topic="test/topic" data="{"test":"123"}" 
   time=2023-07-12 10:20:40 
```