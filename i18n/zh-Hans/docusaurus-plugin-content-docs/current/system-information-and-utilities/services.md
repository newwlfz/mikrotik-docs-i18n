# 服务

> 本文档介绍 MikroTik RouterOS 中的 IP/Services 部分，详细说明了 Telnet、FTP、SSH 和 WinBox 等默认服务及其配置属性，如地址限制、端口、TLS 版本和会话限制。并提供了管理服务访问控制的示例。

# 服务

IP/Services 列出了各种 MikroTik RouterOS 服务和容器所使用的协议和端口，包括用于传入连接的协议和端口。

它有助于确定哪些 MikroTik 服务（或容器）正在特定端口上监听，以及如果您想限制或允许访问某些服务，需要阻止或允许哪些内容。

可从 IP/Services 部分配置的默认服务：

| 属性 | 描述 |
| :-- | :-- |
| **telnet** | Telnet 服务 |
| **ftp** | FTP 服务 |
| **www** | WebFig HTTP 服务 |
| **ssh** | SSH 服务 |
| **www-ssl** | WebFig HTTPS 服务 |
| **api** | API 服务 |
| **winbox** | 负责 WinBox 工具访问，以及 MikroTik 智能手机应用和 Dude |
| **api-ssl** | 基于 SSL 的 API 服务 |
| **reverse-proxy** | 反向代理服务 |

## 属性

请注意，无法添加新服务，仅允许修改现有服务。

**子菜单：** `/ip/service`

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP地址/网络掩码 \| IPv6/0..128*; 默认：) | 允许访问服务的 IP/IPv6 前缀列表。设置此参数后，数据包不会在网络层面被丢弃，但对于不匹配指定地址的源，将拒绝其访问服务。此选项最适合在受信任网络内限制访问。要阻止来自外部或不受信任网络的访问，我们建议改用防火墙。 |
| **certificate** (*名称*; 默认：**none**) | 特定服务使用的证书名称。仅适用于依赖证书的服务（*www-ssl, api-ssl*） |
| **name** (*名称*; 默认：**none**) | 服务名称 |
| **max-sessions**(*整数: 1..1000*; 默认：20) | 服务的最大同时会话数 |
| **port** (*整数: 1..65535*; 默认：) | 特定服务监听的端口 |
| ***tls-version*** (*any* \| *only-1.2*; 默认：**any**) | 指定特定服务允许的 TLS 版本 |
| **vrf** (*名称*; 默认：**main**) | 指定特定服务使用的 VRF 实例 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **Container** | 在端口上监听的容器名称 |
| **Local** | 用于连接的路由器本地地址 |
| **Remote** | 与服务建立连接的远程地址 |

### 示例

例如，仅允许来自特定 IP/IPv6 地址范围的 API 访问

```ros
[admin@dzeltenais_burkaans] /ip/service/set api address=10.5.101.0/24,2001:db8:fade::/64
[admin@dzeltenais_burkaans] /ip/service/print where !dynamic      
Flags: X - DISABLED, I - INVALID
Columns: NAME, PORT, PROTO, ADDRESS, CERTIFICATE, VRF, MAX-SESSIONS
 #   NAME     PORT  PROTO  ADDRESS             CERTIFICATE  VRF   MAX-SESSIONS
 0   ftp        21  tcp                                     main            20
 1   ssh        22  tcp                                     main            20
 2   telnet     23  tcp                                     main            20
 7   www        80  tcp                                     main            20
 9 X www-ssl   443  tcp                        none         main            20
13   winbox   8291  tcp                                     main            20
15   api      8728  tcp    10.5.101.0/24                    main            20
                           2001:db8:fade::/64                                 
16   api-ssl  8729  tcp                        none         main            20
```

显示正在监听或已与路由器服务建立连接的动态服务的示例

```routeros
[admin@dzeltenais_burkaans] /ip/service/print where dynamic  
Flags: D - DYNAMIC; c - CONNECTION
Columns: NAME, NETNS, CONTAINER, PORT, PROTO, LOCAL, REMOTE
 #    NAME        NETNS  CONTAINER  PORT  PROTO  LOCAL         REMOTE            
 3 D  resolver                        53  tcp                                    
 4 D  resolver                        53  udp                                    
 5 D  dhcp                            67  udp                                    
 6 D  dhcpclient                      68  udp                                    
 8 D  snmp                           161  udp                                    
10 D  btest                         2000  tcp                                    
11 D  loader                        3986  tcp                                    
12 D  discover                      5678  udp                                    
14 Dc winbox                        8291  tcp    10.155.221.4  10.145.221.15:51595
17 D  pihole-FTL     16  Pi-hole      53  tcp                                    
18 D  pihole-FTL     16  Pi-hole      53  udp                                    
19 D  lighttpd       16  Pi-hole      80  tcp                                    
28 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52298
29 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52333
30 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52339
31 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52340
32 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52341
33 Dc lighttpd       16  Pi-hole      80  tcp    172.55.1.2    10.145.221.15:52342
26 D  pihole-FTL     16  Pi-hole    4711  tcp
```

## 协议和端口

下表显示了 RouterOS 使用的协议和端口列表。

| 协议/端口 | 描述 |
| :-- | :-- |
| **20/tcp** | FTP 数据连接 |
| **21/tcp** | FTP 控制连接 |
| **22/tcp** | 安全外壳 (SSH) 远程登录协议 |
| **23/tcp** | Telnet 协议 |
| **53/tcp 53/udp** | DNS |
| **67/udp** | 引导协议或 [DHCP 服务器](../network-management/dhcp.md#dhcp-server) |
| **68/udp** | 引导协议或 [DHCP 客户端](../network-management/dhcp.md#dhcp-client) |
| **80/tcp** | 万维网 HTTP |
| **123/udp** | 网络时间协议 ([NTP](./ntp.md) |
| **161/udp** | 简单网络管理协议 ([SNMP](../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| **179/tcp** | 边界网关协议 ([BGP](../user-guides/routing-and-networking-protocols/unicast/bgp/index.md) |
| **443/tcp** | 安全套接字层 (SSL) 加密 HTTP |
| **500/udp** | 互联网密钥交换 (IKE) 协议 |
| **520/udp 521/udp** | [RIP](../user-guides/routing-and-networking-protocols/unicast/rip.md) 路由协议 |
| **546/udp** | [DHCPv6 客户端](../network-management/dhcp.md) 消息 |
| **547/udp** | [DHCPv6 服务器](../network-management/dhcp.md) 消息 |
| **646/tcp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) 传输会话 |
| **646/udp** | [LDP](../user-guides/routing-and-networking-protocols/mpls/ldp.md) 问候协议 |
| **1080/tcp** | [SOCKS](../network-management/socks/index.md) 代理协议 |
| **1698/udp 1699/udp** | RSVP TE 隧道 |
| **1701/udp** | 二层隧道协议 ([L2TP](../virtual-private-networks/l2tp/index.md)) |
| **1723/tcp** | 点对点隧道协议 ([PPTP](../virtual-private-networks/pptp.md)) |
| **1900/udp 2828/tcp** | 通用即插即用 ([uPnP](../firewall-and-quality-of-service/upnp.md)) |
| **1966/udp** | MME 发起方消息流量 |
| **1966/tcp** | MME 网关协议 |
| **2000/tcp** | 带宽测试服务器 |
| **5246,5247/udp** | [CAPsMAN](../wireless/abgn/capsman/ap-controller-capsman.md) |
| **5350/udp** | NAT-PMP 客户端 |
| **5351/udp** | NAT-PMP 服务器 |
| **5678/udp** | Mikrotik 邻居发现协议 |
| **6343/tcp** | 默认 OpenFlow 端口 |
| **8080/tcp** | HTTP Web 代理 |
| **8291/tcp** | [Winbox](../management-tools/winbox.md) |
| **8728/tcp** | [API](../developer-guides/api/index.md) |
| **8729/tcp** | API-SSL |
| **20561/udp** | MAC winbox |
| **/1** | ICMP |
| **/2** | [组播 \| IGMP](../Multicast%20Routing%20Protocols/igmp-proxy) |
| **/4** | [IPIP](../virtual-private-networks/ipip.md) 封装 |
| **/41** | IPv6（封装） |
| **/46** | RSVP TE 隧道 |
| **/47** | 通用路由封装 (GRE) - 用于 PPTP 和 [EoIP](../virtual-private-networks/eoip.md) 隧道 |
| **/50** | IPv4 封装安全载荷 (ESP) |
| **/51** | IPv4 认证头 (AH) |
| **/89** | [OSPF](../user-guides/routing-and-networking-protocols/unicast/ospf/index.md) 路由协议 |
| **/103** | [组播 \| PIM](../Multicast%20Routing%20Protocols/pim-sm) |
| **/112** | [VRRP](../high-availability-solutions/vrrp.md) |

## Web 服务器

下表显示了可以为 Web 服务启用/禁用的属性列表。所有属性默认启用，如果需要可以禁用。

在此表中，“plain” 指 HTTP 连接，“secure” 指 HTTPS 连接。

| 属性 | 描述 |
| :-- | :-- |
| index-plain: (默认：**yes**) | 主页/登录页面（当 webfig-plain 和 graphs-plain 被禁用时可以禁用） |
| webfig-plain: (默认：**yes**) | WebFig 界面 |
| graphs-plain: (默认：**yes**) | 图形页面 |
| rest-plain: (默认：**yes**) | REST API 支持 |
| crl-plain: (默认：**yes**) | CRL（证书吊销列表） |
| scep-plain: (默认：**yes**) | SCEP（简单证书注册协议） |
| acme-plain: (默认：**yes**) | ACME 挑战 |
| index-secure: (默认：**yes**) | 主页/登录页面（当 webfig-secure 和 graphs-secure 被禁用时可以禁用） |
| webfig-secure: (默认：**yes**) | WebFig 界面 |
| graphs-secure: (默认：**yes**) | 图形页面 |
| rest-secure: (默认：**yes**) | REST API 支持 |