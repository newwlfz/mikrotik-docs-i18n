# 使用 MQTT 和 ThingsBoard 进行 GPS 追踪

> 本文档介绍如何在 MikroTik RouterOS 上使用 MQTT 和 ThingsBoard 配置 GPS 追踪，详细说明支持 GPS 的设备向服务器发送位置数据的设置步骤。内容涵盖 broker 配置、设备凭据生成以及 SSL 和非 SSL 环境下的 MQTT 发布命令。

# 使用 MQTT 和 ThingsBoard 进行 GPS 追踪

许多 RouterOS 设备支持 [GPS](./index.md) 功能。这使得 RouterOS 能够确定其 GPS 接收器的精确位置。GPS 坐标将指示当前位置的纬度和经度值（以及其他参数）。

假设您有一台 [LTAP](https://mikrotik.com/product/ltap)（或任何其他支持 GPS 的 RouterOS 设备），并且希望追踪其位置。您希望路由器将此数据发送到服务器，在服务器上数据将被存储并集成到地图中，因为这样更方便监控。在本指南中，我们将演示如何实现这一目标。此场景将利用 MQTT 协议与名为 [ThingsBoard](https://thingsboard.io/) 的平台进行通信。

ThingsBoard 提供云解决方案以及不同的本地安装选项（支持多种操作系统）。

由于我们添加了 [container](../../containers/index.md) 功能，现在也可以在 RouterOS 内运行该平台。这意味着，您可以完全基于 RouterOS 设备构建此场景 → 您希望追踪的具有 GPS 支持的设备（例如，配备 [LTAP](https://mikrotik.com/product/ltap) 的车辆 → 作为 **MQTT 发布者** 的 RouterOS 设备），以及在更强大的 RouterOS 设备（如 [CHR](../../getting-started/routeros-licensing/chr/index.md) 机器 → 作为 **MQTT broker** 的 RouterOS 设备）上运行的 ThingsBoard 服务器。

如果您选择此路线（容器路线），请仔细选择计划用作“服务器”的设备，因为此实现可能对 RAM 使用要求较高（建议使用至少具有 **2 GB RAM** 或 **1 GB RAM** 且 **负载极低** 的设备，并且架构为 **ARM64** 或 **AMD64**）。

## 配置

在本指南中，我们将演示如何配置 GPS 接收器（MQTT 发布者）以及如何设置 ThingsBoard。

如果您希望使用容器功能来运行 ThingsBoard 实例（MQTT broker），请查看 [此处的指南](../../containers/user-guides/container-thingsboard-mqtt-http-server.md)。有关 ThingsBoard 和 MQTT 配置的通用指南，请参阅 [此处的指南](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md)。请务必浏览这两个指南，因为它们包含其他有用的信息。

在继续之前，请确保 ThingsBoard 已启动并运行，并且您可以访问其 Web 管理门户。确认 MQTT 端口已打开和/或已正确进行端口转发。

### ThingsBoard 准备

:::info
本示例将展示 [access-token](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#access-token-scenario-1) 和 [通过 access-token 进行单向 SSL 通信](../../internet-of-things/mqtt/mqtt-and-thingsboard-configuration.md#one-way-ssl-communication-scenario) 场景，为简单起见，但您也可以使用其他可用选项。
:::

导航到“**Devices**”菜单，并通过“**Add new device**”按钮添加新设备 → 为其命名并创建（例如，LTAP）：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-01.webp)

点击您刚刚添加的设备，进入“**Details**”部分，并在“**Manage credentials/Device Credentials**”设置下生成访问令牌：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-02.webp)

### MQTT broker 配置

如果是本地测试或 broker 可通过 VPN 访问，您可以使用非 SSL MQTT：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=1883 username=access_token
```

其中：

- `name` 是您希望为 broker 指定的名称，此名称将在后续脚本中使用。
- `address` 是 broker 的 IP 地址。
- `port` 是 broker 监听的 TCP 端口 → 对于非 SSL，通常为 TCP 1883。
- `username` 由 MQTT broker 决定，在我们的案例中，它是在 ThingsBoard 管理门户中生成的“访问令牌”。

如果是公共访问（当您希望通过其公共 IP 地址访问 broker 时），**我们建议使用 SSL MQTT**：

```ros
/iot/mqtt/brokers/add name=tb address=x.x.x.x port=8883 username=access_token ssl=yes
```

其中：

- `name` 是您希望为 broker 指定的名称，此名称将在后续脚本中使用。
- `address` 是 broker 的 IP 地址。
- `port` 是 broker 监听的 TCP 端口 → 对于 SSL，通常为 TCP 8883。
- `username` 由 MQTT broker 决定，在我们的案例中，它是在 ThingsBoard 管理门户中生成的“访问令牌”。
- `ssl` 启用 SSL MQTT 通信。

### MQTT 发布

您可以使用以下命令测试静态消息的 MQTT 发布：

```ros
/iot/mqtt/publish broker="tb" topic="v1/devices/me/telemetry" message="{\"test\":\"123\"}"
```

要发布 GPS 坐标，请导入以下脚本：

```ros
/system/script/add dont-require-permissions=no name=mqttgps owner=admin policy="ftp,re\
    boot,read,write,policy,test,password,sniff,sensitive,romon" \
    source="    ###配置###\r\
    \n    #在\"\"内输入预配置的 broker 名称：\r\
    \n    :local broker \"tb\"\r\
    \n    #根据 broker 配置，在\"\"内输入主题名称：\r\
    \n    :local topic \"v1/devices/me/telemetry\"\r\
    \n\r\
    \n    ###变量####\r\
    \n    :global lat\r\
    \n    :global lon\r\
    \n    :global alt1\r\
    \n    :global alt2\r\
    \n\r\
    \n    ###GPS####\r\
    \n    :put (\"[*] 正在捕获 GPS 坐标...\")\r\
    \n    /system/gps/monitor once do={\r\
    \n    :set \$lat \$(\"latitude\");\r\
    \n    :set \$lon \$(\"longitude\");\r\
    \n    :set \$alt1 \$(\"altitude\")}\r\
    \n    ###从值中移除\"meters\"，因为 JSON 格式无法识别它###\r\
    \n    :set \$alt2 [:pick \$alt1 0 [find \$alt1 \" m\"]]\r\
    \n\r\
    \n    :local message \\\r\
    \n    \"{\\\"latitude\\\":\$lat,\\\r\
    \n    \\\"longitude\\\":\$lon,\\\r\
    \n    \\\"altitude\\\":\$alt2}\"\r\
    \n\r\
    \n    ###MQTT###\r\
    \n    :if (\$lat != \"none\") do={\\\r\
    \n    :put (\"[*] 正在向 MQTT broker 发送消息...\");\r\
    \n    /iot/mqtt/publish broker=\$broker topic=\$topic message=\$\
    message} else={:put (\"[*] 纬度为 none，不发布任何内容！\
    \");:log info \"纬度为 none，不发布任何内容！\"}"
```

简而言之，该脚本捕获 GPS 信息，特别是纬度、经度和海拔值。然后，它将这些值构造成 JSON 消息。如果在脚本启动时，纬度值不等于“none”（等于任何实际数值）→ 它通过 MQTT 将 JSON 消息发送到名为“**tb**”的 broker。如果无法捕获 GPS 数据 → “latitude” 被识别为“none” → 脚本仅记录无法捕获任何内容，不执行其他操作。

这是一个非常基础的示例。您可以根据需求随意修改脚本，添加自己的“if”条件（例如，如果没有 GPS 信号则发送电子邮件通知）和附加参数（任何其他 RouterOS 捕获的值，例如固件版本）。

使用以下命令运行脚本：

```ros
/system/script/run mqttgps 
[*] 正在捕获 GPS 坐标...
        date-and-time: 2023-02-01 10:39:37
             latitude: 56.969862
            longitude: 24.162425
             altitude: 31.799999 m
                speed: 1.000080 km/h
  destination-bearing: none
         true-bearing: 153.089996 deg. True
     magnetic-bearing: 0.000000 deg. Mag
                valid: yes
           satellites: 6
          fix-quality: 1
  horizontal-dilution: 1.42
             data-age: 0s
[*] 正在向 MQTT broker 发送消息...
```

要自动化此过程，请添加一个 [scheduler](../../system-information-and-utilities/scheduler.md)（例如，每 30 秒运行一次脚本）：

```ros
/system/scheduler/add name=mqttgpsscheduler interval=30s on-event="/system/script/run mqttgps"
```

## 结果验证

转到您创建的设备下的“Latest telemetry”部分，确认数据已发布：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-03.webp)

## 使用地图进行数据可视化

ThingsBoard 允许您使用 [Widgets](https://thingsboard.io/docs/user-guide/ui/widget-library/) 创建视觉上吸引人的仪表板。在我们的案例中，我们希望追踪 LTAP 的 GPS 坐标，因此我们需要一个地图小部件。

选择纬度和经度值，然后点击“**Show on widget**”按钮：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-04.webp)

找到“**Maps**”包，然后点击“**Add to dashboard**”：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-05.webp)

选择现有仪表板或创建新仪表板，并按您的喜好命名：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-06.webp)

通过调度器或手动运行脚本，然后检查结果：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-07.webp)

现在，我们可以将其安装在移动目标上并追踪其位置：

![](https://manual.mikrotik.com/docs/mobile-networking/gps/img/gps-tracking-using-mqtt-and-thingsboard-08.webp)