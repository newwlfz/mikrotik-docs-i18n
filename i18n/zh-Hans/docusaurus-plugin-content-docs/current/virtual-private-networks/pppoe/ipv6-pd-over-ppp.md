# 通过 PPP 进行 IPv6 前缀委派

> 本页面演示了如何在 RouterOS 中通过 PPPoE 配置 IPv6 前缀委派，展示了如何在服务器和客户端上设置 DHCPv6-PD 池，包括接口配置和动态前缀委派的验证。

# 通过 PPP 进行 IPv6 前缀委派

本示例演示了如何设置 PPPoE 服务器和客户端以使用 IPv6 前缀委派。

IPv6 前缀可以通过 PPP 接口进行委派。当客户端连接时，PPP 将自动添加一个动态的 [DHCPv6-PD 服务器](../../network-management/dhcp.md#dhcpv6-server)。这允许在 PPP 接口上运行 DHCPv6 客户端。

### 配置

### 服务器

PPP 配置文件下的 dhcpv6-pd-pool 参数用于启用 PPP-PD。PPP 将使用指定的 [IPv6 池](../../cli-reference/ipv6/pool.md) 来创建动态 DHCP 服务器。

因此，第一步是添加一个 IPv6 池：

```ros
/ipv6/pool
add name=myPool prefix=2001:db8:7501:ff00::/60 prefix-length=62
```

现在我们可以配置一个 PPP 配置文件并添加一个 PPPoE 服务器

```ros
/ppp/profile/set default dhcpv6-pd-pool=myPool

/interface/pppoe-server/server 
add service-name=test interface=ether1
```

### 客户端

在客户端，我们需要设置 PPPoE 客户端接口并在其上运行 DHCP 客户端。

```ros
/interface/pppoe-client
add name=client-test interface=ether1 user=a1 service-name=test

/ipv6/dhcp-client 
add interface=client-test pool-name=ppp-test pool-prefix-length=64
```

### 状态测试

在服务器端，检查是否添加了动态 DHCP 服务器以及前缀是否绑定到特定客户端：

```ros
[admin@RB1100] /ipv6/dhcp-server> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    NAME              INTERFACE            ADDRESS-POOL            LEASE-TIME
 0 D  <pppoe-a1>        <pppoe-a1>           myPool                  3d        

[admin@RB1100] /ipv6/dhcp-server/binding> print 
Flags: X - disabled, D - dynamic 
 #   ADDRESS                                        DU       IAID SER.. STATUS 
 1 D 2001:db8:7501:ff04::/62                                  247 <pp.. bound  
 
```

在客户端，检查 DHCP 客户端是否已绑定以及池是否已添加：

```ros
[admin@x86-test] /ipv6/dhcp-client> print 
Flags: D - dynamic, X - disabled, I - invalid 
 #    INTERFACE           STATUS        PREFIX                            EXPIRES-AFTER  
0    client-test          bound         2001:db8:7501:ff04::/62           2d23h18m17s  

[admin@x86-test] /ipv6/pool> print 
Flags: D - dynamic 
 #   NAME                        PREFIX                                   PREFIX-LENGTH
 0 D ppp-test                    2001:db8:7501:ff04::/62                             64
```