# PIM-SM

> 本页介绍 MikroTik RouterOS 中的 IP 组播和协议无关组播-稀疏模式（PIM-SM），说明其如何实现跨网络的高效数据共享。内容包括在独立接口之间进行组播路由的基本 PIM-SM 配置，涉及接口设置、PIM 实例创建和 IGMP 集成。

# PIM-SM

IP 组播是一种允许数据通过互联网高效地共享给众多接收者的技术。发送方将数据发送到特定的组播 IP 地址，接收方则表示对接收发送到该地址的数据感兴趣。网络随后负责将数据从发送方传递到接收方。

如果某个组播组的发送方和接收方位于同一本地网段，则此过程不需要路由器。通信可以直接进行，并且可以通过使用 [IGMP 侦听](../../../bridging-and-switching/user-guides/bridge-igmp-mld-snooping.md) 交换机来增强此过程。但是，如果发送方和接收方位于不同的网段，则必须使用组播路由协议来建立它们之间的数据传输路径。

协议无关组播-稀疏模式（PIM-SM 或 PIM）使 RouterOS 能够支持跨网络区域的组播流。PIM 代表协议无关组播，意味着它不依赖于任何特定的单播路由。SM 代表稀疏模式，这意味着特定的控制消息确保数据仅传送到存在需要它的接收者的网段。除了管理网段间数据传输的路由协议外，路由器还需要一种方法来发现其直连网段上的本地接收者。对于 IPv4，这通过互联网组管理协议（IGMP）实现，对于 IPv6，则通过组播监听发现（MLD）实现。

![](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/multicast/img/pim-sm-01.webp)

:::info
RouterOS v7 在主要的 **system** 软件包中提供了 PIM-SM 配置。较旧的 RouterOS 版本需要安装额外的 **multicast** 软件包才能使用 PIM-SM。有关 [软件包](../../../getting-started/installation-and-upgrade/packages.md) 的更多详细信息，请参阅。

该功能在 SMIPS 设备（hAP lite、hAP lite TC 和 hAP mini）上不受支持。
:::

## 单设备上的基本组播路由

设想这样一个场景：您有一台路由器，带有两个接口，即 ether1 和 ether2，并且每个接口都设置在独立的网络中。通常，路由器会创建直连路由，两个网络上的主机将能够使用单播流量进行通信。但是，如果您希望在这些网络之间启用组播通信，则需要单独配置组播路由，否则它将无法工作。在此场景中，我们将创建一个简单的配置。这涉及创建一个 PIM 实例并配置所需的接口。

![](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/multicast/img/pim-sm-02.webp)

首先，确保在路由器的接口上设置了 IP 地址。

```ros
/ip/address
add address=192.168.10.1/24 interface=ether1 network=192.168.10.0
add address=192.168.20.1/24 interface=ether2 network=192.168.20.0
```

配置一个 PIM 实例。对于此示例，默认设置应该可以正常工作。

```ros
/routing/pimsm/instance
add name=pimsm-instance-1
```

为将接收组播流量的接口添加 PIM 接口模板。

```ros
/routing/pimsm/interface-template
add interfaces=ether1 instance=pimsm-instance-1
```

在 ether2 上配置一个 IGMP 查询器，以便 PIM 实例能够了解本地组成员关系。

```ros
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether2
```

现在，路由器开始监听 IGMP 成员资格报告（客户端加入消息），并将组播流量路由到有兴趣接收它的客户端。

要测试此配置，您可以使用 RouterOS [流量生成器](../../../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) 配置一个组播发送方，并使用 [GMP](./group-management-protocol.md) 配置一个 IGMP 客户端。

```ros
# 组播发送方
/ip/address
add address=192.168.10.10/24 interface=ether1 network=192.168.10.0
/tool/traffic-generator/packet-template
add interface=ether1 ip-dst=229.1.1.2 mac-dst=01:00:5E:01:01:02/FF:FF:FF:FF:FF:FF name=multicast
/tool/traffic-generator/quick tx-template=multicast mbps=10

# 组播客户端
/ip/address
add address=192.168.20.10/24 interface=ether1 network=192.168.20.0
/routing/gmp
add disabled=no groups=229.1.1.2 interfaces=ether1
```

要验证组播流量是否被正确路由，请监控客户端接口上的接收数据包计数器，或使用 [Torch](../../../diagnostics-monitoring-and-troubleshooting/torch.md) 或 [数据包嗅探器](../../../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) 等工具。

还可以在路由器上监控活动的组播组：

```ros
/routing/pimsm/uib-g/print
Columns: INSTANCE, GROUP
# INSTANCE          GROUP    
0 pimsm-instance-1  229.1.1.2

/routing/pimsm/uib-sg/print
Flags: K - KEEPALIVE; S - SPT-BIT
Columns: INSTANCE, GROUP, SOURCE
#    INSTANCE          GROUP      SOURCE       
0 KS pimsm-instance-1  229.1.1.2  192.168.10.10

```

## 使用静态 RP 的组播路由

在接下来的示例中，我们将使用多台 PIM 路由器，如下方图表所示。PIM-SM 使用共享树，为了实现这一点，我们需要指定一个特定节点作为组播根分发点。在 PIM 中，该路由器称为汇聚点（RP）。在 PIM 中有多种选择 RP 的方法，例如引导路由器（BSR）方法。但是，对于此示例，我们将使用一种称为静态 RP 配置的简单方法。这意味着管理员可以为特定的组播组手动指定一个或多个 RP。

![](https://manual.mikrotik.com/docs/user-guides/routing-and-networking-protocols/multicast/img/pim-sm-03.webp)

首先，我们需要配置 IP 地址并设置单播路由。在此示例中，我们将使用 OSPF 在路由器之间交换路由信息。有关 [OSPF](../unicast/ospf/index.md) 的更多详细信息，请参阅。

```ros
# R1 汇聚点：
/ip/address
add address=10.0.0.1 interface=lo network=10.0.0.1
add address=10.0.1.1/24 interface=ether2 network=10.0.1.0
add address=10.0.2.1/24 interface=ether3 network=10.0.2.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.1
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether2,ether3

# R2：
/ip/address
add address=10.0.0.2 interface=lo network=10.0.0.2
add address=10.0.1.2/24 interface=ether1 network=10.0.1.0
add address=192.168.20.1/24 interface=ether12 network=192.168.20.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.2
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether1,ether12

# R3：
/ip/address
add address=10.0.0.3 interface=lo network=10.0.0.3
add address=10.0.2.3/24 interface=ether1 network=10.0.2.0
add address=192.168.30.1/24 interface=ether12 network=192.168.30.0
/routing/ospf/instance
add disabled=no name=ospf-instance-1 router-id=10.0.0.3
/routing/ospf/area
add disabled=no instance=ospf-instance-1 name=ospf-area-1
/routing/ospf/interface-template
add area=ospf-area-1 disabled=no interfaces=lo,ether1,ether12
```

与之前单路由器的示例一样，我们需要在所有路由器上配置 PIM 实例并添加必要的接口。

```ros
# R1 汇聚点：
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether2,ether3

# R2：
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether1,ether12
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether12

# R3：
/routing/pimsm/instance
add disabled=no name=pimsm-instance-1
/routing/pimsm/interface-template
add instance=pimsm-instance-1 interfaces=lo,ether1,ether12
/routing/pimsm/igmp-interface-template
add instance=pimsm-instance-1 interfaces=ether12

```

现在，让我们查看一下我们的 PIM 邻居及其当前状态。在 R1 上有两个邻居，而在 R2 和 R3 上各只有一个邻居。

```ros
# R1 汇聚点：
/routing/pimsm/neighbor/print
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#    INSTANCE          ADDRESS          PRIORITY
0 RJ pimsm-instance-1  10.0.1.2%ether2  1       
1 RJ pimsm-instance-1  10.0.2.3%ether3  1       

# R2：
/routing/pimsm/neighbor/print 
Flags: R - DESIGNATED-ROUTER; J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#    INSTANCE          ADDRESS          PRIORITY
0  J pimsm-instance-1  10.0.1.1%ether1  1       

# R3：
/routing/pimsm/neighbor/print 
Flags: J - JOIN-TRACKING
Columns: INSTANCE, ADDRESS, PRIORITY
#   INSTANCE          ADDRESS          PRIORITY
0 J pimsm-instance-1  10.0.2.1%ether1  1       

```

最后，我们将选择一台路由器作为我们的汇聚点（RP）。我们将在所有 PIM 路由器上配置 R1 的环回 IP 地址。确保每台路由器都有正确的路由信息以到达 R1 的环回地址，这一点很重要。

```ros
# R1 汇聚点：
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1

# R2：
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1

# R3：
/routing/pimsm/static-rp
add address=10.0.0.1 instance=pimsm-instance-1
```