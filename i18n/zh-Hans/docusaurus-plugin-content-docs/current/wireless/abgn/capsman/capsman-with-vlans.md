# 使用 VLAN 的 CAPsMAN

> 本页说明如何在 MikroTik RouterOS 中配置带 VLAN 的 CAPsMAN，实现集中式无线管理，并为不同客户端组进行 VLAN 标记。内容涵盖本地转发模式设置、配置规则、DHCP 配置以及交换机上的 VLAN 过滤。

# 使用 VLAN 的 CAPsMAN

## 概述

可以为家庭或办公环境创建可扩展至多个接入点的集中式接入点管理方案。此类配置相当简单，已在 [简单 CAPsMAN 设置](./ap-controller-capsman.md#simple-setup-of-a-capsman-system) 指南中说明，但对于更复杂的场景，可能需要使用 VLAN。CAPsMAN 具有在特定条件下分配特定 VLAN ID 的功能。本指南将举例说明如何根据无线客户端所连接的 AP 为其分配 VLAN ID。带 VLAN 的 CAPsMAN 可以通过 [本地转发模式](./ap-controller-capsman.md#local-forwarding-mode) 或 [CAPsMAN 转发模式](./ap-controller-capsman.md#manager-forwarding-mode) 实现。本地转发模式允许在 AP 与 CAPsMAN 路由器之间使用交换机进行数据包交换（以获得更高吞吐量），而 CAPsMAN 转发模式则适用于所有流量都应始终转发至 CAPsMAN 路由器（大多数情况下用于数据包过滤）的场景。

在本示例中，我们将为连接到 **WiFi\_WORK** 的所有无线客户端分配 **VLAN10**，为连接到 **WiFi\_GUEST** 的无线客户端分配 **VLAN20**。我们将使用 Virtual AP 配合 CAPsMAN，在单个物理设备上创建多个 SSID 供无线客户端连接。同时，也会通过 CAPsMAN 配置规则演示如何为单个物理设备使用单一 SSID。

## 使用本地转发模式

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/capsman-with-vlans-01.webp)

在本地转发模式下，CAPsMAN 路由器将配置分发到所有由其管理的 CAP。在本地转发模式下，流量无需发送至 CAPsMAN 路由器，而是可以在转发流量时不经过 CAPsMAN 路由器而直接发送至其他路由器。此模式允许在无线客户端流量发送至网络之前，为其标记特定的 VLAN ID，从而可以利用交换机将特定 VLAN ID 限制在特定端口。在本地转发模式下，流量不会使用特殊的 CAPsMAN 报头进行封装（该报头只能由 CAPsMAN 路由器去除）。

### CAPsMAN 路由器

- 为每个 VLAN 创建相应的 CAP 配置：

```
/caps-man/configuration
add country=latvia datapath.local-forwarding=yes datapath.vlan-id=10 datapath.vlan-mode=use-tag name=Config_WORK security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_work_password ssid=WiFi_WORK
add country=latvia datapath.local-forwarding=yes datapath.vlan-id=20 datapath.vlan-mode=use-tag name=Config_GUEST security.authentication-types=\
    wpa-psk,wpa2-psk security.passphrase=secret_guest_password ssid=WiFi_GUEST
```

- 我们将创建一条 CAPsMAN 配置规则，在单个设备上创建 **WiFi\_WORK** 和 **WiFi\_GUEST** SSID，每个连接的 CAP 将自动创建这些 SSID。

```
/caps-man/provisioning
add action=create-dynamic-enabled master-configuration=Config_WORK slave-configurations=Config_GUEST
```

:::info
您可以通过添加多个 slave-configurations 来创建更多 Virtual AP。这需要事先创建多个 CAPsMAN 配置。
:::

- 出于安全考虑，将 CAPsMAN 限制在单个接口上：

```
/caps-man/manager/interface
set [ find default=yes ] forbid=yes
add disabled=no interface=ether1
```

- 启用 CAPsMAN 管理器：

```
/caps-man/manager
set enabled=yes
```

- 为每个 VLAN 设置 DHCP 服务器：

```
/interface/vlan
add interface=ether1 name=VLAN10 vlan-id=10
add interface=ether1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
/ip/pool
add name=dhcp_pool10 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool20 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool10 disabled=no interface=VLAN10 name=dhcp10
add address-pool=dhcp_pool20 disabled=no interface=VLAN20 name=dhcp20
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=8.8.8.8 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=8.8.8.8 gateway=192.168.20.1
```

### 交换机

在本示例中，我们将使用 [Bridge VLAN 过滤](../../../bridging-and-switching/index.md#vlan-example-trunk-and-access-ports) 来过滤未知 VLAN，并将其他设备分配到相同网络。某些设备能够将此功能卸载到内置交换芯片，请参阅 [基本 VLAN 交换](../../../bridging-and-switching/user-guides/basic-vlan-switching.md) 指南，了解如何在不同类型的设备上进行配置。

- 设置 Bridge VLAN 过滤：

```
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1
add bridge=bridge1 interface=ether2
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4 pvid=10
add bridge=bridge1 interface=ether5 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=ether1,ether2,ether3 untagged=ether4 vlan-ids=10
add bridge=bridge1 tagged=ether1,ether2,ether3 untagged=ether5 vlan-ids=20
```

:::info
在本示例中，CAP 与 CAPsMAN 路由器之间将使用未标记流量进行通信。默认情况下，如果未更改 PVID，未标记流量将在具有相同 PVID 值（包括默认 PVID）的端口之间转发。
:::

### CAP

- 创建桥接并分配连接到 CAPsMAN 路由器的端口：

```
/interface/bridge
add name=bridge1
/interface/bridge/port
add bridge=bridge1 interface=ether1
```

- 在 AP 上启用 CAP 模式，并确保指定使用新创建的桥接：

```
/interface/wireless/cap
set bridge=bridge1 discovery-interfaces=bridge1 enabled=yes interfaces=wlan1
```

- CAP 成功连接到 CAPsMAN 路由器后，wlan1（SSID **WiFi\_WORK**）和新创建的虚拟 wlan5（SSID **WiFi\_GUEST**）接口将作为桥接端口动态添加。VLAN 被分配给无线接口，因此来自无线的所有数据都会被标记，且只有带有此标记的数据才会通过无线发送。如果不需要额外的 VLAN 管理和控制，可以禁用 Bridge vlan-filtering。关联的 VLAN 可以通过端口 VLAN ID（PVID）属性查看：

```
[admin@CAP_1] /interface/bridge/port/pr
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                     BRIDGE                    HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0   H ether1                        bridge1                   yes    1     0x80         10                 10       none
 1  D  wlan1                         bridge1                         10     0x80         10                 10       none
 2  D  wlan5                         bridge1                         20     0x80         10                 10       none
```

就这样！将无线客户端连接到您的 AP 并检查连通性。

## 使用 CAPsMAN 转发模式

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/capsman-with-vlans-02.webp)

在 CAPsMAN 转发模式下，来自 CAP 的所有流量都使用特殊的 CAPsMAN 报头进行封装，该报头只能由 CAPsMAN 路由器去除。这意味着交换机将无法区分 CAP 设置的 VLAN ID，因为 VLAN 标记也会被封装。此模式限制了在 Layer2 网络中分流流量的可能性，但允许您通过 Layer3 网络将每个 CAP 的流量转发到远程 CAPsMAN 路由器进行处理。当您需要控制多个远程位置的 CAP，但希望使用中央网关时，此模式非常有用。

### CAPsMAN 路由器

- 设置 Bridge VLAN 过滤以将接口限制到相应的 VLAN：

```
/interface/bridge
add name=bridge1 vlan-filtering=yes
/interface/bridge/port
add bridge=bridge1 interface=ether1 pvid=10
add bridge=bridge1 interface=ether2 pvid=20
/interface/bridge/vlan
add bridge=bridge1 tagged=bridge1 untagged=ether1 vlan-ids=10
add bridge=bridge1 tagged=bridge1 untagged=ether2 vlan-ids=20
```

:::info
 CAPsMAN 会将 CAP 接口附加到桥接上，并自动在桥接 VLAN 表中添加相应的条目。
:::

- 为每个 VLAN 创建相应的 CAP 配置：

```
/caps-man/configuration
add country=latvia datapath.bridge=bridge1 datapath.vlan-id=10 datapath.vlan-mode=use-tag name=Config_WORK security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_work_password ssid=WiFi_WORK
add country=latvia datapath.bridge=bridge1 datapath.vlan-id=20 datapath.vlan-mode=use-tag name=Config_GUEST security.authentication-types=wpa-psk,wpa2-psk \
    security.passphrase=secret_guest_password ssid=WiFi_GUEST
```

- 我们将创建一条 CAPsMAN 配置规则，在单个设备上创建 **WiFi\_WORK** 和 **WiFi\_GUEST** SSID，每个连接的 CAP 将自动创建这些 SSID

```
/caps-man/provisioning
add action=create-dynamic-enabled master-configuration=Config_WORK slave-configurations=Config_GUEST
```

:::info
您可以通过添加多个 slave-configurations 来创建更多 Virtual AP。这需要事先创建多个 CAPsMAN 配置。
:::

- 出于安全考虑，将 CAPsMAN 限制在 CAP 将要连接的接口上：

```
/caps-man/manager/interface
set [ find default=yes ] forbid=yes
add disabled=no interface=ether3
add disabled=no interface=ether4
```

- 启用 CAPsMAN 管理器：

```
/caps-man/manager
set enabled=yes
```

- 为每个 VLAN 设置 DHCP 服务器：

```
/interface/vlan
add interface=bridge1 name=VLAN10 vlan-id=10
add interface=bridge1 name=VLAN20 vlan-id=20
/ip/address
add address=192.168.10.1/24 interface=VLAN10
add address=192.168.20.1/24 interface=VLAN20
/ip/pool
add name=dhcp_pool10 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool20 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool10 disabled=no interface=VLAN10 name=dhcp10
add address-pool=dhcp_pool20 disabled=no interface=VLAN20 name=dhcp20
/ip/dhcp-server/network
add address=192.168.10.0/24 dns-server=8.8.8.8 gateway=192.168.10.1
add address=192.168.20.0/24 dns-server=8.8.8.8 gateway=192.168.20.1
```

### CAP

- 在每个 AP 上启用 CAP 模式，指定连接到 CAPsMAN 路由器的接口：

```
/interface/wireless/cap
set discovery-interfaces=ether1 enabled=yes interfaces=wlan1
```

- CAP 成功连接到 CAPsMAN 路由器后，CAPsMAN 路由器上将动态创建两个 CAP 接口。由于通过 datapath.bridge=bridge1 显式选择了桥接接口，并使用默认的 CAPsMAN 转发模式 datapath.local-forwarding=no，这两个接口都将作为桥接端口动态添加到同一 CAPsMAN 路由器上。由于使用了启用 vlan-filtering 的桥接，两个 CAP 接口也会出现在桥接 VLAN 表中：

```
[admin@CAPsMAN_Router] /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload 
 #     INTERFACE                       BRIDGE                      HW  PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
 0     ether1                          bridge1                     yes   10     0x80         10                 10       none
 1     ether2                          bridge1                     yes   20     0x80         10                 10       none
 2  D  cap16                           bridge1                           10     0x80         10                 10       none
 3  D  cap17                           bridge1                           20     0x80         10                 10       none
[admin@CAPsMAN_Router] /interface/bridge/vlan/print
Flags: X - disabled, D - dynamic 
 #   BRIDGE                         VLAN-IDS  CURRENT-TAGGED                         CURRENT-UNTAGGED                        
 0 D bridge1                        1                                                bridge1                                 
 1   bridge1                        10        cap16                                  ether1                                  
 2   bridge1                        20        cap17                                  ether2  
```

就这样！将无线客户端连接到您的 AP 并检查连通性。

## 案例研究

### 不使用 Virtual AP

并非所有人都希望创建 Virtual AP，因为这会降低总吞吐量。如果您希望使用多个设备创建多个 SSID，则可以根据 CAP 的身份为其分配特定配置。要实现此目的，您应该使用 CAPsMAN 配置规则配合 RegEx 表达式。在本示例中，我们将为身份设置为 "**AP\_WORK\_\***" 的 CAP 分配 **Config\_WORK** 配置，为身份设置为 "**AP\_GUEST\_\***" 的 CAP 分配 **Config\_GUEST** 配置。为此，您只需更改 CAPsMAN 配置规则。

- 移除任何现有的配置规则：

```
/caps-man/provisioning/remove [f]
```

- 创建新的配置规则，根据 CAP 的身份为其分配相应的配置：

```
/caps-man/provisioning
add action=create-dynamic-enabled identity-regexp=^AP_GUEST_ master-configuration=Config_GUEST
add action=create-dynamic-enabled identity-regexp=^AP_WORK_ master-configuration=Config_WORK
```

:::note
不要忘记在 CAP 上设置正确的身份，因为 CAPsMAN 将根据其身份在 AP 上分配相应的配置。
:::