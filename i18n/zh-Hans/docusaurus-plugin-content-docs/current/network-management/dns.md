# DNS

> 本页介绍 MikroTik RouterOS 中的 DNS 功能，说明如何将路由器配置为 DNS 缓存或主服务器，并提供远程请求、缓存策略和动态服务器集成等选项。详细介绍了缓存大小、TTL 设置和 DNS over HTTPS (DoH) 支持等配置属性。

# DNS

## 简介

域名系统（DNS）通常指互联网的电话簿。换句话说，DNS 是一个数据库，将字符串（称为主机名），如 [mikrotik.com](https://mikrotik.com)，链接到特定的 IP 地址，如 159.148.172.205 或 2a02:610:7501:2000::205。

启用 DNS 功能的 MikroTik 路由器可以被设置为任何符合 DNS 规范的客户端的 DNS 缓存。此外，MikroTik 路由器可以在其 DHCP 服务器设置中被指定为主 DNS 服务器。当启用远程请求时，MikroTik 路由器会在端口 53 上响应 TCP 和 UDP DNS 请求。

当同时设置了静态和动态服务器时，静态服务器条目优先，但这并不表示静态服务器总是会被使用（例如，之前从动态服务器收到查询，但后来添加了静态服务器，则动态条目将被优先使用）。

:::tip
当使用 DNS 服务器 *allow-remote-requests* 时，请确保仅允许已知主机通过 TCP 和 UDP 协议端口 53 访问您的服务器。

:::

有多种方式可以管理局域网上的 DNS 功能——使用公共 DNS、将路由器用作缓存，或不干预 DNS 配置。以以下设置为例：互联网服务提供商（ISP）→ 网关（GW）→ 局域网（LAN）。GW 是基于 RouterOS 的设备，采用默认配置：

- 您不在“GW”DHCP 服务器网络配置中配置任何 DNS 服务器——设备将把从 `ISP` 接收的 DNS 服务器 IP 地址配置转发给 `LAN` 设备。
- 您在“GW”DHCP 服务器网络配置中配置 DNS 服务器——设备将把配置的 DNS 服务器提供给 `LAN` 设备（同时必须启用 `/ip/dns/set allow-remote-requests=yes`）。
- 在“GW”DHCP 服务器网络配置中将“dns-none”配置为 DNS 服务器——设备不会将任何**动态** DNS 服务器转发给 `LAN` 设备。

### DNS 配置

DNS 功能用于为路由器自身以及连接到路由器的客户端提供域名解析。

| 属性 | 描述 |
| :-- | :-- |
| **allow-remote-requests** (*yes* \| *no*; 默认值：**no**) | 指定是否允许将路由器用作远程客户端的 DNS 缓存。否则，只有路由器本身会使用 DNS 配置。 |
| **address-list-extra-time** *(时间; 默认值：**0s**)* | 创建地址列表条目时，在 TTL 基础上额外增加的时间。 |
| **cache-max-ttl** (*时间*; 默认值：**1w**) | 缓存记录的最大生存时间。换句话说，缓存记录在 cache-max-TTL 时间后无条件过期。从 DNS 服务器接收的较短 TTL 会被尊重。 |
| **cache-size** (*整数[64..4294967295]*; 默认值：**2048**) | 指定 DNS 缓存的大小，单位为 KiB。 |
| **max-concurrent-queries** (*整数*; 默认值：**100**) | 指定允许的并发查询数量。 |
| **max-concurrent-tcp-sessions** (*整数*; 默认值：**20**) | 指定允许的并发 TCP 会话数量。 |
| **max-udp-packet-size** (*整数 [50..65507]*; 默认值：**4096**) | 允许的 UDP 数据包的最大大小。 |
| **mdns-repeat-ifaces** (*接口列表*; 默认值：) | 当此列表中的接口收到 mDNS 数据包时，会将其转发到此列表中的所有其他接口。仅支持 IPv4。 |
| **query-server-timeout** (*时间*; 默认值：**2s**) | 指定等待服务器查询响应的时长。 |
| **query-total-timeout** (*时间*; 默认值：**10s**) | 指定等待查询响应的总时长。请注意，此设置必须结合“query-server-timeout”和所用 DNS 服务器的数量进行配置。 |
| **servers** (*IPv4/IPv6 地址列表@vrf*; 默认值：) | DNS 服务器 IPv4/IPv6 地址列表 |
| **cache-used** (*整数*) | 显示当前使用的缓存大小，单位为 KiB |
| **dynamic-server** (*IPv4/IPv6 列表*) | 从不同服务（例如 DHCP）动态添加的 DNS 服务器列表。 |
| **doh-max-concurrent-queries** (*整数*; 默认值：**50**) | 指定允许的 DoH 并发查询数量。 |
| **doh-max-server-connections** (*整数*; 默认值：**5**) | 指定允许的到 DoH 服务器的并发连接数。 |
| **doh-timeout** (*时间*; 默认值：**5s**) | 指定等待 DoH 服务器查询响应的时长。 |
| **use-doh-server** (*字符串; 默认值：)* | 指定 DNS 查询必须使用的 DoH 服务器。如果指定，DoH 功能将覆盖“*servers*”的使用。服务器必须以“https://”前缀指定。仅支持一个 DoH 服务器。 |
| **verify-doh-cert** (*yes* \| *no*; 默认值：**no**) | 指定是否验证 DoH 服务器（当使用 DoH 服务器时）。将使用“/certificate”列表来验证服务器有效性。 |
| **vrf** (vrf; 默认值：main) | 指定应使用 DNS 解析器的 VRF。DNS 解析器仅处理来自指定 VRF 或解析器本身的请求。 |

```text
[admin@MikroTik] > ip dns print         
                      servers: 
              dynamic-servers: 10.155.0.1
               use-doh-server: 
              verify-doh-cert: no
   doh-max-server-connections: 5
   doh-max-concurrent-queries: 50
                  doh-timeout: 5s
        allow-remote-requests: yes
          max-udp-packet-size: 4096
         query-server-timeout: 2s
          query-total-timeout: 10s
       max-concurrent-queries: 100
  max-concurrent-tcp-sessions: 20
                   cache-size: 2048KiB
                cache-max-ttl: 1d
                   cache-used: 48KiB
```

动态 DNS 服务器从 RouterOS 中可用的不同功能获取，例如 DHCP 客户端、VPN 客户端、IPv6 路由器通告等。

服务器按队列顺序处理——静态服务器作为有序列表，动态服务器作为有序列表。当 DNS 缓存需要向服务器发送请求时，它会逐一尝试服务器，直到其中一个响应。之后，该服务器将用于所有类型的 DNS 请求。同一服务器用于任何类型的 DNS 请求，例如 A 和 AAAA 类型。如果只使用动态服务器，则重启后 DNS 返回的结果可能会改变，因为服务器可能以不同的顺序加载到 IP/DNS 设置中，这取决于从上述功能接收它们的速度。

如果在某个时刻正在使用的服务器变得不可用且无法提供 DNS 应答，则 DNS 缓存会重新启动 DNS 服务器查找过程，并再次遍历指定的服务器列表。

### DNS 缓存

此菜单提供两个存储在服务器上的 DNS 记录列表：

- *“*`/ip/dns/cache`*”*：此菜单提供 RouterOS 缓存可以响应客户端请求的缓存 DNS 条目列表；
- *“*`/ip/dns/cache/all`*”*：此菜单提供所有存储的缓存 DNS 记录的完整列表，也包括例如 PTR 记录。

:::tip
您可以使用命令 `/ip/dns/cache/flush` 清空 DNS 缓存。

:::

### DNS 静态

MikroTik RouterOS DNS 缓存具有额外的嵌入式 DNS 服务器功能，允许您配置多种类型的 DNS 条目，供使用路由器作为 DNS 服务器的 DNS 客户端使用。此功能也可用于向网络客户端提供虚假的 DNS 信息。例如，它可以解析对特定域名集合（或整个互联网）的任何 DNS 请求到您自己的页面。

```text
[admin@MikroTik] /ip/dns/static/add name=www.mikrotik.com address=10.0.0.1

```

该服务器还能够基于基本正则表达式解析 DNS 请求，以便多个请求可以匹配同一个条目。如果条目不符合 DNS 命名标准，则被视为正则表达式。列表是有序的，并从上到下进行检查。首先检查正则表达式，然后检查普通记录。

使用正则表达式匹配 DNS 请求：

```text
[admin@MikroTik] /ip/dns/static/add regexp=".*mikrotik.*" address=10.0.0.2
```

如果 DNS 静态条目列表匹配请求的域名，则路由器将假定该路由器负责该特定名称的任何类型的 DNS 请求。例如，如果列表中只有“A”记录，但路由器收到“AAAA”请求，则它将从静态列表回复“A”记录，并将向上游服务器查询“AAAA”记录。如果记录存在，则转发回复。如果不存在，则路由器将回复一个不带任何记录的“ok”DNS 回复。如果您想用不可用的记录覆盖来自上游服务器的域名记录，例如，您可以为特定域名添加静态条目并为其指定一个虚拟 IPv6 地址“::ffff”。

以有序列表形式列出所有配置的 DNS 条目：

```text
[admin@MikroTik] /ip/dns/static/print 
Columns: NAME, REGEXP, ADDRESS, TTL
# NAME             REGEXP       ADDRESS   TTL
0 www.mikrotik.com               10.0.0.1  1d 
1                  [*mikrotik*]  10.0.0.2  1d
```

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IPv4/IPv6*) | 将用于“A”或“AAAA”类型记录的地址。 |
| **cname**(*字符串**)* | 域名的别名。 |
| **forward-to** | 特定 DNS 请求必须转发到的域名服务器的 IP 地址。 |
| **mx-exchange** (*字符串*) | MX 服务器的域名。 |
| **name** (*字符串)* | 域名。 |
| **srv-port** (*整数*; 默认值：0) | 查找服务的 TCP 或 UDP 端口。 |
| **srv-target** | 提供服务的主机的规范主机名，以点结尾。 |
| **text** (*字符串**)* | 关于域名的文本信息。 |
| **type**(*A* \| *AAAA* \| *CNAME* \| *FWD* \| *MX* \| *NS* \| *NXDOMAIN* \| *SRV* \| *TXT* ; 默认值：*A*) | DNS 记录的类型。 |
| **address-list** (*字符串**)* | 防火墙地址列表的名称，当某个请求匹配条目时，地址必须动态添加到该列表。当 TTL 过期时，条目将从地址列表中移除。 |
| **comment**(*字符串**)* | 关于域名记录的注释。 |
| **disabled** (*yes* \| *no*; 默认值：yes) | DNS 记录是否处于活动状态。 |
| **match-subdomain** (*yes* \| *no*; 默认值：no) | 记录是否匹配子域的请求。 |
| **mx-preference** (*整数*; 默认值：0) | 特定 MX 记录的优先级。 |
| **ns**(*字符串*) | 特定记录的权威域名服务器的名称。 |
| **regexp** (正则表达式) | 用于验证域名的正则表达式。 |
| **srv-priority** (*整数*; 默认值：0) | 特定 SRV 记录的优先级。 |
| **srv-weight** (*整数*; 默认值：0) | 特定 SRV 记录的权重。 |
| **ttl** (*时间*; 默认值：*24h*) | 缓存记录的最大生存时间。 |

:::info
对于每个静态 A 和 AAAA 记录，缓存中会自动添加一条 PTR 记录。

:::

:::warning
正则表达式区分大小写，但 DNS 请求不区分大小写，因此 RouterOS 在匹配任何静态条目之前会将 DNS 名称转换为小写。您应该只使用小写字母编写正则表达式。正则表达式匹配比纯文本条目慢得多，因此建议尽量减少正则表达式规则的数量并优化表达式本身。

:::

:::warning
通过混合用户界面（CLI 和 GUI）配置正则表达式时要小心。从 CLI 添加条目本身可能需要转义字符。建议添加条目并执行 print 命令，以验证正则表达式在添加过程中未被更改。

:::

## DNS over HTTPS (DoH)

RouterOS 支持 DNS over HTTPS (DoH)。DoH 使用 HTTPS 协议发送和接收 DNS 请求，以获得更好的数据完整性。主要目标是通过消除“中间人”攻击（MITM）来提供隐私。

[视频：DoH 设置](http://youtube.com/watch?v=w4erB0VzyIE)

配置 DoH 服务器：

```ros
/ip/dns/set use-doh-server=DoH_Server_Query_URL verify-doh-cert=yes
```

:::info
可以使用[内置证书颁发机构存储](../authentication-authorization-accounting/certificates.md#built-in-trust-store-authorities)进行 DoH 服务器证书验证，无需手动导入相关的根证书。
:::

:::info
仅支持一个 DoH 服务器。

:::

请注意，您至少需要配置一个常规 DNS 服务器，以便路由器自行解析 DoH 主机名。

```ros
/ip/dns/set servers=1.1.1.1
```

如果您没有配置任何动态或静态 DNS 服务器，请为 DoH 服务器域名添加静态 DNS 条目，如下所示：

```ros
/ip/dns/static/add address=IP_Address name=Domain_Name
```

:::tip
如果正在使用 DoH 服务器（DoH DNS 名称可以解析），则它将是当时唯一工作的 DNS 服务，IP/DNS 服务器列表中的标准 DNS 服务器将不会被使用。

:::

:::tip
如果 *`/certificate/settings/set` crl-use* 设置为 *yes*，RouterOS 将检查证书链中每个证书的 CRL，因此，应将整个证书链安装到设备中——从根 CA 开始，包括中间 CA（如果有），以及用于特定服务的证书。

例如，Google DoH、Cloudflare 和 OpenDNS 的完整链包含三个证书，NextDNS 有四个证书。

:::
:::info
ARM64、x86 和 CHR 设备在与 DoH 服务器通信时协商 HTTP/2。如果服务器支持，路由器使用 HTTP/2 进行 DNS over HTTPS 查询，与 HTTP/1.1 相比，提供了改进的多路复用和更低的延迟。如果任何一方不支持 HTTP/2，连接将回退到 HTTP/1.1。

:::

### 已知兼容/不兼容的 DoH 服务

#### 兼容的 DoH 服务

- Cloudflare
- Google
- NextDNS
- OpenDNS

#### 不兼容的 DoH 服务

- Mullvad
- Yandex
- UncensoredDNS
- Quad9

## Adlist

Adlist 是网络级广告拦截的组成部分，包含一组精选的已知用于提供广告的域名。此功能通过利用域名系统（DNS）解析来拦截对这些域名的 A 和 AAAA 请求。当客户端设备向 DNS 服务器查询 adlist 上列出的域名时，DNS 解析过程会被改变。DNS 服务器不会返回广告服务域名的实际 IP 地址，而是响应 IP 地址 0.0.0.0。这有效地将请求空路由，因为 0.0.0.0 是一个不可路由的元地址，用于表示无效、未知或不适用的目标。通过以这种方式重定向广告相关请求，adlist 功能确保广告内容不被加载，从而增强网络性能并通过减少不需要的广告流量来改善用户体验。

[视频：Adlist 设置](http://youtube.com/watch?v=RMJnjyAOfLI)

:::warning
**配置前，请增加 DNS 缓存，因为它用于存储 adlist 条目。如果达到限制，DNS 错误主题中会打印错误“*adlist read: max cache size reached*”**

:::

:::warning
Adlist 存储在设备的内部存储器上。确保有足够的可用空间来保存所需的 adlist。

:::

| 属性 | 描述 |
| :-- | :-- |
| url | 用于指定 adlist 的 URL。 |
| ssl-verify | 指定是否验证 Adlist URL 服务器的 SSL 证书。它将使用“/certificate”列表来验证服务器有效性。 |
| match-count | 匹配的 DNS 名称请求计数。 |
| name-count | 从 Adlist 导入的 DNS 名称计数。 |
| file | 用于指定从中读取 adlist 数据的本地文件路径。 |
| pause | 暂时暂停使用所有 adlist。 |
| reload | 检查所有列表的更新，如果发现更新，则更新列表，根据需要移除或添加条目，执行 reload 时不会完整重新下载列表，而是仅执行必要的更新。**重要提示：** 不强制使用 reload 来更新列表，Adlist 每四小时检查一次新更新。     |

### Adlist 白名单

要将某些域名从 Adlist 中豁免，您需要创建静态 DNS FWD 条目，例如 `/ip/dns/static/add name=bar.test type=FWD`，如果存在此类条目，则如果路由器有相关的静态 DNS 条目 `/ip/dns/static/add name=bar.test type=A`，查询将由路由器应答；或者，如果没有静态规则，则转发到下一个 DNS，无论是动态的还是 `/ip/dns/set servers=` 下配置的，FWD 条目也支持 DoH。

### 配置示例

#### 基于 URL 的 adlist

```ros
/ip/dns/adlist/add url=https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts ssl-verify=no
```

要查看存在和匹配的域名数量，您可以运行：

```ros
/ip/dns/adlist/print 
Flags: X - disabled 
0 url="https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts" ssl-verify=no match-count=122 name-count=164769

```

#### 本地托管的 adlist

要创建您自己的 adlist，您可以创建一个包含域名的文本文件。示例：

```
0.0.0.0 example1.com
0.0.0.0 eu1.example.com
0.0.0.0 ex.com
0.0.0.0 com.example.com
```

:::info
您可以在 PC 上创建 txt 文件，但也可以在 RouterOS 中创建，使用以下命令：

“/file/add name=host.txt”，然后您可以运行“/file/edit host.txt contents”添加条目。按“ctrl o”保存条目。

:::

要将文件添加到 adlist：

```ros
/ip/dns/adlist/add file=host.txt

```

:::info
您可以使用 `/ip/dns/adlist/print` 验证文件格式是否正确，结果将显示您添加了多少主机名，主机名格式必须与前面示例中给出的格式匹配。

:::

```ros
/ip/dns/adlist/print 
Flags: X - disabled 
 0   file=host.txt match-count=0 name-count=4 
```

## 转发器

DNS 转发器允许用户配置一个命名的 DNS 转发器，该转发器可用作静态 FWD 条目的 *forward-to* 值。

对于每个 *转发器*，可以配置多个常规上游服务器和 DoH 服务器。配置的 *转发器* 服务器将使用轮询算法——对于每个查询，将使用下一个服务器来解析 DNS 名称。

### 转发器配置

在 *`/ip/dns/forwarders`* 部分，可以添加、修改或删除 *转发器*。

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串;* 默认值：) | 转发器名称。 |
| **dns-servers** (*字符串*; 默认值：) | 域名服务器的 IP 地址或 DNS 名称。可以包含多个记录，例如，*dns-servers=1.1.1.1,8.8.8.8,local.dns* |
| **doh-servers**(*字符串;* 默认值：) | DoH 服务器的 URL。可以包含多个记录。 |
| **verify-doh-cert** (*yes* \| *no**;* 默认值：*yes*) | 指定是否验证 DoH 服务器（当使用 DoH 服务器时）。它将使用“/certificate”列表来验证服务器有效性。 |

### 配置示例

配置/添加一个 *转发器*：

```routeros
/ip/dns/forwarders
add dns-servers=1.1.1.1,local.dns doh-servers=https://dns.google/dns-query name=forwarder1
```

配置/添加一个静态 DNS FWD 条目：

```routeros
/ip/dns/static
add forward-to=forwarder1 name=mikrotik.com type=FWD
```

现在，每次路由器收到解析 [mikrotik.com](http://mikrotik.com) 的请求时，使用轮询算法的请求将被转发到 *1.1.1.1*、*local.dns* 或 *Google DoH* 服务器。

## mDNS

RouterOS 支持[组播 DNS (mDNS)](https://datatracker.ietf.org/doc/html/rfc6762) 用于本地网络服务发现。默认情况下，mDNS 在单个子网内运行。mDNS 中继器功能允许使用“mdns-repeat-ifaces”属性将 mDNS 功能扩展到不同接口或 VLAN。

### 使用 mDNS 中继器的影响

- 跨子网服务发现：不同子网或 VLAN 上的设备可以相互发现，增强了查找服务（例如打印机、文件共享）的能力。
- 增加网络流量：mDNS 中继器可能会增加组播流量，这可能导致拥塞，尤其是在设备较多的大型网络中。

mDNS 中继器通常与以下设备一起使用：

- Apple 生态系统（AirPrint、AirPlay）。
- 智能家居设备（Thread、IoT）。
- Chromecast 和媒体流。
- Avahi（Linux/Unix）。

要在接口之间启用 mDNS 中继器，允许连接到这些接口的设备使用 mDNS 相互发现，请使用以下命令：

```routeros
/ip/dns/set mdns-repeat-ifaces=<interface1>,<interface2>
```

:::info
mDNS 中继器需要支持组播的接口（例如以太网、VLAN、桥接）。不支持隧道接口，如 WireGuard。

目前仅支持 IPv4。

:::

:::warning
MikroTik mDNS 中继器是一种本地服务，拦截组播数据包以重新广播。它需要“input”规则。mDNS 组播流量不经过“forward”链。如果您有严格的防火墙规则保护路由器免受本地子网攻击，则必须在任何 drop 规则之前明确允许 mDNS 流量——允许在“input”链上接收 UDP 端口 5353 的流量。

:::