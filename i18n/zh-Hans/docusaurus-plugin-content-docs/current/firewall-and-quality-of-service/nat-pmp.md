# NAT-PMP

> NAT-PMP 是一种协议，通过动态 NAT 规则将内部 IPv4 地址映射到外部地址，实现透明的点对点连接，客户端和服务端分别使用 UDP 端口 5350 和 5351。

# NAT-PMP

NAT 端口映射协议（NAT-PMP）是一种用于个人计算机及支持网络的智能设备或电器实现透明点对点网络连接的协议。

该协议通过获取 NAT 网关的外部 IPv4 地址，使客户端能够将其外部 IPv4 地址和端口告知希望与之通信的对等方，并通过创建动态 NAT 规则来实现。

NAT-PMP 在客户端使用 UDP 端口号 5350，在服务端使用 UDP 端口号 5351。

PMP 有两种接口类型：**internal**（本地客户端所连接的接口）和 **external**（连接互联网的接口）。路由器只能有一个带有“公网”IP 地址的活动外部接口。

:::warning
路由器只能有一个带有“公网”IP 地址的活动 **external** 接口。NAT-PMP **internal** 接口可以为任何子网创建 NAT 映射，而不仅仅是 internal 接口上存在的子网，因此在设置 **internal** 接口时必须格外谨慎。
:::

有关 NAT-PMP 的更多详细信息，请参阅 [**RFC 6886**](https://www.rfc-editor.org/rfc/rfc6886)。

NAT-PMP 配置可通过 `/ip/nat-pmp` 菜单访问。

## 配置示例

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/img/nat-pmp-01.webp)

假设我们已经有了如上图所示的基本家庭网络设置。

在启用 PMP-NAT 之前，我们需要对出站 LAN 数据包进行伪装（masquerade）。

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether1
```

现在我们可以启用 PMP 并添加 internal、external 接口：

```ros
/ip/nat-pmp/set enable=yes
/ip/nat-pmp/interfaces> add interface=ether1 type=external disabled=no
/ip/nat-pmp/interfaces> add interface=ether2 type=internal disabled=no

```

当 internal 接口侧的客户端发送 PMP 请求时，路由器上会创建动态 NAT 规则：

```text
[admin@MikroTik] > ip firewall nat print 
Flags: X - disabled, I - invalid, D - dynamic 

0 chain=srcnat action=masquerade out-interface=ether1

1 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=tcp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

2 D ;;; nat-pmp 192.168.88.10: ApplicationX
chain=dstnat action=dst-nat to-addresses=192.168.88.10 to-ports=55000 protocol=udp 
dst-address=10.0.0.1 in-interface=ether1 dst-port=55000

```

## 属性

### 常规属性

可通过 `/ip/nat-pmp` 菜单访问。

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*) | 启用 NAT-PMP 服务 |

### NAT-PMP 接口

可通过 `/ip/nat-pmp/interfaces` 菜单访问。

| 属性 | 描述 |
| :-- | :-- |
| **interface** (*string*; 默认值: ) | 运行 PMP 的接口名称 |
| **type** (*external \| internal*) | PMP 接口类型：<code>external</code> - 分配了全局 IP 地址的接口<code>internal</code> - 客户端所连接的路由器本地接口 |
| **forced-ip** (*Ip*; 默认值: ) | 当 external 接口有多个可用 IP 时，允许指定使用哪个公网 IP。 |

:::warning
在包含 VLAN 的更复杂网络设置中，如果 VLAN 接口属于 LAN 的一部分，则为了 PMP 正常工作，应将 VLAN 接口本身指定为 internal 接口。
:::