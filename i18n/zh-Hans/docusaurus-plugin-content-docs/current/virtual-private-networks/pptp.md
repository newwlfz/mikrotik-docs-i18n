# PPTP

> 本文档介绍 MikroTik RouterOS 中 PPTP（点对点隧道协议）的实现，涵盖客户端和服务器的配置选项，包括认证方法、MTU/MRRU 设置以及 TCP 端口要求。文档同时强调其安全局限性，并提供 PPTP 客户端连接的配置示例命令。

# PPTP

点对点隧道协议（PPTP）是一种传统的 VPN 协议，旨在封装 PPP 流量以实现远程访问连接。PPTP 被众多操作系统和网络设备广泛支持，使其在兼容性优先的环境中易于部署和配置。

由于存在多个已知的加密和协议级漏洞，PPTP 不被视为保护敏感或不可信网络流量的安全方案。其使用通常仅限于兼容性场景、测试环境或加密强度非首要要求的网络。

PPTP 不支持 IPv6 传输或 IPv6 流量转发。

PPTP 使用 TCP 端口 1723 进行隧道管理，并使用通用路由封装（GRE，IP 协议号 47）进行数据传输，这些端口号由互联网号码分配机构（IANA）分配。为使 PPTP 能正常穿透防火墙或路由器，必须允许并正确转发 TCP 端口 1723 和 GRE 流量。

PPTP 支持每个客户端会话的 PPP 认证、加密和计费机制。认证和计费可在本地执行，也可通过外部 RADIUS 服务器进行。

## PPTP 客户端

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*; 默认值: **no**) | 是否将 PPTP 远端地址添加为默认路由。 |
| **allow** (*mschap2 \| mschap1 \| chap \| pap*; 默认值: **mschap2, mschap1, chap, pap**) | 允许的认证方法。 |
| **connect-to** (*IP*; 默认值: ) | PPTP 服务器的远端地址。 |
| **default-route-distance** (*byte [0..255]*; 默认值: **1**) | 设置自动创建的默认路由所应用的距离值（当同时选择了 add-default-route 时生效）。 |
| **dial-on-demand** (*yes \| no*; 默认值: **no**) | 仅在产生出站流量时连接到 PPTP 服务器。若选择此项，则在连接未建立时，会添加一条网关地址来自 10.112.112.0/24 网络的路由。 |
| **disabled** (*yes \| no*; 默认值: **yes**) | 接口是否禁用。默认情况下为禁用状态。 |
| **keepalive-timeout** (*integer*; 默认值: **60**) | 设置保活超时时间（秒）。 |
| **max-mru** (*integer*; 默认值: **1450**) | 最大接收单元。PPTP 接口在不进行数据包分片的情况下能够接收的最大数据包大小。 |
| **max-mtu** (*integer*; 默认值: **1450**) | 最大传输单元。PPTP 接口在不进行数据包分片的情况下能够发送的最大数据包大小。 |
| **mrru** (*disabled \| integer*; 默认值: **disabled**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，它将被分割为多个数据包，从而允许全尺寸的 IP 或以太网数据包通过隧道传输。 |
| **name** (*string*; 默认值: ) | 接口的描述性名称。 |
| **password** (*string*; 默认值: **""**) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于认证的密码。 |
| **profile** (*name*; 默认值: **default-encryption**) |  |
| **user** (*string*; 默认值: ) | 用于认证的用户名。 |

## PPTP 服务器

**子菜单:** `/interface/pptp-server`

每当与指定服务器建立隧道时，都会创建一个接口。PPTP 服务器的配置中有两种类型的接口：

- 静态接口是在需要引用为特定用户创建的特定接口名称（例如在防火墙规则或其他地方）时，由管理员手动添加的。
- 动态接口是在用户连接且其用户名与任何现有静态条目不匹配时（或在该条目已激活的情况下，因为不能有两个同名的独立隧道接口被引用），自动添加到列表中的。

动态接口在用户连接时出现，在用户断开时消失，因此无法在路由器配置中（例如防火墙中）引用为该用户创建的隧道。因此，如果您需要为该用户设置持久规则，请为其创建静态条目。否则，使用动态配置是安全的。

:::warning
在两种情况下，都必须正确配置 PPP 用户——静态条目不能替代 PPP 配置。
:::

### *属性*

| 属性 | 描述 |
| :-- | :-- |
| **authentication** (*pap \| chap \| mschap1 \| mschap2*; 默认值: **mschap1,mschap2**) | 服务器将接受的认证方法。 |
| **default-profile** (*name*; 默认值: **default-encryption**) |  |
| **enabled** (*yes \| no*; 默认值: **no**) | 定义 PPTP 服务器是否启用。 |
| **keepalive-timeout** (*time*; 默认值: **30**) | 如果在保活周期内服务器未收到任何数据包，它将每秒发送一次保活数据包，共发送五次。如果服务器未收到客户端的响应，则在 5 秒后断开连接。日志将显示 5 次 "LCP missed echo reply" 消息，然后断开连接。 |
| **max-mru** (*integer*; 默认值: **1450**) | 最大接收单元。PPTP 接口在不进行数据包分片的情况下能够接收的最大数据包大小。 |
| **max-mtu** (*integer*; 默认值: **1450**) | 最大传输单元。PPTP 接口在不进行数据包分片的情况下能够发送的最大数据包大小。 |
| **mrru** (*disabled \| integer*; 默认值: **disabled**) | 链路上可接收的最大数据包大小。如果数据包大于隧道 MTU，它将被分割为多个数据包，从而允许全尺寸的 IP 或以太网数据包通过隧道传输。 |

## 示例

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/pptp-01.webp)

### PPTP 客户端

以下示例演示如何设置一个 PPTP 客户端，用户名为 "MT-User"，密码为 "StrongPass"，服务器地址为 192.168.62.2：

```ros
[admin@MikroTik] > /interface/pptp-client/add connect-to=192.168.62.2 disabled=no name=pptp-out1 password=StrongPass user=MT-User
[admin@MikroTik] > /interface/pptp-client/print 
Flags: X - disabled; R - running 
 0  R name="pptp-out1" max-mtu=1450 max-mru=1450 mrru=disabled connect-to=192.168.62.2 user="MT-User" 
      password="StrongPass" profile=default-encryption keepalive-timeout=60 add-default-route=no 
      dial-on-demand=no allow=pap,chap,mschap1,mschap2 
```

### PPTP 服务器

在另一端，我们只需启用 PPTP 服务器并为特定用户创建 PPP 密钥：

```ros
[admin@MikroTik] >  /interface/pptp-server/server/set enabled=yes
[admin@MikroTik] >  /ppp/secret/add local-address=10.0.0.1 name=MT-User password=StrongPass profile=default-encryption remote-address=10.0.0.5 service=pptp
[admin@MikroTik] >  interface pptp-server print
Flags: D - dynamic; R - running
Columns: NAME, USER, MTU, CLIENT-ADDRESS, UPTIME, ENCODING
#      NAME            USER     MTU  CLIENT-ADDRESS  UPTIM  ENCODING         
0  DR  <pptp-MT-User>  MT-User  1450  192.168.51.3   44m8s  MPPE128 stateless
```