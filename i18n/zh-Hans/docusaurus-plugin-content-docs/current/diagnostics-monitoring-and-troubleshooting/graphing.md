# Graphing（图形化监控）

> Graphing 是 RouterOS 中用于通过可视化图形监控 CPU、内存、磁盘使用情况以及接口/队列流量的工具，可通过 Web 浏览器或菜单访问。配置选项包括数据采集频率、存储设置以及特定 IP 范围的访问权限。

# Graphing（图形化监控）

Graphing 是一种用于随时间监控各种 RouterOS 参数并将收集的数据以图形形式展示的工具。  
观看我们关于此功能的[视频](https://youtu.be/FTQEnDZVHNc)。

:::danger
我们建议对于内置存储空间较小的设备，不要将图形数据存储在磁盘上。
:::

Graphing 工具可以显示以下内容的图形：

- 资源使用情况（CPU、内存和磁盘使用率）。
- 通过接口的流量。
- 通过简单队列的流量。

Graphing 由两部分组成——第一部分负责收集信息，另一部分在 Web 页面上显示数据。要访问图形，请在 Web 浏览器中输入 `http://[Router_IP_address]/graphs/` 并选择要显示的图形。

或者，在 WebFig 界面右上角查找 **≡**（三条横线符号）菜单，即可找到“graphs”：

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/graphing-example.png)

内存图形示例：

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/graphing-01.webp)

## 配置

### 常规设置

配置在 `/tool/graphing` 菜单下完成。默认情况下，graphing 功能处于禁用状态。您可以在相应的子菜单中为接口、资源和简单队列配置 graphing。

**子菜单：** `/tool/graphing`

| 属性 | 说明 |
| :-- | :-- |
| **store-every** (*24hours \| 5min \| hour*；默认值：**5min**) | 将收集的数据写入系统驱动器的频率。 |
| **page-refresh** (*integer \| never*；默认值：**300**) | 图形页面的刷新频率。 |

### 接口图形化监控

该子菜单允许配置 graphing 将收集哪些接口的带宽使用数据。

**子菜单：** `/tool/graphing/interface`

| 属性 | 说明 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*；默认值：**0.0.0.0/0**) | 允许访问图形信息的 IP 地址范围。 |
| **comment** (*string*；默认值：) | 当前条目的描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 定义该项目是否被使用。 |
| **interface** (*all \| interface name*；默认值：**all**) | 定义要监控的接口。**all** 表示将监控路由器上的所有接口。 |
| **store-on-disk** (*yes \| no*；默认值：**yes**) | 定义是否将收集的信息存储在系统驱动器上。 |

### 队列图形化监控

该子菜单允许配置 graphing 将收集哪些简单队列的带宽使用数据。

**子菜单：** `/tool/graphing/queue`

| 属性 | 说明 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*；默认值：**0.0.0.0/0**) | 允许访问图形信息的 IP 地址范围。 |
| **allow-target** (*yes \| no*；默认值：**yes**) | 是否允许从队列的目标地址访问图形。 |
| **comment** (*string*；默认值：) | 当前条目的描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 定义该项目是否被使用。 |
| **simple-queue** (*all \| queue name*；默认值：**all**) | 定义要监控的队列。**all** 表示将监控路由器上的所有队列。 |
| **store-on-disk** (*yes \| no*；默认值：**yes**) | 定义是否将收集的信息存储在系统驱动器上。 |

:::warning
如果简单队列的目标地址设置为 0.0.0.0/0，即使 allow-address 设置为特定地址，所有人都能访问队列图形。这是因为默认情况下，队列图形也可以从目标地址访问。
:::

### 资源图形化监控

该子菜单允许启用系统资源的图形化监控。Graphing 收集以下数据：

- CPU 使用率
- 内存使用率
- 磁盘使用率

**子菜单：** `/tool/graphing/resource`

| 属性 | 说明 |
| :-- | :-- |
| **allow-address** (*IP/IPv6 prefix*；默认值：**0.0.0.0/0**) | 允许访问图形信息的 IP 地址范围。 |
| **comment** (*string*；默认值：) | 当前条目的描述。 |
| **disabled** (*yes \| no*；默认值：**no**) | 定义该项目是否被使用。 |
| **store-on-disk** (*yes \| no*；默认值：**yes**) | 定义是否将收集的信息存储在系统驱动器上。 |

## WinBox 中的图形化监控

WinBox 允许查看与 Web 页面相同的信息。打开 **Tools->Graphing** 窗口。双击您想要查看图形的条目。

下图显示了 WinBox 中的内存使用图形：

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/graphing-02.webp)