# RouterBOOT

> RouterBOOT 负责在 MikroTik 硬件设备上启动 RouterOS，具有主引导加载程序和备份引导加载程序，并带有强制备份引导选项。重置按钮具有多种功能，包括配置重置、CAPs 模式激活和 Netinstall 服务器搜索。对于具有特定设置的 RouterBOARD 设备，可提供串行控制台访问。

# RouterBOOT

RouterBOOT 负责在 MikroTik 硬件设备（如接入点、路由器和其他型号）上启动 RouterOS。由于 MikroTik 已制造了许多新的硬件系列，因此在此处及其他地方使用 RouterBOARD 一词时，它同样适用于所有运行 RouterOS 的其他硬件系列。

### 主引导加载程序和备份引导加载程序

默认情况下，使用主（常规）引导加载程序，但 RouterBOARD 设备还具有辅助（备份）引导加载程序，可在主引导加载程序无法工作时使用。可以通过 RouterOS 中的配置设置来调用备份引导加载程序：

```ros
/system/routerboard/settings/set force-backup-booter=yes
```

也可以在设备开机时按住 RESET 按钮来使用备份引导加载程序。只能升级主 RouterBOOT，因此如果出现故障，可以使用备份引导加载程序启动设备并降级主引导加载程序。有关升级说明，请遵循 [RouterBOARD#UpgradingRouterBOOT](../../hardware/routerboard.md) 中的单独说明。

### RouterBOARD 重置按钮

RouterBOOT 重置按钮具有三个功能：

- 在启动期间按住此按钮，直到 LED 灯开始闪烁，然后松开按钮以重置 RouterOS 配置（总共 5 秒）。
- 继续按住 5 秒，直到 LED 变为常亮，然后松开以启用 CAPs 模式（总共 10 秒）。
- 或者继续按住按钮 5 秒，直到 LED 熄灭，然后松开以使 RouterBOARD 查找 Netinstall 服务器。

:::warning
如果在通电前按住按钮，则除了上述所有操作外，还将使用备份 RouterBOOT。要在不加载备份引导加载程序的情况下执行上述操作，请在设备通电后立即按下按钮。
:::

[重置密码](https://help.mikrotik.com/docs/spaces/RKB/pages/328274/Reset+the+password)

[https://www.youtube.com/watch?v=6Unz92rABs8](https://www.youtube.com/watch?v=6Unz92rABs8)

### **Wireless Wire** 套件的配置重置

重置按钮的功能与其他设备相同，详细说明请参阅 [/docs/Getting%20Started/routeros-configuration-reset](../configuration-management/routeros-configuration-reset.md)

启动时按住按钮 5 秒（USR LED 灯开始闪烁）- 重置为受密码保护的状态。

启动时按住按钮 10 秒（USR LED 闪烁后变为常亮）- 完全移除配置。

### 配置

对于带有串行控制台连接器的 RouterBOARD 设备，可以访问 RouterBOOT 引导加载程序配置菜单。所需电缆在 [串行控制台](../../management-tools/serial-console.md) 手册中进行了说明。RouterBOARD 串行端口配置为 **115200bit/s**、**8 个数据位**、**1 个停止位**，并且**无奇偶校验**。我们建议禁用硬件流控制。

此示例显示了 RouterBOOT 7.4beta4 中可用的菜单：

```ros
RouterBOOT booter 7.4beta4

CRS328-24P-4S+

built by build at 2022-06-15 11:34:09 from revision 73B4521C

CPU frequency: 800 MHz
  Memory size: 512 MiB
 Storage size:  16 MiB

Press Ctrl+E to enter etherboot mode
Press any key within 2 seconds to enter setup

RouterBOOT-7.4beta4
What do you want to configure?
   d - boot delay
   k - boot key
   s - serial console
   n - silent boot
   o - boot device
   z - extra kernel parameters
   r - reset booter configuration
   e - format storage
   w - repartition nand
   g - upgrade firmware
   i - board info
   p - boot protocol
   b - booter options
   j - boot os
   t - hardware tests
   l - erase license
   x - exit setup
your choice: 
```

这些选项不言自明。

| 字母 | 描述 | 说明 |
| :-- | :-- | :-- |
| d | 启动延迟 | 延迟 RouterOS 的启动以允许接口初始化 |
| k | 启动键 | 将打开配置菜单的按钮 |
| s | 串行控制台 | 设置串行端口的波特率 |
| n | 静默启动 | 抑制串行端口上的所有输出，以防有设备连接到它（如 GPS 设备或温度监视器） |
| o | 启动设备 | 允许启用 Netinstall 启动 |
| z | 额外内核参数 |  |
| r | 重置引导加载程序配置 | 重置此菜单中的设置。**警告，无确认！** |
| e | 格式化存储 | 销毁 NAND 上的所有数据，包括 RouterOS 配置和许可证 |
| w | 重新分区 NAND | 有关更多信息，请参阅 [分区](../../system-information-and-utilities/partitions.md) 文档 |
| y | 活动分区 | 选择要从中尝试加载 RouterOS 的活动分区 |
| g | 升级固件 | 允许通过网络或 XModem 协议升级 RouterBOOT 版本 |
| i | 板卡信息 |  |
| p | 启动协议 |  |
| b | 引导加载程序选项 | 选择默认使用的引导加载程序 |
| t | 执行内存测试 |  |
| j | 启动操作系统 |  |
| l | 擦除许可证 |  |
| x | 退出设置 |  |

按下相应的键盘字母将为您提供更多选项列表；如下所示：

```
# d - 启动延迟：

选择启动延迟：
   1 - 1秒
 * 2 - 2秒
   3 - 3秒
   4 - 4秒
   5 - 5秒
   6 - 6秒
   7 - 7秒
   8 - 8秒
   9 - 9秒

# k - 启动键：

选择启动时进入设置的按键：
 * 1 - 任意键
   2 - 仅 <Delete> 键

# s - 串行控制台：

选择串行控制台的波特率：
 * 1 - 115200
   2 - 57600
   3 - 38400
   4 - 19200
   5 - 9600
   6 - 4800
   7 - 2400
   8 - 1200
   9 - 关闭

# n - 静默启动：

静默启动：
   0 - 关闭
 * 1 - 开启

# o - 启动设备：

选择启动设备：
   e - 通过以太网启动
 * n - 从 NAND 启动，如果失败则从以太网启动
   1 - 先以太网启动一次，然后从 NAND 启动
   o - 仅从 NAND 启动
   b - 启动所选设备
   f - 启动 Flash 配置模式
   3 - 先启动 Flash 配置模式一次，然后从 NAND 启动

# f - CPU 频率：

选择 CPU 频率：
   a -  200MHz
   b -  400MHz
   c -  600MHz
   d -  800MHz
   e - 1000MHz
 * f - 1200MHz

# r - 重置引导加载程序配置：

# e - 格式化 NAND：

您真的想格式化存储设备吗？
这将导致丢失所有数据
输入 "yes" 确认： 

# w - 重新分区 NAND：

选择分区数量：
   1 - 分区
 * 2 - 分区
   3 - 分区
   4 - 分区

# y - 活动分区：

选择活动分区：
 * 0 - 分区
   1 - 分区

# g - 升级固件：

升级固件选项：
   e - 通过以太网升级固件
   s - 通过串行端口升级固件

# i - 板卡信息：

板卡信息：

        板卡类型： CCR1009-8G-1S-1S+
     序列号： 48FF01DDE6FD
  固件版本： 3.19
     CPU 频率： 1200 MHz
       内存大小： 2048 MiB
         NAND 大小： 128 MiB
        构建时间： 2014-09-23 15:02:34
  eth1 MAC 地址： 00:0C:42:00:BE:4A
  eth2 MAC 地址： 00:0C:42:00:BE:4B
  eth3 MAC 地址： 00:0C:42:00:BE:4C
  eth4 MAC 地址： 00:0C:42:00:BE:4D
  eth5 MAC 地址： 00:0C:42:00:BE:4E
  eth6 MAC 地址： 00:0C:42:00:BE:4F
  eth7 MAC 地址： 00:0C:42:00:BE:50
  eth8 MAC 地址： 00:0C:42:00:BE:51
  eth9 MAC 地址： 00:0C:42:00:BE:52
 eth10 MAC 地址： 00:0C:42:00:BE:53

# p - 启动协议：

选择要使用的启动协议：
 * 1 - bootp 协议
   2 - dhcp 协议

# b - 引导加载程序选项：

选择要加载的引导加载程序：
 * 1 - 加载常规引导加载程序
   2 - 强制加载备份引导加载程序

#t - 执行内存测试：

启动内置内存测试！

# x - 退出设置：

退出 BIOS 配置菜单并继续系统启动。

```

### 简单升级

可以通过 RouterOS 升级 RouterBOOT：

- 运行命令 *`/system/routerboard/upgrade`*。
- 重启路由器以应用升级（*`/system/reboot`*）。

```ros
[admin@admin] > /system/routerboard/upgrade 
您真的想升级固件吗？ [y/n] 

```

:::warning
每个 ROS 版本都包含一个新的 RouterBoot 版本。执行 ROS 升级后，我们始终建议同时升级 RouterBoot。
:::

### 检查 RouterBOOT 版本

此命令显示您设备的当前 RouterBOOT 版本以及 *routeros-x.yy.npk* 软件包中包含的可用升级，或者如果您上传了与设备型号对应的 *\*.FWF* 文件：

```ros
[admin@admin] >  /system/routerboard/print 
                ;;; 固件升级成功，请重启以使更改生效！
       routerboard: yes
        board-name: hAP ac
             model: RouterBOARD 962UiGS-5HacT2HnT
     serial-number: 6737057562DD
     firmware-type: qca9550L
  factory-firmware: 3.29
  current-firmware: 6.49.5
  upgrade-firmware: 7.4beta5 

```

在这种情况下，您可以看到，当前 RouterOS 版本中已经包含**更新版本**的引导加载程序固件，并且它已更新，需要重启。

:::warning
也可以通过上传较旧版本的 \*.FWF 文件进行降级，这在联系 MikroTik 支持时可能需要进行故障排除。
:::