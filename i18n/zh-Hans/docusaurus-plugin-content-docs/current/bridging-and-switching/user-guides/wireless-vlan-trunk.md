# Wireless VLAN Trunk

> 本页说明如何在 MikroTik RouterOS 上使用桥接 VLAN 过滤配置无线 VLAN 中继，允许通过无线 PtP 链路选择性转发特定 VLAN，同时阻止其他 VLAN。内容包括桥接设置、VLAN 表配置、接口访问控制以及硬件卸载 VLAN 处理。

# Wireless VLAN Trunk

一个非常常见的任务是通过无线点对点（PtP）链路仅转发特定的一组 VLAN。这可以通过桥接 VLAN 过滤来实现，应优先于其他任何方法（包括桥接 VLAN 接口）。假设我们需要通过无线链路转发 2 个不同的 VLAN，而所有其他 VLAN ID 应被丢弃。VLAN 10 将用于我们的互联网流量，而 VLAN 99 将用于我们的管理流量。以下为网络拓扑：

![Wireless VLAN Trunk](https://manual.mikrotik.com/docs/bridging-and-switching/user-guides/img/wireless-vlan-trunk-01.webp)

## 配置

首先在 **AP** 和 **ST** 上创建一个新的桥接，并将 **ether1** 和 **wlan1** 端口添加到其中：

```ros
/interface/bridge
add name=bridge protocol-mode=none
/interface/bridge/port
add bridge=bridge interface=ether1
add bridge=bridge interface=wlan1
```

:::info
如有需要，可以启用 RSTP，但通常 PtP 链路不需要 RSTP，因为不应存在环路发生的可能。
:::

出于安全原因，由于您只期望接收带标签的流量，应启用入口过滤（ingress-filtering）。然后可以设置桥接以过滤掉所有未标记的流量。请在 **AP** 和 **ST** 上执行以下操作：

```ros
/interface/bridge/port
set [find where interface=ether1 or interface=wlan1] frame-types=admit-only-vlan-tagged ingress-filtering=yes
```

设置桥接 VLAN 表。由于 VLAN99 将用于我们的管理流量，因此需要允许此 VLAN ID 访问桥接接口，否则一旦您尝试访问设备，流量将被丢弃。VLAN10 不需要访问桥接，因为它仅用于转发到另一端。为实现此功能，请在 **AP** 和 **ST** 的桥接 VLAN 表中添加以下条目：

```ros
/interface/bridge/vlan
add bridge=bridge tagged=ether1,wlan1 vlan-ids=10
add bridge=bridge tagged=ether1,wlan1,bridge vlan-ids=99
```

:::info 接口访问控制
您可以通过接口限制对设备的管理访问。如果您希望阻止来自特定接口（例如 `wlan1`）的访问，只需将该接口从相应的桥接 VLAN 条目中移除即可。
:::

:::warning 处理无线与硬件卸载 VLAN
对于支持硬件卸载 VLAN 过滤和无线功能的设备（例如 RB4011、LtAP），请务必谨慎。如果未明确允许该 VLAN 的 CPU 访问，从硬件卸载端口流向无线接口的数据包可能会被丢弃。

要允许特定 VLAN 的 CPU 访问：

* **将桥接接口添加** 为该 VLAN 的成员（参见 VLAN99 示例）。
* **或者，禁用受影响桥接端口的硬件卸载**。
:::

所有设备（**R1**、**R2**、**AP** 和 **ST**）都需要创建一个 VLAN 接口，以便通过特定 VLAN ID 访问设备。对于 **AP** 和 **ST**，请在桥接接口之上创建 VLAN 接口并分配 IP 地址：

```ros
/interface/vlan
add interface=bridge name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

对于 **R1** 和 **R2**，执行相同操作，但需要创建 VLAN 接口的接口可能会根据您的设置而有所不同：

```ros
/interface/vlan
add interface=ether1 name=MGMT vlan-id=99
/ip/address
add address=192.168.99.X/24 interface=MGMT
```

:::info
要允许转发更多 VLAN，只需在桥接 VLAN 表中指定更多 VLAN ID，您可以用逗号分隔多个 VLAN，甚至指定 VLAN 范围。
:::

### 在 **AP** 上设置无线链路

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

### 在 **ST** 上设置无线链路

```ros
/interface/wireless/security-profiles
add authentication-types=wpa2-psk mode=dynamic-keys name=wlan_sec wpa2-pre-shared-key=use_a_long_password_here
/interface/wireless
set wlan1 band=5ghz-a/n/ac channel-width=20/40/80mhz-Ceee disabled=no mode=station-bridge scan-list=5180 security-profile=wlan_sec ssid=ptp_test
```

:::info
每种类型的设置都有不同的要求。对于 PtP 链路，通常使用 NV2 无线协议。您可以在 [NV2 手册](../../wireless/abgn/nv2.md) 页面上了解更多关于 NV2 的信息。
:::

当链路设置完成后，您可以在 **AP** 和 **ST** 上启用桥接 VLAN 过滤：

```ros
/interface/bridge
set bridge vlan-filtering=yes
```

:::danger
在启用 VLAN 过滤之前，请仔细检查桥接 VLAN 表。配置错误的桥接 VLAN 表可能导致设备无法访问，可能需要重置配置。
:::