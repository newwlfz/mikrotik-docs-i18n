# RADIUS

> RADIUS 通过 UDP 或 RadSec 协议连接到 RADIUS 服务器，为 MikroTik RouterOS 中的 PPP、HotSpot 及其他服务提供集中式认证和计费功能，并支持可配置的端口、共享密钥及特定于服务的设置。

# RADIUS

RADIUS，即远程认证拨号用户服务（Remote Authentication Dial-In User Service），是一种远程服务器，为各种网络设备提供认证和计费功能。RADIUS 认证和计费允许 ISP 或网络管理员在大型网络中通过单一服务器管理 PPP 用户访问和计费。MikroTik RouterOS 内置 RADIUS 客户端，可对[路由器本地](./user.md) [用户](./user.md)、[HotSpot](./hotspot-captive-portal/index.md)、[PPP](../mobile-networking/ppp.md) 和 ISDN 连接进行认证。从 RADIUS 服务器接收的属性会覆盖默认配置文件中设置的属性，但若某些参数未接收到，则使用相应默认配置文件中的值。

仅当在路由器本地数据库中未找到匹配的用户访问记录时，才会查询 RADIUS 服务器数据库。

如果启用了 RADIUS 计费，计费信息也会发送到该服务的默认 RADIUS 服务器。

## RADIUS 客户端

**子菜单：** `/radius`

此子菜单用于添加和移除 RADIUS 客户端。

:::warning
此列表中条目的顺序非常重要。

:::

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **accounting-backup** (*yes \| no*; 默认值： **no**) | 配置是否用于备份 RADIUS 服务器 |
| **accounting-port** (*整数 [1..65535]*; 默认值： **1813**) | 用于计费的 RADIUS 服务器端口 |
| **address** (*IPv4/IPv6 地址*; 默认值： **0.0.0.0**) | RADIUS 服务器的 IPv4 或 IPv6 地址。支持以下格式：  - *ipv4* - *ipv4*`@`*vrf* - *ipv6* - *ipv6*`@`*vrf* |
| **authentication-port** (*整数 [1..65535]*; 默认值： **1812**) | 用于认证的 RADIUS 服务器端口。 |
| **called-id** (*字符串*; 默认值： ) | 值取决于点对点协议：PPPoE - 服务名称，PPTP - 服务器 IP 地址，L2TP - 服务器 IP 地址。 |
| **certificate** (*字符串*; 默认值： ) | 用于在启用 RadSec 时与 RADIUS 服务器通信的[证书库中的证书](../authentication-authorization-accounting/certificates.md)。 |
| **comment** (*字符串*; 默认值： ) |  |
| **disabled** (*yes \| no*; 默认值： **no**) |  |
| **domain** (*字符串*; 默认值： ) | 传递给需要域验证的 RADIUS 服务器的客户端 Microsoft Windows 域。 |
| **protocol** (*radsec \| udp*; 默认值： **udp**) | 指定与 RADIUS 服务器通信时使用的协议。 |
| **radsec-timeout**(*时间,* 默认值： **3300ms**) | 通过 RadSec 协议重发请求之前的超时时间。 |
| **require-message-auth** (*no \| yes-for-request-resp* 默认值： **yes-for-request-resp**) | 指定是否需要 Message-Authenticator 属性。 |
| **realm** (*字符串*; 默认值： ) | 显式指定的领域（用户域），这样用户无需在用户名中提供正确的 ISP 域名。 |
| **secret** (*字符串*; 默认值： ) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于访问 RADIUS 服务器的共享密钥。 |
| **service** (*ppp\|login\|hotspot\|wireless\|dhcp\|ipsec\|dot1x*; 默认值： ) | 将使用此 RADIUS 服务器的路由器服务：hotspot - HotSpot 认证服务login - 路由器本地用户认证ppp - 点对点客户端认证wireless - 无线客户端认证dhcp - DHCP 协议客户端认证（客户端的 MAC 地址作为 User-Name 发送）ipsec - IPsec 客户端认证dot1x - dot1x 认证 |
| **src-address** (*ipv4/ipv6 地址*; 默认值： **0.0.0.0**) | 发送到 RADIUS 服务器的数据包的源 IP/IPv6 地址 |
| **timeout** (*时间*; 默认值： **1100ms**) | 重发请求之前的超时时间。 |

:::warning
当 RADIUS 服务器使用 CHAP、MS-CHAPv1、MS-CHAPv2 认证用户时，它不使用共享密钥；该密钥仅用于认证回复中，由路由器（RADIUS 客户端）进行验证。因此，如果共享密钥错误，RADIUS 服务器会接受请求，但路由器不会接受回复。您可以通过 "`/radius/monitor`" 命令查看，当有人尝试连接时，"bad-replies" 计数应增加。

:::

:::danger
如果启用了 RadSec，请确保您的 RADIUS 服务器使用 "**radsec**" 作为共享密钥，否则 RADIUS 服务器将无法正确解密数据（不可打印字符）。使用 RadSec 时，RouterOS 会强制将共享密钥设置为 "radsec"，无论手动设置了什么。更多详情请参见 RFC6614。

:::

:::info
如果使用 RadSec，RouterOS 将覆盖并使用 TCP 端口 2083。
:::

### 示例

要为 HotSpot 和 PPP 服务设置一个 RADIUS 客户端，并针对 RADIUS 服务器（10.0.0.3）进行认证，您需要执行以下操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=ex
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 
```

要设置一个使用 RadSec 的 RADIUS 客户端，您需要执行以下操作：

```ros
[admin@MikroTik] > /radius/add service=hotspot,ppp address=10.0.0.3 secret=radsec protocol=radsec certificate=client.crt
[admin@MikroTik] > /radius/print
Flags: X - disabled
# SERVICE CALLED-ID DOMAIN ADDRESS SECRET
0 ppp,hotspot 10.0.0.3 radsec
```

:::warning
确保指定的证书是受信任的，并且两端的 common-name 验证都能正常工作。

:::

以下是一个可用于 RADIUS RadSec 配置的证书简单示例：

```ros
在服务器上：

#CN 应为 RADIUS 服务器 IP
/certificate/add name=radsec_server common-name=10.155.114.91
/certificate/sign radsec_server

#CN 应为 RADIUS 客户端 IP
/certificate/add name=radsec_client1 common-name=10.155.114.92
/certificate/sign radsec_client1
/user-manager/set radsec-certificate=radsec_server

#在服务器上导出证书以便在客户端上应用
/certificate/export-certificate type=pkcs12 export-passphrase=verystrongpassword radsec_client1
/certificate/export-certificate type=pkcs12 radsec_server

在客户端上：

#下载两个文件并上传到客户端
/certificate/import file-name=cert_export_radsec_client1.p12 passphrase=verystrongpassword
/certificate/import file-name=cert_export_radsec_server.p12
/radius/set <radius_client_id_in_list> certificate=cert_export_radsec_client1.p12_0

#之后，当 RADIUS 客户端尝试连接到服务器时，您应该在状态字段中看到：status="TLS connected"。
```

要查看 RADIUS 客户端统计信息，您需要执行以下操作：

```ros
[admin@MikroTik] > /radius/monitor 0
pending: 0
requests: 10
accepts: 4
rejects: 1
resends: 15
timeouts: 5
bad-replies: 0
last-request-rtt: 0s
```

确保为所需服务启用 RADIUS 认证：

```ros
/ppp/aaa/set use-radius=yes
/ip/hotspot/profile/set default use-radius=yes
```

## 从 RADIUS 终止连接

**子菜单：** `/radius/incoming`

此功能支持从 RADIUS 服务器发送的主动消息。主动消息扩展了 RADIUS 协议命令，允许从 RADIUS 服务器终止已建立的会话。为此，使用 DM（Disconnect-Messages，断开消息）。断开消息会导致用户会话立即终止。

:::warning
RouterOS 不支持 POD（Packet of Disconnect，断开数据包），这是另一种执行与断开消息类似功能的 RADIUS 访问请求数据包。

:::

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **accept** (*yes \| no*; 默认值： **no**) | 是否接受主动消息 |
| **port** (*整数*; 默认值： **1700**) | 监听请求的端口号 |
| **vrf** (*VRF 名称*; 默认值： **main**) | 设置服务监听传入连接的 VRF |

## 支持的 RADIUS 属性

您可以在此下载 [RADIUS 参考字典.txt](pathname:///assets/319783010_RADIUS_reference_dictionary.txt)，其中包含 MikroTik 设备支持的所有 RADIUS 属性。此文件专为 FreeRADIUS 设计，但也可用于其他 RADIUS 服务器。请注意，它可能与您的 RADIUS 服务器的默认配置文件冲突。请修正配置，而不是字典，因为 MikroTik RouterOS 不支持其他属性。还有 [MikroTik 厂商属性.txt](pathname:///assets/319783011_MikroTik_Vendor_attributes.txt) 可以包含在现有字典中，以支持 MikroTik 特定厂商属性。

下面您将找到关于属性及其在 MikroTik 设备与 RADIUS 通信期间使用方式的描述。

### 定义

- **PPPs** - PPP, PPTP, PPPoE
- **默认配置** - 默认配置文件中的设置（对于 PPPs）或 HotSpot 服务器设置（对于 HotSpot）

### Access-Request 数据包

- **Service-Type** - 始终为 "Framed"（仅适用于 PPPs）。
- **Framed-Protocol** - 始终为 "PPP"（仅适用于 PPPs）。
- **NAS-Identifier** - 路由器的身份名称。
- **NAS-IP-Address** - 路由器自身的 IP 地址。
- **NAS-Port** - 此属性表示正在认证用户的 NAS 物理端口号。
- **Acct-Session-Id** - 唯一的会话 ID。会话 ID 的前两个符号代表服务（PPP、Hotspot 等）。下一个符号在每次重启时递增。最后一组符号在每次新会话时递增。这意味着，在同一启动周期内，对于相同 RADIUS 类型的服务，在一百万次重新连接中不会得到相同的 ID。如果您丢失了会话停止消息，并且 RADIUS 服务器仍保持会话打开，但随后收到另一条会话开始消息，则它必须意识到停止消息已丢失，关闭旧会话并启动新会话。
- **NAS-Port-Type** - Async PPP - "Async"；PPTP 和 L2TP - "Virtual"；PPPoE - "Ethernet"；ISDN - "ISDN Sync"；HotSpot - "Ethernet | Cable | Wireless-802.11"（根据 `/ip/hotspot/profile` 中 nas-port-type 参数的值）。
- **Calling-Station-Id** - PPPoE 和 HotSpot - 客户端 MAC 地址（大写字母）；PPTP 和 L2TP - 客户端公网 IP 地址。
- **Called-Station-Id** - PPPoE - 服务名称；PPTP 和 L2TP - 服务器 IP 地址；HotSpot - HotSpot 服务器名称。
- **NAS-Port-Id** - Async PPP - 串口名称；PPPoE - 服务器运行所在的以太网接口名称；HotSpot - 物理 HotSpot 接口名称（如果桥接，则显示桥接端口名称）；ISDN、PPTP 和 L2TP 不存在此属性。
- **Framed-IP-Address** - 经过 Universal Client 转换后的 HotSpot 客户端 IP 地址。
- **Mikrotik-Host-IP** - 经过 Universal Client 转换前的 HotSpot 客户端 IP 地址（客户端的原始 IP 地址）。
- **User-Name** - 客户端登录名。
- **MS-CHAP-Domain** - 用户域（如果存在）。
- **Mikrotik-Realm** - 如果在 /radius 菜单中设置，它将作为 Mikrotik-Realm 属性包含在每个 RADIUS 请求中。如果未设置，则发送与 MS-CHAP-Domain 属性相同的值（如果缺少 MS-CHAP-Domain，则也不包含 Realm）。
- **WISPr-Location-ID** - 在 HotSpot 服务器的 radius-location-id 属性中指定的文本字符串。
- **WISPr-Location-Name** - 在 HotSpot 服务器的 radius-location-name 属性中指定的文本字符串。
- **WISPr-Logoff-URL** - 指向注销页面的完整链接（例如，**[](http://10.48.0.1/lv/logout)**）。

根据认证方法（注意：HotSpot 默认使用 CHAP，如果启用了未加密密码，也可能使用 PAP，但不能使用 MSCHAP）：

- **User-Password** - 加密密码（用于 PAP 认证）。
- **CHAP-Password**， **CHAP-Challenge** - 加密密码和挑战值（用于 CHAP 认证）。
- **MS-CHAP-Response**， MS-CHAP-Challenge - 加密密码和挑战值（用于 MS-CHAPv1 认证）。
- **MS-CHAP2-Response**， **MS-CHAP-Challenge** - 加密密码和挑战值（用于 MS-CHAPv2 认证）。

### Access-Accept 数据包

- **Framed-IP-Address** - 分配给客户端的 IP 地址。如果该地址属于 127.0.0.0/8 或 224.0.0.0/3 网络，则使用默认配置文件中的 IP 池来分配客户端 IP 地址。如果指定了 Framed-IP-Address，则忽略 Framed-Pool。
- **Framed-IP-Netmask** - 客户端子网掩码。PPPs - 如果指定，将通过 Framed-IP-Address 网关创建一条指向 Framed-IP-Address 所属网络的路由；HotSpot - HotSpot 忽略此属性。
- **Framed-Pool** - 用于为客户端获取 IP 地址的（路由器上的）IP 池名称。如果指定了 Framed-IP-Address，则忽略此属性。
- **Framed-IPv6-Prefix** - 分配给客户端的 IPv6 前缀。
- **Mikrotik-Delegated-IPv6-Pool** - 用于前缀委派的 IPv6 池。
- **Delegated-IPv6-Prefix** - IPv6 前缀。
- **Delegated-IPv6-Prefix-Pool** - 用于前缀委派的 IPv6 前缀池。

注意：如果指定了 Framed-IP-Address 或 Framed-Pool，它将覆盖默认配置中的 remote-address。

- **Idle-Timeout** - 覆盖默认配置中的 idle-timeout。
- **Session-Timeout** - 覆盖默认配置中的 session-timeout。
- **Port-Limit** - 使用相同用户名进行并发连接的最大数量（覆盖 HotSpot 用户配置文件的 shared-users 属性）。
- **Class** - Cookie。将原样包含在 Accounting-Request 中。
- **Framed-Route** - 在服务器上添加的路由。格式在 RFC 2865（第 5.22 章）中规定。可以根据需要多次指定。
- **Filter-Id** - 防火墙过滤链名称。用于创建动态防火墙规则。防火墙链名称可以带有 .in 或 .out 后缀，这将仅为传入或传出流量安装规则。可以提供多个 Filter-id，但仅使用最后传入和传出的规则。对于 PPPs - ppp 链中的过滤规则，如果数据包来自/发往客户端，将跳转到指定链（这意味着您应该首先创建 ppp 链并创建跳转规则，将实际流量放入此链）。HotSpot 同理，但规则将在 hotspot 链中创建。
- **Mikrotik-Mark-Id** - 防火墙 mangle 链名称（仅限 HotSpot）。MikroTik RADIUS 客户端收到此属性后，会创建一条动态防火墙 mangle 规则，action=jump chain=hotspot，jump-target 等于属性值。Mangle 链名称可以带有 .in 或 .out 后缀，这将仅为传入或传出流量安装规则。可以提供多个 Mark-id 属性，但仅使用最后传入和传出的规则。
- **Acct-Interim-Interval** - RADIUS 客户端的临时更新。PPP - 如果为 0，则使用 RADIUS 客户端中指定的值。HotSpot - 仅在 HotSpot 服务器配置文件中 radius-interim-update=received 时生效。
- **MS-MPPE-Encryption-Policy** - Require-encryption 属性（仅限 PPPs）。
- **MS-MPPE-Encryption-Types** - Use-encryption 属性。非零值表示使用加密（仅限 PPPs）。
- **Ascend-Data-Rate** - 如果提供多个属性，则限制 Tx/rx 数据速率，第一个限制 tx 数据速率，第二个限制 rx 数据速率。如果与 Ascend-Xmit-Rate 一起使用，则指定 rx 速率。0 表示无限制。如果存在 Rate-Limit 属性，则忽略此属性。
- **Ascend-Xmit-Rate** - Tx 数据速率限制。可用于仅指定 tx 限制，而不是发送两个连续的 Ascend-Data-Rate 属性（在这种情况下，Ascend-Data-Rate 将指定接收速率）。0 表示无限制。如果存在 Rate-Limit 属性，则忽略此属性。
- **MS-CHAP2-Success** - 如果使用了 MS-CHAPv2，则为认证响应（仅适用于 PPPs）。
- **MS-MPPE-Send-Key, MS-MPPE-Recv-Key** - 仅当使用 MS-CHAPv2 作为认证方式时，RADIUS 服务器才提供的加密 PPPs 的加密密钥（仅适用于 PPPs）。
- **Ascend-Client-Gateway** - 用于 DHCP-pool HotSpot 登录方式的客户端网关（仅限 HotSpot）。
- **Mikrotik-Recv-Limit** - 客户端的接收总限制（字节）。
- **Mikrotik-Recv-Limit-Gigawords** - 接收总限制的 4G (2^32) 字节部分（第 32..63 位，当第 0..31 位在 Mikrotik-Recv-Limit 中传递时）。
- **Mikrotik-Xmit-Limit** - 客户端的发送总限制（字节）。
- **Mikrotik-Xmit-Limit-Gigawords** - 发送总限制的 4G (2^32) 字节部分（第 32..63 位，当第 0..31 位在 Mikrotik-Xmit-Limit 中传递时）。
- **Mikrotik-Wireless-Forward** - 如果此属性设置为 "0"，则不将客户端的帧转发回无线基础设施（仅限无线）。
- **Mikrotik-Wireless-Skip-Dot1x** - 如果设置为非零值，则对特定无线客户端禁用 802.1x 认证（仅限无线）。
- **Mikrotik-Wireless-Enc-Algo** - WEP 加密算法：0 - 无加密，1 - 40 位 WEP，2 - 104 位 WEP（仅限无线）。
- **Mikrotik-Wireless-Enc-Key** - 客户端的 WEP 加密密钥（仅限无线）。
- **Mikrotik-Wireless-VLANID** - 客户端的 VLAN ID（仅限无线）。
- **Mikrotik-Wireless-VLANID-type** - 客户端的 VLAN ID 类型。0 - 802.1q 标签，1 - 802.1ad 标签（仅限无线）。
- **Mikrotik-Switching-Filter** - 允许在使用 dot1x 服务器认证客户端时创建动态交换规则。
- **Mikrotik-Rate-Limit** - 客户端的速率限制。格式为： rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]，从路由器的角度来看（因此 "rx" 是客户端上传，"tx" 是客户端下载）。所有速率应为数字，可带有 'k'（千）或 'M'（百万）后缀。如果未指定 tx-rate，则 rx-rate 也用作 tx-rate。tx-burst-rate 和 tx-burst-threshold 以及 tx-burst-time 同理。如果 rx-burst-threshold 和 tx-burst-threshold 均未指定（但指定了 burst-rate），则使用 rx-rate 和 tx-rate 作为突发阈值。如果 rx-burst-time 和 tx-burst-time 均未指定，则默认使用 1s。优先级取值 1..8，其中 1 表示最高优先级，8 表示最低。如果未指定 rx-rate-min 和 tx-rate-min，则使用 rx-rate 和 tx-rate 的值。rx-rate-min 和 tx-rate-min 的值不能超过 rx-rate 和 tx-rate 的值。
- **Mikrotik-Group** - 本地用户的路由器本地用户组名称（在 `/user/group` 中定义）；HotSpot 用户的 HotSpot 默认配置文件；PPP 用户的 PPP 默认配置文件名称。
- **Mikrotik-Advertise-URL** - 应向客户端显示的广告页面 URL。如果指定了此属性，广告将自动启用，包括透明代理，即使在相应用户配置文件中明确禁用也是如此。RADIUS 服务器可以发送多个属性实例以指定其他 URL，这些 URL 将以轮询方式选择。
- **Mikrotik-Advertise-Interval** - 两个相邻广告之间的时间间隔。RADIUS 服务器可以发送多个属性实例以指定其他间隔。所有间隔值被视为一个列表，每次成功广告后依次取用。如果到达列表末尾，则继续使用最后一个值。
- **WISPr-Redirection-URL** - 客户端成功登录后将重定向到的 URL。
- **WISPr-Bandwidth-Min-Up** - 为客户端上传提供的最小数据速率（CIR）。
- **WISPr-Bandwidth-Min-Down** - 为客户端下载提供的最小数据速率（CIR）。
- **WISPr-Bandwidth-Max-Up** - 为客户端上传提供的最大数据速率（MIR）。
- **WISPr-Bandwidth-Max-Down** - 为客户端下载提供的最大数据速率（MIR）。
- **WISPr-Session-Terminate-Time** - 用户应断开连接的时间；格式为 "YYYY-MM-DDThh:mm:ssTZD"，其中 Y - 年；M - 月；D - 日；T - 分隔符（必须写在日期和时间之间）；h - 小时（24 小时制）；m - 分钟；s - 秒；TZD - 时区，格式为以下之一： "+hh:mm", "+hhmm", "-hh:mm", "-hhmm"。

接收到的属性会覆盖默认属性（在默认配置文件中设置），但如果未从 RADIUS 服务器接收到某个属性，则使用默认值。Rate-Limit 优先于所有其他指定客户端数据速率的方式。Ascend 数据速率属性次之；WISPr 属性优先级最低。

以下是一些 Rate-Limit 示例：

- **128k** - rx-rate=128000, tx-rate=128000（无突发）。
- **64k/128M** - rx-rate=64000, tx-rate=128000000。
- **64k 256k** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=64000, rx/tx-burst-time=1s。
- **64k/64k 256k/256k 128k/128k 10/10** - rx/tx-rate=64000, rx/tx-burst-rate=256000, rx/tx-burst-threshold=128000, rx/tx-burst-time=10s。

### Accounting-Request 数据包

计费请求携带与 Access Request 相同的属性，外加以下属性：

- **Acct-Status-Type** - Start、Stop 或 Interim-Update。
- **Acct-Authentic** - 由 RADIUS 或本地权威机构认证（仅适用于 PPPs）。
- **Class** - RADIUS 服务器 cookie，如在 Access-Accept 中接收到的。
- **Acct-Delay-Time** - 路由器尝试发送此 Accounting-Request 数据包的时间。

### Stop 和 Interim-Update Accounting-Request 数据包

除了计费开始请求外，以下消息将包含以下属性：

- **Acct-Session-Time** - 连接在线时长（秒）。
- **Acct-Input-Octets** - 从客户端接收的字节数。
- **Acct-Input-Gigawords** - 从客户端接收的 4G (2^32) 字节部分（第 32..63 位，当第 0..31 位在 Acct-Input-Octets 中传递时）。
- **Acct-Input-Packets** - 从客户端接收的数据包数量。
- **Acct-Output-Octets** - 发送给客户端的字节数。
- **Acct-Output-Gigawords** - 发送给客户端的 4G (2^32) 字节部分（第 32..63 位，当第 0..31 位在 Acct-Output-Octets 中传递时）。
- **Acct-Output-Packets** - 发送给客户端的数据包数量。

:::warning
RouterOS 中的 RADIUS 计费消息将输出表示为从客户端角度看的流量，例如，对于 VPN 用户 "test"，输出是用户上传。

:::

### **Stop Accounting-Request 数据包**

这些数据包除了包含 Interim Update 数据包的内容外，还将包含：

- **Acct-Terminate-Cause** - 会话终止原因（参见 RFC 2866 第 5.10 章）
  
  ### **授权变更**

RADIUS 断开连接和授权变更（根据 RFC3576）也受支持。以下属性可以通过 RADIUS 服务器的 CoA 请求进行更改：

- **Mikrotik-Group**
- **Mikrotik-Recv-Limit**
- **Mikrotik-Xmit-Limit**
- **Mikrotik-Rate-Limit**
- **Ascend-Data-Rate**（仅当不存在 Mikrotik-Rate-Limit 时）
- **Ascend-XMit-Rate**（仅当不存在 Mikrotik-Rate-Limit 时）
- **Mikrotik-Mark-Id**
- **Filter-Id**
- **Mikrotik-Advertise-Url**
- **Mikrotik-Advertise-Interval**
- **Session-Timeout**
- **Idle-Timeout**
- **Port-Limit**

请注意，无法通过这种方式更改 IP 地址、池或路由 - 要进行此类更改，必须先断开用户连接。

## MikroTik 特定 RADIUS 属性数值

| 名称                                    | VendorID | 值 | RFC |
|:-- | --:| --:|:-- |
| **MIKROTIK\_RECV\_LIMIT**               | 14988    | 1     |     |
| **MIKROTIK\_XMIT\_LIMIT**               | 14988    | 2     |     |
| **MIKROTIK\_GROUP**                     | 14988    | 3     |     |
| **MIKROTIK\_WIRELESS\_FORWARD**         | 14988    | 4     |     |
| **MIKROTIK\_WIRELESS\_SKIPDOT1X**       | 14988    | 5     |     |
| **MIKROTIK\_WIRELESS\_ENCALGO**         | 14988    | 6     |     |
| **MIKROTIK\_WIRELESS\_ENCKEY**          | 14988    | 7     |     |
| **MIKROTIK\_RATE\_LIMIT**               | 14988    | 8     |     |
| **MIKROTIK\_REALM**                     | 14988    | 9     |     |
| **MIKROTIK\_HOST\_IP**                  | 14988    | 10    |     |
| **MIKROTIK\_MARK\_ID**                  | 14988    | 11    |     |
| **MIKROTIK\_ADVERTISE\_URL**            | 14988    | 12    |     |
| **MIKROTIK\_ADVERTISE\_INTERVAL**       | 14988    | 13    |     |
| **MIKROTIK\_RECV\_LIMIT\_GIGAWORDS**    | 14988    | 14    |     |
| **MIKROTIK\_XMIT\_LIMIT\_GIGAWORDS**    | 14988    | 15    |     |
| **MIKROTIK\_WIRELESS\_PSK**             | 14988    | 16    |     |
| **MIKROTIK\_TOTAL\_LIMIT**              | 14988    | 17    |     |
| **MIKROTIK\_TOTAL\_LIMIT\_GIGAWORDS**   | 14988    | 18    |     |
| **MIKROTIK\_ADDRESS\_LIST**             | 14988    | 19    |     |
| **MIKROTIK\_WIRELESS\_MPKEY**           | 14988    | 20    |     |
| **MIKROTIK\_WIRELESS\_COMMENT**         | 14988    | 21    |     |
| **MIKROTIK\_DELEGATED\_IPV6\_POOL**     | 14988    | 22    |     |
| **MIKROTIK\_DHCP\_OPTION\_SET**         | 14988    | 23    |     |
| **MIKROTIK\_DHCP\_OPTION\_PARAM\_STR1** | 14988    | 24    |     |
| **MIKROTIK\_DHCP\_OPTION\_PARAM\_STR2** | 14988    | 25    |     |
| **MIKROTIK\_WIRELESS\_VLANID**          | 14988    | 26    |     |
| **MIKROTIK\_WIRELESS\_VLANIDTYPE**      | 14988    | 27    |     |
| **MIKROTIK\_WIRELESS\_MINSIGNAL**       | 14988    | 28    |     |
| **MIKROTIK\_WIRELESS\_MAXSIGNAL**       | 14988    | 29    |     |
| **Mikrotik-Switching-Filter** | 14988 | 30 |

## 所有支持的属性数值

| 名称                                   | VendorID | 值 | RFC                           |
|:-- |:-- | --:|:-- |
| **Acct-Authentic**                     |          | 45    | RFC 2866                      |
| **Acct-Delay-Time**                    |          | 41    | RFC 2866                      |
| **Acct-Input-Gigawords**               |          | 52    | RFC 2869                      |
| **Acct-Input-Octets**                  |          | 42    | RFC 2866                      |
| **Acct-Input-Packets**                 |          | 47    | RFC 2866                      |
| **Acct-Interim-Interval**              |          | 85    | RFC 2869                      |
| **Acct-Output-Gigawords**              |          | 53    | RFC 2869                      |
| **Acct-Output-Octets**                 |          | 43    | RFC 2866                      |
| **Acct-Output-Packets**                |          | 48    | RFC 2866                      |
| **Acct-Session-Id**                    |          | 44    | RFC 2866                      |
| **Acct-Session-Time**                  |          | 46    | RFC 2866                      |
| **Acct-Status-Type**                   |          | 40    | RFC 2866                      |
| **Acct-Terminate-Cause**               |          | 49    | RFC 2866                      |
| **Ascend-Client-Gateway**              | 529      | 132   |                               |
| **Ascend-Data-Rate**                   | 529      | 197   |                               |
| **Ascend-Xmit-Rate**                   | 529      | 255   |                               |
| **Called-Station-Id**                  |          | 30    | RFC 2865                      |
| **Calling-Station-Id**                 |          | 31    | RFC 2865                      |
| **CHAP-Challenge**                     |          | 60    | RFC 2866                      |
| **CHAP-Password**                      |          | 3     | RFC 2865                      |
| **Class**                              |          | 25    | RFC 2865                      |
| **Filter-Id**                          |          | 11    | RFC 2865                      |
| **Framed-Compression**                 |          | 13    | RFC 2865                      |
| **Framed-IP-Address**                  |          | 8     | RFC 2865                      |
| **Framed-IP-Netmask**                  |          | 9     | RFC 2865                      |
| **Framed-IPv6-Prefix**                 |          | 97    | RFC 3162                      |
| **Framed-Mtu**                         |          | 12    | RFC 2865                      |
| **Framed-Pool**                        |          | 88    | RFC 2869                      |
| **Framed-Protocol**                    |          | 7     | RFC 2865                      |
| **Framed-Route**                       |          | 22    | RFC 2865                      |
| **Framed-Routing**                     |          | 10    | RFC 2865                      |
| **Idle-Timeout**                       |          | 28    | RFC 2865                      |
| **MS-CHAP-Challenge**                  | 311      | 11    | RFC 2548                      |
| **MS-CHAP-Domain**                     | 311      | 10    | RFC 2548                      |
| **MS-CHAP-Response**                   | 311      | 1     | RFC 2548                      |
| **MS-CHAP2-Response**                  | 311      | 25    | RFC 2548                      |
| **MS-CHAP2-Success**                   | 311      | 26    | RFC 2548                      |
| **MS-MPPE-Encryption-Policy**          | 311      | 7     | RFC 2548                      |
| **MS-MPPE-Encryption-Types**           | 311      | 8     | RFC 2548                      |
| **MS-MPPE-Recv-Key**                   | 311      | 17    | RFC 2548                      |
| **MS-MPPE-Send-Key**                   | 311      | 16    | RFC 2548                      |
| **NAS-Identifier**                     |          | 32    | RFC 2865                      |
| **NAS-Port**                           |          |