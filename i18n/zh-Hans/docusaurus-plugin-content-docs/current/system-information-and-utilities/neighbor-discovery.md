# 邻居发现

> 邻居发现协议能够在二层域中使用 MNDP、CDP 或 LLDP 协议检测设备，显示已连接邻居的 IP/MAC 地址及接口信息。配置选项包括协议选择、发现间隔调整，以及用于 QoS 和 VLAN 共享的 LLDP TLV。

# 邻居发现

邻居发现协议允许我们在二层广播域中找到与 MNDP（MikroTik 邻居发现协议）、CDP（Cisco 发现协议）或 LLDP（链路层发现协议）兼容的设备。它们可用于绘制网络拓扑。

## 邻居列表

邻居列表显示二层广播域中发现的所有邻居。它显示邻居连接到哪个接口、其 IP/MAC 地址以及其他相关参数。该列表为只读。以下是一个邻居列表示例：

```ros
[admin@MikroTik] /ip/neighbor/print 
 # INTERFACE ADDRESS         MAC-ADDRESS       IDENTITY   VERSION    BOARD      
 0 ether13   192.168.33.2    00:0C:42:00:38:9F MikroTik   5.99       RB1100AHx2
 1 ether11   1.1.1.4         00:0C:42:40:94:25 test-host  5.8        RB1000   
 2 Local     10.0.11.203     00:02:B9:3E:AD:E0 c2611-r1   Cisco I...                    
 3 Local     10.0.11.47      00:0C:42:84:25:BA 11.47-750  5.7        RB750  
 4 Local     10.0.11.254     00:0C:42:70:04:83 tsys-sw1   5.8        RB750G    
 5 Local     10.0.11.202     00:17:5A:90:66:08 c7200      Cisco I...
```

**子菜单：** `/ip/neighbor`

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP*) | 被发现设备上配置的最高 IP 地址 |
| **address6** (*IPv6*) | 被发现设备上配置的 IPv6 地址 |
| **add-dns-entries** (*yes \| no*) | 指定是否为该特定邻居创建动态 DNS 条目，并使用 identity 作为域名 |
| **add-dns-entries-suffix** (*string*) | 为每个邻居创建的动态 DNS 条目添加的后缀。 |
| **age** (*time*) | 自上次发现数据包以来的时间间隔 |
| **discovered-by** (*cdp\|lldp\|mndp*) | 显示发现该邻居所使用的协议列表。该属性自 RouterOS 7.7 版本起可用。 |
| **board** (*string*) | RouterBoard 型号。仅对安装了 RouterOS 的设备显示 |
| **identity** (*string*) | 配置的系统标识 |
| **interface** (*string*) | 被发现设备所连接的接口名称 |
| **interface-name** (*string*) | 邻居设备上连接到 L2 广播域的接口名称。适用于 CDP。 |
| **ipv6** (*yes \| no*) | 显示设备是否启用了 IPv6。 |
| **mac-address** (*MAC*) | 远程设备的 MAC 地址。可用于通过 mac-telnet 连接。 |
| **platform** (*string*) | 平台名称。例如 "MikroTik"、"cisco" 等。 |
| **software-id** (*string*) | 远程设备上的 RouterOS 软件 ID。仅适用于安装了 RouterOS 的设备。 |
| **system-caps** (*string*) | 链路层发现协议（LLDP）报告的系统能力。 |
| **system-caps-enabled** (*string*) | 链路层发现协议（LLDP）报告的已启用系统能力。 |
| **unpack** (*none\|simple\|uncompressed-headers\|uncompressed-all*) | 显示发现数据包的压缩类型。 |
| **uptime** (*time*) | 远程设备的运行时间。仅对安装了 RouterOS 的设备显示。 |
| **version** (*string*) | 远程设备上已安装软件的版本号 |
| **running** (string array) | 报告邻居设备上正在运行的"功能"列表。目前仅列出 "CAPsMAN" 功能。 |

:::warning
为避免内存耗尽，每个接口的邻居条目数量限制为（总内存（MB）\* 16）。
:::

### LLDP 邻居

通过 LLDP 发现的邻居在 `/ip/neighbor/lldp` 下的单独只读菜单中显示。此菜单显示从邻居设备接收到的详细 LLDP 类型-长度-值（TLV）。

与聚合所有发现协议（MNDP、CDP 和 LLDP）邻居的通用 `/ip/neighbor` 菜单不同，`/ip/neighbor/lldp` 仅显示通过 LLDP 发现的条目。

输出示例：

```ros
[admin@Switch] > /ip/neighbor/lldp/print
Columns: INTERFACE, ADDRESS4, ADDRESS6, MAC-ADDRESS, LLDP-CHASSIS-ID, LLDP-PORT-ID, LLDP-PORT-DESCRIPTION, LLDP-SYSTEM-NAME, LLDP-SYSTEM-DESCRIPTION
#  INTERFACE  ADDRESS4        ADDRESS6                   MAC-ADDRESS        LLDP-CHASSIS-ID    LLDP-PORT-ID  LLDP-PORT-DESCRIPTION  LLDP-SYSTEM-NAME  LLDP-SYSTEM-DESCRIPTION                                                     
0  ether2     192.168.88.128  fe80::f61e:57ff:fe13:d794  F4:1E:57:13:D7:94  F4:1E:57:13:D7:94  ether1        ether1                 Tested_CRS812     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS812-8DS-2DQ-2DDQ 
   bridge1                                                                                                                                                                                                                        
1  ether3     192.168.88.127  fe80::f61e:57ff:fe47:9255  F4:1E:57:47:92:55  F4:1E:57:47:92:55  ether1        ether1                 Tested_CRS520     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS520-4XS-16XQ     
   bridge1                                                                                                                                                                                                                        
2  ether4     192.168.88.9    fe80::1afd:74ff:fe81:9a    18:FD:74:81:00:9A  18:FD:74:81:00:86  ether1        ether1                 Tester6           MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CCR2216-1G-12XS-2XQ 
   bridge1                                                                                                                                                                                                                        
3  ether5     192.168.88.132  fe80::d601:c3ff:fe43:c035  D4:01:C3:43:C0:35  D4:01:C3:43:C0:35  ether1        ether1                 Tested_L009       MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 L009UiGS            
   bridge1                                                                                                                                                                                                                        
4  ether8     192.168.88.129  fe80::f61e:57ff:fec2:8a3d  F4:1E:57:C2:8A:3D  F4:1E:57:C2:8A:2B  ether17       ether17                Tested_CRS418     MikroTik RouterOS 7.24rc1 (testing) 2026-07-01 13:53:30 CRS418-8P-8G-2S+    
   bridge1   
```

:::note
`lldpRemTable` SNMP 表仅报告通过 LLDP 发现的邻居。仅通过 CDP 或 MNDP 发现的条目不包含在 SNMP LLDP-MIB 中。
:::

## 发现配置

可以使用接口列表更改接口是否参与邻居发现。如果接口包含在发现接口列表中，它将发送关于系统的基本信息，并处理在二层网络中广播的接收发现数据包。从接口列表中移除接口将同时禁用该接口上的邻居发现以及在该接口上发现此设备本身的可能性。

**子菜单：** `/ip/neighbor/discovery-settings`

| 属性 | 描述 |
| :-- | :-- |
| **discover-interface-list** (*string*; 默认值：**static**) | 发现协议将运行的接口列表。 |
| **discover-interval** (*time: 5s..9h6m8s*; 默认值：**30s**) | 调整邻居发现数据包的发送频率。它还使用公式调整 CDP 和 LLDP 数据包的生存时间（TTL）TLV 值：（`discover-interval` \* 4）+ 1。该设置自 RouterOS 7.16 版本起可用。 |
| **dying-gasp** (*yes \| no*; 默认值：**no**) | 是否在优雅重启、关机或升级前发送 TTL=0 的邻居发现数据包。在断电或内核崩溃的情况下不会发送 dying gasp 数据包。在接收端，TTL=0 的数据包会立即移除相应的邻居条目，无论本地的 `dying-gasp` 设置如何。 |
| **lldp-dcbx** (*yes \| no*; 默认值：**no**) | 是否发送数据中心桥接能力交换协议（DCBX）TLV，该协议允许使用 LLDP 与其他邻居设备通信交换机的 [QoS 设置](../bridging-and-switching/quality-of-service.md) 和能力。仅适用于带有 Marvell Prestera 交换芯片的 MikroTik 设备（例如 CRS3xx）。启用 DCBX 包括以下 TLV：ETS（增强传输选择）配置 TLV。此 TLV 用于共享交换机的 ETS 配置。它包括：意愿位，指示设备是否愿意接受来自邻居设备的 QoS 配置。在 RouterOS 中，意愿位设置为禁用，意味着交换机不会接受远程配置，而是使用自身设置。优先级分配表，将优先级映射到特定的流量类别。带宽分配表，RouterOS 根据 <code>weight</code> 属性计算分配给每个队列的带宽百分比。这适用于在 <code>`/interface/ethernet/switch/qos/tx-manager/queue`</code> 设置中使用 <code>high-priority-group</code> 的队列。传输选择算法（TSA）表，其中 <code>high-priority-group</code> 队列分配给 ETS，<code>strict-priority</code> 队列分配给严格优先级，<code>low-priority-group</code> 或非硬件卸载队列分配给厂商特定算法。ETS 推荐 TLV。此 TLV 提供邻居设备应如何配置 ETS 的建议。RouterOS 使用与 ETS 配置 TLV 中相同的数据来给出建议。基于优先级的流控配置 TLV。此 TLV 用于共享 PFC 配置。与 ETS TLV 类似，意愿位设置为禁用，意味着交换机不接受远程 PFC 配置。PFC 根据 <code>`/interface/ethernet/switch/qos/priority-flow-control`</code> 和 <code>`/interface/ethernet/switch/qos/port`</code> 下配置的设置，为特定优先级启用。应用优先级 TLV。此 TLV 用于通信网络中不同应用的优先级。应用 VLAN TLV。此 TLV 用于共享应用的 VLAN 配置。RouterOS 目前不支持在此 TLV 中发送值，将发送空的 VLAN 表。 |
| **lldp-mac-phy-config**(*yes \| no*; 默认值：**no**) | 是否在 LLDP 中发送 MAC/PHY 配置/状态 TLV，该 TLV 指示接口能力、双工状态的当前设置、比特率和自动协商。仅适用于以太网接口。虽然该 TLV 在 LLDP 中是可选的，但在发送 LLDP-MED 时是强制性的，这意味着即使该属性配置为禁用，必要时也会包含此 TLV。 |
| **lldp-max-frame-size** (*yes \| no*; 默认值：**no**) | 是否在 LLDP 中发送最大帧大小 TLV，该 TLV 以字节为单位指示接口的最大帧大小能力（`l2mtu` + 18）。仅适用于以太网接口。 |
| **lldp-med** (*yes \| no*; 默认值：**yes**) | 指定是否通告 LLDP-MED 媒体能力 TLV。当使用 `lldp-med-net-policy-vlan` 时，必须启用此选项。该设置自 RouterOS 7.23 版本起可用。 |
| **lldp-poe-power** (*yes \| no*; 默认值：**yes**) | 两个特定的 TLV 用于促进供电设备（PSE）和受电设备（PD）之间的以太网供电（PoE）管理：IEEE 802.3 组织特定通过 MDI 供电 TLV。TIA-1057（LLDP-MED）组织特定通过 MDI 扩展供电 TLV。`lldp-poe-power` 属性决定是否在 LLDP 消息中传输 IEEE 802.3 组织特定通过 MDI 供电 TLV。LLDP-MED 组织特定通过 MDI 扩展供电 TLV 的传输不可配置。当远程设备已传输接收供电的 LLDP-MED 能力时，它会自动包含在发出的 LLDP-MED 数据包中。这些 TLV 仅与支持 [PoE-Out](../hardware/poe-out.mdx) 的以太网接口相关。该设置自 RouterOS 7.15 版本起可用，并取代了 PoE-out 端口的 `poe-lldp-enabled` 设置。 |
| **lldp-med-net-policy-vlan** (*integer 0..4094*; 默认值：**disabled**) | LLDP-MED 网络策略 TLV 的通告 VLAN ID。这允许为支持 LLDP-MED 的设备（如 VoIP 电话）分配 VLAN ID。该 TLV 仅会添加到发现 LLDP-MED 能力设备且启用了 `lldp-med` 的接口上。其他 TLV 值是预定义的，无法更改：应用类型 - 语音。VLAN 类型 - 标记。L2 优先级 - 0。DSCP 优先级 - 0。与桥接接口一起使用时，应通过 `protocol-mode` 设置启用（R/M）STP 协议。此外，应通过 `protocol` 设置排除其他邻居发现协议（例如 CDP），以避免 LLDP-MED 配置错误。 |
| **lldp-vlan-info** (*yes \| no;* 默认值：**no**) | 是否在 LLDP 中发送与 VLAN 相关的 IEEE 802.1 组织特定 TLV。启用此设置后，将通告三个 TLV：端口 VLAN ID。这适用于桥接端口的 <code>pvid</code> 属性。端口和协议 VLAN ID。此 TLV 未被使用，始终指示"不支持"和"未启用"。VLAN 名称。这包括来自 "<code>`/interface/bridge/vlan`</code>" 表中最多 10 个活动 VLAN。这些 TLV 与添加到 [vlan-filtering](../bridging-and-switching/index.md#bridge-vlan-filtering) 桥接的接口相关，该设置自 RouterOS 7.16 版本起可用。 |
| **mode** (*rx-only \| tx-only \| tx-and-rx*; 默认值：**tx-and-rx**) | 选择邻居发现数据包的发送和接收模式。该设置自 RouterOS 7.7 版本起可用。 |
| **protocol** (*cdp \| lldp \| mndp*; 默认值：**cdp,lldp,mndp**) | 使用的发现协议列表。 |

自 RouterOS v6.44 起，邻居发现在各个从属接口上独立工作。当主接口（例如 bonding 或 bridge）包含在发现接口列表中时，其所有从属接口将自动参与邻居发现。可以仅允许在某些从属接口上进行邻居发现。为此，请将特定从属接口包含在列表中，并确保主接口不包含在内。

```ros
/interface/bonding
add name=bond1 slaves=ether5,ether6
/interface/list
add name=only-ether5
/interface/list/member
add interface=ether5 list=only-ether5
/ip/neighbor/discovery-settings
set discover-interface-list=only-ether5
```

现在邻居列表显示收到发现消息的主接口和实际从属接口。

```ros
[admin@R2] > ip neighbor print
 # INTERFACE ADDRESS                                           MAC-ADDRESS       IDENTITY   VERSION    BOARD         
 0 ether5    192.168.88.1                                      CC:2D:E0:11:22:33 R1         6.45.4 ... CCR1036-8G-2S+
   bond1    
```

## LLDP

根据 RouterOS 配置，LLDP 消息中可以发送不同的类型-长度-值（TLV）。这包括：

- 机箱 ID（MAC 地址）。
- 端口 ID（接口名称）。
- 生存时间。
- 系统名称（系统标识）。
- 系统描述（平台 - MikroTik，软件版本 - RouterOS 版本，硬件名称 - RouterBoard 名称）。
- 管理地址（端口上配置的所有 IP 地址）。
- 系统能力（已启用的系统能力，例如桥接或路由器）。
- 端口描述（如果发送接口是 bridge 或 bond 的一部分，则为组合接口名称，如 "bridge/ether1"，或与端口 ID 相同的接口名称）。
- IEEE 802.1 端口 VLAN ID。
- IEEE 802.1 端口和协议 VLAN ID。
- IEEE 802.1 VLAN 名称。
- IEEE 802.3 MAC/PHY 配置/状态。
- IEEE 802.3 通过 MDI 供电。
- IEEE 802.3 最大帧大小。
- LLDP-MED 媒体能力（MED 能力列表）。
- LLDP-MED 网络策略（为语音流量分配的 VLAN ID）。
- LLDP-MED 通过 MDI 扩展供电。
- LLDPDU 结束。