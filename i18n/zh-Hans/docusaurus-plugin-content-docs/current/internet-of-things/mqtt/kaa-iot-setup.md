# Kaa IoT 设置

> 本页介绍 MikroTik RouterOS 的 Kaa IoT 设置，涵盖 MQTT 和 HTTP 协议支持、通过脚本进行系统资源监控，以及 Kaa IoT 门户配置步骤，包括应用程序/设备创建和端点令牌管理。同时概述 RouterOS 的先决条件，如互联网访问，以及可选的 iot 软件包安装（用于 MQTT 使用）。

# Kaa IoT 设置

[MQTT](./index.md) 和 [HTTP](../../system-information-and-utilities/fetch.md) 是用于传输各种数据的最流行协议之一。这两种协议在不同的 IoT 设置中被广泛使用，并且都受到 [RouterOS](../../getting-started/software-specifications/index.md) 的支持。

你可能会问，传输什么样的数据？几乎任何数据…… RouterOS [脚本](../../developer-guides/scripting/index.md) 是一个非常强大的工具，借助 [调度器](../../system-information-and-utilities/scheduler.md)，它可以帮助你自动化设备操作。

例如，你可以使用命令 `/system/resource/print` 检查系统的资源信息：

```ros
/system/resource/print
                   uptime: 4d1h37m55s
                  version: 7.14.3 (stable)
               build-time: 2024-04-17 12:47:58
         factory-software: 6.45.9
              free-memory: 926.0MiB
             total-memory: 1024.0MiB
                      cpu: ARM
                cpu-count: 4
            cpu-frequency: 533MHz
                 cpu-load: 0%
           free-hdd-space: 88.5MiB
          total-hdd-space: 128.0MiB
  write-sect-since-reboot: 1107
         write-sect-total: 1447413
               bad-blocks: 0%
        architecture-name: arm
               board-name: RB1100AHx4
                 platform: MikroTik
```

此命令显示有用的信息，如 CPU 使用率、RAM 内存使用量、设备运行时间和固件版本。另一个命令将打印 [GPS](../../mobile-networking/gps/index.md) 坐标（如果设备内置 GPS 芯片）等等……

这本质上意味着，任何可以“打印”到 RouterOS [终端](../../management-tools/console.md) 的内容，都可以通过脚本结构化处理为 JSON 格式消息，并按配置的时间间隔发送出去。我们将在本指南后面展示更详细的示例。

换句话说，你可以将 MikroTik 的数据发送到你选择的任何 MQTT 或 HTTP 服务器。[Kaa IoT](https://www.kaaiot.com/) 就是这样一个服务器。

[为什么选择 Kaa IoT？](https://www.kaaiot.com/advantages/platform)

## Kaa IoT 配置

请务必查看 [KAA：连接你的第一个设备](https://www.kaaiot.com/docs/tutorials/getting-started/connecting-your-first-device)。

登录门户后，按照 [playbook](https://www.kaaiot.com/docs/tutorials/getting-started/connecting-your-first-device) 中的步骤开始操作：

a) 在“**Home>Device management>Applications**”下，点击“**Add application**”按钮创建应用程序，为其命名，然后“**Create**”：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/kaa-iot-setup-01.webp)

b) 在“**Home>Device management>Devices**”下，点击“**Add device**”按钮创建设备，为其命名，然后“**Create**”：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/kaa-iot-setup-02.webp)

输入你自己的“Endpoint token”或让系统自动生成一个。务必“保存”它（因为之后你将无法再次访问）。

剩下的就是将路由器连接到服务器，使用 MQTT 或 HTTP 发布一些数据，并自定义你的第一个仪表板以便更直观地可视化数据。

## RouterOS 配置

首先，设备应具有互联网访问权限。请查看我们的 [首次配置](../../getting-started/first-time-configuration.md) 指南。

互联网连接正常后，如果你计划使用 [MQTT](./index.md) 协议，请确保已安装 **iot** 软件包。你可以从我们的 [下载页面](https://mikrotik.com/download) 的“Extra packages”文件中下载（针对你设备的相应架构）。解压“Extra packages”文件并将 **iot** 软件包上传到“[Files](../../system-information-and-utilities/files.md)”（之后重启设备）。如果你只打算使用 [HTTP 发布](../../system-information-and-utilities/fetch.md)，则无需安装 iot 软件包。

在继续之前，请访问 Kaa IoT [MQTT](https://www.kaaiot.com/docs/device-connectivity/mqtt-device-api) 和 [HTTP](https://www.kaaiot.com/docs/device-connectivity/http-device-api) 设备 API 指南。

### 使用 HTTP 发布数据

要发布基本的 JSON 消息：

```bash
{"test":"data"}
```

只需运行命令：

```ros
/tool/fetch url="https://next.kaaiot.com/kpc/kp1/<app-version>/epmx/<token>/update/keys" http-method=post  http-header-field="Content-Type: application/json" http-data="{\"test\":\"data\"}" output=user mode=https
```

其中，你需要将 `<app-version>`（可在“**Home>Device management>Devices>Specific device**”标签页下查看）和 `<token>`（在平台上创建设备后生成的令牌）替换为你自己的值。

你应该能够在“**Home>Device management>Devices>Specific device>Overview**”标签页下看到新的“Metadata”值出现，或者在“**Home>Device management>Devices>Specific device>Data logs**”标签页下查看日志。

要收集 `/system/resource/print` 信息并发布，我们可以使用脚本。将下面脚本的内容复制并粘贴到命令行中：

```ros
/system/script
add dont-require-permissions=no name=systeminfo owner=admin policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#####################\
    ############### System ###################################\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load];\r\
    \n:local freeMemory [/system/resource/get free-memory];\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory);\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n[/system/package/find where name ~ \"^routeros\"]];\r\
    \n:local model [/system/routerboard/get value-name=model];\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number];\r\
    \n:local upTime [/system/resource/get uptime];\r\
    \n\r\
    \n#################################### message #####################################\r\
    \n:local message \\\r\
    \n\"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\\\"cpu\\\":\\\"\$cpuLoad\\\",\\\r\
    \n\\\"umem\\\":\\\"\$usedMemory\\\",\\\r\
    \n\\\"fmem\\\":\\\"\$freeMemory\\\",\\\r\
    \n\\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message...\")\r\
    \n/tool/fetch url=\"https://next.kaaiot.com/kpc/kp1/<app-version>/epmx/<token>/up\
    date/keys\" http-method=post  http-header-field=\"Content-Type: application/json\" http-data=\
    \"\$message\" output=user mode=https\r\
    \n:put (\"[*] Done\")"
```

修改 URL 中的 `<app-version>` 和 `<token>` 值。然后，使用以下命令运行脚本：

```ros
/system/script/run systeminfo
```

JSON 消息将如下所示：

```bash
{
  "model": "RB924iR-2nD-BT5&BG77",
  "sn": "XXXXXXX",
  "ros": "7.99",
  "cpu": "7",
  "umem": "45113344",
  "fmem": "21995520",
  "uptime": "4d22:16:08"
}
```

### 使用 MQTT 发布数据

要使用单向 SSL MQTT 场景，请从“**Home>Device management>Credentials**”中点击“**Get root certificate**”按钮获取根证书。更多信息请参见 [此处](https://www.kaaiot.com/docs/tutorials/getting-started/authenticating-client-with-tls-certificate)。

将 ca.pem 证书文件上传到 RouterOS 并使用以下命令导入：

```ros
/certificate/import file-name=ca.pem passphrase=""
```

添加新的 MQTT broker：

```ros
/iot/mqtt/brokers
add address=mqtt.next.kaaiot.com name=kaaiot port=8883 ssl=yes
```

连接到 broker 并使用“print”命令检查连接是否正常（应显示“**connected=yes**”）：

```ros
/iot/mqtt/connect broker=kaaiot

/iot/mqtt/brokers/print
0 name="kaaiot" address="mqtt.next.kaaiot.com" port=8883 ssl=yes auto-connect=no keep-alive=60 parallel-scripts-limit=off connected=yes

```

要发布基本的 JSON 消息：

```bash
{"test":"data"}
```

只需运行命令：

```ros
/iot/mqtt/publish broker=kaaiot message="{\"test\":\"data\"}" topic="kp1/<app-version>/epmx/<token>/update/keys/88"
```

其中，你需要将 `<app-version>`（可在“**Home>Device management>Devices>Specific device**”标签页下查看）和 `<token>`（在平台上创建设备后生成的令牌）替换为你自己的值。

你应该能够在“**Home>Device management>Devices>Specific device>Overview**”标签页下看到新的“Metadata”值出现，或者在“**Home>Device management>Devices>Specific device>Data logs**”标签页下查看日志。

要收集 `/system/resource/print` 信息并发布，我们可以使用脚本。将下面脚本的内容复制并粘贴到命令行中：

```ros
/system/script
add dont-require-permissions=no name=systeminfo owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="#####\
    ############################### System ###################################\r\
    \n:put (\"[*] Gathering system info...\")\r\
    \n:local cpuLoad [/system/resource/get cpu-load];\r\
    \n:local freeMemory [/system/resource/get free-memory];\r\
    \n:local usedMemory ([/system/resource/get total-memory] - \$freeMemory);\r\
    \n:local rosVersion [/system/package/get value-name=version \\\r\
    \n[/system/package/find where name ~ \"^routeros\"]];\r\
    \n:local model [/system/routerboard/get value-name=model];\r\
    \n:local serialNumber [/system/routerboard/get value-name=serial-number];\r\
    \n:local upTime [/system/resource/get uptime];\r\
    \n\r\
    \n#################################### message #####################################\r\
    \n:local message \\\r\
    \n\"{\\\"model\\\":\\\"\$model\\\",\\\r\
    \n\\\"sn\\\":\\\"\$serialNumber\\\",\\\r\
    \n\\\"ros\\\":\\\"\$rosVersion\\\",\\\r\
    \n\\\"cpu\\\":\\\"\$cpuLoad\\\",\\\r\
    \n\\\"umem\\\":\\\"\$usedMemory\\\",\\\r\
    \n\\\"fmem\\\":\\\"\$freeMemory\\\",\\\r\
    \n\\\"uptime\\\":\\\"\$upTime\\\"}\"\r\
    \n\r\
    \n:log info \"\$message\";\r\
    \n:put (\"[*] Total message size: \$[:len \$message] bytes\")\r\
    \n:put (\"[*] Sending message...\")\r\
    \n/iot/mqtt/publish broker=kaaiot message=\$message topic=\"kp1/<app-version>/epmx/<token>/update/keys/88\"\r\
    \n:put (\"[*] Done\")"
```

修改主题中的 `<app-version>` 和 `<token>` 值。然后，使用以下命令运行脚本：

```ros
/system/script/run systeminfo
```

JSON 消息将如下所示：

```bash
{
  "model": "RB924iR-2nD-BT5&BG77",
  "sn": "XXXXXXX",
  "ros": "7.99",
  "cpu": "7",
  "umem": "45113344",
  "fmem": "21995520",
  "uptime": "4d22:16:08"
}
```

## 使用仪表板进行数据可视化

要可视化之前发布的数据，请转到“**Home>Solutions>Your\_Solution>Dashboards>Your\_Dashboard**”并点击“**Add widget**”：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/kaa-iot-setup-03.webp)

选择小部件类型（我们将使用“**Device management**”）和预设小部件（我们将使用“**Endpoint metadata**”）。

“**Edit**”小部件并在“**Data source>Endpoint ID**”下选择你的“Endpoint ID”。从这里，你可以进一步自定义仪表板：

![](https://manual.mikrotik.com/docs/internet-of-things/mqtt/img/kaa-iot-setup-04.webp)

因此，你可以创建自己的脚本来收集对你重要的信息，然后只需应用 [调度器](../../system-information-and-utilities/scheduler.md) 按你选择的时间间隔运行脚本。也许你想从你的 [LTAP](https://mikrotik.com/product/ltap#fndtn-specifications) 收集 GPS 坐标并使用“map”小部件进行可视化？这完全取决于你！