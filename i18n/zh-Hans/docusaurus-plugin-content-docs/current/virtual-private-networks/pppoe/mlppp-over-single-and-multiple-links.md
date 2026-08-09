# 单链路与多链路 MLPPP

> MLPPP 通过将数据分割并重组到多条逻辑或物理链路上，增强 PPP 链路性能，在不升级硬件的情况下提升带宽。它支持单链路（使用 MRRU）和多链路配置，并提供 PPPoE 服务器/客户端的配置示例。

# 单链路与多链路 MLPPP

**标准：** `RFC 1990`

多链路点对点协议（MP、Multi-Link PPP、MultiPPP 或 MLPPP）是一种在多个逻辑数据链路上分割、重组和排序数据的方法。

当两台设备之间存在多条 DSL 链路时，通过使用多链路 PPP 来“拓宽管道”可以提升性能，而无需采用更新、更昂贵的技术。

大包实际上会被分割成片段，并均匀地发送到所有逻辑数据链路上。这一过程是即时完成的，不会损失带宽。重要的是，链路对端必须使用相同的协议来重组数据。

多链路基于 [LCP](../../mobile-networking/ppp.md#introduction) 选项协商，用于向对端表明其具备组合多条物理链路的能力。

## 单链路 MLPPP

通常，通过 PPP 链路发送的数据包大小会因开销而减小。MP 可用于在单条 PPP 链路上传输和接收完整帧。为此，多链路协议使用额外的 LCP 配置选项 **多链路最大接收重组单元（MRRU）**。

要在单条链路上启用多链路 PPP，必须指定 MRRU（最大接收重组单元）选项。如果双方都支持此功能，则无需进行 MSS 调整（在防火墙 mangle 中）。研究表明，MRRU 比每个客户端两条 mangle 规则更节省 CPU。MRRU 允许将数据包分割到多个通道，从而增加可能的 MTU 和 MRU（最高可达 65535 字节）。

在 Windows 下，可以在“网络”选项卡的“设置”按钮中启用“为单链路连接协商多链路”。其 MRRU 被硬编码为 1614。

:::warning
启用 MPPE 加密后，MTU 将减少 4 字节以确保正常工作。
:::

### 配置示例

让我们配置一个兼容 Windows 客户端且启用 MRRU 的 PPPoE 服务器。

```ros
[admin@RB800] /interface/pppoe-server/server> add service-name=myPPP interface=ether1 mrru=1614
[admin@RB800] /interface/pppoe-server/server> print 
Flags: X - disabled 
 0   service-name="myPPP" interface=ether1 max-mtu=1480 max-mru=1480 mrru=1614 
     authentication=pap,chap,mschap1,mschap2 keepalive-timeout=10 one-session-per-host=no 
     max-sessions=0 default-profile=default 
 
```

简而言之——标准 PPP 链路——只需在双方指定 MRRU 即可。

## 多链路 MLPPP

多链路 MLPPP 允许通过多条物理连接创建单条 PPP 链路。所有 PPP 链路必须来自同一服务器（服务器必须支持多链路 MLPPP），且所有 PPP 链路必须使用相同的用户名和密码。

要启用 MLPPP，只需创建一个 PPP 客户端并指定多个接口，而不是单个接口。RouterOS 仅支持 MLPPP 客户端。目前尚无 MLPPP 服务器支持。

### 配置示例

![](https://manual.mikrotik.com/docs/virtual-private-networks/pppoe/img/mlppp-over-single-and-multiple-links-01.webp)

ISP 为其客户提供两条物理链路（DSL 线路），每条带宽为 1Mbps。要获得聚合的 2Mbps 管道，我们必须设置 MLPPP。假设 ISP 路由器已预先配置为支持 MLPPP。

路由器（R1）上的配置如下：

```ros
/interface/pppoe-client 
   add service-name=ISP interface=ether1,ether2 user=xxx password=yyy disabled=no \
   add-default-route=yes use-peer-dns=yes
```

```ros
[admin@RB800] /interface/pppoe-client> print 
Flags: X - disabled, R - running 
 0    name="pppoe-out1" max-mtu=1480 max-mru=1480 mrru=disabled interface=ether1,ether2 
      user="xxx" password="yyy" profile=default service-name="ISP" ac-name="" add-default-route=yes
      dial-on-demand=no use-peer-dns=yes allow=pap,chap,mschap1,mschap2  
```

现在 PPPoE 客户端已连接，我们可以配置其余部分：本地网络地址、启用 DNS 请求、设置伪装和防火墙。

```ros
/ip/address/add address=192.168.88.1/24 interface=local

/ip/dns/set allow-remote-request=yes

/ip/firewall/nat
add chain=srcnat action=masquerade out-interface=pppoe-out1

/ip/firewall/filter
add chain=input connection-state=invalid action=drop \
	comment="丢弃无效连接"  
add chain=input connection-state=established action=accept \
	comment="允许已建立连接"  
add chain=input protocol=icmp action=accept \
	comment="允许 ICMP" 
add chain=input src-address=192.168.88.0/24 action=accept \
	in-interface=!pppoe-out1
add chain=input action=drop comment="丢弃所有其他流量"   
```

有关更高级的路由器和客户保护，请参阅 [防火墙示例](../../firewall-and-quality-of-service/firewall/filter.md)。