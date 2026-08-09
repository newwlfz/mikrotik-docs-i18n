# 策略路由

> RouterOS 中的策略路由允许根据条件将流量引导至特定网关，利用自定义路由表和规则实现。它支持通过防火墙 mangle 标记或基本路由规则配置进行动态路由决策，以实现流量控制。

# 策略路由

策略路由将符合特定条件的流量引导至指定网关。可用于强制特定客户或协议（如 HTTP 流量）始终使用特定网关，也可将本地流量和海外流量分别路由至不同网关。

RouterOS 提供以下组件用于策略路由：

- 路由表。
- 路由规则。
- 防火墙 mangle 标记。

## 路由表

路由器可拥有多个路由表，每个路由表针对同一目的地配置不同网关的独立路由。

可在 `/routing/table` 菜单中查看和配置路由表。

默认情况下，RouterOS 仅包含 **main** 路由表：

```text
[admin@rack1_b33_CCR1036] /routing/table> print
Flags: D - dynamic; X - disabled, I - invalid; U - used
0 D name="main" fib

```

在配置中使用自定义路由表之前，需先在此菜单中定义。

考虑一个基本示例：两个网关分别为 172.16.1.1 和 172.16.2.1，在名为 **myTable** 的路由表中为 8.8.8.8 配置一条使用网关 172.16.2.1 的路由：

```ros
/routing/table/add name=myTable fib
/ip/route/add dst-address=8.8.8.8 gateway=172.16.1.1
/ip/route/add dst-address=8.8.8.8 gateway=172.16.2.1@main routing-table=myTable
```

:::tip
用户创建的路由表若要能解析目的地，主路由表也应能解析该目的地。
:::

在此示例中，**main** 路由表也应包含到 8.8.8.8 的路由，或至少包含一条默认路由。由于 DHCP 会动态添加默认路由以确保安全，请将 8.8.8.8 显式添加到主路由表中。

```text
[admin@rack1_b33_CCR1036] /ip/route> print detail Flags: D - dynamic; X - disabled, I - inactive, A - active;
c - connect, s - static, r - rip, b - bgp, o - ospf, d - dhcp, v - vpn, m - modem, y - cop
y;
H - hw-offloaded; + - ecmp
   DAd   dst-address=0.0.0.0/0 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10
         vrf-interface=ether8 suppress-hw-offload=no

 0  As   dst-address=8.8.8.8/32 routing-table=main pref-src="" gateway=172.16.1.1
         immediate-gw=172.16.1.1%ether8 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

    DAc   dst-address=172.16.1.0/24 routing-table=main gateway=ether8 immediate-gw=ether8
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.1.2%ether8

    DAc   dst-address=172.16.2.0/24 routing-table=main gateway=ether7 immediate-gw=ether7
         distance=0 scope=10 suppress-hw-offload=no local-address=172.16.2.2%ether7

 1  As   dst-address=8.8.8.8/32 routing-table=myTable pref-src="" gateway=172.16.2.1
         immediate-gw=172.16.2.1%ether7 distance=1 scope=30 target-scope=10 suppress-hw-offload=no

```

上述配置尚不完整。您需要一种方式强制流量使用新路由表。RouterOS 提供两种选项：

- 防火墙 mangle - 对流量的引导条件提供更精细的控制，例如按连接或按数据包进行负载均衡。示例请参见 [防火墙标记](../../firewall-and-quality-of-service/firewall/mangle.md)。
- 路由规则 - 提供一组基本参数，用于快速引导流量。本示例使用路由规则。

除非必要，否则请勿同时使用两种方法。若同时使用 mangle 和路由规则，mangle 默认具有更高优先级。如果 mangle 标记的流量能在路由表中解析，路由规则将不会看到该流量。执行顺序可以[更改](./routing-decision.md#routing-table-lookup)。

:::warning
路由表数量限制为 4096 个唯一表。
:::

## 路由规则

路由规则基于基本参数（如源地址、目的地址、入接口等）引导流量。

在此示例中，选择发往 8.8.8.8 的流量，并防止回退到 **main** 路由表：

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable
```

如果客户连接到 ether4，且仅该客户应将 8.8.8.8 路由至特定网关，请使用以下规则：

```ros
/routing/rule/add dst-address=8.8.8.8 action=lookup-only-in-table table=myTable interface=ether4
```

如果路由表中使用的网关失效，查找将失败，目的地将变得不可达。在主备配置中，可通过将操作从 `lookup-only-in-table` 改为 `lookup`，允许流量回退到 **main** 路由表。

路由规则还可充当基本防火墙。例如，阻止 ether4 上的客户访问 192.168.1.0/24：

```ros
/routing/rule/add dst-address=192.168.1.0/24 interface=ether4 action=drop
```