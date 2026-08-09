# 容器 - ThingsBoard MQTT/HTTP 服务器

> 本页面介绍 MikroTik RouterOS 中的容器功能，使用户能够直接在路由器上运行 ThingsBoard MQTT/HTTP IoT 平台等服务器。文中说明了如何配置容器模式、网络接口（veth 和 bridge）、用于出站流量的 NAT 规则以及存储要求。本指南强调了 RAM/磁盘空间方面的考量，并提供了使用

# 容器 - ThingsBoard MQTT/HTTP 服务器

RouterOS 中引入容器功能后，用户可以在路由器内部运行各种类型的服务器以完成各类任务。这对于希望减少网络中设备数量的用户尤其有用。与其在单独的设备/机器上运行服务器，为何不直接在路由器内部运行呢？

许多用户需要一个能够收集数据、存储数据并以易于理解的方式展示数据的服务器。这时，像 [ThingsBoard](https://thingsboard.io/) 这样的平台就可以发挥作用了。

它主要定位为 IoT 平台，您可以在[此链接](https://thingsboard.io/iot-use-cases/)中找到其展示的各种用例。

从 RouterOS 用户的角度来看，最吸引人的一点是，它可以作为 MQTT 服务器（MQTT broker）或 HTTP 服务器使用，这意味着您可以使用 [MQTT 发布](../../internet-of-things/mqtt/index.md) 或 [HTTP 提交](../../system-information-and-utilities/fetch.md) 来发布数据。您可以在此[链接](https://thingsboard.io/docs/reference/mqtt-api/)找到 ThingsBoard MQTT API 指南，并在此[链接](https://thingsboard.io/docs/reference/http-api/)找到 HTTP API 指南。

简而言之，您可以使用[脚本](../../developer-guides/scripting/index.md)来收集 RouterOS 统计数据（如运行时间、GPS 坐标、数据包统计以及几乎所有您能在终端中打印出来的信息），然后将这些信息存储到变量中，并据此构建 JSON 消息。随后，您可以通过[调度器](../../system-information-and-utilities/scheduler.md)（在您需要时运行此脚本）使用 MQTT 或 HTTP 提交方式将此消息发送到 ThingsBoard。您可以在[本指南](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md)中找到执行此操作的基本脚本示例。

ThingsBoard 将借助[组件](https://thingsboard.io/docs/user-guide/ui/widget-library/)来存储和展示数据，这些组件可帮助您设置仪表板，以图表、表格、地图等方式可视化数据。

例如，以下提供了两种 ThingsBoard 实例选项，每种都使用不同的数据库：

- [thingsboard/tb-postgres](https://hub.docker.com/r/thingsboard/tb-postgres/)
- [thingsboard/tb-cassandra](https://hub.docker.com/r/thingsboard/tb-cassandra/)

您可以在 ThingsBoard/docker 文档中找到更多信息。

在我们的示例中，我们将展示 **tb-postgres** - 一个带有 PostgreSQL 数据库的 ThingsBoard 单实例，用于测试目的。

本指南将展示“内存中”队列类型的服务，但对于生产环境，请考虑使用其他服务类型。您可以在此[链接](https://thingsboard.io/docs/user-guide/install/docker/)找到更多信息。

## 摘要

**子菜单：** `/container`

***注意***：*需要 **container** 软件包。*

早于 v7.8 的 RouterOS 版本将无法运行此场景。

在继续配置之前，请务必研读我们的[容器](../)指南。请务必查看[免责声明](../#disclaimer)和[要求](../#requirements)部分，以了解所有风险以及您可能需要执行的必要步骤。

在此示例中，我们将在[云托管路由器，CHR](../../getting-started/routeros-licensing/chr/index.md) 上运行它。

在本指南发布时，**thingsboard/tb-postgres** 镜像仅适用于 linux/**arm64** 和 linux/**amd64** 操作系统/架构。这意味着您无法在我们的 arm32 位架构 RouterOS 设备上运行此场景。

有几个参数需要牢记：

- 您需要了解这是一个**服务器**，并且您需要有额外的空间来存储数据以及镜像本身。在我们的测试中，8 GB 的磁盘空间绰绰有余，但是！对于实际应用，您可能需要考虑增加更多空间，尤其是如果您计划运行更多容器。请记住 → 最好有备用空间。
- 与磁盘空间一样，RAM 内存也很重要。根据 ThingsBoard 文档，当使用带有 PostgreSQL 数据库的 ThingsBoard 单实例时，建议至少分配 1GB 的 RAM，并承受最低负载（每秒几条消息）。建议使用 2-4GB RAM。换句话说，如果您想在 RouterBoard 设备上运行它，请理解在 RAM 低于 1 GB 的设备上可能无法实现。这就是为什么 → 请考虑使用具有更多可用 RAM 内存的设备。

请参阅[技巧和窍门](../#tips-and-tricks)部分，了解如何限制 RAM。

## 配置

### 容器模式

启用容器模式：

```ros
/system/device-mode/update container=yes
```

您需要按下重置按钮确认设备模式，或者如果在 X86 上使用容器，则需要进行冷重启。

### 网络

为容器添加 veth 接口

```ros
/interface/veth/add name=veth1 address=172.18.0.2/24 gateway=172.18.0.1
```

为容器创建网桥，为其分配 IP 网络，并将 veth 添加到网桥

```ros
/interface/bridge/add name=dockertb
/ip/address/add address=172.18.0.1/24 interface=dockertb
/interface/bridge/port/add bridge=dockertb interface=veth1
```

为出站流量设置 NAT

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.18.0.0/24
```

转发 TCP 9090 端口用于 HTTP 管理（根据 ThingsBoard 文档，这是默认 HTTP 端口）

:::warning

我们建议仅在本地测试或通过 VPN 时使用 HTTP 访问（当您确定本地网络安全时）。

当您想从互联网（公共网络/WAN）访问容器 WEB 管理时，请改用 **HTTPS**。

:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=9090 protocol=tcp to-addresses=172.18.0.2 to-ports=9090
```

在上面显示的 DNAT（dst-nat）规则中的 `dst-address` 字段中，我们使用了设备的本地 IP 地址。首先，**使用本地 IP**（本地访问）**来** **设置一切** **并** **确认一切正常**。

:::info
在完成本指南中显示的其余步骤并验证 ThingsBoard 管理门户在本地正常工作后 →  **进一步保护设置**：
>
- (a) 确保所有默认的 ThingsBoard 用户凭据都已更改/删除，并实施了强密码（参考 ThingsBoard 文档）；
- (b) **启用** **HTTPS**（步骤将在本指南后面解释）；
- (c) 最好将 HTTPS 端口更改为非标准端口（参考 ThingsBoard 文档）。
>
只有当您增强了安全性，并且只有那时 → 您才可以考虑启用来自 WAN 的远程访问（在 `dst-address` 字段中使用您的公共 IP 地址，而不是上面示例中使用的本地 IP）。此外，为了进一步提高安全性，请使用 `src-address` 或 `src-address-list` 参数，您可以在其中输入您信任的公共源 IP 地址（已知/受信任的地址列表，例如，属于您希望访问服务器的分支机构的地址）。请理解，只有您自己对安全负责。如果您留了一扇门开着，有人可能会利用它。在设置此类场景时，您需要具备网络知识并了解相关风险。
:::

转发 TCP 1883 端口用于非 SSL MQTT（根据 ThingsBoard 文档，这是默认 MQTT 端口）

:::warning
我们建议仅在本地测试或通过 VPN 时使用非 SSL MQTT（TCP 1883）通信（当您确定本地网络安全时）。
>
在实际应用中，当涉及从互联网（公共网络）访问时，请考虑使用 **SSL MQTT（TCP 端口 8883）**，而不是非 SSL MQTT（TCP 端口 1883）。如果您使用非 SSL MQTT，客户端（MQTT 发布者）和服务器（MQTT broker）之间的通信很容易被嗅探/数据包捕获，这将危及身份验证数据（如客户端 ID、用户名和密码）。
:::

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=1883 protocol=tcp to-addresses=172.18.0.2 to-ports=1883
```

与 HTTP 访问一样，在上面显示的 DNAT（dst-nat）规则中的 `dst-address` 字段中，我们使用了设备的本地 IP 地址。首先，**使用本地 IP**（本地访问）**来** **设置一切** **并** **确认一切正常**。

:::info
在完成本指南中显示的其余步骤并验证 ThingsBoard 非 SSL MQTT 通信在本地正常工作后 →  **进一步保护设置**：
>
- (a) 考虑从 ThingsBoard 安装中移除模板设备；
- (b) **启用 SSL MQTT**（步骤将在本指南后面解释）；
- (c) 最好将 MQTT 端口更改为非标准端口（参考 ThingsBoard 文档）。
>
当您启用 SSL MQTT 时，您可以考虑从 WAN 开放 TCP 8883（这是默认的 SSL MQTT 端口）（在 `dst-address` 字段中使用您的公共 IP 地址而不是本地 IP，并将 `dst-port` 和 `to-ports` 从 1883 更改为 8883）。此外，为了进一步提高安全性，请使用 `src-address` 或 `src-address-list` 参数，您可以在其中设置您信任的公共 IP 地址列表。这样，只有配置的受信任 IP 才能与 ThingsBoard broker 建立 MQTT 连接。
:::

### 环境变量和挂载

请查阅 [docker-thingsboard](https://hub.docker.com/r/thingsboard/tb-postgres) 文档，了解需要添加的确切挂载和变量。

#### 环境变量

```ros
/container/envs/add list=tb_envs key=TB_QUEUE_TYPE value="in-memory"
```

#### 挂载

```ros
/container/mounts/add list=mytb-data src=tb/mytb-data dst=/data
/container/mounts/add list=mytb-logs src=tb/mytb-logs dst=/var/log/thingsboard
```

### 获取镜像

为简化配置，我们将从外部库获取镜像，但您也可以通过 [.tar](../#option-b-import-image-from-pc) 文件导入。

确保您已正确设置“Registry URL”，限制 RAM 使用（如有必要），并为镜像设置目录。

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull ram-high=2048.0MiB
```

拉取镜像：

```ros
/container/add remote-image=thingsboard/tb-postgres:latest interface=veth1 root-dir=ThingsBoard mountlists=mytb-data,mytb-logs envlists=tb_envs logging=yes
```

运行命令后，RouterOS 应开始“解压”软件包。检查“文件系统”中新建的文件夹，并使用 `/container/print` 命令监控容器状态。

### 启动容器

在您确认容器已添加且使用 `/container/print` 后状态已变为 `status=stopped` 后，您可以启动它：

```ros
/container/start 0
```

等待几分钟让容器完全加载。

## 验证

### 管理访问

容器启动并安装完成后，使用任何浏览器访问 → [http://192.168.88.1:9090](http://192.168.88.1:9090)（其中 IP 地址是 DNAT 规则中使用的地址）：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-01.webp)

默认凭据为（用户名/密码）：

- **系统管理员**：sysadmin@thingsboard.org / sysadmin
- **租户管理员**：tenant@thingsboard.org / tenant

登录提示应确认服务器正在运行。

### MQTT 测试

使用**租户**登录并创建一个新设备。转到“**设备**”菜单，点击“**+**”（添加设备）按钮，然后选择“**添加新设备**”选项：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-02.webp)

随意命名，然后点击“**添加**”：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-03.webp)

点击您刚创建的设备并选择“**管理凭据**”设置，检查您的设备访问令牌（复制生成的访问令牌或输入您自己的 → “YOUR\_TOKEN”）：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-04.webp)

完成这些步骤后，转到 RouterOS 设置（返回 CHR 设置）并创建一个新的 [MQTT broker](../../internet-of-things/mqtt/index.md)（**确保您已安装 IoT 软件包**，否则您将没有此菜单）：

```ros
/iot/mqtt/brokers/add name=tb address=172.18.0.2 port=1883 username=YOUR_TOKEN
```

发布一条 JSON 格式的静态测试 MQTT 消息：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

确认消息已发布：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-05.webp)

## 启用 HTTPS 和 SSL MQTT

默认情况下，使用 HTTP 和 MQTT 协议。如前面“网络”部分所述，使用非 SSL HTTP 和非 SSL MQTT 不太安全（除非在受到严格保护的网络中使用，并配置了良好的防火墙/受限访问），**我们建议启用 HTTPS** 和 **SSL MQTT**。

请查阅 ThingsBoard 文档了解更多信息 → [HTTP over SSL](https://thingsboard.io/docs/user-guide/ssl/http-over-ssl/) 和 [MQTT over SSL](https://thingsboard.io/docs/user-guide/mqtt-over-ssl/) 指南。

首先，没有证书就没有 SSL，需要制作（或购买）一个证书。

简而言之，本节将演示如何为 HTTPS 和 SSL MQTT 生成自签名证书。然后，您需要将它们上传到 ThingsBoard 安装中的正确文件夹，并相应地修改 ThingsBoard 配置文件。

在我们的指南中，我们将使用 RouterOS 生成两个[证书](../../authentication-authorization-accounting/certificates.md)（但您也可以使用 OpenSSL 或您想要的任何其他工具）。

### 创建证书

为 HTTPS 创建证书：

```ros
/certificate/add name=TBhttps common-name=172.18.0.2
/certificate/sign TBhttps
```

为 MQTT 创建证书：

```ros
/certificate/add name=TBmqtt common-name=172.18.0.2
/certificate/sign TBmqtt
```

使用 `/certificate/print` 命令确认它们已添加：

```ros
[admin@MikroTik] > /certificate/print
Flags: K - PRIVATE-KEY; A - AUTHORITY; T - TRUSTED
Columns: NAME, COMMON-NAME, FINGERPRINT
#     NAME     COMMON-NAME  FINGERPRINT                                                     
0 KAT TBhttps  172.18.0.2   863f4547c74ce3ec70c3e82172502711517b52bbc055d18c24ba4aafec46152c
1 KAT TBmqtt   172.18.0.2   ebf3ff5d03ed4cc73546e058da9bc414cdaf24ce45da29b203348045fbbd21ae
```

使用 PKCS12 格式导出证书，并为其设置密码/口令：

```ros
/certificate/export-certificate file-name=keystore export-passphrase=thingsboard_cert_password type=pkcs12 numbers=0
/certificate/export-certificate file-name=mqttserver export-passphrase=thingsboard_mqttcert_password type=pkcs12 numbers=1
```

使用您自己的 `export-passphrase` 并记住它。

上述命令的输出将创建证书文件 **keystore.p12** 和 **mqttserver.p12**，您可以从“[文件列表](../../system-information-and-utilities/files.md)”菜单下载：

```ros
[admin@MikroTik] > /file/print 
Columns: NAME, TYPE, SIZE, CREATION-TIME
 #  NAME                 TYPE             SIZE       CREATION-TIME       
 0  tb/mytb-data         container store             2023-01-19 13:43:16
 1  container-log.0.txt  .txt file        2240.5KiB  2023-01-27 15:37:41
 2  skins                directory                   2023-01-18 15:12:22
 3  tb/mytb-logs         container store             2023-01-27 12:24:30
 4  pull                 directory                   2023-01-19 13:41:01
 5  pub                  directory                   2023-01-18 16:15:29
 6  tb                   directory                   2023-01-23 15:46:39
 7  tb/data              container store             2023-01-18 16:50:08
 8  tb/logs              container store             2023-01-18 16:50:08
 9  mqttserver.p12       .p12 file        2438       2023-01-27 15:36:26
10  keystore.p12         .p12 file        2448       2023-01-27 15:08:07
11  ThingsBoard          container store             2023-01-19 13:40:50
```

将这两个文件从路由器下载到您 PC 上的任意目录。例如，我们已将它们下载到 `C:\Users\Admin\Desktop\ThingsBoard` 文件夹中。

### 下载 ThingsBoard 的配置文件

打开您的命令终端（Windows 用户为“CMD”，以管理员身份运行，Linux 用户为“Linux Shell 或命令终端”），并导航到证书所在的目录：

```powershell
C:\Windows\System32>cd c:\Users\Admin\Desktop\ThingsBoard
C:\Users\Admin\Desktop\ThingsBoard>dir
Directory of C:\Users\Admin\Desktop\ThingsBoard

27.01.2023  15:36    <DIR>          .
27.01.2023  15:36    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
               2 File(s)          4 882 bytes
               2 Dir(s)  51 380 154 368 bytes free
```

在此目录中，您需要通过 SFTP 连接到路由器的 IP（这允许您使用 SSH 协议传输文件，因此您需要确保事先已启用 [SSH 服务](../../system-information-and-utilities/services.md)）：

```powershell
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
The authenticity of host '192.168.88.1 (192.168.88.1)' can't be established.
RSA key fingerprint is SHA256:/WmmZErqWL51SOlS4EaGvSQ0i4HPnSIHCEjnc8AmP2c.
Are you sure you want to continue connecting (yes/no/[fingerprint])?yes
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp>
```

在容器运行时，转到 ThingsBoard 配置文件文件夹（使用 `dir` 或 `ls` 命令查看您所在文件夹的内容，使用 `cd` 命令转到我们选择的文件夹）。默认情况下，它应该是包含“**thingsboard.yml**”配置文件的文件夹。在我们的示例中，我们可以在以下位置找到它：

```powershell
sftp> cd ThingsBoard/usr/share/thingsboard/conf

sftp> dir

banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

使用 `get` 命令下载“**thingsboard.yml**”配置。这会将默认的 ThingsBoard 配置文件下载到您的机器上（到您启动 SFTP 的目录）：

```powershell
sftp> get thingsboard.yml
Fetching /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml to thingsboard.yml
/ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml                               100%   67KB   2.0MB/s   00:00
sftp> quit

c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
```

### 修改 ThingsBoard 的设置

使用您喜欢的文本编辑器（记事本或其他）打开“**thingsboard.yml**”，并修改几行。您可以备份此文件并以不同的名称保存，以保留默认设置的副本，以防配置错误。

#### HTTPS 相关设置

1. 启用 SSL → 将“SSL\_ENABLED:**false**”更改为“SSL\_ENABLED:**true**”。
2. 更改凭据类型 → 从“SSL\_CREDENTIALS\_TYPE:**PEM**”更改为“SSL\_CREDENTIALS\_TYPE:**KEYSTORE**”。
3. 更改路径 → 从“SSL\_KEY\_STORE:**classpath:keystore/keystore.p12**”更改为“SSL\_KEY\_STORE:**keystore.p12**”（可选）。
4. 禁用密钥别名设置 → 注释掉它 → 只需在 `key_alias: "${SSL_KEY_ALIAS:tomcat}"` 行前面加上“**#**”符号。
5. 输入您在 RouterOS 中使用的证书密码 → 从“SSL\_KEY\_STORE\_PASSWORD:**thingsboard**”更改为“SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_cert\_password**”，并从“SSL\_KEY\_PASSWORD:**thingsboard**”更改为“SSL\_KEY\_PASSWORD:**thingsboard\_cert\_password**”。

```js
  ssl:
    # 启用/禁用 SSL 支持
    enabled: "${SSL_ENABLED:true}"
    # 服务器 SSL 凭据
    credentials:
      # 服务器凭据类型（PEM - pem 证书文件；KEYSTORE - java 密钥库）
      type: "${SSL_CREDENTIALS_TYPE:KEYSTORE}"
      # 密钥库服务器凭据
      keystore:
        # 密钥库类型（JKS 或 PKCS12）
        type: "${SSL_KEY_STORE_TYPE:PKCS12}"
        # 保存 SSL 证书的密钥库路径
        store_file: "${SSL_KEY_STORE:keystore.p12}"
        # 用于访问密钥库的密码
        store_password: "${SSL_KEY_STORE_PASSWORD:thingsboard_cert_password}"
        # 密钥别名
        #key_alias: "${SSL_KEY_ALIAS:tomcat}"
        # 用于访问密钥的密码
        key_password: "${SSL_KEY_PASSWORD:thingsboard_cert_password}"
```

#### MQTT 相关设置

1. 启用 SSL → 将“MQTT\_SSL\_ENABLED:**false**”更改为“MQTT\_SSL\_ENABLED:**true**”；
2. 更改凭据类型 → 从“MQTT\_SSL\_CREDENTIALS\_TYPE:**PEM**”更改为“MQTT\_SSL\_CREDENTIALS\_TYPE:**KEYSTORE**”；
3. 更改密钥类型 → 从“MQTT\_SSL\_KEY\_STORE\_TYPE:**JKS**”更改为“MQTT\_SSL\_KEY\_STORE\_TYPE:**PKCS12**”；
4. 更改路径（扩展名） → 从“MQTT\_SSL\_KEY\_STORE:mqttserver**.jks**”更改为“MQTT\_SSL\_KEY\_STORE:mqttserver**.p12**”。
5. 禁用密钥别名设置 → 注释掉它 → 只需在 `key_alias: "${MQTT_SSL_KEY_ALIAS:}"` 行前面加上“**#**”符号；
6. 输入您在 RouterOS 中使用的证书密码 → 从“MQTT\_SSL\_KEY\_STORE\_PASSWORD:**server\_ks\_password**”更改为“MQTT\_SSL\_KEY\_STORE\_PASSWORD:**thingsboard\_mqttcert\_password**”，并从“MQTT\_SSL\_KEY\_PASSWORD:**server\_key\_password**”更改为“MQTT\_SSL\_KEY\_PASSWORD:**thingsboard\_mqttcert\_password**”。

```js
    ssl:
      # 启用/禁用 SSL 支持
      enabled: "${MQTT_SSL_ENABLED:true}"
      # 服务器 SSL 凭据
      credentials:
        # 服务器凭据类型（PEM - pem 证书文件；KEYSTORE - java 密钥库）
        type: "${MQTT_SSL_CREDENTIALS_TYPE:KEYSTORE}"
        # 密钥库服务器凭据
        keystore:
          # 密钥库类型（JKS 或 PKCS12）
          type: "${MQTT_SSL_KEY_STORE_TYPE:PKCS12}"
          # 保存 SSL 证书的密钥库路径
          store_file: "${MQTT_SSL_KEY_STORE:mqttserver.p12}"
          # 用于访问密钥库的密码
          store_password: "${MQTT_SSL_KEY_STORE_PASSWORD:thingsboard_mqttcert_password}"
          # 私钥的可选别名；如果未设置，平台将加载密钥库中的第一个私钥；
          #key_alias: "${MQTT_SSL_KEY_ALIAS:}"
          # 访问私钥的可选密码。如果未设置，平台将尝试加载未受密码保护的私钥；
          key_password: "${MQTT_SSL_KEY_PASSWORD:thingsboard_mqttcert_password}"
```

:::info
将其余设置保留为默认值。除非您知道自己在做什么，否则不要删除/更改上面示例中未显示的行。
:::

将更改应用到“**thingsboard.yml**”文件（编辑后重新保存）。

### 上传修改后的 ThingsBoard 配置文件

剩下要做的就是使用修改后的文件覆盖当前的配置文件，并上传两个证书。

再次确保您的终端指向正确的文件夹（其中包含 3 个文件 → 两个证书和一个修改后的“thingsboard.yml”文件），然后从那里通过 SFTP 进入容器的配置文件目录：

```powershell
c:\Users\Admin\Desktop\ThingsBoard>dir
 Directory of c:\Users\Admin\Desktop\ThingsBoard

30.01.2023  10:59    <DIR>          .
30.01.2023  10:59    <DIR>          ..
27.01.2023  15:09             2 448 keystore.p12
27.01.2023  15:36             2 434 mqttserver.p12
30.01.2023  10:59            68 846 thingsboard.yml
               3 File(s)         73 728 bytes
               2 Dir(s)  50 901 626 880 bytes free
c:\Users\Admin\Desktop\ThingsBoard>sftp admin@192.168.88.1
admin@192.168.88.1's password:
Connected to 192.168.88.1.
sftp> cd ThingsBoard/usr/share/thingsboard/conf
sftp> dir
banner.txt          i18n                logback.xml         templates           thingsboard.conf    thingsboard.yml     
```

使用 `put` 命令上传这些文件：

```powershell
sftp> put thingsboard.yml
Uploading thingsboard.yml to /ThingsBoard/usr/share/thingsboard/conf/thingsboard.yml
thingsboard.yml                                                                       100%   67KB   2.2MB/s   00:00
sftp> put keystore.p12
Uploading keystore.p12 to /ThingsBoard/usr/share/thingsboard/conf/keystore.p12
keystore.p12                                                                          100% 2448     1.2MB/s   00:00
sftp> put mqttserver.p12
Uploading mqttserver.p12 to /ThingsBoard/usr/share/thingsboard/conf/mqttserver.p12
mqttserver.p12                                                                        100% 2434   608.5KB/s   00:00
sftp> dir
banner.txt          i18n                keystore.p12        logback.xml         mqttserver.p12      templates           
thingsboard.conf    thingsboard.yml
```

重启容器：

```ros
[admin@MikroTik] > /container/stop 0
[admin@MikroTik] > /container/start 0
```

在再次启动之前，请确保等待容器停止（使用 `/container/print` 命令后应显示 `status=stopped`）。

### 确认 HTTPS 访问

现在，您应该能够访问 [https://your\_IP:9090](https://192.168.88.1)（其中 IP 地址是 DNAT 规则中使用的地址）：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-06.webp)

:::info
由于我们使用的是非受信任机构颁发的自签名证书，可能会出现指示连接不安全的错误，但您可以通过浏览器查看证书（确认是您的那份），接受风险，然后继续。
:::

### 确认 SSL MQTT 连接

:::info
**不要忘记修改“网络”部分中显示的端口转发规则**，将 **`dst-port`** 和 **`to-ports`** 从 1883（标准非 SSL MQTT 端口）**更改为 8883**（**SSL MQTT 端口**）。
:::

在此示例中，我们将测试[单向 SSL 通信访问令牌场景](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario)。

#### 使用运行容器的设备进行测试

:::info
MQTT 证书应已安装到设备的系统中（因为它是生成该证书的设备）。
:::

添加 MQTT broker：

```ros
/iot/mqtt/brokers/add name=tbssl address=172.18.0.2 port=8883 username=YOUR_TOKEN ssl=yes
```

发布一条 JSON 格式的静态测试 MQTT 消息：

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

确认 MQTT broker 已收到：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-thingsboard-mqtt-http-server-07.webp)

#### 使用另一台设备进行测试

当您有两台 RouterOS 设备，一台运行容器（在我们的示例中，是生成证书的同一台设备），另一台您希望从中测试 MQTT 连接（假设是 [LTAP](https://mikrotik.com/product/ltap) 或任何其他安装了 IoT 软件包的 RouterOS 设备）→ 您需要将证书导入到第二台设备。

将导出的证书（**mqttserver.p12**）拖放到设备的“文件列表”中：

```ros
[admin@LTAP] > /file/print
Columns: NAME, TYPE, SIZE, CREATION-TIME
#  NAME            TYPE       SIZE  CREATION-TIME       
0  mqttserver.p12  .p12 file  2438  2023-01-30 13:28:11
1  flash           disk             2021-07-06 14:51:53
2  flash/pub       directory        2021-07-06 14:51:53
3  flash/skins     directory        1970-01-01 02:00:07
[admin@LTAP] > 
```

导入证书：

```ros
[admin@LTAP] > /certificate/import file-name=mqttserver.p12 passphrase=thingsboard_mqttcert_password
```

添加 MQTT broker，其中地址是 ThingsBoard 容器路由器上 TCP 8883 端口转发规则中使用的 IP 地址 `dst-address`：

```ros
/iot/mqtt/brokers/add name=tbssl address=192.168.88.1 port=8883 username=YOUR_TOKEN ssl=yes
```

发布一条 JSON 格式的静态测试 MQTT 消息：

```ros
/iot/mqtt/publish broker="tbssl" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

并确认 broker 已收到 → 在 ThingsBoard 上的“最新遥测”部分下查看。