# Layer7

> MikroTik RouterOS 中的 Layer7 协议检测会在网络流量流中搜索模式，收集初始数据包以识别特定协议。它需要针对双向流量进行仔细配置，且资源消耗较大，并附有关于过度使用的警告。示例配置演示了如何匹配 RDP 和 Telnet 协议，同时管理内存使用。

# Layer7

Layer7 协议是一种在 ICMP/TCP/UDP 流中搜索模式的方法。

:::warning
L7 匹配器非常消耗资源。请仅将此功能用于非常特定的流量。不建议将 L7 匹配器用于通用流量，例如阻止网页。这几乎永远不会正确工作，并且您的设备会耗尽资源，试图捕获所有流量。请使用其他功能按 URL 阻止网页。
:::

L7 匹配器会收集连接的**前 10 个数据包**或连接的**前 2KB** 数据，并在收集的数据中搜索模式。如果在收集的数据中未找到该模式，匹配器将停止进一步检查。分配的内存将被释放，协议被视为**未知**。您应考虑到，大量连接将显著增加内存和 CPU 使用率。为避免这种情况，请添加常规防火墙匹配器以减少重复传递给 layer-7 过滤器的数据量。

另一个要求是 layer7 匹配器必须看到流量的两个方向（传入和传出）。为满足此要求，l7 规则应设置在 **forward** 链中。如果规则设置在 **input/prerouting** 链中，则**必须**在 **output/postrouting** 链中也设置相同的规则，否则收集的数据可能不完整，导致模式匹配错误。

:::danger
Layer 7 匹配器不区分大小写！
:::

与 RouterOS 兼容的 L7 模式示例可在 [l7-filter 项目页面](https://l7-filter.sourceforge.net/Pattern-HOWTO) 上找到。

:::warning
在某些情况下，当 layer 7 正则表达式无法执行时，RouterOS 将记录 *topic=firewall, warning* 以及一条说明问题的错误消息！
:::

## 示例

#### 简单的 L7 使用示例

首先，将 Regexp 字符串添加到协议菜单中，以定义您要查找的字符串。在此示例中，我们将使用一个模式来匹配 RDP 数据包。

```ros
/ip/firewall/layer7-protocol
add name=rdp regexp="rdpdr.*cliprdr.*rdpsnd"
```

然后，在防火墙中使用定义的协议。

```ros
/ip/firewall/filter

# 添加几个已知协议以减少内存使用
add action=accept chain=forward comment="" disabled=no port=80 protocol=tcp
add action=accept chain=forward comment="" disabled=no port=443 protocol=tcp

# 添加 l7 匹配器
add action=accept chain=forward comment="" disabled=no layer7-protocol=\
    rdp protocol=tcp
```

如您所见，在 l7 规则之前，我们添加了几条常规规则，这些规则将匹配已知流量，从而减少内存使用。

#### input 链中的 L7

在此示例中，我们将尝试匹配连接到我们路由器的 telnet 协议。

```ros
/ip/firewall/layer7-protocol/add comment="" name=telnet regexp="^\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe].\\xff[\\xfb-\\xfe]"
```

请注意，我们需要两个方向，这就是为什么我们还需要在 output 链中设置 l7 规则以查看传出数据包的原因。

```ros
/ip/firewall/filter

add action=accept chain=input comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp

add action=passthrough chain=output comment="" disabled=no layer7-protocol=telnet \
    protocol=tcp
```

#### YouTube 匹配器

:::warning
当用户登录时，YouTube 将使用 HTTPS，这意味着 L7 将无法匹配此流量。只有未加密的 HTTP 才能被匹配。
:::

```ros
/ip/firewall/layer7-protocol
add name=youtube regexp="(GET \\/videoplayback\\\?|GET \\/crossdomain\\.xml)"
```