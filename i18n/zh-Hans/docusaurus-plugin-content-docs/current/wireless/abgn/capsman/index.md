# CAPsMAN

> 本页介绍 RouterOS 中的 CAPsMAN（集中式接入点管理），涵盖无线控制器设置，包括 AAA 认证、RADIUS 服务器集成、用于客户端管理的访问列表以及安全配置文件。它提供了详细的参数，如 MAC 地址格式、缓存间隔和 RADIUS 计费更新，以及跨多个 SSID 的 RADIUS 认证配置示例。

import DocCardList from '@theme/DocCardList';

# CAPsMAN

:::info
这是旧版 CAPsMAN（`/caps-man`），适用于运行 `wireless` 软件包（`/interface/wireless`）的设备。对于运行 `wifi-qcom` 或 `wifi-qcom-ac` 软件包（`/interface/wifi` 菜单）的设备，请参阅 [WiFi CAPsMAN](../../wifi/capsman.md)。两者是独立的：WiFi CAP 只能加入 WiFi CAPsMAN，而旧版 CAP 只能加入旧版 CAPsMAN。
:::

本节涵盖 CAPsMAN 无线控制器文档。使用它来为受支持的 RouterOS 无线设备配置集中式接入点管理。

<DocCardList />

## CAPsMAN AAA

用于配置 CAPsMAN AAA 功能的设置位于 `/caps-man/aaa` 菜单中：

| 属性 | 描述 |
| :-- | :-- |
| **mac-format** (*string*; 默认值：**XX:XX:XX:XX:XX:XX**) | 控制接入点在 MAC 认证和 MAC 计费 RADIUS 请求的 User-Name 属性中如何编码客户端的 MAC 地址。 |
| **mac-mode** (*as-username \| as-username-and-password*; 默认值：**as-username**) | 默认情况下，接入点在 MAC 认证期间发送 Access-Request 时使用空密码。当此属性设置为 as-username-and-password 时，接入点将使用与 User-Name 属性相同的值作为 User-Password 属性。 |
| **mac-caching** (*disabled \| time-interval*; 默认值：**disabled**) | 如果此值设置为时间间隔，接入点将缓存 RADIUS MAC 认证响应指定时间，如果已存在匹配的缓存条目，则不会联系 RADIUS 服务器。值 disabled 将禁用缓存。接入点将始终联系 RADIUS 服务器。 |
| **interim-update** (*disabled \| time-interval*; 默认值：**disabled**) | 当使用 RADIUS 计费时，接入点会定期向 RADIUS 服务器发送计费信息更新。此属性指定默认更新间隔，RADIUS 服务器可以使用 [Acct-Interim-Interval](#capsman-aaa) 属性覆盖该间隔。 |
| **called-format** (*mac \| mac:ssid \| ssid*; 默认值：**mac:ssid**) | "called-id" 标识符传递给 RADIUS 的格式。在配置 RADIUS 服务器客户端时，您可以指定 "called-id" 以区分多个条目。 |

### 示例

假设其余设置均已配置完成，仅剩 "Security" 部分。

#### 使用一台服务器进行 RADIUS 认证

1. 创建 CAPsMAN 安全配置。

2. 配置 RADIUS 服务器客户端。

3. 将配置分配给您的主配置文件（或直接分配给 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless
/caps-man/configuration/set security=radius
```

#### 为每个 SSID 使用不同的 RADIUS 服务器进行认证

1. 创建 CAPsMAN 安全配置。

2. 配置 AAA 设置。

3. 配置 RADIUS 服务器客户端。

4. 将配置分配给您的主配置文件（或直接分配给 CAP 本身）。

```ros
/caps-man/security/add authentication-types=wpa2-eap eap-methods=passthrough encryption=aes-ccm group-encryption=aes-ccm name=radius 
/caps-man/aaa/set called-format=ssid 
/radius/add address=x.x.x.x secret=SecretUserPass service=wireless called-id=SSID1 
/radius/add address=y.y.y.y secret=SecretUserPass service=wireless called-id=SSID2 
/caps-man/configuration/set security=radius
```

现在，所有连接到 ssid=**SSID1** 的 CAP 的客户端，其 RADIUS 认证请求将发送至 **x.x.x.x**；所有连接到 ssid=**SSID2** 的 CAP 的客户端，其 RADIUS 认证请求将发送至 **y.y.y.y**。

## CAPsMAN 访问列表

CAPsMAN 上的访问列表是一个有序规则列表，用于允许/拒绝客户端连接到 CAPsMAN 控制下的任何 CAP。当客户端尝试连接到由 CAPsMAN 控制的 CAP 时，CAP 会将该请求转发给 CAPsMAN。作为注册过程的一部分，CAPsMAN 会查阅访问列表以确定是否应允许客户端连接。访问列表的默认行为是允许连接。

访问列表规则会逐一处理，直到找到匹配的规则。然后执行匹配规则中的操作。如果操作指定应接受客户端，则客户端被接受，并可能使用访问列表规则中指定的参数覆盖其默认连接参数。

访问列表在 `/caps-man/access-list` 菜单中配置。访问列表规则有以下参数：

- 客户端匹配参数：
  - address - 客户端的 MAC 地址。
  - mask - 比较客户端地址时应用的 MAC 地址掩码。
  - interface - 可选接口，用于与客户端实际连接的接口进行比较。
  - time - 规则匹配的日期和时间。
  - signal-range - 客户端信号必须处于的范围内，规则才能匹配。
  - allow-signal-out-of-range - 允许客户端信号始终或在一段时间间隔内超出范围的选项。
- 操作参数 - 指定客户端匹配时要执行的操作：
  - accept - 接受客户端。
  - reject - 拒绝客户端。
  - query-radius - 查询 RADIUS 服务器以确定特定客户端是否允许连接。
- 连接参数：
  - ap-tx-limit - 指向客户端的传输速度限制。
  - client-tx-limit - 指向 AP 的传输速度限制（仅适用于 RouterOS 客户端）。
  - client-to-client-forwarding - 指定是否允许将从此客户端接收的数据转发到连接到同一接口的其他客户端。
  - private-passphrase - *[敏感参数](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* 如果使用某种 PSK 认证算法，则用于此客户端的 PSK 密码短语。
  - radius-accounting - 指定如果对此客户端进行 RADIUS 认证，是否应使用 RADIUS 流量计费。
  - vlan-mode - VLAN 标记模式，指定来自客户端的数据是否应被标记（以及发往客户端的数据是否应取消标记）。
  - vlan-id - 如果进行 VLAN 标记，则使用的 VLAN ID。

## CAPsMAN 信道

信道组设置允许配置与无线电信道相关的设置列表，例如无线电频段、频率、发射功率、扩展信道和宽度。

信道组设置在信道配置文件菜单 `/caps-man/channels` 中配置。

| 属性 | 描述 |
| :-- | :-- |
| **band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn*; 默认值：) | 定义工作无线电频段和模式，取自无线网卡的硬件能力 |
| **comment** (*string*; 默认值：) | 信道组配置文件的简短描述 |
| **extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| disabled*; 默认值：) | 扩展信道配置。（例如：Ce = 扩展信道在控制信道之上，eC = 扩展信道在控制信道之下） |
| **frequency** (*integer [0..4294967295]*; 默认值：) | AP 将工作的信道频率值，单位为 MHz。 |
| **name** (*string*; 默认值：) | 信道组配置文件的描述性名称 |
| **tx-power** (*integer [-30..40]*; 默认值：) | CAP 接口的发射功率（针对整个接口，而非单个链），单位为 dBm。不能设置高于国家法规或接口允许的值。默认使用国家或接口允许的最大值。 |
| **width** (; 默认值：) | 设置信道宽度，单位为 MHz。（例如：20, 40） |
| **save-selected** (; 默认值：**yes**) | 保存 CAP 无线电的选定信道 - CAP 重新连接到 CAPsMAN 后将选择此信道，并一直使用，直到对此 CAP 完成信道重新优化。 |

## CAPsMAN 配置

配置配置文件允许将预定义的“顶级”主设置应用于正在配置的 CAP 无线电。

配置配置文件在 `/caps-man/configuration` 菜单中配置：

| 属性 | 描述 |
| :-- | :-- |
| **channel** (*list*; 默认值：) | 用户定义的列表，取自信道名称（`/caps-man/channels`） |
| **channel.band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-only-ac*; 默认值：) | 定义一组使用的信道。 |
| **channel.control-channel-width** (*40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*; 默认值：) | 定义一组使用的信道宽度。 |
| **channel.extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| xx \| xxxx \| disabled*; 默认值：) | 扩展信道配置。（例如：Ce = 扩展信道在控制信道之上，eC = 扩展信道在控制信道之下） |
| **channel.frequency** (*integer [0..4294967295]*; 默认值：) | AP 将工作的信道频率值，单位为 MHz。如果留空，CAPsMAN 将自动确定占用最少的最佳频率。 |
| **channel.reselect-interval** (*time [00:00:00]; [00:00:00..00:00:00]*; 默认值：) | 选择占用最少频率的间隔，可以定义为随机间隔，例如 "30m..60m"。仅在 **channel.frequency** 留空时有效。 |
| **channel.save-selected** (*yes \| no*; 默认值：**no**) | 如果自动选择信道频率并使用 **channel.reselect-interval**，则保存最后选择的频率。 |
| **channel.secondary-frequency** (*integer [0..4294967295]*; 默认值：**auto**) | 指定用于 80+80MHz 配置的第二个频率。将其设置为 **Disabled** 以禁用 80+80MHz 功能。 |
| **channel.skip-dfs-channels** (*yes \| no*; 默认值：**no**) | 如果 **channel.frequency** 留空，选择将跳过 DFS 信道 |
| **channel.tx-power** (*integer [-30..40]*; 默认值：) | CAP 接口的发射功率（针对整个接口，而非单个链），单位为 dBm。不能设置高于国家法规或接口允许的值。默认使用国家或接口允许的最大值。 |
| **channel.width** (; 默认值：) | 设置信道宽度，单位为 MHz。 |
| **comment** (*string*; 默认值：) | 配置配置文件的简短描述 |
| **country** (*国家名称 \| no\_country\_set*; 默认值：**no\_country\_set**) | 限制每个频率的可用频段、频率和最大发射功率。同时指定 **scan-list** 的默认值。值 *no\_country\_set* 是符合 FCC 的信道集。 |
| **datapath** (*list*; 默认值：) | 用户定义的列表，取自数据路径名称（`/caps-man/datapath`） |
| **datapath.bridge** (*list*; 默认值：) | 特定接口应自动添加为端口的桥接。仅在未使用本地转发时需要。 |
| **datapath.bridge-cost** (*integer [1..*200000000*]*; 默认值：) | 添加为桥接端口时使用的桥接端口开销 |
| **datapath.bridge-horizon** (*integer [0..4294967295]*; 默认值：) | 添加为桥接端口时使用的桥接水平线 |
| **datapath.client-to-client-forwarding** (*yes \| no*; 默认值：**no**) | 控制是否允许连接到接口的无线客户端之间的客户端到客户端转发，在本地转发模式下此功能由 CAP 执行，否则由 CAPsMAN 执行 |
| **datapath.interface-list** (; 默认值：) |  |
| **datapath.l2mtu** (; 默认值：) | 设置第 2 层 MTU 大小 |
| **datapath.local-forwarding** (*yes \| no*; 默认值：**no**) | 控制转发模式。如果禁用，所有 L2 和 L3 数据将转发到 CAPsMAN，然后才做出进一步的转发决策。**注意**，如果禁用，请确保参与同一广播域的每个 CAP 接口 MAC 地址都是唯一的（包括本地 MAC，如 Bridge-MAC）。 |
| **datapath.mtu** (; 默认值：) | 设置 MTU 大小 |
| **datapath.openflow-switch** (; 默认值：) | 启用时将接口添加到的 OpenFlow 交换机端口 |
| **datapath.vlan-id** (*integer [1..4095]*; 默认值：) | 如果 vlan-mode 启用 VLAN 标记，则分配给接口的 VLAN ID |
| **datapath.vlan-mode** (*use-service-tag \| use-tag*; 默认值：) | 启用并指定分配给接口的 VLAN 标签类型（导致所有接收到的数据都带有 VLAN 标签，并允许接口仅发送带有给定标签的数据） |
| **disconnect-timeout** (; 默认值：) |  |
| **distance** (; 默认值：) |  |
| **frame-lifetime** (; 默认值：) |  |
| **guard-interval** (*any \| long*; 默认值：**any**) | 是否允许使用短保护间隔（请参阅 802.11n MCS 规范以了解这可能如何影响吞吐量）。"any" 将根据数据速率使用短或长间隔，"long" 将仅使用长间隔。 |
| **hide-ssid** (*yes \| no*; 默认值：) | yes - AP 不在信标帧中包含 SSID，并且不回复具有广播 SSID 的探测请求。no - AP 在信标帧中包含 SSID，并回复具有广播 SSID 的探测请求。此属性仅在 AP 模式下有效。将其设置为 *yes* 可以将此网络从某些客户端软件显示的无线网络列表中移除。更改此设置不会提高无线网络的安全性，因为 SSID 包含在 AP 发送的其他帧中。 |
| **hw-protection-mode** (; 默认值：) |  |
| **hw-retries** (; 默认值：) |  |
| **installation** (*any \| indoor \| outdoor*; 默认值：**any**) |  |
| **keepalive-frames** (*enabled \| disabled*; 默认值：**enabled**) |  |
| **load-balancing-group** (*string*; 默认值：) | 将接口标记到负载均衡组。对于客户端要连接到此组中的接口，该接口的已连接客户端数量应与此组中所有其他接口相同或更少。在 CAP 范围大部分重叠的设置中很有用。 |
| **max-sta-count** (*integer [1..2007]*; 默认值：) | 最大关联客户端数。 |
| **mode** (; 默认值：**ap**) | 设置操作模式。目前仅支持 ap。 |
| **multicast-helper** (*default \| disabled \| full*; 默认值：**default**) | 设置为 full 时，多播数据包将使用单播目标 MAC 地址发送，解决无线链路上的多播问题。此选项应仅在接入点上启用，客户端应配置为 **station-bridge** 模式。disabled - 禁用助手，并使用多播目标 MAC 地址发送多播数据包。full - 在发送之前，所有多播数据包 MAC 地址都更改为单播 MAC 地址。default - 当前设置为 disabled 的默认选择。该值可能在将来的版本中更改。 |
| **name** (*string*; 默认值：) | 配置配置文件的描述性名称 |
| **rates** (; 默认值：) | 用户定义的列表，取自速率名称（`/caps-man/rates`） |
| **rates.basic** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*; 默认值：) |  |
| **rates.supported** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*; 默认值：) |  |
| **rates.ht-basic-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每个连接客户端必须支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有关 MCS 规范，请参阅 802.11n。 |
| **rates.ht-supported-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此设备通告为支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有关 MCS 规范，请参阅 802.11n。 |
| **rates.vht-basic-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 默认值：**none**) | 每个连接客户端必须支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有关 MCS 规范，请参阅 802.11ac。您可以为每个空间流设置 MCS 间隔。none - 不使用选定的空间流。MCS 0-7 - 客户端必须支持 MCS-0 到 MCS-7。MCS 0-8 - 客户端必须支持 MCS-0 到 MCS-8。MCS 0-9 - 客户端必须支持 MCS-0 到 MCS-9。 |
| **rates.vht-supported-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 默认值：**none**) | 此设备通告为支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。有关 MCS 规范，请参阅 802.11ac。您可以为每个空间流设置 MCS 间隔。none - 不使用选定的空间流。MCS 0-7 - 设备将通告支持 MCS-0 到 MCS-7。MCS 0-8 - 设备将通告支持 MCS-0 到 MCS-8。MCS 0-9 - 设备将通告支持 MCS-0 到 MCS-9。 |
| **rx-chains** (*list of integer [0..3]*; 默认值：**0**) | 用于接收的天线。 |
| **security** (*string*; 默认值：**none**) | 来自 `/caps-man/security` 的安全配置名称 |
| **security.authentication-types** (*list of string*; 默认值：**none**) | 指定认证类型，从 **wpa-psk**、**wpa2-psk**、**wpa-eap** 或 **wpa2-eap** 中选择 |
| **security.disable-pmkid** (; 默认值：) |  |
| **security.eap-methods** (*eap-tls \| passthrough*; 默认值：**none**) | eap-tls - 使用内置的 EAP TLS 认证。passthrough - 接入点将认证过程中继到 RADIUS 服务器。 |
| **security.eap-radius-accounting** (; 默认值：) | 指定如果对此客户端进行 RADIUS 认证，是否应使用 RADIUS 流量计费 |
| **security.encryption** (*aes-ccm \| tkip*; 默认值：) | 设置使用的单播加密算法类型 |
| **security.group-encryption** (*aes-ccm \| tkip*; 默认值：**aes-ccm**) | 接入点通告这些密码之一，可以选择多个值。接入点使用它来加密所有广播和多播帧。客户端仅尝试连接到使用指定组密码之一的接入点。tkip - 临时密钥完整性协议 - 加密协议，与旧版 WEP 设备兼容，但增强了以纠正 WEP 的一些缺陷。aes-ccm - 更安全的 WPA 加密协议，基于可靠的 AES（高级加密标准）。没有 WEP 旧版设备的网络应仅使用此密码。 |
| **security.group-key-update** (*time: 30s..1h*; 默认值：**5m**) | 控制接入点更新组密钥的频率。此密钥用于加密所有广播和多播帧。此属性仅对接入点有效。 |
| **security.passphrase** (*string*; 默认值：) *[敏感参数](../../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | WPA 或 WPA2 预共享密钥 |
| **security.tls-certificate** (*none \| name*; 默认值：) | 当 **security.tls-mode** 设置为 **no-certificates** 以外的值时，接入点始终需要证书。 |
| **security.tls-mode** (*verify-certificate \| dont-verify-certificate \| no-certificates \| verify-certificate-with-crl*; 默认值：) | 此属性仅在 **security.eap-methods** 包含 *eap-tls* 时有效。verify-certificate - 要求远程设备具有有效证书。检查它是否由已知证书颁发机构签名。不进行额外的身份验证。证书可能包含其有效时间段的信息。如果路由器时间不正确，它可能会拒绝有效证书，因为路由器的时钟在该时间段之外。另请参阅证书配置。dont-verify-certificate - 不检查远程设备的证书。接入点将不要求客户端提供证书。no-certificates - 不使用证书。TLS 会话使用 2048 位匿名 Diffie-Hellman 密钥交换建立。verify-certificate-with-crl - 与 verify-certificate 相同，但还通过检查证书吊销列表来验证证书是否有效。 |
| **ssid** (*string (0..32 chars)*; 默认值：) | SSID（服务集标识符）是在信标中广播的名称，用于标识无线网络。 |
| **tx-chains** (*list of integer [0..3]*; 默认值：**0**) | 用于传输的天线。 |

## CAPsMAN 数据路径

数据路径设置控制与数据转发相关的方面。在 CAPsMAN 中，数据路径设置在数据路径配置文件菜单 `/caps-man/datapath` 中配置，或直接在配置配置文件或接口菜单中以 **datapath.** 前缀的设置形式配置。

有两种主要的转发模式：

- 本地转发模式，CAP 在本地转发来自和发往无线接口的数据。
- 管理器转发模式，CAP 将通过无线接收的所有数据发送到 CAPsMAN，并且仅发送从 CAPsMAN 接收的无线数据。在此模式下，甚至客户端到客户端的转发也由 CAPsMAN 控制和执行。

转发模式是按接口配置的 - 因此，如果一个 CAP 提供 2 个无线电接口，则可以将一个配置为在本地转发模式下运行，另一个配置为在管理器转发模式下运行。这同样适用于 Virtual-AP 接口 - 每个接口都可以具有与主接口或其他 Virtual-AP 接口不同的转发模式。

大多数数据路径设置仅在管理器转发模式下使用，因为在本地转发模式下 CAPsMAN 无法控制数据转发。

有以下数据路径设置：

- bridge -- 启用时，将接口添加为桥接端口的桥接接口。
- bridge-cost -- 添加为桥接端口时使用的桥接端口开销。
- bridge-horizon -- 添加为桥接端口时使用的桥接水平线。
- client-to-client-forwarding -- 控制是否允许连接到接口的无线客户端之间的客户端到客户端转发，在本地转发模式下此功能由 CAP 执行，否则由 CAPsMAN 执行。
- local-forwarding -- 控制转发模式。
- openflow-switch -- 启用时，将接口添加为端口的 OpenFlow 交换机。
- vlan-id -- 如果 vlan-mode 启用 VLAN 标记，则分配给接口的 VLAN ID。
- vlan-mode -- VLAN 标记模式，指定是否应将 VLAN 标签分配给接口（导致所有接收到的数据都带有 VLAN 标签，并允许接口仅发送带有给定标签的数据）。

## CAPsMAN 接口

CAPsMAN 接口在 `/caps-man/interface` 菜单中管理：

```ros
[admin@CM] > /caps-man/interface/print 
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
# NAME RADIO-MAC MASTER-INTERFACE 
0 M BR cap2 00:0C:42:1B:4E:F5 none 
1 B cap3 00:00:00:00:00:00 cap2
```

## CAPsMAN 管理器

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*; 默认值：**no**) | 禁用或启用 CAPsMAN 功能 |
| **certificate** (*auto \| certificate name \| none*; 默认值：**none**) | 设备证书 |
| **ca-certificate** (*auto \| certificate name \| none*; 默认值：**none**) | 设备 CA 证书 |
| **require-peer-certificate** (*yes \| no*; 默认值：**no**) | 要求所有连接的 CAP 都具有有效证书 |
| **package-path** (*string \|*; 默认值：) | RouterOS 软件包的文件夹位置。例如，使用 "/upgrade" 指定文件部分中的升级文件夹。如果设置为空字符串，CAPsMAN 可以使用内置的 RouterOS 软件包，请注意，在这种情况下，只有与 CAPsMAN 具有相同架构的 CAP 才会被升级。 |
| **upgrade-policy** (*none \| require-same-version \| suggest-same-version*; 默认值：**none**) | CAPsMAN 可以向 CAP 设备发送 NPK 软件包以升级它们。这绕过了 CAP 设备可能拥有的任何升级通道偏好，并通过简单的数字比较工作。如果 CAPsMAN 上安装了较新的版本，它将发送软件包并升级设备，无论通道如何。none - 不执行升级。require-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败，则不会配置 CAP。（手动配置仍然可能）suggest-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败，仍将配置它。 |

## CAPsMAN 配置

CAPsMAN 基于通用名称标识符区分 CAP。该标识符根据以下规则生成：

- 如果 CAP 提供证书，则标识符设置为证书中的通用名字段。
- 否则，标识符基于 CAP 提供的 Base-MAC，格式为：'[XX:XX:XX:XX:XX:XX]'。

当与 CAP 的 DTLS 连接成功建立（这意味着 CAP 标识符已知且有效）时，CAPsMAN 确保没有使用相同标识符的与 CAP 的过时连接。当前连接的 CAP 列在 `/caps-man/remote-cap` 菜单中：

```ros
[admin@CM] /caps-man> remote-cap print 
# ADDRESS IDENT STATE RADIOS
0 00:0C:42:00:C0:32/27044 MT-000C4200C032 Run 1
```

CAPsMAN 基于其内置 MAC 地址（radio-mac）区分实际的无线接口（无线电）。这意味着无法在一个 CAPsMAN 上管理两个具有相同 MAC 地址的无线电。当前由 CAPsMAN 管理的无线电（由连接的 CAP 提供）列在 `/caps-man/radio` 菜单中：

```ros
[admin@CM] /caps-man> radio print 
Flags: L - local, P - provisioned 
# RADIO-MAC INTERFACE REMOTE-AP-IDENT 
0 P 00:03:7F:48:CC:07 cap1 MT-000C4200C032
```

当 CAP 连接时，CAPsMAN 首先尝试根据 radio-mac 将每个 CAP 无线电绑定到 CAPsMAN 主接口。如果找到合适的接口，则使用主接口配置以及引用特定主接口的从接口配置来设置无线电。此时，接口（主接口和从接口）被视为绑定到无线电，无线电被视为已配置。

如果未找到匹配的无线电主接口，CAPsMAN 将执行“配置规则”。配置规则是一个有序规则列表，包含指定匹配哪个无线电的设置以及指定如果无线电匹配则采取什么操作的设置。

用于匹配无线电的配置规则在 `/caps-man/provisioning` 菜单中配置：

| 属性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled \| create-enabled \| create-dynamic-enabled \| none*; 默认值：**none**) | 如果规则匹配，则采取的操作，由以下设置指定：create-disabled - 为无线电创建禁用的静态接口。即，接口将绑定到无线电，但无线电在接口手动启用之前不会运行。create-enabled - 创建启用的静态接口。即，接口将绑定到无线电，并且无线电将运行。create-dynamic-enabled - 创建启用的动态接口。即，接口将绑定到无线电，并且无线电将运行。none - 不执行任何操作，使无线电保持未配置状态。 |
| **comment** (*string*; 默认值：) | 配置规则的简短描述 |
| **common-name-regexp** (*string*; 默认值：) | 用于按通用名称匹配无线电的正则表达式。每个 CAP 的通用名称标识符可以在 `/caps-man/radio` 下找到，作为 "REMOTE-CAP-NAME" 值 |
| **hw-supported-modes** (*a\|a-turbo\|ac\|an\|b\|g\|g-turbo\|gn*; 默认值：) | 按支持的无线模式匹配无线电 |
| **identity-regexp** (*string*; 默认值：) | 用于按路由器身份匹配无线电的正则表达式 |
| **ip-address-ranges** (*IpAddressRange[,IpAddressRanges] max 100x*; 默认值：**""**) | 匹配 IP 在配置的地址范围内的 CAP。 |
| **master-configuration** (*string*; 默认值：) | 如果 **action** 设置为创建接口，则将创建一个新的主接口，其配置设置为此配置配置文件 |
| **name-format** (*cap \| identity \| prefix \| prefix-identity*; 默认值：**cap**) | 指定 CAP 接口名称创建的语法。cap - 默认名称。identity - CAP 板的系统身份名称。prefix - 来自 name-prefix 值的名称。prefix-identity - 来自 name-prefix 值和 CAP 板的系统身份名称。 |
| **name-prefix** (*string*; 默认值：) | 可用于 name-format 中创建 CAP 接口名称的名称前缀 |
| **radio-mac** (*MAC address*; 默认值：**00:00:00:00:00:00**) | 要匹配的无线电的 MAC 地址，空 MAC（00:00:00:00:00:00）表示匹配所有 MAC 地址 |
| **slave-configurations** (*string*; 默认值：) | 如果 **action** 设置为创建接口，则为列表中的每个配置配置文件创建一个新的从接口。 |

:::warning
如果没有规则匹配无线电，则执行隐式默认规则，其操作 **create-enabled** 且未设置配置。
:::

要获取活动的配置匹配器：

```ros
[admin@CM] /caps-man/provisioning> print 
Flags: X - disabled 
0 radio-mac=00:00:00:00:00:00 action=create-enabled master-configuration=main-cfg 
slave-configurations=virtual-ap-cfg name-prefix=""
```

为了方便用户，有一些命令允许对某些无线电或某个 AP 提供的所有无线电重新执行配置过程：

```ros
[admin@CM] > /caps-man/radio/provision 0
```

和

```ros
[admin@CM] > /caps-man/remote-cap/provision 0
```

### CAPsMAN 无线电

[参见 `/caps-man/provisioning`](#capsman-provisioning)

### CAPsMAN 速率

[参见 `/caps-man/configuration`](#capsman-configuration)

### CAPsMAN 注册表

注册表包含连接到由 CAPsMAN 控制的无线电的客户端列表，可在 `/caps-man/registration-table` 菜单中找到：

```ros
[admin@CM] /caps-man> registration-table print
# INTERFACE MAC-ADDRESS UPTIME RX-SIGNAL
0 cap1 00:03:7F:48:CC:0B 1h38m9s210ms -36
```

### CAPsMAN 远程 CAP

[参见 `/caps-man/provisioning`](#capsman-provisioning)

### CAPsMAN 安全

