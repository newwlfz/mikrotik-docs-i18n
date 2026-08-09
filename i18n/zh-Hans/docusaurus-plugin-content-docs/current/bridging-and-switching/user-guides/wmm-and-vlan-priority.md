# WMM 与 VLAN 优先级

> 本页说明 MikroTik RouterOS 如何实现 WMM（Wi-Fi 多媒体）和 VLAN 优先级以支持 QoS，详细介绍了流量如何分类到访问类别（后台、尽力而为、视频、语音）、VLAN 优先级处理，以及使用 IP 防火墙 mangle 规则或桥接过滤器设置数据包优先级的方法。

# WMM 与 VLAN 优先级

## WMM 工作原理

---

WMM 通过将流量划分为 4 个访问类别来工作：后台、尽力而为、视频、语音。QoS 策略（对不同访问类别的不同处理）应用于传输的数据包，因此发送设备对不同数据包进行不同处理，例如，AP 无法控制客户端如何传输数据包，客户端也无法控制 AP 如何传输数据包。

MikroTik AP 和客户端根据分配给数据包的优先级进行分类，依据下表（根据 WMM 规范）：1、2 - 后台；0、3 - 尽力而为；4、5 - 视频；6、7 - 语音。

要使用多个 WMM 访问类别，而不仅仅是默认优先级为 0 的所有数据包所进入的尽力而为类别，必须为这些数据包设置优先级。默认情况下，路由器内部的所有数据包（传入和本地生成的）优先级均为 0。

数据包的“更好”访问类别并不一定意味着它将比所有具有“较差”访问类别的其他数据包更先在空中发送。WMM 通过为每个访问类别执行具有不同设置的 DCF 介质访问方法（EDCF）来工作，这意味着“更好”的访问类别有更高的概率获得介质访问权——启用 WMM 的站点可以被视为 4 个站点，每个访问类别一个，具有“更好”访问类别的站点在竞争介质时使用更有可能获得传输机会的设置（通过使用更短的退避超时）。详细信息可参阅 802.11e 和 WMM 规范。

:::info
WMM 支持可通过 `wmm-support` 设置启用。它仅适用于 B 和 G 频段。其他频段无论此设置如何都将启用它。
:::

## VLAN 优先级工作原理

---

VLAN 优先级是 VLAN 标记头中的一个 3 位字段，称为优先级代码点（PCP），值在 0 到 7 之间。它用于在桥接器和交换机上实现 QoS。MikroTik 设备默认发送优先级为 0 的 VLAN 数据包（本地生成或封装的）。RouterOS 桥接器原样转发 VLAN 标记的数据包，这意味着接收到的具有特定 VLAN 优先级的 VLAN 标记数据包将以相同的 VLAN 优先级离开桥接器。唯一的例外是当桥接器对数据包进行去标记时；在这种情况下，由于缺少 VLAN 头，VLAN 优先级不会被保留。

更多详细信息可参阅 IEEE 802.1p 规范。

## 如何设置优先级

---

数据包的优先级可以通过 IP 防火墙 mangle 规则或桥接过滤器/NAT 规则中的 `action=set-priority` 来设置。优先级可以设置为特定值，或使用 `from-ingress` 设置从入口优先级获取。入口优先级是在传入数据包上检测到的优先级值（如果可用）。目前，入口优先级有 2 个来源——VLAN 头中的优先级和通过无线接口接收的 WMM 数据包的优先级。对于所有其他数据包，入口优先级为 0。

请注意，入口优先级值不会自动复制到 IP mangle 的 `priority` 值中。需要设置正确的规则来实现这一点。

有两种控制优先级的方法——使用具有特定匹配器（协议、地址等）的规则分配优先级，或从入口优先级设置。两种选项都需要设置正确的规则。

这实质上意味着，如果无法或不想通过规则对数据包进行分类，则网络配置必须使路由器能够从传入帧中提取入口优先级。请记住，目前有 2 个来源——数据包中的 VLAN 标记和接收到的 WMM 数据包。

:::info
不要将队列的优先级与分配给数据包的优先级混淆。队列的优先级是独立工作的，指定队列的“重要性”，并且仅在特定队列设置中有意义。将数据包优先级视为某种通过规则附加到数据包的标记。此外，请注意，此标记目前仅用于通过启用 WMM 的链路发送的出站数据包，以及在发送 VLAN 标记数据包时（无论该数据包是本地标记还是桥接的）。
:::

### 基于特定匹配器设置 VLAN 或 WMM 优先级

可以根据 IP mangle 或桥接过滤器/NAT 规则中的特定匹配器更改 VLAN 和 WMM 优先级。在此示例中，所有出站 ICMP 数据包将通过 IP mangle 规则以 VLAN 或 WMM 优先级发送：

```ros
/ip/firewall/mangle
add action=set-priority chain=output new-priority=2 protocol=icmp
```

### 自定义优先级映射

有时需要将某些 VLAN 或 WMM 优先级更改或清除为默认值。我们可以使用 IP mangle 或桥接防火墙/NAT 规则中的 `ingress-priority` 匹配器仅过滤所需的优先级，并使用 `new-priority` 操作设置将其更改为不同的值。例如，通过桥接转发的优先级为 5 的 VLAN 标记数据包需要更改为 0。

```ros
/interface/bridge/filter
add action=set-priority chain=forward ingress-priority=5 new-priority=0
```

### 在桥接器内将 WMM 优先级转换为 VLAN 优先级

当接收到已设置 WMM 优先级的无线数据包时，RouterOS 桥接器不会自动将其转换为 VLAN 头。这意味着接收到的具有 WMM 优先级的无线数据包如果由桥接器添加 VLAN 标记，将以 VLAN 优先级 0 转发。但是，我们可以使用带有 `from-ingress` 设置的桥接过滤器规则来保留 VLAN 数据包中的优先级。例如，我们希望将无线数据包通过 ether2 转发并带有 VLAN 10 头，同时保留已设置的 WMM 优先级（由无线客户端设置）。

```ros
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2 pvid=10
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2 vlan-ids=10

# 将 WMM 优先级转换为 VLAN 优先级
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

同样的情况适用于无线数据包通过无线接口使用 `vlan-mode=use-tag` 和 `vlan-id` 设置进行 VLAN 标记时。您仍然需要使用相同的桥接过滤器规则将 WMM 优先级转换为 VLAN 优先级：

```ros
/interface/wireless
set [ find default-name=wlan2 ] vlan-mode=use-tag vlan-id=10

/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan2

 # 将 WMM 优先级转换为 VLAN 优先级
/interface/bridge/filter
add action=set-priority chain=forward new-priority=from-ingress out-interface=ether2
```

:::info
相同的原则也适用于反向情况。RouterOS 不会自动将 VLAN 优先级转换为 WMM 优先级；您可以使用 `new-priority=from-ingress` 规则来执行此转换。

RouterOS 桥接器原样转发 VLAN 标记的数据包，这意味着它们以进入时的相同优先级离开桥接器。唯一的例外是当桥接器对数据包进行去标记时，因为移除 VLAN 头时优先级信息会丢失。
:::

## 从 DSCP 设置优先级

---

设置 VLAN 或 WMM 优先级的另一种方法是使用 IP 头中的 DSCP 字段。这只能通过 IP 防火墙 mangle 规则使用 `new-priority=from-dscp` 或 `new-priority=from-dscp-high-3-bits` 设置以及 `set-priority` 操作属性来完成。请注意，IP 头中的 DSCP 值可以是 0-63，但优先级仅为 0-7。使用 `new-priority=from-dscp` 设置时，优先级将是 DSCP 值的低 3 位，但使用 `new-priority=from-dscp-high-3-bits` 时，优先级将是 DSCP 值的高 3 位。

请记住，DSCP 只能在 IP 数据包上访问，并且 IP 头中的 DSCP 值应在某处设置（由客户端设备或 IP mangle 规则）。

最好在某些边界路由器（例如，用于连接互联网的主路由器）上根据流量类型设置 IP 头中的 DSCP 值，例如，将来自互联网的属于 SIP 连接的数据包的 DSCP 值设置为 7，其余设置为 0。这样，数据包只需在一个地方进行标记。然后，网络中的所有 AP 只需一条规则即可从 DSCP 值设置数据包优先级。

### 从 DSCP 设置 VLAN 或 WMM 优先级

在此示例中，AP 设备将在数据包通过无线接口路由时从 DSCP 设置 WMM 优先级。

```ros
/ip/firewall/mangle
add action=set-priority chain=forward new-priority=from-dscp out-interface=wlan2
```

:::info
当数据包通过桥接器转发时，可以在桥接设置下使用 `use-ip-firewall=yes` 使数据包通过 IP mangle 规则。
:::

## 从优先级设置 DSCP

---

类似地，如果接收到的数据包包含 VLAN 或 WMM 优先级，则可以设置 DSCP 值。这可以通过 IP mangle 规则使用 `new-dscp=from-priority` 或 `new-dscp=from-priority-to-high-3-bits` 设置以及 `change-dscp` 操作属性来实现。请注意，VLAN 或 WMM 数据包中的优先级值可以是 0-7，但 IP 头中的 DSCP 是 0-63。使用 `new-dscp=from-priority` 设置时，优先级值将设置 DSCP 的低 3 位，但使用 `new-dscp=from-priority-to-high-3-bits` 时，优先级值将设置 DSCP 的高 3 位。

但是，此设置不能直接使用接收到的 VLAN 或 WMM 数据包中的入口优先级。您首先需要使用 IP mangle 或桥接过滤器/NAT 规则设置优先级（在这种情况下可以使用入口优先级），然后才能应用 DSCP 规则。

### 从 VLAN 或 WMM 优先级设置 DSCP

在此示例中，AP 设备需要在数据包路由时从 WMM 优先级设置 DSCP。首先，添加一条规则来设置优先级。DSCP 规则需要它来正确更改 DSCP 值。此规则可以从入口获取优先级。然后添加 DSCP 规则来更改其值。

```ros
/ip/firewall/mangle
add action=set-priority chain=prerouting in-interface=wlan2 new-priority=from-ingress
add action=change-dscp chain=prerouting in-interface=wlan2 new-dscp=from-priority
```

:::info
当数据包通过桥接器转发时，可以在桥接设置下使用 `use-ip-firewall=yes` 使数据包通过 IP mangle 规则。
:::

## 组合优先级设置和处理方案

---

复杂的网络和不同的情况可以通过组合不同的方法来携带优先级信息以确保 QoS 并优化资源使用，基于上述“构建块”。几点建议：

- 整个网络中的过滤器规则越少越好（越快）。尝试仅在必要时对数据包进行分类，最好在快速路由器上执行此操作，因为很可能需要连接跟踪。
- 使用 DSCP 在网络中转发的 IP 数据包中携带优先级信息。这样您可以在需要时使用它。
- 在必要时使用 VLAN，因为它们也携带优先级信息。确保路径中的以太网桥接器和交换机不会清除 VLAN 标记中的优先级信息。
- 请记住，QoS 不会提高链路的吞吐量；它只是对不同数据包进行不同处理，并且无线链路上的 WMM 流量将在空中区分常规流量。

## 另请参阅

---

- [RouterOS 中的数据包流](../../firewall-and-quality-of-service/packet-flow-in-routeros.md)
- [IP mangle](../../firewall-and-quality-of-service/firewall/mangle.md)
- [桥接防火墙](../#bridge-firewall)