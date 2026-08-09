# 地址列表

> 本页说明如何在 MikroTik RouterOS 中创建和管理用于防火墙规则的地址列表，包括添加静态条目以及基于连接尝试的动态条目，并设置超时时间以控制流量阻断时长。

# 地址列表

以下示例创建了一个动态地址列表，用于记录尝试连接路由器端口 23（telnet）的客户端，并在 5 分钟内丢弃来自这些客户端的后续所有流量。此外，该地址列表还将包含一个静态地址列表条目 192.0.34.166/32（[www.example.com](http://www.example.com)）：

```ros
/ip/firewall/address-list/add list=drop_traffic address=192.0.34.166/32
```

```ros
/ip/firewall/address-list/print
Flags: X - disabled, D - dynamic
 #   LIST         ADDRESS
 0   drop_traffic 192.0.34.166
```

```ros
/ip/firewall/mangle/add action=add-src-to-address-list address-list=drop_traffic address-list-timeout=5m chain=prerouting dst-port=23 protocol=tcp
/ip/firewall/filter/add action=drop chain=input src-address-list=drop_traffic
```

```ros
/ip/firewall/address-list/print
Flags: X - disabled, D - dynamic
 #   LIST         ADDRESS
 0   drop_traffic 192.0.34.166
 1 D drop_traffic 1.1.1.1
 2 D drop_traffic 10.5.11.8
```

从最后一条打印命令的输出可以看出，地址列表中出现了两个新的动态条目（标记为“D”状态）。具有这些 IP 地址的主机尝试向路由器发起 telnet 会话，随后被过滤规则丢弃。