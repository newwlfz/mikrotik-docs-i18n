# IS-IS

> IS-IS 是一种内部网关协议，用于在单个自治系统内分发 IP 路由信息，作为一种链路状态协议，在邻居之间交换拓扑数据。它支持 IPv4 和 IPv6，使用基于 TLV 的扩展，并且需要配置区域 ID、系统 ID 和 NSAP 地址才能正确路由。

# IS-IS

IS-IS（中间系统到中间系统）协议是一种内部网关协议（IGP），用于在整个自治系统内分发 IP 路由信息。

它最初是作为 CLNP 的路由协议开发的，但在 IP 变得流行后，后来被扩展以包含 IP 路由。扩展版本有时被称为集成 IS-IS。

IS-IS 属于链路状态协议家族，它在最近的邻居之间交换拓扑信息，并将其洪泛到整个 AS。主要优势在于，对网络拓扑的完整了解使路由器能够选择到目的地的最佳路径。它还可以用于流量工程目的。

邻居之间定期交换 **Hello** 数据包，形成邻接关系，并根据协商选择指定中间系统（DIS）。Hello 数据包分别针对 **Level-1** 和 **Level-2** 发送。

## 标准与技术

- [RFC 1195](https://datatracker.ietf.org/doc/html/rfc1195) 在 TCP/IP 和双协议环境中使用 OSI IS-IS 进行路由
- [RFC 5302](https://datatracker.ietf.org/doc/html/rfc5302) 使用两级 IS-IS 进行域范围前缀分发
- [RFC 5303](https://datatracker.ietf.org/doc/html/rfc5303) IS-IS 点对点邻接的三次握手
- [RFC 5305](https://datatracker.ietf.org/doc/html/rfc5305) IS-IS 流量工程扩展（仅支持宽度量）
- [RFC 5308](https://datatracker.ietf.org/doc/html/rfc5308) 使用 IS-IS 路由 IPv6

## IS-IS 术语

- **IS** - 中间系统是一种能够在远端主机之间转发流量的路由器。
- **LSP** - 链路状态 PDU 包含路由器本地状态的信息（可用接口、可达邻居以及接口的度量值）。参见 [`/routing/isis/lsp`](../../../cli-reference/routing/isis.md#routingisislsp)。
- **SPF** - 最短路径优先算法。
- **DIS** - 指定中间系统。DIS 确保网络中的所有路由器维护同步的数据库。L1 和 L2 路由分别选举独立的 DIS。DIS 的选举基于最高的接口优先级。
- **Level-1 (L1) 路由** - 控制 IS-IS 区域内的路由信息分发。L1 路由基于系统 ID。
- **Level-2 (L2) 路由** - 控制 IS-IS 区域之间的路由信息分发。L2 路由基于区域 ID。
- **IS-IS 邻接** - IS-IS 邻居之间的链路（参见 [`/routing/isis/neighbor`](../../../cli-reference/routing/isis.md#routingisisneighbor)）。形成的邻接类型取决于 IS-IS Hello 数据包中交换的参数。每个相邻路由器都运行 DIS 选举过程，以确定其是否有资格成为广播网络上的 L1 或 L2 DIS。
- **NSAP** - 网络服务访问点地址，用于标识路由器。
- **NET** - 网络实体名称。NSAP 地址的最后一个字节始终设置为零。

## 协议基础

IS-IS 协议基于 TLV（类型/长度/值），这使得它易于扩展。它使用 OSI 寻址原则，NSAP 地址按节点分配，而不是按接口分配。

NSAP 地址分为三个部分：

```
+-----+------+-----------+----+
| AFI | Area | System-ID | NS |
+-----+------+-----------+----+
```

- **AFI** - 最左侧的第一个字节定义 NSAP 地址的含义。IS-IS [`afi`](../../../cli-reference/routing/isis.md#afi) 参数控制实例处理的地址族。
- **区域 ID** - 2 个八位组。
- 大多数 IS-IS 实现使用 6 个八位组的 **系统 ID**。
- **NS**（N 选择器）- 一个字节，IS-IS 始终将其设置为零。

地址以十六进制字符串形式书写，每两个字节用点分隔，但有一些例外。
例如，NET 地址 `49222211112222aded00` 写为 `49.2222.1111.2222.aded.00`：

- 最左边的点分隔 AFI（2 个字符）。
- 后面是区域 ID（4 个字符）。
- 后面是系统 ID，分为 3 组，每组 4 个字符。
- 最右边的点必须位于系统 ID 和 N 选择器之间。

RouterOS 将 NET 地址拆分为两个配置选项。前 3 个字节（AFI 和区域）通过 [`areas`](../../../cli-reference/routing/isis.md#areas) 参数配置，接下来的 6 个字节是系统 ID，通过 [`system-id`](../../../cli-reference/routing/isis.md#system-id) 参数配置，最后一个 NS 字节不在任何地方显式配置。它始终假定为零。

某些其他厂商的实现可能要求 AFI 字节设置为特定值，例如 `0x47` 表示经典的 ISO NSAP 地址。
此外，`0x49` 可以用作私有地址空间，类似于 IPv4 私有地址范围（10.0.0.0/8 等）。

## 基本配置示例

基本配置需要创建一个实例（在 [`/routing/isis/instance`](../../../cli-reference/routing/isis.md#routingisisinstance) 下），设置区域 ID 和系统 ID，并通过 [`/routing/isis/interface-template`](../../../cli-reference/routing/isis.md#routingisisinterface-template) 在接口上启用 IS-IS。

例如，在三台路由器之间设置 IS-IS，一台 Cisco 和两台 RouterOS。

**R1:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no name=isis-instance-1 system-id=90ab.cdef.0001
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=ether1 levels=l1,l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=ether1 level-type=l2 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

 2 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=ether1 level-type=l1 snpa=D4:CA:6D:78:2F:2E srcid="1111.2222.cded" state=up 

[] /routing/route> print where is-is
Flags: A - ACTIVE; i - IS-IS
Columns: DST-ADDRESS, GATEWAY, AFI, DISTANCE, SCOPE, TARGET-SCOPE, IMMEDIATE-GW
   DST-ADDRESS        GATEWAY                AFI  DISTANCE  SCOPE  TARGET-SCOPE  IMMEDIATE-GW         
 i 0.0.0.0/0          10.155.101.214%ether1  ip4       115     20            10  10.155.101.214%ether1
 i 10.155.101.0/24    10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1
Ai 10.255.255.162/32  10.155.101.216%ether1  ip4       115     20            10  10.155.101.216%ether1

```

**R2:**

```ros
/routing/isis/instance
add afi=ip areas=49.2222 disabled=no l1.originate-default=always l2.originate-default=always name=isis-instance-1 \
    system-id=1111.2222.cded
/routing/isis/interface-template
add instance=isis-instance-1 interfaces=sfp12 levels=l1,l2
add instance=isis-instance-1 interfaces=lo levels=l2

[] /routing/isis/neighbor> print 
 0 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 1 instance=isis-instance-1 interface=sfp12 level-type=l1 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

 2 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=08:00:27:22:B4:A2 srcid="1111.2222.aded" state=up 

 3 instance=isis-instance-1 interface=sfp12 level-type=l2 snpa=C4:AD:34:43:EA:5C srcid="90ab.cdef.0001" state=up 

```

**R3 Cisco:**

```ros
interface Loopback0
 ip address 10.255.255.162 255.255.255.255
 ip router isis 
!
interface GigabitEthernet1
 ip address dhcp
 ip router isis 
 negotiation auto
!
router isis
 net 49.2222.1111.2222.aded.00
!

# 显示 IS-IS 邻居

Tag null:
System Id      Type Interface   IP Address      State Holdtime Circuit Id
90AB.CDEF.0001 L1   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
90AB.CDEF.0001 L2   Gi1         10.155.101.183  UP    27       1111.2222.CDED.01  
1111.2222.CDED L1   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01  
1111.2222.CDED L2   Gi1         10.155.101.214  UP    9        1111.2222.CDED.01 

# 显示 IP 路由

i*L1  0.0.0.0/0 [115/11] via 10.155.101.214, 4w5d, GigabitEthernet1
      10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
C        10.155.101.0/24 is directly connected, GigabitEthernet1
L        10.155.101.216/32 is directly connected, GigabitEthernet1
i L2     10.155.255.214/32 [115/10] via 10.155.101.183, 2w3d, GigabitEthernet1

```

## 故障排除

### IS-IS 无法工作并打印警告消息 "invalid 3way tlv"

此警告表示远端邻居很可能不符合 RFC 5303 中针对点对点网络的三次握手规范。例如，在 Cisco 上，您必须在接口上启用 "isis three-way-handshake ietf" 才能获得 15 字节的 TLV。