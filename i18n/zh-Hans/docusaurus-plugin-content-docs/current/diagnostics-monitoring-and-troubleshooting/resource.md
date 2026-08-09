# 资源

> RouterOS 中的资源菜单提供了系统统计信息的概览，包括运行时间、内存、磁盘使用情况以及 CPU 型号和频率等硬件详情。它还提供了子菜单，用于查看每个 CPU 的详细使用情况、IRQ 和磁盘统计信息。

# 资源

### 常规

**子菜单：** `/system/resource`

常规资源菜单显示整体资源使用情况和路由器统计信息，如运行时间、内存使用情况、磁盘使用情况、版本等。

它还有几个子菜单，用于查看更详细的硬件统计信息，如 CPU、IRQ 和硬件。

```ros
[admin@MikroTik] > /system/resource/print 
                   uptime: 29s
                  version: 7.24rc2
               build-time: 2023-08-31 13:55:47
          minimum-version: 7.6
              free-memory: 94.2MiB
             total-memory: 224.0MiB
                      cpu: ARM
                cpu-count: 2
            cpu-frequency: 800MHz
                 cpu-load: 2%
           free-hdd-space: 93.5MiB
          total-hdd-space: 128.5MiB
  write-sect-since-reboot: 85
         write-sect-total: 222100
               bad-blocks: 0%
        architecture-name: arm
               board-name: hAP ax lite LTE6
                 platform: MikroTik

```

所有属性均为只读

| 属性 | 描述 |
| :-- | :-- |
| **architecture-name** (*字符串*) | CPU 架构 |
| **bad-blocks** (*百分比*) | 显示 NAND 上坏块的百分比。 |
| **board-name** (*字符串*) | RouterBOARD 型号名称 |
| **build-time**(*字符串*) | 已安装 RouterOS 版本的构建时间 |
| **cpu** (*字符串*) | 板上的 CPU 型号 |
| **cpu-count** (*整数*) | 系统上存在的 CPU 数量。每个核心是一个独立的 CPU，Intel 超线程也视为独立的 CPU。 |
| **cpu-frequency** (*字符串*) | 当前 CPU 频率 |
| **cpu-load** (*百分比*) | 已使用的 CPU 资源百分比。综合所有 CPU。每个核心的 CPU 使用率可在 [CPU 子菜单](#cpu) 中查看 |
| **minimum-version**(*字符串*) | 最低 RouterOS 版本（原为 'factory-software'） |
| **free-hdd-space** (*字符串*) | 硬盘或 NAND 上的可用空间 |
| **free-memory** (*字符串*) | 未使用的 RAM 量 |
| **platform** (*字符串*) | 平台名称 |
| **total-hdd-space** (*字符串*) | 硬盘或 NAND 的大小 |
| **total-memory** (*字符串*) | 已安装的 RAM 量 |
| **uptime** (*时间*) | 自启动以来经过的时间间隔 |
| **version** (*字符串*) | 已安装的 RouterOS 版本号 |
| **write-sect-since-reboot** (*整数*) | 自路由器上次重启以来，HDD 或 NAND 上的扇区写入次数 |
| **write-sect-total** (*整数*) | 扇区写入总次数 |

### CPU

**子菜单：** `/system/resource/cpu`

此子菜单显示每个 CPU 的使用情况，以及 IRQ 和磁盘使用情况。

```ros
[admin@RB1100test] /system/resource/cpu> print 
CPU LOAD IRQ DISK 
0 5% 0% 0% 
[admin@RB1100test] /system/resource/cpu> 

```

## 属性

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **cpu** (*整数*) | 显示使用情况的 CPU 标识号。 |
| **load** (*百分比*) | CPU 使用率（百分比） |
| **irq** (*百分比*) | IRQ 使用率（百分比） |
| **disk** (*百分比*) | 磁盘使用率（百分比） |

### IRQ

**子菜单：** `/system/resource/irq`

该菜单显示路由器上所有已使用的 IRQ。在多核系统上，可以通过将 IRQ 分配给特定核心来设置 [IRQ 负载均衡](#irq)。IRQ 分配由硬件完成，无法从 RouterOS 更改。例如，如果所有以太网接口都分配到一个 IRQ，那么您必须处理硬件问题：升级主板 BIOS，在 BIOS 中手动重新分配 IRQ，如果以上方法均无效，则更换硬件。

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **cpu** (*自动 \| 整数*; 默认值：) | 指定分配给 IRQ 的 CPU。自动 - 根据中断数量选择 CPU。使用 NAPI 优化中断。 |

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **active-cpu** (*整数*) | 在多核系统中显示活动 CPU。 |
| **count** (*整数*) | 中断次数。在以太网接口上，中断=数据包。 |
| **irq** (*整数*) | IRQ 标识号 |
| **users** (*字符串*) | 分配给 IRQ 的进程 |

### RPS

**子菜单：** `/system/resource/irq/rps`

接收数据包导向（RPS）类似于接收端缩放（RSS），用于将数据包导向特定 CPU 进行处理。然而，RPS 在软件层面实现，有助于防止单个网络接口卡的硬件队列成为网络流量的瓶颈。

当数据包需要额外的处理且消耗相对较多的 CPU 时间时（如 PPP 隧道终止、VPLS 或防火墙处理），RPS 非常有用。RPS 在分类和转发数据包到另一个 CPU 上消耗的 CPU 资源，会被所需的额外处理所抵消。不幸的是，RPS 不能总是替代以太网驱动程序中的几行代码，因为将数据包转发到另一个 CPU 本身就很昂贵。

对于具有多个队列的网络设备，通常配置 RPS 和 RSS 没有额外好处，因为 RSS 默认配置为将 CPU 映射到每个接收队列。然而，如果硬件队列少于 CPU 数量，RPS 可能仍然有益，具体取决于设备处理的流量。

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **disable**(*数字*) | 禁用所选条目的 RPS |
| **edit** (*数字*) | 编辑现有条目的属性 |
| **enable** (*数字*) | 启用所选条目的 RPS |
| **reset**(*数字*) | 将属性重置为默认值 |

### **硬件**

显示通过 PCI、USB 或 SCSI 总线检测到的硬件设备。

标志：

```ros
I - inactive   设备存在但未激活
```

**子菜单：** `/system/resource/hardware`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **location** (*字符串*) | 设备在系统拓扑中的位置 |
| **parent** (*枚举*) | 父总线或控制器 |
| **type** (usb\|pci\|scsi\|serial) | 设备的总线类型 |
| **vendor** (*字符串*) | 设备供应商名称 |
| **name** (*字符串*) | 设备名称或型号 |
| **serial-number** (*字符串*) | 设备序列号 |
| **vendor-id**(字符串) | 供应商标识符（VID） |
| **device-id** (字符串) | 设备标识符（PID / 设备 ID） |
| **speed** (*字符串*) | 协商的设备速度 |
| **ports**(*数字*) | 设备提供的端口数量 |
| **usb-version** (*字符串*) | 支持的 USB 版本 |
| **owner** (*字符串*) | 拥有设备的子系统或驱动程序 |
| **device-path** (*字符串*) | 从根总线到端点的设备路径 |

**只读属性**

| 属性 | 描述 |
| :-- | :-- |
| **category** (*字符串*) | 设备类别 |
| **irq** (*数字*) | 分配的中断号 |

### 设备授权

控制硬件设备的授权状态。

**子菜单：** `/system/resource/hardware/authorize`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **allow** (*是\|否*) | 启用或禁用 USB 设备授权 |

### 全局 USB 子系统设置

**子菜单：** `/system/resource/hardware/usb-settings`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **authorization** (*是\|否*) | 启用或禁用 USB 设备授权 |
| **numbers** (*数字*) |  |

**子菜单：** `/system/resource/hardware/usb-power-reset`

#### 属性

| 属性 | 描述 |
| :-- | :-- |
| **duration** (时间) | 重新启用 USB 前的断电持续时间 |
| **bus**(数字) | USB 总线编号 |
| **slot**(数字) | 总线上的 USB 端口/插槽编号 |