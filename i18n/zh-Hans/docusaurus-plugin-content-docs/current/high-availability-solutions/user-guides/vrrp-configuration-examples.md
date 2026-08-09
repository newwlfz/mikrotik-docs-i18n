# VRRP 配置示例

> 本页面提供 MikroTik RouterOS 的 VRRP 基本配置示例，演示如何在两台路由器之间设置主备冗余，实现 IP 地址共享及故障切换期间的 ARP 表更新。

# VRRP 配置示例

## 基本设置

以下是 VRRP 基本配置示例。

:::info
注意

建议所有使用相同 VRID 实现 VRRP 的设备采用相同版本的 RouterOS。

:::

![](https://manual.mikrotik.com/docs/high-availability-solutions/user-guides/img/vrrp-configuration-examples-01.webp)

根据此配置，只要主路由器 R1 正常工作，所有发往外部网络的流量都将指向 R1。但一旦 R1 发生故障，R2 将接管成为主路由器，并开始处理转发到与 IP(R1) 关联接口的数据包。在此设置中，路由器 R2 在备份期间完全处于空闲状态。

## 配置

### R1 配置

```ros
/ip/address/add address=192.168.1.10/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49 priority=254
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

### R2 配置

```ros
/ip/address/add address=192.168.1.20/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49
/ip/address/add address=192.168.1.1/32 interface=vrrp1
```

### 测试

首先，检查两台路由器在 VRRP 接口上是否具有正确的标志。在路由器 R1 上应显示如下内容。

```ros
/interface/vrrp/print detail
 0   RM name="vrrp1" mtu=1500 mac-address=00:00:5E:00:01:31 arp=enabled interface=ether1 vrid=49 
        priority=254 interval=1 preemption-mode=yes authentication=none password="" on-backup="" 
        on-master="" version=3 v3-protocol=ipv4
```

在路由器 R2 上应显示：

```ros
/interface/vrrp/print detail
 0    B name="vrrp1" mtu=1500 mac-address=00:00:5E:00:01:31 arp=enabled interface=ether1 vrid=49 
        priority=100 interval=1 preemption-mode=yes authentication=none password=""
         on-backup="" on-master="" version=3 v3-protocol=ipv4
```

如您所见，两台路由器上的 VRRP 接口 MAC 地址完全相同。现在，要检查 VRRP 是否正常工作，请尝试从客户端 ping 虚拟地址并检查 ARP 条目：

```ros
[admin@client] > /ping 192.168.1.1
192.168.1.1 64 byte ping: ttl=64 time=10 ms
192.168.1.1 64 byte ping: ttl=64 time=8 ms
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 8/9.0/10 ms
```

现在拔掉路由器 R1 上的 ether1 网线。R2 将成为 VRRP 主路由器，客户端上的 ARP 表不会发生变化，但流量将开始通过 R2 路由器传输。

:::info
如果 VRRP 与反向路径过滤（Reverse Path Filtering）一起使用，建议将 `rp-filter` 设置为 `loose`，否则 VRRP 接口可能无法访问。

:::

## 负载分担

在基本配置示例中，R2 在备份状态下完全处于空闲状态。这种行为可能被视为对宝贵资源的浪费。在这种情况下，可以将 R2 路由器设置为部分客户端的网关。
此配置的明显优势是建立了负载分担方案。但这样做，R2 路由器无法受到当前 VRRP 设置的保护。
要使此设置生效，我们需要两个虚拟路由器。

![](https://manual.mikrotik.com/docs/high-availability-solutions/user-guides/img/vrrp-configuration-examples-02.webp)

V1 虚拟路由器的配置将与基本示例中的配置相同——R1 为主路由器，R2 为备份路由器。在 V2 中，主路由器为 R2，备份路由器为 R1。
通过此配置，我们在 R1 和 R2 之间建立了负载分担；此外，我们通过让两台路由器互为备份来创建保护设置。

## 配置

### R1 配置

```ros
/ip/address/add address=192.168.1.1/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49 priority=254
/interface/vrrp/add interface=ether1 vrid=77 
/ip/address/add address=192.168.1.253/32 interface=vrrp1
/ip/address/add address=192.168.1.254/32 interface=vrrp2
```

### R2 配置

```ros
/ip/address/add address=192.168.1.2/24 interface=ether1
/interface/vrrp/add interface=ether1 vrid=49
/interface/vrrp/add interface=ether1 vrid=77 priority=254
/ip/address/add address=192.168.1.253/32 interface=vrrp1
/ip/address/add address=192.168.1.254/32 interface=vrrp2
```

## 无抢占的 VRRP

每当具有更高优先级的路由器可用时，它就会成为主路由器。有时这不是期望的行为，可以通过在 VRRP 配置中设置 `preemption-mode=no` 来关闭此功能。

### 配置

我们将使用与基本示例相同的设置。唯一的区别是在配置过程中设置 preemption-mode=no。这可以通过修改现有配置轻松完成：

```ros
/interface/vrrp/set [find] preemption-mode=no
```

### 测试

尝试关闭 R1 路由器，R2 将成为主路由器，因为它在可用路由器中具有最高优先级。

现在重新开启 R1 路由器，您将看到 R2 路由器继续作为主路由器，即使 R1 具有更高的优先级。