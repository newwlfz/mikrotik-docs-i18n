# Dot1X

> 本文档介绍 MikroTik RouterOS 的 Dot1X 实现，涵盖基于 IEEE 802.1X 端口网络访问控制的客户端与服务器配置，支持 EAP-TLS、EAP-TTLS 和 PEAP 等 EAP 方法。

# Dot1X

Dot1X 是 RouterOS 中 IEEE 802.1X 标准的实现。其主要目的是通过 EAP over LAN（也称为 EAPOL）提供基于端口的网络访问控制。802.1X 由请求方（客户端）、认证方（服务器）和认证服务器（RADIUS 服务器）组成。RouterOS 同时支持认证方和请求方，当安装了 [User Manager](./user-manager.md) 软件包时，也支持认证服务器。请求方支持的 EAP 方法包括 EAP-TLS、EAP-TTLS、EAP-MSCHAPv2 和 PEAPv0/EAP-MSCHAPv2。

:::warning
该功能在 SMIPS 设备（hAP lite、hAP lite TC 和 hAP mini）上不受支持。

:::

## 客户端

请求方配置设置。

**子菜单：** `/interface/dot1x/client`

| 属性 | 说明 |
| :-- | :-- |
| **anon-identity** (*字符串*；默认值：) | 外层 EAP 认证的身份标识。仅用于 `eap-ttls` 和 `eap-peap` 方法。如果未设置，则使用 `identity` 参数的值进行外层 EAP 认证。 |
| **client-certificate** (*字符串*；默认值：) | [System/Certificates](./certificates.md) 中列出的证书名称。使用 `eap-tls` 方法时必需。 |
| **comment** (*字符串*；默认值：) | 条目的简短描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 客户端是否启用。 |
| **eap-methods** (*eap-tls \| eap-ttls \| eap-peap \| eap-mschapv2*；默认值：) | 用于认证的 EAP 方法的有序列表。 |
| **identity** (*字符串*；默认值：) | 用于 EAP 认证的请求方身份标识。 |
| **interface** (*字符串*；默认值：) | 客户端运行的接口名称。 |
| **password** (*字符串*；默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 请求方的明文密码。 |

### 只读属性

| 属性 | 说明 |
| :-- | :-- |
| **status** (*authenticated \| authenticating \| disabled*) | 可能的状态：authenticated - 客户端已成功认证。authenticating - 已连接到服务器，认证过程正在进行中。disabled - 客户端已禁用。error - 发生内部错误。interface is down - 父接口未运行。rejected - 服务器拒绝了认证。 |

## 服务器

---

RouterOS dot1x 服务器充当认证方。启用 dot1x 服务器的接口将阻止除用于认证的 EAPOL 数据包之外的所有流量。客户端成功认证后，该接口将接受端口上接收的所有流量。如果接口连接到共享介质且存在多个主机，则当至少一个客户端成功认证后，将接受来自所有主机的流量。但是，可以[配置动态交换规则](./dot1x.md#dynamic-switch-rule-configuration)以仅接受已认证用户的源 MAC 地址并丢弃所有其他源 MAC 地址。如果认证失败，可以通过专用的端口 VLAN ID 来接受流量。

:::warning
在桥接端口上创建 dot1x 服务器时，桥接应运行 (R/M)STP，否则无法正确接受来自客户端的 EAP 数据包。桥接接口默认以 `protocol-mode=rstp` 创建。如果桥接端口不应发送任何 BPDU 或应忽略任何接收到的 BPDU，请在桥接端口上使用 `edge=yes` 配置。

:::

**子菜单：** `/interface/dot1x/server`

| 属性 | 说明 |
| :-- | :-- |
| **accounting** (*yes \| no*；默认值：**yes**) | 是否向认证服务器发送 RADIUS 计费请求。 |
| **auth-timeout** (*时间*；默认值：**1m**) | EAP 认证可用的总时间。 |
| **auth-types** (*dot1x \| mac-auth*；默认值：**dot1x**) | 服务器接口上使用的认证类型。当同时选择两个选项时，服务器将优先使用 `dot1x` 认证类型，仅在 3 个 `retrans-timeout` 周期后，认证类型才会回退到 `mac-auth`。为使 `mac-auth` 认证类型生效，服务器接口应至少收到一个包含客户端设备源 MAC 地址的帧。 |
| **comment** (*字符串*；默认值：) | 条目的简短描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 服务器配置是否启用。 |
| **guest-vlan-id** (*整数：1..4094*；默认值：**!guest-vlan-id**) | 当终端设备不支持 `dot1x` 认证且未配置 `mac-auth` 回退时分配的 VLAN。该设置将在 3 个 `retrans-timeout` 周期后生效。一旦创建了启用 dot1x 的客户端并成功完成重新认证，端口将从 guest VLAN 中移除。此设置自 RouterOS 7.2 版本起可用，并在桥接 `vlan-filtering` 启用时生效。默认情况下，guest VLAN 处于禁用状态。 |
| **interface** (*字符串*；默认值：) | 服务器运行的接口或接口列表名称。 |
| **interim-update** (*时间*；默认值：**0s**) | 计划 RADIUS Interim-Update 消息之间的间隔。 |
| **mac-auth-mode** (*mac-as-username \| mac-as-username-and-password*；默认值：**mac-as-username**) | 允许在使用 MAC 认证时控制 User-Name 和 User-Password RADIUS 属性。 |
| **radius-mac-format** (*XX-XX-XX-XX-XX-XX \| XX:XX:XX:XX:XX:XX \| XXXXXXXXXXXX \| xx-xx-xx-xx-xx-xx \| xx:xx:xx:xx:xx:xx \| xxxxxxxxxxxx*；默认值：**XX:XX:XX:XX:XX:XX**) | 控制使用 MAC 认证时客户端 MAC 地址在 User-Name 和 User-Password 属性中的编码方式。 |
| **reauth-period**(*时间*；默认值：**!reauth-period**) | 启用服务器端口重新认证。当使用 `dot1x` 认证类型启用时，服务器将尝试通过向客户端发送 EAP-Request Identity 来重新认证客户端。当使用 `mac-auth` 认证类型启用时，服务器将尝试使用最后看到的 MAC 地址向 RADIUS 服务器重新认证客户端。此设置自 RouterOS 7.2 版本起可用。默认情况下，重新认证处于禁用状态。 |
| **reject-vlan-id** (*整数：1..4094*；默认值：**!reject-vlan-id**) | 当认证失败且 RADIUS 服务器响应 Access-Reject 消息时分配的 VLAN。如果 RADIUS 服务器完全没有响应，则此属性不适用，客户端认证将直接超时，服务将不可用。此属性仅在桥接 `vlan-filtering` 启用时生效。默认情况下，reject VLAN 处于禁用状态。 |
| **retrans-timeout** (*时间*；默认值：**30s**) | 如果未收到请求方的响应，消息重传之间的时间间隔。 |
| **server-fail-vlan-id** (*整数：1..4094*；默认值：**!server-fail-vlan-id**) | 当 RADIUS 服务器无响应且请求超时后分配的 VLAN。此设置自 RouterOS 7.2 版本起可用，并在桥接 `vlan-filtering` 启用时生效。默认情况下，server-fail VLAN 处于禁用状态。 |

当前已认证的客户端列在活动菜单中（只读属性）。

**子菜单：** `/interface/dot1x/server/active`

| 属性 | 说明 |
| :-- | :-- |
| **auth-info** (*字符串*) | 认证信息：dot1xdot1x (guest vlan)dot1x (reject vlan)dot1x (server fail vlan)mac-authmac-auth (reject vlan)mac-auth (server fail vlan) |
| **client-mac** (*MAC 地址*) | 请求方的 MAC 地址。 |
| **interface** (*字符串*) | 接口名称。 |
| **session-id** (*字符串*) | 唯一会话标识符。 |
| **username** (*字符串*) | 请求方的身份标识。 |
| **vlan-id** (*字符串*) | 分配给接口的未标记 VLAN ID。必须在桥上启用 VLAN ID 过滤。 |

所有活动 dot1x 服务器接口的状态列在状态菜单中（只读属性）。

**子菜单：** `/interface/dot1x/server/state`

| 属性 | 说明 |
| :-- | :-- |
| **interface** (*字符串*) | 接口名称。 |
| **status** (*字符串*) | 可能的接口状态：authorized - 已授予接口访问权限；iface-down - 接口未运行；rejected-holding - 访问被 RADIUS 服务器拒绝；un-authorized - 未授予接口访问权限。 |

## 示例

下面描述了 dot1x 服务器和客户端最常见的配置示例。

### RouterOS 认证方配置

![](https://manual.mikrotik.com/docs/authentication-authorization-accounting/img/dot1x-01.webp)

首先添加一个新的 RADIUS 客户端。认证服务器（RADIUS）不必与认证方位于同一 LAN 中，但必须可从认证方访问，因此必须考虑任何防火墙限制。

```ros
/radius 
add address=10.1.2.3 secret=radiussecret service=dot1x
```

:::warning
如果 RADIUS 通信通过公共网络进行，建议使用 RadSec 进行 RADIUS 通信。更多信息：[RADIUS](./radius.md)

:::

添加新的 dot1x 服务器实例。

```ros
/interface/dot1x/server
add interface=ether2 interim-update=30s comment=accounted
add interface=ether12 accounting=no comment=notaccounted
```

#### 基于端口的 VLAN ID 分配

可以使用桥接 VLAN 过滤将已认证的接口分配到特定的 VLAN ID。这可以通过 RADIUS Tunnel-Type、Tunnel-Medium-Type 和 Tunnel-Private-Group-ID 属性完成。请注意，只有具有硬件卸载 VLAN 过滤的设备才能在交换芯片中执行此操作。

首先，确保接口已添加到启用了 VLAN 过滤的桥接中。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether12
```

需要为通过 ether1 接口发送的标记 VLAN 流量添加静态 VLAN 配置。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=2
add bridge=bridge1 tagged=ether1 vlan-ids=12
```

启用 RADIUS 调试日志后，可以查看包含所有属性的完整 RADIUS 消息数据包。在我们的示例中，Tunnel 属性在来自 RADIUS 服务器的 Access-Accept 消息中收到：

```text
09:51:45 radius,debug,packet received Access-Accept with id 64 from 10.1.2.3:1812
09:51:45 radius,debug,packet     Tunnel-Type = 13 
09:51:45 radius,debug,packet     Tunnel-Medium-Type = 6 
09:51:45 radius,debug,packet     Tunnel-Private-Group-ID = "12" 
(..)
09:51:45 radius,debug,packet     User-Name = "dot1x-user" 
```

VLAN ID 现在出现在活动会话列表中，未标记端口已添加到之前创建的静态 VLAN 配置中。

```ros
/interface/dot1x/server/active/print 
  0 interface=ether12 username="dot1x-user" client-mac=00:0C:42:EB:71:F6 session-id="86b00006" vlan-id=12
```

```ros
/interface/bridge/vlan/print detail 
Flags: X - disabled, D - dynamic 
 0 D bridge=bridge1 vlan-ids=1 tagged="" untagged="" current-tagged="" current-untagged=bridge1,ether3 

 1   bridge=bridge1 vlan-ids=2 tagged=ether1 untagged="" current-tagged=ether1 current-untagged=ether2 

 2   bridge=bridge1 vlan-ids=12 tagged=ether1 untagged="" current-tagged=ether1 current-untagged=ether12 
```

#### 动态交换规则配置

在某些网络配置中，需要为特定请求方添加额外的访问规则，以限制或允许某些网络服务。这可以通过 Mikrotik-Switching-Filter 属性完成，请参阅 [RADIUS 供应商字典](./radius.md)。当客户端被认证服务器成功认证后，服务器可以传回 Mikrotik-Switching-Filter 属性。基于接收到的信息，认证方将在客户端所在的交换端口上创建动态访问规则。只要客户端会话处于活动状态且接口正在运行，这些规则就会生效。关于正确的交换规则实现，存在一定的顺序和限制：

- 支持 `mac-protocol`、`src-mac-address`（仅自 RouterOS 7.2 版本起可用）、`src-address`（IPv4/掩码，仅自 RouterOS 7.2 版本起可用）、`dst-address`（IPv4/掩码）、`protocol`（IPv4）`src-port`（L4，仅自 RouterOS 7.2 版本起可用）、`dst-port`（L4）条件参数。
- `mac-protocol` 和 `protocol` 参数可以使用十六进制或十进制表示（例如 `protocol 17` 或 `protocol 0x11`）。
- `src-port` 和 `dst-port` 支持单个值或范围值（例如 `src-port 10` 或 `src-port 10-20`）。
- `src-mac-address` 支持 "xx:xx:xx:xx:xx:xx" 或 "xxxxxxxxxxxx" 格式，可以使用 "none" 关键字设置不带任何源 MAC 地址的交换规则（例如 `src-mac-address none`）。
- `src-mac-address`（如果属性未设置）、`switch` 和 `ports` 条件参数会自动为每条规则设置。
- 每条规则应以动作属性结尾，支持的值是 **drop** 或 **allow**。如果未设置动作属性，将使用默认的 **allow** 值。
- 单个请求方支持多条规则，必须用逗号 "," 分隔。

以下是 Mikrotik-Switching-Filter 属性及其创建的动态交换规则的一些示例：

```ros
# 丢弃 ARP 帧（EtherType：0x0806 或 2054）
Mikrotik-Switching-Filter = "mac-protocol 2054 action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=arp copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# 允许 UDP（IP 协议：0x11 或 17）目标端口 100 并丢弃所有其他数据包
Mikrotik-Switching-Filter = "protocol 17 dst-port 100 action allow, action drop"

/interface/ethernet/switch/rule/print
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF protocol=udp dst-port=100 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports=""

# 仅允许已认证的源 MAC 地址，丢弃所有其他数据包
Mikrotik-Switching-Filter = "action allow, src-mac-address none action drop"

/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 src-mac-address=CC:2D:E0:01:6D:EB/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether1 copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

在我们的示例中，ether2 上的 Supplicant2 仅被允许使用 UDP 目标端口 50 访问 192.168.50.0/24 网络；所有其他流量应被丢弃。首先，确保桥接端口上的硬件卸载正常工作，否则交换规则可能无法正常工作。

```ros
/interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                   BRIDGE                   HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                      bridge1                  yes    1     0x80         10                 10       none
 1   H ether2                      bridge1                  yes    1     0x80         10                 10       none
 2   H ether12                     bridge1                  yes    1     0x80         10                 10       none
```

启用 RADIUS 调试日志后，可以查看包含所有属性的完整 RADIUS 消息数据包。在我们的示例中，Mikrotik-Switching-Filter 属性在来自 RADIUS 服务器的 Access-Accept 消息中收到：

```text
02:35:38 radius,debug,packet received Access-Accept with id 121 from 10.1.2.3:1812 
(..)
02:35:38 radius,debug,packet     MT-Switching-Filter = "mac-protocol 2048 dst-address 192.168.50.0/24 dst-port 50 protocol 17 action allow,action drop"
```

动态交换规则现在出现在交换菜单下：

```ros
/interface/ethernet/switch/rule/print 
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF mac-protocol=ip dst-address=192.168.50.0/24 protocol=udp dst-port=50 copy-to-cpu=no redirect-to-cpu=no mirror=no 

 1  D ;;; dot1x dynamic
      switch=switch1 ports=ether2 src-mac-address=CC:2D:E0:11:22:33/FF:FF:FF:FF:FF:FF copy-to-cpu=no redirect-to-cpu=no mirror=no new-dst-ports="" 
```

:::warning
动态交换规则仅适用于支持交换规则的 RouterBoard - 具有 Marvell Prestera 交换机的 MikroTik 设备以及具有 QCA8337、Atheros8327 和 Atheros8316 交换芯片的设备。CRS1xx/2xx 系列交换机不支持此功能。请考虑每个设备的最大规则数，请参阅 [具有 Marvell Prestera 交换机的 MikroTik 设备](../bridging-and-switching/marvell-prestera-switch-chip-features.md#models) 和 [基本交换芯片表](../bridging-and-switching/switch-chip-features.md)

:::

### RouterOS 请求方配置

`eap-tls、eap-ttls` 和 `eap-peap` 认证方法需要 CA 证书。此外，`eap-tls` 方法需要客户端证书。在此示例中，我们已经导入了包含自签名客户端和 CA 证书的 P12 证书包。有关如何在 RouterOS 中导入证书的更多信息，请访问 [System/Certificates](./certificates.md)。

```ros
/certificate/print 
Flags: K - private-key, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #         NAME                                            COMMON-NAME                                         SUBJECT-ALT-NAME                             FINGERPRINT                                        
 0 K  A  T dot1x-client                                    ez_dot1x-client                                     IP:10.1.2.34
 1  L A  T dot1x CA                                        ca            
```

只需添加一个新的 dot1x 客户端实例，它将启动认证过程。

```ros
/interface/dot1x/client
add anon-identity=anonymous client-certificate=dot1x-client eap-methods=eap-tls identity=dot1x-user interface=ether1 password=dot1xtest
```

如果认证成功，接口的状态应为 authenticated。

```ros
/interface/dot1x/client/print 
Flags: I - inactive, X - disabled 
  0   interface=ether1 eap-methods=eap-tls identity="dot1x-user" password="dot1xtest" anon-identity="anonymous" client-certificate=dot1x-client status="authenticated"
```