# 无线网络中的VLAN

> 本页说明如何在MikroTik RouterOS无线接口上配置VLAN，实现不同虚拟AP（Virtual AP）和网络之间的Layer2隔离。文中包含使用VLAN接口隔离访客（Guest）和工作（Work）AP的配置示例、带VLAN过滤的桥接配置以及安全配置文件（Security Profile）设置。

# 无线网络中的VLAN

## 概述

VLAN允许在共享同一Layer1介质的同时，将设备隔离到不同的Layer2网段。这在需要分离不同类型设备或用户的场景中非常有用。该功能对无线网络同样重要，因为您可以通过VLAN隔离不同的虚拟AP，并利用防火墙限制对特定服务或网络的访问。以下示例展示了在同一设备上配置两个接入点（Access Point），并将其隔离到不同VLAN的配置方法。这种场景在您拥有**访客AP**和**工作AP**时非常常见。

## 示例

![](https://manual.mikrotik.com/docs/wireless/abgn/img/vlans-on-wireless-01.webp)

[桥接VLAN过滤](../../bridging-and-switching/index.md#bridge-vlan-filtering) 提供了VLAN感知的Layer2转发功能，并可在桥接器内进行VLAN标签修改。

### R1

- 在以太网接口上添加必要的VLAN接口，使其成为VLAN中继端口（Trunk Port）。在VLAN接口上配置IP地址：

```ros
/interface/vlan
add interface=ether1 name=vlan111 vlan-id=111
add interface=ether1 name=vlan222 vlan-id=222

/ip/address
add address=192.168.1.1/24 interface=vlan111
add address=192.168.2.1/24 interface=vlan222
```

### R2

- 在wlan1接口下添加虚拟AP（VirtualAP），并为wlan1和wlan2创建无线安全配置文件：

```ros
/interface/wireless/security-profiles
add name=vlan111 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys wpa-pre-shared-key=secret111 wpa2-pre-shared-key=secret111
add name=vlan222 authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys wpa-pre-shared-key=secret222 wpa2-pre-shared-key=secret222
/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=ap-bridge security-profile=vlan111 ssid=vlan111 vlan-id=111 vlan-mode=use-tag
add disabled=no master-interface=wlan1 name=wlan2 security-profile=vlan222 ssid=vlan222 vlan-id=222 vlan-mode=use-tag
```

:::info
务必确保将wlan1、wlan2的vlan-mode设置为“use-tag”。
:::

- 创建一个启用*vlan-filtering=yes*的桥接器；
- 添加必要的桥接端口；
- 在*interface bridge vlan*部分下，添加带有正确*vlan-ids*的*标记（tagged）*接口：

```ros
/interface/bridge
add fast-forward=no name=bridge1 vlan-filtering=yes

/interface/bridge/port
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=wlan1
add bridge=bridge1 interface=wlan2
/interface/bridge/vlan
add bridge=bridge1 tagged=ether2,wlan1 vlan-ids=111
add bridge=bridge1 tagged=ether2,wlan2 vlan-ids=222
```

:::warning
某些设备内置交换芯片，能够以线速在以太网端口间交换数据包。桥接VLAN过滤会禁用某些设备的[硬件卸载](../../bridging-and-switching/index.md#bridge-hardware-offloading)功能，从而阻止数据包交换。这不会影响无线接口，因为通过无线接口的流量无论如何都无法卸载到交换芯片。
:::

:::tip
本配置中并非强制要求启用VLAN过滤，但出于安全考虑，强烈建议启用。若不启用VLAN过滤，在某些场景下未知VLAN ID可能被转发。禁用VLAN过滤确实能带来性能上的提升。
:::

### R3

- 在wlan1接口上添加IP地址；
- 创建与R2 wlan1兼容的无线安全配置文件：

```ros
/ip/address
add address=192.168.1.3/24 interface=wlan1

/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=station security-profile=vlan111 ssid=vlan111
```

### R4

- 在wlan1接口上添加IP地址；
- 创建与R2 wlan2兼容的无线安全配置文件：

```ros
/ip/address
add address=192.168.2.4/24 interface=wlan1

/interface/wireless
set [ find default-name=wlan1 ] disabled=no mode=station security-profile=vlan222 ssid=vlan222
```