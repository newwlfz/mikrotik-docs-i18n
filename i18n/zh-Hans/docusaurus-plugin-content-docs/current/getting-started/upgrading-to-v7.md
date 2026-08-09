# 升级至 v7

> 本文档概述了将 MikroTik RouterOS 升级至第 7 版的步骤与注意事项，详细说明了与 BGP、OSPF、MPLS 及用户管理器等功能的兼容性。文中强调了 BGP 连接中的必填参数、OSPF 菜单的合并，并提醒注意 MPLS 配置备份事宜。

# 升级至 v7

### 引言

本文档描述了将 RouterOS 升级至 v7 主版本的建议步骤，以及升级过程中可能遇到的注意事项。

从 v6 升级至 v7 的方式与 v6 版本内部升级相同。请参阅 [升级手册](./installation-and-upgrade/upgrade.md) 获取更详细的步骤。如果您当前运行的是 RouterOS 6 或更早版本，我们建议先升级至 v6 的最新稳定版或长期支持版。

:::info
在大多数运行上述 v6 版本且运行正常的 RouterOS 配置中，无需额外步骤。升级至 v7 将自动转换配置，您的设备将立即正常工作。

:::

:::note
**注意：** 我们不建议在内存低于 64 MB 的硬件上运行 v7。

:::

### 功能兼容性列表

如前所述，几乎所有 RouterOS 系统都可以使用“检查更新”功能，通过几次点击即可升级至 v7，但某些功能可能需要额外步骤：

| 功能 | 状态 |
| :-- | :-- |
| CAPsMAN | 正常 |
| 接口 | 正常 |
| 无线 | 正常 |
| 桥接/交换 | 正常 |
| 隧道/PPP | 正常 |
| IPv6 | 正常 |
| BGP | 正常，但需注意 [\*](#bgp) |
| OSPF | 正常，但需注意 [\*\*](#ospf) |
| MPLS | 正常，但需注意 [\*\*\*](#mpls) |
| 路由过滤器 | 正常，但需注意 [\*\*\*\*](#routing-filters) |
| PIM-SM | 参见 [注意事项](#notes) |
| IGMP 代理 | 正常 |
| 工具 | 正常 |
| 队列 | 正常 |
| 防火墙 | 正常 |
| HotSpot | 正常 |
| 静态路由 | 正常 |
| 用户管理器 | 参见 [注意事项](#notes) |

### 注意事项

:::danger
路由协议配置升级仅触发一次。这意味着，如果路由器降级至 ROSv6，配置被修改后再次升级至 ROSv7，则最终配置为降级前存在的配置。要重新触发 v6 配置转换，请加载带有 `force-v6-to-v7-configuration-upgrade=yes` 选项的 ROSv6 备份。

:::

### **BGP**

所有已知配置均可成功从 6.x 升级至 7.x。但请注意，配置已完全重新设计。v7 BGP 实现提供了 **`connection`**、**`template`** 和 **`session`** 菜单。

**`Template`** 包含所有与 BGP 协议相关的配置选项。它可用作动态对等体的模板，并可将类似配置应用于一组对等体。大多数参数与之前的实现相似，只是部分参数被分组在输出和输入部分，使配置更易读，也更易理解选项是应用于输入还是输出。

BGP **`connection`** 的最小参数集为 `remote.address`、`template`、`connect`、`listen` 和 `local.role`。  
Connect 和 listen 参数指定对等体是尝试连接并监听远程地址，还是仅连接或仅监听。在多跳连接场景中，可能还需要配置 `local.address`。对等体角色现在是必填参数。对于基本配置，您可以直接使用 ibgp、ebgp。

现在，您可以从 `/routing/bgp/session` 菜单监控所有已连接和未连接对等体的状态。  
其他关于所有路由进程的出色调试信息可从 `/routing/stats` 菜单监控。

网络被添加到防火墙地址列表中，并在 BGP **`connection`** 配置中引用。

### OSPF

所有已知配置均可成功从 6.x 升级至 7.x。  
OSPFv2 和 OSPFv3 现已合并为单一菜单 `/routing/ospf`。目前没有默认实例和区域。要启动 OSPF，您需要创建实例，然后向实例添加区域。

RouterOSv7 使用模板将接口与模板匹配，并应用匹配模板中的配置。OSPF 菜单 `interface` 和 `neighbor` 包含用于状态监控的只读条目。

### MPLS

升级 MPLS 配置时请谨慎操作，并确保在升级前备份配置。

### 路由过滤器

所有支持的选项均可无问题升级，若存在不支持的选项，则会创建空条目。路由过滤器配置已更改为类似脚本的配置。

规则现在可以使用“if .. then”语法，根据“if”语句中的条件设置参数或应用操作。

没有操作的多个规则会堆叠在单个规则中，并像防火墙一样按顺序执行，原因是“set”参数的顺序很重要，每行写一个“set”可以更轻松地自上而下理解应用了哪些操作。

更多 RouterOSv7 路由过滤器示例请参见 [此处](../user-guides/routing-and-networking-protocols/moving-from-rosv6-to-rosv7.md#routing-filters)。

### PIM-SM

升级 RouterOS 至 v7 不会保留 PIM 相关配置。升级后，组播路由配置将在 `/routing/pimsm` 菜单下可用，且不再需要额外的“multicast”软件包。更多信息请参见 [此处](../user-guides/routing-and-networking-protocols/multicast/pim-sm.md)。

### 用户管理器

RouterOSv7 提供了全新设计的用户管理器实现，配置现已集成到 RouterOS WinBox 和控制台中（Web 管理配置界面不可用），更多信息请参见 [此处](../authentication-authorization-accounting/user-manager.md)。无法从旧版用户管理器直接迁移，但可以通过 `/user-manager/database/migrate-legacy-db` 迁移旧数据库。不过，从头开始配置可能是个更好的选择。

### 新特性

RouterOSv7 采用了新内核，由于路由缓存的原因，性能会有所变化，某些任务可能需要更高的 CPU 和 RAM 使用率。

- 全新的 NTP 客户端和服务器实现。
- 合并了独立软件包，仅保留 bundle 和少量额外软件包 *（取消了对 LCD 和 KVM 软件包的支持）*。
- 新的命令行界面（CLI）风格（仍支持 RouterOS v6 命令）。
- 支持 Let's Encrypt 证书生成。
- 支持 REST API。
- 支持 x86 上的 UEFI 启动模式。
- CHR FastPath 支持“vmxnet3”和“virtio-net”驱动。
- 支持“Cake”和“FQ\_Codel”类型队列。
- 支持 IPv6 NAT。
- 支持 Marvell Prestera 交换芯片的 MikroTik 设备上的 Layer 3 硬件加速、QoS 和 MLAG。
- 支持 MBIM 驱动，对所有支持 MBIM 模式的调制解调器提供基本功能支持。
- 支持 VRRP 分组和节点间连接跟踪数据同步。
- 支持虚拟可扩展局域网（VXLAN）。
- 支持 L2TPv3。
- 支持 OpenVPN UDP 传输协议。
- 支持 WireGuard。
- 支持 RTL8367（RB4011、RB100AHx4）和 MT7621（hEX、hEX S、RBM33G）交换机上的硬件卸载 VLAN 过滤。
- 支持 ARM 和 ARM64 设备上的 ZeroTier。
- 支持 x86 设备的 CPU 频率缩放。

### 取消的支持

在 RouterOS v7 中，已取消对以下内容的支持：

- LCD 软件包
- KVM 软件包