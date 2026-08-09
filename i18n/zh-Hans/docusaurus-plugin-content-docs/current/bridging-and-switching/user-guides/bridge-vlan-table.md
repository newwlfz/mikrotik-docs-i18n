# Bridge VLAN 表

> 本页介绍 MikroTik RouterOS 的 Bridge VLAN 表功能，解释如何在桥接中使用带标签/不带标签端口、PVID 以及入站/出站规则配置 VLAN 过滤。内容包括 trunk 和 access 端口的设置示例，并强调通过管理访问控制和 EtherType 过滤来增强安全性。

# Bridge VLAN 表

---

可以在网络中使用桥接来过滤 VLAN。要实现此目的，应使用 [Bridge VLAN Filtering](../index.md#bridge-vlan-filtering) 功能。应使用此功能，而不是许多已知的 VLAN 错误配置，这些配置很可能导致性能问题或连接问题。您可以在 [VLAN in a bridge with a physical interface](layer2-misconfiguration.md#vlan-in-a-bridge-with-a-physical-interface) 部分阅读关于最流行的错误配置之一。Bridge VLAN 过滤功能最重要的部分是 bridge VLAN 表，它指定了每个端口上允许哪些 VLAN，但如果您尝试进行更高级的设置，配置可能会变得相当复杂。对于通用设置，您应该能够使用 [Trunk and Access ports](../index.md#vlan-example-trunk-and-access-ports) 示例来配置设备，但本指南的目的是提供深入的解释，并指出使用 Bridge VLAN 过滤时的一些行为特征。

## 背景

---

在深入解释 Bridge VLAN 过滤之前，您应该了解涉及 Bridge VLAN 过滤的几个基本概念。

- **Tagged/Untagged（带标签/不带标签）** - 在 `/interface/bridge/vlan` 菜单下，您可以指定包含 tagged 和 untagged 端口的条目。通常，tagged 端口应为您的 trunk 端口，untagged 端口应为您的 access 端口。通过指定 tagged 端口，桥接将始终为通过该端口（出站）发送的数据包设置 VLAN 标签。通过指定 untagged 端口，桥接将始终从出站数据包中移除 VLAN 标签。

- **VLAN-ids** - 在 `/interface/bridge/vlan` 菜单下，您可以指定一个条目，其中特定 VLAN 在特定端口上被允许。VLAN ID 在出站端口上进行检查。如果数据包包含的 VLAN ID 在 bridge VLAN 表中不存在于出站端口，则该数据包在发送前会被丢弃。

- **PVID** - 端口 VLAN ID 用于 access 端口，为所有入站流量打上特定 VLAN ID 的标签。对于每个使用的 PVID，会在 bridge VLAN 表中添加一个动态条目，并且该端口会自动添加为 untagged 端口。

- **Ingress filtering（入站过滤）** - 默认情况下，bridge VLAN 表中不存在的 VLAN 在发送（出站）前会被丢弃，但此属性允许您在接收（入站）时丢弃数据包。

- **Management access（管理访问）** - 桥接本应简单地在桥接端口之间转发数据包，对其他设备而言，它们之间似乎只是一根线缆。使用 Bridge VLAN 过滤，您可以限制哪些数据包允许访问配置了桥接的设备。最常见的做法是仅使用非常特定的 VLAN ID 允许访问设备，但也有其他方式可以授予设备访问权限。管理访问是通过桥接端口访问设备时增加另一层安全性的好方法；这种访问有时被称为管理端口。对于支持硬件卸载 VLAN 过滤的设备，这也与桥接的 CPU 端口相关。

- **CPU port（CPU 端口）** - 每个带有交换芯片的设备都有一个称为 CPU 端口的专用端口，用于与设备的 CPU 通信。对于支持硬件卸载 VLAN 过滤的设备，此端口就是桥接接口本身。此端口主要用于创建管理访问，但也可用于其他目的，例如在 VLAN 之间路由流量、标记数据包以及应用队列。

- **frame-type（帧类型）** - 您可以根据数据包是否带有 VLAN 标签来过滤数据包；这对于为桥接端口增加额外的安全层非常有用。

- **EtherType** - 默认情况下，VLAN 感知桥接将通过检查 C-TAG（0x8100）来过滤 VLAN；所有其他 VLAN 标签类型都被视为不带标签的数据包（无 VLAN 标签）。所选的 EtherType 将用于 VLAN 过滤和 VLAN 标签添加/移除。

- **VLAN Tunnelling（VLAN 隧道）** - 如果数据包的 EtherType 与桥接配置的 EtherType 不匹配，则入站数据包被视为不带标签的数据包；这种行为提供了将 VLAN 封装到另一个不同 VLAN 中的可能性。这也提供了将特定流量通过网络中不同设备转发的可能性。

- **Tag stacking（标签堆叠）** - 如果数据包具有与 EtherType 匹配的 VLAN 标签，则该数据包被视为带标签的数据包，但您可以强制添加另一个 VLAN 标签，无论数据包内容如何。通过在桥接端口上设置 `tag-stacking=yes`，您将为所有入站数据包在任何其他标签之上添加另一个带有 PVID 值的 VLAN 标签。

## Trunk/Access 端口设置

---

下面您可以找到一个非常常见的拓扑图，适用于由 trunk 端口和多个 access 端口组成的典型设置：

![Trunk and Access Setup](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-01.webp)

这种设置非常常见，因为它提供了使用单个交换机（可能还有单个路由器）将网络划分为多个网段的可能性。这种需求对于想要分离多个部门的公司来说非常普遍。使用 VLAN，您可以使用不同的 DHCP 服务器，根据 VLAN ID 从不同子网分配 IP 地址，这使得创建防火墙规则和 QoS 更加容易。

在这种设置中，您会将一些通用设备（如台式电脑）连接到 **ether2** 和 **ether3**。这些可以被视为工作站，它们通常只使用不带标签的流量（虽然可以强制所有从通用工作站发送的流量都带有 VLAN 标签，但这并不常见）。为了将某些工作站与其他工作站隔离，您必须为所有进入 **ether2** 或 **ether3** 的数据包添加 VLAN 标签，但为了决定数据包应获得哪个 VLAN ID，您需要使用称为 **基于端口的 VLAN** 的概念。在此概念中，数据包根据设备连接的桥接端口获得带有 VLAN ID 的 VLAN 标签。例如，在此设置中，**ether2** 上的设备将获得带有 **VLAN20** 的 VLAN 标签，**ether3** 上的设备将获得带有 **VLAN30** 的 VLAN 标签。只要您有足够的桥接端口，这个概念就非常可扩展。这应该让您理解，桥接与 **ether2/ether3** 后面的设备之间的流量是不带标签的（因为没有 VLAN 标签，因此得名）。

当我们确定了 untagged 端口后，现在可以确定 tagged 端口。Tagged 端口将是 trunk 端口（承载多个 VLAN 的端口），通常此端口连接到路由器或另一个交换机/桥接。您也可以有多个 trunk 端口。Tagged 端口始终携带带有 VLAN 标签的数据包（因此得名），并且您**必须**为希望此端口转发的每个 VLAN ID 指定 tagged 端口。一个端口可能是一个 VLAN ID 的 tagged 端口，同时是另一个 VLAN ID 的 untagged 端口，但这适用于不同类型的设置（Hybrid 端口设置）。

必须为 PVID 属性添加特别说明。此属性应使用在 access 端口上，但也可以用于 trunk 端口（在 Hybrid 端口设置中）。通过使用 PVID 属性，您将为在该特定桥接端口上接收的所有**不带标签**的数据包添加一个带有 PVID 中指定的 VLAN ID 的新 VLAN 标签。PVID 对带标签的数据包没有任何影响，这意味着，例如，如果在 **ether2**（具有 `PVID=20`）上接收到带有 **VLAN40** VLAN 标签的数据包，则 VLAN 标签**不会**被更改，转发将取决于 bridge VLAN 表中的条目。

要配置 trunk/access 端口设置，您需要首先创建一个桥接：

```ros
/interface/bridge
add name=bridge1
```

:::danger
暂时不要启用 VLAN 过滤，因为您可能会因缺乏管理访问而无法访问设备，管理访问将在最后配置。
:::

添加桥接端口并为每个 access 端口指定 PVID：

```ros
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 pvid=20
add bridge=bridge1 interface=ether3 pvid=30
```

:::warning
在启用 VLAN 过滤之前，PVID 不会生效。
:::

在 bridge VLAN 表中添加适当的条目：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
```

您可能认为可以用一个条目简化这些配置，如下所示：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2,ether3 vlan-ids=20,30
```

**不要**在 access 端口上使用多个 VLAN ID。这将无意中允许 **VLAN20** 和 **VLAN30** 同时通过两个 access 端口。在上面的示例中，**ether3** 应该为所有入站数据包设置 VLAN 标签为 **VLAN30**（因为 `PVID=30`），但这并不限制通过此端口发送 VLAN 时允许的 VLAN。Bridge VLAN 表负责决定是否允许特定 VLAN 通过特定端口发送。上面的条目指定 **VLAN20** 和 **VLAN30** 都允许通过 **ether2** 和 **ether3** 发送，并且该条目还指定数据包应以不带 VLAN 标签的方式发送（数据包作为不带标签的数据包发送）。结果，您可能会造成 VLAN 数据包泄漏到本不应接收此类流量的端口，如下图所示。

![Trunk and Access Setup Bad](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-02.webp)

错误配置的 VLAN 表允许 VLAN20 通过 ether3 发送；同时也会允许 VLAN30 通过 ether2 发送

:::danger
不要在 access 端口的 bridge VLAN 表条目中指定多个 VLAN ID；您只应为 trunk 端口指定多个 VLAN ID。
:::

不需要将桥接端口添加为 untagged 端口，因为每个桥接端口都会根据 PVID 属性中指定的 VLAN ID 自动动态添加为 untagged 端口。这是因为一个功能会自动在 bridge VLAN 表中添加适当的条目，以方便和性能考虑。此功能有一些您必须注意的注意事项。所有具有相同 PVID 的端口将被添加到相应 VLAN ID 的单个条目中作为 untagged 端口，但请注意 **Bridge 接口** 也有一个 VLAN ID。

出于测试目的，我们将启用 VLAN 过滤，但请注意，这可能会使您无法访问设备，因为它尚未配置管理访问（我们稍后将配置）。始终建议在使用串行控制台时配置 VLAN 过滤，尽管您也可以通过未添加到桥接的端口配置设备。确保您使用串行控制台或通过不同的端口（不在桥接中）连接，然后启用 VLAN 过滤：

```ros
/interface/bridge/set bridge1 vlan-filtering=yes
```

:::warning
您可能不会在启用 VLAN 过滤后立即失去对设备的访问，但您可能会断开连接，因为桥接必须重置自身才能使 VLAN 过滤生效，这将迫使您重新连接（这在使用 MAC-telnet 时最为相关）。您有可能能够使用不带标签的流量访问设备。此场景将在下面描述。
:::

如果您现在启用了 VLAN 过滤并打印出当前的 VLAN 表，您将看到如下表：

```text
[admin@MikroTik] > /interface/bridge/vlan/print
Flags: X - disabled, D - dynamic 
 #   BRIDGE                     VLAN-IDS  CURRENT-TAGGED       CURRENT-UNTAGGED
 0   bridge1                    20        ether1               ether2
 1   bridge1                    30        ether1               ether3
 2 D bridge1                    1                              bridge1
                                                               ether1
```

由于默认情况下所有桥接端口（包括我们的 trunk 端口 **ether1**）都设置了 `PVID=1`，因此为 **VLAN1** 添加了一个动态条目，但您还应该注意到 **bridge1** 接口（CPU 端口）也被动态添加。您应该意识到 **bridge1** 也是一个桥接端口，因此可能会被动态添加到 bridge VLAN 表中。由于此功能，您可能会无意中允许访问设备。例如，如果您按照本指南操作，将 trunk 端口（**ether1**）的 **PVID=1** 保留，并且没有更改 CPU 端口（**bridge1**）的 PVID，那么通过 **ether1** 使用不带标签的流量访问设备是被允许的。这在您打印 bridge VLAN 表时也是可见的。此场景如下图所示：

![Trunk and Access Setup Unintentional Management](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-03.webp)

通过 trunk 端口使用不带标签的流量无意中允许了管理访问

:::danger
始终检查 bridge VLAN 表，确保您没有无意中允许某些 VLAN 或不带标签的流量访问特定端口，尤其是 CPU 端口（桥接）。
:::

有一种简单的方法可以防止桥接（CPU 端口）被添加为 untagged 端口。您可以简单地将 trunk 端口上的 PVID 设置为与桥接的 PVID 不同（或更改桥接的 PVID），但还有另一个选项，更直观且推荐。由于您期望 trunk 端口只应接收带标签的流量（在此示例中，它应仅接收 **VLAN20/VLAN30**），而不应接收不带标签的流量，您可以使用 `ingress-filtering` 结合 `frame-type` 来过滤不需要的数据包，但要完全理解 ingress filtering 的行为，我们必须首先了解管理访问的细节。

管理访问用于创建通过启用了 VLAN 过滤的桥接访问设备的方式。您可以简单地允许不带标签的访问，这样做相当简单。假设您希望 **ether3** 后面的工作站能够访问设备。我们之前假设工作站是一台通用计算机，不会使用带标签的数据包，因此只会发送不带标签的数据包。这意味着我们应该将 CPU 端口（**bridge1**）添加为 bridge VLAN 表中的 untagged 接口，为此，只需为 **bridge1** 和 **ether3** 端口使用相同的 PVID 值，并将两个端口设置为该 VLAN ID 的 untagged 成员。在这种情况下，您将从具有 `PVID=30` 的 **ether3** 连接，因此相应地更改配置：

```ros
/interface/bridge/set [find name=bridge1] pvid=30
/interface/bridge/vlan/set [find vlan-ids=30] untagged=bridge1,ether3
```

:::warning
您可以使用自动添加具有相同 PVID 值的 untagged 端口的功能，或者您可以简单地更改 PVID 以匹配 **ether3** 和 **bridge1**。
:::

使用不带标签的流量允许访问设备不被视为良好的安全实践。更好的方式是使用非常特定的 VLAN（有时称为管理 VLAN）允许访问设备。在我们的案例中，这将是 **VLAN99**。这增加了显著的安全层，因为攻击者必须猜测用于管理目的的 VLAN ID，然后猜测登录凭据。除此之外，您甚至可以通过仅允许特定 IP 地址访问设备来增加另一层安全性。本指南的目的是提供深入的解释。因此，我们在设置中增加了一些复杂性，以了解您必须考虑的一些潜在注意事项。我们将允许从 access 端口使用带标签的流量进行访问（如下图所示）。要允许从 **ether3** 使用 **VLAN99** 访问设备，我们必须在 bridge VLAN 表中添加适当的条目。此外，连接到 ether3 的网络设备必须支持 VLAN 标签。

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
```

![Trunk and Access Setup Management Access](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-04.webp)

通过 access 端口（使其成为 hybrid 端口）使用带标签的流量进行管理访问

:::warning
如果 ether1 和 bridge1 的 PVID 匹配（默认情况下，它们匹配为 1），则由于自动将 untagged 端口添加到 bridge VLAN 表的功能，允许从 ether1 使用不带标签的流量访问设备。
:::

但您可能会注意到，此时使用 **VLAN99** 的访问不起作用。这是因为您需要一个监听带标签流量的 VLAN 接口。您可以简单地为相应的 VLAN ID 创建此接口，并可以为该接口设置 IP 地址：

```ros
/interface/vlan
add interface=bridge1 name=VLAN99 vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

:::warning
此时我们的 access 端口（**ether3**）同时期望带标签和不带标签的流量；这样的端口称为 **hybrid 端口**。
:::

此时，我们可以利用 `ingress-filtering` 和 `frame-type`。首先，我们将关注 `frame-type`，它限制了允许的数据包类型（带标签、不带标签、两者），但要使 `frame-type` 正常工作，必须启用 `ingress-filtering`，否则它将不会生效。在我们的示例中，我们希望允许从 **ether3** 使用带标签的流量（**VLAN99**）进行访问，同时允许通用工作站访问网络，我们可以得出结论，此端口需要允许带标签和不带标签的数据包，但 **ether1** 和 **ether2** 应只接收特定类型的数据包，基于这些结论，我们可以增强网络的安全性。由于 **ether1** 是我们的 trunk 端口，它应只携带带标签的数据包，而 **ether2** 是我们的 access 端口，因此不应携带任何带标签的数据包，基于这些结论，我们可以丢弃无效数据包：

```ros
/interface/bridge/port
set [find where interface=ether1] ingress-filtering=yes frame-types=admit-only-vlan-tagged
set [find where interface=ether2] ingress-filtering=yes frame-types=admit-only-untagged-and-priority-tagged
```

假设您忘记在 **ether1** 上启用 ingress-filtering 并更改 frame-type 属性，这将无意中允许通过 **ether1** 使用不带标签的流量访问设备，因为 **bridge1** 和 **ether1** 的 PVID 匹配，但您期望只有带标签的流量才能访问设备。可以丢弃所有目标为 **CPU 端口** 的不带标签的数据包：

```ros
/interface/bridge
set bridge1 frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

这不仅丢弃了不带标签的数据包，还禁用了自动将 untagged 端口添加到 bridge VLAN 表的功能。如果您打印出当前的 bridge VLAN 表，您会注意到 **bridge1** 不再被动态添加为 untagged 端口：

```text
[admin@MikroTik] > /interface/bridge/vlan/print 
Flags: X - disabled, D - dynamic 
 #   BRIDGE       VLAN-IDS  CURRENT-TAGGED        CURRENT-UNTAGGED
 0   bridge1      20        ether1
 1   bridge1      30        ether1                ether3
 2 D bridge1      1                               ether1
 3   bridge1      99        bridge1
                            ether3  
```

:::warning
当端口上使用 `frame-type=admit-only-vlan-tagged` 时，该端口不会为 PVID 动态添加为 untagged 端口。
:::

虽然 `frame-type` 可用于丢弃特定类型的数据包，但 `ingress-filtering` 可用于在数据包发送前过滤掉它们。要完全理解 ingress filtering 的必要性，请考虑以下场景：**VLAN99** 在 **ether3** 和 **bridge1** 上被允许，但您仍然可以从 **ether1** 向 **ether3** 发送 **VLAN99** 流量。这是因为 bridge VLAN 表仅在出站端口上检查端口是否允许携带特定 VLAN。在我们的案例中，**ether3** 被允许携带 **VLAN99**，因此它被转发。要防止这种情况，您**必须**使用 `ingress-filtering`。使用 ingress filtering，入站数据包也会被检查。在我们的案例中，bridge VLAN 表不包含 **VLAN99** 在 **ether1** 上被允许的条目，因此数据包将立即被丢弃。当然，在没有 ingress filtering 的情况下，连接无法建立，因为 **VLAN99** 只能从 **ether1** 转发到 **ether3**，而不能从 **ether3** 转发到 **ether1**，但仍然存在可能利用此类错误配置的攻击（例如，ARP 欺骗）。数据包丢弃行为如下图所示：

![Trunk and Access Setup Ingress](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-05.webp)

带和不带 ingress filtering 的 trunk/access 端口设置。Ingress filtering 可以防止不需要的流量被转发。请注意，ether1 在 bridge VLAN 表中不允许携带 VLAN99。

:::danger
始终尝试在可能的地方使用 `ingress-filtering`。它增加了显著的安全层。
:::

Ingress-filtering 也可以用于 **CPU 端口**（桥接）。这可以用于防止一些可能的攻击向量，并限制允许访问 CPU 的 VLAN。最好在入站端口上丢弃数据包，而不是在出站端口上。这减少了 CPU 负载，在使用硬件卸载与 bridge VLAN 过滤时非常关键。

:::warning
`ingress-filtering` 属性仅影响入站流量，但 `frame-type` 同时影响出站和入站流量。
:::

尽管您可以限制端口上允许的 VLAN 和数据包类型，但通过 access 端口允许访问设备从来都不是良好的安全实践，因为攻击者可以嗅探数据包并提取管理 VLAN 的 ID。您应只允许从 trunk 端口（**ether1**）访问设备，因为 trunk 端口通常具有更好的物理安全性。您应移除之前的条目，并允许通过连接到路由器的端口访问设备（如下图所示）：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether1 vlan-ids=99
```

![Basic VLAN Switching](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-06.webp)

## VLAN 隧道设置

---

在某些情况下，您可能希望通过某些交换机转发已经带标签的流量。这是骨干基础设施中相当常见的设置，因为它提供了封装来自例如边缘路由器的流量，并无缝地通过骨干网转发到另一个边缘路由器的可能性。下面您可以找到一个 VLAN 隧道拓扑的示例：

![Provider Bridge](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-07.webp)

Provider bridge 拓扑

SVID 代表 Service VID，指示标签类型以及 VID。

:::warning
要完全理解如何正确配置 VLAN 隧道，您应首先阅读 Trunk/Access 端口设置部分，然后再继续。
:::

有两种可能的方式来实现这一点，一种是标准化的 IEEE 802.1ad 方式，另一种是使用 **Tag stacking**。我们将首先回顾标准化方式，因为相同的原则适用于两种方式，只需更改几个参数即可使用另一种方法。VLAN 隧道的工作原理是桥接检查外部 VLAN 标签是否使用与 ether-type 中指定的相同 VLAN 标签。如果 VLAN 标签匹配，则该数据包被视为带标签的数据包，否则被视为不带标签的数据包。

:::warning
桥接只检查外部标签（最靠近 MAC 地址的标签）；在桥接配置中的任何地方都忽略任何其他标签。桥接不感知数据包内容；即使可能存在另一个 VLAN 标签，也只检查第一个 VLAN 标签。
:::

ether-type 属性允许您为 VLAN 标签选择以下 EtherType：

- 0x88a8 - IEEE 802.1ad，服务标签。
- 0x8100 - IEEE 802.1Q，客户 VLAN（常规 VLAN 标签）。
- 0x9100 - 非官方标签类型（很少使用）。

要正确配置 Bridge VLAN 过滤，您必须理解桥接如何区分带标签和不带标签的数据包。如前所述，桥接将检查 EtherType 是否与数据包中的外部 VLAN 标签匹配。例如，考虑以下数据包：

```text
FFFFFFFFFFFF 6C3B6B7C413E 8100 6063 9999
----------------------------------------
DST-MAC = FFFFFFFFFFFF
SRC-MAC = 6C3B6B7C413E
外部 EtherType = 8100 (IEEE 802.1Q VLAN 标签)
VLAN 优先级 = 3
VLAN ID = 99 (HEX = 63)
内部 EtherType = 9999
```

让我们假设我们设置了 **`ether-type=0x88a8`**，在这种情况下，上面的数据包将被视为不带标签的，因为桥接正在寻找不同的 VLAN 标签。现在让我们考虑以下数据包：

```text
FFFFFFFFFFFF 6C3B6B7C413E 88A8 6063 8100 5062 9999
----------------------------------------
DST-MAC = FFFFFFFFFFFF
SRC-MAC = 6C3B6B7C413E
外部 EtherType = 88A8 (IEEE 802.1ad VLAN 标签)
VLAN 优先级 = 3
VLAN ID = 99 (HEX = 63)
内部 EtherType 1 = 8100 (IEEE 802.1Q VLAN 标签)
VLAN 优先级 = 2
VLAN ID = 98 (HEX = 62)
内部 EtherType 2 = 9999
```

这次让我们假设我们设置了 **`ether-type=0x8100`**。在这种情况下，上面的数据包也被视为不带标签的，因为外部标签使用的是 IEEE 802.1ad VLAN 标签。相同的原则适用于其他 VLAN 相关功能，例如，`PVID` 属性将在 access 端口上添加新的 VLAN 标签，并且该 VLAN 标签将使用 ether-type 中指定的 EtherType。

**SW1** 和 **SW2** 都使用相同的配置：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes ether-type=0x88a8
/interface/bridge/port
add interface=ether1 bridge=bridge1 pvid=200
add interface=ether2 bridge=bridge1 pvid=300
add interface=ether3 bridge=bridge1
/interface/bridge/vlan
add bridge=bridge1 tagged=ether3 untagged=ether1 vlan-ids=200
add bridge=bridge1 tagged=ether3 untagged=ether2 vlan-ids=300
```

在此示例中，我们假设所有路由器都传递使用常规/客户 VLAN 标签的流量。根据上述原则，交换机上的此类流量将被视为不带标签的流量。交换机将使用服务 VLAN 标签（外部 802.1ad 标签）封装此流量，**SW1** 和 **SW2** 之间的流量将被视为带标签的。在流量到达目的地之前，交换机将解封装外部标签并转发原始的 802.1Q 带标签帧。请参见下面的数据包示例：

![Service VLAN 802.1ad](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-08.webp)802.1ad VLAN 封装前后的数据包示例

:::warning
适用于使用 IEEE 802.1Q 的常规 trunk/access 端口设置的所有原则也适用于 VLAN 隧道设置。确保您使用 bridge VLAN 表和 ingress filtering 正确限制 VLAN 和数据包类型。
:::

如果您想从，例如，**ether3** 创建管理访问到设备，并希望使用 **VLAN99**，那么您将使用以下命令：

```ros
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1,ether3 vlan-ids=99
/interface/vlan
add interface=bridge1 name=VLAN99 use-service-tag=yes vlan-id=99
/ip/address
add address=192.168.99.2/24 interface=VLAN99
```

您可能注意到，唯一的区别是 VLAN 接口使用 `use-service-tag=yes`；这将 VLAN 接口设置为监听 IEEE 802.1ad VLAN 标签。这将要求您使用 IEEE 802.1ad VLAN 标签来使用管理 VLAN 访问设备 - 在启用 Bridge VLAN 过滤时，您将无法使用常规 VLAN 标签连接到设备。ether-type 是全局设置的，将影响所有 Bridge VLAN 过滤功能。

:::danger
带有 Marvell-98DX3257 交换芯片的设备（例如 CRS354 系列）不支持在 1Gbps 以太网接口上对其他 VLAN 类型（`0x88a8` 和 `0x9100`）进行 VLAN 过滤。
:::

### 标签堆叠

在 VLAN 隧道设置中，我们添加了一个与 VLAN 标签不同的新 VLAN 标签，但可以添加新的 VLAN 标签，无论数据包内容如何。与常规 VLAN 隧道设置的区别在于，桥接不检查数据包是带标签还是不带标签，它假定在特定端口上接收的所有数据包都是不带标签的数据包，并将添加新的 VLAN 标签，无论是否存在 VLAN 标签。这称为 **标签堆叠**，因为它将 VLAN 标签“堆叠”在先前标签之上，无论 VLAN 标签类型如何。这是不支持 IEEE 802.1ad 标准但仍希望将 VLAN 流量封装到新 VLAN 中的网络的非常常见的设置。

将要添加的 VLAN 标签取决于 `ether-type` 和 `PVID`。例如，如果您在端口上设置了 `ether-type=0x8100` 和 `PVID=200`，则桥接将在任何其他标签（如果存在）之上直接添加新的 IEEE 802.1Q VLAN 标签。相同的 VLAN 过滤原则仍然适用。您必须确定哪些端口将是您的 trunk 端口并将其标记为 tagged 端口，确定您的 access 端口并将其添加为 untagged 端口。

为了解释 VLAN 标签添加和移除如何与标签堆叠一起工作，让我们使用与之前相同的网络拓扑：

![Basic VLAN Switching 2](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-09.webp)

我们想要实现的是，无论 **ether2** 和 **ether3** 上接收到什么，都会添加一个新的 VLAN 标签来封装来自这些端口的流量。`Tag-stacking` 强制添加新的 VLAN 标签，因此我们可以使用此属性来实现我们想要的设置。我们将使用与 Trunk/Access 端口设置相同的配置，但在 access 端口上启用 `tag-stacking`：

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes ether-type=0x8100
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2 tag-stacking=yes pvid=20
add bridge=bridge1 interface=ether3 tag-stacking=yes pvid=30
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 untagged=ether2 vlan-ids=20
add bridge=bridge1 tagged=ether1 untagged=ether3 vlan-ids=30
```

:::warning
添加的 VLAN 标签将使用指定的 `ether-type`。所选的 EtherType 也将用于 VLAN 过滤。只检查外部标签，但使用标签堆叠时，标签检查被跳过，并假定无论如何都必须添加新标签。
:::

让我们假设 **ether2** 和 **ether3** 后面的设备正在发送带标签的 **VLAN40** 流量。使用此配置，**所有**数据包都将被封装为新的 VLAN 标签，但您必须确保已将外部标签中的 VLAN ID 添加到 bridge VLAN 表中。**VLAN40** 未添加到 bridge VLAN 表中，因为它是内部标签且不被检查；我们只关心外部标签，根据端口不同，它要么是 **VLAN20** 要么是 **VLAN30**。

与其他设置类似，bridge VLAN 表将用于确定是否需要移除 VLAN 标签。例如，当 **ether1** 接收到带标签的 **VLAN20** 数据包时，桥接检查 **ether2** 被允许携带 **VLAN20**，因此它即将通过 **ether2** 发送，但它还检查 bridge VLAN 表以确定是否应移除 VLAN 标签，由于 **ether2** 被标记为 untagged 端口，桥接将把这些数据包从 **ether1** 转发到 **ether2**，而不带 **VLAN20** VLAN 标签。

从 access 端口的角度来看，与 Trunk/Access 端口设置中相同的原则适用。在 **ether2** 上接收的所有数据包都将获得带有 PVID 中指定的 VLAN ID 的新 VLAN 标签，在这种情况下，将添加带有 **VLAN20** 的新 VLAN 标签，并且此 VLAN 将受到 VLAN 过滤的影响。请参见下面的数据包示例：

![Tag Stacking](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/bridge-vlan-table-10.webp)

标签堆叠前后的数据包示例