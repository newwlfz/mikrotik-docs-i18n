# PPP AAA

> MikroTik RouterOS PPP AAA 功能提供本地及 RADIUS 支持的身份验证、授权和记账功能。PPP 配置文件为用户访问记录定义默认设置，包括桥接配置、速率限制以及加密和压缩等安全选项。

# PPP AAA

## 概述

**子菜单：** `/ppp`

MikroTik RouterOS 提供可扩展的身份验证、授权和记账（AAA）功能。

本地身份验证使用用户数据库和配置文件数据库执行。给定用户的实际配置由用户数据库中的相应用户记录、配置文件数据库中的关联条目以及配置文件数据库中设置为该用户所认证服务的默认条目共同组成。配置文件数据库中的默认配置文件设置优先级最低，而用户数据库中的用户访问记录设置优先级最高，唯一例外是特定 IP 地址在 local-address 和 remote-address 设置中优先于 IP 地址池，这将在后文描述。

对 RADIUS 身份验证的支持使 ISP 或网络管理员能够通过一个服务器在整个大型网络中管理 PPP 用户访问和记账。MikroTik RouterOS 具有一个 [RADIUS 客户端](./radius.md)，可为 PPP、[PPPoE](../virtual-private-networks/pppoe/index.md)、[PPTP](../virtual-private-networks/pptp.md)、[L2TP](../virtual-private-networks/l2tp/index.md)、[OpenVPN](../virtual-private-networks/openvpn.md) 和 ISDN 连接进行身份验证。从 RADIUS 服务器接收的属性会覆盖默认配置文件中设置的属性，但如果某些参数未接收到，则从相应的默认配置文件中获取。

## 用户配置文件

**子菜单：** `/ppp/profile`

PPP 配置文件用于为 `/ppp/secret` 子菜单下存储的用户访问记录定义默认值。`/ppp/secret` 用户数据库中的设置会覆盖相应的 `/ppp/profile` 设置，但指定为 local-address 或 remote-address 参数时，单个 IP 地址始终优先于 IP 地址池。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **address-list** (*字符串*；默认：) | PPP 分配（服务器端）或接收（客户端）的地址将被添加到的 [地址列表](../firewall-and-quality-of-service/firewall/address-lists.md) 名称。 |
| **remote-ipv6-prefix-reuse** (*no \| yes*；默认：**no**) | 如果指定了 "remote-ipv6-prefix-pool" 且仅包含一个 "/64" 前缀，则该前缀只能用于单个 PPP 客户端的 RADVD 配置。当此选项设置为 "yes" 时，该前缀可在此 PPP 配置文件的所有客户端之间重复使用。 |
| **bridge** (*字符串*；默认：) | PPP 接口将作为从属端口添加到的 [桥接](../bridging-and-switching/index.md) 接口名称。要使此功能生效，隧道两端（服务器和客户端）都必须位于桥接中，更多详情请参阅桥接手册。 |
| **bridge-horizon** (*整数 0..429496729*；默认：) | 用于动态创建的桥接端口的 split-horizon 值。可用于防止桥接环路和隔离流量。为一组端口设置相同的值，以防止它们向具有相同 horizon 值的端口发送数据。 |
| **bridge-learning** (*default \| no \| yes*；默认：**default**) | 更改动态创建的桥接端口上的 MAC 学习行为：yes - 启用 MAC 学习no - 禁用 MAC 学习default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 yes |
| **bridge-path-cost** (*整数 1..200000000*；默认：) | 用于动态创建的桥接端口的路径开销，由 STP/RSTP 用于确定最佳路径，由 MSTP 用于确定区域间的最佳路径。当桥接协议模式设置为 none 时，此属性无效。 |
| **bridge-port-priority** (*整数 0..240*；默认：) | 用于动态创建的桥接端口的优先级，由 STP/RSTP 用于确定根端口，由 MSTP 用于确定区域间的根端口。当桥接协议模式设置为 none 时，此属性无效。 |
| **bridge-port-vid** (*整数 1..4094*；默认：**1**) | 用于为动态创建的接口分配 PVID 参数。此属性仅在桥接 vlan-filtering 设置为 yes 时生效。 |
| **bridge-port-trusted**(*no \| yes*；默认：**no**) | 用于将动态创建的接口设置为 DHCP 受信任。 |
| **change-tcp-mss** (*yes \| no \| default*；默认：**no**) | 修改连接 MSS 设置（仅适用于 IPv4）：yes - 调整连接 MSS 值no - 不调整连接 MSS 值default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 no |
| **comment** (*字符串*；默认：) | 配置文件注释 |
| **dhcpv6-lease-time** (*字符串*；默认：) | 租约时间可从 7.20ab202 版本开始设置，默认时间为 1d。 |
| **dhcpv6-pd-pool** (*字符串*；默认：) | 客户端连接时，动态创建的 [DHCPv6 服务器](../network-management/dhcp.md#dhcpv6-server) 将使用的 [IPv6 地址池](../cli-reference/ipv6/pool.md) 名称。 [`了解更多 >>`](../virtual-private-networks/pppoe/ipv6-pd-over-ppp.md) |
| **dhcpv6-use-radius** (*no \| yes*；默认：**no**) | 为动态生成的 DHCPv6 PD 服务器指定 "use-radius" 选项的值。 |
| **dns-server** (*IP*；默认：) | 提供给 PPP 客户端的 DNS 服务器 IP 地址 |
| **idle-timeout** (*时间*；默认：) | 指定在无活动后链路将被终止的时间。默认不设置超时。 |
| **incoming-filter** (*字符串*；默认：) | 用于入站数据包的防火墙链名称。指定的链控制来自客户端的每个数据包。应手动添加 ppp 链，并在其他相关链中添加 action=jump jump-target=ppp 的规则，此功能才能生效。更多信息请参阅示例部分。 |
| **insert-queue-before** (*bottom \| first \| 队列名称*；默认：) | 将新队列插入为最后、第一个或指定队列之前 |
| **interface-list** (*接口列表名称*；默认：) | 指定配置文件接口将被添加到的接口列表 |
| **local-address** (*IP 地址 \| 地址池*；默认：) | 隧道地址或本地 ppp 接口分配地址的 [地址池](../cli-reference/ip/pool.md) 名称 |
| **name** (*字符串*；默认：) | PPP 配置文件名称 |
| **on-up** (*脚本*；默认：) | 在用户登录事件时执行脚本。事件脚本可访问的变量如下：userlocal-addressremote-addresscaller-idcalled-idinterface *interface* 变量将返回接口 ID 值，而非接口名称。 |
| **on-down** (*脚本*；默认：) | 在用户注销时执行脚本。更多详情请参阅 ***on-up*** |
| **only-one** (*yes \| no \| default*；默认：**default**) | 定义用户是否允许同时拥有多个 PPP 会话yes - 用户不允许同时拥有多个 PPP 会话no - 用户允许同时拥有多个 PPP 会话default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 no |
| **outgoing-filter** (*字符串*；默认：) | 用于出站数据包的防火墙链名称。指定的链控制发往客户端的每个数据包。应手动添加 PPP 链，并在其他相关链中添加 action=jump jump-target=ppp 的规则，此功能才能生效。更多信息请参阅示例部分。 |
| **parent-queue** (*none* \| *队列名称*；默认：) | 指定父队列 |
| **queue-type** (*default \| ethernet-default \| wireless-default \| synchronous-default \|* *hotspot-default \| pcq-upload-default \| pcq-download-default \| only-hardware-queue \| multi-queue-ethernet-default \| default-small \| 自定义队列类型名称*；默认：) | 指定队列类型。从 7.19 版本开始，可以为客户端的 "upload" 和 "download" 分别指定 rx/tx 的队列类型。使用 / 配置单独的队列类型，第一个是 rx 队列类型，然后是 tx 队列类型。 |
| **rate-limit** (*字符串*；默认：) | 速率限制格式为 **rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time] [priority] [rx-rate-min[/tx-rate-min]]]]**，从路由器的角度（因此 "rx" 是客户端上传，"tx" 是客户端下载）。所有速率均以比特每秒为单位，除非后跟可选的 'k' 后缀（千比特每秒）或 'M' 后缀（兆比特每秒）。如果未指定 tx-rate，则 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果未指定 rx-burst-threshold 和 tx-burst-threshold（但指定了 burst-rate），则使用 rx-rate 和 tx-rate 作为突发阈值。如果未指定 rx-burst-time 和 tx-burst-time，则默认使用 1s。优先级取值 1..8，其中 1 表示最高优先级，8 表示最低。如果未指定 rx-rate-min 和 tx-rate-min，则使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 的值不能超过 rx-rate 和 tx-rate 的值。 |
| **remote-address** (*IP*；默认：) | 隧道地址或远程 ppp 接口分配地址的 [地址池](../cli-reference/ip/pool.md) 名称。 |
| **remote-ipv6-prefix-pool** (*字符串 \| none*；默认：**none**) | 从 IPv6 地址池分配前缀给客户端，并安装相应的 IPv6 路由。 |
| **session-timeout** (*时间*；默认：) | 连接可以保持的最大时间。默认不设置时间限制。 |
| **use-compression** (*yes \| no \| default*；默认：**default**) | 指定是否使用数据压缩。yes - 启用数据压缩no - 禁用数据压缩default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 no此设置不影响 OVPN 隧道。 |
| **use-encryption** (*yes \| no \| default \| require*；默认：**default**) | 指定是否使用数据加密。yes - 启用数据加密no - 禁用数据加密default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 norequire - 明确要求加密此设置不适用于 OVPN 和 SSTP 隧道。 |
| **use-ipv6** (*yes \| no \| default \| require*；默认：**default**) | 指定是否允许 IPv6。默认情况下，如果安装了 IPv6 软件包，则启用。yes - 启用 IPv6 支持no - 禁用 IPv6 支持default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 norequire - 明确要求 IPv6 支持 |
| **use-mpls** (*yes \| no \| default \| require*；默认：**default**) | 指定是否允许在 PPP 上使用 MPLS。yes - 启用 MPLS 支持no - 禁用 MPLS 支持default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 norequire - 明确要求 MPLS 支持 |
| **use-upnp** (*yes \| no \| default*；默认：**default**) | 指定是否允许 UPnP：yes - 启用 UPnP。no - 禁用 UPnP。default - 从接口默认配置文件派生此值；如果这是接口默认配置文件，则等同于 no。 |
| **wins-server** (*IP 地址*；默认：) | 提供给 Windows 客户端的 WINS 服务器 IP 地址 |

### 备注

两个默认配置文件无法删除：

```ros
[admin@rb13] /ppp/profile> print
Flags: * - default
 0 * name="default" use-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1 * name="default-encryption" use-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] /ppp/profile>
```

*incoming-filter* 和 *outgoing-filter* 参数会向链 *ppp* 添加动态跳转规则，其中 jump-target 参数将等于配置文件中的 *incoming-filter* 或 *outgoing-filter* 参数。因此，在更改这些参数之前，应手动添加链 *ppp*。

如果使用 RADIUS 身份验证，则忽略 only-one 参数。

PPP 隧道使用 LCP 协议进行 MTU 协商，这在连接建立时立即发生。不支持 Framed MTU 属性，因为它仅在通过 Radius 身份验证后发送。

## 用户数据库

**子菜单：** `/ppp/secret`

PPP 用户数据库存储 PPP 用户访问记录，并为每个用户分配 PPP 用户配置文件。

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **caller-id** (*字符串*；默认：) | 对于 [PPTP](../virtual-private-networks/pptp.md) 和 [L2TP](../virtual-private-networks/l2tp/index.md)，是客户端必须从其连接的 IP 地址。对于 [PPPoE](../virtual-private-networks/pppoe/index.md)，是客户端必须从其连接的 MAC 地址（以大写字母书写）。对于 ISDN，是客户端可以拨入的主叫号码（运营商可能提供也可能不提供） |
| **comment** (*字符串*；默认：) | 用户的简短描述。 |
| **disabled** (*yes \| no*；默认：**no**) | 是否使用该 secret。 |
| **limit-bytes-in** (*整数*；默认：**0**) | 客户端在会话中可以上传的最大字节数。 |
| **limit-bytes-out** (*整数*；默认：**0**) | 客户端在会话中可以下载的最大字节数。 |
| **local-address** (*IP 地址*；默认：) | 将在 ppp 接口本地设置的 IP 地址。 |
| **name** (*字符串*；默认：) | 用于身份验证的名称 |
| **password** (*字符串*；默认：) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于身份验证的密码 |
| **profile** (*字符串*；默认：**default**) | 使用哪个 [用户配置文件](#user-profiles) |
| **remote-address** (*IP*；默认：) | 将分配给远程 ppp 接口的 IP 地址。 |
| **remote-ipv6-prefix** (*IPv6 前缀*；默认：) | 分配给 ppp 客户端的 IPv6 前缀。该前缀被添加到 [ND 前缀列表](../system-information-and-utilities/neighbor-discovery.md)，从而在 ppp 接口上启用 [无状态](../getting-started/networking-fundamentals/ipv6-neighbor-discovery.md#stateless-address-autoconfiguration) 地址自动配置。 |
| **routes** (*字符串*；默认：) | 客户端连接时出现在服务器上的路由。路由格式为：dst-address gateway metric（例如，10.1.0.0/ 24 10.0.0.1 1）。不接受其他语法，因为它可能被错误地表示。可以指定多条路由，用逗号分隔。此参数对 [OpenVPN](../virtual-private-networks/openvpn.md) 将被忽略。 |
| **service** (*any \| async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*；默认：**any**) | 指定特定用户可以使用的服务。 |

## 活动用户

**子菜单：** `/ppp/active`

此子菜单允许监控活动（已连接）用户。

`/ppp/active/print` 命令将显示所有当前连接的用户。

`/ppp/active/print stats` 命令将显示接收/发送的字节和数据包

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP 地址*) | 客户端从服务器获取的 IP 地址 |
| **bytes** (*整数*) | 通过此连接传输的字节数。第一个数字表示从路由器角度出发的发送流量，第二个数字表示接收流量。 |
| **caller-id** (*字符串*) | 对于 [PPTP](../virtual-private-networks/pptp.md) 和 [L2TP](../virtual-private-networks/l2tp/index.md)，是客户端连接来源的 IP 地址。对于 [PPPoE](../virtual-private-networks/pppoe/index.md)，是客户端连接来源的 MAC 地址。 |
| **encoding** (*字符串*) | 显示此连接中使用的加密和编码（如果不对称，则用 '/' 分隔） |
| **limit-bytes-in** (*整数*) | 允许用户发送到路由器的最大字节数。 |
| **limit-bytes-out** (*整数*) | 允许用户发送到客户端的最大字节数。 |
| **name** (*字符串*) | 在身份验证阶段提供的用户名 |
| **packets** (*整数/整数*) | 通过此连接传输的数据包数。第一个数字表示从路由器角度出发的发送流量，第二个数字表示接收流量 |
| **service** (*async \| isdn \| l2tp \| pppoe \| pptp \| ovpn \| sstp*) | 用户正在使用的服务类型。 |
| **session-id** (*字符串*) | 显示唯一的客户端标识符。 |
| **uptime** (*时间*) | 用户的在线时长 |

## 远程 AAA

**子菜单：** `/ppp/aaa`

此子菜单中的设置允许配置 RADIUS 记账和身份验证。请注意，仅当在本地用户数据库中找不到所需的用户名时，才会查询 RADIUS 用户数据库。

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **accounting** (*yes \| no*；默认：**yes**) | 启用 RADIUS 记账 |
| **interim-update** (*时间*；默认：**0s**) | Interim-Update 时间间隔 |
| **use-radius** (*yes \| no*；默认：**no**) | 通过 RADIUS 启用用户身份验证。如果在本地 secret 数据库中找不到条目，则客户端将通过 RADIUS 进行身份验证。 |
| **enable-ipv6-accounting** (*yes \| no*；默认：**no**) | 启用 IPv6 独立记账。默认情况下，PPP 服务在向 RADIUS 服务器报告网络使用统计信息时，会将 Layer2、IPv4 和 IPv6 数据全部计算在一起。如果需要区分 IPv4 和 IPv6 流量，则可以启用此选项。其工作的前提是必须通过 PPP 服务将前缀分配给客户端，并且必须提供 rate-limit。动态创建的队列统计信息将用作 IPv6 数据的计数器，然后作为单独的 IPv6 统计属性包含在记账数据包中。这不适用于由动态创建的 DHCPv6 服务器根据提供的前缀池或 PPP/Profile 配置分配的前缀。此时前缀分配由 DHCP 服务处理，而非 PPP，因此 PPP 服务无法管理记账。 |

## 示例

#### 添加新配置文件

要添加名为 ex 的配置文件，该配置文件将路由器自身分配为 10.0.0.1 地址，并将 ex 地址池中的地址分配给客户端，同时通过 mypppclients 链过滤来自客户端的流量：

```ros
[admin@rb13] /ppp/profile> add name=ex local-address=10.0.0.1 remote-address=ex incoming-filter=mypppclients
[admin@rb13] /ppp/profile> print
Flags: * - default
 0 * name="default" use-compression=no use-vj-compression=no use-encryption=no only-one=no
     change-tcp-mss=yes
 1   name="ex" local-address=10.0.0.1 remote-address=ex use-compression=default
     use-vj-compression=default use-encryption=default only-one=default change-tcp-mss=default
     incoming-filter=mypppclients
 2 * name="default-encryption" use-compression=default use-vj-compression=default use-encryption=yes
     only-one=default change-tcp-mss=default
[admin@rb13] /ppp/profile>
```

#### 添加新用户

要添加用户 "ex"，密码为 "lkjrht"，配置文件为 "ex"，且仅可用于 PPTP 服务，请输入以下命令：

```ros
[admin@rb13] /ppp/secret> add name=ex password=lkjrht service=pptp profile=ex
[admin@rb13] /ppp/secret> print
Flags: X - disabled
 #   NAME                SERVICE CALLER-ID         PASSWORD          PROFILE            REMOTE-ADDRESS
 0   ex                  pptp                      lkjrht            ex                 0.0.0.0
[admin@rb13] /ppp/secret>
```