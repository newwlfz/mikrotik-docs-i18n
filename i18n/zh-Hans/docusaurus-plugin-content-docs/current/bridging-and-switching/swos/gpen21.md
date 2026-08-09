# GPEN21 系列手册

> MikroTik GPEN21 智能 PoE 供电注入器与中继器的 SwOS Lite 手册：功能、端口设置、VLAN 及交换机管理。

# GPEN21 系列手册

## 概述

GPEN21 是一款智能供电注入器，可作为先进的软件控制中继器使用。它不仅能通过 PoE 为上行链路设备供电，还能提供一系列实用的软件功能。GPEN21 配备一个以太网端口和一个用于光纤连接的 SFP 端口。客户可以选择使用 GPEN21 为光模块供电以实现与运营商的上行连接，或提供 PoE 为以太网上行链路供电（该链路使用我们的 GPeR 和/或 netPower 产品）。GPEN21 设备可以牢固地安装在墙壁或通信机柜上。以太网线缆可根据需要直接穿过设备底部的线缆开口或引入墙内。

SwOS Lite 是一款专为 MikroTik GPEN21 产品管理而设计的操作系统。GPEN21 仅支持 SwOS Lite 操作系统。

---

## GPEN21 系列特性

| 特性 | 描述 |
| --- | --- |
| **转发** | 全线速无阻塞交换；主机表中最多支持 2k 条 MAC 条目 ¹；转发表仅基于 SVL 工作；支持巨型帧 - 10222 字节 |
| **监控** | SNMP；链路故障检测；SFP 诊断；接口统计 |
| **VLAN** | 完全兼容 IEEE802.1Q；基于端口的 VLAN；最多支持 250 条 VLAN 条目（受 SwOS 限制）；VLAN 过滤 |
| **安全** | 端口锁定；广播风暴控制 |
| **服务质量（QoS）** | 入口流量限制；出口流量限制 |
| **访问控制列表** | 入口 ACL 表；最多支持 32 条 ACL 规则（受 SwOS 限制）；基于端口、L2、L3、L4 协议头字段的分类；ACL 操作包括过滤、转发和修改协议头字段 |

¹ 主机表限制不影响转发，因为即使达到 MAC 学习上限，数据包仍会在上行和下行端口之间正常转发。

---

## 连接设备

打开您的网页浏览器，输入设备的 IP 地址（默认为 192.168.88.1），将出现登录界面。设备也可以运行 DHCP 客户端，请检查 DHCP 服务器是否分配了其他 IP 地址。

![Gpen21 登录](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-01.webp)

SwOS 默认 IP 地址：**192.168.88.1**，用户名：**admin**，无密码。

可以使用 [MikroTik 邻居发现](../../system-information-and-utilities/neighbor-discovery) 来发现 MikroTik 交换机的 IP 地址。不支持 LLDP。

---

## 界面概览

SwOS 界面菜单根据设备型号包含多个选项卡。以下是所有可能的 SwOS 菜单：Link、SFP、Forwarding、Stats、Errors、Hist、VLAN、VLANs、Hosts、SNMP、ACL、System 和 Upgrade。

SwOS 配置工具中按钮的说明：

- **Append** - 在列表末尾添加新项目
- **Apply All** - 应用当前配置更改
- **Cut** - 从列表中移除项目
- **Clear** - 重置项目属性
- **Discard Changes** - 丢弃未保存的配置
- **Insert** - 在列表中插入新项目（放置在当前项目之前）
- **Sort** - 按 VLAN-ID 对 VLAN 表排序；按 MAC 地址对主机表排序
- **Change Password** - 更改设备密码
- **Logout** - 退出当前设备
- **Reboot** - 重启设备
- **Reset Configuration** - 将配置重置为出厂默认值
- **Choose File** - 浏览选择升级或备份文件
- **Upgrade** - 使用所选文件升级设备固件
- **Download & Upgrade** - 自动尝试下载并升级固件，运行网页浏览器的 PC 需能访问互联网
- **Restore Backup** - 使用所选备份文件恢复设备
- **Save Backup** - 生成并下载设备备份文件

> **注意：** 每个设备都有其专属固件，不能安装到其他系列型号上！
>
> - GPEN21 支持 SwOS Lite v2.13 及更新版本。

---

## 系统

System 选项卡执行以下功能：

- 设备常规信息
- 设备管理
- 配置重置
- 配置备份与恢复

> **注意：** SwOS 使用一种简单的算法来确保 TCP/IP 通信——它仅回复数据包来源的 IP 和 MAC 地址。这样设备本身无需配置默认网关。

![Gpen21 系统](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-02.webp)

| 属性 | 描述 |
| --- | --- |
| **地址获取方式** | 指定使用的地址获取方法：`DHCP with fallback` - 设备尝试从 DHCP 服务器请求 IPv4 地址。如果请求失败，则可通过 **静态 IP 地址** 值访问设备；`static` - 地址设置为 **静态 IP 地址** 值（仅 IPv4）；`DHCP only` - 设备使用 DHCPv4 客户端获取地址 |
| **静态 IP 地址** | 当 **地址获取方式** 设置为 `DHCP with fallback` 或 `static` 时设备的 IP 地址 |
| **标识名称** | 设备名称（用于 Mikrotik 邻居发现协议） |
| **允许来源** | 可访问设备的 IP 地址。默认值为 `0.0.0.0/0` - 任意地址 |
| **允许来源端口** | 可访问设备的设备端口列表 |
| **允许来源 VLAN** | 可访问服务的 VLAN ID。请确保先配置 VLAN 和 VLANs 页面 |
| **看门狗** | 启用或禁用系统看门狗。在故障条件下将重置设备 CPU |
| **Mikrotik 发现协议** | 启用或禁用 Mikrotik 邻居发现协议 |
| **暗色模式** | 禁用或启用设备上的所有 LED |
| **MAC 地址** | 设备的 MAC 地址（只读） |
| **序列号** | 设备的序列号（只读） |
| **板卡名称** | 设备的 MikroTik 型号名称（只读） |
| **运行时间** | 设备当前运行时间（只读） |
| **PoE 输出模式** | 指定 PoE-Out 状态：`auto-on` - 板卡将尝试检测是否可向端口供电。要完成供电，备用线对上需存在 3kΩ 至 26.5kΩ 范围内的电阻；`forced-on` - 移除检测范围。因此 PoE 将始终开启；`off` - 该端口的检测和供电全部关闭 |
| **PoE 输出状态** | 显示端口当前的 PoE-Out 状态（只读） |

### 密码与备份

![Swos system3 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-03.webp)

---

## 链路

Link 选项卡允许您配置每个接口的设置并监控链路状态。

![Gpen21 链路](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-04.webp)

| 属性 | 描述 |
| --- | --- |
| **启用** | 启用或禁用端口 |
| **名称** | 可编辑的端口名称 |
| **链路状态** | 当前链路状态（只读） |
| **自动协商** | 启用或禁用自动协商 |
| **速率** | 显示协商速率，或允许手动更改端口速率设置（需禁用自动协商） |
| **全双工** | 显示协商的双工模式，或允许手动更改端口双工模式（需禁用自动协商） |
| **跳数** | 显示链路中 GPER 中继器的数量 |
| **最后一跳** | 如果链路已终止，显示最后一个 GPER 中继器的编号 |
| **长度** | 如果链路已终止，显示线缆长度（米） |
| **故障位置** | 如果线缆损坏但链路仍处于活动状态，显示到故障点的距离（米） |
| **线缆线对** | 显示四个线缆线对位置及其状态：`O` - 开路；`S` - 短路；`P` - 极性反接 |

设备支持最大 10222 字节的巨型帧。SwOS Lite 设备不支持手动减小 MTU 设置。

---

## SFP

SFP 选项卡允许您监控 SFP 模块的状态。

![Gpen21 sfp](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-05.webp)

---

## 转发

Forwarding 选项卡提供设备端口间的高级转发选项、端口锁定、带宽限制和广播风暴控制功能。

![Gpen21 转发](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-06.webp)

| 属性 | 描述 |
| --- | --- |
| **端口锁定** | `Port Lock` - 启用或禁用此端口上的 MAC 地址学习。启用后，将限制 MAC 地址学习，此时应配置静态 MAC 地址。任何接收到且源 MAC 地址未知的帧将被丢弃。`Lock On First` - 允许从接收到的第一个帧学习源 MAC 地址；此属性应与 `Port Lock` 配合使用。每当接口状态变化时，第一个 MAC 地址的学习将重置。 |
| **上行链路端口** | `Set As Uplink Port` - 允许在 PoE-in（端口1）、PoE-out（端口2）或 SFP 接口之间更改上行链路端口。在下行端口接收到的数据包仅转发到上行链路端口；只能使用单个接口作为上行链路。 |
| **广播风暴控制** | `Storm Rate` - 限制接口传输的广播数据包数量。速率以比特每秒（bps）为单位。`Limit Unknown Unicast` - 将主机表中无条目的单播数据包纳入 `Storm Rate` 限制。 |
| **带宽限制** | `Ingress Rate` - 限制进入此端口的流量（bps）；`Egress Rate` - 限制离开此端口的流量（bps） |

> **注意：** 可以按端口限制入口/出口流量。入口流量使用 policer（策略器），出口流量使用 shaper（整形器）。入口 policer 通过丢包来控制接收流量——超过定义限制的所有数据包将被丢弃。这可能会影响终端主机的 TCP 拥塞控制机制，实际可达带宽可能低于设定值。出口 shaper 尝试对超过限制的数据包进行排队而非丢弃。最终，当输出队列满时也会丢弃数据包；但应能更好地利用设定的吞吐量。

---

## 统计、错误和直方图

这些菜单提供有关接收和传输数据包的详细信息。

![Gpen21 统计](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-07.webp)

![Gpen21 错误](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-08.webp)

![Gpen21 直方图](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-09.webp)

---

## VLAN 和 VLANs

设备端口的 VLAN 配置。

![Gpen21 vlan](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-10.webp)

| 属性 | 描述 |
| --- | --- |
| **VLAN 模式** (*disabled \| optional \| strict*；默认值：**optional**) | VLAN 过滤模式；这些选项与出口端口相关（strict 模式除外）。`disabled` - 不使用 VLAN 表。设备在出口端口丢弃带 VLAN 标签的数据包。如果数据包带有 VLAN 标签且 VLAN ID 与出口端口上的 `Default VLAN ID` 匹配，则在 `VLAN Receive=any` 时设备将移除 VLAN 标签并转发数据包。`optional` - 禁用 VLAN 过滤。将带有 VLAN 表中不存在的 VLAN 标签 ID 的数据包视为无 VLAN 标签的数据包处理。`strict` - 启用 VLAN 过滤并附加入口过滤，检查入口端口是否为 VLAN 表中接收到的 VLAN ID 的成员。在入口端口接收到的 VLAN ID 与 VLAN 表不匹配的数据包将被丢弃。必须为接入端口指定 Default VLAN ID，因为它将用于标记入口流量并为特定端口去标记出口流量。 |
| **VLAN 接收** (*any \| only tagged \| only untagged*；默认值：**optional**) | 基于 VLAN 标签存在性的接收流量过滤。`any` - 允许特定端口上的带标签和不带标签数据包；`only tagged` - 仅允许带 VLAN 标签的数据包。"Default VLAN ID" 将不起作用，因为它仅适用于不带标签的流量；`only untagged` - 仅允许不带 VLAN 标签的数据包 |
| **默认 VLAN ID** (*整数：1..4095*；默认值：**1**) | 设备将接收到的无标签数据包放入 "Default VLAN ID" 对应的 VLAN 中。仅对无标签流量有效，且当 **VLAN Receive** 设置为 "any" 或 "only untagged" 时生效。不适用于带标签的流量。此参数通常用于为接入端口分配特定 VLAN。当数据包的 VLAN ID 与 Default VLAN ID 匹配时，也用于去标记出口流量。 |
| **强制 VLAN ID** (*yes \| no*；默认值：**no**) | 将 `Default VLAN ID` 值分配给所有入口流量（带标签和不带标签）。在所有 VLAN 模式下均生效。如果端口接收到带标签的流量且 `Default VLAN ID` 设置为 1，则启用此参数后出口流量将被去标记。 |

设备端口的 VLAN 成员配置。

![Gpen21 vlans](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-11.webp)

| 属性 | 描述 |
| --- | --- |
| **VLAN ID** (*整数：1..4094*；默认值：**0**) | 要分配端口的 VLAN ID |
| **成员** (*端口*；默认值：**none**) | 允许在定义的 VLAN 上转发流量的端口组 |

### VLAN 配置示例

VLAN 配置示例取自 [CSS610 交换机用户手册](https://help.mikrotik.com/docs/display/SWOS/CSS610+series+Manual#CSS610seriesManual-VLANConfigurationExample)；但相同的原理可应用于 GPEN21 设备。

#### 中继和接入端口

![接入端口](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-12.webp)

1. 在 VLANs 菜单中添加 VLAN 条目并指定端口成员。

![Css610 vlans](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-13.webp)

2. 在 VLAN 菜单中为计划的接入端口（无标签）配置 Default VLAN ID，选择正确的 VLAN Receive 设置（端口2 仅带标签，端口6-8 仅无标签），并启用 strict VLAN 过滤以确保仅允许的 VLAN 可以通过端口。

![Css610 vlan](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-14.webp)

#### 中继和混合端口

![混合端口](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-15.webp)

1. 在 VLANs 菜单中添加 VLAN 条目并指定端口成员。

![Css610 vlans hybrid](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-16.webp)

2. 在 VLAN 菜单中为计划的混合端口（用于无标签 VLAN）配置 Default VLAN ID，选择正确的 VLAN Receive 设置（端口2 仅带标签，端口6-8 any），并启用 strict VLAN 过滤以确保仅允许的 VLAN 可以通过端口。

![Css610 vlan hybrid](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-17.webp)

#### 管理访问

在此示例中，将创建 VLAN 200 上的设备管理访问。配置方案与 "**中继和接入端口**" 相同，步骤 **1.、2.** 完全一致。额外的 **第3** 步需要在 System 菜单中指定管理 VLAN ID。应用配置后，设备将仅响应端口2 上带标签的 VLAN 200 数据包和端口6 上的无标签数据包。DHCP 客户端也将在指定的 VLAN ID 中工作。

![Css610 system vlan](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-18.webp)

> **警告：** 如果 VLAN 设置配置不正确，更改管理 VLAN 可能完全禁用对设备管理的访问。在更改此设置前请保存配置备份，若管理访问丢失，请使用 [重置与重装](#reset-and-reinstall)。

---

## 主机

此表表示动态学习的 MAC 地址到端口映射条目。它可以包含两种条目：动态和静态。动态条目自动添加——这也称为学习过程：当设备从某个端口接收到数据包时，它会将数据包的源 MAC 地址和接收端口添加到主机表中，这样当收到具有特定目的 MAC 地址的数据包时，它就知道应转发到哪个端口。如果目的 MAC 地址不在主机表中，则将该数据包转发到组内的所有端口。动态条目大约需要 5 分钟超时。

如果已存在相同 MAC 地址的动态条目，静态条目将覆盖动态条目。添加静态条目还可以访问更多功能。

![Gpen21 主机](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-19.webp)

**静态主机属性**

| 属性 | 描述 |
| --- | --- |
| **端口** | 数据包应转发到的端口 |
| **MAC** | MAC 地址 |

**动态主机属性（只读）**

| 属性 | 描述 |
| --- | --- |
| **端口** | 数据包应转发到的端口 |
| **MAC** | 学习到的 MAC 地址 |

---

## SNMP

SwOS 支持 SNMP v1 和 v2c（响应 GetRequest、GetNextRequest 和 GetBulkRequest），并使用 IF-MIB、SNMPv2-MIB、BRIDGE-MIB 和 MIKROTIK-MIB（仅用于健康状态、PoE-out 和 SFP 诊断）。不支持 SNMP 陷阱和写入 SwOS 配置。

可用的 SNMP 数据：

- 系统信息
- 系统运行时间
- 端口状态
- 接口统计
- 主机表信息

![Swos snmp2 1](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-20.webp)

| 属性 | 描述 |
| --- | --- |
| **启用** | 启用或禁用 SNMP 服务 |
| **团体名** | SNMP 团体名称 |
| **联系信息** | NMS 的联系信息 |
| **位置** | NMS 的位置信息 |

---

## ACL

访问控制列表（ACL）规则表是一个非常强大的工具，允许基于 L2、L3 和 L4 协议头字段条件进行线速数据包过滤、转发和 VLAN 标记。每条规则包含条件部分和操作部分。

![Gpen21 acl](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/gpen21-21.webp)

**条件部分参数**

| 属性 | 描述 |
| --- | --- |
| **来源端口** | 数据包进入的端口 |
| **MAC 源** | 源 MAC 地址和掩码 |
| **MAC 目的** | 目的 MAC 地址和掩码 |
| **以太类型** | 以太网帧负载中封装的协议 |
| **VLAN** | VLAN 头存在性：`any` / `present` / `not present` |
| **VLAN ID** | VLAN 标签 ID |
| **优先级** | VLAN 标签中的优先级 |
| **IP 源** (IP/子网掩码:端口) | 源 IPv4 地址、子网掩码和 L4 端口号 |
| **IP 目的** (IP/子网掩码:端口) | 目的 IPv4 地址、子网掩码和 L4 端口号 |
| **协议** *(整数)* | IP 协议 |
| **DSCP** | IP DSCP 字段 |

**操作部分参数**

| 属性 | 描述 |
| --- | --- |
| **丢弃** | 丢弃数据包 |
| **设置 VLAN ID** | 更改 VLAN 标签 ID（如果 VLAN 标签存在） |
| **优先级** | 更改 VLAN 标签优先级位（如果 VLAN 标签存在） |

---

## 重置与重装

GPEN21 内置备份 SwOS 固件，可在标准固件损坏或升级失败时加载：

- 在设备启动时按住 Reset 按钮几秒钟将重置配置并加载备份固件。重置按钮位于前面板盖后面。
- 加载备份固件后，可以使用网页浏览器连接到 192.168.88.1（或 DHCP 服务器分配的地址）并安装新的 SwOS 固件。