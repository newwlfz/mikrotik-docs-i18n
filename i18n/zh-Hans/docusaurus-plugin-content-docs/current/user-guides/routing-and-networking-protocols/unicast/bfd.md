# BFD

> 双向转发检测（BFD）是一种用于检测网络路径故障的低延迟协议，独立于路由协议运行。它使用UDP封装，支持可配置端口，并支持多跳会话，但目前不支持回声模式和认证。配置涉及在RouterOS CLI中指定接口、地址和VRF。

# BFD

**双向转发检测**（**BFD**）是一种低开销、短时长的协议，用于检测两个转发引擎之间双向路径中的故障。这包括物理接口、子接口、数据链路，以及尽可能包括转发引擎本身，且具有极低的延迟。它独立于介质、数据协议和路由协议运行。

**BFD** 是一种Hello协议，用于检查双向邻居可达性。它提供亚秒级链路故障检测，并且不像协议Hello定时器那样特定于任何路由协议。

**控制**数据封装在目标端口为3784的**UDP**帧中；端口4784用于多跳路径。源端口范围为49152–65535。  
**回声**封装在目标端口为3785的UDP帧中。

标准与技术：

- [RFC 5880 双向转发检测（BFD）](https://datatracker.ietf.org/doc/rfc5880/)
- [RFC 5881 IPv4和IPv6的BFD](https://datatracker.ietf.org/doc/rfc5881/)
- [RFC 5882 BFD的通用应用](https://datatracker.ietf.org/doc/rfc5882/)
- [RFC 5883 多跳路径的双向转发检测（BFD）](https://datatracker.ietf.org/doc/rfc5883/)

## 尚不支持的功能

- 回声模式。
- 为IP路由网关启用BFD。
- 认证。

## 配置

允许或禁止**BFD**会话可以在[`/routing/bfd/configuration`](../../../cli-reference/routing/bfd.md#routingbfdconfiguration)菜单中完成。例如：

```ros
/routing bfd configuration
add interfaces=sfp12 forbid-bfd=yes
add interfaces=static
```

配置条目按顺序敏感，这意味着在上述示例中，我们明确禁止了"sfp12"接口上的BFD会话（使用[`forbid-bfd`](../../../cli-reference/routing/bfd.md#forbid-bfd)），并允许属于"static"接口列表的其余接口上的BFD会话。

为了能够过滤多跳会话，可以使用[`addresses`](../../../cli-reference/routing/bfd.md#addresses)或[`address-list`](../../../cli-reference/routing/bfd.md#address-list)属性来匹配目标地址，以及相应的[`vrf`](../../../cli-reference/routing/bfd.md#vrf)，如果会话不在"main" VRF中运行。

```ros
/ip firewall address-list
add address=10.155.255.183 list=bgp_allow_bfd
add address=10.155.255.217 list=bgp_allow_bfd

/routing bfd configuration
add addresses=111.111.0.0/16 vrf=vrf1
add address-list=bgp_allow_bfd
```

配置中未明确列出的任何内容默认被禁止。

### BFD与BGP

要为[BGP](./bgp/index.md)会话启用BFD，请在[`/routing/bgp/connection`](../../../cli-reference/routing/bgp.md#routingbgpconnection)菜单中的所需条目上设置[`use-bfd`](../../../cli-reference/routing/bgp.md#use-bfd)。

BGP会话输出显示关联的BFD会话何时关闭：

```ros
[admin@dr_02_BGP_MUM] /routing/bgp/session> print 
Flags: E - established 
 0 E ;;; BFD session down
     name="ovpn_test1-1" 
     remote.address=111.111.11.11@vrf1 .as=65530 .id=10.155.101.217 
     .capabilities=mp,rr,as4 .hold-time=infinity .messages=40717 
     .bytes=3436281 .eor="" 
     local.address=111.111.11.12@vrf1 .as=555 .id=111.111.11.12 
     .capabilities=mp,rr,gr,as4 .messages=1 .bytes=19 .eor="" 
     output.procid=20 
     input.procid=20 .filter=bgp-in ebgp 
     hold-time=infinity use-bfd=yes uptime=3s210ms 
     last-started=2023-05-19 09:54:04 prefix-count=3853 
```

### BFD与OSPF

要为[OSPF](./ospf/index.md)邻居启用BFD，请在[`/routing/ospf/interface-template`](../../../cli-reference/routing/ospf.md#routingospfinterface-template)菜单中的所需条目上设置[`use-bfd`](../../../cli-reference/routing/ospf.md#use-bfd)。

## 会话状态

在[`/routing/bfd/session`](../../../cli-reference/routing/bfd.md#routingbfdsession)菜单中查看当前会话的状态：

```ros
[admin@dr_02_BGP_MUM] /routing/bfd/session> print 
Flags: U - up, I - inactive 
 0 I ;;; BFD forbidden for destination address
     multihop=yes remote-address=10.155.101.183 local-address="" desired-tx-interval=0ms required-min-rx=0ms 
     multiplier=0 

 1   multihop=no remote-address=111.111.11.11%ovpn-out1@vrf1 local-address=111.111.11.12@vrf1 state=down 
     state-changes=0 desired-tx-interval=200ms required-min-rx=200ms remote-min-rx=1us multiplier=5 
     packets-rx=0 packets-tx=7674 
```

BFD选择本地发送间隔和远程最小接收间隔中的较大值作为期望发送间隔。如果会话未建立，期望的最小发送间隔默认为1秒。