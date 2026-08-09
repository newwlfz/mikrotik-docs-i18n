# DHCP

> MikroTik RouterOS 文档页面描述了 DHCP 客户端功能，解释了如何通过 DHCP 配置和管理 IP 地址分配。它涵盖了客户端属性，如默认路由处理、DNS/NTP 集成和 VLAN 优先级设置，以及只读状态指示器，如分配的 IP 地址和 DHCP 服务器详细信息。

# DHCP

## DHCP 客户端

### 概述

**子菜单：** `/ip/dhcp-client`

DHCP（动态主机配置协议）用于在网络中轻松分配 IP 地址。MikroTik RouterOS 的实现包括服务器和客户端部分，并符合 RFC 2131 标准。

MikroTik RouterOS DHCP 客户端一次只能在一个类似以太网的接口上启用。客户端将接受一个地址、子网掩码、默认网关和两个 DNS 服务器地址。接收到的 IP 地址将连同相应的子网掩码添加到接口上。默认网关将作为动态条目添加到路由表中。如果 DHCP 客户端被禁用或未续租地址，动态默认路由将被移除。如果在 DHCP 客户端获取默认路由之前已存在默认路由，则 DHCP 客户端获取的路由将显示为无效。

RouterOS DHCP 客户端请求以下选项：

- 选项 1 - 子网掩码。
- 选项 3 - 网关地址。
- 选项 6 - DNS 服务器地址。
- 选项 15 - 域名。
- 选项 33 - 静态路由。
- 选项 42 - NTP 服务器地址。
- 选项 43 - 厂商特定信息。
- 选项 121 - 无类静态路由。
- 选项 138 - CAPWAP 接入控制器地址。

### DHCP 选项

DHCP 客户端可以设置发送到 DHCP 服务器的选项，例如主机名和 MAC 地址。语法与 DHCP 服务器选项相同。

目前，选项中可以使用三个变量：

- HOSTNAME。
- CLIENT\_MAC - 客户端接口 MAC 地址。
- CLIENT\_DUID - 路由器的客户端 DUID，与 DHCPv6 客户端使用的相同。符合 RFC4361 标准。

DHCP 客户端默认选项包括以下默认选项：

| 名称 | 代码 | 值 |
| :-- | --: | :-- |
| clientid\_duid | 61 | 0xff$(CLIENT\_DUID) |
| clientid | 61 | 0x01$(CLIENT\_MAC) |
| hostname | 12 | $(HOSTNAME) |

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no \| special-classless*; 默认值：**yes**) | 是否将从 DHCP 服务器接收到的默认路由安装到路由表中。默认情况下，RouterOS 客户端符合 RFC 标准，如果收到无类选项 121，则忽略选项 3。要强制客户端不忽略选项 3，请设置 *special-classless*。此参数在 v6rc12+ 中可用。yes - 如果收到无类路由则添加，否则添加默认路由（旧行为）。special-classless - 如果收到无类路由和默认路由则同时添加（微软风格）。 |
| **allow-reconfigure** (*yes \| no*; 默认值：**no**) | 允许接收来自 DHCP 服务器的 Reconfigure (forcerenew) 消息。对于现有的 dhcp-client 更改，请续租。 |
| **check-gateway** *(none \| arp \| bfd \| ping***;** 默认值：**none)** | 检查路由[网关可达性](../user-guides/routing-and-networking-protocols/routing-decision.md)的方法。 |
| **client-id** (*string*; 默认值：) | 对应网络管理员或 ISP 建议的设置。如果未指定，将发送客户端的 MAC 地址。 |
| **comment** (*string*; 默认值：) | 客户端的简短描述。 |
| **default-route-tables** (*table:distance*; 默认值：*default*) | 必须添加默认路由的路由表列表。表名可以以 ":x" 为前缀，其中 x 是安装路由时使用的距离。 |
| **default-route-distance** (*integer:0..255*; 默认值：) | 默认路由距离。 |
| **disabled** (*yes \| no*; 默认值：**yes**) | 客户端是否被禁用。 |
| **dscp** (*integer:0..63*; 默认值：**0**) | 为出站 DHCP 客户端数据包设置 DSCP（差异化服务代码点）值。此值是 IP 头的一部分，用于指示网络流量所需的 QoS（服务质量）级别。 |
| **host-name** (*string*; 默认值：) | 发送到 DHCP 服务器的客户端主机名。如果未指定，将使用客户端的系统标识。 |
| **interface** (*string*; 默认值：) | DHCP 客户端将运行的接口。 |
| **name** (*string*; 默认值：) | DHCP 客户端的名称，如果未指定，则由 RouterOS 生成。 |
| **script** (*script*; 默认值：) | 当 DHCP 客户端获得新租约或失去现有租约、接收到的网关地址或 DNS 服务器列表更改时执行脚本。事件脚本可访问的变量：bound - 1 - 租约已添加/更改；0 - 租约已移除。server-address - 服务器地址。lease-address - 服务器提供的租约地址。interface - 客户端配置所在的接口名称。gateway-address - 服务器提供的网关地址。vendor-specific - 存储从 DHCP 服务器接收的选项 43 的值。lease-options - 从服务器接收的选项数组。[`示例 >>`](#example) |
| **use-broadcast** (*always* \| *both* \| *never*; 默认值：**both**) | 是否在 DHCPDISCOVER 和 DHCPREQUEST 消息中设置 *broadcast* 位。 *always - broadcast* 位始终设置。 *both - broadcast* 位仅在前 15 秒设置。 *never - broadcast* 位不设置。 |
| **use-peer-dns** (*yes \| no*; 默认值：**yes**) | 是否接受 [DHCP 服务器](./dhcp.md#dhcp-server) 通告的 [DNS](./dns.md) 设置。（将覆盖 `/ip/dns` 子菜单中的设置。） |
| **use-peer-ntp** (*yes \| no*; 默认值：**yes**) | 是否接受 [DHCP 服务器](./dhcp.md#dhcp-server) 通告的 [NTP](../system-information-and-utilities/ntp.md) 设置。（将覆盖 `/system/ntp/client` 子菜单中的设置。） |
| **vlan-priority** (*integer:0..7*; 默认值：**0**) | 如果 DHCP 客户端在 [VLAN 接口](../bridging-and-switching/vlan.md) (/interface/vlan) 上运行，您可以指定 PCP（优先级代码点）值。PCP 是 VLAN 头中的 3 位字段，用于标记 VLAN 内数据包的优先级，从而允许相应地优先处理流量。此设置仅适用于 VLAN 接口，并影响出站 DHCP 客户端数据包的优先级。 |

#### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP/Netmask*) | 从服务器分配给 DHCP 客户端的 IP 地址和子网掩码。 |
| **dhcp-server** (*IP*) | DHCP 服务器的 IP 地址。 |
| **expires-after** (*time*) | 租约到期的时间（由 DHCP 服务器指定）。 |
| **gateway** (*IP*) | 由 DHCP 服务器分配的网关 IP 地址。 |
| **invalid** (*yes \| no*) | 显示配置是否无效。 |
| **netmask** (*IP*) |  |
| **primary-dns** (*IP*) | 由 DHCP 服务器分配的第一个 DNS 解析器的 IP 地址。 |
| **primary-ntp** (*IP*) | 由 DHCP 服务器分配的主 NTP 服务器的 IP 地址。 |
| **secondary-dns** (*IP*) | 由 DHCP 服务器分配的第二个 DNS 解析器的 IP 地址。 |
| **secondary-ntp** (*IP*) | 由 DHCP 服务器分配的辅助 NTP 服务器的 IP 地址。 |
| **status** (*bound \| error \| rebinding... \| requesting... \| searching... \| stopped*) | 显示 DHCP 客户端的状态。 |
| **reconfigure-key**(string) | 重新配置认证密钥。 |
| **reconfigure-last-counter** *(integer)* | 接收到的 Reconfigure (*forcerenew*) 消息计数。 |
| **custom-source-mac-address** *(MAC)* | DHCP 客户端使用的自定义源 MAC 地址。 |
| **custom-hostname-suffix** *(string)* | 附加到发送到 DHCP 服务器的主机名的后缀。 |
| **caps-managers** *(string)* | 通过 DHCP 选项 138 发现的 CAPsMAN 控制器地址列表。 |

#### 菜单特定命令

| 属性 | 描述 |
| :-- | :-- |
| **release** (*numbers*) | 释放当前绑定并重启 DHCP 客户端。 |
| **renew** (*numbers*) | 续租当前租约。如果续租操作不成功，客户端会尝试重新初始化租约（即，它像尚未收到 IP 地址一样启动租约请求过程 (rebind)）。 |

### 配置示例

#### 简单 DHCP 客户端

在 ether1 接口上添加 DHCP 客户端：

```ros
/ip/dhcp-client/add interface=ether1 disabled=no
```

添加接口后，您可以使用 "print" 或 "print detail" 命令查看 DHCP 客户端获取的参数：

```ros
[admin@MikroTik] /ip/dhcp-client> print detail
Flags: X - disabled, I - invalid 
 0   interface=ether1 add-default-route=yes use-peer-dns=yes use-peer-ntp=yes
     status=bound address=192.168.0.65/24 gateway=192.168.0.1
     dhcp-server=192.168.0.1 primary-dns=192.168.0.1 primary-ntp=192.168.0.1
     expires-after=9m44s 
[admin@MikroTik] /ip/dhcp-client>
```

:::warning
如果 DHCP 客户端使用的接口是 VRF 配置的一部分，则默认路由和从 DHCP 服务器接收的其他路由将添加到 VRF 路由表中。

:::

可以使用以下命令检查 DHCP 客户端状态：

```ros
/ip/dhcp-client/print detail 
```

#### 租约脚本示例

可以在 DHCP 客户端获得新租约或失去现有租约时执行脚本。这是一个示例脚本，它自动添加一条 routing-table=WAN1 的默认路由，并在租约到期或被移除时删除它。

:::warning
请注意，某些变量可能在特定菜单中被保留，无法在那里使用。更多信息请参见[此处](../developer-guides/scripting/index.md#reserved-variable-names)。

:::

```ros
/ip/dhcp-client
add add-default-route=no dhcp-options=hostname,clientid disabled=no interface=ether2 script="{\r\
    \n    :local rmark \"WAN1\"\r\
    \n    :local count [/ip/route/print count-only where comment=\"WAN1\"]\r\
    \n    :if (\$bound=1) do={\r\
    \n        :if (\$count = 0) do={\r\
    \n            /ip/route/add gateway=\$\"gateway-address\" comment=\"WAN1\" routing-table=\$rmark\r\
    \n        } else={\r\
    \n            :if (\$count = 1) do={\r\
    \n                :local test [/ip/route/find where comment=\"WAN1\"]\r\
    \n                :if ([/ip/route/get \$test gateway] != \$\"gateway-address\") do={\r\
    \n                    /ip/route/set \$test gateway=\$\"gateway-address\"\r\
    \n                }\r\
    \n            } else={\r\
    \n                :error \"Multiple routes found\"\r\
    \n            }\r\
    \n        }\r\
    \n    } else={\r\
    \n        /ip/route/remove [find comment=\"WAN1\"]\r\
    \n    }\r\
    \n}\r\
    \n"
```

#### 使用接收到的选项 43 设置 ACS URL

当 DHCP 客户端租约绑定时，如果 DHCP 服务器发送的选项配置为发送它，则可以在 TR069 客户端设置中设置 *自动配置服务器 (ACS)* URL。以下是一个示例：

```ros
:if ($bound=1) do={
/tr069-client/set acs-url=$"vendor-specific"
}
```

#### 当 'router' (选项3) 来自不同子网时解析默认网关

在某些情况下，管理员倾向于设置无法通过提供的 IP 子网解析的 'router' 选项。例如，DHCP 服务器向客户端提供 192.168.88.100/24，而选项 3 设置为 172.16.1.1。这将导致无法解析的默认路由：

```ros
 #      DST-ADDRESS        PREF-SRC        GATEWAY            DISTANCE
 0  DS  0.0.0.0/0                          172.16.1.1              1
 1 ADC  192.168.88.0/24    192.168.88.100  ether1 
```

要解决此问题，我们需要添加一条 /32 路由以通过 ether1 解析网关，这可以通过每次 DHCP 客户端获取地址时运行以下脚本来完成：

```ros
/system/script/add name="dhcpL" source={ /ip/address/add address=($"lease-address" . "/32") network=$"gateway-address" interface=$interface }
```

现在我们可以进一步扩展脚本，检查地址是否已存在，并在需要更改时删除旧地址：

```ros
/system/script/add name="dhcpL" source={ 
  /ip/address {
    :local ipId [find where comment="dhcpL address"]
    :if ($ipId != "") do={
      :if (!([get $ipId address] = ($"lease-address" . "/32") && [get $ipId network]=$"gateway-address" )) do={
        remove $ipId;
        add address=($"lease-address" . "/32") network=$"gateway-address" \
          interface=$interface comment="dhcpL address"
      }
    } else={
      add address=($"lease-address" . "/32") network=$"gateway-address" \
        interface=$interface comment="dhcpL address"
    }
  }
}
```

## DHCPv6 客户端

### 概述

**子菜单：** `/ipv6/dhcp-client`

RouterOS 中的 DHCP 客户端能够充当 DHCPv6 客户端和 DHCP-PD 客户端。因此，它既可以从 DHCP-PD 服务器获取前缀，也可以从 DHCPv6 服务器获取 DHCPv6 有状态地址。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **add-default-route** (*yes \| no*; 默认值：**no**) | 客户端连接后是否添加默认 IPv6 路由。 |
| **allow-reconfigure** (*yes \| no*; 默认值：**no**) | 允许接收来自 DHCP 服务器的 Reconfigure (forcerenew) 消息。 |
| **default-route-tables** (*table:distance*; 默认值：main) | 必须添加默认路由的路由表列表。表名可以以 ":x" 为前缀，其中 x 是安装路由时使用的距离。 |
| **comment** (*string*; 默认值：) | 客户端的简短描述。 |
| **disabled** (*yes \| no*; 默认值：**no**) |  |
| **interface** (*string*; 默认值：) | DHCPv6 客户端将运行的接口。 |
| **pool-name** (*string*; 默认值：) | 接收到的 IPv6 前缀将添加到的 [IPv6 池](../cli-reference/ipv6/pool.md) 的名称。 |
| **pool-prefix-length** (*integer*; 默认值：) | 将为接收到的 IPv6 前缀添加到的 [IPv6 池](../cli-reference/ipv6/pool.md) 设置的前缀长度参数。前缀长度必须大于或等于接收到的前缀长度。如果未设置，则前缀将按照从服务器接收到的长度添加。 |
| **prefix-address-lists**(*string*; 默认值：) | 接收到的前缀将添加到的防火墙地址列表的名称。 |
| **prefix-hint** (*string*; 默认值：) | 包含首选前缀长度。 |
| **request** (*prefix, address*; 默认值：) | 选择 DHCPv6 请求是请求地址、IPv6 前缀还是两者都请求。 |
| **script** (*string*; 默认值：) | 在 DHCP 客户端状态更改时运行此脚本。可用变量：pd-valid - 客户端是否获取了前缀；pd-prefix - 客户端获取的前缀（如果有）；na-valid - 客户端是否获取了地址；na-address - 客户端获取的地址（如果有）。options - 接收到的选项数组（仅 ROSv7）。 |
| **use-peer-dns** (*yes \| no*; 默认值：**yes**) | 是否接受 IPv6 DHCP 服务器通告的 DNS 设置。 |
| **custom-duid** (*hex string*; 默认值：) | 允许指定自定义 DUID。 |
| **use-interface-duid**(*yes \| no*; 默认值：**no**) | 根据 RFC，DHCPv6 客户端基于路由器的第一个接口 MAC 地址生成 DUID，而不是客户端配置所在的接口。启用此选项后，将覆盖此要求，并使用客户端上指定的 "interface" 中的 MAC 地址。 |
| ****validate-server-duid**** (*yes \| no*; 默认值：**yes**) | 允许忽略 DHCPv6 服务器提供的格式错误的 DUID。仍会检查最小 DUID 长度是否正确。 |
| **custom-iapd-id**(integer; 默认值：) | 允许指定自定义 IAPD ID。 |
| **custom-iana-id**(*integer*; 默认值：) | 允许指定自定义 IANA ID。 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **duid** (*string*) | 发送到服务器的自动生成 DUID。DUID 使用路由器上可用的 MAC 地址之一生成。 |
| **request** (*list*) | 指定请求的内容 - 前缀、地址或两者。 |
| **dynamic** (*yes \| no*) |  |
| **expires-after** (*time*) | IPv6 前缀到期的时间（由 DHCPv6 服务器指定）。 |
| **invalid** (*yes \| no*) | 显示配置是否无效。 |
| **prefix** (*IPv6 prefix*) | 显示从 DHCPv6-PD 服务器接收的 IPv6 前缀。 |
| **status** (*stopped \| searching \| requesting... \| bound \| renewing \| rebinding \| error \| stopping*) | 显示 DHCPv6 客户端的状态：stopped - dhcpv6 客户端已停止。searching - 发送 "solicit" 并尝试获取 "advertise"。requesting - 已发送 "request" 等待 "reply"。bound - 已收到 "reply"。前缀已分配。renewing - 已发送 "renew"，等待 "reply"。rebinding - 已发送 "rebind"，等待 "reply"。error - 未及时收到回复或发生其他错误。stopping - 已发送 "release"。 |
| **reconfigure-key**(string) | 重新配置认证密钥。 |
| **reconfigure-last-counter** (integer) | 接收到的 forcerenew 消息计数。 |
| dhcp-server-v6  | |
| address  | |

### 菜单特定命令

| 属性 | 描述 |
| :-- | :-- |
| **release** (*numbers*) | 释放当前绑定并重启 DHCPv6 客户端。 |
| **renew** (*numbers*) | 续租当前租约。如果续租操作不成功，客户端会尝试重新初始化租约（即，它像尚未收到 IP 地址一样启动租约请求过程 (rebind)）。 |

### 脚本

可以使用 DHCP 客户端添加一个脚本，该脚本将在获取并应用前缀或地址，或过期并被移除时执行。由于客户端可以同时获取前缀和地址，并且它们中的每一个都可能对路由器配置产生不同的影响，因此存在单独的变量集，其值将由客户端根据前缀或地址状态更改来设置。

#### DHCP 客户端的可用变量

- pd-valid - 值 - 1 或 0 - 前缀是否已获取并应用
- pd-prefix - 值 ipv6/num (带掩码的 ipv6 前缀) - 前缀本身
- na-valid - 值 - 1 或 0 - 地址是否已获取并应用
- na-address - 值 - ipv6 地址 - 地址

### IAID

要确定将使用哪个 IAID，请将运行 DHCP 客户端的接口的内部 ID 从十六进制转换为十进制。

例如，DHCP 客户端在接口 PPPoE-out1 上运行。要获取内部 ID，请使用以下命令：

```ros
[admin@t36] /interface> :put [find name="pppoe-out1"] 
*15
```

现在将十六进制值 15 转换为十进制，您将得到 IAID=21。

### 配置示例

#### 简单 DHCPv6 客户端

这个简单的示例演示了如何启用 dhcp 客户端以接收 IPv6 前缀并将其添加到池中。

```ros
/ipv6/dhcp-client/add request=prefix pool-name=test-ipv6 pool-prefix-length=64 interface=ether13 

```

详细打印应显示客户端的状态，我们可以验证是否收到了前缀：

```ros
[admin@x86-test] /ipv6/dhcp-client> print detail 
Flags: D - dynamic, X - disabled, I - invalid
 0 interface=bypass pool-name="test-ipv6" pool-prefix-length=64 status=bound 
prefix=2001:db8:7501:ff04::/62 expires-after=2d23h11m53s request=prefix
```

请注意，服务器给了我们前缀 2001:db8:7501:ff04::/62。它也应该被添加到 ipv6 池中：

```ros
[admin@MikroTik] /ipv6/pool> print 
Flags: D - dynamic 
# NAME PREFIX REQUEST PREFIX-LENGTH
0 D test-ipv6 2001:db8:7501:ff04::/62 prefix 64

```

成功了！现在您可以使用这个池，例如，用于 pppoe 客户端。

#### 使用接收到的前缀进行本地 RA

考虑以下设置：

![](https://manual.mikrotik.com/docs/network-management/img/dhcp-01.webp)

- ISP 将前缀 2001:DB8::/62 路由到路由器 R1。
- 路由器 R1 运行 DHCPv6 服务器，将 /64 前缀委派给客户路由器 CE1 和 CE2。
- 路由器 CE1 和 CE2 上的 DHCP 客户端从 DHCP 服务器 (R1) 接收委派的 /64 前缀。
- 客户端路由器使用接收到的前缀在本地接口上设置 RA。

**配置**

**R1**

```ros
/ipv6/route 
add gateway=fe80::1:1%to-ISP 

/ipv6/pool 
add name=myPool prefix=2001:db8::/62 prefix-length=64 

/ipv6/dhcp-server
 add prefix-pool=myPool disabled=no interface=to-CE-routers lease-time=3m name=server1
```

**CE1**

```ros
/ipv6/dhcp-client
add interface=to-R1 request=prefix pool-name=my-ipv6

/ipv6/address
add address=::1/64 from-pool=my-ipv6 interface=to-clients advertise=yes

```

**CE2**

```ros
/ipv6/dhcp-client
 add interface=to-R1 request=prefix pool-name=my-ipv6 
/ipv6/address/add address=::1/64 from-pool=my-ipv6 interface=to-clients advertise=yes
```

**检查状态**

配置完成后，我们可以验证每个 CE 路由器是否收到了自己的前缀。

在服务器上：

```ros
[admin@R1] /ipv6/dhcp-server/binding> print
 Flags: X - disabled, D - dynamic 
# ADDRESS DUID IAID SERVER STATUS
 1 D 2001:db8:1::/64 0019d1393536 566 server1 bound 
2 D 2001:db8:2::/64 0019d1393535 565 server1 bound
```

在客户端上：

```ros
[admin@CE1] /ipv6/dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
# INTERFACE STATUS REQUEST PREFIX 
0 to-R1 bound prefix 2001:db8:1::/64 

[admin@CE1] /ipv6/dhcp-client> /ipv6/pool/print 
Flags: D - dynamic 
# NAME PREFIX PREFIX-LENGTH
0 D my-ipv6 2001:db8:1::/64 64
```

我们还可以看到，一个 IPv6 地址已自动从前缀池中添加：

```ros
[admin@CE1] /ipv6/address> print 
Flags: X - disabled, I - invalid, D - dynamic, G - global, L - link-local 
# ADDRESS FROM-POOL INTERFACE ADVERTISE 0 G 2001:db8:1::1/64 to-clients yes 
..
```

并且池使用情况显示 'Address' 正在分配该池：

```ros
[admin@CE1] /ipv6/pool/used> print
 POOL PREFIX OWNER INFO 
my-ipv6 2001:db8:1::/64 Address to-clients
```

## DHCP 服务器

### 概述

DHCP（动态主机配置协议）用于在网络中轻松分配 IP 地址。MikroTik RouterOS 的实现包括服务器和客户端部分，并符合 RFC 2131 标准。

路由器支持为每个类似以太网的接口提供独立的服务器。MikroTik RouterOS DHCP 服务器支持基本功能，即为每个请求的客户端提供 IP 地址/子网掩码租约、默认网关、域名、DNS 服务器和 WINS 服务器（用于 Windows 客户端）信息（在 DHCP 网络子菜单中设置）。

为了使 DHCP 服务器正常工作，还必须配置 IP 池（不要将 DHCP 服务器自身的 IP 地址包含在池范围内），并且还必须配置 DHCP 网络。

也可以使用 RADIUS 服务器为 DHCP 客户端分配租约；RADIUS 服务器支持的参数如下：

#### Access-Request

- NAS-Identifier - 路由器标识。
- NAS-IP-Address - 路由器自身的 IP 地址。
- NAS-Port - 配置 DHCP 服务器的接口 ID。此值与 IF-MIB::ifIndex 相同。
- NAS-Port-Id - 配置 DHCP 服务器的接口名称。
- NAS-Port-Type - Ethernet。
- Calling-Station-Id - 客户端标识符 (active-client-id)。
- Framed-IP-Address - 客户端的 IP 地址 (active-address)。
- Called-Station-Id - DHCP 服务器的名称。
- User-Name - 客户端的 MAC 地址 (active-mac-address)。
- Password - " "。

#### Access-Accept

- Framed-IP-Address - 将分配给客户端的 IP 地址。
- Framed-Pool - 从中为客户端分配 IP 地址的 IP 池。
- Rate-Limit - DHCP 客户端的数据速率限制。格式为：rx-rate[/tx-rate] [rx-burst-rate[/tx-burst-rate] [rx-burst-threshold[/tx-burst-threshold] [rx-burst-time[/tx-burst-time][priority] [rx-rate-min[/tx-rate-min]]]]。所有速率应为数字，可选用 'k' (1,000s) 或 'M' (1,000,000s)。如果未指定 tx-rate，则 rx-rate 也用作 tx-rate。tx-burst-rate、tx-burst-threshold 和 tx-burst-time 同理。如果未指定 rx-burst-threshold 和 tx-burst-threshold（但指定了 burst-rate），则使用 rx-rate 和 tx-rate 作为突发阈值。如果未指定 rx-burst-time 和 tx-burst-time，则默认使用 1s。优先级取值 1..8，其中 1 表示最高优先级，8 表示最低。如果未指定 rx-rate-min 和 tx-rate-min，则使用 rx-rate 和 tx-rate 值。rx-rate-min 和 tx-rate-min 值不能超过 rx-rate 和 tx-rate 值。
- Ascend-Data-Rate - TX/RX 数据速率限制。如果提供多个属性，第一个限制 TX 数据速率，第二个限制 RX 数据速率。如果与 Ascend-Xmit-Rate 一起使用，则指定 RX 速率。0 表示无限制。
- Ascend-Xmit-Rate - TX 数据速率限制。它可以仅用于指定 TX 限制，而不是发送两个连续的 Ascend-Data-Rate 属性（在这种情况下，Ascend-Data-Rate 将指定接收速率）。0 表示无限制。
- Session-Timeout - 最大租约时间 (lease-time)。

:::warning
DHCP 服务器需要一个真实接口来接收原始以太网数据包。如果接口是 Bridge 接口，则该 Bridge 必须有一个真实接口作为端口连接到该 Bridge，以接收原始以太网数据包。它无法在 dummy（空桥接）接口上正常运行。

:::

### DHCP 服务器属性

| 属性 | 描述 |
| :-- | :-- |
| **add-arp** (*yes \| no*; 默认值：**no**) | 是否添加动态 ARP 条目。如果设置为 **no**，则应在该接口上启用 ARP 模式，或者在 *`/ip/arp`* 子菜单中管理性地定义静态 ARP 条目。 |
| **add-dns-entries** (*yes \| no*; 默认值：**no**) | 设置为 **yes** 时，DHCP 服务器会自动为每个租约使用客户端的主机名创建动态 DNS A 记录。主机名取自客户端发送的 DHCP 选项 12。生成的 FQDN 通过将 **add-dns-entries-suffix**（如果未设置后缀，则为 DHCP 网络配置中的 **domain**）附加到主机名来形成。 |
| **add-dns-entries-suffix** (*string*; 默认值：**""**) | 创建动态 DNS 条目时附加到主机名的后缀。例如，如果设置为 `example.lan` 且客户端主机名为 `laptop`，则将创建 DNS 条目 `laptop.example.lan`。如果留空，则使用 DHCP 网络配置中的 **domain** 值。 |
| **address-pool** (*string \| static-only*; 默认值：**static-only**) | 从中为客户端获取 IP 地址的 IP 池。如果设置为 **static-only**，则只允许具有静态租约（在租约子菜单中添加）的客户端。 |
| **allow-dual-stack-queue** (*yes \| no*; 默认值：**yes**) | 为 IPv4 和 IPv6 地址创建单个简单队列条目，并使用 MAC 地址和 DUID 进行标识。要求 IPv6 DHCP 服务器也启用此选项才能正常工作。 |
| **always-broadcast** (*yes \| no*; 默认值：**no**) | 更改是否强制广播 DHCP 回复：no - 回复根据客户端的广播标志发送。如果服务器发送三个连续的 offer，则第三个和第四个 offer 将作为广播发送；yes - 即使客户端未指定广播标志，回复也始终广播。 |
| **authoritative** (*after-10sec-delay \| after-2sec-delay \| yes \| no*; 默认值：**yes**) | 该选项更改服务器响应 DHCP 请求的方式：yes - 回复客户端对此服务器不可用的地址的请求，DHCP 服务器将发送否定确认 (DHCPNAK)；no - DHCP 服务器忽略客户端对此服务器不可用的地址的请求；after-10sec-delay - "secs &lt; 10" 的请求将按照 "no" 设置的情况处理，"secs &gt;= 10" 的请求将按照 "yes" 的情况处理；after-2sec-delay - "secs &lt; 2" 的请求将按照 "no" 设置的情况处理，"secs &gt;= 2" 的请求将按照 "yes" 的情况处理； 如果应忽略所有 "secs < x" 的请求，则应使用 **delay-threshold=x** 设置。 |
| **bootp-lease-time** (*forever \| lease-time \| time*; 默认值：**forever**) | 接受两个预定义选项或时间值：forever - 租约永不过期。lease-time - 使用 lease-time 参数中的时间。 |
| **bootp-support** (*none \| static \| dynamic*; 默认值：**static**) | 对 BOOTP 客户端的支持：none - 不响应 BOOTP 请求。static - 仅向 BOOTP 客户端提供静态租约。dynamic - 为 BOOTP 客户端提供静态和动态租约。 |
| **client-mac-limit** (*integer \| unlimited*; 默认值：**unlimited**) | 指定是限制每个 MAC 地址的特定客户端数量还是保持无限制。请注意，此设置不应用于中继设置。 |
| **conflict-detection** (*yes \| no*; 默认值：**yes**) | 允许禁用/启用冲突检测。如果启用该选项，则每当服务器尝试分配租约时，它都会发送 ICMP 和 ARP 消息以检测网络中是否已存在此类地址。如果上述任何消息得到回复，则认为该地址已被使用。 |
| **delay-threshold** (*time \| none*; 默认值：**none**) | 如果 DHCP 数据包中的 secs 字段小于延迟阈值，则忽略此数据包。如果设置为 **none** - 没有阈值（处理所有 DHCP 数据包）。 |
| **dhcp-option-set** (*name \| none*; 默认值：**none**) | 使用在选项集菜单中定义的自定义 DHCP 选项集。 |
| **dynamic-lease-identifiers** (*list of client-id, client-mac, opt-82*; 默认值：**client-id,client-mac**) | 指定在生成动态 DHCP 租约时使用和存储哪些参数。 |
| **insert-queue-before** (*bottom \| first \| name*; 默认值：**first**) | 指定为设置了 rate-limit 参数的静态 DHCP 租约放置动态简单队列条目的位置。 |
| **interface** (*string*; 默认值：) | DHCP 服务器将运行的接口。 |
| **lease-script** (*string*; 默认值：**""**) | 在分配或取消分配租约后执行的脚本。可在脚本中使用的内部 "global" 变量：leaseBound - 如果绑定则设置为 "1"，否则设置为 "0"。leaseServerName - DHCP 服务器名称。leaseActMAC - 活动 MAC 地址。leaseActIP - 活动 IP 地址。lease-agent-circuit-id - 租约代理电路 ID。lease-agent-remote-id - 租约代理远程 ID。lease-hostname - 客户端主机名。lease-options - 发送给客户端的选项数组。 |
| **lease-time** (*time*; 默认值：**30m**) | 客户端可以使用分配地址的时间。客户端将在此时间的一半后尝试续租此地址，并在时间限制到期后请求新地址。 |
| **name** (*string*; 默认值：) | 引用名称。 |
| **parent-queue** (*string \| none*; 默认值：**none**) | 为此租约动态创建的队列将配置为指定父队列的子队列。 |
| **relay** (*IP*; 默认值：**0.0.0.0**) | 此 DHCP 服务器应处理来自哪个中继