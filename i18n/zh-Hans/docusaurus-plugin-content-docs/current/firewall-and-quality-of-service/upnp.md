# UPnP

> MikroTik RouterOS 支持 UPnP 以实现透明的点对点连接，支持动态网络发现和 NAT 穿透。本文档涵盖了通用属性（如接口类型（internal/external）和安全设置），以及如何在路由器接口上启用 UPnP 的配置示例。

# UPnP

MikroTik RouterOS 支持通用即插即用（UPnP）架构，该架构可实现个人计算机与支持网络的设备或电器之间的透明点对点网络连接。

UPnP 允许网络中任何控制设备命令下的任意两个设备之间进行数据通信。该技术完全独立于任何特定的物理介质。它支持具有自动发现功能的网络连接，这意味着设备可以在无需任何初始配置的情况下动态加入网络。DHCP 和 DNS 服务器是可选的，如果网络中存在则会使用。UPnP 实现了一种简单而强大的 NAT 穿透解决方案，使客户端能够从 NAT 后面获得完整的双向点对点网络支持。

UPnP 有两种接口类型：**internal**（本地客户端设备连接的接口）和 **external**（连接到互联网的接口）。路由器只能有一个带有“公网”IP 地址的活动外部接口，以及任意数量的内部接口，所有内部接口都使用源 NAT 的“内部”IP 地址。该协议通过创建动态 NAT 条目规则来工作。

:::info
UPnP **internal** 接口可以为任何子网创建 NAT 映射，而不仅仅是存在于内部接口上的子网，因此在设置 **internal** 接口时必须谨慎。
:::

UPnP 协议被许多现代应用程序使用，例如大多数 DirectX 游戏，以及各种 Windows Messenger 功能，如远程协助、应用程序共享、文件传输、语音和视频通信（在防火墙后面）。

## 配置

### 通用属性

**子菜单：** `/ip/upnp`

| 属性 | 描述 |
| :-- | :-- |
| **allow-disable-external-interface** (*yes \| no*; 默认值：**yes**) | 是否允许用户禁用路由器的外部接口。标准要求此功能（用户无需任何身份验证过程即可关闭路由器的外部接口），但有时在标准未设计的 UPnP 部署中（标准主要设计用于家庭用户建立自己的本地网络），此功能并非预期或不需要，因此您可以禁用此行为 |
| **enabled** (*yes \| no*) | 启用 UPnP 服务 |
| **show-dummy-rule** (*yes \| no*; 默认值：**yes**) | 为某些有缺陷的实现启用一种变通方法，这些实现错误地处理了 UPnP 规则缺失的情况（例如，弹出错误消息）。此选项将指示服务器安装一条虚拟（无意义的）UPnP 规则，以便那些否则无法正常工作的客户端可以观察到该规则 |

:::danger
如果您不禁用 **allow-disable-external-interface**，本地网络中的任何用户都将能够（无需任何身份验证过程）禁用路由器的外部接口。
:::

### UPnP 接口

**子菜单：** `/ip/upnp/interfaces`

| 属性 | 描述 |
| :-- | :-- |
| **interface** (*string*; 默认值：) | UPnP 将运行的接口名称 |
| **type** (*external \| internal*) | UPnP 接口类型：<code>external</code> - 分配了全局 IP 地址的接口<code>internal</code> - 客户端连接的路由器本地接口 |
| **forced-external-ip** (*Ip*; 默认值：) | 允许指定当外部接口有多个可用 IP 时使用哪个公网 IP。 |

:::warning
在更复杂的 VLAN 设置中，如果 VLAN 接口被视为 LAN 接口，则应将该 VLAN 接口本身指定为 internal 接口，UPnP 才能正常工作。
:::

## 配置示例

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/upnp-01.webp)

我们已经在路由器上启用了伪装（masquerading）：

```ros
[admin@MikroTik] /ip/upnp> /ip/firewall/nat/print
Flags: X - disabled, I - invalid, D - dynamic
  0   chain=srcnat action=masquerade out-interface=ether1
[admin@MikroTik] /ip/upnp>
```

要启用 UPnP 功能：

```ros
[admin@MikroTik] /ip/upnp> set enable=yes
[admin@MikroTik] /ip/upnp> print
                             enabled: yes
    allow-disable-external-interface: yes
                     show-dummy-rule: yes
[admin@MikroTik] /ip/upnp>
```

现在，我们只需添加接口：

```ros
[admin@MikroTik] /ip/upnp/interfaces> add interface=ether1 type=external
[admin@MikroTik] /ip/upnp/interfaces> add interface=ether2 type=internal
[admin@MikroTik] /ip/upnp/interfaces> print
Flags: X - disabled
  #   INTERFACE TYPE
  0 X ether1    external
  1 X ether2    internal

[admin@MikroTik] /ip/upnp/interfaces> enable 0,1
```

一旦内部接口侧的客户端发送 UPnP 请求，路由器上就会创建动态 NAT 规则，示例规则可能类似于以下内容：

```ros
[admin@MikroTik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 

0 chain=srcnat action=masquerade out-interface=ether1

1 D ;;; upnp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=tcp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

2 D ;;; upnp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=udp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

```