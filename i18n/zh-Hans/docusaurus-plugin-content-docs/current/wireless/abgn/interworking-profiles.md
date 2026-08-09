# 互联配置文件

> 本页介绍 MikroTik RouterOS 无线网络的互联配置文件，使设备能够通过 IEEE 802.11u 和 Hotspot 2.0 标准交换信息。文中详细说明了网络类型、ANQP 元素和场所信息等配置属性，以增强客户端设备的选择和安全性。

# 互联配置文件

## 互联（Interworking）

互联是指两个或多个事物协同工作的过程。为了获得更好的无线网络体验，接入点（Access Point）与无线客户端设备之间必须交换网络信息。基本的无线信标（Beacon）和探测请求（Probe Request）中所包含的信息是有限的。因此，IEEE 802.11u™-2011（与外部网络互联）标准应运而生，该标准规定了设备之间应如何交换信息。通过互联服务，可以增强网络发现和接入点选择过程。无线客户端设备可以有更多依据来选择要关联的网络。

## Hotspot 2.0

Hotspot 2.0 是由 Wi-Fi 联盟开发和拥有的一项规范。它旨在连接 Wi-Fi 网络时提供更类似于蜂窝网络的体验。为了提高无线网络安全性，Hotspot 2.0 接入点使用强制性的 WPA2 认证。Hotspot 2.0 依赖于互联（Interworking）并添加了一些自身的属性和流程。

互联配置文件根据 IEEE 802.11u 和 Hotspot 2.0 Release 1 规范实现。

:::info
本手册页面描述的是传统 `wireless` 软件包（`/interface/wireless`）的互联配置。对于 `wifi` 软件包（`/interface/wifi`），请参阅 [WiFi6 的互联配置](../wifi/interworking-for-wifi6.md)。
:::

## 配置属性

**子菜单:** `/interface/wireless/interworking-profiles`

### 信标和探测响应中的信息元素

可以通过互联元素（Interworking element）向信标和探测响应数据包中添加一些信息。可以配置互联元素的以下参数：

| 属性 | 描述 |
| :-- | :-- |
| **asra** (*yes \| no*; 默认值: **no**) | 访问需要额外步骤（Additional Steps Required for Access）。如果用户需要采取额外步骤才能访问互联网（例如访问围墙花园），则设置为 `yes`。 |
| **esr** (*yes \| no*; 默认值: **no**) | 紧急服务可达（Emergency Services Reachable）。设置为 `yes` 以表示可以通过该接入点访问紧急服务。 |
| **hessid** (*MAC 地址*; 默认值: ) | 同质扩展服务集标识符（Homogenous Extended Service Set Identifier）。提供对相同外部网络访问的设备属于同一个同质扩展服务集。该服务集可以通过 HESSID 来标识，此集合中所有接入点的 HESSID 相同。HESSID 的 6 字节值以 MAC 地址形式表示。它应该是全局唯一的，因此建议使用服务集中某个接入点的 MAC 地址。 |
| **internet** (*yes \| no*; 默认值: **yes**) | 是否可以通过此连接访问互联网。此信息包含在互联元素中。 |
| **network-type** (*emergency-only \| personal-device \| private \| private-with-guest \| public-chargeable \| public-free \| test \| wildcard*; 默认值: **wildcard**) | 关于网络访问类型的信息。<code>emergency-only</code> - 专用于访问紧急服务且受限的网络；<code>personal-device</code> - 个人设备网络。此类网络的示例是连接到打印机的相机，从而形成一个用于打印照片的网络；<code>private</code> - 供拥有用户账户的用户使用的网络。通常用于企业员工，而非访客；<code>private-with-guest</code> - 与 private 相同，但提供访客账户；<code>public-chargeable</code> - 可供任何愿意付费的人使用的网络。例如，Hotspot 2.0 服务订阅或酒店客房内的互联网接入；<code>public-free</code> - 任何人都可以免费使用的网络。例如，城市市政网络或机场热点；<code>test</code> - 用于测试和实验用途的网络。不用于生产环境；<code>wildcard</code> - 用于无线客户端。发送带有通配符作为网络类型值的探测请求将使所有互联接入点响应，无论其实际的 network-type 设置如何。客户端发送探测请求帧时，会将 network-type 设置为其感兴趣的值。它将只收到具有相同值的接入点的回复（通配符情况除外）。 |
| **uesa** (*yes \| no*; 默认值: **no**) | 非认证紧急服务可访问（Unauthenticated Emergency Service Accessible）。<code>no</code> - 表示通过此接入点无法访问任何非认证紧急服务；<code>yes</code> - 表示通过此接入点可以访问更高层的非认证紧急服务。 |
| **venue** (*venue*; 默认值: **unspecified**) | 指定接入点所在的场所。从可用值中选择。一些示例：`venue=business-bank``venue=mercantile-shopping-mall``venue=educational-university-or-college` |

### ANQP 元素

接入网络查询协议（Access Network Query Protocol）。并非所有必要信息都包含在探测响应和信标帧中。为了让客户端设备在选择关联的接入点之前获取更多信息，使用了 ANQP。接入点可以在多个 ANQP 元素中存储信息。客户端设备将使用 ANQP 仅查询其感兴趣的信息。这减少了关联前所需的时间。

| 属性 | 描述 |
| :-- | :-- |
| **3gpp-raw** (*十六进制八位字节字符串*; 默认值: ) | 蜂窝网络通告信息 - 国家和网络代码。这有助于 Hotspot 2.0 客户端选择接入点以访问 3GPP 网络。有关此字段的格式，请参阅 3GPP TS 24.302（附录 H）。如果被查询，此值将在 ANQP 响应中发送。 |
| **3gpp-info**(*数字/数字*; 默认值: ) | 蜂窝网络通告信息 - 国家和网络代码。这有助于 Hotspot 2.0 客户端选择接入点以访问 3GPP 网络。格式为 “mcc/mnc”。用法与 “3gpp-raw” 相同，但无需使用十六进制。可以通过逗号分隔来定义多个 mcc/mnc 对。 |
| **authentication-types** (*dns-redirection:`url` \| https-redirection:`url` \| online-enrollment:`url` \| terms-and-conditions:`url`*; 默认值: ) | 此属性仅在 asra 设置为 `yes` 时有效。如果选择 `dns-redirection` 或 `online-enrollment`，则 `url` 的值是可选的，不需要提供。要将 `url` 的值设置为空字符串，请使用双引号。例如：`authentication-types=online-enrollment:""` |
| **connection-capabilities** (*数字:数字:closed\|open\|unknown*; 默认值: ) | 此选项允许提供有关允许的 IP 协议和端口的信息。此信息可以在 ANQP 响应中提供。第一个数字代表 IP 协议号，第二个数字代表端口号。<code>closed</code> - 如果协议和端口组合不允许，则设置；<code>open</code> - 如果协议和端口组合允许，则设置；<code>unknown</code> - 如果协议和端口组合是开放或关闭的，则设置。示例： `connection-capabilities=6:80:open,17:5060:closed` 在接入点上设置这样的值会告知正在连接接入点的无线客户端，HTTP（6 - TCP，80 - HTTP）是允许的，而 VoIP（17 - UDP；5060 - VoIP）是不允许的。此属性不限制或允许使用这些协议和端口，它仅向正在连接接入点的站点设备提供信息。 |
| **domain-names** (*字符串列表*; 默认值: ) | 一个或多个完全限定域名（FQDN），用于指示运营该热点的实体。正在连接接入点的站点可以请求此 ANQP 属性，并检查其拥有凭据的任何域名是否存在后缀匹配。 |
| **ipv4-availability** (*double-nated \| not-available \| port-restricted \| port-restricted-double-nated \| port-restricted-single-nated \| public \| single-nated \| unknown*; 默认值: **not-available**) | 关于可用的 IPv4 地址和访问类型的信息。<code>not-available</code> - 地址类型不可用；<code>public</code> - 公共 IPv4 地址可用；<code>port-restricted</code> - 端口受限的 IPv4 地址可用；<code>single-nated</code> - 单一 NAT 后的私有 IPv4 地址可用；<code>double-nated</code> - 双重 NAT 后的私有 IPv4 地址可用；<code>port-restricted-single-nated</code> - 端口受限的 IPv4 地址和单一 NAT 后的 IPv4 地址均可用；<code>port-restricted-double-nated</code> - 端口受限的 IPv4 地址和双重 NAT 后的 IPv4 地址均可用；<code>unknown</code> - 地址类型的可用性未知。 |
| **ipv6-availability** (*available \| not-available \| unknown*; 默认值: **not-available**) | 关于可用的 IPv6 地址和访问类型的信息。<code>not-available</code> - 地址类型不可用；<code>available</code> - 地址类型可用；<code>unknown</code> - 地址类型的可用性未知。 |
| **realms** (*字符串:eap-sim\|eap-aka\|eap-tls\|not-specified*; 默认值: ) | 关于支持的领域及相应 EAP 方法的信息。`realms=example.com:eap-tls,foo.ba:not-specified` |
| **realms-raw** (*十六进制八位字节字符串*; 默认值: ) | 手动设置 NAI Realm ANQP 元素。 |
| **roaming-ois** (*十六进制八位字节字符串*; 默认值: ) | 组织标识符（OI）通常是一个 24 位的唯一标识符，如组织唯一标识符（OUI）或公司标识符（CID）。在某些情况下，OI 更长，例如 OUI-36。订阅服务提供商（SSP）可以通过其 OI 来指定。roaming-ois 属性可以包含零个或多个 SSP 的 OI，这些 SSP 的网络可通过此 AP 访问。OI 的长度应在 OI 本身之前指定。例如，要设置 E4-8D-8C 和 6C-3B-6B： `roaming-ois=03E48D8C036C3B6B` |
| **venue-names** (*字符串:语言代码*; 默认值: ) | 场所名称可用于提供有关场所的附加信息。它可以帮助客户端选择合适的接入点。venue-names 参数由零个或多个包含场所名称和语言代码的二元组组成： `venue-names=CoffeeShop:eng,TiendaDeCafe:es`语言代码字段值是从 ISO-639 中选择的两个或三个字符的语言代码。 |

#### Realms raw

**realms-raw** - 包含十六进制值的字符串列表。每个字符串指定 “NAI Realm Tuple” 的内容，不包括 “NAI Realm Data Field Length” 字段。

每个十六进制编码的字符串必须包含以下字段：

```
- NAI Realm Encoding (1 字节)
- NAI Realm Length (1 字节)
- NAI Realm (可变长度)
- EAP Method Count (1 字节)
- EAP Method Tuples (可变长度)
```

例如，值 “00045465737401020d00” 解码为：

```
- NAI Realm Encoding: 0 (rfc4282)
- NAI Realm Length: 4
- NAI Realm: Test
- EAP Method Count: 1
- EAP Method Length: 2
- EAP Method Tuple: TLS, 无 EAP 方法参数
```

请注意，设置 “realms-raw=00045465737401020d00” 产生的通告内容与设置 “realms=Test:eap-tls” 相同。

有关完整的 NAI Realm 编码，请参阅 802.11-2016 第 9.4.5.10 节。

### Hotspot 2.0 ANQP 元素

Hotspot 2.0 规范引入了一些额外的 ANQP 元素。这些元素使用 ANQP 厂商特定元素 ID。以下是可用于更改这些元素的属性。

| 属性 | 描述 |
| :-- | :-- |
| **hotspot20** (*yes \| no*; 默认值: **yes**) | 指示接入点的 Hotspot 2.0 能力。 |
| **hotspot20-dgaf** (*yes \| no*; 默认值: **yes**) | 下行组播/广播转发（Downstream Group-Addressed Forwarding）。设置 DGAF 位的值，以指示发送到客户端的组播和广播帧是禁用还是启用。<code>yes</code> - 发送到客户端的组播和广播帧已启用；<code>no</code> - 发送到客户端的组播和广播帧已禁用。要禁用组播和广播帧，请设置 `multicast-helper=full`。 |
| **operational-classes** (*数字列表*; 默认值: ) | 关于同一 ESS 的其他可用频段的信息。 |
| **operator-names** (*字符串:语言代码*; 默认值: ) | 设置运营商名称。必须为每个运营商名称条目指定语言。operator-names 参数由零个或多个包含运营商名称和语言代码的二元组组成： `operator-names=BestOperator:eng,MejorOperador:es`语言代码字段值是从 ISO-639 中选择的两个或三个字符的语言代码。 |
| **wan-at-capacity** (*yes \| no*; 默认值: **no**) | 接入点或网络是否处于最大容量。如果设置为 `yes`，将不允许其他移动设备关联到该 AP。 |
| **wan-downlink** (*数字*; 默认值: **0**) | WAN 连接的下行速度，以 kbps 为单位。如果下行速度未知，则设置为 0。 |
| **wan-downlink-load** (*数字*; 默认值: **0**) | 在 `wan-measurement-duration` 期间测量的 WAN 连接下行负载。值范围为 0 到 255。<code>0</code> - 未知；<code>255</code> - 100%。 |
| **wan-measurement-duration** (*数字*; 默认值: **0**) | 测量 wan-downlink-load 和 `wan-uplink-load` 的持续时间。值是一个从 0 到 65535 的数字，表示十分之一秒。<code>0</code> - 未测量；<code>10</code> - 1 秒；<code>65535</code> - 1 小时 49 分钟或更长。 |
| **wan-status** (*down \| reserved \| test \| up*; 默认值: **reserved**) | 关于接入点 WAN 连接状态的信息。值 `reserved` 表示不通告状态。 |
| **wan-symmetric** (*yes \| no*; 默认值: **no**) | WAN 链路是否对称（上传和下载速度相同）。 |
| **wan-uplink** (*数字*; 默认值: **0**) | WAN 连接的上行速度，以 kbps 为单位。如果上行速度未知，则设置为 0。 |
| **wan-uplink-load** (*数字*; 默认值: **0**) | 在 wan-measurement-duration 期间测量的 WAN 连接上行负载。值范围为 0 到 255。<code>0</code> - 未知；<code>255</code> - 100%。 |

### 其他属性

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*; 默认值: ) | 配置文件的简短描述 |
| **name** (*字符串*; 默认值: ) | 互联配置文件的名称。 |

## 使用原生 RadSec 和 Orion Wifi 的配置指南

本指南介绍如何设置您的 MikroTik 设备，以便将其与 RadSec 代理和 Orion Wifi 配合使用，不过主要配置步骤是相同的，也适用于其他提供商：
请确保使用最新的长期版或稳定版 RouterOS 版本。

在无线局域网控制器（WLAN Controller）和 Orion Wifi 之间建立安全的 RADIUS 连接非常重要。
Orion Wifi 使用基于 TLS 的 RADIUS（RadSec）来确保 AAA 流量的端到端加密。

1) 导入从 Orion 下载的 RadSec 证书：

在 WinBox 中拖放证书，然后使用导入功能，该功能位于 WinBox 的 `/system/certificates` 下。命令行等效操作如下：

```
/certificate/import file-name=bw.radsec.cacert.pem passphrase=""
/certificate/import file-name=cert.pem passphrase=""
/certificate/import file-name=key.pem passphrase=""
```

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-01.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-02.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-03.webp)

证书导入后，应如下所示：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-04.webp)

1) 配置 Radius 客户端：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-05.webp)

命令行等效操作：

```
/radius/add address=216.239.32.91 certificate=cert.pem_0 protocol=radsec service=wireless timeout=1s500ms
```

1) 创建一个执行 802.1x 认证的无线安全配置文件：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-06.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-07.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-08.webp)

命令行等效操作是：

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) 下一步是配置无线接口并分配已创建的安全配置文件。按 “Advanced mode” 查看所有选项：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-09.webp)

命令行等效操作是：

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

确保配置了正确的国家/地区配置文件。在此示例中，我们使用 “wlan1”，但相同的命令也适用于其他接口，或者使用 `/interface/wireless/set wlan1`。

1) 配置互联设置（hotspot 2.0）：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-10.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-11.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-12.webp)

命令行等效操作：

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
请特别注意 “wan-downlink” 和 “wan-uplink”，在此场景中，值 “50” 用作占位符，请务必根据您的设置调整这些值。某些客户端设备会使用它来评估是否应加入网络。根据实际情况设置 “venue” – 场所类型、”venue-names” 和其他属性。“domain-names” 应为 hotspot 2.0 运营商的域名。
:::

1) 将互联配置文件分配给接口：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-13.webp)

命令行等效操作是：

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

如果您看不到 interworking-profile 字段，请按 “Advanced mode”。

注意：Orion 用于区分网络的 NAS-id 等于系统标识。要调整 nas-id，可以执行 `/system/identity/set name=exampleName`。

## 使用 RadSec 代理和 Orion Wifi 的配置指南

本指南介绍如何设置您的 MikroTik 设备，以便将其与 RadSec 代理和 Orion Wifi 配合使用，不过主要配置步骤是相同的，也适用于其他提供商：
本指南假设您已经配置了一个带有 Orion Wifi 凭据的 radsecproxy。请确保使用最新的长期版或稳定版 RouterOS 版本。

在无线局域网控制器和 Orion Wifi 之间建立安全的 RADIUS 连接非常重要。
Orion Wifi 使用基于 TLS 的 RADIUS（RadSec）来确保 AAA 流量的端到端加密。本指南适用于 RouterOS 接入点将 AAA 流量重定向到 RadSec 代理（radsecproxy），然后再通过互联网发送的场景。

1) 配置指向 radsecproxy 的 Radius 客户端：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-14.webp)

命令行等效操作是：

```
/radius/add address=192.168.88.233 secret=yourSecret service=wireless timeout=1s500ms
```

该 secret 应与 radsecproxy 上配置的 secret 匹配。在此示例中，“192.168.88.233” 是运行代理的虚拟机。

1) 创建一个执行 802.1x 认证的无线安全配置文件：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-06.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-07.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-08.webp)

命令行等效操作是：

```
/interface/wireless/security-profiles/add authentication-types=wpa2-eap management-protection=allowed mode=dynamic-keys name=dot1x_profile supplicant-identity="" radius-eap-accounting=yes eap-methods=passthrough
```

1) 下一步是配置无线接口并分配已创建的安全配置文件。按 “Advanced mode” 查看所有选项：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-09.webp)

命令行等效操作是：

```
/interface/wireless/set [ find default-name=wlan1 ] mode=ap-bridge security-profile=dot1x_profile wps-mode=disabled
```

确保配置了正确的国家/地区配置文件。在此示例中，我们使用 “wlan1”，但相同的命令也适用于其他接口，或者使用 `/interface/wireless/set wlan1`。

1) 配置互联设置（hotspot 2.0）：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-10.webp)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/ANQP_1.png)

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-12.webp)

命令行等效操作：

```
/interface/wireless/interworking-profile/add domain-names=orion.area120.com ipv4-availability=public name=Orion_MikroTik network-type=public-chargeable operator-names=Orion:eng realms=orion.area120.com:eap-tls roaming-ois=f4f5e8f5f4,baa2D00100,baa2d00000 venue=business-unspecified venue-names=Orion:eng wan-downlink=50 wan-uplink=50 wan-status=up
```

:::warning
请务必在 “wan-downlink” 和 “wan-uplink” 中指定一些值，在此场景中，值 “50” 用作占位符，某些客户端设备会使用它来评估是否应加入网络。根据实际情况设置 “venue” – 场所类型、”venue-names” 和其他属性。“domain-names” 应为 hotspot 2.0 运营商的域名。
:::

1) 将互联配置文件分配给接口：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-13.webp)

此步骤也可以使用以下命令完成：

```
/interface/wireless/set wlan1 interworking-profile=Orion_MikroTik
```

如果 radsecproxy 工作正常，则安装了相应 Hotspot 配置文件的客户端应该能够连接。

注意：Orion 用于区分网络的 NAS-id 等于系统标识。要调整 nas-id，可以执行 `/system/identity/set name=exampleName`。

## 故障排除

要检查 RADIUS 消息的状态，可以使用 radius 菜单。
![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-15.webp)
或者，通过命令行运行 `/radius/monitor X`，X 为数字 ID。您可以使用 `/radius/print` 查看 ID。
如需更多信息，可以在 `/system/logging/add topics=radius,debug,packet` 下配置额外的日志记录。您可以在 [`/log`](../../diagnostics-monitoring-and-troubleshooting/log/index.md) 下查看结果。

要查看活动的无线连接，请检查无线注册表 `/interface/wireless/registration-table/print`：

![](https://manual.mikrotik.com/docs/wireless/abgn/img/interworking-profiles-16.webp)