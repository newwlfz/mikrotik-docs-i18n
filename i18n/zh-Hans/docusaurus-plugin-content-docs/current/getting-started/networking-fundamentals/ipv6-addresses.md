# IPv6 地址

> 本页介绍 MikroTik RouterOS 中的 IPv6 寻址，涵盖其相对于 IPv4 的优势、地址类型与语法、通过零压缩实现的简化表示、前缀表示法，以及由组播取代广播地址的情况。

# IPv6 地址

互联网协议第六版（IPv6）是互联网协议（IP）的新版本。最初预计在较短时间内取代 IPv4，但目前看来，在可预见的未来，这两个版本将在互联网上共存。尽管如此，随着未分配 IPv4 地址池枯竭日期的临近，IPv6 变得越来越重要。

- 四大主要优势：

- 更大的地址空间；
- 支持无状态和有状态地址自动配置；
- 内置安全性；
- 新的报头格式（更快的转发）。

IPv6 使用 16 字节地址，而 IPv4 使用 4 字节地址。IPv6 地址语法和类型在 [RFC 4291](https://tools.ietf.org/html/rfc4291) 中描述。

有多种 IPv6 地址类型，可通过其前缀识别。RouterOS 区分以下类型：

- 组播（前缀为 ff00::/8）
- 链路本地（前缀为 fe80::/10）
- 唯一本地地址（前缀为 fc00::/7）
- 环回（地址 ::1/128）
- 未指定（地址 ::/128）
- 其他（所有其他地址，包括已废弃的站点本地地址和 [RFC 4193](https://tools.ietf.org/html/rfc4193) 唯一本地地址；它们均被视为全局单播）。

IPv6 与 IPv4 地址的一个区别是，IPv6 会为每个支持 IPv6 的活动接口自动生成一个**链路本地** IPv6 地址。

IPv6 地址的表示方式与 IPv4 地址略有不同。对于 IPv6，128 位地址被分为八个 16 位块，每个 16 位块转换为 4 位十六进制数字，并用冒号分隔。由此产生的表示形式称为冒号十六进制。

在下面的示例中，二进制格式的 IPv6 地址被转换为冒号十六进制表示形式

```
0010000000000001 0000010001110000 0001111100001001 0000000100110001
0000000000000000 0000000000000000 0000000000000000 0000000000001001
```

```
2001:0470:1f09:0131:0000:0000:0000:0009
```

IPv6 地址可以通过去除每个块中的前导零进一步简化：

```
2001:470:1f09:131:0:0:0:9
```

如您所见，IPv6 地址可能包含长串的零。这个连续的序列可以压缩为 **::**

```
2001:470:1f09:131::9
```

:::note
零压缩只能使用一次。否则，您将无法确定每个双冒号实例所表示的 0 位数。
:::

IPv6 前缀以 **地址/前缀长度** 格式书写。与 IPv4 不同，IPv6 不能使用十进制表示的网络掩码。前缀示例：

```
2001:470:1f09:131::/64
2001:db8:1234::/48
2607:f580::/32
2000::/3
```

IPv6 网络中没有**广播地址**，广播功能已完全被组播取代。

### 单播地址

发送到单播地址的数据包仅传送到单个接口。此组包括：

- 全局唯一地址，可用于连接到全球范围内的任何地址；
- 链路本地地址；
- 唯一本地地址（ULA RFC4193）
- 站点本地地址（FEC0::/10）- 已废弃；
- 特殊用途地址；
- 兼容性地址；

全局单播地址可以通过**无状态地址自动配置**自动分配给节点。

### 链路本地地址

每个启用 IPv6 的接口都需要链路本地地址，应用程序即使在没有 IPv6 路由的情况下也可能依赖链路本地地址的存在，这就是为什么每个活动接口都会使用其接口标识符（如果存在 MAC 地址，则计算 EUI-64）自动生成链路本地地址。地址前缀始终为 **FE80::/64**，IPv6 路由器绝不会将链路本地流量转发到链路之外。

这些地址可类比于 IPv4 的自动配置地址 169.254.0.0/16。

链路本地地址也是 IPv6 邻居发现过程所必需的。

:::info
如果接口被设置为桥接端口，则特定于接口的链路本地地址将被移除，仅保留桥接的链路本地地址。
:::

### 唯一本地地址

唯一本地地址（ULA）保留用于家庭和企业环境中的本地使用，不会在公共地址空间中路由，相当于 IPv4 私有地址范围。

保留地址范围为 **fc00::/7**

### 特殊用途地址

| 地址                             | 描述                                                                                                                                           |
|:--|:--|
| **未指定地址 (::/128)**          | 从不分配给接口或用作目的地址，仅用于表示地址不存在。相当于 IPv4 的 0.0.0.0 地址。                                                              |
| **环回地址 (::1/128)**           | 用于标识环回接口，使节点能够向自身发送数据包。相当于 IPv4 的环回地址 127.0.0.1。                                                              |
| **2002::/16**                    | 此前缀用于 6to4 寻址。此处，也使用了 IPv4 网络 192.88.99.0/24 中的地址。                                                                        |
| **2001:db8::/32**                | 为文档用途保留的地址范围。这些地址不应作为源地址或目的地址出现。                                                                               |
| **2001:0010::/28**               | Orchid 固定期限实验。不应作为源地址或目的地址出现。                                                                                             |
| **2001:0002::/48**               | 用于基准测试，不应作为源地址或目的地址出现。                                                                                                   |
| **2001:0000::/32**               | Teredo                                                                                                                                          |

#### 兼容性地址

| 地址                         | 描述                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:--|:--|
| **IPv4 兼容地址**            | 用于通过 IPv4 基础设施进行 IPv6 通信的双栈节点。当 IPv4 兼容地址用作 IPv6 目的地址时，IPv6 流量会自动封装 IPv4 报头，并通过 IPv4 基础设施发送到目的地。地址格式如下：`::w.x.y.z`，其中 w.x.y.z 是公共 IPv4 地址的点分十进制表示。                                                       |
| **IPv4 映射地址**            | 用于向 IPv6 节点表示仅支持 IPv4 的节点。仅用于内部表示。IPv4 映射地址从不作为 IPv6 数据包的源地址或目的地址使用。IPv6 协议不支持使用 IPv4 映射地址。地址格式如下：`::ffff:w.x.y.z`，其中 `w.x.y.z` 是公共 IPv4 地址的点分十进制表示。                                                    |

### 组播地址

组播最重要的方面是：

- 流量发送到单个地址，但由多个主机处理；
- 组成员身份是动态的，允许主机随时加入和离开组；
- 在 IPv6 中，使用组播监听发现（MLD）消息来确定网段（也称为链路或子网）上的组成员身份；
- 主机可以向组地址发送流量，而无需属于相应的组。

每个 IPv6 组播地址标识一个组播组。每个组保留的 IPv6 地址由组内所有监听并接收发送到该组地址的任何 IPv6 消息的主机成员共享。

组播地址由以下部分组成：

- 组播地址的前 8 位始终为 1111 1111（十六进制格式为 FF）。
- 标志位使用第 9 至 12 位，表示此组播地址是预定义的（众所周知的）还是非预定义的。如果是众所周知的，则所有位均为 0。
- 范围 ID 指示组播地址所属的范围，例如，范围 ID=2 表示链路本地范围。
- 组 ID 用于指定组播组。有预定义的组 ID，例如组 ID=1 - 所有节点。因此，如果组播地址为 ff02::1，则表示范围 ID=2 且组 ID=1，指示链路本地范围内的所有节点。这类似于 IPv4 中的广播。

以下是保留的 IPv6 组播地址表：

| 地址                     | 描述                                                                                                                                                                                                                                                |
|:--|:--|
| **FF02::1**              | 全节点地址用于到达同一链路上的所有节点。                                                                                                                                                                                                            |
| **FF02::2**              | 全路由器地址用于到达同一链路上的所有路由器。                                                                                                                                                                                                        |
| **FF02::5**              | 所有 OSPF 路由器地址用于到达同一链路上的所有 OSPF 路由器。                                                                                                                                                                                           |
| **FF02::6**              | 所有 OSPF 指定路由器地址用于到达同一链路上的所有 OSPF 指定路由器。                                                                                                                                                                                  |
| **FF02::1:FFXX:XXXX**    | 请求节点地址在地址解析过程中用于将链路本地节点的 IPv6 地址解析为其链路层地址。请求节点地址的最后 24 位（XX:XXXX）是 IPv6 单播地址的最后 24 位。                                                                                                       |

下表是保留用于 IPv6 组播并在互联网号码分配局（IANA）注册的 IPv6 组播地址的部分列表。有关已分配地址的完整列表，请阅读 [IANA 文档](https://www.iana.org/assignments/ipv6-multicast-addresses/ipv6-multicast-addresses.xhtml)。

组播地址可用于发现网络中的节点。例如，发现所有节点

```text
mrz@bumba:/media/aaa/ver$ ping6 ff02::1%eth0
PING ff02::1%eth0(ff02::1) 56 data bytes
64 bytes from fe80::21a:4dff:fe5d:8e56: icmp_seq=1 ttl=64 time=0.037 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=4.03 ms (DUP!)
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=5.59 ms (DUP!)
64 bytes from fe80::20c:42ff:fe49:fce5: icmp_seq=1 ttl=64 time=5.60 ms (DUP!)
64 bytes from fe80::20c:42ff:fe21:f1ec: icmp_seq=1 ttl=64 time=5.88 ms (DUP!)
64 bytes from fe80::20c:42ff:fe72:a1b0: icmp_seq=1 ttl=64 time=6.70 ms (DUP!)
```

发现所有路由器

```text
mrz@bumba:/media/aaa/ver$ ping6 ff02::2%eth0
PING ff02::2%eth0(ff02::2) 56 data bytes
64 bytes from fe80::20c:42ff:fe28:7945: icmp_seq=1 ttl=64 time=0.672 ms
64 bytes from fe80::20c:42ff:fe0d:2c38: icmp_seq=1 ttl=64 time=1.44 ms (DUP!)
```

### 任播地址

任播地址是 IPv6 中引入的一种新地址类型。

任播是一种支持面向服务地址的新网络范例，其中可以将相同的地址分配给提供特定服务的多个节点。任播数据包（即具有任播目的地址的数据包）将被传送到具有相同任播地址的其中一个节点。

任播地址没有分配特定的地址范围。它从单播地址范围中分配。

### 接口标识符

IPv6 地址的最后 64 位是接口标识符，该标识符对于 IPv6 地址的 64 位前缀是唯一的。有几种方法可以确定接口标识符：

- EUI-64；
- 随机生成以提供一定程度的匿名性；
- 手动配置。

### EUI-64

网络适配器的传统接口标识符是 48 位 MAC 地址。该地址由 24 位制造商 ID 和 24 位板卡 ID 组成。

IEEE EUI-64 是网络接口地址的新标准。公司 ID 仍为 24 位，但扩展 ID 为 40 位，为网络适配器创建了更大的地址空间。

要从接口 MAC 地址创建 EUI-64 地址：

- 将 0xFFFE 插入 MAC 地址的制造商 ID 和板卡 ID 之间。
- 第一个字节的第七位被反转。

让我们以 MAC 地址 00:0C:42:28:79:45 为例。

![](img/eui_328256.png)

上图说明了转换过程。当结果转换为冒号十六进制表示法时，我们得到接口标识符 `20C:42FF:FE28:7945`。因此，相应的链路本地地址为

```
FE80::20C:42FF:FE28:7945/64
```

在 RouterOS 中，如果配置了地址的 EUI-64 参数，则该地址的最后 64 位将使用接口标识符自动生成和更新。在这种情况下，最后几位必须配置为零。示例：

```ros
[admin@MikroTik] > ipv6 address add address=fc00:3::/64 interface=ether3 eui-64=yes
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::20c:42ff:fe1d:3d4/64                ether3                     yes
[admin@MikroTik] > interface ethernet set ether3 mac-address=10:00:00:00:00:01
[admin@MikroTik] > ipv6 address print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     INTERFACE                  ADVERTISE
...
5  G fc00:3::1200:ff:fe00:1/64                   ether3                     yes
```

### 配置 IPv6 地址

此示例展示如何在两台路由器之间使用全局 IPv6 地址设置简单的寻址。

R1 配置：

```ros
/ipv6 address
add address=2001:DB8::1/64 interface=ether1 advertise=no
```

R2 配置：

```ros
/ipv6 address
add address=2001:DB8::2/64 interface=ether1 advertise=no
```

检查地址列表：

```text
[admin@R1] /ipv6 address> print
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local
#    ADDRESS                                     FROM-POOL INTERFACE     ADVERTISE
0  G 2001:db8::1/64                                        ether1        no
3 DL fe80::219:d1ff:fe39:3535/64                           ether1        no
```

请注意，我们添加的地址具有 G 标志，表示该地址可以进行全局路由。我们还在接口上有一个链路本地地址，该地址是为每个支持 IPv6 的接口自动创建的。

测试连通性：

```text
[admin@R1] /ipv6 address> /ping 2001:DB8::2
HOST                                     SIZE TTL TIME  STATUS
2001:db8::2                 56  64 12ms  echo reply
2001:db8::2                 56  64 0ms   echo reply
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=6ms max-rtt=12ms
```

### SLAAC IPv6 地址

如果在 IPv6/设置 菜单中启用了“接受路由器通告”选项，并且路由器收到路由器通告数据包，则 SLAAC IPv6 地址将自动分配给接收通告的接口。此地址将具有 DG 标志，表示该地址是动态且全局的。此类地址将显示有效和首选生命周期参数。

```text
[admin@R1] /ipv6/address/print detail where dynamic && global 
Flags: X - disabled, I - invalid, D - dynamic; G - global, L - link-local 
 0 DG address=2001:db8::ba69:f4ff:fe84:545/64 from-pool="" interface=ether1 
      actual-interface=test_fp eui-64=no advertise=no no-dad=no valid=4w2d 
      preferred=1w 
```

如果接受 SLAAC 地址，则还会生成指向互联网的动态路由。如果通告数据包中指定了限制，它还将包含一些限制。例如，跳数限制和 MTU。如果在同一接口上接收到多个地址，则将使用每个接口的最低 MTU 值。

```text
[admin@R1] /routing/route/print detail where slaac 
Flags: X - disabled, F - filtered, U - unreachable, A - active; 
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, a - ldp-address, l - ldp-mapping, g - slaac, y - bgp-mpls-vpn; 
H - hw-offloaded; + - ecmp, B - blackhole 
 Ag + afi=ip6 contribution=active dst-address=::/0 routing-table=main 
       pref-src="" gateway=fe80::ba69:f4ff:fe84:7b2%ether1
       immediate-gw=fe80::ba69:f4ff:fe84:7b2%ether1 distance=1 scope=30 
       target-scope=10 belongs-to="slaac" mtu=1400 hoplimit=10 
       debug.fwp-ptr=0x201C2C00 
```