# Bonding 示例

> 本页演示如何使用 MikroTik RouterOS 在两条无线链路上绑定 EoIP 隧道，展示创建绑定接口及验证流量在链路间分布的配置步骤。

# Bonding 示例

## 在两条无线链路上绑定 EoIP 隧道

本示例展示如何将多个网络接口聚合为单一通道。具体而言，演示如何聚合多个虚拟（EoIP）接口以实现最大吞吐量（MT），并重点强调可用性。

### 网络拓扑

路由器 R1 和 R2 通过无线链路互连。两侧的无线接口均已分配 IP 地址。

### ![](https://manual.mikrotik.com/docs/high-availability-solutions/user-guides/img/bonding-examples-01.webp)配置

Bonding 仅可用于 OSI 第二层（以太网层）连接。因此，我们需要在每条无线链路上创建 EoIP 接口。操作如下：

在路由器 R1 上：

```ros
/interface/eoip/add remote-address=10.0.1.1 tunnel-id=1 
/interface/eoip/add remote-address=10.2.2.1 tunnel-id=2
```

在路由器 R2 上：

```ros
/interface/eoip/add remote-address=10.0.1.2 tunnel-id=1 
/interface/eoip/add remote-address=10.2.2.2 tunnel-id=2
```

第二步是添加绑定接口，并将 EoIP 接口指定为从属接口：

R1：

```ros
/interface/bonding/add slaves=eoip-tunnel1,eoip-tunnel2 mode=balance-rr
```

R2：

```ros
/interface/bonding/add slaves=eoip-tunnel1,eoip-tunnel2 mode=balance-rr
```

最后一步是为绑定接口添加 IP 地址：

R1：

```ros
/ip/address/add address=192.168.0.1/24 interface=bonding1
```

R2：

```ros
/ip/address/add address=192.168.0.2/24 interface=bonding1
```

### 测试配置

现在两台路由器可以通过 192.168.0.0/24 网络中的地址相互访问。要验证绑定接口的功能，请执行以下操作：

R1：

```ros
/interface/monitor-traffic eoip-tunnel1,eoip-tunnel2
```

R2：

```ros
/tool/bandwidth-test 192.168.0.1 direction=transmit
```

您应看到流量在两个 EoIP 接口间均匀分布：

```ros
/int monitor-traffic eoip-tunnel1,eoip-tunnel2              
    received-packets-per-second: 685      685                                  
       received-bits-per-second: 8.0Mbps  8.0Mbps                              
        sent-packets-per-second: 21       20                                   
           sent-bits-per-second: 11.9kbps 11.0kbps                             
    received-packets-per-second: 898      899                                  
       received-bits-per-second: 10.6Mbps 10.6Mbps                             
        sent-packets-per-second: 20       21                                   
           sent-bits-per-second: 11.0kbps 11.9kbps                             
    received-packets-per-second: 975      975                                  
       received-bits-per-second: 11.5Mbps 11.5Mbps                             
        sent-packets-per-second: 22       22                                   
           sent-bits-per-second: 12.4kbps 12.3kbps                             
    received-packets-per-second: 980      980                                  
       received-bits-per-second: 11.6Mbps 11.6Mbps                             
        sent-packets-per-second: 21       21                                   
           sent-bits-per-second: 11.9kbps 11.8kbps                             
    received-packets-per-second: 977      977                                  
       received-bits-per-second: 11.6Mbps 11.5Mbps                             
        sent-packets-per-second: 21       21                                   
           sent-bits-per-second: 11.9kbps 11.8kbps                             
-- [Q quit|D dump|C-z pause]
```

### 链路监控

不难发现，使用上述配置时，一旦任何单条链路发生故障，绑定接口的吞吐量便会崩溃。这是因为未执行链路监控，导致绑定驱动无法感知底层链路的问题。在大多数绑定配置中，启用链路监控是必需的。要启用 ARP 链路监控，请执行以下操作：

#### R1

```ros
/interface/bonding/set bonding1 link-monitoring=arp arp-ip-targets=192.168.0.2
```

#### R2

```ros
/interface/bonding/set bonding1 link-monitoring=arp arp-ip-targets=192.168.0.1
```