# 基础 VLAN 交换

> 本页概述了 MikroTik RouterOS 上基础 VLAN 交换配置，涵盖 Marvell Prestera 和 RTL8367/CRS 系列交换芯片设备的设置，包括硬件卸载 VLAN 过滤和端口配置示例。

# 基础 VLAN 交换

---

许多 MikroTik 设备内置交换芯片，支持硬件级 VLAN 交换。只要采用适当的配置方法，即可在使用 VLAN 时实现线速性能。由于不同型号的配置方法各异，本指南重点介绍如何在不同设备上设置基本的 trunk/access 端口，并从 trunk 端口配置管理端口，以达成最佳性能并充分利用可用硬件组件。

![基础 VLAN 交换](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/basic-vlan-switching-01.webp)

## 搭载 Marvell Prestera 交换芯片及 RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523 交换芯片的 MikroTik 设备

---

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/bridge
set bridge1 vlan-filtering=yes
```

更多详细示例请参见 [此处](../index.md#bridge-vlan-filtering)。

:::info
RTL8367、88E6393X、88E6191X、88E6190、MT7621、MT7531 和 EN7523 交换芯片自 RouterOS v7 起支持硬件卸载 VLAN 过滤。
:::

:::warning
将 `frame-types` 设置为 `admit-all` 或 `admit-only-untagged-and-priority-tagged` 的桥接端口，将自动作为 `pvid` VLAN 的 untagged 端口添加。
:::

## CRS1xx/CRS2xx 系列交换机

---

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface/ethernet/switch/ingress-vlan-translation
add ports=ether2 customer-vid=0 new-customer-vid=20
add ports=ether3 customer-vid=0 new-customer-vid=30
/interface/ethernet/switch/egress-vlan-tag
add tagged-ports=ether1 vlan-id=20
add tagged-ports=ether1 vlan-id=30
add tagged-ports=ether1,switch1-cpu vlan-id=99
/interface/ethernet/switch/vlan
add ports=ether1,ether2 vlan-id=20
add ports=ether1,ether3 vlan-id=30
add ports=ether1,switch1-cpu vlan-id=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/ethernet/switch
set drop-if-invalid-or-src-port-not-member-of-vlan-on-ports=ether1,ether2,ether3
```

更多详细示例请参见 [此处](./crs1xx-2xx-series-switches-examples.md#vlan)。

## 其他内置交换芯片的设备

---

```ros
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
/interface/ethernet/switch/vlan
add ports=ether1,ether2 switch=switch1 vlan-id=20
add ports=ether1,ether3 switch=switch1 vlan-id=30
add ports=ether1,switch1-cpu switch=switch1 vlan-id=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/ethernet/switch/port
set ether1 vlan-mode=secure vlan-header=add-if-missing
set ether2 vlan-mode=secure vlan-header=always-strip default-vlan-id=20
set ether3 vlan-mode=secure vlan-header=always-strip default-vlan-id=30
set switch1-cpu vlan-header=leave-as-is vlan-mode=secure
```

更多详细示例请参见 [此处](../switch-chip-features.md#setup-examples)。

:::info 适用范围与范围
此配置适用于 RouterBOARD 系列设备（RB4xx、RB9xx、RB2011、RB3011、hAP、hEX、cAP 等）。

并非所有带交换芯片的设备都支持硬件级 VLAN 交换。如果设备支持 `VLAN table`，则可以使用内置交换芯片。请通过 `/interface/ethernet/switch/print` 或 [兼容性表](../switch-chip-features.md) 检查您芯片的能力。
:::

:::warning 硬件限制与配置规则

* **多交换芯片：** 在配备多个芯片的设备上（如 RB2011、RB3011、RB1100），VLAN 流量仅在*同一*芯片上的端口之间进行硬件交换。跨芯片桥接端口意味着 VLAN 无法在硬件层面进行过滤。要解决此问题，可以在芯片之间连接物理线缆，或使用 Bridge VLAN 过滤（这会禁用硬件卸载）。
* **QCA8337 与 Atheros8327 芯片：** 您必须保留默认的 `vlan-header=leave-as-is` 属性。交换芯片使用 `default-vlan-id` 属性（该属性应仅应用于 access/hybrid 端口）将未标记的入站流量分配到 VLAN。
* **RSTP 冲突：** 默认情况下，桥接接口使用 `protocol-mode=rstp`。在某些设备上，这会禁用硬件卸载。请参阅 [Bridge 硬件卸载](../#bridge-hardware-offloading) 部分了解支持的功能。
:::

## 其他无内置交换芯片的设备

---

可以使用 CPU 进行 VLAN 过滤；有多种方法可以实现，但强烈建议使用 Bridge VLAN 过滤。

```ros
/interface/bridge
add name=bridge1 frame-types=admit-only-vlan-tagged
/interface/bridge/port
add bridge=bridge1 interface=ether1 frame-types=admit-only-vlan-tagged
add bridge=bridge1 interface=ether2 pvid=20 frame-types=admit-only-untagged-and-priority-tagged
add bridge=bridge1 interface=ether3 pvid=30 frame-types=admit-only-untagged-and-priority-tagged
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1 vlan-ids=20
add bridge=bridge1 tagged=ether1 vlan-ids=30
add bridge=bridge1 tagged=ether1,bridge1 vlan-ids=99
/interface/vlan
add interface=bridge1 vlan-id=99 name=MGMT
/ip/address
add address=192.168.99.1/24 interface=MGMT
/interface/bridge
set bridge1 vlan-filtering=yes
```

更多详细示例请参见 [此处](../index.md#bridge-vlan-filtering)。