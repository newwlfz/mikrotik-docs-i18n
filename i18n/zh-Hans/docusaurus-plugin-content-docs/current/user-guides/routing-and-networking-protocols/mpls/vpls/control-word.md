# 控制字

> VPLS在RouterOS中使用控制字（CW）进行数据包的分片与重组，增加4字节开销以应对L2MTU限制。CW字段包括标志、分片指示、长度及用于数据包跟踪的序列号，其使用由`use-control-word`参数控制。

# 控制字

VPLS允许远程站点通过分组交换网络（PSN）上的**伪线（PW）**隧道连接站点，从而共享以太网广播域。由于VPLS封装增加了额外开销，LSP中的每个接口都应能够传输足够大的数据包。

每个以太网芯片组在可传输的最大数据包大小上都有硬件限制。即使到现在，仍有一些以太网仅支持单个VLAN标签，这意味着不含以太网头和校验和的最大数据包大小（L2MTU）为1504字节。显然，这不足以在不分片的情况下转发VPLS封装的以太网帧（至少需要支持1526 L2MTU）。有关RouterBOARD上支持的最大L2MTU，请参阅[RouterOS中的MTU](../../../../hardware/mtu-in-routeros.md)。

由于并非所有RouterBOARD都支持足够的L2MTU来传输不分片的VPLS封装数据包，RouterOS根据RFC 4623增加了伪线分片与重组（PWE3）支持，使用4字节的**控制字（CW）**。

## 控制字的使用

在RouterOS中，控制字用于VPLS隧道内的数据包分片与重组。这是通过利用可选的**控制字（CW）**实现的。CW位于PW标签（解复用器）和数据包负载之间，增加了4字节的额外开销。

:::warning
未实现乱序（OOO）数据包的重排序，乱序分片将被丢弃
:::

CW的使用由VPLS配置中的`use-control-word`参数控制。

![](img/VPLS_CW_light.jpg#gh-light-mode-only)
![](img/VPLS_CW_dark.png#gh-dark-mode-only)

如您所见，**控制字**分为5个字段：

- 0000 - 4位，标识数据包为PW（非IP）。
- Flags - 4位。
- Frag - 2位，指示负载分片情况。
- Len - 6位。
- Seq - 16位序列号，用于检测数据包丢失/乱序。

根据RFC，序列号的生成和处理是可选的。