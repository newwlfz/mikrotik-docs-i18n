# 用户管理器

> RouterOS 中的用户管理器为 DHCP、Hotspot 和 PPP 等服务提供集中的 RADIUS 认证和授权，支持多种认证方法。它包含可自定义的 RADIUS 属性，用于隧道配置和会话管理，许可证级别会影响活动会话数。

# 用户管理器

## 概述

用户管理器是 RouterOS 中实现的 RADIUS 服务器，为特定服务提供集中的用户认证和授权。集中的用户数据库可以更好地跟踪系统用户和客户。作为一个独立的软件包，用户管理器适用于除 SMIPS 之外的所有架构；但需注意可用空间有限。它支持多种认证方法，包括 PAP、CHAP、MS-CHAP、MS-CHAPv2、EAP-TLS、EAP-TTLS 和 EAP-PEAP。在 RouterOS 中，DHCP、Dot1x、Hotspot、IPsec、PPP 和 Wireless 是受益于用户管理器最多的功能。每个用户都可以通过 WEB 界面查看其账户统计信息并管理可用的配置文件。此外，用户可以使用最流行的支付网关 - PayPal 购买自己的数据套餐（配置文件），使其成为服务提供商的绝佳系统。可以生成自定义报告，方便计费部门处理。用户管理器遵循 [RFC2865](https://tools.ietf.org/html/rfc2865) 和 [RFC3579](https://tools.ietf.org/html/rfc3579) 中定义的 RADIUS 标准。

用户管理器是受 RouterOS 许可证级别限制的功能之一。根据[许可证级别](../getting-started/routeros-licensing/x86/index.md#routeros-license-key-levels)，活动会话数将受到限制，包括每个用户的多个连接（非唯一账户）。

![](https://manual.mikrotik.com/docs/authentication-authorization-accounting/img/user-manager-01.webp)

## 属性

**子菜单：** `/user-manager/attribute`

RADIUS 属性是定义授权、信息和配置参数的，在 RADIUS 服务器和客户端之间传递。用户管理器允许发送在“属性”菜单中定义的自定义属性。RouterOS 已有一组预定义的属性，但如有必要，也可以添加额外的属性。预定义属性：

| 属性 | 厂商 ID | 类型 ID | 值类型 | 数据包类型 | 描述 |
| :-- | :-- | --: | :-- | :-- | :-- |
| Framed-IP-Address | 0（标准） | 8 | ip address | Access-Accept | [RFC2865 第 5.8 节](https://tools.ietf.org/html/rfc2865#section-5.8) |
| Framed-IP-Netmask | 0（标准） | 9 | `/ip/address` | Access-Accept | [RFC2865 第 5.9 节](https://tools.ietf.org/html/rfc2865#section-5.9) |
| Session-Timeout | 0（标准） | 27 | integer（最大值：21474720） | Access-Accept, Access-Challenge | [RFC2865 第 5.27 节](https://tools.ietf.org/html/rfc2865#section-5.27) |
| Idle-Timeout | 0（标准） | 28 | integer | Access-Accept, Access-Challenge | [RFC2865 第 5.28 节](https://tools.ietf.org/html/rfc2865#section-5.28) |
| Tunnel-Type | 0（标准） | 64 |  | 值 | 描述 |  | --------: | :----------------------------------------------------------- |  | 1 | 点对点隧道协议（PPTP） |  | 2 | 第二层转发（L2F） |  | 3 | 第二层隧道协议（L2TP） |  | 4 | Ascend 隧道管理协议（ATMP） |  | 5 | 虚拟隧道协议（VTP） |  | 6 | 隧道模式下的 IP 认证头（AH） |  | 7 | IP-in-IP 封装（IP-IP） |  | 8 | 最小 IP-in-IP 封装（MIN-IP-IP） |  | 9 | 隧道模式下的 IP 封装安全载荷（ESP） |  | 10 | 通用路由封装（GRE） |  | 11 | Bay 拨号虚拟服务（DVS） |  | 12 | IP-in-IP 隧道 |  | 13 | 虚拟局域网 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 1 | 点对点隧道协议（PPTP） |  |  |  |  |
| 2 | 第二层转发（L2F） |  |  |  |  |
| 3 | 第二层隧道协议（L2TP） |  |  |  |  |
| 4 | Ascend 隧道管理协议（ATMP） |  |  |  |  |
| 5 | 虚拟隧道协议（VTP） |  |  |  |  |
| 6 | 隧道模式下的 IP 认证头（AH） |  |  |  |  |
| 7 | IP-in-IP 封装（IP-IP） |  |  |  |  |
| 8 | 最小 IP-in-IP 封装（MIN-IP-IP） |  |  |  |  |
| 9 | 隧道模式下的 IP 封装安全载荷（ESP） |  |  |  |  |
| 10 | 通用路由封装（GRE） |  |  |  |  |
| 11 | Bay 拨号虚拟服务（DVS） |  |  |  |  |
| 12 | IP-in-IP 隧道 |  |  |  |  |
| 13 | 虚拟局域网 |  |  |  |  |
| Tunnel-Medium-Type | 0（标准） | 65 |  | 值 | 描述 |  | --------: | :-------------------------------------------------------------- |  | 1 | IPv4（IP 版本 4） |  | 2 | IPv6（IP 版本 6） |  | 3 | NSAP |  | 4 | HDLC（8 位多点） |  | 5 | BBN 1822 |  | 6 | 802（包括所有 802 介质以及以太网“规范格式”） |  | 7 | E.163（POTS） |  | 8 | E.164（SMDS、Frame Relay、ATM） |  | 9 | F.69（Telex） |  | 10 | X.121（X.25、Frame Relay） |  | 11 | IPX |  | 12 | Appletalk |  | 13 | Decnet IV |  | 14 | Banyan Vines |  | 15 | 带 NSAP 格式子地址的 E.164 |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 1 | IPv4（IP 版本 4） |  |  |  |  |
| 2 | IPv6（IP 版本 6） |  |  |  |  |
| 3 | NSAP |  |  |  |  |
| 4 | HDLC（8 位多点） |  |  |  |  |
| 5 | BBN 1822 |  |  |  |  |
| 6 | 802（包括所有 802 介质以及以太网“规范格式”） |  |  |  |  |
| 7 | E.163（POTS） |  |  |  |  |
| 8 | E.164（SMDS、Frame Relay、ATM） |  |  |  |  |
| 9 | F.69（Telex） |  |  |  |  |
| 10 | X.121（X.25、Frame Relay） |  |  |  |  |
| 11 | IPX |  |  |  |  |
| 12 | Appletalk |  |  |  |  |
| 13 | Decnet IV |  |  |  |  |
| 14 | Banyan Vines |  |  |  |  |
| 15 | 带 NSAP 格式子地址的 E.164 |  |  |  |  |
| Tunnel-Private-Group-ID | 0（标准） | 81 | string | Access-Accept | [RFC2868 第 3.6 节](https://tools.ietf.org/html/rfc2868#section-3.6) |
| Framed-Pool | 0（标准） | 88 | string | Access-Accept | [RFC2869 第 5.18 节](https://tools.ietf.org/html/rfc2869#section-5.18) |
| Framed-IPv6-Prefix | 0（标准） | 97 | ipv6 prefix | Access-Accept | [RFC3162 第 2.3 节](https://tools.ietf.org/html/rfc3162#section-2.3) |
| Framed-IPv6-Pool | 0（标准） | 100 | string | Access-Accept | [RFC3162 第 2.6 节](https://tools.ietf.org/html/rfc3162#section-2.6) |
| Delegated-IPv6-Prefix | 0（标准） | 123 | ipv6 prefix | Access-Accept | [RFC4818](https://tools.ietf.org/html/rfc4818) |
| Framed-IPv6-Address | 0（标准） | 168 | ip address | Access-Accept | [RFC6911 第 3.1 节](https://tools.ietf.org/html/rfc6911#section-3.1) |
| Mikrotik-Recv-Limit | 14988（Mikrotik） | 1 | integer | Access-Accept | 客户端的接收总限制（字节）。 |
| Mikrotik-Xmit-Limit | 14988（Mikrotik） | 2 | integer | Access-Accept | 客户端的发送总限制（字节）。 |
| Mikrotik-Group | 14988（Mikrotik） | 3 | string | Access-Accept | 本地用户的用户组。HotSpot 用户的 HotSpot 配置文件。PPP 用户的 PPP 配置文件。 |
| Mikrotik-Wireless-Forward | 14988（Mikrotik） | 4 | integer | Access-Accept | 如果此属性设置为“0”，则不将客户端的帧转发回无线基础设施（仅限无线）。 |
| Mikrotik-Wireless-Skip-Dot1x | 14988（Mikrotik） | 5 | integer | Access-Accept | 如果设置为非零值，则禁用特定无线客户端的 802.1x 认证（仅限无线）。 |
| Mikrotik-Wireless-Enc-Algo | 14988（Mikrotik） | 6 |  | 值 | 描述 |  | --------: | :-------------- |  | 0 | 无加密 |  | 1 | 40 位 WEP |  | 2 | 104 位 WEP |  | 3 | AES-CCM |  | 4 | TKIP |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 0 | 无加密 |  |  |  |  |
| 1 | 40 位 WEP |  |  |  |  |
| 2 | 104 位 WEP |  |  |  |  |
| 3 | AES-CCM |  |  |  |  |
| 4 | TKIP |  |  |  |  |
| Mikrotik-Wireless-Enc-Key | 14988（Mikrotik） | 7 | string | Access-Accept | 客户端的 WEP 加密密钥（仅限无线）。 |
| Mikrotik-Rate-Limit | 14988（Mikrotik） | 8 | string | Access-Accept | 客户端的数据速率限制。格式为：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]，从路由器的角度来看（因此“rx”是客户端上传，“tx”是客户端下载）。所有速率应为数字，可选用 'k'（千）或 'M'（百万）后缀。如果未指定 tx-rate，则 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果未指定 rx-burst-threshold 和 tx-burst-threshold（但指定了 burst-rate），则使用 rx-rate 和 tx-rate 作为突发阈值。如果未指定 rx-burst-time 和 tx-burst-time，则默认使用 1 秒。优先级取值为 1..8，其中 1 表示最高优先级，8 表示最低优先级。如果未指定 rx-rate-min 和 tx-rate-min，则使用 rx-rate 和 tx-rate 的值。rx-rate-min 和 tx-rate-min 的值不能超过 rx-rate 和 tx-rate 的值。 |
| Mikrotik-Realm | 14988（Mikrotik） | 9 | string | Access-Request | 如果在 /radius 菜单中设置，则作为 Mikrotik-Realm 属性包含在每个 RADIUS 请求中。如果未设置，则发送与 MS-CHAP-Domain 属性相同的值（如果缺少 MS-CHAP-Domain，则也不包含 Realm）。 |
| Mikrotik-Host-IP | 14988（Mikrotik） | 10 | ip address | Access-Request | 通用客户端转换之前 HotSpot 客户端的 IP 地址（客户端的原始 IP 地址）。 |
| Mikrotik-Mark-Id | 14988（Mikrotik） | 11 | string | Access-Accept | 防火墙 mangle 链名称（仅限 HotSpot）。MikroTik RADIUS 客户端收到此属性后，会创建一条动态防火墙 mangle 规则，action=jump chain=hotspot，jump-target 等于属性值。Mangle 链名称可以带有 .in 或 .out 后缀，这将仅对入站或出站流量安装规则。可以提供多个 Mark-id 属性，但仅使用入站和出站的最后一个。 |
| Mikrotik-Advertise-URL | 14988（Mikrotik） | 12 | string | Access-Accept | 应向客户端显示的广告页面的 URL。如果指定了此属性，则自动启用广告，包括透明代理，即使在相应的用户配置文件中明确禁用了广告也是如此。RADIUS 服务器可以发送多个属性实例以指定额外的 URL，这些 URL 以轮询方式选择。 |
| Mikrotik-Advertise-Interval | 14988（Mikrotik） | 13 | integer | Access-Accept | 两个相邻广告之间的时间间隔。RADIUS 服务器可以发送多个属性实例以指定额外的间隔。所有间隔值被视为一个列表，每次成功广告后依次取用。如果到达列表末尾，则继续使用最后一个值。 |
| Mikrotik-Recv-Limit-Gigawords | 14988（Mikrotik） | 14 | integer | Access-Accept | 接收总限制的 4G（2^32）字节（第 32..63 位，当第 0..31 位在 Mikrotik-Recv-Limit 中传递时）。 |
| Mikrotik-Xmit-Limit-Gigawords | 14988（Mikrotik） | 15 | integer | Access-Accept | 发送总限制的 4G（2^32）字节（第 32..63 位，当第 0..31 位在 Mikrotik-Xmit-Limit 中传递时）。 |
| Mikrotik-Wireless-PSK | 14988（Mikrotik） | 16 | string | Access-Accept |  |
| Mikrotik-Total-Limit | 14988（Mikrotik） | 17 | integer | Access-Accept |  |
| Mikrotik-Total-Limit-Gigawords | 14988（Mikrotik） | 18 | integer | Access-Accept |  |
| Mikrotik-Address-List | 14988（Mikrotik） | 19 | string | Access-Accept |  |
| Mikrotik-Wireless-MPKey | 14988（Mikrotik） | 20 | string | Access-Accept |  |
| Mikrotik-Wireless-Comment | 14988（Mikrotik） | 21 | string | Access-Accept |  |
| Mikrotik-Delegated-IPv6-Pool | 14988（Mikrotik） | 22 | string | Access-Accept | 用于前缀委派的 IPv6 地址池。 |
| Mikrotik-DHCP-Option-Set | 14988（Mikrotik） | 23 | string | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR1 | 14988（Mikrotik） | 24 | string | Access-Accept |  |
| Mikrotik-DHCP-Option-Param-STR2 | 14988（Mikrotik） | 25 | string | Access-Accept |  |
| Mikrotik-Wireless-VLANID | 14988（Mikrotik） | 26 | integer | Access-Accept | 客户端的 VLAN ID（仅限无线）。 |
| Mikrotik-Wireless-VLANIDtype | 14988（Mikrotik） | 27 |  | 值 | 描述 |  | --------: | :-------------- |  | 0 | 802.1q |  | 1 | 802.1ad |  | 值 | 描述 |
| 值 | 描述 |  |  |  |  |
| 0 | 802.1q |  |  |  |  |
| 1 | 802.1ad |  |  |  |  |
| Mikrotik-Wireless-Minsignal | 14988（Mikrotik） | 28 | string | Access-Accept |  |
| Mikrotik-Wireless-Maxsignal | 14988（Mikrotik） | 29 | string | Access-Accept |  |
| Mikrotik-Switching-Filter | 14988（Mikrotik） | 30 | string | Access-Accept | 允许在使用 dot1x 服务器认证客户端时创建动态交换规则。 |

**属性**

| 属性 | 描述 |
| :-- | :-- |
| **name** (*string*；默认：) | 属性的名称。 |
| **packet-types** (*string*；默认：**access-accept**) | access-accept - 在 RADIUS Access-Accept 消息中使用此属性access-challenge - 在 RADIUS Access-Challenge 消息中使用此属性 |
| **type-id** (*integer:1..255*；默认：) | 来自特定厂商属性数据库的属性标识号。 |
| **value-type** (*string*；默认：) | hexip-address - IPv4 或 IPv6 IP 地址ip6-prefix - IPv6 前缀macrostringuint32 |
| **vendor-id** (*integer*；默认：**0**) | IANA 分配的特定企业标识号。 |

## 数据库

**子菜单：** `/user-manager/database`

所有与 RADIUS 相关的信息都存储在单独的 User Manager 数据库中，可在“数据库”子菜单下配置。“Enabled”和“db-path”是仅有的两个不存储在 User Manager 数据库中，而是存储在主 RouterOS 配置表中的参数，这意味着这些参数将受到 RouterOS 配置重置的影响。其余的配置、会话和支付数据存储在设备 FLASH 存储上的单独 SQLite 数据库中。在对数据库执行任何操作时，建议在任何活动之前和之后进行备份。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **db-path** (*string*；默认：) | 数据库文件存储位置的路径。 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **db-size** | 数据库的当前大小。 |
| **free-disk-space** | 存储数据库的磁盘上的剩余空间。 |

### 命令

| 属性 | 描述 |
| :-- | :-- |
| **load** (*name*) | 恢复以前创建的 .umb 格式备份文件。 |
| **migrate-legacy-db** (*database-path; overwrite*) | 将旧版 User Manager（来自 RouterOS v6 或更早版本）转换为新标准。可以覆盖当前数据库。 |
| **optimize-db** () |  |
| **save** (name; overwrite) | 保存 User Manager 数据库的当前状态。 |

## 限制

**子菜单：** `/user-manager/limitation`

限制由配置文件使用，并通过配置文件-限制关联在一起。必须启用 RADIUS 计费和临时更新，才能在达到 *download-limit*、*upload-limit* 或 *uptime-limit* 时无缝切换多个限制或断开活动会话。

要从 User Manager 断开已活动的会话，RADIUS 客户端侧的 *accept* 必须设置为 *yes*。如果同时会话限制不是无限制的（shared-users），并且已达到允许的最大数量，则路由器将首先尝试断开较旧的用户会话。

User-Manager 尝试在接受新用户之前断开活动会话（当设置了适当的限制时）。这就是为什么在此类设置中建议对 `/radius/client/timeout` 使用 1 秒。

:::danger
RouterOS 中的 IPsec 服务不支持速率限制。

:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*string*；默认：) | 限制的简短描述。 |
| **download-limit** (*integer*；默认：**0**) | 用户可下载的总流量（字节）。 |
| **name** (*string*；默认：) | 限制的唯一名称。 |
| **rate-limit-burst-rx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-threshold-rx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-threshold-tx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-time-rx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-time-tx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-burst-tx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-min-rx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-min-tx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-priority** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-rx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **rate-limit-tx** () | *MT-Rate-Limit* RADIUS 属性的一部分。请参阅 [Queues#SimpleQueue](../firewall-and-quality-of-service/queues/index.md)。 |
| **reset-counters-interval** (*hourly* \| *daily* \| *weekly* \| *monthly* \| *disabled*); 默认：**disabled**) | 从 *reset-counters-start-time* 开始的时间间隔，所有关联的用户统计信息在此间隔后被清除。 |
| **reset-counters-start-time** (*datetime*；默认：) | 计算 *reset-counters-interval* 的静态日期和时间值。 |
| **transfer-limit** (*integer*；默认：**0**) | 聚合（下载+上传）总流量（字节）。 |
| **upload-limit** (*integer*；默认：**0**) | 用户可上传的总流量（字节）。 |
| **uptime-limit** (*time*；默认：**00:00:00**) | 用户可保持活动的总在线时间。 |

## 支付

**子菜单：** `/user-manager/payment`

本节提供所有已收到支付的信息。

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **currency** (*string*) | 交易中使用的货币。 |
| **method** (*string*) | 用于交易的服务（目前仅 PayPal）。 |
| **price** (*decimal*) | 用户支付的金额。 |
| **profile** (*profile*) | 用户购买的配置文件的名称。 |
| **trans-end** (*datetime*) | 交易结束的日期和时间。 |
| **trans-start** (*datetime*) | 交易开始的日期和时间。 |
| **trans-status** (*string*) | 交易的状态。可能的状态 - *started*、*pending*、*approved*、*declined*、*error*、*timeout*、*aborted*、*user approved*。只有 *approved* 应被视为完整交易。 |
| **user** (*string*；默认：) | 执行交易的用户的名称。 |
| **user-message** (*string*；默认：) |  |

## 配置文件

**子菜单：** `/user-manager/profile`

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*string*；默认：) | 条目的简短描述。 |
| **name** (*string*；默认：) | 配置文件的唯一名称。 |
| **name-for-users** (*string*；默认：) | 在网页上向用户显示的配置文件名称。 |
| **override-shared-users** (*decimal \| off \| unlimited*；默认：**off**) | 是否允许同一用户名建立多个会话。这会覆盖 *shared-users* 设置。 |
| **price** (*decimal*；默认：**0.00**) |  |
| **starts-when** (*assigned* \| *first-auth*；默认：**assigned**) | 配置文件变为活动的时间。*Assigned* - 创建用户配置文件条目时立即生效。*First-auth* - 用户首次认证请求时生效。 |
| **validity** (*time \| unlimited*；默认：**unlimited**) | 用户可以使用此配置文件的总时间。 |

## 配置文件限制

**子菜单：** `/user-manager/profile-limitation`

配置文件-限制表将限制和配置文件关联在一起，并定义其有效期。当多个限制分配给同一配置文件时，用户必须满足所有限制才能建立会话。这允许创建更复杂的设置，例如，单独的每月和每日带宽限制。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*string*；默认：) | 条目的简短描述。 |
| **from-time** (*time*；默认：**00:00:00**) | 限制应开始的时间。 |
| **limitation** (*limitation*；默认：) | 已创建的**限制**的名称。 |
| **profile** (*profile*；默认：) | 已创建的**配置文件**的名称。 |
| **till-time** (*time*；默认：**23:59:59**) | 限制应结束的时间。 |
| **weekdays** (*day of week*；默认：**Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday**) | 限制应生效的星期几。 |

## 路由器

**子菜单：** `/user-manager/router`

您可以在此定义可以使用 User Manager 作为 RADIUS 服务器的 NAS 设备。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **coa-port** (*integer:1..65535*；默认：**3799**) | CoA（授权变更）通信的端口号。 |
| **address** (*IP/IPv6***;** 默认：) | RADIUS 客户端的 IP 地址。 |
| **comment** (*string*；默认：) | NAS 的简短描述。 |
| **disabled** (*yes \| no*；默认：**no**) | 控制条目当前是否活动。 |
| **name** (*string*；默认：) | RADIUS 客户端的唯一名称。 |
| **protocol**(*radsec*\| *udp*;默认 udp) | 与路由器使用的协议。 |
| **shared-secret** (*string*；默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于保护 RADIUS 服务器和 RADIUS 客户端之间的通信。 |

### 命令

| 属性 | 描述 |
| :-- | :-- |
| **reset-counters** () | 清除特定 RADIUS 客户端的的所有统计信息。 |

## 会话

**子菜单：** `/user-manager/session`

仅在 NAS 上启用计费时才记录会话。

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **acct-session-id** (*string*) | 计费会话的唯一标识。 |
| **active** (*yes \| no*) | 会话当前是否正在使用。 |
| **calling-station-id** (*string*) | 用户标识符，通常是 IP 地址或 MAC 地址。 |
| **download** (*Bytes*) | 下载的流量量。 |
| **ended** (*datetime*) | 会话关闭的日期和时间。活动会话为空。 |
| **last-accounting-packet** (*datetime*) | 收到最后一次计费更新的日期和时间。 |
| **nas-ip-address** (*IP address*) | NAS 的 IP 地址。 |
| **nas-port-id** (*string*) | 正在认证用户的 NAS 端口标识符。 |
| **nas-port-type** (*string*) | 正在认证用户的端口类型（*physical* 或 *virtual*）。 |
| **started** (*datetime*) | 会话建立的日期和时间。 |
| **status** (*list of statuses*) | 会话的可能可用状态：*start -* 已收到计费消息 *Start*，*stop -* 已收到计费消息 *Stop*，*interim - 已收到临时更新*，*close-acked* - 会话已成功关闭，*expired.* |
| **terminate-cause** (*string*) | 会话关闭的原因。 |
| **upload** (*Bytes*) | 上传的流量量。 |
| **uptime** (*time*) | 会话上记录的总在线时间。 |
| **user** (*string*) | 用户的名称。 |
| **user-address** (*IP address*) | 提供给用户的 IP 地址。 |

## 设置

**子菜单：** `/user-manager`

**属性**

| 属性 | 描述 |
| :-- | :-- |
| **accounting-port** (*integer*；默认：**1813**) | 监听 RADIUS 计费请求的端口。 |
| **authentication-port**(*integer*；默认：**1812**) | 监听 RADIUS 认证请求的端口。 |
| ***certificate*** (*certificate*；默认：) | [来自证书库的证书](../authentication-authorization-accounting/certificates.md)，用于 EAP TLS 类型认证方法。 |
| ***enabled*** (*yes \| no*；默认：**no**) | User Manager 功能是否启用。 |
| **radsec-certificate**(certificate; 默认：) | [来自证书库的证书](../authentication-authorization-accounting/certificates.md)，用于 RadSec 协议。 |
| **use-profiles**(*yes \| no*；默认：**no**) | 是否使用**配置文件**和**限制**。设置为 *no* 时，仅需**用户**配置即可运行 User Manager。 |

### 高级

**子菜单：** `/user-manager/advanced`

**属性**

| 属性 | 描述 |
| :-- | :-- |
| **paypal-allow** (*yes \| no*；默认：**no**) | 是否为 User Manager 启用 PayPal 功能。 |
| **paypal-currency** (*string*；默认：**USD**) | 与 *price* 设置相关的货币，用户将以此货币计费。 |
| **paypal-password** (*string*；默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 您的 PayPal API 账户的密码。 |
| **paypal-signature** (*string*；默认：) | 您的 PayPal API 账户的签名。 |
| **paypal-use-sandbox** (*yes \| no*；默认：**no**) | 是否使用 PayPal 的沙盒环境进行测试。 |
| **paypal-user** (*string*；默认：) | 您的 PayPal API 账户的用户名。 |
| **web-private-password** (*string*；默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 通过 HTTP 访问 */um/PRIVATE/* 部分的密码。 |
| **web-private-username** (*string*；默认：) | 通过 HTTP 访问 */um/PRIVATE/* 部分的用户名。 |

## 用户

**子菜单：** `/user-manager/user`

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **attributes** (*array of attributes*；默认：) | 自定义的**属性**集及其值，将额外添加到 Access-Accept 消息中。 |
| **caller-id**(*string*；默认：) | 允许用户使用特定的 *Calling-Station-Id* 值进行认证。 |
| **comment** (*string*；默认：) | 用户的简短描述。 |
| **disabled** (*yes \| no*；默认：**no**) | 控制用户是否可以使用。 |
| **group** (*group*；默认：**default**) | 用户关联的**组**的名称。 |
| **name** (*string*；默认：) | 会话认证的用户名。 |
| **otp-secret** (*string*；默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 附加到密码的一次性密码令牌。 |
| **password** (*string*；默认：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用户会话认证的密码。 |
| **shared-users** (*integer \| unlimited*；默认：**1**) | 用户可以同时建立的会话总数。 |

### 命令

| 属性 | 描述 |
| :-- | :-- |
| **add-batch-users** () | 该命令可以根据各种参数生成多个用户账户。 |
| **generate-voucher** () | 基于 *voucher-template* 生成可呈现给最终用户的文件。 |
| **monitor** () | 显示用户的总统计信息。统计信息包括 *total-uptime*、*total-download*、*total-upload*、*active-sessions*、*actual-profile*、*attributes-details*。 |

## 用户组

**子菜单：** `/user-manager/user/group`

用户组定义了多个用户的共同特征，例如允许的认证方法和 RADIUS 属性。User Manager 中已有两个组，名为 *default* 和 *default-anonymous*。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **attributes** (*array of attributes*；默认：) | 自定义的**属性**集及其值，将额外添加到该组用户的 Access-Accept 消息中。 |
| **comment** (*string*；默认