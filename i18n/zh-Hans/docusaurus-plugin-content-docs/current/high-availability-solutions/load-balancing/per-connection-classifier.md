# 每连接分类器

> MikroTik RouterOS 中的每连接分类器（PCC）利用 IP 头部字段（如源/目标地址和端口）将流量划分为多个流，通过哈希算法将连接分配到不同链路上，以实现负载均衡。

# 每连接分类器

PCC 匹配器允许您将流量划分为相等的流，并能够将具有特定选项组合的数据包保留在某个特定的流中（您可以从 src-address、src-port、dst-address、dst-port 中指定这些选项组合）。

### 原理

PCC 从 IP 头部选取指定字段，通过哈希算法将这些字段转换为一个 32 位值。该值随后除以指定的 *Denominator*（分母），所得余数与指定的 *Remainder*（余数）进行比较，若相等则数据包将被匹配。您可以从头部选择 src-address、dst-address、src-port、dst-port 用于此操作。

:::danger
PCC 在 Hotspot（强制门户）场景下并非有效方法——因为目前 Hotspot 使用 Web 代理，且仅使用默认路由表。
:::

```ros
per-connection-classifier=
PerConnectionClassifier ::= [!]ValuesToHash:Denominator/Remainder
  Remainder ::= 0..4294967295    (整数)
  Denominator ::= 1..4294967295    (整数)
  ValuesToHash ::= both-addresses|both-ports|dst-address-and-port|
  src-address|src-port|both-addresses-and-ports|dst-address|dst-port|src-address-and-port 
```

### 示例

以下配置将基于源地址和端口将所有连接分为 3 组：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
 new-connection-mark=1st_conn per-connection-classifier=src-address-and-port:3/0
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=2nd_conn per-connection-classifier=src-address-and-port:3/1
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=3rd_conn per-connection-classifier=src-address-and-port:3/2
```

### PCC 工作原理

本文旨在以通俗易懂的方式解释 PCC 的工作原理。官方手册 Wiki 页面的定义如下：“PCC 从 IP 头部选取指定字段，通过哈希算法将这些字段转换为一个 32 位值。该值随后除以指定的 Denominator，所得余数与指定的 Remainder 进行比较，若相等则数据包将被匹配。您可以从头部选择 src-address、dst-address、src-port、dst-port 用于此操作。”可用字段的完整列表为：“both-addresses|both-ports|dst-address-and-port|src-address|src-port|both-addresses-and-ports|dst-address|dst-port|src-address-and-port”。如果您已经理解该定义，那么本文对您而言将没有新的内容。

首先，以下是理解该定义所需的术语。

IP 数据包具有包含多个字段的头部。其中两个字段是数据包的源 IP 地址和目标 IP 地址。TCP 和 UDP 数据包也具有包含源端口和目标端口的头部。

分母和余数是模运算的组成部分。模运算产生两个数相除后的整数余数，并且只接受结果的整数部分。它用 % 符号表示。以下是一些示例：3 % 3 = 0，因为 3 可以被 3 整除。4 % 3 = 1，因为 4 之前能被 3 整除的最大数是 3，且 4 - 3 = 1。5 % 3 = 2，因为 5 之前能被 3 整除的最大数是 3，且 5 - 3 = 2。6 % 3 = 0，因为 6 可以被 3 整除。

哈希是一种接收输入并产生输出的函数。哈希具有许多有趣的特性，但就本文而言，唯一重要的是哈希函数是确定性的。这意味着当您向哈希函数输入“hello”并得到输出“1”时，您可以确信再次输入“hello”仍会得到输出“1”。当您向哈希函数输入相同的输入时，它总是会产生相同的输出。PCC 具体使用哪种哈希算法并不重要，因此为了便于讨论，我们假设当您输入 IP 地址和端口时，它只是将 IP 地址的各八位字节作为十进制数以及端口相加，然后取最后一位数字作为输出。以下是一个示例：

哈希函数接收 1.1.1.1 作为源 IP 地址，10000 作为源 TCP 端口，2.2.2.2 作为目标 IP 地址，80 作为目标 TCP 端口。输出将为 1+1+1+1+10000+2+2+2+2+80 = 10092。该数字的最后一位是 2，因此哈希输出为 2。每次输入该 IP 地址和端口组合时，它都会产生 2。

此时需要指出的是，尽管 PCC 最常用于跨线路分散负载，但 PCC 本身与路由、路由标记或负载分散完全无关。PCC 仅仅是一种匹配数据包的方式，与随后对这些匹配数据包进行标记的操作没有直接关系，即使这是它的主要用途。

以下是常用于 PCC 的三行配置及其解释：

```ros
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
 new-connection-mark=1st_conn per-connection-classifier=src-address-and-port:3/0
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=2nd_conn per-connection-classifier=src-address-and-port:3/1
/ip/firewall/mangle/add chain=prerouting action=mark-connection \
  new-connection-mark=3rd_conn per-connection-classifier=src-address-and-port:3/2
```

以下是不同字段选项在数据包匹配方面的含义，这些字段将被输入哈希算法（并且，在跨链路分散负载的用途中，决定数据包将被置于哪条链路上）。请记住，哈希函数在输入相同的情况下总是会产生相同的输出：

- src-address：客户端的源地址始终相同，因此来自特定客户端的所有流量将始终匹配相同的 PCC 匹配器，并始终被置于同一条链路上。
- dst-address：特定服务器的目标地址始终相同，因此发往该服务器（例如 MikroTik Wiki）的所有流量将始终匹配相同的 PCC 匹配器，并始终被置于同一条链路上。
- both-addresses：同一客户端和服务器之间的源和目标 IP 对始终相同，因此特定客户端与特定服务器（例如您的笔记本电脑和 MikroTik Wiki）之间的所有流量将始终匹配相同的 PCC 匹配器，并始终被置于同一条链路上。
- src-port：客户端的源端口通常在创建连接时随机选择，因此在众多连接中，不同的源端口将被输入哈希函数，不同的 PCC 匹配器将匹配，流量将分散到不同链路上。然而，某些客户端协议总是选择相同的源端口，并且路由器后面的服务器很可能总是使用相同的服务端口向客户端发送回流量。路由器后面的 Web 服务器将主要从其 HTTP（80）和 HTTPS（443）端口发送流量，这些流量将始终匹配相同的 PCC 匹配器，并被置于同一条链路上。
- dst-port：客户端的目标端口通常是定义明确的服务端口，客户端与互联网服务器之间的所有 HTTP（80）流量将始终匹配相同的 PCC 匹配器，并被置于同一条链路上。然而，同一客户端进行的 HTTPS（443）流量可能匹配不同的 PCC 匹配器，并走不同的链路。
- both-ports：由于客户端端口（通常）是随机选择的，因此两个端口的组合（通常）是随机的，将能够分散负载到不同链路上。
- src-address-and-port：与 src-port 有相同的注意事项。
- dst-address-and-port：与 dst-port 有相同的注意事项。
- both-addresses-and-ports：这是将流量分散到链路的最随机方式，因为它具有最多的变量数量。

需要指出的是，尽管本文讨论的哈希函数被大大简化，并非实际使用的函数，但它很好地展示了哈希函数的另一个特性：两个完全不同的输入可以产生相同的输出。在我们的示例中，3 % 3 = 0，6 % 3 = 0；输入 3 和输入 6 都得到输出 0。PCC 使用的实际函数也是如此，尽管我不知道具体是什么，但从定义可知它产生一个 32 位值作为输出。IP 地址是 32 位，端口是 16 位，因此假设我们使用 both-addresses-and-ports，我们将输入 32+32+16+16 = 96 位数据，而只收到 32 位输出，因此它必然会对不同的输入产生相同的输出。这意味着两个完全不相关的连接可能匹配相同的 PCC 匹配器，并被置于同一条线路上。PCC 在承载的连接越多时效果越好，因为哈希函数有更多机会产生不同的输出。

### 配置示例

假设以下配置：

![](https://manual.mikrotik.com/docs/high-availability-solutions/load-balancing/img/per-connection-classifier-01.webp)

### IP 地址

```ros
/ip/address
add address=10.10.4.100/24 interface=ether_ISP1 network=10.10.4.0
add address=10.10.5.100/24 interface=ether_ISP2 network=10.10.5.0
add address=192.168.100.1/24 interface=ether_LAN network=192.168.100.0
```

路由器有两个上游（ISP）接口，地址分别为 10.10.4.100/24 和 10.10.5.100/24。LAN 接口的 IP 地址为 192.168.100.1/24。

我们添加两个新的路由表，稍后将使用：

```ros
/routing/table
add disabled=no fib name=ISP1_table
add disabled=no fib name=ISP2_table
```

### 策略路由

```ros
/ip/firewall/mangle
add action=accept chain=prerouting dst-address=10.10.4.0/24 in-interface=ether_LAN
add action=accept chain=prerouting dst-address=10.10.5.0/24 in-interface=ether_LAN
```

通过策略路由，可以强制所有流量发往特定网关，即使流量是发往来自连接网络的特定主机（而非该网关）。这样将产生路由环路，导致与这些主机的通信无法进行。为避免这种情况，我们需要允许对发往连接网络的流量使用默认路由表。

```ros
add action=mark-connection chain=input connection-state=new in-interface=ether_ISP1 new-connection-mark=ISP1
add action=mark-connection chain=input connection-state=new in-interface=ether_ISP2 new-connection-mark=ISP2

add action=mark-connection chain=output connection-mark=no-mark connection-state=new new-connection-mark=ISP1 per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=output connection-mark=no-mark connection-state=new new-connection-mark=ISP2 per-connection-classifier=both-addresses:2/1
```

首先，需要管理从外部发起的连接——回复必须通过请求到达的同一接口（来自相同的公网 IP）发出。我们将标记所有新的入站连接，以记住其到达的接口。

```ros
add action=mark-connection chain=prerouting connection-mark=no-mark connection-state=new dst-address-type=!local in-interface=ether_LAN new-connection-mark=ISP1 per-connection-classifier=both-addresses:2/0
add action=mark-connection chain=prerouting connection-mark=no-mark connection-state=new dst-address-type=!local in-interface=ether_LAN new-connection-mark=ISP2 per-connection-classifier=both-addresses:2/1
```

mark-routing 操作只能用于 mangle 链的 output 和 prerouting，但 prerouting 链会捕获所有发往路由器自身的流量。为避免这种情况，我们将使用 dst-address-type=!local。借助新的 PCC，我们将基于源地址和目标地址将流量分为两组。

```ros
add action=mark-routing chain=output connection-mark=ISP1 new-routing-mark=ISP1_table
add action=mark-routing chain=prerouting connection-mark=ISP1 in-interface=ether_LAN new-routing-mark=ISP1_table

add action=mark-routing chain=output connection-mark=ISP2 new-routing-mark=ISP2_table
add action=mark-routing chain=prerouting connection-mark=ISP2 in-interface=ether_LAN new-routing-mark=ISP2_table
```

然后，我们需要为来自这些连接的所有数据包标记适当的标记。由于策略路由仅对发往互联网的流量是必需的，请不要忘记指定 in-interface 选项。

```ros
/ip/route
add check-gateway=ping disabled=no dst-address=0.0.0.0/0 gateway=10.10.4.1 routing-table=ISP1_table suppress-hw-offload=no
add check-gateway=ping disabled=no dst-address=0.0.0.0/0 gateway=10.10.5.1 routing-table=ISP2_table suppress-hw-offload=no
```

为每个路由标记创建一条路由：

```ros
add distance=1 dst-address=0.0.0.0/0 gateway=10.10.4.1
add distance=2 dst-address=0.0.0.0/0 gateway=10.10.5.1
```

为实现故障转移，需要有路由在网关故障时立即接管。（这仅在 check-gateway 选项激活时才会发生）

### NAT

```ros
/ip/firewall/nat
add action=masquerade chain=srcnat out-interface=ether_ISP1
add action=masquerade chain=srcnat out-interface=ether_ISP2
```

由于路由决策已经完成，我们只需要规则来为所有出站数据包修正源地址。如果数据包通过 ether\_ISP1 发出，将被 NAT 为 10.10.4.100；如果通过 ether\_ISP2 发出，则被 NAT 为 10.10.5.100。