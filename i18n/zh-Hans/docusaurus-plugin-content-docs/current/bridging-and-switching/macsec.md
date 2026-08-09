# MACsec

> MACsec 是一种用于以太网的安全协议，通过 GCM-AES-128 加密提供机密性、完整性和真实性。RouterOS 支持手动密钥配置和有限的硬件加速，需要预共享密钥来确保设备之间安全的二层连接。

# MACsec

MACsec（媒体访问控制安全）协议是一种在以太网中使用的标准安全技术，用于确保通过物理介质传输的数据的机密性、完整性和真实性。MACsec 由 IEEE 标准 802.1AE 定义。

MACsec 在以太网上使用 GCM-AES-128 加密，并保护所有局域网流量，包括 DHCP、ARP、LLDP 以及更高层协议。

:::warning
RouterOS 的 MACsec 实现尚处于早期阶段；它**不支持**通过 [Dot1x](../authentication-authorization-accounting/dot1x.md) 进行动态密钥管理（需要手动配置密钥），并且硬件加速加密仅在部分产品上逐步推出。
:::

## 基本配置示例

假设 Host1 的 ether1 连接到 Switch 的 ether1，Host2 的 ether1 连接到 Switch 的 ether2。在此示例中，我们将创建两个 MACsec 接口对，并使用 bridge 在两个终端设备之间建立安全的二层连接。

首先，在 Host1 和 Host2 上配置 MACsec 接口。我们只需指定以太网接口，RouterOS 将自动生成连接关联密钥（CAK）和连接关联名称（CKN）。使用 `print` 命令查看这些值：

```ros
# Host1
/interface/macsec
add interface=ether1 name=macsec1

[admin@Host1] /interface/macsec/print show-sensitive
Flags: I - inactive, X - disabled, R - running 
 0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=71a7c363794da400dbde595d3926b0e9
     ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f profile=default

# Host2
/interface/macsec
add interface=ether1 name=macsec1

[admin@Host2] /interface/macsec/print show-sensitive
Flags: I - inactive, X - disabled, R - running 
 0   name="macsec1" mtu=1468 interface=ether1 status="negotiating" cak=dc47d94291d19a6bb26a0c393a1af9a4
     ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 profile=default
```

在 Switch 设备上，要启用 MACsec，我们需要为相应的以太网接口配置匹配的 CAK 和 CKN 值：

```ros
# Switch
/interface/macsec
add comment=Host1 cak=71a7c363794da400dbde595d3926b0e9 ckn=f2c4660060169391d29d8db8a1f06e5d4b84a128bad06ad43ea2bd4f7d21968f interface=ether1 name=macsec1
add comment=Host2 cak=dc47d94291d19a6bb26a0c393a1af9a4 ckn=e9bd0811dad1e56f06876aa7715de1855f1aee0baf5982ac8b508d4fc0f162d9 interface=ether2 name=macsec2
```

一旦预共享密钥成功交换，MACsec 密钥协议（MKA）即被激活。MKA 负责确保链路上 MACsec 的连续性，并决定在点对点连接中哪一方成为密钥服务器。密钥服务器生成一个安全关联密钥（SAK），该密钥仅与链路另一端的设备共享。此 SAK 用于保护通过链路的所有数据流量。密钥服务器会定期生成新的随机 SAK，并通过点对点链路共享，以维持 MACsec 功能。

在 RouterOS 中，MACsec 接口可以像任何以太网接口一样进行配置。它可以作为带有 IP 地址的可路由接口使用，也可以放置在 bridge 中。在 Host1 和 Host2 上，我们将添加同一网段的 IP 地址。在 Switch 上，我们将使用 bridge。

```ros
# Host1
/ip/address
add address=192.168.10.10/24 interface=macsec1

# Host2
/ip/address
add address=192.168.10.20/24 interface=macsec1

# Switch
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=macsec1
add bridge=bridge1 interface=macsec2
```

最后，确认 Host1 可以通过 ping 访问 Host2。

```ros
 [admin@Host1] > ping 192.168.10.20
  SEQ HOST                                     SIZE TTL TIME       STATUS
    0 192.168.10.20                              56  64 1ms438us  
    1 192.168.10.20                              56  64 818us     
    2 192.168.10.20                              56  64 791us     
    3 192.168.10.20                              56  64 817us     
    4 192.168.10.20                              56  64 783us     
    sent=5 received=5 packet-loss=0% min-rtt=783us avg-rtt=929us max-rtt=1ms438us
```

## 属性参考

### 接口设置

**子菜单：** `/interface/macsec`

MACsec 接口的配置设置。

| 属性 | 描述 |
| :-- | :-- |
| **cak** (*字符串*; 默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 一个 16 字节的预共享连接关联密钥（CAK）。要启用 MACsec，请在链路两端配置匹配的 CAK 和 CKN。如果未指定，RouterOS 将自动生成一个随机值。 |
| **ckn** (*字符串*; 默认值：) | 一个 32 字节的连接关联名称（CKN）。要启用 MACsec，请在链路两端配置匹配的 CAK 和 CKN。如果未指定，RouterOS 将自动生成一个随机值。 |
| **comment** (*字符串*; 默认值：) | 接口的简短描述。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 更改接口是否被禁用。 |
| **interface** (*名称*; 默认值：) | 创建 MACsec 的以太网接口名称，每个以太网接口仅限一个 MACsec 接口。 |
| **mtu** (*整数*; 默认值：**1468**) | 设置最大传输单元。`l2mtu` 将根据关联的 `interface` 自动设置（减去与 MACsec 封装对应的 32 字节）。`l2mtu` 不可更改。 |
| **name** (*字符串*; 默认值：**macsec1**) | 接口的名称。 |
| **profile** (*名称*; 默认值：**default**) | 设置 MACsec profile，用于确定点对点连接中的密钥服务器。 |
| **status** (*只读：disabled \| initializing \| invalid \| negotiating \| open-encrypted*) | 显示当前 MACsec 接口的状态。 |

### Profile 设置

**子菜单：** `/interface/macsec/profile`

MACsec profile 的配置设置。

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串*; 默认值：) | profile 的名称。 |
| **server-priority** (*整数：0..255*; 默认值：**10**) | 设置用于确定点对点连接中密钥服务器的优先级。数值越低表示优先级越高。如果优先级相同，则 MAC 地址最小的接口将充当密钥服务器。 |