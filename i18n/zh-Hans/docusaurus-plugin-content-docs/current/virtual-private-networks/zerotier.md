# ZeroTier

> ZeroTier 是 MikroTik RouterOS 的网络虚拟化引擎，通过以太网虚拟化和加密的点对点网络实现安全、跨网络的设备连接。它支持游戏、局域网访问、NAT 穿透和远程 Pi-Hole 管理，同时需要正确的 UDP 端口配置、NAT 类型选择以及最少的 NAT 层级以确保连接可靠。

# ZeroTier

[ZeroTier](https://docs.zerotier.com/) 网络虚拟化平台是一个自包含的网络虚拟化引擎，实现了类似于 VXLAN 的以太网虚拟化层，构建在加密安全的全球点对点网络之上。它提供与企业级 SDN 交换机相当的高级网络虚拟化和管理能力，但可跨越局域网和广域网，连接几乎任何类型的应用或设备。

MikroTik 已在 RouterOS v7.1rc2 中为 **ARM/ARM64** 架构添加了 ZeroTier 独立软件包。

### 等等，那它能用来做什么？

- 在家中托管游戏服务器（适用于仅限局域网的游戏），或与朋友创建局域网派对。
- 直接访问 NAT 后面的局域网设备。
- 通过 SSH 访问局域网设备，而无需向互联网开放端口。
- 通过互联网从任何地方使用本地的 Pi-Hole 设置。

:::info
重要提示

ZeroTier 功能可能被设备模式（device-mode）阻止。在配置 ZeroTier 之前，请确保已在 system/device-mode 中启用该功能。（[更多信息](../system-information-and-utilities/device-mode.md)）
:::

### 视频教程

- [ZeroTier](https://youtu.be/60uIlyF8Z5s)

## 所需网络配置

### ZeroTier 使用哪些端口？

它监听 3 个 UDP 端口：

- 9993 - 默认端口
- 一个由 ZeroTier 地址派生的随机高位端口
- 一个用于 UPnP/NAT-PMP 映射的随机高位端口

这意味着您的 *对等节点* 可能监听任意端口。要直接与它们通信，您需要能够向任意端口发送数据。

### 推荐的本地网络和互联网网关配置

以下 ZeroTier 推荐指南与绝大多数使用普通网关和接入点的典型部署场景一致：

- 不要限制出站 UDP 流量。
- 在网络中支持 UPnP 或 NAT-PMP 可以大幅提升性能，使 ZeroTier 端点能够映射外部端口并完全避免 NAT 穿透。
- 建议使用 IPv6，如果直连链路两端均支持，可大幅提升直接连接的可靠性。如果存在 IPv6，应无需 NAT 实现（IPv6 完全不需要 NAT，只会增加复杂性），并使用允许双向 UDP 会话的有状态防火墙。
- 不要使用“对称型”NAT。请使用“全锥型”或“端口限制锥型”NAT。对称型 NAT 对点对点流量极为不利，会降低 VoIP、视频聊天、游戏、WebRTC 以及许多其他协议和 ZeroTier 的性能。
- ZeroTier 端点和互联网之间不应存在超过一层的 NAT。多层 NAT 会因不同层级状态和行为之间的混乱交互而导致连接不稳定。**禁止双重 NAT。**
- NAT 的端口映射或连接超时时间不应短于 60 秒。
- 每个 NAT 管理的外部 IP 地址后面不要放置超过约 16,000 台设备，以确保每台设备都能映射足够数量的端口。
- 交换机和无线接入点应允许本地设备之间的直接本地流量。关闭所有“本地隔离”功能。某些交换机可能支持更细粒度的控制，在这些交换机上，允许本地 UDP 流量进出 9993 端口（或一般情况）即可。

## 配置示例

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-01.webp)

默认情况下，ZeroTier 设计为零配置。用户可以启动新的 ZeroTier 节点，无需编写配置文件或提供其他节点的 IP 地址。它还设计为快速运行。世界上任意两台设备都应能几乎瞬间找到彼此并进行通信，因此以下示例将在 RouterOS 设备上启用 ZeroTier，并连接一台使用 ZeroTier 应用程序的手机。

1. 在 [my.zerotier.com](https://my.zerotier.com/) 注册并 **创建网络**，获取 *网络 ID*，本示例中为：*1d71939404912b40*。  
   ![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-02.webp)
2. [下载](https://mikrotik.com/download) 并在 RouterOS 中安装 ZeroTier NPK 软件包，您可以在“Extra packages”下找到它，将软件包上传到设备并重启设备。
3. 启用默认（官方）ZeroTier 实例：

   ```ros
   [admin@MikroTik] > /zerotier/enable zt1
   ```

4. 添加新网络，指定您在 ZeroTier 云控制台中创建的网络 ID：

   ```ros
   [admin@mikrotik] /zerotier/interface/add network=1d71939404912b40 instance=zt1
   ```

5. 验证 ZeroTier 配置：

   ```ros
   [admin@MikroTik] > /zerotier/interface/print
   Flags: R - RUNNING
   Columns: NAME, MAC-ADDRESS, NETWORK, NETWORK-NAME, STATUS
   #   NAME       MAC-ADDRESS        NETWORK           NETWORK-NAME     STATUS
   0 R zerotier1  42:AC:0D:0F:C6:F6  1d71939404912b40  modest_metcalfe  OK   
   ```

6. 现在您可能需要允许从 ZeroTier 接口到路由器的连接，并且**可选地**，允许到其他局域网接口的连接：

   ```ros
   /ip/firewall/filter/add action=accept chain=forward in-interface=zerotier1 place-before=0
   /ip/firewall/filter/add action=accept chain=input in-interface=zerotier1 place-before=0
   ```

7. 在您的智能手机或计算机上安装 ZeroTier 客户端，按照 ZeroTier 手册从那里连接到同一网络。
8. 如果 **“访问控制”** 设置为 **“私有”**，您必须先授权节点，然后它们才能成为成员：  
   ![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-03.webp)

9. ```ros
   [admin@MikroTik] > `/ip/address/print` where interface~"zero"
   Flags: D - DYNAMIC
   Columns: ADDRESS, NETWORK, INTERFACE
   #   ADDRESS             NETWORK        INTERFACE
   3 D 192.168.192.105/24  192.168.192.0  zerotier1

   [admin@MikroTik] > ping 192.168.192.252 count=3
   SEQ HOST                                     SIZE TTL TIME       STATUS                                                                                                                                           
   0 192.168.192.252                            56  64 407us     
   1 192.168.192.252                            56  64 452us     
   2 192.168.192.252                            56  64 451us     
   sent=3 received=3 packet-loss=0% min-rtt=407us avg-rtt=436us max-rtt=452us 
   ```

:::tip
您应该在 [ZeroTier 云控制台](https://my.zerotier.com/) 中指定到特定内部子网的路由，以确保从其他设备连接时能够访问这些网络。
:::

### 对等节点

**子菜单：** `/zerotier/peer`

ZeroTier 的对等节点是一个信息展示区域，列出了您的节点已知的节点列表。节点之间无法通信，除非它们已加入同一网络并获得授权。

```ros
[admin@Home] > `/zerotier/peer/print` 
Columns: INSTANCE, ZT-ADDRESS, LATENCY, ROLE, PATH
# INSTANCE  ZT-ADDRESS  LATENCY  ROLE    PATH
0 zt1       61d294b9cb  186ms    PLANET  active,preferred,50.7.73.34/9993,recvd:4s526ms                  
1 zt1       62f865ae71  270ms    PLANET  active,preferred,50.7.252.138/9993,recvd:4s440ms,sent:9s766ms   
2 zt1       778cde7190  132ms    PLANET  active,preferred,103.195.103.66/9993,recvd:4s579ms,sent:9s766ms 
3 zt1       992fcf1db7  34ms     PLANET  active,preferred,195.181.173.159/9993,recvd:4s675ms,sent:4s712ms
4 zt1       159924d630  130ms    LEAF    active,preferred,34.121.192.xx/21002,recvd:3s990ms,sent:3s990ms
```

# 参数

**子菜单：** `/zerotier`

| 属性                                                                                                                                          | 描述                                                                                                 |
|:--|:--|
| **name**(*string*; 默认值：**zt1**)                                                                                                              | 实例名称。                                                                                              |
| **port** (*number*; 默认值：**9993**)                                                                                                             | 实例监听的端口号。                                                                         |
| **identity** (*string*; 默认值) *[敏感参数](https://help.MikroTik.com/docs/spaces/ROS/pages/380076066/List+of+menus+with+sensitive+parameters)* | 实例的 40 位唯一地址。                                                                             |
| **interface** (string; 默认值：**all**)                                                                                                          | 用于通过 ARP 和 IP 类型连接发现 ZeroTier 对等节点的接口列表。 |
| **route-distance** (number; 默认值：**1** )                                                                                                      | 从 planet/moon 服务器获取的路由的路由距离。                                                |

```ros
[admin@MikroTik] > zerotier/interface/
```

| 属性                                       | 描述                                                        |
|:--|:--|
| **allow-default** (*string; yes \| no*)         | 网络可以覆盖系统的默认路由（强制 VPN 模式）。 |
| **allow-global**(*string; yes \| no*)           | ZeroTier IP 地址和路由可以重叠公共 IP 空间。      |
| **allow-managed**(*string; yes \| no*)          | 分配 ZeroTier 管理的 IP 地址和路由。             |
| **arp-timeout** ( *number*; 默认值：**auto**) | ARP 超时值。                                                |
| **comment** (*string*; 默认值：)              | 接口的描述性注释。                            |
| **copy-from**                                  | 允许复制现有接口配置。                  |
| **disable-running-check**(*string; yes \| no*)  | 强制接口处于“运行”状态。                                |
| **instance**(*string*; 默认值：**zt1**)        | ZeroTier 实例名称。                                            |
| **name**(*string*; 默认值：**zerotier1**)     | 短名称。                                                      |
| **network**(*string*; 默认值)                 | 16 位网络 ID。                                               |

# 控制器

RouterOS 以节点角色实现 ZeroTier 功能，大部分网络配置必须在 ZeroTier 网页仪表板上完成。但是，如果您更倾向于在自己的设备上完成所有配置，RouterOS 也支持托管您自己的控制器。

一个常见的误解是将网络控制器与根服务器（planet 和 moon）混为一谈。根服务器是连接促进器，运行在 **[VL1 层](https://docs.zerotier.com/zerotier/manual/#2networkhypervisoroverviewaname2a)**。网络控制器是配置管理器和证书颁发机构，属于 **[VL2 层](https://docs.zerotier.com/zerotier/manual/#22vl2theethernetvirtualizationlayeraname2_2a)**。一般来说，根服务器不加入或控制虚拟网络，网络控制器也不是根服务器，尽管一个节点可以同时承担两种角色。

**子菜单：** `/zerotier/controller`

每个 ZeroTier 实例都有一个自托管的网络控制器，可用于托管虚拟网络。控制器负责接纳网络成员，并发布包括证书在内的默认配置信息。理论上，控制器最多可以托管 2^24 个网络，并为数百万台设备（或更多）提供服务，但我们建议将大量网络分散到多个控制器上，以实现负载均衡和容错。

## 参数

| 属性                                         | 描述                                                                                                                                                                                                                                                                                                          |
|:--|:--|
| **broadcast** *( yes \| no; 默认值：**yes**)*    | 允许接收广播（*FF:FF:FF:FF:FF:FF*）数据包。                                                                                                                                                                                                                                                             |
| **comment** (*string*; 默认值：)                | 控制器的描述性注释。                                                                                                                                                                                                                                                                              |
| **copy-from** (*string*; 默认值：)         | 复制现有项目。它从另一个项目获取新项目属性的默认值。如果您不想完全复制，可以为某些属性指定新值。复制具有名称的项目时，通常需要为新副本指定新名称。                                     |
| **instance** (*string*; 默认值：**zt1**)        | ZeroTier 实例名称。                                                                                                                                                                                                                                                                              |
| **ip-range** (*IP*; 默认值：)                   | IP 范围，*例如，172.16.16.1-172.16.16.254。*                                                                                                                                                                                                                                                                  |
| **ip6-6plane** *( yes \| no; 默认值：**no**)*    | 此选项为每个成员分配 /40 网络内的 /80 地址段，但使用 NDP 仿真将所有该 /80 下的 *所有* IP 路由到其所有者。`6plane` 模式非常适合 Docker 等使用场景，因为它允许每个成员在其 /80 内分配 IPv6 地址，这些地址可以即时生效并在整个网络中全局可用。 |
| **ip6-rfc4193** *( yes \| no; 默认值：**no**)*   | *rfc4193* 模式为每个成员分配 /88 网络上的 /128 地址。                                                                                                                                                                                                                                                       |
| **ip6-range** (*IPv6*; 默认值：)                | IPv6 范围，*例如 fd00:feed:feed:beef::-fd00:feed:feed:beef:ffff:ffff:ffff:ffff。*                                                                                                                                                                                                                             |
| **mtu** *(integer;* 默认值：**2800**)           | 网络 MTU。                                                                                                                                                                                                                                                                                                         |
| **multicast-limit** (*integer*: 默认值：**32**) | 组播数据包的最大接收者数量。                                                                                                                                                                                                                                                                           |
| **name** (*string*; 默认值：)                   | 此控制器的短名称。                                                                                                                                                                                                                                                                                    |
| **network** (*string*; 默认值)                  | 16 位网络 ID。                                                                                                                                                                                                                                                                                                 |
| **private** *( yes \| no; 默认值：**yes**)*      | 启用访问控制。                                                                                                                                                                                                                                                                                              |
| **routes** (*IP@GW*; 默认值：)                  | 以下列格式推送路由：*Routes ::= Route[,Routes]* *Route ::= Dst[@Gw]*                                                                                                                                                                                                                                |

## 配置示例

在以下示例中，我们将使用 RouterOS 内置的 ZeroTier 控制器向新网络主机发送适当的证书、凭据和配置信息。控制器将在“RouterOS Home”设备上运行，我们将把 3 台设备加入网络：手机、笔记本电脑、RouterOS Office 设备，但理论上，您可以在一个网络中连接多达 100 台设备。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-04.webp)

### RouterOS Home

首先，我们启用运行在 **VL1** 层的默认实例：

```ros
[admin@Home] /zerotier> print
Columns: NAME, PORT, IDENTITY.PUBLIC
# NAME  PORT  IDENTITY.PUBLIC
;;; ZeroTier Central controller - https://my.zerotier.com/
0 zt1   9993  879c0b5265:0:d5fd2d17805e011d9b93ce8779385e427c8f405e520eea9284809d8444de0335a817xxb21aa4ba153bfbc229ca34d94e08de96d925a4aaa19b252da546693a28
```

现在我们通过控制器部分创建一个新网络，该网络将运行在 **VL2** 层。每个网络都有自己的控制器，每个网络 ID 由控制器地址和控制器 ID 组合生成。

请注意，我们使用 ***private=yes*** 选项以获得更安全的网络：

```ros
[admin@Home] /zerotier> controller/add name=ZT-private instance=zt1 ip-range=172.27.27.10-172.27.27.20 private=yes routes=172.27.27.0/24
[admin@Home] /zerotier> controller/print
Columns: INSTANCE, NAME, NETWORK, PRIVATE
# INSTANCE  NAME        NETWORK           PRIVATE
0 zt1       ZT-private  879c0b5265a99e4b  yes
```

在接口部分添加我们的新网络：

```ros
[admin@Home] /zerotier> interface/add network=879c0b5265a99e4b name=myZeroTier instance=zt1 
[admin@Home] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME        MAC-ADDRESS        NETWORK           STATUS
0 myZeroTier  4A:19:35:6E:00:6E  879c0b5265a99e4b  ACCESS_DENIED
```

每个新对等节点都会向控制器请求加入网络，在这种情况下，我们收到 *ACCESS\_DENIED* 状态，必须授权新对等节点，这是因为我们使用了 **private=yes** 选项。

授权后，网络中的每个成员都会从控制器收到关于新对等节点的信息以及可以与其交换数据包的批准：

```ros
[admin@Home] /zerotier> controller/member/print
Columns: NETWORK, ZT-ADDRESS
# NETWORK     ZT-ADDRESS
0  ZT-private  879a0b5265
[admin@Home] /zerotier> controller/member/set 0 authorized=yes
```

## 验证新配置的 IP 地址和路由

```ros
[admin@Home] /zerotier> `/ip/address/print` where interface~"Zero"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
4 D 172.27.27.15/24  172.27.27.0  myZeroTier

[admin@Home] /zerotier> `/ip/route/pr` where gateway~"Zero"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY     DISTANCE
DAc 172.27.27.0/24  myZeroTier         0
```

### RouterOS Office

Office 设备上的配置。我们将启用默认实例，并请求控制器加入 *879c0b5265a99e4b* 网络：

```ros
[admin@office] /zerotier> interface/add network=879c0b5265a99e4b instance=zt1 name=ZT-interface 
[admin@office] /zerotier> interface/print interval=1
Columns: NAME, MAC-ADDRESS, NETWORK, STATUS
# NAME          MAC-ADDRESS        NETWORK           STATUS
0 ZT-interface  4A:40:1C:38:97:BA  879c0b5265a99e4b  ACCESS_DENIED
```

与之前一样，由于我们的网络是私有的，我们必须通过“RouterOS home device”授权新对等节点。之后验证从控制器接收的 IP 地址和路由：

```ros
[admin@Home] /zerotier> controller/member/print
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3    ZT-private  deba5dc5b1  172.27.27.13  3s348ms  
[admin@Home] /zerotier> controller/member/set 3 authorized=yes
[admin@Home] /zerotier> controller/member/print               
Flags: A - AUTHORIZED
Columns: NETWORK, ZT-ADDRESS, IP-ADDRESS, LAST-SEEN
# NETWORK     ZT-ADDRESS  IP-ADDRESS    LAST-SEEN
0 A  ZT-private  879a0b5265  172.27.27.15           
1 A  ZT-private  554a914c7f  172.27.27.17           
2 A  ZT-private  a83ac6032a  172.27.27.10           
3 A  ZT-private  deba5dc5b1  172.27.27.13  4s55ms 
```

通过 ZeroTier 验证获取的 IP 地址和路由：

```ros
[admin@office] /zerotier> `/ip/address/print` where interface~"ZT"
Flags: D - DYNAMIC
Columns: ADDRESS, NETWORK, INTERFACE
# ADDRESS          NETWORK      INTERFACE
0 D 172.27.27.13/24  172.27.27.0  ZT-interface

[admin@office] /zerotier> `/ip/route/print` where gateway~"ZT"
Flags: D - DYNAMIC; A - ACTIVE; c, y - COPY
Columns: DST-ADDRESS, GATEWAY, DISTANCE
    DST-ADDRESS     GATEWAY       DISTANCE
DAc 172.27.27.0/24  ZT-interface         0
```

### 其他设备

[下载 ZeroTier 应用](https://www.zerotier.com/download/) 到您的手机或计算机，并加入您新创建的网络：

1) 通过我们的笔记本电脑 ZeroTier 应用加入 *879c0b5265a99e4b* 网络；

2) 使用 ZeroTier 手机应用加入 *879c0b5265a99e4b* 网络；

:::warning
所有其他新主机也必须在 */zerotier/controller/member/* 部分进行授权。
:::

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-05.webp)

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/zerotier-network-config.png)