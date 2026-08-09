# LTE/5G

> 本文档介绍 MikroTik RouterOS 中的 LTE 和 5G 配置，涵盖接口设置、APN 配置文件、LTE 设置以及操作模式，包括 RouterOS v7 中的 MBIM 支持。文中包含用于启用 PPP 模拟、管理漫游以及配置 MTU 和 PIN 码等调制解调器参数的 CLI 命令。

# LTE/5G

```ros
Package: system
可选 lte-mipsbe.npk 包仅适用于 SXT 3-7 内置调制解调器。
```

仅支持 Direct-IP 模式类型的网卡。MBIM 支持在 RouterOS v7 版本中可用，且 MBIM 驱动会自动加载。如果调制解调器在 RouterOS v6 中无法被识别，请在寻求 RouterOS v6 支持之前，先在 v7 版本中进行测试。

要通过 PPP 接口而非 LTE 接口进行访问，请使用 `/interface/lte/settings/set mode=serial` CLI 命令将操作模式更改为“serial”，然后重新启动。请注意，使用 PPP 模拟模式可能无法获得与 LTE 接口模拟类型相同的吞吐速度。

:::warning
对于 RouterOS v7，`ignore-direct-modem` 参数已重命名为 `mode`，并移至 `/interface/lte/settings` 菜单。
:::

### LTE 客户端

**子菜单：** `/interface/lte`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **allow-roaming** (*yes \| no*; 默认值：**no**) | 启用数据漫游以连接其他国家的数据提供商。并非所有 LTE 调制解调器都支持此功能。某些不完全支持此功能的调制解调器，在 allow-roaming 设置为 no 时，可以连接到网络但无法建立 IP 数据连接。 |
| **apn-profiles** (*string*; 默认值：**default**) | 此接口使用的 APN 配置文件 |
| **band** (*integer list*; 默认值：**""**) | 通信中使用的 LTE 频段 `LTE 频段和带宽` |
| **nr-band** (*integer list*; 默认值："") | 通信中使用的 5G NR 频段 `5G NR 频段和带宽` |
| **comment** (*string*; 默认值：**""**) | 项目的描述性名称 |
| **disabled** (*yes \| no*; 默认值：**no**) | 接口是否禁用。默认情况下为启用。 |
| **modem-init** (*string*; 默认值：**""**) | 调制解调器初始化字符串（调制解调器启动时执行的 AT 命令） |
| **mtu** (*integer \| auto*; 默认值：**1500**) | 最大传输单元。LTE 接口在不进行数据包分片的情况下能够发送的最大数据包大小。auto - 对于支持该功能的调制解调器（MBIM 调制解调器），使用网络通告的 MTU。其他调制解调器将回退到默认值 (1500)。 |
| **name** (*string*; 默认值：**""**) | 接口的描述性名称。 |
| **network-mode** (*3g \| gsm \| lte \| 5g*) | 选择/强制 LTE 接口运行的 RAT 模式。要使 5G NSA 工作，必须同时选择 lte 和 5g 网络模式！仅选择 5g 将只允许连接到 5G SA。 |
| **operator** (*integer*; 默认值：**""**) | 用于将设备锁定到特定运营商。锁定使用完整的 PLMN 号码，由 MCC+MNC 组成。 [PLMN 代码](https://en.wikipedia.org/wiki/Public_land_mobile_network) |
| **pin** (*integer*; 默认值：**""**) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SIM 卡的 PIN 码。 |
| **sms-protocol** (*at \| auto \| mbim*) | 短信功能。 **mbim**：使用 MBIM 驱动。 **at**：使用 AT 命令。 **auto**：根据调制解调器选择适当的选项。 |

#### APN 配置文件

所有与网络相关的设置都在配置文件中

**子菜单：** `/interface/lte/apn`

| 属性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*) | 是否添加默认路由以将所有流量转发到 LTE 接口。 |
| **apn** (*string*) | 服务提供商的接入点名称 |
| **authentication** (*pap \| chap \| none*; 默认值：**none**) | 用于认证的允许协议 |
| **default-route-distance** (*integer*; 默认值：**2**) | 如果同时选择了 add-default-route，则设置应用于自动创建的默认路由的距离值。LTE 路由默认距离为 2，以优先于有线路由使用 LTE |
| **ip-type** (*auto \| ipv4 \| ipv4-ipv6 \| ipv6*; 默认值：auto ) | 请求的 PDN 类型 |
| **ipv6-interface** (; 默认值： ) | 用于通告 IPv6 前缀的接口 |
| **name** (*string*; 默认值： ) | APN 配置文件名称 |
| **number** (*integer*; 默认值： ) | APN 配置文件编号 |
| **passthrough-interface** (; 默认值： ) | 用于透传 IP 配置的接口（激活透传） |
| **passthrough-mac** (*MAC*; 默认值：**auto**) | 如果设置为 auto，则将从第一个数据包学习 MAC 地址 |
| **passthrough-subnet-selection** (*auto / p2p*; 默认值：**auto**) | “auto” 为透传接口选择尽可能小的子网。“p2p” 将透传接口子网设置为 /32，并从 10.177.0.0/16 范围内选取网关地址。网关地址在 apn 配置更改前保持不变。 |
| **password** (*string*; 默认值： ) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 如果任何认证协议处于活动状态，则使用的密码 |
| **use-network-apn** (*yes \| no*; 默认值：**yes**) | 该参数从 RouterOS v7 开始可用，仅用于 MBIM 调制解调器。如果设置为 yes，则使用网络提供的 APN。 |
| **use-peer-dns** (*yes \| no*; 默认值：**yes**) | 如果设置为 yes，则使用从 LTE 接口接收的 DNS |
| **user** (*string*) | 如果任何认证协议处于活动状态，则使用的用户名 |

#### LTE 设置

LTE 和路由器特定的 LTE 设置。该菜单从 RouterOS v7 开始可用。

**子菜单：** `/interface/lte/settings`

| 属性 | 描述 |
| :-- | :-- |
| **mode** (*auto \| mbim \| serial* / *user*; *默认值：**auto***) | 操作模式设置。auto - 自动选择操作模式。serial - 仅提供串行端口。mbim - 如果可能，将调制解调器切换到 MBIM 模式。user - 操作系统不会尝试自动切换调制解调器模式。（从 RouterOS 7.16 开始可用） |
| **firmware-path** (*string*) | 主机操作系统中的固件路径。 [Modem gobi 固件](lte-5g.md#modem-fotadfota-downloads) |
| **external-antenna** (*auto \| both \| div \| main \| none*; 默认值：**auto**) | 此设置仅适用于“Chateau”路由器，Chateau 5G 版本除外。auto - 测量内部和外部天线上的信号电平，并选择信号最佳（RSRP）的天线。both - 两个天线都设置为外部。div - 分集天线设置为外部。main - 主天线设置为外部。none - 未选择外部天线（使用内部天线） |
| **external-antenna-selected** () | 此设置仅适用于“Chateau”路由器，Chateau 5G 版本除外。当“**external-antenna**”设置为“auto”时，显示当前选择的天线 |
| **sim-slot** () | 此设置适用于具有可切换 SIM 卡槽的路由器（LtAP、SXT）。选择选项因产品而异。 |
| **esim-channel** (*auto \| at;* 默认值：*auto*) | 用于 eSIM 管理的控制通道 |
| **link-recovery-timer** (*integer* 默认值：*120* 范围：*120..4294967295*) | 如果 LTE 接口未进入 (R) 运行状态，则在此时间（秒）后重新配置该接口 |

#### LTE eSIM

```ros
RouterOS 版本：7.18+
```

[MikroTips: 如何首次激活您的 eSIM！](https://www.youtube.com/watch?v=v0WtU1xBB-Q)

此菜单包含与 eSIM（[嵌入式用户身份识别模块](http://en.wikipedia.org/wiki/ESIM)）配置和管理相关的命令，使用 RouterOS 内置的 LPA（eSIM [本地配置文件助手](http://en.wikipedia.org/wiki/Remote_SIM_provisioning)）。

单个 eSIM 芯片可以存储多个 eSIM 配置文件，最大配置文件数量取决于所使用的 eSIM 芯片。

RouterOS LPA 支持：

- 固件支持 SIM 低层访问命令（AT+CCHO; AT+CCHC; AT+CGLA）的 AT 调制解调器。
- 固件支持 SIM 低层访问服务（UUID\_SERVICE\_MS\_UICC）的 MBIM 调制解调器。

其他要求：

- 以 SIM 卡外形规格（物理 eSIM）插入 RouterBoard SIM 卡槽的 eSIM。
- 调制解调器上存在 eSIM/eUICC（焊接芯片），且调制解调器设置为使用此卡槽。
- 在配置和删除 eSIM 芯片上的 SIM 配置文件期间，能够连接到 eSIM 配置文件提供商 SM-DP+ 配置服务器（对于连接，您可以使用另一个 eSIM 配置文件或另一个 WAN 接口）。
- 仅当活动卡槽为 eSIM 时，才能配置 eSIM。
- 某些设备有多个 SIM 卡槽，要使用 eSIM，您需要使用命令 `/interface/lte/settings/set sim-slot=esim` 切换卡槽。

命令 `/interface/lte/esim/esim-id [find /interface/lte]` 可用于检查调制解调器是否支持 SIM 低层访问命令以及 eSIM 是否存在。

如果使用带有嵌入式 eSIM 芯片的第三方调制解调器，请查阅调制解调器手册，了解选择 eSIM 卡槽所需的 AT 命令（AT!UIMS; AT+QUIMSLOT 等）。

**命令**

| 属性 | 描述 |
| :-- | :-- |
| **deactivate** | 停用（禁用）eSIM 配置文件。 `/interface/lte/esim/deactivate number=0` |
| **activate** | 激活（启用）eSIM 配置文件。 `/interface/lte/esim/activate number=0` |
| **delete** | 从 eSIM 卡中永久删除 eSIM 配置文件。 `/interface/lte/esim/delete number=0` |
| **print** | 列出 eSIM 上安装的 eSIM 配置文件 `/interface/lte/esim/print` |
| **provision** | 配置新的 eSIM 配置文件。该命令接受四个参数：interface - 将为其启用 eSIM 配置文件的接口。matching-id - 激活码令牌。示例： matching-id=ABCD10EFGHI5KL6Msm-dp-plus - SM-DP+ 服务器主机名。confirmation-code - 确认码（某些情况下需要的一次性密码）。activate - 配置后激活新创建的配置文件（yes\|no；默认值：yes）[从 7.20beta6 版本开始可用。在 7.20beta6 之前，配置文件在配置后默认不激活。] 从 QR 码解码的 eSIM LPA 字符串示例：**LPA:1$server.example.io$ABCD10EFGHI5KL6M** `/interface/lte/esim/provision interface=lte1 sm-dp-plus=server.example.io matching-id=ABCD10EFGHI5KL6M` |
| **esim-id** | 查询 eSIM ID。该命令接受一个参数：interface - 选择要查询 eSIM ID 的接口。`/interface/lte/esim/esim-id interface=lte1   eid: 8903302342630000000004181FFFFFFF` |
| **set-nickname** | 为 eSIM 配置文件设置昵称。 `/interface/lte/esim/set-nickname number=0 nickname=nickname1` |
| **refresh-profile-list** | 重新查询 eSIM 配置文件列表。该命令接受一个参数：interface - 选择将重新查询 eSIM 配置文件的接口。 |

##### 带有内置 eSIM 芯片的设备（MikroTik Connectivity）

:::info
这些设备预装了 MikroTik Connectivity eSIM 配置文件。
https://mikrotik.com/connectivity
:::

| 设备型号 | 调制解调器 |
| :-- | :-- |
| S53UG+5HaxD2HaxD-TC&RG650E-EU | RG650E-EU |
| ATLGM&RG520F-EU | RG520F-EU |
| EC25-EU&KNe | EC25-EU |

##### 调制解调器 eSIM 管理支持表

:::note
\* 这些调制解调器没有内置 eSIM。它们需要外部 eSIM 芯片。例如，物理 eSIM 卡（标准 SIM 卡外形规格的 eSIM）。
:::

| 调制解调器 | 支持 | 备注 |
| :-- | :-- | :-- |
| EC200A-EU | 是\* |  |
| EG06-A | 是\* |  |
| EG18-EA | 是\* |  |
| EG12-EA | 是\* |  |
| EG120K-EA | 是\* |  |
| RG520F-EU | 是\* |  |
| EP06-A | 是\* |  |
| RG502Q-EA | 是\* |  |
| FG621-EA | 是\* | 无法管理空的 eSIM（无配置文件） |
| R11e-LTE6 | 是\* | 从固件版本 R11e-LTE6\_V039 开始 |
| R11e-LTE-US | 否 |  |
| R11e-4G | 否 |  |
| R11e-LTE | 否 |  |

#### 扫描器

可以使用 `/interface/lte/scan` 命令扫描 LTE 接口。示例：

```ros
[admin@MikroTik] > /interface/lte/scan duration=60 number=0
Columns: OPERATOR, MCC-MNC, RSSI, RSRP, RSRQ
OPERATOR  MCC-MNC  RSSI    RSRP    RSRQ
LMT         24701  -36dBm  -63dBm  -7dB
```

可用属性：

| 属性 | 描述 |
| :-- | :-- |
| **duration** (*integer*) | 扫描持续时间（秒） |
| **freeze-frame-interval** (*integer*) | 数据打印输出之间的时间 |
| **number** (*integer*) | 接口编号或名称 |

#### 监控 LTE 详细信息

您可以使用 CLI 命令监控 LTE 接口参数：`/interface/lte/monitor`。它返回小区级数据（例如，运营商、小区 ID、信号信息）和调制解调器元数据（固件、型号、SIM 标识符）。

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

#### LTE 接口能力

您可以使用 `/interface/lte/show-capabilities` CLI 命令检查 LTE 接口的能力。

##### 示例输出

```
[admin@MikroTik] > interface/lte/show-capabilities lte1
  modem-bus-location: 2-1
           cell-scan: yes
        network-scan: yes
     roaming-barring: yes
  apn-address-family: IPv4,IPv6
       max-apn-count: 8
           rat-modes: 3g,lte,5g
      band-selection: yes
           lte-bands: 1,3,5,7,8,20,28,32,38,40,41,42,43
            nr-bands: 1,3,5,7,8,20,28,38,40,41,75,76,77,78
         passthrough: yes
     firmware-update: yes
   lte-attach-config: yes
             at-chat: yes
    framed-route-apn: any
```

| 能力 | 描述 |
|------------|-------------|
| **modem-bus-location** | LTE 调制解调器连接的物理 USB 总线 |
| **cell-scan** | 支持 `interface/lte/cell-monitor` 命令 |
| **network-scan** | 支持 `interface/lte/scan` 命令 |
| **roaming-barring** | 支持漫游限制 |
| **apn-address-family** | 支持的 IP 协议族（IPv4、IPv6） |
| **max-apn-count** | 可同时激活的最大 APN 配置文件数量 |
| **rat-modes** | 支持的无线接入技术（GSM、3G、LTE、5G） |
| **band-selection** | 支持 LTE/5G 频段设置命令 |
| **lte-bands** | 调制解调器支持的 LTE 频段列表 |
| **nr-bands** | 调制解调器支持的 5G 频段列表 |
| **passthrough** | 支持 LTE 透传 |
| **firmware-update** | 支持 `interface/lte/firmware-upgrade` |
| **lte-attach-config** | 支持 LTE attach apn 配置（设置与配置相同的 APN） |
| **at-chat** | 支持 `interface/lte/at-chat` |
| **framed-route-apn** | 在多 APN 设置中，哪个 APN 支持帧路由（路由转发） |

#### 调制解调器固件升级命令

该命令允许检查并在有可用更新时升级受支持的 MikroTik 调制解调器的固件。

要进行固件更新可用性检查和安装，需要有效的互联网连接，根据调制解调器的不同，互联网连接可以通过任何 RouterOS 接口或调制解调器接口（FOTA）提供，请参阅下表了解每个调制解调器支持的连接方式。

| 参数 / 属性 | 描述 |
| :-- | :-- |
| **upgrade** (*yes \| no; 默认值：**no***) | 设置命令执行模式：no - 显示当前调制解调器固件版本并显示最新的可用固件版本。yes - 执行固件安装。 |
| **update-channel** (*stable \| testing*; 默认值：**stable**) | 设置使用的固件更新通道：stable - 用于一般用途的固件版本。testing - 早期访问/测试通道，调制解调器固件在稳定通道发布之前在此发布。该功能从 v7.17beta2 开始可用。 |
| **firmware-file** (*string*; 默认值："") | 允许用户覆盖固件更新源，并从自定义位置（文件、URL）执行升级，适用于通过互联网连接到 MikroTik 升级服务器不可行的环境，例如专用网络等。 |

:::warning
在尝试进行 LTE 调制解调器固件升级之前 - 请将 RouterOS 版本升级到最新版本 [如何升级 RouterOS](../getting-started/installation-and-upgrade/upgrade.md)
:::

##### 支持固件更新且需要连接的调制解调器

使用命令 ***`/interface/lte/monitor [find]` 一次*** 获取返回的属性“model”以识别已安装的调制解调器型号。

| 调制解调器 | 连接到 MikroTik 升级服务器所需的方式 |
| :-- | :-- |
| **EC200A-EU** R11eL-EC200A-EU | 使用调制解调器 LTE 接口 使用任何 RouterOS 接口 (7.18beta1+) |
| **EG06-A** | 使用任何 RouterOS 接口 |
| **EP06-A** | 使用任何 RouterOS 接口 |
| **EG12-EA** | 使用任何 RouterOS 接口 |
| **EG18-EA** | 使用任何 RouterOS 接口 |
| **FG621-EA** R11eL-FG621-EA | 使用任何 RouterOS 接口 |
| **R11-LTE** | 使用调制解调器 LTE 接口 |
| **R11e-4G** | 使用任何 RouterOS 接口 |
| **R11e-LTE6** | 使用任何 RouterOS 接口 |
| **RG502Q-EA** | 使用任何 RouterOS 接口 |
| **RG520F-EU** | 使用任何 RouterOS 接口 |

##### 调制解调器固件升级命令示例

检查是否有新的固件更新可用

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1
  installed: EG12EAPAR01A13M4G_02.001.02.001
     latest: EG12EAPAR01A15M4G_01.201.01.201
```

在早期访问/测试通道中检查是否有新的固件更新可用

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 update-channel=testing
  installed: EG12EAPAR01A15M4G_01.201.01.201
     latest: EG12EAPAR01A15M4G_01.203.01.203
```

安装最新固件

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes
```

从早期访问/测试通道安装最新固件

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 upgrade=yes update-channel=testing
```

从自定义位置（文件或 HTTP URL）执行固件升级。
在执行 `firmware-upgrade` 命令之前，接口必须处于 R (运行) 或 X (禁用) 状态。

```ros
[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=R11e-LTE6_V039_image upgrade=yes

[admin@D53G] > /interface/lte/firmware-upgrade lte1 firmware-file=http://firmwareserver.com/R11e-LTE6_V039_image upgrade=yes
```

##### 调制解调器 FOTA/DFOTA 下载

以下是我们调制解调器的所有最新固件版本：
https://box.mikrotik.com/d/bfa49081454e4da1972d/

您可以使用这些 FOTA 文件进行离线更新，或在 MikroTik 升级服务器无法访问标准调制解调器固件升级的环境中更新。

:::warning
在尝试进行 LTE 调制解调器固件升级之前，请将 RouterOS 升级到最新版本。 [如何升级 RouterOS](../getting-started/installation-and-upgrade/upgrade)

LTE 调制解调器设计为在可能的情况下拒绝不兼容的 FOTA/DFOTA 固件包。但是，手动固件升级始终存在风险。安装不正确的固件映像可能导致调制解调器故障、功能丢失或需要更换调制解调器的永久性损坏。

不要中断升级过程。在写入固件时，断电、设备重启、调制解调器重置或任何其他中断都可能使调制解调器处于无法恢复的状态。

用户有责任验证固件文件是否适用于正在升级的确切调制解调器型号和硬件版本，并确保在整个升级过程中电源稳定。MikroTik 不对因刷入不正确的固件文件或固件升级过程中断而导致的任何损坏、功能丢失或其他问题承担责任。
:::

###### FOTA 调制解调器

FOTA（空中固件升级）。这些调制解调器没有源版本子文件夹。您可以从任何当前固件版本安装最新的调制解调器固件。

| 调制解调器型号 | 备注 |
|---|---|
| R11e-LTE | 调制解调器通过其 LTE 连接自行下载固件（FOTA）。无法进行离线升级，您可以将固件托管在调制解调器可以访问的某个 http 服务器上，如果您的设置中无法访问 MikroTik 升级服务器，则可以这样升级固件 |
| R11e-LTE6 | - |
| R11l-LTE7 | - |
| R11e-4G | - |
| EC25-EU | 调制解调器固件作为 NPK 包安装 |
| EG25-G | 调制解调器固件作为 NPK 包安装 |
| SXT-LTE | 仅单一产品 - RBSXTLTE3-7。调制解调器固件作为 NPK 包安装 |

###### DFOTA 调制解调器

DFOTA（增量空中固件升级）。这些调制解调器具有按版本划分的子文件夹 `modem/<model>/<currentVersion>/<targetVersion>_image`，其中 targetVersion 是您当前固件版本可用的最新升级。如果您的当前固件版本较旧，则可能需要进行多步升级。

| 调制解调器型号 | 备注 |
|---|---|
| EC200A-EU | 支持使用最新的 RouterOS v7 版本进行离线 DFOTA 升级。在较旧版本中，调制解调器通过其 LTE 连接自行下载固件 |
| EP06-A | - |
| EG06-A | - |
| EG12-EA | - |
| EG18-EA | - |
| EG120K-EA | - |
| RG502Q-EA | - |
| RG520F-EU | - |
| RG520F-EUX | 适用于 ATL 5G R16 (ATLGM&RG520F-EU) 的特殊调制解调器固件版本 |
| RG650E-EU | 此调制解调器使用 A/B 系统更新机制而不是 DFOTA。由于完整的固件映像写入非活动系统分区，固件包明显大于典型的 DFOTA 包 |
| FG621-EA | - |
| BG77 | PPP 串行调制解调器。 `/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |
| BG770A | PPP 串行调制解调器。 `/interface/ppp-client/firmware-upgrade ppp-out1 upgrade=yes firmware-file=` |

#### 用户 at-chat 命令

可以使用 `/interface/lte/at-chat` 命令向 LTE 接口发送用户定义的“at-chat”命令。

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="AT"
  output: OK
```

也可以将命令与“wait”参数 *wait=yes* 一起使用，使“at-chat”等待 5 秒并返回所有输出，而不是仅返回第一个接收到的数据。这对于某些返回多行输出或大量数据块的命令很有用。

```ros
[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?"
  output:

[admin@MikroTik] > /interface/lte/at-chat lte1 input="at+qcfg=?" wait=yes
  output: +QCFG: "rrc",(0-5)
          +QCFG: "hsdpacat",(6,8,10-24)
          +QCFG: "hsupacat",(5,6)
          +QCFG: "pdp/duplicatechk",(0,1)
          +QCFG: "risignaltype",("respective","physical")
          +QCFG: "lte/bandprior",(1-43),(1-43),(1-43)
          +QCFG: "volte_disable",(0,1)
          +QCFG: "diversity/config",(4,6),(1-4),(0)
          +QCFG: "div_test_mode",(0,1)
          +QCFG: "usbspeed",("20","30")
          +QCFG: "data_interface",(0,1),(0,1)
          +QCFG: "pcie/mode",(0,1)
          +QCFG: "pcie_mbim",(0,1)
          +QCFG: "sms_control",(0,1),(0,1)
          +QCFG: "call_control",(0,1),(0,1)
          +QCFG: "usb/maxpower",(0-900)
          +QCFG: "efratctl",(0,1)
          +QCFG: "netmaskset",(0,1)[,<netmask>]
          +QCFG: "mmwave",ant_chip,ant_type
          +QCFG: "gatewayset",(0,1)[,<gateway>]
          +QCFG: "clat",(0,1),(0,1),<prefix>,(0,32,40,48,56,64,96),<fqdn>,(0,1),(0,1,2,4,8),(0,1),(0,1),(0,1,2),(0,1,2)
          +QCFG: "usage/apmem"
          +QCFG: "enable_gea1"[,(0,1)]
          +QCFG: "dhcppktfltr",(0,1)
          OK
```

您还可以在脚本中使用“at-chat”函数，并将命令输出分配给变量。

```ros
[admin@MikroTik] > :global "lte_command" [/interface/lte/at-chat lte1 input="AT+CEREG?" as-value ]
[admin@MikroTik] > :put $"lte_command"
output=+CEREG: 0,1
OK
```

### 快速设置示例

从网络设置开始 - 在 LTE apn 配置文件下添加新的连接参数（由网络提供商提供）：

```ros
/interface/lte/apn/add name=profile1 apn=phoneprovider.net authentication=chap password=web user=web
```

为 LTE 连接选择新创建的配置文件：

```ros
/interface/lte/set [find] apn-profiles=profile1
```

LTE 接口应显示运行 (R) 标志：

```ros
[admin@MikroTik] > /interface/lte/print
Flags: X - disabled, R - running
0 R name="lte1" mtu=1500 mac-address=AA:AA:AA:AA:AA:AA
```

如果需要，为 LTE 接口添加 NAT Masquerade 以将互联网提供给本地网络：

```ros
/ip/firewall/nat/add action=masquerade chain=srcnat out-interface=lte1
```

添加接口后，您可以使用“info”命令查看客户端获取了哪些参数（返回的参数取决于 LTE 硬件设备）：

```
[admin@MikroTik] > /interface/lte/monitor lte1
            status: connected
             model: EG18-EA
          revision: EG18EAPAR01A12M4G
  current-operator: LMT
    current-cellid: 3103242
            enb-id: 12122
         sector-id: 10
        phy-cellid: 480
        data-class: LTE
    session-uptime: 15m54s
              imei: 86981604098XXXX
              imsi: 24701060267XXXX
              iccid: 8937101122102057XXXX
      primary-band: B3@20Mhz earfcn: 1300 phy-cellid: 480
     dl-modulation: qpsk
               cqi: 7
                ri: 2
               mcs: 1
              rssi: -68dBm
              rsrp: -97dBm
              rsrq: -9dB
              sinr: 6dB
```

### 透传示例

某些 LTE 接口支持 LTE 透传功能，其中 IP 配置直接应用于客户端设备。在这种情况下，调制解调器固件负责 IP 配置，路由器仅用于配置调制解调器设置 - APN、网络技术和 IP 类型。在此配置中，路由器不会从调制解调器获取 IP 配置。如果调制解调器支持，LTE 透传调制解调器可以同时传递 IPv4 和 IPv6 地址。某些调制解调器支持多个 APN，您可以将来自每个 APN 的流量传递到特定的路由器接口。

透传仅适用于一台主机。路由器将自动检测第一个接收到的数据包的 MAC 地址，并将其用于透传。如果网络上有多个主机，则可以将透传锁定到特定的 MAC。在透传提供 IP 的网络主机上，该接口上也应启用 DHCP 客户端。请注意，将无法通过公共 LTE IP 地址连接到 LTE 路由器，也无法从用于透传的主机连接。建议从 LTE 路由器到主机创建额外的连接以进行配置。例如，LTE 路由器和主机之间的 vlan 接口。

要启用透传，需要在 `/interface/lte/apn` 菜单中新建条目或更改默认条目

:::warning
并非所有芯片组都支持透传。
要检查您的调制解调器是否支持透传：

```ros
/interface/lte/show-capabilities [find]
```

:::

#### 示例

在 ether1 上配置透传：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1
```

在 ether1 主机 00:0C:42:03:06:AB 上配置透传：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1 passthrough-mac=00:0C:42:03:06:AB
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1
```

在 ether1 和 ether2 上配置多个 APN：

```ros
[admin@MikroTik] > /interface/lte/apn/add apn=apn1 passthrough-interface=ether1
[admin@MikroTik] > /interface/lte/apn/add apn=apn2 passthrough-interface=ether2
[admin@MikroTik] > /interface/lte/set lte1 apn-profiles=apn1,apn2
```

为不同接口配置具有相同 APN 的多个 APN：

```ros
[admin@MikroTik] > /interface/lte/apn/add name=interface1 apn=apn1
[admin@MikroTik] > /interface/lte/apn/add name=interface2 ap