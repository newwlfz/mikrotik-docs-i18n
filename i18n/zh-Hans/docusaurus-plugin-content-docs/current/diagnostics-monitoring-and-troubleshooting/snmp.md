# SNMP

> 本文档介绍 MikroTik RouterOS 中的 SNMP 配置，涵盖启用服务、常规设置（如联系信息和 Trap 配置）、SNMPv1/2c/3 的社区访问权限，以及监控慢速服务或 OID 时关于超时的警告。

# SNMP

简单网络管理协议（SNMP）是一种互联网标准协议，用于监控和管理 IP 网络上的设备。它可以与 Cacti、MRTG 或 The Dude 等监控工具配合使用，以收集、可视化和绘制系统数据图表。

SNMP 写入访问仅适用于选定的 OID。对于支持的 OID，可以使用 SNMP v1、v2c 或 v3 进行写操作。SNMP 回复通过接收请求的同一接口发送，确保响应使用与原始请求发送到路由器的目的地址相同的源地址。

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/snmp-01.webp)

:::warning
SNMP 服务从系统上运行的各种服务收集数据。如果 SNMP 与其中一个服务之间的通信耗时超过预期，系统可能会记录类似 `timeout while waiting for program` 或 `SNMP did not get OID data within the expected time, ignoring OID` 的警告。每个服务的超时时间为 30 秒，路由服务的超时时间最长可达 5 分钟。发生此类超时后，受影响的服务可能会暂时停止响应 SNMP 数据请求，然后再次尝试检索请求的信息。

这些警告并不表示 SNMP 服务本身存在问题。大多数情况下，它们发生在使用 SNMP 监控缓慢或负载过重的服务时。当监控不适合通过 SNMP 轮询的 OID 时，也可能会出现这些警告。在这种情况下，建议的解决方案是将这些 OID 从监控工具配置中排除。
:::

## 快速配置

在 RouterOS 中启用 SNMP：

```ros
[admin@MikroTik] /snmp> print 
enabled: no
contact: 
location: 
engine-id: 
trap-community: (unknown)
trap-version: 1
[admin@MikroTik] /snmp> set enabled yes
```

您还可以在上述设置中指定管理联系信息。所有 SNMP 数据将对在 *community* 菜单中配置的社区可用。

## 常规属性

**子菜单：** `/snmp`

 此子菜单允许启用 SNMP 并配置常规设置。

| 属性 | 描述 |
| :-- | :-- |
| **contact** (*字符串*; 默认值：**""**) | 联系信息 |
| **enabled** (*是 \| 否*; 默认值：**否**) | 用于禁用/启用 SNMP 服务 |
| **engine-id** (*字符串*; 默认值：**""**) | 对于 SNMP v3，用作标识符的一部分。您可以使用此参数配置 engine id 的后缀部分。如果 SNMP 客户端无法检测设置的 engine-id 值，则必须使用此前缀十六进制 `0x80003a8c04` |
| **location** (*字符串*; 默认值：**""**) | 位置信息 |
| **trap-community** (*字符串*; 默认值：**public**) | 在 *community* 菜单中配置的哪些社区用于发送 Trap。 |
| **trap-generators** (*interfaces \| start-trap*; 默认值：) | 哪些操作将生成 Trap：`interfaces` - 接口更改；`start-trap` - 路由器上 SNMP 服务器启动；`temp-exception` - 当温度达到 100°C（或在 `/system/health` 中为 `cpu-overtemp-threshold` 配置的值）时发送 Trap |
| **trap-interfaces** (*字符串 \| all*; 默认值：) | 将发送 Trap 的接口列表。 |
| **trap-target** (*IP/IPv6 地址列表*; 默认值：**0.0.0.0**) | 必须接收 Trap 的 SNMP 数据收集器的 IP（IPv4 或 IPv6）地址 |
| **trap-version** (*1\|2\|3*; 默认值：**1**) | 用于 Trap 的 SNMP 协议版本 |
| **src-address** (*IPv4 或 IPv6 地址*; 默认值：**::**) | 强制路由器对所有 SNMP 消息始终使用相同的 IP 源地址 |
| **vrf** (*VRF 名称*; 默认值：**main**) | 设置服务监听传入连接的 VRF |

:::note
engine-id 字段保存 engine-id 的后缀值，通常 SNMP 客户端应该能够检测到该值，因为 SNMP 值是从路由器读取的。但是，也有可能无法检测。在这种情况下，engine-ID 值必须根据以下规则设置：\<engine-id 前缀> + \<十六进制转储后缀>，例如，如果您将 `1234` 设置为后缀值，则必须提供 `80003a8c04` + `31323334`，组合后的十六进制（结果）为 `80003a8c0431323334`
:::

## 社区属性

**子菜单：** `/snmp/community`

此子菜单允许设置 SNMP 数据的访问权限。

v1 和 v2c 的安全性很低，只有明文社区字符串（“用户名”）和按 IP 地址限制访问的能力。

在生产环境中，应使用 SNMP v3，因为它提供了安全性 - 使用 MD5/SHA1 进行授权（用户+密码），使用 DES 和 AES 进行加密。

```ros
[admin@MikroTik] /snmp/community> print value-list 
name: public
address: 0.0.0.0/0
security: none
read-access: yes
write-access: no
authentication-protocol: MD5
encryption-protocol: DES
authentication-password: *****
encryption-password: *****
```

:::danger
默认设置只有一个名为 *public* 的社区，没有任何额外的安全设置。这些设置应被视为不安全，应根据所需的安全配置文件进行调整。
:::

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP/IPv6 地址*; 默认值：**0.0.0.0/0**) | 允许连接到 SNMP 服务器的地址 |
| **authentication-password** (*字符串*; 默认值：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于向服务器进行连接认证的密码（SNMPv3）。密码长度必须至少为 8 个字符。 |
| **authentication-protocol** (*MD5 \| SHA1*; 默认值：**MD5**) | 用于认证的协议（SNMPv3） |
| **encryption-password** (*字符串*; 默认值：**""**) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于加密的密码（SNMPv3）。密码长度必须至少为 8 个字符。 |
| **encryption-protocol** (*DES \| AES*; 默认值：**DES**) | 用于加密通信的加密协议（SNMPv3）。AES（参见 rfc3826）自 v6.16 起可用。 |
| **name** (*字符串*; 默认值：) | SNMP 社区的名称。 |
| **read-access** (*是 \| 否*; 默认值：**是**) | 是否为此社区启用读访问权限 |
| **security** (*authorized \| none \| private*; 默认值：**none**) | 安全级别：`none` - 无需加密或认证（noAuthNoPriv）；`authorized` - 无需加密，但需要认证（authNoPriv）；`private` - 需要加密和认证（authPriv） |
| **write-access** (*是 \| 否*; 默认值：**否**) | 是否为此社区启用写访问权限 |

## 管理信息库（MIB）

管理信息库（MIB）是由代理维护的、管理器可以查询的信息数据库。您可以从此处下载最新的 MikroTik RouterOS MIB 文件：[https://mikrotik.com/download/tools](https://mikrotik.com/download/tools)

RouterOS 中使用的 MIB：

- MIKROTIK-MIB
- MIB-2
- HOST-RESOURCES-MIB
- IF-MIB
- IP-MIB
- IP-FORWARD-MIB
- IPV6-MIB
- BRIDGE-MIB
- DHCP-SERVER-MIB
- CISCO-AAA-SESSION-MIB
- ENTITY-MIB
- UPS-MIB
- SQUID-MIB

## 对象标识符（OID）

每个 OID 标识一个可以通过 SNMP 读取的变量。虽然 MIB 文件包含所有需要的 OID 值，您也可以在控制台的任何菜单级别使用 **print oid** 命令打印单个 OID 信息：

```ros
[admin@MikroTik] /interface> print oid

Flags: D - dynamic, X - disabled, R - running, S - slave 
0 R name=.1.3.6.1.2.1.2.2.1.2.1 mtu=.1.3.6.1.2.1.2.2.1.4.1 
mac-address=.1.3.6.1.2.1.2.2.1.6.1 admin-status=.1.3.6.1.2.1.2.2.1.7.1 
oper-status=.1.3.6.1.2.1.2.2.1.8.1 bytes-in=.1.3.6.1.2.1.2.2.1.10.1 
packets-in=.1.3.6.1.2.1.2.2.1.11.1 discards-in=.1.3.6.1.2.1.2.2.1.13.1 
errors-in=.1.3.6.1.2.1.2.2.1.14.1 bytes-out=.1.3.6.1.2.1.2.2.1.16.1 
packets-out=.1.3.6.1.2.1.2.2.1.17.1 discards-out=.1.3.6.1.2.1.2.2.1.19.1 
errors-out=.1.3.6.1.2.1.2.2.1.20.1 
```

## Traps

SNMP Trap 使路由器能够通过发送 Trap 通知数据收集器有关接口更改和 SNMP 服务状态更改的信息。可以发送带有安全功能的 Trap，以支持 SNMPv1（无安全性）、SNMPv2 变体以及带有加密和授权的 SNMPv3。

对于 SNMPv2 和 v3，您必须将适当配置的社区设置为 *trap-community*，以启用所需的功能（密码或加密/授权）。

## SNMP 写入

SNMP 写入允许通过 SNMP 请求更改路由器配置。当启用 SNMP 和写访问权限时，请考虑保护对路由器或路由器 SNMP 的访问安全。

要通过 SNMP 请求更改设置，请使用以下命令允许所选社区的 SNMP 写入。

```ros
/snmp/community/set <number> write-access=yes
```

### 系统标识

可以通过 SNMP set 命令更改路由器系统标识。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.2.1.1.5.0 s New_Identity
```

- *snmpset* - 用于向网络实体发送 SNMP SET 请求以设置信息的 SNMP 应用程序；
- *public* - 路由器的社区名称；
- *192.168.88.1* - 路由器的 IP 地址；
- *1.3.6.1.2.1.1.5.0* - 路由器标识的 SNMP 值；

上述 SNMPset 命令等同于 RouterOS 命令：

```ros
/system/identity/set identity=New_Identity
```

### 重启

可以通过 SNMP set 命令重启路由器。您需要为重启 SNMP 设置设置一个非零值。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.4.1.14988.1.1.7.1.0 s 1
```

- **1.3.6.1.4.1.14988.1.1.7.1.0**，用于路由器重启的 SNMP 值。
- **s 1**，snmpset 命令用于设置值，该值不应等于 0。

重启 SNMPset 命令等同于 RouterOS 命令：

```ros
/system/reboot
```

### 运行脚本

SNMP 写入允许在需要为脚本的 SNMP 设置设置值时，从 **system script** 菜单在路由器上运行脚本。

```bash
snmpset -c public -v 1 192.168.88.1 1.3.6.1.4.1.14988.1.1.8.1.1.3.X s 1
```

- **X**，脚本编号，编号从 1 开始。
- **s 1**，snmpset 命令用于设置值，该值不应等于 0。

在 RouterOS 上的相同命令：

```ros
/system/script> print 
Flags: I - invalid 
0 name="test" owner="admin" policy=ftp,reboot,read,write,policy,
test,winbox,password,sniff last-started=1970-01-01
01:31:57 run-count=23 source=:beep 

/system/script/run 0
```

:::danger
SNMP 仅限于 *ftp,reboot,**read,write,test,romon* 脚本策略。如果脚本的策略大于 *ftp,reboot,**read,write,test,romon* - 则脚本将不会被执行。确保您的脚本不超过上述策略。
:::

### 使用 GET 运行脚本

可以通过 SNMP GET 请求脚本 OID 来运行 `/system/scripts`（自 6.37 起）。为此，需要一个具有写权限的 SNMP 社区。由于表是动态的，可以通过 SNMPWALK 命令检索脚本的 OID。

#### 添加脚本

```ros
/system/script
add name=script1 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="/sy reboot "
add name=script2 owner=admin policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon source="[:put output]"
```

#### 获取脚本 OID 表

```bash
$ snmpwalk -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.8
iso.3.6.1.4.1.14988.1.1.8.1.1.2.1 = STRING: "script1"
iso.3.6.1.4.1.14988.1.1.8.1.1.2.2 = STRING: "script2"
iso.3.6.1.4.1.14988.1.1.8.1.1.3.1 = INTEGER: 0
iso.3.6.1.4.1.14988.1.1.8.1.1.3.2 = INTEGER: 0
```

#### 使用表 18 运行脚本

```bash
$ snmpget -v2c -cpublic 192.168.88.1 1.3.6.1.4.1.14988.1.1.18.1.1.2.2
iso.3.6	.1.4.1.14988.1.1.18.1.1.2.2 = STRING: "output"
```

:::danger
SNMP 仅限于 *ftp,reboot,**read,write,test,romon* 脚本策略。如果脚本的策略大于 *ftp,reboot,**read,write,test,romon* - 则脚本将不会被执行。确保您的脚本不超过上述策略。
:::