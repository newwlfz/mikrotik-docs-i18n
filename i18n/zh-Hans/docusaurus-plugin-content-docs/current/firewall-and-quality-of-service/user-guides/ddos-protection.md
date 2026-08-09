# DDoS 防护

> 本页面介绍 MikroTik RouterOS 的 DDoS 防护配置，涵盖用于检测和阻断各类攻击（如 HTTP 洪水、SYN 洪水、DNS 放大攻击等）的防火墙规则。内容包括地址列表、防火墙链以及用于缓解 DoS/DDoS 攻击的特定 TCP SYN Cookie 设置的详细配置示例。

# DDoS 防护

拒绝服务（DoS）或分布式拒绝服务（DDoS）攻击是一种恶意行为，旨在通过大量互联网流量淹没目标服务器、服务或网络及其周边基础设施，从而破坏其正常流量。DDoS 攻击有多种类型，例如 HTTP 洪水、SYN 洪水、DNS 放大攻击等。

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/user-guides/img/ddos-attack-diagram.jpg)

## DDoS 防护措施

### 配置命令行

:::warning
这些规则仅是对防火墙的改进，请勿忘记妥善保护您的设备。
:::

```ros
/ip/firewall/address-list
add list=ddos-attackers
add list=ddos-targets
/ip/firewall/filter
add chain=forward connection-state=new action=jump jump-target=detect-ddos
add action=return chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s
add action=add-dst-to-address-list address-list=ddos-targets address-list-timeout=10m chain=detect-ddos
add action=add-src-to-address-list address-list=ddos-attackers address-list-timeout=10m chain=detect-ddos
/ip/firewall/raw
add action=drop chain=prerouting dst-address-list=ddos-targets src-address-list=ddos-attackers
```

### 配置说明

首先，我们将每个新连接发送到特定的防火墙链，以便在其中检测 DDoS：

```ros
/ip/firewall/filter/add chain=forward connection-state=new action=jump jump-target=detect-ddos
```

在新创建的链中，我们将添加带有“dst-limit”参数的以下规则。该参数的格式为：**dst-limit=****count[/time],burst,mode[/expire]**。我们将基于源和目的地址流匹配 32 个数据包，突发大小为 32 个数据包，每 10 秒更新一次。该规则将持续生效，直到超过给定速率。

```ros
/ip/firewall/filter/add chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s action=return
```

到目前为止，所有合法流量都应通过“action=return”处理，但在 DoS/DDoS 情况下，“dst-limit”缓冲区将被填满，规则将不再“捕获”任何新流量。接下来是处理攻击的规则。首先，我们为需要丢弃的攻击者和受害者创建列表：

```ros
/ip/firewall/address-list/add list=ddos-attackers
/ip/firewall/address-list/add list=ddos-targets
/ip/firewall/raw/add chain=prerouting action=drop src-address-list=ddos-attackers dst-address-list=ddos-targets
```

在防火墙过滤部分，我们将攻击者添加到“ddos-attackers”列表，将受害者添加到“ddos-targets”列表：

```ros
/ip/firewall/filter
add action=add-dst-to-address-list address-list=ddos-targets address-list-timeout=10m chain=detect-ddos
add action=add-src-to-address-list address-list=ddos-attackers address-list-timeout=10m chain=detect-ddos
```

## SYN 攻击

### SYN 洪水

SYN 洪水是一种 DoS 攻击形式，攻击者向目标系统发送一系列 SYN 请求，试图消耗足够的服务器资源，使系统无法响应合法流量。幸运的是，RouterOS 提供了针对此类攻击的特定功能：

```ros
/ip/settings/set tcp-syncookies=yes
```

该功能的工作原理是发送包含少量加密哈希的 SYN-ACK 数据包，响应客户端会将其作为 ACK 数据包的一部分回显。如果内核在回复数据包中未看到此“cookie”，则会认为连接是伪造的并将其丢弃。

### SYN-ACK 洪水

SYN-ACK 洪水是一种攻击方法，涉及以高速率向目标服务器发送伪造的 SYN-ACK 数据包。服务器需要大量资源来处理此类乱序数据包（不符合正常的 SYN、SYN-ACK、ACK TCP 三次握手机制）。服务器可能因忙于处理攻击流量而无法处理合法流量，从而使攻击者实现 DoS/DDoS 状态。在 RouterOS 中，我们可以配置与前述示例类似的规则，但更专门针对 SYN-ACK 洪水：

```ros
/ip/firewall/filter/add action=return chain=detect-ddos dst-limit=32,32,src-and-dst-addresses/10s protocol=tcp tcp-flags=syn,ack
```