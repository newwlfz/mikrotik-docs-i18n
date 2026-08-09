# 代理

> MikroTik RouterOS 代理功能支持 HTTP 和 FTP 缓存、透明代理、基于源/目标地址的访问控制、URL 过滤以及日志记录。它支持直连、父代理以及用于安全性的内容扫描，配置示例包括常规代理和透明代理设置。

import DocCardList from '@theme/DocCardList';

# 代理

本章节涵盖代理功能。使用它来配置反向代理行为及相关的 RouterOS 代理服务。

<DocCardList />

MikroTik RouterOS 对 HTTP 和 HTTP-proxy（针对 FTP 和 HTTP 协议）请求执行代理功能。代理服务器通过存储请求的互联网对象（即通过 HTTP 和 FTP 协议可用的数据）在更靠近接收方的系统上，从而实现互联网对象缓存功能，从而以本地网络速度向客户提供所请求文件的副本，加快客户浏览速度。MikroTik RouterOS 实现了以下代理服务器功能：

- 常规 HTTP 代理 – 客户（自身）指定代理服务器为其服务。
- 透明代理 – 客户不知道代理已启用，且客户端 Web 浏览器无需任何额外配置。
- 基于源地址、目标地址、URL 和请求方法的访问列表（HTTP 防火墙）。
- 缓存访问列表，用于指定哪些对象应缓存，哪些不应缓存。
- 直连访问列表 – 用于指定哪些资源应直接访问，哪些应通过另一台代理服务器访问。
- 日志功能 – 允许获取和存储有关代理操作的信息。
- 父代理支持 – 允许指定另一台代理服务器，*（如果它们没有所请求的对象，则向父代理或原始服务器请求）。*

代理服务器通常放置在用户与互联网上目标服务器（*也称为源服务器*）之间的各个位置。

![](https://manual.mikrotik.com/docs/network-management/proxy/img/proxy-01.webp)

*Web 代理（缓存）* 监视来自客户端的请求，并保存响应的副本。然后，如果对同一 URL 有另一个请求，它可以使用已有的响应，而无需再次向源服务器请求。如果代理未请求过某个文件，它会从原始服务器下载该文件。

代理服务器可能有许多潜在用途：

- 提高资源访问速度（客户端获取对象所需时间更短）。
- 充当 HTTP 防火墙（拒绝访问不希望的网页）。

允许过滤 Web 内容（通过特定参数，如源地址、目标地址、端口、URL、HTTP 请求方法）并扫描出站内容，例如用于数据泄露防护。

:::warning
即使没有缓存，运行 Web 代理也可能很有用，当您只想将其用作类似 HTTP 和 FTP 防火墙（例如，拒绝访问不希望的网页或拒绝特定类型的文件，如 .mp3 文件）或将请求透明地重定向到外部代理（可能具有缓存功能的代理）时。
:::

## 配置示例

**子菜单：** `/ip/proxy`

在 MikroTik RouterOS 中，代理配置在 *`/ip/proxy`* 菜单中执行。以下示例展示如何在端口 8080 上启用代理并将 192.168.88.254 设置为代理源地址：

```ros
[admin@MikroTik] > /ip/proxy/set enabled=yes port=8080 src-address=192.168.88.254
[admin@MikroTik] > /ip/proxy/print 
                 enabled: yes
             src-address: 192.168.88.254
                    port: 8080
               anonymous: no
            parent-proxy: ::
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited
   max-cache-object-size: 2048KiB
           cache-on-disk: no
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: web-proxy
```

:::tip
在设置常规代理服务时，请确保它仅服务于您的客户端，并通过创建防火墙仅允许您的客户端使用代理来防止未经授权的访问；否则，它可能被用作开放代理。
:::

### 透明代理配置示例

RouterOS 还可以充当透明缓存服务器，客户 Web 浏览器无需任何配置。透明代理不会修改请求的 URL 或响应。RouterOS 将接收所有 HTTP 请求并将其重定向到本地代理服务。此过程对用户完全透明（用户可能不知道位于他们与原始服务器之间的代理服务器），对他们来说唯一的区别是浏览速度的提高。

要启用透明模式，必须添加目标 NAT 中的防火墙规则，指定哪些连接（到哪些端口）应被透明地重定向到代理。检查上述代理设置并将我们的用户（192.168.1.0/24）重定向到代理服务器：

```ros
[admin@MikroTik] /ip/firewall/nat> add chain=dstnat protocol=tcp src-address=192.168.1.0/24 dst-port=80 action=redirect to-ports=8080
[admin@MikroTik] /ip/firewall/nat> print
Flags: X - disabled, I - invalid, D - dynamic
 0   chain=dstnat protocol=tcp src-address=192.168.1.0/24 dst-port=80 action=redirect to-ports=8080
```

 Web 代理可以同时用作透明代理和普通 Web 代理。在透明模式下，也可以将其用作标准 Web 代理。但是，在这种情况下，代理用户可能无法访问通过透明方式访问的网页。

### 基于代理的防火墙 – 访问列表

访问列表的实现方式与 MikroTik 防火墙规则相同，从上到下处理。第一条匹配的规则指定对此连接采取的决定。连接可以通过其源地址、目标地址、目标端口、请求的 URL（统一资源定位符）的子字符串或请求方法进行匹配。如果未指定这些参数中的任何一个，则每个连接都将匹配此规则。

如果连接匹配某条规则，则该规则的 action 属性指定连接是被允许还是被拒绝（deny）。如果连接不匹配任何规则，则允许该连接。

在此示例中，假设我们已配置了透明代理服务器。它将阻止网站 [http://www.facebook.com](http://www.facebook.com/)。我们可以通过指定 src-address 来始终为不同网络阻止相同内容：

```ros
/ip/proxy/access/add src-address=192.168.1.0/24 dst-host=www.facebook.com action=deny
```

来自网络 192.168.1.0/24 的用户将无法访问网站 [www.facebook.com](http://www.facebook.com/)。

您还可以阻止 URL 中包含特定词语的网站：

```ros
/ip/proxy/access/add dst-host=:mail action=deny
```

此语句将阻止 URL 中包含词语“mail”的所有网站，例如 [www.mail.com](http://www.mail.com/)、[www.hotmail.com](http://www.hotmail.com/)、[mail.yahoo.com](http://mail.yahoo.com) 等。

***我们还可以阻止下载特定类型的文件，如 .flv、.avi、.mp4、.mp3、.exe、.dat 等。***

```ros
 /ip/proxy/access
 add path=*.flv action=deny
 add path=*.avi action=deny
 add path=*.mp4 action=deny
 add path=*.mp3 action=deny
 add path=*.zip action=deny
 add path=*.rar action=deny
```

这里还提供不同的通配符，用于创建特定条件并通过代理访问列表进行匹配。通配符属性（dst-host 和 path）匹配完整字符串（即，如果设置为“example”，则不会匹配“[example.com](http://example.com)”）。可用的通配符为 '\*'（匹配任意数量的任意字符）和 '?'（匹配任意单个字符）。

此处也接受正则表达式，但如果属性应被视为正则表达式，则应以冒号（':'）开头。

为了表示在给定模式之前不允许任何符号，我们在模式开头使用 ^ 符号。

为了指定在给定模式之后不允许任何符号，我们在模式末尾使用 $ 符号。

## 启用基于 RAM 或存储的缓存

在此示例中，我们假设您已经配置并运行了代理，并且只想启用缓存。如果需要详细的命令/参数说明，请参阅示例部分正下方的参考部分。

- 基于 RAM 的缓存：
  - 适用于具有大量 RAM 用于缓存的设备。在 256MB 或更少 RAM 的设备上启用此功能不会为您的网络带来任何好处。
  - 缓存写入/读取速度远快于存储在 USB 或 SATA 连接介质上的缓存。

- 基于存储的缓存：
  - 由于介质容量差异，可提供更大的代理缓存。

### **RAM 代理缓存：**

## 重要命令

- max-cache-size=
- max-cache-object-size=
- cache-on-disk=

```ros
[admin@MikroTik] /ip/proxy> set max-cache-size=unlimited max-cache-object-size=50000KiB cache-on-disk=no 
...
[admin@MikroTik] /ip/proxy> print 
                 enabled: yes
             src-address: ::
                    port: 8080
               anonymous: no
            parent-proxy: 0.0.0.0
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited  <-------
   max-cache-object-size: 50000KiB  <-------
           cache-on-disk: no  <-------
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no 
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: proxy-cache
```

### **存储代理缓存：**

重要命令：

- max-cache-size=
- max-cache-object-size=
- cache-on-disk=
- cache-path=

```ros
[admin@MikroTik] > /ip/proxy set cache-on-disk=yes cache-path=/usb1/proxy/cache

[admin@MikroTik] > /ip/proxy print                                                
                 enabled: yes
             src-address: ::
                    port: 8080
               anonymous: no
            parent-proxy: 0.0.0.0
       parent-proxy-port: 0
     cache-administrator: webmaster
          max-cache-size: unlimited  <-------
   max-cache-object-size: 50000KiB  <-------
           cache-on-disk: yes  <-------
  max-client-connections: 600
  max-server-connections: 600
          max-fresh-time: 3d
   serialize-connections: no
       always-from-cache: no
          cache-hit-dscp: 4
              cache-path: usb1/proxy/cache  <-------

[admin@MikroTik] > /file/print                                                    
 # NAME                                                           TYPE              
 0 skins                                                          directory        
 5 usb1/proxy                                                     directory           
 6 usb1/proxy/cache                                               web-proxy store   <-------      
 7 usb1/lost+found                                                directory  
```

### 检查缓存是否正常工作

```ros
[admin@MikroTik] > /ip/proxy/monitor 
                 status: running
                 uptime: 2w20h28m25s
     client-connections: 15
     server-connections: 7
               requests: 79772
                   hits: 30513
             cache-used: 481KiB
         total-ram-used: 1207KiB
  received-from-servers: 4042536KiB
        sent-to-clients: 4399757KiB
   hits-sent-to-clients: 176934KiB
```

## 参考

每个菜单的所有可用参数和命令列表。

#### 常规

**子菜单：** `/ip/proxy`

| 属性 | 描述 |
| :-- | :-- |
| **always-from-cache** (*yes \| no*; 默认值：**no**) | 如果内容被视为新鲜，则忽略客户端的刷新请求 |
| **anonymous** (*yes \| no*; 默认值：**no**) | 如果未设置，客户端的 IP 地址将通过 X-Forwarded-For 头传递（可在远程服务器上通过 HTTP\_X\_FORWARDED\_FOR 环境变量访问） |
| **cache-administrator** (*string*; 默认值：**webmaster**) | 在代理错误页面上显示的管理员电子邮件 |
| **cache-hit-dscp** (*integer: 0..63*; 默认值：**4**) | 自动使用提供的 DSCP 值标记缓存命中 |
| **cache-on-disk** (*yes \| no*; 默认值：**no**) | 是否将缓存存储在磁盘上 |
| **cache-path** (*string*; 默认值：**web-proxy**) | 当 cache-on-disk 启用时，缓存将存储的路径。 |
| **max-cache-object-size** (*integer: 0..4294967295[KiB]*; 默认值：**2048KiB**) | 指定最大缓存对象大小，以千字节为单位 |
| **max-cache-size** (*none \| unlimited \| integer: 0..4294967295[KiB]*; 默认值：**unlimited**) | 指定最大缓存大小，以千字节为单位 |
| **max-client-connections** (*integer: Dynamic*; 默认值：**600**) | 从客户端接受的最大连接数（任何进一步的连接将被拒绝） |
| **max-fresh-time** (*time*; 默认值：**3d**) | 存储缓存对象的最长时间。对象的有效期通常由对象本身定义，但如果设置过高，您可以覆盖最大值 |
| **max-server-connections** (*integer: Dynamic*; 默认值：**600**) | 与服务器建立的最大连接数（任何进一步的客户端连接将暂停，直到某些服务器连接终止） |
| **parent-proxy** (*Ip4 \| ip6*; 默认值：**0.0.0.0**) | 另一台 HTTP 代理的 IP 地址，用于将所有请求重定向到该代理。如果设置为 **0.0.0.0**，则不使用父代理。 |
| **parent-proxy-port** (*integer: 0..65535*; 默认值：**0**) | 父代理监听的端口。 |
| **port** (*integer: 0..65535*; 默认值：**8080**) | 代理服务器将监听的 TCP 端口。所有想要使用该服务器作为 HTTP 代理的客户端都必须指定此端口。可以通过在 IP 防火墙中使用目标 NAT 功能将 HTTP 请求重定向到此端口来实现透明（客户端零配置）代理设置 |
| **serialize-connections** (*yes \| no*; 默认值：**no**) | 如果可能，不要为多个客户端连接建立多个服务器连接（即服务器支持持久 HTTP 连接）。客户端将按 FIFO 原则提供服务；当响应传输到前一个客户端完成时，处理下一个客户端。如果客户端空闲时间过长（默认最多 5 秒），它将放弃等待并打开另一个服务器连接 |
| **src-address** (*Ip4 \| Ip6*; 默认值：**0.0.0.0**) | 代理在连接到父代理或网站时将使用指定的地址。如果设置为 **0.0.0.0**，则将从路由表中获取适当的 IP 地址。 |

#### 访问列表

**子菜单：** `/ip/proxy/access`

访问列表的配置类似于常规防火墙规则。规则从上到下处理。第一条匹配的规则指定对此连接采取的决定。总共有 6 个分类器用于指定匹配约束。如果未指定这些分类器中的任何一个，则特定规则将匹配每个连接。

如果连接匹配某条规则，则该规则的 action 属性指定连接是被允许还是被拒绝。如果特定连接不匹配任何规则，则允许该连接。

| 属性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 默认值：**allow**) | 指定是传递还是拒绝匹配的数据包 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 目标服务器的目标地址。 |
| **dst-host** (*string*; 默认值：) | 用于与目标服务器建立连接的 IP 地址或 DNS 名称（这是用户在浏览器中指定特定网页的端口和路径之前输入的字符串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 默认值：) | 数据包目标端口的列表或范围 |
| **local-port** (*integer: 0..65535*; 默认值：) | 指定接收数据包的 Web 代理端口。此值应与 Web 代理正在监听的端口之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 默认值：) | 请求中使用的 HTTP 方法（请参阅本文档末尾的 HTTP 方法部分） |
| **path** (*string*; 默认值：) | 目标服务器内所请求页面的名称（即特定网页或文档的名称，不包括其所在服务器的名称） |
| **redirect-to** (*string*; 默认值：) | 如果访问被此规则拒绝，用户将被重定向到此 URL |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 连接发起方的源地址。 |

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 与此规则匹配的请求计数 |

通配符属性（dst-host 和 dst-path）匹配完整字符串（即，如果设置为“example”，则不会匹配“[example.com](http://example.com)”）。可用的通配符为 '\*'（匹配任意数量的任意字符）和 '?'（匹配任意单个字符）。此处也接受正则表达式，但如果属性应被视为正则表达式，则应以冒号（':'）开头。

使用正则表达式的小提示：

- \\ 符号序列用于在控制台中输入 \ 字符；
- \. 模式仅表示（在正则表达式中，模式中的单个点表示任意符号）；
- 为了表示在给定模式之前不允许任何符号，我们在模式开头使用 ^ 符号。
- 为了指定在给定模式之后不允许任何符号，我们在模式末尾使用 $ 符号。
- 要输入 [ 或 ] 符号，您应该使用反斜杠“\[”对其进行转义；

强烈建议拒绝除路由器后面的 IP 地址之外的所有 IP 地址，因为代理仍可能被用来访问仅供内部使用的（内网）Web 服务器。此外，请参阅防火墙手册中的示例，了解如何保护您的路由器。

#### 直连访问

**子菜单：** `/ip/proxy/direct`

如果指定了 **parent-proxy** 属性，则可以告诉代理服务器是尝试将请求传递给父代理，还是通过直接连接到请求的服务器来解析。直连访问列表的管理方式与前一章中描述的代理访问列表相同，只是 action 参数不同。与访问列表不同，直连代理访问列表的默认操作等于 deny。当未指定规则或特定请求不匹配任何规则时，将采用此操作。

| 属性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 默认值：**allow**) | 指定对匹配数据包执行的操作：allow - 始终直接解析匹配的请求，绕过父代理deny - 通过父代理解析匹配的请求。如果未指定，则与 allow 效果相同。 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 目标服务器的目标地址。 |
| **dst-host** (*string*; 默认值：) | 用于与目标服务器建立连接的 IP 地址或 DNS 名称（这是用户在浏览器中指定特定网页的端口和路径之前输入的字符串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 默认值：) | 与目标服务器连接使用的端口列表或范围。 |
| **local-port** (*integer: 0..65535*; 默认值：) | 指定接收数据包的 Web 代理端口。此值应与 Web 代理正在监听的端口之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 默认值：) | 请求中使用的 HTTP 方法（请参阅本文档末尾的 [HTTP 方法](#http-methods) 部分） |
| **path** (*string*; 默认值：) | 目标服务器内所请求页面的名称（即特定网页或文档的名称，不包括其所在服务器的名称） |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 连接发起方的源地址。 |

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 与此规则匹配的请求计数 |

#### 缓存管理

**子菜单：** `/ip/proxy/cache`

缓存访问列表指定哪些请求（域、服务器、页面）应由 Web 代理在本地缓存，哪些不应缓存。此列表的实现方式与 Web 代理访问列表完全相同。默认操作是缓存对象（如果未找到匹配规则）。

| 属性 | 描述 |
| :-- | :-- |
| **action** (*allow \| deny*; 默认值：**allow**) | 指定对匹配数据包执行的操作：allow - 缓存匹配请求中的对象deny - 不缓存匹配请求中的对象 |
| **dst-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 目标服务器的目标地址 |
| **dst-host** (*string*; 默认值：) | 用于与目标服务器建立连接的 IP 地址或 DNS 名称（这是用户在浏览器中指定特定网页的端口和路径之前输入的字符串） |
| **dst-port** (*integer[-integer[,integer[,...]]]: 0..65535*; 默认值：) | 数据包目标端口的列表或范围。 |
| **local-port** (*integer: 0..65535*; 默认值：) | 指定接收数据包的 Web 代理端口。此值应与 Web 代理正在监听的端口之一匹配。 |
| **method** (*any \| connect \| delete \| get \| head \| options \| post \| put \| trace*; 默认值：) | 请求中使用的 HTTP 方法（请参阅本文档末尾的 HTTP 方法部分） |
| **path** (*string*; 默认值：) | 目标服务器内所请求页面的名称（即特定网页或文档的名称，不包括其所在服务器的名称） |
| **src-address** (*Ip4[-Ip4 \| /0..32] \| Ip6/0..128*; 默认值：) | 连接发起方的源地址 |

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **hits** (*integer*) | 与此规则匹配的请求计数 |

#### 连接

**子菜单：** `/ip/proxy/connections`

此菜单包含代理当前正在服务的连接列表。

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **client** () |  |
| **dst-address** (*Ip4 \| Ip6*) | 连接的 IPv4/IPv6 目标地址 |
| **protocol** (*string*) | 协议名称 |
| **rx-bytes** (*integer*) | 客户端接收的字节数 |
| **server** () |  |
| **src-address** (*Ip4 \| Ip6*) | 连接发起方的 IPv4/IPv6 地址 |
| **state** (*closing \| connecting \| converting \| hotspot \| idle \| resolving \| rx-header \| tx-body \| tx-eof \| tx-header \| waiting*) | 连接状态：closing - 数据传输已完成，连接正在结束connecting - 正在建立连接converting - 替换响应或请求数据包中的头部和尾部字段hotspot - 检查热点认证是否允许继续（用于热点代理）idle - 保持空闲resolving - 正在解析服务器的 DNS 名称rx-header - 正在接收 HTTP 头部tx-body - 正在向客户端传输 HTTP 主体tx-eof - 正在写入块结束（当转换为分块响应时）tx-header - 正在向客户端传输 HTTP 头部waiting - 等待对端传输 |
| **tx-bytes** (*integer*) | 客户端发送的字节数 |

#### 缓存插入

**子菜单：** `/ip/proxy/inserts`

此菜单显示存储在缓存中的对象统计信息（缓存插入）。

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **denied** (*integer*) | 被缓存列表拒绝的插入次数。 |
| **errors** (*integer*) | 磁盘或其他系统相关错误的数量 |
| **no-memory** (*integer*) | 由于内存不足而未存储的对象数量 |
| **successes** (*integer*) | 成功的缓存插入次数。 |
| **too-large** (*integer*) | 因过大而无法存储的对象数量 |

#### 缓存查找

**子菜单：** `/ip/proxy/lookup`

此菜单显示从缓存中读取的对象的统计信息（缓存查找）。

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **denied** (*integer*) | 被访问列表拒绝的请求数量。 |
| **expired** (*integer*) | 在缓存中找到但已过期，因此向外部服务器请求的请求数量 |
| **no-expiration-info** (*integer*) | 收到针对没有信息可比较请求的页面的条件请求 |
| **non-cacheable** (*integer*) | 无条件向外部服务器请求的请求数量（因为缓存访问列表拒绝缓存它们） |
| **not-found** (*integer*) | 在缓存中未找到，因此向外部服务器（或根据配置向父代理）请求的请求数量 |
| **successes** (*integer*) | 在缓存中找到的请求数量。 |

#### 缓存内容

**子菜单：** `/ip/proxy/cache-contents`

此菜单显示缓存的内容。

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **file-size** (*integer*) | 缓存对象大小 |
| **last-accessed** (*time*) |  |
| **last-accessed-time** (*time*) |  |
| **last-modified** (*time*) |  |
| **last-modified-time** (*time*) |  |
| **uri** (*string*) | 缓存对象的统一资源标识符 |

## HTTP 方法

##### Options

此方法是请求获取有关客户端与由 **Request-URI** 标识的服务器之间链路上可用通信选项的信息。该方法允许客户端确定与资源关联的选项和（或）要求，而无需发起任何资源检索。

##### GET

此方法检索由 Request-URI 标识的任何信息。如果 Request-URI 引用数据处理过程，则对 GET 方法的响应应包含该过程产生的数据，而不是过程程序的源代码，除非源代码是过程的结果。

如果请求消息包含 If-Modified-Since、If-Unmodified-Since、If-Match、If-None-Match 或 If-Range 头字段，则 GET 方法可以变为条件 GET。条件 GET 方法用于通过指定仅在条件头字段描述的情况下才应发生实体传输来减少网络流量。

如果请求消息包含 Range 头字段，则 GET 方法可以变为部分 GET。部分 GET 方法旨在通过仅请求实体的部分内容而不传输客户端已持有的数据来减少不必要的网络使用。

对 GET 请求的响应是可缓存的，当且仅当它满足 HTTP 缓存的要求。

##### HEAD

此方法具有 GET 方法的所有特性，但服务器不得在响应中返回消息体。这检索请求所隐含的实体的元信息，这导致其广泛用于测试超文本链接的有效性、可访问性和最近修改。

对 HEAD 请求的响应可以以响应中包含的信息可用于更新先前由该 Request-URI 标识的缓存实体的方式缓存。

##### POST

此方法请求源服务器接受请求中包含的实体作为由 Request-URI 标识的资源的新下属。

POST 方法执行的实际操作由源服务器确定，并且通常依赖于 Request-URI。

对 POST 方法的响应不可缓存，除非响应包含适当的 Cache-Control 或 Expires 头字段。

##### PUT

此方法请求将包含的实体存储在提供的 Request-URI 下。如果在指定的 Request-URI 下存在另一个实体，则包含的实体应被视为源服务器上驻留实体的更新（更新）版本。如果 Request-URI 未指向现有资源，则源服务器应使用该 URI 创建资源。

如果请求通过缓存并且 Request-URI 标识一个或多个当前缓存的实体，则这些条目应被视为过时。对此方法的响应不可缓存。

##### TRACE

此方法调用远程的应用层请求消息环回。请求的最终接收者应将接收到的消息作为 200 (OK) 响应的实体主体反射回客户端。最终接收者是源服务器或第一个在请求中接收到 Max-Forwards 值为 0 的代理或网关。TRACE 请求不得包含实体。

对此方法的响应不得缓存。