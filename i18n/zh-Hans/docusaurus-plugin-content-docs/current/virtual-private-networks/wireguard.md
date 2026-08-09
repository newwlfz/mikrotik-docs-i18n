# WireGuard

> WireGuard 是一种现代 VPN 解决方案，提供跨平台的快速、安全加密，并支持详细的配置选项，包括私钥/公钥、VRF 路由以及对等体管理，用于在设备之间建立加密隧道。

# WireGuard

WireGuard 是一种极其简单但快速且现代的 VPN，它利用了最先进的密码学技术。它的目标是比 IPsec 更快、更简单、更精简、更有用，同时避免令人头疼的复杂问题。它旨在比 OpenVPN 具有更高的性能。WireGuard 被设计为一种通用 VPN，既适用于嵌入式接口，也适用于超级计算机，能够适应多种不同的场景。它最初为 Linux 内核发布，现在已跨平台（Windows、macOS、BSD、iOS、Android）并广泛部署。

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*; 默认值: ) | 隧道的简短描述。 |
| **disabled** (*yes \| no*; 默认值: **no**) | 启用/禁用隧道。 |
| **listen-port** (*整数; 默认值: 13231*) | WireGuard 服务监听传入会话的端口。 |
| **mtu** (*整数 [0..65536]*; 默认值: **1420**) | 三层最大传输单元。 |
| **name** (*字符串*; 默认值: ) | 隧道的名称。 |
| **vrf** (*字符串*; 默认值: **main**) | 为 WireGuard socket 指定 VRF，详见下文。 |
| **private-key** (*字符串*; 默认值: ) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 一个 base64 私钥。如果未指定，将在接口创建时自动生成。每个网络接口都有一个私钥和一个对等体列表。 |

### WireGuard 上下文中的 `vrf` 参数

:::info
`vrf` 参数**不**适用于 WireGuard 接口本身（例如 `wg0`、`wg1`），而是适用于用于传输加密数据包的 **UDP socket**。

WireGuard 运行涉及两个不同的层级：

1. **WireGuard 接口** — 这是虚拟网络设备，*明文*（未加密）数据包通过它流动。这些数据包被加密后通过 UDP socket 发送出去，或者从 UDP socket 接收后解密。
2. **UDP sockets** — 这些处理*加密*流量：从网络接收加密数据包并发送加密数据包。

`vrf` 参数与 **UDP socket 层**（第 2 种情况）相关。它指定 socket 应使用**哪个路由表（VRF）** 来确定加密数据包的发送或接收方式。
这确保了加密流量遵循正确的路由路径并使用正确的源 IP，防止数据包可能通过错误的接口或路由发送的问题。

#### 示例

> 假设接口 `eth1` 属于 VRF `foo`。
> 如果您希望 WireGuard 通过 `eth1` 发送和接收加密数据包，则应配置 WireGuard 使用 `vrf=foo`。
> WireGuard 接口（`wg0`）本身与内部 UDP socket 使用的 `vrf` 参数位于不同的 VRF 中是完全正常的。
:::

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **public-key** (*字符串*) | 从私钥计算得出的 base64 公钥。每个对等体都有一个公钥。对等体使用公钥相互认证。它们可以传递用于配置文件。 |
| **running** (*yes \| no*) | 接口是否正在运行。 |

## 对等体

| 属性 | 描述 |
| :-- | :-- |
| **allowed-address** (*IP/IPv6 前缀*; *默认值*: ) | 带有 CIDR 掩码的 IP（v4 或 v6）地址列表，允许来自该对等体的传入流量，并将发往该对等体的传出流量定向到这些地址。allowed-address 前缀定义了对等体的路由和过滤规则，不需要与 WireGuard 接口地址位于同一子网。如果 WireGuard 接口位于 192.168.99.1/24，则必须在客户端输入 192.168.99.2。通过将此 IP 添加到“Allowed Address”下，您表示只有这个特定客户端（例如手机）被允许连接到该对等体配置。同一接口上的 allowed-address 范围不能重叠，因此您需要为每个对等体设置自己的范围。 |
| **comment** (*字符串; 默认值: )* | 对等体的简短描述。 |
| **disabled** (*yes \| no; 默认值: **no**)* | 启用/禁用对等体。 |
| **endpoint-address** (*IP/主机名; 默认值: )* | IP 地址或主机名。WireGuard 使用它来在两个对等体之间建立安全连接。 |
| **endpoint-port** (*整数:0..65535**; 默认值:* ) | Endpoint 端口是 WireGuard 对等体监听传入流量的 UDP 端口。 |
| **interface** (*字符串; 默认值:* ) | 对等体所属的 WireGuard 接口名称。 |
| **persistent-keepalive** (*整数:0..65535; 默认值: 0*) | 以秒为单位的间隔（0 到 65535 之间），表示向对等体发送经过认证的空数据包的频率，以保持有状态防火墙或 NAT 映射持续有效。值为 0 表示禁用 keepalive。例如，如果接口很少发送流量，但可能随时从对等体接收流量，并且它位于 NAT 后面，则该接口可能受益于 25 秒的持久 keepalive 间隔。 |
| **preshared-key** (*字符串; 默认值:* ) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 一个 base64 预共享密钥。可选，可以省略。此选项在现有的公钥密码学基础上增加了额外的对称密钥密码学层，以提供后量子抗性。它也可以自动生成或由系统管理员手动输入。 |
| **private-key** *(auto/none; 默认值: **none**) [敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 一个 base64 私钥。 |
| **public-key** (*字符串; 默认值:* ) | 从私钥计算得出的 base64 公钥。每个对等体都有一个公钥。对等体使用公钥相互认证。它们可以传递用于配置文件。 |
| **show-client-config**\**[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | *将显示已创建的对等体配置，并生成 QR 码，以便在客户端设备上更轻松地进行对等体设置。不影响 WireGuard 服务器。要查看 QR 码，从 7.21\_ab548 起需要 show-sensitive。* |
| 用于客户端-服务器设置场景，当使用 QR 码为客户端导入配置时，一旦在字段中设置，带有 QR 码的选项卡上的配置详细信息将显示： |  |
| **client-address** (*IP/IPv6 前缀; 默认值: )* | 当使用 QR 码为客户端（例如手机）导入时，该设备上会设置此 wg 接口地址。 |
| **client-dns** (*IP/IPv6 前缀; 默认值: )* | 指定将 WireGuard 服务器用作对等体流量的 VPN 网关时使用。 |
| **client-endpoint** (*IP/IPv6 前缀; 默认值: )* | WireGuard 服务器的 IP 地址和端口号。 |
| **client-keepalive** (*整数:0..65535; 默认值: 0*) | 与 **persistent-keepalive** 相同，但从对等体侧设置。 |
| **client-listen-port** (*整数:0..65535**; 默认值:* ) | 此 WireGuard 隧道监听来自对等体的传入流量的本地端口，以及发送传出数据包时使用的源端口。 |
| **client-allowed-address** (*IP/IPv6 前缀; 默认值: ::/0*) | 从 7.21 开始，可以配置 Allowed IPs。 |
| **name** (*字符串; 默认值:*) | 允许为对等体添加名称。该名称将用作 WireGuard 日志中对等体的引用。（从 RouterOS 版本 7.15 开始可用） |
| **responder** (*yes \| no; 默认值: **no**)* | 指定对等体是作为连接发起者还是仅作为响应者。应将其用于作为其他设备（客户端）连接目标的“服务器”的 WireGuard 设备。否则，路由器将反复尝试连接到“endpoint-address”或“current-endpoint-address”。 |

通过 WireGuard 对等体导出（配置文件或 QR 码）提供给客户端的“**AllowedIPs**”配置无法更改，目前将设置为“0.0.0.0/0, ::/0”。如果需要在远端修改这些值，必须通过用于 WireGuard 连接的远端对等体软件来完成。从版本 7.21 开始已添加支持。

## 导入、导出 WireGuard

可以通过多种方式进行配置，这里是一个简单的 wg 导入文件示例：[export](pathname:///assets/319783040_export)

:::warning
在客户端设备上通过 QR 码/文件导入时，必须指定最小参数。注意 - 如果客户端地址字段留空，则在生成 QR 码时会添加默认 IP 地址 [192.168.177.2/24](http://192.168.177.2/24 "Follow link")。

示例：

```
interface: wireguard1
public-key: v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M=
private-key: KMwxqe/iXAU8Jn9dd1o5pPdHep2blGxNWm9I944/I24=
allowed-address: 192.168.88.3/24
client-address: 192.168.88.3/32
client-endpoint: example.com:13231
```

**警告：** 使用 `/interface/wireguard/wg-import` file= 时，如果 Wireguard 导入文件以 # 开头，您可能会收到 Could not parse 错误，请按照示例使用干净的文件：

```
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=
```

**警告：** 从 7.19\_ab41 开始，添加了 config-string 参数，例如，使用此 CLI 命令可以导入您的配置：

```
/interface/wireguard/wg-import config-string="  
[Interface]  
Address =192.168.88.3/24  
ListenPort = 13533  
PrivateKey = UBLqJEFZZf9wszZSUF2BPWa9dsMX99RbEcxlNfxWffk=  
[Peer]  
PublicKey = EoF7HlFu3fbOnuYbyGqLMJkPZgQk9n3WwONZuJZ6qWc=  
Endpoint = 199.168.100.10:51820  
AllowedIPs = 0.0.0.0/0  
PersistentKeepalive = 25"
```

:::

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **current-endpoint-address** (*IP/IPv6*) | 来自对等体的最近一次正确认证数据包的源 IP 地址。 |
| **current-endpoint-port** (*整数*) | 来自对等体的最近一次正确认证数据包的源 IP 端口。 |
| **last-handshake** (*整数*) | 距离上次成功握手的时间（秒）。 |
| **rx** (*整数*) | 从对等体接收的总字节数。 |
| **tx** (*整数*) | 向对等体发送的总字节数。 |

:::note
当您遇到回复流量具有错误源地址的问题时，使用 NAT 将数据包源地址转换到您的环回接口是一种常见的解决方法。这种方法有助于确保当数据包通过路由返回网络时，源地址保持一致和正确。
:::

### 应用示例

### 站点到站点 WireGuard 隧道

考虑如下所示的设置。两个远程办公室路由器连接到互联网，办公室工作站位于 NAT 后面。每个办公室都有自己的本地子网，Office1 为 10.1.202.0/24，Office2 为 10.1.101.0/24。两个远程办公室都需要到路由器后面本地网络的安全隧道。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-01.webp)

#### WireGuard 接口配置

首先，必须在两个站点上配置 WireGuard 接口，以允许自动生成私钥和公钥。两个路由器的命令相同：

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
```

现在打印接口详细信息时，私钥和公钥都应可见，以便进行交换。

:::warning
任何私钥在远端设备上都不需要 - 因此称为私钥。
:::

**Office1**

```ros
/interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="yKt9NJ4e5qlaSgh48WnPCDCEkDmq+VsBTt/DDEBWfEo=" 
      public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI=" 
```

**Office2**

```ros
/interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="KMwxqe/iXAU8Jn9dd1o5pPdHep2blGxNWm9I944/I24=" 
      public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M=" 
```

#### 对等体配置

对等体配置定义了谁可以使用 WireGuard 接口以及可以通过它发送什么类型的流量。为了识别远程对等体，必须指定其公钥以及创建的 WireGuard 接口。

**Office1**

```ros
/interface/wireguard/peers
add allowed-address=10.1.101.0/24,10.255.255.2/32 endpoint-address=192.168.80.1 endpoint-port=13231 interface=wireguard1 \
public-key="v/oIzPyFm1FPHrqhytZgsKjU7mUToQHLrW+Tb5e601M="
```

**Office2**

```ros
/interface/wireguard/peers
add allowed-address=10.1.202.0/24,10.255.255.1/32 endpoint-address=192.168.90.1 endpoint-port=13231 interface=wireguard1 \
public-key="u7gYAg5tkioJDcm3hyS7pm79eADKPs/ZUGON6/fF3iI="
```

#### IP 和路由配置

最后，必须配置 IP 和路由信息，以允许流量通过隧道发送。

**Office1**

```ros
/ip/address
add address=10.255.255.1/30 interface=wireguard1
/ip/route
add dst-address=10.1.101.0/24 gateway=wireguard1
```

**Office2**

```ros
/ip/address
add address=10.255.255.2/30 interface=wireguard1
/ip/route
add dst-address=10.1.202.0/24 gateway=wireguard1
```

#### 防火墙注意事项

默认的 RouterOS 防火墙会阻止隧道正常建立。在两个站点上，应在任何丢弃规则之前接受“input”链中的流量。

**Office1**

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.80.1
```

**Office2**

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=13231 protocol=udp src-address=192.168.90.1
```

此外，“forward”链也可能限制子网之间的通信，因此此类流量也应在任何丢弃规则之前被接受。

**Office1**

```ros
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
```

**Office2**

```ros
/ip/firewall/filter
add action=accept chain=forward dst-address=10.1.101.0/24 src-address=10.1.202.0/24
add action=accept chain=forward dst-address=10.1.202.0/24 src-address=10.1.101.0/24
```

## RoadWarrior WireGuard 隧道

### RouterOS 配置

添加一个新的 WireGuard 接口并为其分配 IP 地址。

```ros
/interface/wireguard
add listen-port=13231 name=wireguard1
/ip/address
add address=192.168.100.1/24 interface=wireguard1
```

添加新的 WireGuard 接口将自动生成一对私钥和公钥。您需要在远程设备上配置公钥。要获取公钥值，只需打印接口详细信息。

```ros
[admin@home] > /interface/wireguard/print 
Flags: X - disabled; R - running 
 0  R name="wireguard1" mtu=1420 listen-port=13231 private-key="cBPD6JNvbEQr73gJ7NmwepSrSPK3np381AWGvBk/QkU=" 
      public-key="VmGMh+cwPdb8//NOhuf1i1VIThypkMQrKAO9Y55ghG8=" 
```

接下来的步骤中，您需要确定远程设备的公钥。获得公钥后，通过指定远程设备的公钥和允许通过 WireGuard 隧道传输的允许地址来添加新的对等体。

```ros
/interface/wireguard/peers
add allowed-address=192.168.100.2/32 interface=wireguard1 public-key="<paste public key from remote device here>"
```

## 防火墙注意事项

如果您配置了默认或严格的防火墙，您需要允许远程设备建立到您设备的 WireGuard 连接。

```ros
/ip/firewall/filter
add action=accept chain=input comment="allow WireGuard" dst-port=13231 protocol=udp place-before=1
```

要允许远程设备连接到 RouterOS 服务（例如请求 DNS），请在 input 链中允许 WireGuard 子网。

```ros
/ip/firewall/filter
add action=accept chain=input comment="allow WireGuard traffic" src-address=192.168.100.0/24 place-before=1
```

或者简单地将 WireGuard 接口添加到“LAN”接口列表中。

```ros
/interface/list/member
add interface=wireguard1 list=LAN
```

### iOS 配置

从 App Store 下载 WireGuard 应用程序。打开它并从零开始创建新配置。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-02.webp)

首先为您的连接指定一个“Name”，并选择生成密钥对。生成的公钥对于 RouterOS 端的对等体配置是必需的。

**![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-03.webp)**

在“Addresses”字段中指定一个与服务器端配置在同一子网的 IP 地址。此地址将用于通信。在此示例中，我们在 RouterOS 端使用了 192.168.100.1/24。您可以在此处使用 192.168.100.2。

如有必要，配置 DNS 服务器。如果在 RouterOS 端的 IP/DNS 部分将 allow-remote-requests 设置为 yes，您可以在此处指定远程 WireGuard IP 地址。

**![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-04.webp)**

点击“Add peer”以显示更多参数。

“Public key”值是 RouterOS 端 WireGuard 接口上生成的公钥值。

“Endpoint”是 iOS 设备可以通过互联网与之通信的 RouterOS 设备的 IP 或 DNS 及端口号。

“Allowed IPs”设置为 0.0.0.0/0，以允许所有流量通过 WireGuard 隧道发送。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-05.webp)

```ros
根据您的配置，您可能需要添加 NAT 规则
chain=dstnat action=dst-nat to-ports=port protocol=udp in-interface=interface dst-port=port
```

### Windows 10 配置

从 WireGuard 下载 WireGuard 安装程序  
以管理员身份运行。

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/wireguard-06.webp)

按 <kbd>Control</kbd>+<kbd>N</kbd> 添加一个新的空隧道，为接口添加名称，公钥应自动生成。将其复制到 RouterOS 对等体配置中。  
将其添加到服务器配置中，使完整配置如下所示（在 [Interface] 部分保留您自动生成的 PrivateKey：

```actionscript3
[Interface]
PrivateKey = your_autogenerated_private_key=
Address = 192.168.100.2/24
DNS = 192.168.100.1

[Peer]
PublicKey = your_MikroTik_public_KEY=
AllowedIPs = 0.0.0.0/0
Endpoint = example.com:13231
```

保存并激活

## 多 WAN 设置

对于 WireGuard，不存在服务器-客户端关系，两端都可以作为端点，并且如果两端在配置中定义了端点，则双方都会向对方发送 UDP 握手消息（这并非总是如此，因为您可以在对等体设置中启用“responder”选项，这将允许您模拟服务器-客户端行为，因为“服务器”对等体只会回复来自“客户端”对等体的握手消息，而不会自行发送握手消息）。  
由于上述隧道建立的性质，来自 WireGuard 隧道不同端点的握手消息被视为两个独立的连接。  
在到“客户端”对等体存在多条路径的设置中，我们需要考虑到这一点，因为这可能导致“服务器”不通过传入路由而是通过其他路由回复“客户端”，具体取决于设置。  
下面您可以看到一个配置示例，说明如何解决此行为并确保“服务器”使用传入路由回复“客户端”。

### 配置示例

此示例不包括 WireGuard 接口配置，因为它适用于具有两条 WAN 连接的 [RoadWarrior](./wireguard.md#roadwarrior-wireguard-tunnel) 和 [Site to Site](./wireguard.md#site-to-site-wireguard-tunnel) 设置，例如 [PCC](../high-availability-solutions/load-balancing/per-connection-classifier.md) 设置。  
为了使这些规则按预期工作，您需要在 WireGuard 对等体设置中启用“responder”选项，因为“服务器”可能通过错误的接口发送握手消息，因为路由未被标记。

```ros
/ip/firewall/mangle 
add action=add-src-to-address-list chain=prerouting address-list=WAN2_WireGuard_clients address-list-timeout=1m dst-port=13231 in-interface=ether2 protocol=udp comment="add source IP address of WAN2 incoming WireGuard traffic to address list"
add action=mark-connection chain=output dst-address-list=WAN2_WireGuard_clients dst-port=13231 new-connection-mark=wan2 protocol=udp comment="mark WireGuard connection to the client peer by checking destination address from the address list" 
add action=mark-routing chain=output connection-mark=wan2 dst-port=13231 new-routing-mark=wan2 protocol=udp comment="ensure that WireGuard traffic uses routing table associated with the WAN2 incoming interface"
add action=add-src-to-address-list chain=prerouting address-list=WAN3_WireGuard_clients address-list-timeout=1m dst-port=13231 in-interface=ether3 protocol=udp comment="add source IP address of WAN3 incoming WireGuard traffic to address list"
add action=mark-connection chain=output dst-address-list=WAN3_WireGuard_clients dst-port=13231 new-connection-mark=wan3 protocol=udp comment="mark WireGuard connection to the client peer by checking destination address from the address list" 
add action=mark-routing chain=output connection-mark=wan3 dst-port=13231 new-routing-mark=wan3 protocol=udp comment="ensure that WireGuard traffic uses routing table associated with the WAN3 incoming interface"
 
/ip/firewall/nat 
add action=masquerade chain=srcnat log=yes out-interface=ether2 comment="ensure that packet has source IP of WAN2 interface"
add action=masquerade chain=srcnat log=yes out-interface=ether3 comment="ensure that packet has source IP of WAN3 interface"
```

第一条 mangle 规则用于通过匹配传入 WireGuard 握手的目标端口来捕获源 IP 地址，并将其添加到列表中，该列表将进一步用于标记传出的 WireGuard 握手。使用超时是为了确保将来相同的源 IP 地址可以使用不同的 WAN 接口建立 WireGuard 隧道。  
第二条 mangle 规则标记连接，这些连接进一步用于标记路由，并确保在 IP 地址从地址列表中消失且隧道建立后，标记仍保留在连接上。  
第三条 mangle 规则用于强制数据包为第二个 WAN 接口使用正确的路由表。  
最后一条 NAT 规则是必需的，以确保数据包以正确的源 IP 发送出去，因为它不受 mangle 规则的调整，如果未实现，数据包可能根据设置具有不同的源 IP。
如您所见，规则为 WAN3 复制了一份，以确保 WAN3 接口也可用于 WireGuard。  
  
此规则集确保 WireGuard 隧道在接收到传入握手的接口上建立。

## 2FA 设置

在 RouterOSv7 中，[HotSpot](../authentication-authorization-accounting/hotspot-captive-portal/index.md) 服务可以绑定到 WireGuard 接口。这允许管理员将 WireGuard 的高性能加密与 HotSpot 的强制门户功能相结合，通过本地数据库、User Manager 或 RADIUS 支持额外的用户级认证，而 OTP 功能可以进一步增强安全性。

### 配置示例

确保您的设备上已配置 Wireguard 接口：

```routeros
/interface/wireguard> print 
Flags: X - DISABLED; R - RUNNING 
 0  R name="wg1" mtu=1420 listen-port=49422 
      public-key="MikroTikMikroTikMikroTik=" 
```

在 Wireguard 接口上设置 HotSpot：

```routeros
/ip/hotspot> setup 
Select interface to run HotSpot on 
hotspot interface: wg1

or
/ip/hotspot/add interface=wg1

*从 7.22 开始支持
```

HotSpot 设置完成后，一旦 Wireguard 对等体连接，将需要额外登录门户才能继续。可以使用常规的 HotSpot 用户名/密码授权。为了更好的安全性，可以利用 `/ip/hotspot/user` otp-password 或 `/user-manager/user` totp-password 字段。添加带有 totp-secret 的用户：

```routeros
/ip/hotspot/user/add name=peer1 totp-secret=HVR4CFHAFOWFGGFAGSA5JVTIMMPG6GMT
```

您可以找到多个开源 totp 生成器工具，它们可以为您提供适当的密钥和必要的选项，以将其导入到您的“authenticator”应用程序中。

设置完成后，在您的设备上启动 Wireguard，在通过 Wireguard/HotSpot 服务器成功授权后，将提示 HotSpot 登录页面，您需要输入 HotSpot 用户名和来自“authenticator”应用程序的 totp 6 位密码（每 30 秒更改一次）。

强烈建议为 HotSpot 使用 HTTPS 登录页面，并确保 Wireguard 对等体具有验证登录页面证书的选项。