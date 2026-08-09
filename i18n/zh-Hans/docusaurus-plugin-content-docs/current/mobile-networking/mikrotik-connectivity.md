# MikroTik Connectivity（MikroTik 连接）

> MikroTik Connectivity 推出了一款 eSIM 解决方案，无需实体 SIM 卡更换即可实现设备的无缝连接，可通过 MikroTik 账户门户以及 RouterOS CLI/WinBox 界面完成激活步骤。

# MikroTik Connectivity（MikroTik 连接）

### 概述

MikroTik Connectivity 是我们全新内置的 eSIM 解决方案，可确保您的设备在任何地方保持连接，无需更换实体 SIM 卡或执行外部激活步骤。更多信息，请访问 [https://mikrotik.com/connectivity](https://mikrotik.com/connectivity)

### 激活示例

1) 登录您的 MikroTik 账户，选择“我的设备”。

![](img/esim_1.png)

1) 输入您设备的序列号——系统将自动识别。选择区域，然后点击“添加到列表”。

![](img/esim_2.png)

1) 选择适合您需求的数据套餐和支付方式，然后将其加入购物车。

![](img/esim_3.png)

1) 在购物车中完成支付。

![](img/esim_4.png)

1) 支付完成后，返回“我的设备”，您将看到订阅现已处于“活动”状态。

![](img/esim_5.png)

:::info
MikroTik eSIM 配置文件已预加载，因此激活过程中无需互联网连接。激活本身通常只需几分钟，但在某些情况下可能需要几个小时。
:::

1) 在 RouterOS 中检查您的设备是否设置为使用“esim”，并确认正确的配置文件已激活。

CLI：

```
[admin@EG25-G&KNe] > /interface/lte/settings/print 
                 mode: auto    
         esim-channel: auto    
        firmware-path: firmware
  link-recovery-timer: 120     
             sim-slot: sim      
[admin@EG25-G&KNe] > /interface/lte/settings/set sim-slot=esim      
[admin@EG25-G&KNe] > /interface/lte/esim/print
Flags: A - ACTIVE
Columns: INTERFACE, NAME, SPN, ICCID
#   INTERFACE  NAME       SPN                      ICCID
0 A lte1       Profile 1  MikroTik  89358152000001049461
1   lte1       Profile 4  MikroTik  89358152000001349465
```

在 WinBox 中：

 前往 Interfaces > LTE > Modem 选择 esim SIM 卡槽：

![](img/esim_6.png)

前往 Interfaces > LTE > eSIM 查看哪个是活动的 eSIM 配置文件：

![](img/esim_7.png)

如需更改活动配置文件，请右键点击该配置文件并选择“激活”：

![](img/esim_8.png)

#### [视频教程：我们的官方 YouTube 频道，MikroTips 系列](https://www.youtube.com/watch?v=2YxHL9A4Ys0)

### 常见问题解答

<details>
<summary>分配给我设备的 IP 地址是公网 IP 地址吗？</summary>

不是，该 IP 地址是私有的。您可以配置 BTH（Back To Home）以远程访问您的设备：[Back To Home](../network-management/cloud/back-to-home.md)

</details>

<details>
<summary>是否也支持 IPv6？</summary>

仅支持 IPv4。

</details>

<details>
<summary>我应该配置哪个接入点名称（APN）？</summary>

您可以使用“use-network-apn=yes”选项，或手动将 APN 设置为“[mikrotik.net](http://mikrotik.net "http://mikrotik.net/")”。

</details>

<details>
<summary>为什么使用 MikroTik Connectivity 时的延迟比使用本地运营商 SIM 卡时更高？</summary>

MikroTik Connectivity 作为漫游服务运行。它通过一组可能位于其他国家的 PDN 网关路由数据。额外的距离和网络跳数增加了往返时间，因此延迟看起来比使用本地运营商服务时更高。

</details>

<details>
<summary>为什么使用 MikroTik Connectivity 时的下载/上传速度比使用本地运营商 SIM 卡时更低？</summary>

MikroTik Connectivity 作为漫游服务运行。它通过一组可能位于其他国家的 PDN 网关路由数据。额外的距离和网络跳数增加了往返时间，因此延迟增加。由于延迟较高，TCP 性能会直接受到影响。TCP 依赖确认机制来增大其拥塞窗口并扩展吞吐量。当往返时间变长时，确认返回所需时间增加，拥塞窗口增长变慢，可实现的吞吐量随之降低。

</details>

<details>
<summary>如何暂停、升级或取消我的 MikroTik Connectivity 订阅？</summary>

要管理您的 eSIM 订阅套餐，请登录您的 **mikrotik.com** 账户，进入**“我的设备”**部分。搜索您设备的序列号并点击它。

在那里，您有两种方式管理您的套餐：

* **通过“套餐”选项卡：** 您可以在此找到**“取消订阅”**选项，或通过选择不同的数据套餐进行升级。
* **通过“详细信息”选项卡：** 前往**“状态”**字段，您可以在**“活动”**、**“暂停数据传输”**或**“取消订阅”**之间切换。

</details>