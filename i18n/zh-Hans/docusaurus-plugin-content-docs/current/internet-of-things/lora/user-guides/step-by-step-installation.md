# 分步安装指南

> 本页提供在 MikroTik RouterOS 上安装和配置 LoRa mini-PCIe 网卡的分步指南，包括硬件安装、GUI 设置、软件包管理及初始网络服务器配置。

# 分步安装指南

### LoRa 网卡安装

本节将以 LtAP LTE 套件为例进行说明。

打开路由器外壳。对于 LtAP 型号，卸下所有螺丝后，需小心地将上盖向左侧移动，因为 LTE 天线连接在上盖内侧：

![1.png](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-01.webp)

将 R11e-LoRa 网卡插入 mini-PCIe 插槽，并用两颗螺丝固定到螺纹孔中：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-02.webp)

将天线连接到网卡（UFL 接口）。本例中同时使用了 UFL → SMA 转接线，因为 LtAP 外壳为此设计了专用槽位。

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-03.webp)

完成上述步骤后，即可合上路由器外壳，进入配置阶段。

### 配置

#### GUI 设置

通过 Winbox 或 WebFig 连接到路由器。

Winbox 可通过[此链接](https://mikrotik.com/download/winbox)下载。

运行 Winbox：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-04.webp)

强烈建议将 RouterOS 升级至最新可用版本。安装新版本将触发重启：

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-05.webp)

如果设备没有 **IoT>LoRa** 菜单，请下载针对路由器架构和 RouterOS 版本的“**Extra packages**”扩展包。可在 Winbox 窗口顶部或 System → Resources → Architecture Name 中查看路由器架构类型。
[https://mikrotik.com/download](https://mikrotik.com/download)
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-06.webp)

下载并解压软件包后，将 **IoT** 软件包上传至路由器。也可直接拖拽上传。上传完成后，文件应出现在文件目录中。重启路由器（System → Reboot）以安装软件包：
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-07.webp)

重启后，软件包应显示在软件包列表中：
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-08.webp)

检查 LoRa 网关是否已在 **IoT>LoRa>Devices** 下初始化。如果是 LtAP 型号，请确保将 USB 类型设置为 Mini-PCIe：
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-09.webp)

网关出现后（位于 **IoT>LoRa>Devices** 下），选中它，从默认列表中选择网络服务器或自行添加（位于 **IoT>LoRa>Servers** 下），然后启用：
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-10.webp)

切换到 Traffic 选项卡，监控周围节点发送的请求：
![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/step-by-step-installation-11.webp)

至此，LoRa mini-PCIe 网卡的基本安装和配置已完成。更多设置请参阅：[通用属性](../general-properties.md)