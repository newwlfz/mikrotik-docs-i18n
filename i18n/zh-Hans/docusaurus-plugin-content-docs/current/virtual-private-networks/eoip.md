# EoIP

> MikroTik RouterOS 中的以太网 over IP (EoIP) 隧道技术通过 GRE 封装在 IP 网络上创建安全的二层桥接，支持局域网扩展和与 IPsec 结合的加密连接等灵活拓扑。

# EoIP

以太网 over IP（EoIP）隧道是 MikroTik RouterOS 的一种协议，旨在通过 IP 网络在两台路由器之间创建以太网隧道。它基于 GRE 封装（RFC 1701），允许以太网帧通过路由 IP 基础设施传输，从而有效扩展远程站点之间的二层网络。

EoIP 隧道接口在 RouterOS 中表现为虚拟以太网接口，可与桥接功能配合使用。当添加到桥接时，所有以太网流量（包括广播和非 IP 协议）都会通过隧道转发，如同两端通过物理以太网链路直接连接一样。

EoIP 隧道可以运行在 IPIP、PPTP 或任何其他支持 GRE 封装的基于 IP 的传输之上。这为构建各种网络拓扑提供了灵活性。

EoIP 的典型使用场景包括：通过互联网桥接局域网段、通过加密隧道（结合 IPsec 或其他安全传输）扩展局域网，以及通过无线点对点或 ad-hoc 链路连接网络。

EoIP 将以太网帧封装在 GRE（IP 协议 47）数据包中，并转发到远程隧道端点。接收路由器解封装数据包，并将原始以太网帧注入本地桥接域。
**子菜单：** `/interface/eoip`

## 属性说明

| 属性 | 说明 |
| :-- | :-- |
| **allow-fast-path** (*yes \| no*; 默认值：**yes**) | 是否允许 FastPath 处理。如果使用 IPsec 隧道，必须禁用。 |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | 地址解析协议模式。disabled - 接口不使用 ARP；enabled - 接口使用 ARP；proxy-arp - 接口使用 ARP 代理功能；reply-only - 接口仅回复来自 `/ip/arp` 表中静态条目匹配的 IP 地址/MAC 地址组合的请求。不会自动在 `/ip/arp` 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-timeout** (*integer[/time]*; 默认值：**auto**) | ARP 条目应超时的时间间隔。 |
| **clamp-tcp-mss** (*yes \| no*; 默认值：**yes**) | 控制是否更改接收到的 TCP SYN 包的 MSS 大小。启用时，如果当前 MSS 大小超过隧道接口 MTU（考虑 TCP/IP 开销），路由器将更改接收到的 TCP SYN 包的 MSS 大小。接收到的封装包仍包含原始 MSS，仅在解封装后 MSS 才会被更改。 |
| **comment** (*string*; 默认值：) | 接口的简短描述。 |
| **disabled** (*yes \| no*; 默认值：**no**) | 项目是否禁用。 |
| **dont-fragment** (*inherit \| no*; 默认值：**no**) | 是否在相关数据包中包含 DF 位：*no* - 需要时分片，*inherit* - 使用原始数据包的“不分片”标志。（不使用“不分片”：inherit - 数据包可能被分片）。 |
| **dscp** (*integer: 0-63*; 默认值：**inherit**) | 数据包的 DSCP 值。继承选项表示 DSCP 值将从待封装的数据包中继承。 |
| **ipsec-secret** (*string*; 默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 指定密钥时，路由器会向 remote-address 添加动态 IPsec 对等体，使用预共享密钥和策略（默认 phase2 使用 sha1/aes128cbc）。 |
| **keepalive** (*integer[/time],integer 0..4294967295*; 默认值：**10s,10**) | 隧道 keepalive 参数设置时间间隔，在此间隔内即使隧道远端宕机，隧道运行标志仍将保持。如果配置的时间、重试失败，接口运行标志将被移除。参数格式为：`KeepaliveInterval,KeepaliveRetries`，其中 `KeepaliveInterval` 是时间间隔，`KeepaliveRetries` 是重试次数。默认 keepalive 设置为 10 秒和 10 次重试。 |
| **l2mtu** (*integer; 只读*) | 二层最大传输单元。EoIP 不可配置。[RouterOS 中的 MTU](../hardware/mtu-in-routeros.md) |
| **local-address** (*IP*; 默认值：) | 隧道数据包的源地址，位于路由器本地。 |
| **loop-protect** |  |
| **loop-protect-disable-time** |  |
| **loop-protect-send-interval** |  |
| **mac-address** (*MAC*; 默认值：) | 接口的媒体访问控制编号。地址编号机构 IANA 允许自由使用 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 范围内的 MAC 地址。 |
| **mtu** (*integer*; 默认值：**auto**) | 三层最大传输单元。 |
| **name** (*string*; 默认值：) | 接口名称。 |
| **remote-address** (*IP*; 默认值：) | EoIP 隧道远端的 IP 地址。 |
| **tunnel-id** (*integer: 0..65535*; 默认值：) | 唯一隧道标识符，必须与隧道另一端匹配。 |

## 配置示例

参数 tunnel-id 是标识隧道的一种方法。每个 EoIP 隧道必须唯一。

:::tip
EoIP 隧道至少增加 42 字节开销（8 字节 GRE + 14 字节以太网 + 20 字节 IP）。MTU 应设置为 1500，以消除隧道内的数据包分片（这允许透明桥接以太网类网络，从而可以通过隧道传输全尺寸以太网帧）。
:::

桥接 EoIP 隧道时，强烈建议为每个隧道设置唯一的 MAC 地址，以确保桥接算法正常工作。对于 EoIP 接口，可以使用 IANA 为此类情况保留的 **00:00:5E:80:00:00 - 00:00:5E:FF:FF:FF** 范围内的 MAC 地址。或者，可以设置第一个字节的第二位，将自动分配的地址修改为网络管理员分配的“本地管理地址”，从而使用任何 MAC 地址。只需确保连接到同一桥接的主机之间地址唯一即可。

### 示例

假设我们要桥接两个网络：“Station”和“AP”。通过使用 EoIP，可以设置使 Station 和 AP 局域网处于同一二层广播域。

考虑以下设置：

![](https://manual.mikrotik.com/docs/virtual-private-networks/img/eoip-01.webp)

如您所知，无线站点无法桥接；为了克服此限制（不涉及 WDS），我们将在无线链路上创建 EoIP 隧道，并将其与连接到本地网络的接口桥接。

本示例不涉及无线配置，假设无线链路已建立。

首先，在 AP 上创建 EoIP 隧道：

```ros
/interface/eoip/add name="eoip-remote" tunnel-id=0 remote-address=10.0.0.2 disabled=no
```

验证接口已创建：

```ros
[admin@AP] > /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-remote" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:A5:6C:3F:26:C5 arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.2 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes 
```

Station 路由器：

```ros
/interface/eoip/add name="eoip-main" tunnel-id=0 remote-address=10.0.0.1 disabled=no
```

验证接口已创建：

```ros
[admin@Station] >  /interface/eoip/print
Flags: X - disabled; R - running 
 0  R name="eoip-main" mtu=auto actual-mtu=1458 l2mtu=65535 mac-address=FE:4B:71:05:EA:8B arp=enabled 
      arp-timeout=auto loop-protect=default loop-protect-status=off loop-protect-send-interval=5s 
      loop-protect-disable-time=5m local-address=0.0.0.0 remote-address=10.0.0.1 tunnel-id=0 
      keepalive=10s,10 dscp=inherit clamp-tcp-mss=yes dont-fragment=no allow-fast-path=yes  
```

接下来，我们将在 AP 上将本地接口与 EoIP 隧道桥接。如果您已有本地桥接接口，只需将 EoIP 接口添加到其中：

```ros
/interface/bridge/port/add bridge=bridge1 interface=eoip-remote
```

桥接端口列表应列出所有本地 LAN 接口和 EoIP 接口：

```ros
[admin@AP] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE       BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2          bridge1  yes     1  0x80             10                  10  none   
1  H ether3          bridge1  yes     1  0x80             10                  10  none    
2    eoip-remote     bridge1  yes     1  0x80             10                  10  none    
```

在 Station 路由器上，如果您没有本地桥接接口，请创建新桥接并将 EoIP 和本地 LAN 接口添加到其中：

```ros
/interface/bridge/add name=bridge1
/interface/bridge/port/add bridge=bridge1 interface=ether2
/interface/bridge/port/add bridge=bridge1 interface=eoip-main
```

验证桥接端口部分：

```ros
[admin@Station] > /interface/bridge/port/print 
Flags: I - INACTIVE; H - HW-OFFLOAD
Columns: INTERFACE, BRIDGE, HW, PVID, PRIORITY, PATH-COST, INTERNAL-PATH-COST, HORIZON
#    INTERFACE     BRIDGE   HW   PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0  H ether2        bridge1  yes     1  0x80             10                  10  none    
2    eoip-main     bridge1  yes     1  0x80             10                  10  none    
```

现在两个站点处于同一二层广播域。您可以在两个站点上设置来自同一网络的 IP 地址。