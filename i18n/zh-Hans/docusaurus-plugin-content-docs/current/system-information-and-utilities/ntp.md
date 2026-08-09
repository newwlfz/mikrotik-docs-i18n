# NTP

> RouterOS 文档中的 NTP 部分涵盖了客户端和服务器的配置，包括启用模式、支持 IPv4/IPv6 的服务器列表、VRF 设置、认证密钥以及状态监控（如频率漂移和同步层级）。文档还警告了使用本地时钟进行精确计时的风险，并列出了 NTP 日志消息。

# NTP

RouterOS 主包中包含基于 RFC5905 的网络时间协议（NTP）客户端和服务器功能。

### NTP 客户端属性

客户端配置位于 `/system/ntp/client`

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes, no 默认: no*) | 启用 NTP 客户端进行时间同步 |
| **mode** (*broadcast, manycast, multicast, unicast*) | NTP 客户端将运行的模式 |
| **NTP 服务器** | NTP 服务器列表。可以添加静态条目。支持以下格式：  - 可以使用 FQDN（如果地址已解析，则在“服务器”窗口的相应列中显示“已解析地址”）或 IP 地址。如果 DHCP-Client 属性 **use-peer-ntp=yes** - 由 [DHCP](../network-management/dhcp.md) 通告的动态条目  - *ipv4*  - *ipv4*`@`*vrf*  - *ipv6*  - *ipv6*`@`*vrf*  - *ipv6-linklocal*`%`*interface* |
| **vrf** (*默认: main*) | 虚拟路由和转发 |
| **服务器** (*按钮/部分*) | 动态和静态添加的 NTP 服务器的详细表格（地址、已解析地址、最小轮询、最大轮询、iBurst、认证密钥） 要使用 FQDN 设置 NTP 服务器。每次发送 NTP 请求时都会解析域名。路由器必须配置了 *`/ip/dns`*。 |
| **对等体** | 当前参数值  `[admin@ntp-example_v7] > /system/ntp/monitor-peers``type="ucast-client" address=x.x.x.x refid="y.y.y.y" stratum=3 hpoll=10 ppoll=10 root-delay=28.869 ms root-disp=50.994 ms``offset=-0.973 ms delay=0.522 ms disp=15.032 ms jitter=0.521 ms``-- [Q quit  D dump  C-z pause]` |
| **密钥** | NTP 对称密钥，用于 NTP 客户端和服务器之间的认证。密钥标识符（Key ID）- 一个整数，用于标识生成消息认证码的加密密钥。 |

#### 状态

- **synchronized, stopped, waiting, using-local-clock** - NTP 客户端的当前状态。
- **频率漂移** - 每单位时间的分数频率漂移。
- **synced-server** - NTP 服务器的 IP 地址。
- **synced-stratum** - 每台服务器的准确性由称为层级的数字定义，最高层（主服务器）分配为 1，层级中的每一层（次服务器）分配为比前一层大 1 的数字。
- **system-offset** - 这是一个带符号的定点数，表示 NTP 服务器时钟相对于本地时钟的偏移量，以秒为单位。

### NTP 客户端服务器属性

客户端配置位于 `/system/ntp/client/servers`

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no; 默认: yes*) | 启用 NTP 客户端服务器。 |
| **comment** (*string;* 默认: ) | 项目的描述性名称。 |
| **address** (IPv4 地址 [IPv4]*, IPv6 地址 [IPv6],* 域名; 默认: ) | NTP 服务器的 IP 地址或域名。 |
| **resolved-address** (IPv4 地址 [IPv4]*, IPv6 地址 [IPv6]; 默认:* ) | 域名解析后获得的 NTP 服务器的实际 IP 地址。 |
| **min-poll** (*integer:* 3..17; 默认: 6) | 确定 NTP 查询之间的最短间隔（2 的幂，以秒为单位）。更多详细信息请参阅 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html)。 |
| **max-poll** (*integer*: 3..17; 默认: 10) | 确定 NTP 查询之间的最长间隔（2 的幂，以秒为单位）。更多详细信息请参阅 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html)。 |
| **iburst**(*yes \| no; 默认: yes*) | 确定初始突发是禁用还是启用。IBurst 告诉 NTP 客户端仅在启动时发送快速突发数据包。更多详细信息请参阅 [RFC5905](https://www.rfc-editor.org/rfc/rfc5905.html)。 |
| **auth-key** (默认值: *none*) | NTP 对称密钥，用于 NTP 客户端和服务器之间的认证。密钥标识符（Key ID）- 一个整数，用于标识生成消息认证码的加密密钥。 |

### NTP 服务器设置

服务器配置位于 `/system/ntp/server`

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes* 或 *no*; 默认值: *no*) | 启用 NTP 服务器 |
| **broadcast** (*yes* 或 *no*; 默认值: *no*) | 启用特定的 NTP 服务器模式，要使此模式工作，您必须设置广播地址字段 |
| **multicast** (*yes* 或 *no*; 默认值: *no*) | 启用特定的 NTP 服务器模式 |
| **manycast** (*yes* 或 *no*; 默认值: *no*) | 启用特定的 NTP 服务器模式 |
| **broadcast-addresses** (*IP 地址*; 默认值: ) | 设置用于 NTP 服务器广播模式的广播地址 |
| **vrf** (*默认: main*) | 虚拟路由和转发 |
| **use-local-clock** (*yes* 或 *no*; 默认值: *no*) | 如果其他时间源不可用，服务器将提供其本地系统时间作为有效时间。 |
| **local-clock-stratum** | 如果 **use-local-clock=yes**，手动设置层级 |
| **auth-key** (默认值: *none*) | NTP 对称密钥，用于 NTP 客户端和服务器之间的认证。密钥标识符（Key ID）- 一个整数，用于标识生成消息认证码的加密密钥。 |

:::danger
如果您使用 use-local-clock，请注意路由器的内部 CPU 时钟不是精确计时操作的可靠时间源，因为其频率可能因电源管理、热条件和硬件差异而变化，即使在相同型号之间也是如此。这种变化是预期的，不会影响路由器的正常性能。为了准确计时，建议使用基于网络的时间同步，例如 NTP（网络时间协议）。
:::

### 日志消息

SNTP 客户端可以生成以下日志消息。有关如何设置日志记录和检查日志，请参阅“[日志](../diagnostics-monitoring-and-troubleshooting/log/index.md)”一文。

- **ntp**,**debug** 逐渐调整 *OFFS*。
- **ntp**,**debug** 立即调整 *OFFS*。
- **ntp**,**debug** 等待 *N* 秒后再发送下一条消息。
- **ntp**,**debug** 等待 *N* 秒后重新启动。
- **ntp**,**debug**,**packet** 数据包收到错误，正在重新启动。
- **ntp**,**debug**,**packet** 收到 *PKT*。
- **ntp**,**debug**,**packet** 忽略收到的 *PKT*。
- **ntp**,**debug**,**packet** 发送到 *IP* 时出错，正在重新启动。
- **ntp**,**debug**,**packet** 正在发送到 *IP* *PKT*。

#### 日志消息字段说明

- *OFFS* - 两个 NTP 时间戳值之间的差异，以十六进制表示。
- *PKT* - NTP 数据包的转储。如果数据包短于最小 48 字节，则将其转储为十六进制字符串。否则，数据包将转储为字段名称和值的列表，每行一个。字段名称遵循 RFC4330。
- *IP* - 远程 IP 地址。

**注意**：上述日志规则仅适用于内置的 SNTP 客户端；单独的 NTP 包没有任何日志记录功能。