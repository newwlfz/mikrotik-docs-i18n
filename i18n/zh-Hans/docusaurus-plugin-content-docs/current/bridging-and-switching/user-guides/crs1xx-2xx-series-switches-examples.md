# CRS1xx/2xx 系列交换机示例

> 本页提供 Cloud Router Switch 功能在 CRS1xx/2xx 系列交换机上的配置示例和使用案例，涵盖端口交换、带 VLAN 过滤的管理访问设置以及基于 IP 访问的安全注意事项。

# CRS1xx/2xx 系列交换机示例

---

Cloud Router Switch 功能的基本使用案例和配置示例。

:::info
本文适用于 CRS1xx 和 CRS2xx 系列交换机，不适用于 [采用 Marvell Prestera 交换芯片的 MikroTik 设备](../marvell-prestera-switch-chip-features.md)（例如 CRS3xx 系列交换机）。
:::

## 端口交换

---

要在 CRS1xx/2xx 系列交换机上设置端口交换，请参阅 [桥接硬件卸载](../#bridge-hardware-offloading) 页面。

:::danger
可以通过使用多个启用了硬件卸载的桥接来创建多个隔离的交换组；但这仅在 CRS1xx/2xx 系列交换机上可行。对于更复杂的设置（例如 VLAN 过滤），应改用端口隔离功能。
:::

## 管理访问配置

---

通常，交换机仅应通过内置交换芯片转发数据包，但出于安全原因，不应允许访问设备本身。可以使用设备的串行端口进行管理访问，但在大多数情况下，这种访问方式并不理想，使用 IP 地址进行访问更为合适。在这种情况下，您需要配置管理访问。

在所有类型的管理访问中，都假定端口必须被交换在一起。使用以下命令将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

您还应该为桥接接口分配一个 IP 地址，以便设备可以通过 IP 地址访问（设备也可以通过 MAC 地址访问）：

```ros
/ip/address
add address=192.168.88.1/24 interface=bridge1
```

### 未标记 (Untagged)

如果未启用无效 VLAN 过滤，则已经允许从任何端口使用标记或未标记（**VLAN 0**）流量对设备进行管理访问，尽管这不是一个好做法；这可能会导致安全问题，并且在某些情况下（最常见的是广播类型流量）可能导致设备 CPU 过载。

如果您打算使用无效 VLAN 过滤（您应该这样做），则必须将要访问交换机的端口添加到 VLAN 表中，用于未标记（**VLAN 0**）流量，例如，如果您想从 **ether2** 访问交换机：

```ros
/interface/ethernet/switch/vlan
add vlan-id=0 ports=ether2,switch1-cpu  
```

### 标记 (Tagged)

仅允许标记流量通过特定端口对设备进行管理访问是一种更好的做法。例如，仅允许 **VLAN99** 通过 **ether2** 访问设备，您应首先在 VLAN 表中添加一个条目，该条目将允许所选端口和 CPU 端口（**switch1-cpu**）转发所选 VLAN ID，从而允许管理访问：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,switch1-cpu vlan-id=99
```

从 CPU 发送出的数据包（例如 ping 回复）将不带 VLAN 标签，要解决此问题，您需要指定哪些端口应始终为特定 VLAN ID 发送带有 VLAN 标签的数据包：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,switch1-cpu vlan-id=99
```

在设置有效的 VLAN99 配置后，您可以启用未知/无效 VLAN 过滤，这将不允许通过 VLAN 表中未指定的端口进行管理访问：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether3,ether4,ether5
```

在此示例中，VLAN99 将用于访问设备。必须在桥接上创建 VLAN 接口并为其分配 IP 地址。

```ros
/interface/vlan
add interface=bridge1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.1/24 interface=MGMT
```

## VLAN

---

:::danger 锁定风险
强烈建议在配置 VLAN 之前准备好并测试好串行控制台电缆。错误配置很容易使您无法访问 CPU 或您连接的端口。
:::

:::tip 排除缓存 MAC 地址故障
由于已学习的 MAC 地址，某些更改可能看起来有延迟。如果更改后流量未按预期流动，请刷新单播转发数据库：
`/interface/ethernet/switch/unicast-fdb/flush`
:::

:::info 架构最佳实践
使用多个硬件卸载桥接是实现简单端口隔离的快速方法，但这会限制 CRS 交换芯片上的高级 VLAN 功能。对于高级设置，请为所有端口使用**单个桥接**，配置您的 VLAN，并使用端口隔离配置文件隔离端口组。
:::

### 基于端口的 VLAN

:::warning
对于 CRS3xx 系列设备，您必须使用桥接 VLAN 过滤；您可以在 [桥接 VLAN 过滤](../index.md#bridge-vlan-filtering) 部分阅读更多相关信息。
:::

#### 示例 1（Trunk 和 Access 端口）

![Access Ports](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-01.webp)

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

为每个接入端口指定交换机必须为未标记（VLAN0）流量设置的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

:::warning
在 `/interface/ethernet/switch/ingress-vlan-translation` 下创建条目时，交换芯片将在指定端口的入站帧上添加 VLAN 标签。要在同一端口的出站帧上移除 VLAN 标签，应为相同 VLAN ID 创建 `/interface/ethernet/switch/egress-vlan-tag` 条目，并且仅指定 tagged 端口。如果特定 VLAN 仅在接入端口之间转发，则仍应创建不带任何 tagged 端口的 `/interface/ethernet/switch/egress-vlan-tag` 条目。另一种选择是在 `/interface/ethernet/switch/egress-vlan-translation` 菜单下创建额外条目以设置未标记（VLAN0）流量。
:::

您还必须指定应将哪些 VLAN 以 VLAN 标签发送到 trunk 端口。使用 tagged-ports 属性设置 trunk 端口：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

在 VLAN 表中添加条目，为每个端口和每个 VLAN ID 指定 VLAN 成员资格：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6 vlan-id=200
add ports=ether2,ether7 vlan-id=300
add ports=ether2,ether8 vlan-id=400
```

在设置有效的 VLAN 配置后，您可以启用未知/无效 VLAN 过滤：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

:::warning
可以同时使用内置交换芯片和 CPU 来创建交换机-路由器设置，使设备同时充当交换机和路由器。
:::

#### 示例 2（Trunk 和 Hybrid 端口）

![Hybrid Ports](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-02.webp)

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

为每个接入端口指定交换机必须为未标记（VLAN0）流量设置的 VLAN ID：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

通过将端口指定为 tagged-ports，交换机将始终发送带有相应 VLAN ID 的标记数据包。根据上图添加适当的条目：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2,ether7,ether8 vlan-id=200
add tagged-ports=ether2,ether6,ether8 vlan-id=300
add tagged-ports=ether2,ether6,ether7 vlan-id=400
```

在 VLAN 表中添加条目，为每个端口和每个 VLAN ID 指定 VLAN 成员资格：

```ros
/interface/ethernet/switch/vlan
add ports=ether2,ether6,ether7,ether8 vlan-id=200 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=300 learn=yes
add ports=ether2,ether6,ether7,ether8 vlan-id=400 learn=yes
```

在设置有效的 VLAN 配置后，您可以启用未知/无效 VLAN 过滤：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether2,ether6,ether7,ether8
```

### 基于协议的 VLAN

![Protocol Based VLAN](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-03.webp)

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

为 IP 和 ARP 协议设置 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=arp set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=arp set-customer-vid-for=all new-customer-vid=200
add port=ether2 protocol=ip set-customer-vid-for=all new-customer-vid=0
add port=ether6 protocol=ip set-customer-vid-for=all new-customer-vid=200
```

为 IPX 协议设置 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=ipx set-customer-vid-for=all new-customer-vid=0
add port=ether7 protocol=ipx set-customer-vid-for=all new-customer-vid=300
```

为 AppleTalk AARP 和 AppleTalk DDP 协议设置 VLAN：

```ros
/interface/ethernet/switch/protocol-based-vlan
add port=ether2 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x80F3 set-customer-vid-for=all new-customer-vid=400
add port=ether2 protocol=0x809B set-customer-vid-for=all new-customer-vid=0
add port=ether8 protocol=0x809B set-customer-vid-for=all new-customer-vid=400
```

### 基于 MAC 的 VLAN

:::danger
在内部，基于 MAC 的 VLAN 中的所有 MAC 地址都会被哈希处理。某些 MAC 地址可能具有相同的哈希值，如果哈希值与已加载的 MAC 地址的哈希值匹配，则会阻止 MAC 地址被加载到交换芯片中，因此，建议将基于端口的 VLAN 与基于 MAC 的 VLAN 结合使用。这是一个硬件限制。
:::

![MAC Based VLAN](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-04.webp)

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
```

在接入端口上启用基于 MAC 的 VLAN 转换：

```ros
/interface/ethernet/switch/port
set ether7 allow-fdb-based-vlan-translate=yes
```

在基于 MAC 的 VLAN 表中添加 MAC 到 VLAN 映射条目：

```ros
/interface/ethernet/switch/mac-based-vlan
add src-mac=A4:12:6D:77:94:43 new-customer-vid=200
add src-mac=84:37:62:DF:04:20 new-customer-vid=300
add src-mac=E7:16:34:A1:CD:18 new-customer-vid=400
```

在 ether2 端口上添加 VLAN200、VLAN300 和 VLAN400 标记，将其创建为 VLAN trunk 端口：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=200
add tagged-ports=ether2 vlan-id=300
add tagged-ports=ether2 vlan-id=400
```

此外，在 VLAN 表中添加条目，为每个端口指定 VLAN 成员资格，并启用未知/无效 VLAN 过滤，请参见下面的示例 - 未知/无效 VLAN 过滤。这对于将更多接口添加到桥接的网络设置是必需的，因为它允许定义 VLAN 边界。

### VLAN 间路由

![VLAN Routing](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-05.webp)

VLAN 间路由配置由两个主要部分组成 – 交换芯片中的 VLAN 标记和 RouterOS 中的路由。此配置可通过与 DHCP 服务器、Hotspot、PPP 以及每个 VLAN 的其他功能相结合，用于许多应用。

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
```

为所有 VLAN 在 CPU 端口上设置 VLAN 标记，使数据包在被路由前带有标签：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=switch1-cpu vlan-id=200
add tagged-ports=switch1-cpu vlan-id=300
add tagged-ports=switch1-cpu vlan-id=400
```

添加入站 VLAN 转换规则，以确保在接入端口上完成正确的 VLAN ID 分配：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether6 customer-vid=0 new-customer-vid=200
add ports=ether7 customer-vid=0 new-customer-vid=300
add ports=ether8 customer-vid=0 new-customer-vid=400
```

在桥接接口之上创建 VLAN 接口：

```ros
/interface/vlan
add name=VLAN200 interface=bridge1 vlan-id=200
add name=VLAN300 interface=bridge1 vlan-id=300
add name=VLAN400 interface=bridge1 vlan-id=400
```

:::danger
确保 VLAN 接口是在桥接接口之上创建的，而不是在任何物理接口之上。如果在从属接口上创建 VLAN 接口，则数据包可能无法被正确接收，从而导致路由失败。更详细的信息可以在 [从属接口上的 VLAN 接口](layer2-misconfiguration.md#vlan-interface-on-a-slave-interface) 手册页面中找到。
:::

在创建的 VLAN 接口上添加 IP 地址。在此示例中，将三个 192.168.x.1 地址添加到 VLAN200、VLAN300 和 VLAN400 接口：

```ros
/ip/address
add address=192.168.20.1/24 interface=VLAN200
add address=192.168.30.1/24 interface=VLAN300
add address=192.168.40.1/24 interface=VLAN400
```

### 未知/无效 VLAN 过滤

VLAN 成员资格在 VLAN 表中定义。添加带有 VLAN ID 和端口的条目会使该 VLAN 流量在这些端口上有效。在设置有效的 VLAN 配置后，可以启用未知/无效 VLAN 过滤。此 VLAN 过滤配置示例适用于 VLAN 间路由设置。

```ros
/interface/ethernet/switch/vlan
add ports=switch1-cpu,ether6 vlan-id=200
add ports=switch1-cpu,ether7 vlan-id=300
add ports=switch1-cpu,ether8 vlan-id=400
```

- 选项 1：在特定端口上禁用无效 VLAN 转发（更常见）。

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether6,ether7,ether8
```

- 选项 2：在所有端口上禁用无效 VLAN 转发。

```ros
/interface/ethernet/switch
set forward-unknown-vlan=no
```

:::danger
在启用了未知/无效 VLAN 过滤的单个交换芯片上使用多个桥接可能会导致意外行为。每当使用 VLAN 过滤时，您应始终使用单个桥接配置。如果需要端口隔离，则应使用端口隔离功能，而不是使用多个桥接。
:::

### VLAN 隧道 (Q-in-Q)

此示例涵盖典型的 VLAN 隧道使用案例，其中服务提供商设备添加另一个 VLAN 标签以进行独立转发，同时允许客户使用自己的 VLAN。

:::warning
此示例仅包含服务 VLAN 标记部分。建议另外在端口上设置未知/无效 VLAN 过滤配置。
:::

![QinQ](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-06.webp)

**CRS-1**：服务提供商网络边缘的第一台交换机必须正确识别端口上来自客户 VLAN ID 的流量，并通过入站 VLAN 转换规则分配新的服务 VLAN ID。服务提供商 VLAN 标签的 VLAN trunk 端口配置位于同一个 `egress-vlan-tag` 表中。与基本基于端口的 VLAN 配置的主要区别在于，CRS 交换芯片必须设置为根据服务（*外部*）VLAN ID 而不是客户（*内部*）VLAN ID 进行转发。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether9 hw=yes

/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=200 new-service-vid=400 ports=ether1
add customer-vid=300 new-service-vid=500 ports=ether2

/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether9 vlan-id=400
add tagged-ports=ether9 vlan-id=500

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

**CRS-2**：服务提供商网络中的第二台交换机仅需要交换端口根据服务（*外部*）VLAN ID 而不是客户（*内部*）VLAN ID 进行转发。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether9 hw=yes
add bridge=bridge1 interface=ether10 hw=yes

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

**CRS-3**：第三台交换机的配置与 CRS-1 类似：

- 使用桥接的交换组中的端口。
- 用于在端口上定义新服务 VLAN 分配的入站 VLAN 转换规则。
- 服务提供商 VLAN trunk 的 tagged-ports。
- CRS 交换芯片设置为在交换查找中使用服务 VLAN ID。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether10 hw=yes

/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=200 new-service-vid=400 ports=ether3
add customer-vid=300 new-service-vid=500 ports=ether4

/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether10 vlan-id=400
add tagged-ports=ether10 vlan-id=500

/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

### CVID 堆叠

可以使用 CRS1xx/CRS2xx 系列交换机进行 CVID 堆叠设置。CRS1xx/CRS2xx 系列交换机能够基于具有两个 CVID 标签（双 CVID 标签）的标记数据包的外部标签进行 VLAN 过滤。这些交换机还能够在现有 CVID 标签之上添加另一个 CVID 标签（CVID 堆叠）。例如，在 **ether1** 接收带有 CVID 10 的标记数据包，但要求 **ether2** 发送带有另一个标签 CVID 20（VLAN20 内的 VLAN10）的这些数据包，同时过滤掉任何其他 VLAN 的设置中，必须配置以下内容：

将 **ether1** 和 **ether2** 交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
```

将交换机设置为基于服务标签（0x88a8）过滤 VLAN：

```ros
/interface/ethernet/switch
set bridge-type=service-vid-used-as-lookup-vid
```

为 **ether1** 上带有 CVID 10 标签的数据包添加服务标签 SVID 20：

```ros
/interface/ethernet/switch/ingress-vlan-translation
add customer-vid=10 new-service-vid=20 ports=ether1
```

将 **ether2** 指定为 SVID 20 的 tagged/trunk 端口：

```ros
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether2 vlan-id=20
```

允许 **ether1** 和 **ether2** 转发 SVID 20：

```ros
/interface/ethernet/switch/vlan
add ports=ether1,ether2 vlan-id=20
```

在 **ether2** 上将 SVID EtherType (0x88a8) 覆盖为 CVID EtherType (0x8100)：

```ros
/interface/ethernet/switch/port
set ether2 egress-service-tpid-override=0x8100 ingress-service-tpid-override=0x8100
```

启用未知/无效 VLAN 过滤：

```ros
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1,ether2
```

:::warning
由于交换机设置为基于服务标签查找 VLAN ID，而服务标签被覆盖为不同的 EtherType，因此 VLAN 过滤仅对数据包的外部标签进行；内部标签不被检查。
:::

## 镜像

---

![Mirroring](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-07.webp)

Cloud Router Switch 支持三种类型的镜像。基于端口的镜像可应用于任何交换芯片端口，基于 VLAN 的镜像适用于所有指定的 VLAN，无论交换芯片端口如何，基于 MAC 的镜像复制从单播转发数据库中配置的端口可达的特定设备发送或接收的流量。

### 基于端口的镜像

第一个配置将 ether5 端口设置为 mirror0 分析端口，用于入站和出站镜像。镜像流量将被发送到此端口。从 ether6 端口启用基于端口的入站和出站镜像。

```ros
/interface/ethernet/switch
set ingress-mirror0=ether5 egress-mirror0=ether5

/interface/ethernet/switch/port
set ether6 ingress-mirror-to=mirror0 egress-mirror-to=mirror0
```

### 基于 VLAN 的镜像

第二个示例要求端口在一个组中交换。镜像配置将 ether5 端口设置为 mirror0 分析端口，并设置在进行 VLAN 镜像时使用 mirror0 端口。VLAN 表条目仅对 ether2 和 ether7 端口之间的 VLAN 300 流量启用镜像。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether7 hw=yes

/interface/ethernet/switch
set ingress-mirror0=ether5 vlan-uses=mirror0

/interface/ethernet/switch/vlan
add ports=ether2,ether7 vlan-id=300 learn=yes ingress-mirror=yes
```

### 基于 MAC 的镜像

第三个配置也要求端口作为一个组交换。镜像配置将 ether5 端口设置为 mirror0 分析端口，并设置在进行单播转发数据库镜像时使用 mirror0 端口。单播转发数据库中的条目启用了对来自 ether8 端口的源或目标 MAC 地址为 E7:16:34:A1:CD:18 的数据包的镜像。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether8 hw=yes

/interface/ethernet/switch
set ingress-mirror0=ether5 fdb-uses=mirror0

/interface/ethernet/switch/unicast-fdb
add port=ether8 mirror=yes svl=yes mac-address=E7:16:34:A1:CD:18
```

## 链路聚合 (Trunking)

---

![Trunking 3](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-08.webp)

Cloud Router Switch 中的链路聚合提供静态链路聚合组，具有硬件自动故障转移和负载均衡功能。尚不支持兼容 IEEE802.3ad 和 IEEE802.1ax 的链路聚合控制协议。最多支持 8 个 Trunk 组，每个 Trunk 组最多支持 8 个 Trunk 成员端口。

配置需要一个交换端口组和一个 Trunk 表条目：

```ros
/interface/bridge
add name=bridge1 protocol-mode=none
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes

/interface/ethernet/switch/trunk
add name=trunk1 member-ports=ether6,ether7,ether8
```

此示例还展示了 RouterOS 另一端的正确 bonding 配置：

```ros
/interface/bonding
add name=bonding1 slaves=ether2,ether3,ether4 mode=balance-xor transmit-hash-policy=layer-2-and-3
```

:::danger
桥接 (R)STP 不了解底层的交换机 trunk 配置，某些 trunk 端口可能会进入丢弃或阻塞状态。当 trunk 成员端口连接到其他桥接时，您应该禁用 (R)STP 或过滤掉 trunk 设备之间的任何 BPDU（例如使用 ACL 规则）。
:::

## 每端口 MAC 访问限制

---

禁用 MAC 学习并配置静态 MAC 地址可以控制哪些确切设备可以与 CRS1xx/2xx 交换机通信以及通过它们通信。

配置需要一个交换端口组、在这些端口上禁用 MAC 学习以及静态 FDB 条目：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes learn=no unknown-unicast-flood=no
add bridge=bridge1 interface=ether7 hw=yes learn=no unknown-unicast-flood=no

/interface/ethernet/switch/unicast-fdb
add mac-address=4C:5E:0C:00:00:01 port=ether6 svl=yes
add mac-address=D4:CA:6D:00:00:02 port=ether7 svl=yes

/interface/ethernet/switch/acl
add action=drop src-mac-addr-state=sa-not-found src-ports=ether6,ether7 table=egress
add action=drop src-mac-addr-state=static-station-move src-ports=ether6,ether7 table=egress
```

CRS1xx/2xx 交换机还允许每个端口学习一个动态 MAC，以确保无论 MAC 地址如何，只连接一个最终用户设备：

```ros
/interface/ethernet/switch/port
set ether6 learn-limit=1
set ether7 learn-limit=1
```

## 隔离

---

### 端口级隔离

![Port Level Isolation](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-09.webp)

端口级隔离通常用于私有 VLAN，其中：

- 一个或多个上行链路端口在所有用户之间共享，用于访问网关或路由器。
- 端口组 Isolated Ports 用于访客用户。通信仅通过上行链路端口进行。
- 端口组 Community 0 用于部门 A。允许组成员之间以及通过上行链路端口进行通信。
- 端口组 Community X 用于部门 X。允许组成员之间以及通过上行链路端口进行通信。

Cloud Router Switch 使用端口级隔离配置文件实现私有 VLAN：

- 上行链路端口 – 端口级隔离配置文件 0
- 隔离端口 – 端口级隔离配置文件 1
- Community 0 端口 - 端口级隔离配置文件 2
- Community X (X \<= 30) 端口 - 端口级隔离配置文件 X

**此示例需要一个交换端口组。假设此示例中使用的所有端口都在一个交换组中。**

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
add bridge=bridge1 interface=ether8 hw=yes
add bridge=bridge1 interface=ether9 hw=yes
add bridge=bridge1 interface=ether10 hw=yes
```

端口隔离配置的第一部分是设置上行链路端口 – 为 ether2 设置端口配置文件为 0：

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=0
```

然后继续在所有隔离端口上设置隔离配置文件 1，并为端口隔离配置文件 1 添加通信端口：

```ros
/interface/ethernet/switch/port
set ether5 isolation-leakage-profile-override=1
set ether6 isolation-leakage-profile-override=1

/interface/ethernet/switch/port-isolation
add port-profile=1 ports=ether2 type=dst
```

设置 Community 2 和 Community 3 端口的配置类似：

```ros
/interface/ethernet/switch/port
set ether7 isolation-leakage-profile-override=2
set ether8 isolation-leakage-profile-override=2

/interface/ethernet/switch/port-isolation
add port-profile=2 ports=ether2,ether7,ether8 type=dst

/interface/ethernet/switch/port
set ether9 isolation-leakage-profile-override=3
set ether10 isolation-leakage-profile-override=3

/interface/ethernet/switch/port-isolation
add port-profile=3 ports=ether2,ether9,ether10 type=dst
```

### 协议级隔离

![Protocol Level Isolation](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/crs1xx-2xx-series-switches-examples-10.webp)

CRS 交换机上的协议级隔离可用于增强网络安全性。例如，限制用户（ether2、ether3、ether4、ether5）之间的 DHCP 流量，并仅允许其到达受信任的 DHCP 服务器端口（ether1），可以防止 DHCP 欺骗攻击等安全风险。以下示例展示了如何在 CRS 上进行配置。

将所需端口交换在一起：

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1 hw=yes
add bridge=bridge1 interface=ether2 hw=yes
add bridge=bridge1 interface=ether3 hw=yes
add bridge=bridge1 interface=ether4 hw=yes
add bridge=bridge1 interface=ether5 hw=yes
```

为所有 DHCP 客户端端口设置相同的 Community 端口配置文件。Community 端口配置文件编号为 2 到 30。

```ros
/interface/ethernet/switch/port
set ether2 isolation-leakage-profile-override=2
set ether3 isolation-leakage-profile-override=2
set ether4 isolation-leakage-profile-override=2
set ether5 isolation-leakage-profile-override=2
```

并为选定的 Community (2) 配置端口隔离/泄漏配置文件，以仅允许 DHCP 流量到达受信任 DHCP 服务器所在的端口。必须将注册状态和流量类型属性设置为空，以便仅对 DHCP 协议应用限制。

```ros
/interface/ethernet/switch/port-isolation
add port-profile=2 protocol-type=dhcpv4 type=dst forwarding-type=bridged ports=ether1 registration-status="" traffic-type=""
```

## 服务质量 (QoS)

---

**QoS 配置方案**

基于 MAC 的流量调度和整形： [UFDB 中的 MAC 地址] -> [QoS 组] -> [优先级] -> [队列] -> [整形器]

基于 VLAN 的流量调度和整形： [VLAN 表中的 VLAN ID] -> [QoS 组] -> [优先级] -> [队列] -> [整形器]

基于协议的流量调度和整形： [协议 VLAN 表中的协议] -> [QoS 组] -> [优先级] -> [队列] -> [整形器]

基于 PCP/DEI 的流量调度和整形： [交换机端口 PCP/DEI 映射] -> [优先级] -> [队列] -> [整形器]

基于 DSCP 的流量调度和整形： [QoS DSCP 映射] -> [优先级] -> [队列] -> [整形器]

### 使用内部优先级的基于 MAC 的流量调度

在严格优先级调度模式下，首先服务最高优先级的队列。队列编号代表优先级，队列编号最高的队列具有最高优先级。流量从最高优先级队列开始传输，直到队列为空，然后移动到下一个最高优先级队列，依此类推。如果出口端口没有拥塞，数据包一收到就会被传输。如果高优先级流量持续到达的端口发生拥塞，则较低优先级的队列会饥饿。

在所有 CRS 交换机上，根据内部优先级进行基于 MAC 的出口流量调度的方案如下： [MAC 地址] -> [QoS 组] -> [优先级] -> [队列]；
在此示例中，host1 (E7:16:34:00:00:01) 和 host2 (E7:16:34:00:00:02) 将具有更高的优先级 1，而其余主机在 ether7 端口上传输的流量将具有较低的优先级 0。请注意，CRS 每个端口最多有 8 个队列。

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether6 hw=yes
add bridge=bridge1 interface=ether7 hw=yes
