# 软件规格

> 本页概述 RouterOS 软件规格，涵盖 MikroTik 设备的硬件兼容性、安装方法、配置工具、备份/恢复功能、防火墙特性、路由协议及 MPLS 支持。

import DocCardList from '@theme/DocCardList';

# 软件规格

#### 硬件支持

**MikroTik 自有设备：** RouterOS 与 MikroTik 硬件兼容，并预装于其上。即使是较老、已停产的 MikroTik 设备也能运行最新版 RouterOS，但需注意性能可能有所差异。对于极早期的产品线存在少数例外。最新 RouterOS v7 不兼容所有 MIPS-LE 系列设备（如 RB100 系列、部分 RB700 系列设备等，请查看具体设备的架构）。简而言之，软件兼容性或升级没有固定限制。即使是已停产 20 年的设备，只要拥有足够的 RAM 且非基于 MIPS-LE CPU，仍可能获得软件更新。

**第三方设备：** 若满足以下要求，RouterOS 也可在第三方设备上运行：

- x86 或 AMPERE 架构的 ARM CPU。
- 至少 64MB 内存。
- IDE、SATA、USB 及闪存存储介质，空间至少 64MB。
- Linux 内核支持的网卡。

:::info
**注意：** NVMe 存储仅支持 CHR、x86、Tile 和 MMIPS 架构。具体信息请参阅各产品手册或框图。
:::

:::info
**注意：** 默认配置的 RouterOS 7 至少需要 32MB 内存，但对于更复杂的配置，建议至少 64MB。
:::

#### 安装

- [Netinstall](../installation-and-upgrade/netinstall)：基于网络的完整安装，通过支持 PXE 或 EtherBoot 的网卡进行。
- [CHR](../installation-and-upgrade/install/chr-installation)：专为虚拟机运行而设计的 RouterOS 版本。
- 基于 CD 的安装。

#### 配置

- 基于 MAC 地址的初始配置访问。
- [WinBox](../../management-tools/winbox) – 独立的 Windows GUI 配置工具。
- [WebFig](../../management-tools/webfig) – 高级的基于 Web 的配置界面。
- MikroTik - [基于 Android 和 iOS 的配置工具](../../management-tools/mikrotik-mobile-app)。
- 强大的命令行配置界面，具备集成脚本功能，可通过本地终端、串口控制台、telnet 和 ssh 访问。
- API – 用于创建自定义配置和监控应用程序的方式。

#### 备份/恢复

- 二进制配置[备份](../../getting-started/configuration-management/backup)的保存与加载。
- 以人类可读文本格式进行[配置导出与导入](../../getting-started/configuration-management#configuration-export-and-import)。

#### 防火墙

- 状态过滤。
- 源和目标 NAT。
- NAT 助手（h323、pptp、quake3、sip、ftp、irc、tftp）。
- 内部连接、路由和数据包标记。
- 按 IP 地址及地址范围、端口及端口范围、IP 协议、DSCP 等进行过滤。
- 地址列表。
- 自定义 Layer7 匹配器。
- IPv6 支持。
- PCC – 每连接分类器，用于负载均衡配置。
- RAW 过滤以绕过连接跟踪。

#### 路由

- 静态路由。
- 虚拟路由转发（VRF）。
- 基于策略的路由。
- 接口路由。
- ECMP 路由。
- IPv4 动态路由协议：RIP v1/v2、OSPFv2、BGP v4。
- IPv6 动态路由协议：RIPng、OSPFv3、BGP。
- 双向转发检测（BFD）。

#### MPLS

- IPv4 静态标签绑定。
- IPv4 标签分发协议。
- RSVP 流量工程隧道。
- 基于 MP-BGP 的 VPLS 自动发现和信令。
- 基于 MP-BGP 的 MPLS IP VPN。

#### VPN

- IPSec – 隧道和传输模式、证书或 PSK、AH 和 ESP 安全协议。
- IKEv2 支持。
- IPSec 的 AES-NI 硬件加速支持。
- 点对点隧道（OpenVPN、PPTP、PPPoE、L2TP、SSTP）。
- 高级 PPP 功能（MLPPP、BCP）。
- BCP 支持于 sstp、ppp、pptp、l2tp 和 pppoe。
- 简单隧道（IPIP、EoIP）支持 IPv4 和 IPv6。
- 6to4 隧道支持（IPv6 over IPv4 网络）。
- VLAN – IEEE802.1q 虚拟局域网支持，Q-in-Q 支持。
- 基于 MPLS 的 VPN。
- WireGuard。
- ZeroTier。

#### 无线

- IEEE802.11a/b/g 无线客户端和接入点。
- 完整 IEEE802.11n 支持。
- Nstreme 和 Nstreme2 专有协议。
- NV2 协议。
- 无线分布系统（WDS）。
- 虚拟 AP。
- WEP、WPA、WPA2。
- 访问控制列表。
- 无线客户端漫游。
- WMM。
- HWMP+ 无线 MESH 协议。
- MME 无线路由协议。

#### DHCP

- 每接口 DHCP 服务器。
- DHCP 客户端和中继。
- 静态和动态 DHCP 租约。
- RADIUS 支持。
- 自定义 DHCP 选项。
- DHCPv6 前缀委派（DHCPv6-PD）。
- DHCPv6 客户端。

#### 热点

- 即插即用的网络访问。
- 本地网络客户端认证。
- 用户计费。
- 支持 RADIUS 认证和计费。

#### QoS

- 分层令牌桶（HTB）QoS 系统，支持 CIR、MIR、突发和优先级。
- 简单队列 – 基础 QoS 实施的简单快速解决方案。
- 动态客户端速率均衡（PCQ）。

#### 代理

- HTTP 缓存代理服务器。
- 透明 HTTP 代理。
- SOCKS 协议支持。
- DNS 静态条目。
- 支持在独立驱动器上缓存。
- 父代理支持。
- 访问控制列表。
- 缓存列表。

#### 工具

- Ping、traceroute
- 带宽测试、ping flood
- 数据包嗅探器、torch
- Telnet、ssh
- 电子邮件和短信发送工具
- 自动化脚本执行工具
- CALEA
- 文件获取工具
- 高级流量生成器
- WoL（网络唤醒）发送

#### 其他功能

- Samba 支持。
- OpenFlow 支持。
- 桥接 – 生成树协议（STP、RSTP）、桥接防火墙和 MAC 地址转换。
- 动态 DNS 更新工具。
- NTP 客户端/服务器及与 GPS 系统同步。
- VRRP v2 和 v3 支持。
- SNMP。
- M3P – MikroTik 数据包打包协议，用于无线链路和以太网。
- MNDP – MikroTik 邻居发现协议，支持 CDP（Cisco 发现协议）。
- RADIUS 认证和计费。
- TFTP 服务器。
- 同步接口支持（仅 Farsync 卡）（在 v5.x 中移除）。
- 异步 – 串行 PPP 拨入/拨出、按需拨号。
- ISDN – 拨入/拨出、128K 捆绑支持、Cisco HDLC、x75i、x75ui、x75bui 线路协议、按需拨号。

#### 内核版本

- RouterOS 6.x 版本使用 3.3.5
- RouterOS 7.x 版本使用 5.6.3

#### 支持的加密方式

RouterOS 7 用于管理网络（电信）设备。

- RouterOS 7 包含加密功能（组件），旨在确保通过电信信道和设备控制信道传输的数据（信息）安全。
- 所有加密功能（组件）均为 RouterOS 7 的组成部分，最终用户无法更改。
- RouterOS 7 旨在供最终用户在无需供应商重大支持的情况下自行安装。
- RouterOS 7 使用以下安全协议。

| 支持的安全协议 | 加密算法 | 最大密钥长度 |
| :-- | :-- | :-- |
|  IPSec | DES | 56 位 |
|  | 3DES | 168 位 |
|  | AES | 128、192、256 位 |
|  | Blowfish | 448 位 |
|  | Twofish | 256 位 |
|  | Camellia | 128、192、256 位 |
| PPTP（使用 MPPE） | RC4 | 128 位 |
| L2TP（使用 MPPE） | RC4 | 128 位 |
| SNMP | DES | 56 位 |
|  | AES | 128 位 |
| SSH | Blowfish | 128 位 |
|  | 3DES | 168 位 |
|  | AES | 128、192、256 位 |
| SSTP | AES | 256 位 |
|  | RC4 | 128 位 |
| 用于 WinBox 连接（未命名） | AES | 128 位 |
| WEP | RC4 | 104 位 |
| WPA-TKIP | RC4 | 128 位 |
| WPA2-TKIP | RC4 | 128 位 |
| WPA-AES | AES | 128 位 |
| WPA2-AES | AES | 128、256 位 |
| WPA3 | AES | 128、256 位 |
| HTTPS | NULL、RC4、DES、DES40、3DES、AES | 128、192、256 位 |

## 相关主题

<DocCardList />