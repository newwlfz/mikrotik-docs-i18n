# 保护您的路由器安全

> 本页面提供 MikroTik RouterOS 的安全建议，包括升级 RouterOS 版本、更改默认用户名和密码、通过防火墙规则和 VPN 保护访问安全、禁用 MAC-Telnet 和 Neighbor Discovery 等不必要服务，以及管理 DNS 缓存以增强路由器安全性。

# 保护您的路由器安全

以下步骤是在已配置好[强防火墙规则](../firewall-and-quality-of-service/firewall/filter.md)的基础上，进一步保护您设备的建议。

## RouterOS 版本

首先升级您的 RouterOS 版本。某些旧版本存在已被修复的弱点或漏洞。请保持设备更新以确保安全。在 WinBox 或 WebFig 中点击“检查更新”即可升级。建议关注我们的[安全公告博客](https://blog.mikrotik.com)以了解任何新的安全问题。

### 访问用户名

将默认用户名 **admin** 更改为自定义名称。使用唯一用户名有助于在他人获得设备物理访问权限时保护路由器的访问安全：

```ros
/user/add name=myname password=mypassword group=full
/user/disable admin
```

### 访问密码

MikroTik 路由器要求配置密码。我们建议使用密码生成器工具创建安全且不重复的密码。所谓安全密码，我们指的是：

- 至少 12 个字符。
- 包含数字、符号、大写和小写字母。
- 不是字典单词或字典单词的组合。
- 注意密码中的引号字符需要转义。

```ros
/user/set myname password="!={Ba3N!40TуX+GvKBz?jTLIUcx/,"
```

### 保护设备访问安全

默认情况下，预配置的防火墙会阻止来自 WAN（面向互联网）接口的所有管理访问。**这是有意为之——除非您完全理解后果，否则请勿删除这些规则。**

:::danger[请勿将管理服务暴露到互联网]
管理接口开放到互联网的网络设备会不断被自动化攻击扫描和攻击。将 WinBox、SSH 或其他管理服务直接暴露到互联网可能导致：

- 针对登录凭据的**暴力破解攻击**。
- 利用未修补 RouterOS 版本中的**已知漏洞**。
- **设备完全被入侵**——攻击者可以拦截流量、重定向 DNS、安装恶意软件，或将路由器用作进一步攻击的代理。

如果您需要远程访问设备，**请使用 VPN**（如 [WireGuard](../virtual-private-networks/wireguard.md)）创建加密隧道。这样管理流量就完全不会经过公共互联网。
:::

### 从 WAN 开放管理访问（高级）

以下防火墙规则适用于无法避免直接从 WAN 访问管理服务的情况——例如 ISP 管理的基础设施或没有 VPN 网关的站点。**除非您有直接面向互联网管理的特定需求，否则请勿应用这些规则。**

这些规则仅允许来自 WAN 接口的 ICMP（ping 和 traceroute）、WinBox 和 SSH，并丢弃所有其他流量：

```ros
/ip/firewall/filter
add chain=input action=accept connection-state=established,related,untracked comment="接受已建立、相关、未跟踪连接"
add chain=input action=drop connection-state=invalid comment="丢弃无效连接"
add chain=input in-interface=ether1 action=accept protocol=icmp comment="接受 ICMP"
add chain=input in-interface=ether1 action=accept protocol=tcp dst-port=8291 comment="允许 WinBox"
add chain=input in-interface=ether1 action=accept protocol=tcp dst-port=22 comment="允许 SSH"
add chain=input in-interface=ether1 action=drop comment="阻止所有其他流量"
```

:::warning
如果公共接口是 PPPoE、LTE 或其他接口类型，`in-interface` 应相应设置。如果选择了错误的接口，您可能会失去对设备的访问权限。
:::

:::danger[需要额外的加固措施]
如果您从 WAN 开放管理访问，**还必须**：

- 使用强且唯一的密码（参见[访问密码](#访问密码)）。
- 尽可能限制访问到特定的源地址。
- 保持 RouterOS 更新到最新的稳定版本。
- 监控日志以发现未经授权的连接尝试。
:::

您还可以使用 **Allowed Address** 属性将特定用户账户限制到某些源地址：

```ros
/user/set 0 address=192.168.88.0/24
```

### RouterOS MAC 访问

RouterOS 包含内置功能选项，可提供便捷的网络设备管理访问。但是，以下服务应在生产网络中禁用：**MAC-Telnet、MAC-WinBox** 和 **MAC-Ping。**

```ros
/tool/mac-server/set allowed-interface-list=none 
/tool/mac-server/mac-winbox/set allowed-interface-list=none 
/tool/mac-server/ping/set enabled=no
```

### Neighbor Discovery

MikroTik Neighbor Discovery 协议用于发现和识别网络上的其他 MikroTik 路由器。要在所有接口上禁用 Neighbor Discovery，请使用以下命令：

```ros
/ip/neighbor/discovery-settings/set discover-interface-list=none
```

### Bandwidth server

Bandwidth server 用于测试两台 MikroTik 路由器之间的吞吐量。在生产环境中禁用它：

```ros
/tool/bandwidth-server/set enabled=no 
```

### DNS 缓存

DNS 缓存通过将解析后的 DNS 查询结果存储在路由器本地来提高性能，减少客户端设备向远程服务器解析 DNS 请求所需的时间。如果您的路由器不需要 DNS 缓存——例如，网络上的另一台设备负责 DNS 缓存——您应禁用此功能以提高安全性：

```ros
/ip/dns/set allow-remote-requests=no
```

### 其他服务

RouterOS 包含多项服务，可能根据您的配置而启用。以下服务应在生产环境中禁用：caching proxy、SOCKS、UPnP 和 MikroTik Cloud 服务。

```ros
/ip/proxy/set enabled=no
/ip/socks/set enabled=no
/ip/upnp/set enabled=no
/ip/cloud/set ddns-enabled=auto update-time=no
```

### 管理服务端口

在 `/ip/service` 菜单中禁用您不使用的 RouterOS 管理服务：

```ros
/ip/service/disable telnet,ftp,www,api
```

更改默认 SSH 端口可以减少自动化暴力破解尝试的暴露：

```ros
/ip/service/set ssh port=2200
```

每个服务也可以限制到特定的源地址，尽管使用防火墙规则（如上所述）强制执行访问控制是首选方法，因为它可以完全阻止连接到达服务：

```ros
/ip/service/set winbox address=192.168.88.0/24
```

### 更安全的 SSH 访问

您可以在路由器上启用更严格的 SSH 安全设置。这包括启用 aes-128-ctr 加密算法并禁用 hmac-sha1 和带 sha1 的 group 算法。要应用这些更安全的 SSH 设置，请使用以下命令：

```ros
/ip/ssh/set strong-crypto=yes
```

## 路由器接口

### 以太网/SFP 接口

建议禁用路由器上所有未使用的接口，以减少对路由器的未授权访问：

```ros
/interface/print 
/interface/set X disabled=yes
```

其中 **X** 是未使用接口的编号。

### LCD

某些 RouterBOARD 设备包含用于显示系统信息的 LCD 模块。要保护 LCD 安全，请设置 PIN 码：

```ros
/lcd/pin/set pin-number=3659 hide-pin-number=yes
```

或者，您可以完全禁用 LCD：

```ros
/lcd/set enabled=no
```