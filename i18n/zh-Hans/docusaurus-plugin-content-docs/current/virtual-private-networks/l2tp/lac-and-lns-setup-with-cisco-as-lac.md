# 使用 Cisco 作为 LAC 的 LAC 和 LNS 设置

> 本页说明如何将 MikroTik RouterOS 设备配置为 L2TP 网络服务器（LNS），以与充当 LAC 的 Cisco 路由器建立 VPDN 连接。内容包括 LAC 上 PPPoE 客户端设置的基本配置示例、LNS 上 L2TP 服务器激活方法，以及适用于两种角色的 RouterOS 命令示例。

# 使用 Cisco 作为 LAC 的 LAC 和 LNS 设置

LAC/LNS 设置，也称为虚拟私有拨号网络（VPDN），允许远程拨号用户与私有网络之间建立长途点对点连接。

拨号客户端使用 PPPoE 连接到 L2TP 接入集中器（LAC），LAC 判断该会话应通过 IP 网络转发至 L2TP 网络服务器（LNS），创建 L2TP 隧道并将 PPP 帧转发至服务器，在服务器上完成客户端认证并建立会话（如下图所示）。

![](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/img/lac-and-lns-setup-with-cisco-as-lac-01.svg)

在撰写本文时，RouterOS 尚不能用作 LAC 角色。因此，本文将演示如何搭建一个非常基础的网络，其中 RouterOS 作为 LNS，Cisco 路由器作为 LAC。

## 配置

我们将使用一个简单的配置来演示 VPDN 设置的基本原理。假设 LAC 会将 FQDN 名称中包含 [mt.lv](https://mt.lv) 域名的客户端转发至 LNS。

### 客户端

为简单起见，假设客户端是一台 RouterOS 路由器：

```ros
/interface/pppoe-client/add interface=ether1 user=good_worker@mt.lv password=strongpass
```

### LAC

假设客户端连接到 GigabitEthernet1 端口，LNS 服务器的 IP 地址为 10.155.101.231

```text
aaa new-model
!
aaa authentication ppp default local
!
vpdn enable
vpdn aaa attribute nas-ip-address vpdn-nas
vpdn search-order domain dnis 
!
vpdn-group LAC
 request-dialin
  protocol l2tp
  domain mt.lv
 initiate-to ip 10.155.101.231
 source-ip 10.155.101.216
 local name LAC
 l2tp tunnel password 0 tunnelpass
!
bba-group pppoe MAIN-BBA
 virtual-template 1
!
interface GigabitEthernet1
 pppoe enable group MAIN-BBA
!
interface Virtual-Template1
 description pppoe MAIN-BBA
 no ip address
 no peer default ip address
 ppp mtu adaptive
 ppp authentication chap
!

```

请注意，此设置既不在本地也不通过 RADIUS 对客户端进行认证，实际上不检查域名，也不控制 L2 访问，仅为简化起见。如需使用这些功能，请参阅 Cisco 配置手册。

### LNS

在 LNS 上，我们需要启用 L2TP 服务器，并设置一种方法来认证来自 LAC 的 L2TP 连接。

```ros
/interface/l2tp-server/server
set enabled=yes
/ppp/l2tp-secret
add address=10.155.101.216/32 secret=tunnelpass
```

接下来是实际的用户认证。为简单起见，本例将使用本地认证方法。

```ros
/ip/pool
add name=pool0 ranges=192.168.99.2-192.168.99.99
/ppp/profile
set default local-address=192.168.99.1 remote-address=pool0
/ppp/secret
add name=good_worker@mt.lv password=strongpass
```

## 状态检查

在 LNS 上，您可以通过检查 l2tp 服务器接口或查看活动的 PPP 连接来查看所有成功连接的客户端：

```text
[admin@CHR_v6_bgp] /interface/l2tp-server> print
Flags: X - disabled, D - dynamic, R - running
# NAME USER MTU CLIENT-ADDRESS UPTIME ENCODING
0 DR <l2tp-... good_worker@mt.lv 1450 10.155.101.216 6h13m49s

[admin@CHR_v6_bgp] /ppp/active> print
Flags: R - radius
# NAME SERVICE CALLER-ID ADDRESS UPTIME ENCODING
0 good_worker@mt.lv l2tp 10.155.101.216 192.168.99.2 6h15m57s 

```

在 LAC 上，我们也可以查看活动的客户端会话以及 LAC 与 LNS 之间的活动 L2TP 隧道：

```text
csrLAC#show vpdn

L2TP Tunnel and Session Information Total tunnels 1 sessions 1

LocTunID RemTunID Remote Name State Remote Address Sessn L2TP Class/
Count VPDN Group
26090 11 CHR_v6_bgp est 10.155.101.231 1 LAC

LocID RemID TunID Username, Intf/ State Last Chg Uniq ID
Vcid, Circuit
18521 16 26090 good_worker@mt.lv, Gi1 est 06:17:07 571

```

## 会话建立

让我们仔细看看客户端会话是如何通过 LAC 进行认证和建立的。

![](https://manual.mikrotik.com/docs/virtual-private-networks/l2tp/img/lac-and-lns-setup-with-cisco-as-lac-02.svg)

- 客户端发起 PPPoE 呼叫。
- LAC 与客户端开始 LCP 协商。
- CHAP 协商完成后，LAC 发送 CHAP 挑战。
- 客户端发送 CHAP 响应。
- LAC 根据收到的域名判断客户端会话是否应转发至 LNS。该检查可在本地完成，也可使用 RADIUS 服务器。在转发会话之前，也可以在此处对客户端进行认证。
- LAC 建立 L2TP 隧道。
- LNS 检查 LAC 是否被允许打开隧道并执行认证过程。隧道建立后即可转发 VPDN 会话。
- LAC 将与客户端协商的 LCP 选项、用户名和密码转发至 LNS。
- LNS 在本地或通过 RADIUS 对客户端进行认证，并发送 CHAP 成功或 CHAP 失败消息。
- 执行 IP 控制协议（IPCP）阶段，安装 IP 地址和路由。此时会话被视为已建立。