# VETH

> VETH（虚拟以太网）为 RouterOS 中的容器提供网络连接，作为一个虚拟接口，支持静态 IP 和 DHCP 分配的 IP、SLAAC，并可集成到桥接或路由配置中。

# VETH

VETH（虚拟以太网）是一种虚拟网络接口，为容器提供网络连接。它充当一个虚拟以太网端口，将 RouterOS 连接到容器，使容器能够与其他接口和网络进行通信。

VETH 接口的行为类似于标准以太网接口。它们可以被分配静态 IPv4 和 IPv6 地址，通过 DHCP 客户端获取地址，并支持 SLAAC。此外，VETH 接口可以像物理接口一样参与桥接或路由配置。

## 基本配置示例

有多种配置 VETH 的方法。以下是简单的示例。

```ros
# 使用 DHCP 客户端的 VETH
/interface/veth/add dhcp=yes

# 使用静态地址的 VETH
/interface/veth/add address=10.1.1.10/24 gateway=10.1.1.1 
```

配置接口后，您可以将其分配给容器。  
容器应获取由 DHCP 服务器分配的 IP 或静态地址。

## 属性

### VETH

**子菜单：** `/interface/veth/add`

VETH 接口的配置设置。

| 参数 | 类型 | 默认值 | 描述 |
| :-- | :-- | :-- | :-- |
| **address** | IPv4/IPv6 地址 | **无** | 将分配给接口的 IPv4 或 IPv6 地址 |
| **gateway** | IPv4 地址 | **无** | IPv4 网关地址 |
| **gateway6** | IPv6 地址 | **无** | IPv6 网关地址 |
| **mac-address** | MAC 地址 | **无** | 接口 MAC 地址 |
| **container-mac-address** | MAC 地址 | **无** | 将分配给容器的 MAC 地址 |
| **dhcp** | 是 / 否 | **否** | 在接口上启用 DHCP 客户端 |
| **name** | 字符串 | **无** | 接口名称 |