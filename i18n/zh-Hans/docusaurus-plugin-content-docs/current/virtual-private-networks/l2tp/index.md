# L2TP

> 本文档介绍 MikroRouterOS L2TP 配置，涵盖客户端和服务器设置，包括认证方法、MTU/MRRU 设置、IPsec 集成以及用于二层隧道协议场景的动态接口管理。

import DocCardList from '@theme/DocCardList';

# L2TP

本节涵盖 L2TP 示例。用于配置 LAC 和 LNS 场景以及相关的 L2TP 互操作案例。

<DocCardList />

二层隧道协议“L2TP”扩展了 PPP 模型，允许 L2 和 PPP 端点位于通过分组交换网络互连的不同设备上。L2TP 包含每个 L2TP 连接的 PPP 认证和计费。每个连接的完整认证和计费可以通过 RADIUS 客户端或本地完成。L2TP 流量对控制和数据包均使用 UDP 协议。UDP 端口 1701 仅用于链路建立，后续流量使用任何可用的 UDP 端口（可能为 1701，也可能不是）。这意味着 L2TP 可以与大多数防火墙和路由器（甚至 NAT）配合使用，只需允许 UDP 流量通过防火墙或路由器路由即可。L2TP 标准定义于 [RFC 2661](https://tools.ietf.org/html/rfc2661)。L2TPv3 支持在 7.1 版本中添加。它支持 IPv4 和 IPv6。

## 简介

使用 L2TP 可以像使用任何其他隧道协议一样，无论是否加密。L2TP 标准规定，最安全的数据加密方式是使用 IPsec 之上的 L2TP（注意，这是 Microsoft L2TP 客户端的默认模式），因为特定隧道的所有 L2TP 控制和数据包在 IPsec 系统中表现为同质的 UDP/IP 数据包。

支持多链路 PPP（MP）以提供 MRRU（传输完整 1500 字节及更大数据包的能力）和通过 PPP 链路进行桥接（使用桥接控制协议（BCP），允许通过 PPP 链路发送原始以太网帧）。这样，无需 EoIP 即可设置桥接。桥接应具有管理设置的 MAC 地址或包含类似以太网的接口，因为 PPP 链路没有 MAC 地址。

:::warning
L2TP 不为隧道流量提供加密机制。IPsec 可用于额外的安全层。
:::

## L2TP 客户端

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*; 默认值: **no**) | 是否将 L2TP 远程地址添加为默认路由。 |
| **allow** (*mschap2 \| mschap1 \| chap \| pap*; 默认值: **mschap2, mschap1, chap, pap**) | 允许的认证方法。 |
| **connect-to** (*IP\|IPv6*; 默认值: ) | L2TP 服务器的远程地址（如果地址在 VRF 表中，则应指定 VRF）`/interface/l2tp-client``add connect-to=192.168.88.1@vrf1 name=l2tp-out1 user=l2tp-client)`    |
| **comment** (*string*; 默认值: ) | 隧道的简短描述。 |
| **default-route-distance** (*byte*; 默认值: ) | 自 v6.2 起，设置应用于自动创建的默认路由的距离值（如果同时选择了 add-default-route） |
| **dial-on-demand** (*yes \| no*; 默认值: **no**) | 仅在生成出站流量时连接。如果选择，则在连接未建立时，将添加一条网关地址来自 10.112.112.0/24 网络的路由。 |
| **disabled** (*yes \| no*; 默认值: **yes**) | 启用/禁用隧道。 |
| **keepalive-timeout** (*integer [1..4294967295]*; 默认值: **60s**) | 自 v6.0rc13 起，隧道 keepalive 超时时间（秒）。 |
| **max-mru** (*integer*; 默认值: **1450**) | 最大接收单元。L2TP 接口无需分片即可接收的最大数据包大小。 |
| **max-mtu** (*integer*; 默认值: **1450**) | 最大传输单元。L2TP 接口无需分片即可发送的最大数据包大小。 |
| **mrru** (*disabled \| integer*; 默认值: **disabled**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，它将被分割成多个数据包，允许通过隧道发送完整大小的 IP 或以太网数据包。 |
| **name** (*string*; 默认值: ) | 接口的描述性名称。 |
| **password** (*string*; 默认值: **""**) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于认证的密码。 |
| **profile** (*name*; 默认值: **default-encryption**) | 指定建立隧道时使用的 PPP profile 配置。 |
| **user** (*string*; 默认值: ) | 用于认证的用户名。 |
| **use-ipsec** (*yes \| no*; 默认值: **no**) | 启用此选项时，将添加动态 IPSec 对等体配置和策略（传输模式）以将 L2TP 连接封装到 IPSec 隧道中。**注意：** 同一 NAT 后面的多个 L2TP/IPsec 客户端在此模式下将无法工作。要实现此场景，请禁用 use-ipsec 并为客户端设置静态策略，启用 tunnel=yes, level=unique 设置。     |
| **allow-fast-path** (*yes \| no*; 默认值: ) | 允许在 Linux 内核中无需额外处理即可转发数据包。 |
| **l2tp-proto-version** ( l2tpv2 *\| l2tpv3-ip \| l2tpv3-udp \| l2tpv3*; 默认值:  **l2tpv2** ) | 指定协议版本。 |
| **l2tpv3-cookie-length** ( 0 *\| 4-bytes \| 8-bytes* ; 默认值:  **0** ) | 配置 L2TPv3 伪线静态会话 cookie。 |
| **l2tpv3-digest-hash** (*md5 \| none \| sha1* ; 默认值: **md5** ) | 指定要使用的哈希函数。 |
| **use-peer-dns** (*yes \| no \| exclusively*; 默认值:  **no**  ) | 使用对等 DNS。 |
| **copy-from** | 复制已创建的对等体。 |
| **src-address** | 指定源地址。 |
| **l2tpv3-circuit-id** | 设置虚拟电路标识符以绑定 L2TPv3 控制通道的一端。 |
| **ipsec-secret** (*string*; 默认值: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 启用 use-ipsec 时使用的预共享密钥。 |

## L2TP 服务器

为每个建立到给定服务器的隧道创建一个接口。L2TP 服务器的配置中有两种类型的接口：

- 静态接口是在需要引用为特定用户创建的特定接口名称（在防火墙规则或其他地方）时由管理员添加的。
- 动态接口在用户连接且其用户名与任何现有静态条目不匹配时自动添加到此列表（或者如果该条目已处于活动状态，因为不能有两个由相同名称引用的独立隧道接口）。

动态接口在用户连接时出现，在用户断开连接时消失，因此无法在路由器配置中引用为该用户创建的隧道（例如，在防火墙中），因此如果您需要为该用户提供持久规则，请为他/她创建静态条目。否则，使用动态配置是安全的。

:::warning
在这两种情况下，都必须正确配置 PPP 用户 - 静态条目不能替代 PPP 配置。
:::

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **authentication** (*pap \| chap \| mschap1 \| mschap2*; 默认值: **mschap1,mschap2**) | 服务器将接受的认证方法。 |
| **default-profile** (*name*; 默认值: **default-encryption**) | 要使用的默认 profile |
| **enabled** (*yes \| no*; 默认值: **no**) | 定义 L2TP 服务器是否启用。 |
| **max-mru** (*integer*; 默认值: **1450**) | 最大接收单元。L2TP 接口无需分片即可接收的最大数据包大小。 |
| **keepalive-timeout** (*integer*; 默认值: **30**) | 如果服务器在 keepalive-timeout 期间未收到任何数据包，它将每秒发送一次 keepalive 数据包，共五次。如果服务器仍未收到客户端的任何响应，则客户端将在 5 秒后断开连接。日志将显示 5 次“LCP missed echo reply”消息，然后断开连接。 |
| **max-mtu** (*integer*; 默认值: **1450**) | 最大传输单元。L2TP 接口无需分片即可发送的最大数据包大小。 |
| **use-ipsec** (*no \| yes \| require*; 默认值: **no**) | 启用此选项时，将添加动态 IPSec 对等体配置以适合大多数 L2TP 远程访问设置。选择 require 时，服务器将仅接受封装在 IPSec 隧道中的 L2TP 连接尝试。 |
| **ipsec-secret** (*string*; 默认值: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 启用 use-ipsec 时使用的预共享密钥 |
| **accept-proto-version** ( all *\|* l2tpv2 *\|* l2tpv3; 默认值: **all** ) 仅 CLI | 指定协议版本。 |
| **accept-pseudowire-type** ( all *\|* ether *\|* ppp; 默认值: **all** ) | 为特定伪线类型设置伪线信令协议。 |
| **allow-fast-path** (*no \| yes*; 默认值: **no** ) | 在 Linux 内核中无需额外处理即可转发数据包。 |
| **caller-id-type** ( ip-address *\|* number; 默认值: **ip-address**) | 如果多个客户端使用相同的源 IP 地址，请将 ID 类型设置为 number。 |
| **max-sessions** ( unlimited / number; 默认值: **unlimited** ) | 设置所需会话数。 |
| **one-session-per-host**( *no \| yes*; 默认值: **no** ) | 允许每个主机一个会话。 |
| **l2tpv3-circuit-id** (默认值: ) | 设置虚拟电路标识符以绑定 L2TPv3 控制通道的一端。 |
| **l2tpv3-cookie-length** (0 *\|* 4-bytes *\|* 8-bytes; 默认值: **0** ) | 配置 L2TP 伪线静态会话 cookie。 |
| **l2tpv3-digest-hash** ( md5 *\|* none *\|* sha1; 默认值: **md5** ) | 指定要使用的哈希函数。 |
| **l2tpv3-ether-interface-list** (默认值: ) | 设置您的接口列表，例如默认的 - all, dynamic, none, static。 |
| **mrru** (*disabled \| integer*; 默认值: **disabled**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，它将被分割成多个数据包，允许通过隧道发送完整大小的 IP 或以太网数据包。 |

## 快速示例

![](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/img/l2tp-01.webp)

### L2TP 服务器

在服务器端，我们将启用 L2TP 服务器并为特定用户创建 PPP profile：

```ros
[admin@MikroTik] > /interface/l2tp-server/server/set enabled=yes
[admin@MikroTik] > /ppp/secret/add local-address=10.0.0.2 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.1 service=l2tp
```

### L2TP 客户端

在 RouterOS 中设置 L2TP 客户端非常简单。在以下示例中，我们已有一个预配置的 3 单元设置。我们将更详细地了解如何使用用户名“MT-User”、密码“StrongPass”和服务器 192.168.51.3 设置 L2TP 客户端：

```ros
[admin@MikroTik] > /interface/l2tp-client \
add connect-to=192.168.51.3 disabled=no name=MT-User password=StrongPass user=MT-User
[admin@MikroTik] > /interface/l2tp-client/print 
Flags: X - disabled, R - running 
0 R name="MT-User" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.51.3 user="MT-User" 
password="StrongPass" profile=default-encryption keepalive-timeout=60 use-ipsec=no ipsec-secret="" 
allow-fast-path=no add-default-route=no dial-on-demand=no allow=pap,chap,mschap1,mschap2
```

## L2TP Ether

## 概述

第 2 层隧道协议版本 3（L2TPv3）由互联网工程任务组（IETF）的 [RFC 3931](https://tools.ietf.org/html/rfc3931) 定义。它对原始 L2TP 进行了各种改进，允许在 L2TP 内封装第 2 层（L2）负载。更准确地说，L2TPv3 概述了使用 L2 虚拟专用网络（VPN）通过 IP 核心网络隧道传输第 2 层负载的协议。

要建立 **L2TP Ether** 隧道，必须在**客户端**创建 **L2TP Ether 接口**，同时必须在**远程（服务器）端**启用 **L2TP 服务器**。一旦双方配置正确，它们之间将自动创建**动态接口**，从而在 IP 网络上形成透明的第 2 层连接。

---

##### **服务器端（L2TP 服务器）**

`/interface/l2tp-server/server/set enabled=yes`

##### **客户端（L2TP Ether 接口）**

`/interface/l2tp-ether/add` connect-to=1.1.1.1 disabled=no

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **connect-to** ( *IP*; 默认值: ) | L2TP 服务器的远程地址。  |
| **comment** ( *string*; 默认值: ) | 隧道的简短描述。 |
| **disabled** ( *yes \| no*; 默认值: **yes**) | 启用/禁用隧道。 |
| **mac-address** ( string; 默认值: **auto**) | 设置接口所需的 MAC 地址。 |
| **unmanaged-mode** ( *yes \| no*; 默认值: **no**) | 激活非管理模式。将可以配置其他设置，例如：**peer-cookie, send-cookie, local-tunnel-id, local-session-id, remote-tunnel-id, remote-session-id, local-address.** |
| **local-tunnel-id ( string; 默认值: disabled)** | 设置 local-tunnel-id 的值；需要整数。 |
| **local-session-id ( string; 默认值: disabled)** | 设置 local-session-id 的值；需要整数。 |
| **remote-tunnel-id (** string; 默认值: **disabled)** | 设置 remote-tunnel-id 的值；需要整数。 |
| **remote-session-id (** string; 默认值: **disabled)** | 设置 remote-session-id 的值；需要整数。 |
| **peer-cookie (** string; 默认值: **disabled)** | 设置可选的对等 cookie。要启用 cookie，请输入远程 cookie 值（需要 8 或 16 字符的十六进制字符串值）；要禁用，请留空。 |
| **send-cookie (** string; 默认值: **disabled)** | 设置可选的 cookie。要启用 cookie，请输入远程 cookie 值（需要 8 或 16 字符的十六进制字符串值）；要禁用，请留空。 |
| **mtu** (*auto*; 默认值: **1420**) | 最大传输单元。L2TP 接口无需分片即可发送的最大数据包大小。 |
| **name** (*string*; 默认值: ) | 接口的描述性名称。 |
| **local-address** (*IP address*; 默认值: ) | 为**非管理**模式设置本地地址。 |
| **use-ipsec** (*yes \| no*; 默认值: **no**) | 启用此选项时，将添加动态 IPSec 对等体配置和策略以将 L2TP 连接封装到 IPSec 隧道中。 |
| **allow-fast-path** (*yes \| no*; 默认值: **no** ) | 允许在 Linux 内核中无需额外处理即可转发数据包。 |
| **l2tp-proto-version** ( *l2tpv3-ip \| l2tpv3-udp* ; 默认值: ***l2tpv3-udp***) | 指定协议版本。 |
| **cookie-length** ( 0 *\| 4-bytes \| 8-bytes* ; 默认值:  **0** ) | 配置 L2TPv3 伪线静态会话 cookie。 |
| **digest-hash** (*md5 \| none \| sha1* ; 默认值: **md5** ) | 指定要使用的哈希函数。 |
| **use-l2-specific-sublayer** ( *yes \| no*; 默认值: **no**) | 启用 L2TPv3 以太网伪线第 2 层默认子层。 |
| **circuit-id** | 设置虚拟电路标识符以绑定 L2TPv3 控制通道的一端。这用作每个冗余伪线的标识符。 |
| **ipsec-secret** (*string*; 默认值: ) *[sensitive](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 启用 use-ipsec 时使用的预共享密钥。 |