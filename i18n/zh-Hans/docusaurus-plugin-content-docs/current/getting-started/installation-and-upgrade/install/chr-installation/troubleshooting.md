# CHR：故障排查

> 本页涵盖 MikroTik RouterOS CHR 的故障排查，涉及 Linux 桥接上的 IGMP 侦听问题、客户机与外部世界之间的 VLAN 相关数据流问题、虚拟机监控程序中的 VLAN 标记要求，以及 VMware 客户机自动化的限制。

# CHR：故障排查

### 在 Linux 上使用 Bridge

如果 Linux 桥接启用了 IGMP 侦听，并且您遇到 IPv6 流量问题，请禁用此功能。IGMP 侦听会干扰 MLD 数据包（组播），并阻止它们通过桥接。

```
echo -n 0 > /sys/class/net/vmbr0/bridge/multicast_snooping
```

### 数据包无法从客户机传出

**问题：** 在客户机 CHR 上配置软件接口（VLAN、EoIP、Bridge 等）后，路由器停止向外部世界传递数据。

**解决方案：** 检查您的虚拟化管理系统的安全设置。请确认：

- 允许其他 MAC 地址通过
- 允许带有 VLAN 标记的数据包通过

根据需要调整安全设置——例如，启用 MAC 欺骗或允许特定的 MAC 地址范围。对于 VLAN 接口，您通常可以定义允许的 VLAN 标记或 VLAN 标记范围。

### 在各种虚拟机监控程序中的 CHR 上使用 VLAN

CHR 不控制外部 VLAN 标记；它仅处理从虚拟网络接口接收到的 VLAN 标记。
在某些虚拟机监控程序中，必须先在其侧配置 VLAN 标记，然后才能在 CHR 虚拟机内部使用。

**相关文章：**

- Hyper-V VLAN 配置（微软官方文档）：
  - https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/deploy/configure-virtual-local-area-networks-for-hyper-v

- 使用 PowerShell 进行 Hyper-V VLAN 中继配置：
  - https://learn.microsoft.com/en-us/powershell/module/hyper-v/set-vmnetworkadaptervlan?view=windowsserver2025-ps

## VMware 集成说明

CHR 不支持 VMware Tools 或任何客户机代理集成。

客户机级自动化（例如通过 VMware Tools、VIX 或 vSphere API 在 CHR 内部运行脚本）不可用。

仅支持基本的虚拟机监控程序功能，如电源管理和资源分配。