# 默认配置

> 本页介绍各类 MikroTik RouterOS 设备的默认配置，包括 CPE 路由器、LTE CPE AP 路由器及其他接口类型。文中概述了每种配置类型的具体设置，如 WAN/LAN 接口、防火墙规则及 DHCP 配置。

# 默认配置

所有 MikroTik 设备均附带某种默认配置。根据主板类型，存在多种不同的配置：

- CPE 路由器
- LTE CPE AP 路由器
- AP 路由器（单频或双频）
- PTP 网桥、W60G 网桥（AP 或 CPE）
- WISP 网桥（ap\_bridge 模式下的 AP）
- 交换机
- 仅 IP
- CAP

您可以运行命令 `/system/default-configuration/print` 查看实际应用的默认配置命令。

## CPE 路由器

在此类配置中，路由器被配置为无线客户端设备。WAN 接口为**无线**接口。WAN 端口配置了 DHCP 客户端，受 IP 防火墙保护，且 MAC 发现/连接功能已禁用。

使用此类配置的路由器列表：

- RB 711,911,912,921,922 - 搭载 level3 许可证
- SXT
- QRT
- SEXTANT
- LHG
- LDF
- DISC
- Groove
- Metal

:::info
CPE 路由器模式：

- \* 无线接口连接至提供商网络（WAN 端口）；
- \* WAN 端口受防火墙保护，并启用 DHCP 客户端

wlan1 配置：

- mode: station;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation: outdoor;
- wpa2: no;
- ht-extension: 20/40mhz-XX;

LAN 配置：

- IP 地址 192.168.88.1/24 设置在 ether1（LAN 端口）上
- DHCP 服务器：已启用；
- DNS：已启用；

WAN（网关）配置：

- gateway:wlan1 ;
- ip4 firewall: 已启用；
- ip6 firewall: 已启用；
- NAT: 已启用；
- DHCP 客户端：已启用；

## 登录

- admin 用户受密码保护

配置**预览**：  
[CPE_Router.txt](pathname:///assets/167706794_CPE_Router.txt)。

:::

## LTE CPE AP 路由器

此配置类型应用于同时具备 LTE 和无线接口的路由器。LTE 接口被视为 WAN 端口，受防火墙保护，且 MAC 发现/连接功能已禁用。WAN 端口上的 IP 地址自动获取。无线接口配置为接入点，并与所有可用的以太网端口桥接。

使用此类配置的路由器列表：

- wAP LTE Kit
- SXT LTE
- LtAP 4G kit
- LtAP LTE kit
- Chateau

:::info

### CPE 路由器模式

\* 无线接口连接至提供商网络（WAN）

此处指 LTE 接口，而非无线接口。

\* WAN 端口受防火墙保护，并启用 DHCP 客户端）

### LAN 配置

- IP 地址 192.168.188.1/24 设置在桥接（LAN 端口）上
- DHCP 服务器：已启用；
- DNS：已启用；

### WAN（网关）配置

- gateway:lte1 ;
- ip4 firewall: 已启用；
- ip6 firewall: 已启用；
- NAT: 已启用；

### 登录

- admin 用户受密码保护

配置**预览**：  
[LTE_CPE_AP_router.txt](pathname:///assets/167706791_LTE_CPE_AP_router.txt)。

:::

## AP 路由器

此配置类型应用于家用接入点路由器，开箱即用，无需额外配置（路由器密码和无线密钥除外）。

第一个以太网端口始终配置为 WAN 端口（受防火墙保护、启用 DHCP 客户端，并禁用 MAC 连接/发现）。其他以太网端口和无线接口加入本地 LAN 桥接，设置 192.168.88.1/24 地址并配置 DHCP 服务器。对于双频路由器，一个无线接口配置为 5 GHz 接入点，另一个配置为 2.4 GHz 接入点。

使用此类配置的路由器列表：

- RB 450,751,850,951,953,2011,3011,4011
- hEX, PowerBox
- mAP
- wAP, wAP R（不带 LTE 卡）
- hAP
- cAP
- OmniTIK
- 带无线接口的 CRS 系列
- L009 系列
- Audience
- Knot
- PWR

:::info

### 路由器模式

\* WAN 端口受防火墙保护，并启用 DHCP 客户端

\* 无线和以太网接口（除 WAN 端口外）属于 LAN 桥接的一部分

### LAN 配置

- IP 地址 192.168.88.1/24 设置在桥接（LAN 端口）上
- DHCP 服务器：已启用；
- DNS：已启用；

### wlan1 配置

- mode: ap-bridge;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation: indoor;
- wpa2: no;
- ht-extension: 20/40mhz-XX;

### WAN（网关）配置

- ip4 firewall: 已启用；
- ip6 firewall: 已启用；
- NAT: 已启用；
- DHCP 客户端：已启用；

### 登录

- admin 用户受密码保护

### 配置**预览**

[RouterMode.txt](pathname:///assets/167706790_RouterMode.txt)

:::

## PTP 网桥、W60G 网桥

以太网与无线接口桥接。默认 IP 地址 192.168.88.1/24 设置在桥接接口上。有两种可选模式 - CPE 和 AP。对于 CPE，无线接口设置为 "station-bridge" 模式；对于 AP，则使用 "bridge" 模式。W60G 网桥 - 此配置类型应用于具有 60 GHz 点对点链路的路由器。

:::info
PTP 网桥：

\* 无线和 LAN 接口已桥接；

### LAN 配置

#### 登录

- admin 用户受密码保护

配置**预览**：  
[PTP_Bridge.txt](pathname:///assets/167706792_PTP_Bridge.txt)

:::

使用此类配置的路由器列表：

- DynaDish - 作为 CPE

:::info
W60G 网桥：

 \* W60G 和 LAN 接口已桥接；

### wlan60-1 配置

- SSID: MikroTik;
- mode:station-bridge;
- password: no;
- IP 地址 192.168.88.1/24 设置在桥接上

#### 登录

- admin 用户受密码保护

配置**预览**：  
[W60G_Bridge.txt](pathname:///assets/167706793_W60G_Bridge.txt)

:::

## 使用此类配置的路由器列表

- Cube, Cube Pro
- nRAY, Dish
- Wireless Wire kit
- wAP 60G - 搭载 level3 许可证

## WISP 网桥

配置与 AP 模式下的 PTP 网桥相同，区别在于无线模式设置为 ap\_bridge 以支持 PTMP 组网。可通过 MAC 地址直接访问路由器。如果设备连接到启用了 DHCP 服务器的网络，桥接接口上配置的 DHCP 客户端将获取 IP 地址，可用于访问路由器。

使用此类配置的路由器列表：

- RB 911,912,921,922 - 搭载 Level4 许可证。
- Groove A, RB 711 A
- BaseBox, NetBox
- mANTBox, NetMetal
- wAP 60G AP - 搭载 level4 许可证。
- LtAP
- CME

:::info
WISP 网桥：

 \* 无线和 LAN 接口已桥接；

### wlan1 配置

- mode: ap-bridge;
- band: 2ghz-b/g/n;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation:   outdoor;
- wpa2: no;
- ht-extension:   20/40mhz-XX;

### wlan2 配置

- mode: ap-bridge;
- band: 5ghz-a/n/ac;
- tx-chains: 0;1;
- rx-chains: 0;1;
- installation:   outdoor;
- wpa2: no;
- ht-extension:   20/40/80mhz-XXXX;

### LAN 配置

- DHCP 客户端：在桥接（LAN 端口）上启用；

### 登录

- admin 用户受密码保护

配置**预览**：  
[WISP_Bridge.txt](pathname:///assets/167706789_WISP_Bridge.txt)

:::

## 交换机

此配置利用交换芯片功能来配置基本交换机。所有以太网端口加入交换机组，默认 IP 地址 192.168.88.1/24 设置在桥接接口上。

使用此类配置的路由器列表：

- FiberBox
- 不带无线接口的 CRS

:::info
交换机模式：

- 所有接口已交换；

### 登录

- admin 用户受密码保护

配置**预览**：  
[switch.txt](pathname:///assets/234914118_switch.txt)

:::

## 仅 IP

当未找到特定配置时，IP 地址 192.168.88.1/24 设置在 ether1、combo1 或 sfp1 上。

使用此类配置的路由器列表：

- RB 411,433,435,493,800,M11,M33,1100
- CCR, ROSE Data server

:::info

### LAN

- etherx 上的 IP：192.168.88.1/24；

### 登录

- admin 无密码。

### 配置预览  

[ccr.txt](pathname:///assets/234914117_ccr.txt)

:::

## CAP

当设备需要用作由 [CAPsMAN](../../wireless/abgn/capsman/index.md) 控制的无线客户端设备时，使用此配置类型。

加载 CAP 默认配置后，ether1 被视为管理端口，并配置了 DHCP 客户端。所有其他以太网接口均已桥接，wlan1 设置为由 CAPsMAN 管理。

要加载 CAP 配置，请参阅 [Reset Button manual](./routeros-configuration-reset.md)。