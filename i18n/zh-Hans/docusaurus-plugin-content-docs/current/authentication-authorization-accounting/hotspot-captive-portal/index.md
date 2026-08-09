# HotSpot - 强制门户

> MikroTik HotSpot 网关支持通过DHCP地址池、多种认证方式及围墙花园访问控制等功能，为公共网络提供客户端认证。该功能要求使用IPv4，并存在特定的路由限制，本文提供了相应的配置示例。

# HotSpot - 强制门户

MikroTik HotSpot 网关在客户端访问公共网络之前提供认证功能。

:::warning
Hotspot（强制门户）使用 web-proxy，且目前仅能使用默认路由表，这使得 PCC（基于连接分类器）方法因涉及多路由表而无法生效。
:::

:::warning
HotSpot 功能可能被设备模式（device-mode）所限制。在配置 HotSpot 之前，请确保已在 `/system/device-mode` 中启用该功能（[更多信息](../../system-information-and-utilities/device-mode.md)）。
:::

### HotSpot 属性

| 属性 | 描述 |
| :--- | :--- |
| **name** | HotSpot 服务器实例的描述性名称。 |
| **interface** | HotSpot 服务监听客户端请求的特定本地接口（物理或虚拟）。 |
| **address-pool** | HotSpot 客户端通过 DHCP 获取 IP 地址的地址池。 |
| **profile** | 引用包含登录方法和 HTML 目录等通用设置的 HotSpot 服务器配置文件。 |
| **idle-timeout** | 客户端无流量活动时自动注销的闲置超时时间。 |
| **keepalive-timeout** | 用于检查客户端是否仍然可达的时间间隔；如果客户端无响应，则终止会话。 |
| **login-timeout** | 登录页面显示后，允许客户端完成认证过程的最大时长。 |
| **addresses-per-mac** | 限制单个 MAC 地址可关联的 IP 地址数量。 |
| **proxy-status** | 指示 HotSpot 系统使用的内部 web-proxy 的当前运行状态。 |

### HotSpot 网关特性

- 支持多种客户端认证方法，可使用路由器上的本地客户端数据库或远程 RADIUS 服务器。
- 支持在路由器本地数据库或远程 RADIUS 服务器上进行用户计费。
- 围墙花园系统，允许未经授权访问某些网页。
- 登录页面可修改，可添加公司相关信息。
- 自动且透明地将客户端的任何 IP 地址更改为有效地址。
- HotSpot 可通知 DHCP 客户端其位于强制门户之后（RFC7710）。

Hotspot 仅在 IPv4 环境下才能可靠运行。Hotspot 依赖防火墙 NAT 规则，而当前 NAT 规则不支持 IPv6。

## 示例

```ros
[admin@MikroTik] /ip/hotspot> setup 
Select interface to run HotSpot on 

hotspot interface: ether3
Set HotSpot address for interface 

local address of network: 10.5.50.1/24
masquerade network: yes
Set pool for HotSpot addresses 

address pool of network: 10.5.50.2-10.5.50.254
Select hotspot SSL certificate 

select certificate: none
Select SMTP server 

ip address of smtp server: 0.0.0.0
Setup DNS configuration 

dns servers: 10.1.101.1
DNS name of local hotspot server 

dns name: myhotspot
Create local hotspot user 

name of local hotspot user: admin
password for the user: 
[admin@MikroTik] /ip/hotspot>
```

## 验证 HotSpot 配置

```ros
[admin@MikroTik] /ip/hotspot> print 
Flags: X - disabled, I - invalid, S - HTTPS 
# NAME INTERFACE ADDRESS-POOL PROFILE IDLE-TIMEOUT
0 hotspot1 ether3 hs-pool-3 hsprof1 5m 
[admin@MikroTik] /ip/hotspot> 
[admin@MikroTik] /ip/pool> print 
# NAME RANGES 
0 hs-pool-3 10.5.50.2-10.5.50.254 
[admin@MikroTik] /ip/pool> /ip/dhcp-server 
[admin@MikroTik] /ip/dhcp-server> print 
Flags: X - disabled, I - invalid 
# NAME INTERFACE RELAY ADDRESS-POOL LEASE-TIME ADD-ARP
0 dhcp1 ether3 hs-pool-3 1h 
[admin@MikroTik] /ip/dhcp-server> /ip/firewall/nat 
[admin@MikroTik] /ip/firewall/nat> print 
Flags: X - disabled, I - invalid, D - dynamic 
0 X ;;; 在此处放置 hotspot 规则
chain=unused-hs-chain action=passthrough 

1 ;;; 对 hotspot 网络进行 masquerade
chain=srcnat action=masquerade src-address=10.5.50.0/24 
[admin@MikroTik] /ip/firewall/nat> 
```

### **设置过程中询问的参数**

| 参数 | 描述 |
| :-- | :-- |
| **hotspot interface** (*字符串*; 默认值: **allow**) | 运行 HotSpot 的接口名称。要在桥接接口上运行 HotSpot，请确保公共接口未包含在桥接端口中。 |
| **local address of network** (*IP*; 默认值: **10.5.50.1/24**) | HotSpot 网关地址 |
| **masquerade network** (*yes \| no*; 默认值: **yes**) | 是否对 HotSpot 网络进行 masquerade，当设置为 **yes** 时，会在 *`/ip/firewall/nat`* 中添加一条 *action=masquerade* 的规则 |
| **address pool of network** (*字符串*; 默认值: **yes**) | HotSpot 网络的地址池，用于将用户 IP 地址更改为有效地址。适用于为不愿更改网络设置的移动客户端提供网络访问。 |
| **select certificate** (*none \| import-other-certificate*; 默认值: ) | 当需要 HTTPS 认证方法时，选择 SSL 证书。 |
| **ip address of smtp server** (*IP*; 默认值: **0.0.0.0**) | SMTP 服务器的 IP 地址，用于重定向 HotSpot 网络的 SMTP 请求（TCP 端口 25） |
| **dns servers** (*IP*; 默认值: **0.0.0.0**) | 用于 HotSpot 客户端的 DNS 服务器地址，配置取自 HotSpot 网关的 *`/ip/dns`* 菜单 |
| **dns name** (*字符串*; 默认值: **""**) | HotSpot 服务器的域名，需要完全限定域名，例如 [www.example.com](http://www.example.com) |
| **name of local hotspot user** (*字符串*; 默认值: **"admin"**) | 自动创建的一个 HotSpot 用户的用户名，添加到 *`/ip/hotspot/user`* |
| **password for the user** (*字符串*; 默认值: ) | 自动创建的 HotSpot 用户的密码 |

## HotSpot

**子菜单：** `/ip/hotspot`

该菜单用于管理路由器的 HotSpot 服务器。可以在以太网、无线、VLAN 和桥接接口上运行 HotSpot。每个接口允许运行一个 HotSpot 服务器。当在桥接接口上配置 HotSpot 时，应将 HotSpot 接口设置为桥接接口本身，而不是桥接端口，且不要将公共接口添加到桥接端口。您可以手动在 *`/ip/hotspot`* 菜单中添加 HotSpot 服务器，但建议运行 *`/ip/hotspot/setup`*，它会自动添加所有必要的设置。

| 参数 | 描述 |
| :-- | :-- |
| **name** (文本) | HotSpot 服务器的名称或标识符 |
| **address-pool** (名称/none; 默认值: *none*) | 用于将任何 HotSpot 客户端 IP 地址更改为有效地址的地址空间。适用于为不愿更改网络设置的移动客户端提供公共网络访问 |
| **idle-timeout** (时间/none; 默认值: *5m*) | 未授权客户端的闲置超时时间。当该客户端无流量时（即客户端计算机已关闭），超时后，用户将从 HotSpot 主机列表中移除，其使用的地址变为可用 |
| **keepalive-timeout** (时间/none; 默认值: *none*) | 主机在不可达状态下保持多长时间后将从 HotSpot 中移除 |
| **login-timeout** (时间/none; 默认值: *none*) | 如果主机在指定时间内未通过系统认证，其主机条目将从主机表中删除。此循环重复，直到主机登录系统。当存在主机长时间未认证而滞留在主机表中的情况时，建议启用此选项。 |
| **interface** (接口名称) | 运行 HotSpot 的接口 |
| **addresses-per-mac** (整数**/**unlimited; 默认值: 2) | 允许与 MAC 地址绑定的 IP 地址数量，适用于多个 HotSpot 客户端使用同一 MAC 地址连接的情况 |
| **profile** (名称; 默认值: ***default*)** | HotSpot 服务器的默认 HotSpot 配置文件，位于 *`/ip/hotspot/profile`* |

## 只读属性

| 参数 | 描述 |
| :-- | :-- |
| keepalive-timeout (只读; 时间) | 应用于用户的 keepalive-timeout 的确切值。该值显示主机在不可达状态下保持多长时间后将从 HotSpot 中移除 |

## HotSpot 配置文件

此子菜单包含 HotSpot 服务器配置文件列表。在同一网关机器上可以定义多个不同的 HotSpot 系统，称为服务器配置文件。一个或多个接口可以分组到一个服务器配置文件中。特定接口上的服务器设置很少——大部分配置都在服务器配置文件中设置。例如，可以为每个服务器配置文件创建完全不同的 servlet 页面集，并定义不同的 RADIUS 服务器进行认证。

| 属性 | 描述 |
| :-- | :-- |
| **dns-name** (*字符串*; 默认值: **""**) | HotSpot 服务器的 DNS 名称。此 DNS 名称用作 HotSpot 服务器的名称（即，它显示为登录页面的位置）。此名称将自动作为静态 DNS 条目添加到 DNS 缓存中。 |
| **hotspot-address** (*IP*; 默认值: **0.0.0.0**) | HotSpot 服务的 IP 地址。 |
| **html-directory** (*字符串*; 默认值: **hotspot**) | 存储 HotSpot HTML 页面的目录名称（默认为 *hotspot* 目录）。可以指定包含修改后 HTML 页面的不同目录。要更改 HotSpot 登录页面，请从路由器获取 HotSpot 文件，修改后上传回相同位置。必须在 html-directory 字段中输入完整路径，包括 "/flash/(hotspot\_dir)" |
| **html-directory-override** (*字符串*; 默认值: **none**) | Hotspot HTML 文件的替代路径。仅当自定义的 hotspot HTML 文件存储在外部存储上时才应使用。 |
| **http-cookie-lifetime** (*时间*; 默认值: **3d**) | HTTP cookie 的有效期，该选项与 *cookie* HotSpot 登录方法相关 |
| **http-proxy** (*IP:端口*; 默认值: **0.0.0.0:0**) | HotSpot 服务的代理服务器地址和端口，使用默认值时，所有请求由本地 `/ip/proxy` 解析 |
| **https-redirect** (*yes \| no*; 默认值: **yes**) | 当用户访问 https:// URL 时，是否将未认证用户重定向到 hotspot 登录页面。由于证书域名不匹配，这通常会导致错误，因此可以将此参数设置为 "no"，所有 https 请求将被直接拒绝，用户必须访问 http 页面。 |
| **login-by** (*cookie\|http-chap\|http-pap\|https\|mac\|trial\|mac-cookie*; 默认值: **http-chap, cookie**) | HotSpot 认证方法mac-cookie - 通过 mac cookie 方法启用登录cookie - 只能与另一种 HTTP 认证方法一起使用。当用户首次在 HotSpot 中认证时，会生成 HTTP cookie。在 cookie-lifetime 有效期内，用户无需输入登录名/密码即可自动认证http-chap - 用户需要在 HotSpot 中输入登录名/密码进行认证。使用基于 MD5 哈希算法的 CHAP 挑战-响应方法来保护密码。http-pap - 用户需要在 HotSpot 中输入登录名/密码进行认证。用户名和密码以明文形式通过网络发送。https - 用户需要在 HotSpot 中输入登录名/密码进行认证。客户端与服务器之间的登录名/密码交换通过 SSL 隧道加密。mac - 客户端无需填写登录表单即可认证。客户端 MAC 地址添加到 `/ip/hotspot/user` 数据库中，客户端连接 HotSpot 后即完成认证trial - 允许客户端在指定时间内无需 HotSpot 登录即可使用互联网 |
| **mac-auth-password** (*字符串*; 默认值: ) *[敏感参数](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 与 MAC 认证一起使用，该字段用于为通过 MAC 地址认证的用户指定密码。当特定 RADIUS 服务器拒绝使用空白密码的客户端认证时，需要以下选项 |
| **name** (*字符串*; 默认值: ) | 配置文件的描述性名称 |
| **nas-port-type** (*字符串*; 默认值: **wireless-802.11**) | 发送到 RADIUS 服务器的 NAS-Port-Type 值，NAS-Port-Type 值在 RADIUS RFC 2865 中有描述。此可选值属性指示 HotSpot 服务器物理端口的类型。 |
| **radius-accounting** (*yes \| no*; 默认值: **yes**) | 当设置为 yes 时，为每个用户向 RADIUS 服务器发送计费信息 |
| **radius-default-domain** (*字符串*; 默认值: ) | 用于 RADIUS 请求的默认域。允许为每个 *`/ip/hotspot/profile`* 使用单独的 RADIUS 服务器。如果使用，应在 /radius 域值下指定相同的域名。 |
| **radius-interim-update** (*时间 \| received*; 默认值: **received**) | 发送计费更新的频率。当设置为 *received* 时，使用 RADIUS 服务器发送的 interim-time。**0s** 与 *received* 相同。 |
| **radius-location-name** (*字符串*; 默认值: ) | 发送到 RADIUS 服务器的 RADIUS-Location-Id。用于在与 RADIUS 服务器通信时标识 HotSpot 服务器的位置。该值是可选的，与 RADIUS 服务器一起使用。 |
| **radius-mac-format** (*"XX XX XX XX XX XX"\|XX:XX:XX:XX:XX:XX\|XXXXXX-XXXXXX\|XXXXXXXXXXXX\|XX-XX-XX-XX-XX-XX\|XXXX:XXXX:XXXX\|XXXXXX:XXXXXX*; 默认值: **XX:XX:XX:XX:XX:XX**) | 设置 AAA 会话期间发送到 RADIUS 服务器的用户 MAC 地址格式的选项。 |
| **rate-limit** (*字符串*; 默认值: **""**) | 速率限制格式为 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time]]]] [priority] [rx-rate-min[/tx-rate-min]]**，从路由器的角度（因此 "rx" 是客户端上传，"tx" 是客户端下载）。所有速率应为数字，可带 'k'（1,000）或 'M'（1,000,000）后缀。如果未指定 tx-rate，则 tx-rate 与 rx-rate 相同。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果未指定 rx-burst-threshold 和 tx-burst-threshold（但指定了 burst-rate），则使用 rx-rate 和 tx-rate 作为突发阈值。如果未指定 rx-burst-time 和 tx-burst-time，则默认使用 1s。rx-rate-min 和 tx-rate-min 是 limit-at 属性的值 |
| **smtp-server** (*IP*; 默认值: **0.0.0.0**) | 用于重定向 HotSpot 用户 SMTP 请求的 SMTP 服务器地址。 |
| **split-user-domain** (*yes \| no*; 默认值: **no**) | 当用户名以 "user@domain" 或 "domain\user" 格式提供时，将用户名与域名拆分 |
| **ssl-certificate** (*字符串 \| none*; 默认值: **none**) | 路由器上仅用于 HTTPS 认证的 SSL 证书名称。 |
| **trial-uptime** (*时间/时间*; 默认值: **30m/1d**) | 仅与 *trial* 认证方法一起使用。第一个时间值指定由 MAC 地址标识的试用用户无需 HotSpot 认证即可访问公共网络的时长。第二个时间值指定用户再次允许试用前必须经过的时间量。 |
| **trial-user-profile** (*字符串*; 默认值: **default**) | 为试用用户指定 **hotspot 用户配置文件**。 |
| **use-radius** (*yes \| no*; 默认值: **no**) | 使用 RADIUS 认证 HotSpot 用户。 |

## HotSpot 用户配置文件

**子菜单：** `/ip/hotspot/user/profile`

用户配置文件菜单用于通用 HotSpot 客户端设置。配置文件类似于具有相同设置集的用户组，包括速率限制、过滤器链名称等。

| 属性 | 描述 |
| :-- | :-- |
| **add-mac-cookie** (*yes\|no*; 默认值: **yes**) | 允许为用户添加 mac cookie。 |
| **address-list** (*字符串*; 默认值: ) | 用户 IP 地址将被添加到的地址列表名称。用于在队列树配置中按用户组标记流量。 |
| **address-pool** (*字符串 \|none*; 默认值: **none**) | 用户获取 IP 的 IP 池名称。当用户的计算机网络设置配置不正确时，HotSpot 服务器会进行转换，并从池中分配正确的 IP 地址以替代不正确的地址 |
| **advertise** (*yes \| no*; 默认值: **no**) | 启用强制广告弹窗。经过一定时间间隔后，HotSpot 用户会看到特定的网页。广告页面可能被浏览器弹窗拦截器阻止。 |
| **advertise-interval** (*时间[,时间[,..]]*; 默认值: **30m,10m**) | 广告弹窗之间的时间间隔集合。列表用完后，后续所有广告使用最后一个值，即 10 分钟 |
| **advertise-timeout** (*时间 \| immediately \| never*; 默认值: **1m**) | 在阻止 HotSpot 客户端网络访问之前，广告显示的时长。广告未显示时，不允许连接互联网。 |
| **advertise-url** (*字符串[,字符串[,..]]*; 默认值: ) | 用于广告弹窗显示的 URL 列表。最后一个 URL 使用后，列表从头开始。 |
| **idle-timeout** (*时间 \| none*; 默认值: **none**) | 已授权 HotSpot 客户端的最大闲置时间。当没有来自该客户端且经过路由器的流量时（例如计算机已关闭），计时器开始计时。超时后，用户将被注销，从主机列表中移除，其使用的地址被释放。 |
| **incoming-filter** (*字符串*; 默认值: ) | 应用于来自此配置文件用户的入站数据包的防火墙链名称。需要从内置链（input、forward、output）到 chain=hotspot 的跳转规则 |
| **incoming-packet-mark** (*字符串*; 默认值: ) | 应用于此配置文件每个用户的入站数据包的数据包标记 |
| **keepalive-timeout** (*时间 \| none*; 默认值: ) | 已授权 HotSpot 客户端的 keepalive 超时时间。用于检测客户端计算机是否存活且可达。超时后用户将被注销 |
| **mac-cookie-timeout** (*时间*; 默认值: **3d**) | 选择从上次登录或注销起的 mac-cookie 超时时间。 |
| **name** (*字符串*; 默认值: ) | 配置文件的描述性名称 |
| **on-login** (*字符串*; 默认值: **""**) | 用户从特定配置文件登录 HotSpot 时执行的脚本名称。可以从内部 **user** 和 **interface** 变量获取用户名。例如，*:log info "User $user logged in!"*。如果 hotspot 设置在桥接接口上，则 **interface** 变量将显示桥接接口为实际接口，除非在桥接设置中设置了 **use-ip-firewall**。可用变量列表：$user$username（$user 的替代变量名）$address$"mac-address"$interface |
| **on-logout** (*字符串*; 默认值: **""**) | 用户从 HotSpot 注销时执行的脚本名称。可以从内部 **user** 和 **interface** 变量获取用户名。例如，*:log info "User $user logged in!"*。如果 hotspot 设置在桥接接口上，则 **interface** 变量将显示桥接接口为实际接口，除非在桥接设置中设置了 **use-ip-firewall**。可用变量列表：$user$username（$user 的替代变量名）$address$"mac-address"$interface$cause 从 v6.34rc11 开始，提供一些附加变量：$uptime-secs - 最终会话时间（秒）$bytes-in - 上传字节数$bytes-out - 下载字节数$bytes-total - 上传 + 下载字节数$packets-in - 上传数据包数$packets-out - 下载数据包数$packets-total - 上传 + 下载数据包数 |
| **open-status-page** (*always \| http-login*; 默认值: **always**) | 为使用 mac 登录方法认证的用户显示状态页面的选项。例如，在状态页面（alogin.html）上显示广告http-login - 仅为 HTTP 登录（包括 cookie 和 HTTPS）打开状态页面always - 在 mac 登录的情况下也打开 HTTP 状态页面 |
| **outgoing-filter** (*字符串*; 默认值: ) | 应用于来自此配置文件用户的出站数据包的防火墙链名称。需要从内置链（input、forward、output）到 chain=hotspot 的跳转规则 |
| **outgoing-packet-mark** (*字符串*; 默认值: ) | 应用于此配置文件每个用户的出站数据包的数据包标记 |
| **rate-limit** (*字符串*; 默认值: **""**) | 用户登录 HotSpot 后，会为其创建一个简单的动态队列。速率限制按以下格式配置 **[rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**。例如，要为客户端设置 1M 下载、512k 上传，使用 rate-limit=512k/1M |
| **session-timeout** (*时间*; 默认值: **0s**) | 允许的客户端会话时间。超过此时间后，用户将被无条件注销 |
| **shared-users** (*整数*; 默认值: **1**) | 允许使用相同 HotSpot 用户名同时登录的用户数量 |
| **status-autorefresh** (*时间 \| none*; 默认值: **none**) | HotSpot 状态页面自动刷新间隔 |
| **transparent-proxy** (*yes \|*; 默认值: **yes**) | 为此配置文件的已授权用户使用透明 HTTP 代理 |

## HotSpot 用户

这是实际添加客户端用户名/密码信息的菜单。HotSpot 用户的附加配置选项也在此处配置。

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP*; 默认值: **0.0.0.0**) | IP 地址，指定后，客户端将从 HotSpot 一对一 NAT 转换中获取该地址。该地址不限制 HotSpot 登录只能从此地址进行 |
| **comment** (*字符串*; 默认值: ) | HotSpot 用户的描述性信息。可用于脚本为特定客户端更改参数 |
| **email** (*字符串*; 默认值: ) | HotSpot 客户端的电子邮件，HotSpot 用户的信息性值 |
| **limit-bytes-in** (*整数*; 默认值: **0**) | 可从用户接收的最大字节数。达到限制后，用户将从 HotSpot 断开连接。 |
| **limit-bytes-out** (*整数*; 默认值: **0**) | 可从用户传输的最大字节数。达到限制后，用户将从 HotSpot 断开连接。 |
| **limit-bytes-total** (*整数*; 默认值: **0**) | （limit-bytes-in+limit-bytes-out）。达到限制后，用户将从 HotSpot 断开连接。 |
| **limit-uptime** (*时间*; 默认值: **0**) | HotSpot 客户端的在线时间限制。达到在线时间后，用户将立即从 HotSpot 断开连接。 |
| **mac-address** (*MAC*; 默认值: **00:00:00:00:00:00**) | 客户端仅允许从指定的 MAC 地址登录。如果值为 *00:00:00:00:00:00*，则允许任何 MAC 地址。 |
| **name** (*字符串*; 默认值: ) | HotSpot 登录页面用户名。使用 MAC 地址认证时，名称配置为客户端的 MAC 地址 |
| **password** (*字符串*; 默认值: ) *[敏感参数](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用户密码 |
| **profile** (*字符串*; 默认值: **default**) | 在 *`/ip/hotspot/user/profile`* 中配置的用户配置文件 |
| **routes** (*字符串*; 默认值: ) | 客户端连接时添加到 HotSpot 网关的路由。路由格式为 **dst-address gateway metric**（例如，*192.168.1.0/24 192.168.0.1 1*） |
| **server** (*字符串 \| all*; 默认值: **all**) | 允许用户登录的 HotSpot 服务器名称 |
| **otp-secret** (*字符串*; 默认值: ) *[敏感参数](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于 HotSpot 用户授权的一次性密码令牌。可作为 HotSpot 用户认证的独立 "密码" 使用。 |

## 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **bytes-in** (*整数*) | 从客户端接收的数据字节总数。 |
| **bytes-out** (*整数*) | 发送给客户端的数据字节总数。 |
| **packets-in** (*整数*) | 从客户端接收的数据包总数。 |
| **packets-out** (*整数*) | 发送给客户端的数据包总数。 |
| **uptime** (*时间*) | 自客户端认证以来的当前会话时长。 |

## HotSpot 活动会话

**子菜单：** `/ip/hotspot/active`

HotSpot 活动菜单显示所有在 HotSpot 中认证的客户端，该菜单为信息性（只读）菜单。此处无法更改任何内容，但可以使用 remove 命令注销用户。

| 参数 | 描述 |
| :-- | :-- |
| **server** (只读; 名称) | 客户端登录的 HotSpot 服务器名称 |
| **user** (只读; 名称) | HotSpot 用户名 |
| **domain** (只读; 文本) | 用户的域（如果从用户名中拆分），该参数仅与 RADIUS 认证一起使用 |
| **address** (只读; IP 地址) | HotSpot 用户的 IP 地址 |
| **mac-address** (只读; MAC 地址) | HotSpot 用户的 MAC 地址 |
| **login-by** (只读; 多选: cookie **/** http-chap **/** http-pap **/** https **/** mac **/** mac-cookie **/** trial) | HotSpot 客户端使用的认证方法 |
| **uptime** (只读; 时间) | 用户的当前会话时间，显示用户已登录多长时间 |
| **idle-time** (只读; 时间) | 用户闲置的时间量 |
| **session-time-left** (只读; 时间) | 应用于用户的 session-time 的确切值。该值显示用户被允许在线多长时间，之后将因 **uptime** 达到限制而被自动注销 |
| **idle-timeout** (只读; 时间) | 用户 idle-timeout 的确切值 |
| **keepalive-timeout** (只读; 时间) | 应用于用户的 keepalive-timeout 的确切值。该值显示主机在不可达状态下保持多长时间后将从 HotSpot 中移除 |
| **limit-bytes-in** (只读; 整数) | 显示从客户端接收的字节数，当为 HotSpot 用户配置了相应参数时，此选项处于活动状态 |
| **limit-bytes-out** (只读; 整数) | 显示发送给客户端的字节数，当为 HotSpot 用户配置了相应参数时，此选项处于活动状态 |
| **limit-bytes-total** (只读; 整数) | 显示从客户端发送/接收的总字节数，当为 HotSpot 用户配置了相应参数时，此选项处于活动状态 |

## HotSpot 主机

**子菜单：** `/ip/hotspot/host`

主机表列出所有连接到 HotSpot 服务器的计算机。主机表为信息性表格，无法更改其中的任何值：

| 参数 | 描述 |
| :-- | :-- |
| **mac-address** (只读; MAC 地址) | HotSpot 用户 MAC 地址 |
| **address** (只读; IP 地址) | HotSpot 客户端的原始 IP 地址 |
| **to-address** (只读; IP 地址) | HotSpot 分配的新客户端地址，可能与原始 **address** 相同 |
| **server** (只读; 名称) | 客户端连接的 HotSpot 服务器名称 |
| **bridge-port** (只读; 名称) | 客户端连接的 *`/interface/bridge/port`*，当 HotSpot 未配置在桥接接口上时，该值未知 |
| **uptime** (只读; 时间) | 显示用户在线（连接到 HotSpot）的时间 |
| **idle-time** (只读; 时间) | 用户闲置的时间 |
| **idle-timeout** (只读; 时间) | 客户端 idle-timeout 的值（未授权客户端） |
| **keepalive-timeout** (只读; 时间) | 未授权客户端的 keepalive-timeout 值 |
| **bytes-in** (只读; 整数) | 从未授权客户端接收的字节数 |
| **packet-in** (只读; 整数) | 从未授权客户端接收的数据包数 |
| **bytes-out** (只读; 整数) | 发送给未授权客户端的字节数 |
| **packet-out** (只读; 整数) | 发送给未授权客户端的数据包数 |

## HotSpot 围墙花园

围墙花园是一种允许未经授权使用某些资源，但访问其他资源需要授权的系统。例如，这对于提供有关 HotSpot 服务提供商或计费选项的通用信息访问非常有用。

该菜单仅管理 HTTP 和 HTTPS 协议的围墙花园。其他协议也可以包含在围墙花园中，但需在其他位置配置（在 `/ip/hotspot/walled-garden/ip` 中）。

| 属性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 默认值: **allow**) | 当数据包匹配规则时执行的操作allow - 允许无需授权访问网页deny - 访问网页需要授权 |
| **server** (*字符串*; 默认值: ) | 应用规则的 HotSpot 服务器名称。 |
| **src-address** (*IP*; 默认值: ) | 用户源地址，通常是 HotSpot 客户端的 IP 地址 |
| **method** (*字符串*; 默认值: ) | 请求的 HTTP 方法 |
| **dst-host** (*字符串*; 默认值: ) | 目标 Web 服务器的域名 |
| **dst-port** (*整数*; 默认值: ) | 客户端发送请求的 TCP 端口号 |
| **path** (*字符串*; 默认值: ) | 请求的路径。路径位于 '''http://dst\_host' 之后 |

# 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **dst-address** (*IP*) |  |
| **hits** (*整数*) |  |

通配符属性（dst-host 和 path）匹配完整字符串（即，如果设置为 "example"，则不会匹配 "[example.com](http://example.com)"）。可用的通配符为 '\*'（匹配任意数量的任意字符）和 '?'（匹配任意单个字符）。此处也接受正则表达式，但如果属性应被视为正则表达式，则应以冒号（':'）开头。要表示给定模式之前不允许任何符号，请在模式开头使用 ^ 符号。要指定给定模式之后不允许任何符号，请在模式末尾使用 $ 符号。

### 示例

仅允许围墙花园中绕过访问 "[www.example.com/test](http://www.example.com/test)"，但不允许访问 "[www.example.com/test/test.php](http://www.example.com/test/test.php)"：

```
/ip/hotspot/walled-garden
add dst-host=:^www.example.com path=":/test\$"
```

## HotSpot 围墙花园 IP

用于绕过其他协议以及不同源/目标地址（或地址列表）的 HotSpot 认证。用于不同的服务（Winbox、SSH、Telnet、SIP 等）

| 属性 | 描述 |
| :-- | :-- |
| **action** (*accept \|drop\|reject*; 默认值: **allow**) | 当数据包匹配规则时执行的操作allow - 允许无需授权访问开放服务drop - 访问服务需要授权reject - 访问服务需要授权，当访问服务时，将生成 ICMP 拒绝消息 host-unreachable |
| **server** (*字符串*; 默认值: ) | 应用规则的 HotSpot 服务器名称。 |
| **src-address** (*IP*; 默认值: ) | 用户源地址，通常是 HotSpot 客户端的 IP 地址 |
| **dst-address** (*IP*; 默认值: ) | 目标 IP 地址，即 WEB 服务器的 IP 地址。如果已指定 **dst-host**，则忽略此参数。 |
| **src-address-list** (*字符串*; 默认值: ) | 源地址列表名称 |
| **dst-address-list** (*字符串*; 默认值: ) | 目标地址列表。如果已指定 **dst-host**，则忽略此参数。 |
| **dst-host** (*字符串*; 默认值: ) | 目标 Web 服务器的域名。指定此参数时，会向围墙花园添加动态条目 |
| **dst-port** (*整数*; 默认值: ) | 客户端发送请求的 TCP 端口号 |
| **protocol** (*整数 \| 字符串*; 默认值: ) | IP 协议 |

## IP 绑定

**子菜单：** `/ip/hotspot/ip-binding`

IP-Binding HotSpot 菜单允许设置静态一对一 NAT 转换，允许绕过特定 HotSpot 客户端的认证，也允许阻止 HotSpot 网络中的特定主机和子网

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP 范围*; 默认值: **""**) | 客户端的原始 IP 地址 |
| **mac-address** (*MAC*; 默认值: **""**) | 客户端的 MAC 地址 |
| **server** (*字符串 \| all*; 默认值: **"all"**) | HotSpot 服务器名称。all - 将应用于所有 hotspot 服务器 |
| **to-address** (*IP*; 默认值: **""**) | 客户端的新 IP 地址，转换发生在路由器上（客户端不知道转换） |
| **type** (*blocked \| bypassed \| regular*; 默认值: **""**) | IP 绑定操作的类型regular - 根据规则执行一对一 NAT，将