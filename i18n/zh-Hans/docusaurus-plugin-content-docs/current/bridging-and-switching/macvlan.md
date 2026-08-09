# MACVLAN

> MACVLAN 允许在物理接口上创建多个具有唯一 MAC 地址的虚拟网络接口，从而实现高效的 IP 地址管理和独立的 PPPoE 连接。它在 MAC 层运行，无需 VLAN 标记，但存在限制，如数据包接收受限，并且在桥接场景下需要谨慎配置。

# MACVLAN

MACVLAN 提供了一种创建多个虚拟网络接口的方法，每个接口都拥有自己唯一的媒体访问控制（MAC）地址，并依附于物理网络接口。该技术用于解决特定的网络需求，例如从单个物理以太网接口获取多个 IP 地址，或使用不同的 MAC 地址建立独立的 PPPoE 客户端连接。与依赖带 VLAN 标识符的以太网帧的传统 [VLAN](./vlan.md)（虚拟局域网）接口不同，MACVLAN 在 MAC 地址层面运行，使其成为特定网络场景中通用且高效的解决方案。

:::info
MACVLAN 接口只能接收广播数据包、发往其自身 MAC 地址的数据包以及有限数量的组播地址。如果物理接口配置了 VLAN，则 MACVLAN 接口无法接收来自该 VLAN 的数据包。

对于涉及 VLAN 的桥接和更复杂的 Layer2 解决方案，应使用专用交换机。
:::

## 基本配置示例

设想一个场景：ether1 接口连接到您的 ISP，而您的路由器需要租用两个 IP 地址，每个地址对应不同的 MAC 地址。传统上，这需要使用两个物理以太网接口和一个额外的交换机。然而，更高效的解决方案是创建一个虚拟 MACVLAN 接口。

要创建 MACVLAN 接口，请选择所需的以太网接口。如果未手动指定，将自动分配一个 MAC 地址：

```ros
/interface/macvlan
add interface=ether1 name=macvlan1

/interface/macvlan/print
Flags: R - RUNNING
Columns: NAME, MTU, INTERFACE, MAC-ADDRESS, MODE
#   NAME       MTU  INTERFACE  MAC-ADDRESS        MODE  
0 R macvlan1  1500  ether1     76:81:BF:68:69:83  bridge
```

现在，可以在 ether1 和 macvlan1 接口上创建 DHCP 客户端：

```ros
/ip/dhcp-client
add interface=ether1
add interface=macvlan1
```

## 属性参考

**子菜单：** `/interface/macvlan`

MACVLAN 接口的配置设置。

| 属性 | 描述 |
| :-- | :-- |
| **arp** (*disabled \| enabled \| local-proxy-arp \| proxy-arp \| reply-only*；默认值：**enabled**) | 地址解析协议设置<code>disabled</code> - 接口将不使用 ARP<code>enabled</code> - 接口将使用 ARP<code>local-proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到同一接口<code>proxy-arp</code> - 路由器在接口上执行代理 ARP，并将回复发送到其他接口<code>reply-only</code> - 接口将仅回复来自匹配的 IP 地址/MAC 地址组合的请求，这些组合作为静态条目输入到 IP/ARP 表中。不会自动在 IP/ARP 表中存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **arp-timeout** (*auto \| integer*；默认值：**auto**) | 设置在没有从 IP 接收到数据包后，ARP 记录在 ARP 表中保留的时间。值 `auto` 等于 `/ip/settings/` 中 `arp-timeout` 的值，默认为 30 秒。 |
| **comment** (*string*；默认值：) | 接口的简短描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 更改接口是否禁用。 |
| **interface** (*name*；默认值：) | MACVLAN 将运行的底层接口名称。MACVLAN 接口可以在任何具有 MAC 地址的接口上创建。**警告：** 不支持在 MACVLAN 接口之上添加 VLAN 接口。不支持在已桥接或已绑定的接口上添加 MACVLAN。 |
| **loop-protect** (*on \| off \| default*；默认值：**default**) | 启用或禁用接口上的环路保护，**default** 相当于关闭。 |
| **loop-protect-disable-time** (*time interval \| 0*；默认值：**5m**) | 设置检测到环路时禁用所选接口的时间。**0** - 永久禁用。 |
| **loop-protect-send-interval** (*time interval*；默认值：**5s**) | 设置环路保护数据包在所选接口上发送的频率。 |
| **mac-address** (*MAC*；默认值：) | 接口的静态 MAC 地址。未指定时将分配一个随机生成的 MAC 地址。 |
| **mode** (*private \| bridge*；默认值：**bridge**) | 设置 MACVLAN 接口模式：<code>private</code> - 不允许同一父接口上的 MACVLAN 实例之间通信。<code>bridge</code> - 允许同一父接口上的 MACVLAN 实例之间通信。 |
| **mtu** (*integer*；默认值：**1500**) | 设置 Layer 3 最大传输单元。对于 MACVLAN 接口，其值不能高于父 **interface**。 |
| **name** (*string*；默认值：) | 接口名称。 |