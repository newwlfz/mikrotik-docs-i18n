# CRS3xx 与 CSS3xx 系列手册

> SwOS 是一款专为 MikroTik 交换机产品管理而设计的操作系统。它提供了基础的可管理交换机功能，并具备高级特性，如端口到端口转发、广播风暴控制、通过 ACL 规则进行 MAC/IP/端口过滤、VLAN 配置、流量镜像和带宽限制。

# CRS3xx 与 CSS3xx 系列手册

## 概述

SwOS 是一款专为 MikroTik 交换机产品管理而设计的操作系统。它提供了基础的可管理交换机功能，并具备高级特性，如端口到端口转发、广播风暴控制、通过 ACL 规则进行 MAC/IP/端口过滤、VLAN 配置、流量镜像和带宽限制。

SwOS 仅通过 Web 浏览器（HTTP）在 IPv4 上进行管理。不支持控制台访问、SSH、API 或其他管理接口。

---

## 连接交换机

打开 Web 浏览器并输入默认管理 IP 地址。

![Swos login css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-01.webp)

* **默认 IP 地址**：`192.168.88.1`
* **默认用户名**：`admin`
* **默认密码**：*（空白）*

---

## 系统选项卡

系统选项卡管理常规配置参数、设备发现选项和管理安全性。

![Swos system css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-02.webp)

### 系统管理设置

| 属性 | 描述 |
| :--- | :--- |
| **地址获取** | 定义通过静态设置、带回退的 DHCP 或仅 DHCP 进行 IP 分配。 |
| **静态 IP 地址** | 指定用于管理访问的静态 IPv4 地址。 |
| **标识** | 为交换机标识符设置可自定义名称。 |
| **允许来源** | 将管理 Web 访问限制到指定的 IP 范围或子网。 |
| **允许来源端口** | 将 Web 访问限制到指定的物理交换机接口。 |
| **允许来源 VLAN** | 将访问限制到特定的入站 VLAN ID 配置文件。 |

![SwOS Management](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-03.webp)

### DHCP 与 PPPoE 侦听

SwOS 内置安全机制，可在指定的不可信接口上阻止未经授权或恶意的 DHCP 服务器和 PPPoE 发现序列。

![CSS326 DHCP Snooping](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-04.webp)

### 配置安全与维护

下方区域处理备份和管理密码。

![Swos system3 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-05.webp)

* **更改密码**：更新设备访问密钥。
* **备份配置**：将当前设置保存到本地文件。
* **恢复配置**：上传并应用现有配置状态。

---

## 链路选项卡

链路选项卡配置物理链路参数，并监控每个接口的活动连接属性。

![Swos link css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-06.webp)

* **链路配置文件**：管理接口状态，切换速度/双工自动协商，并控制流控暂停帧。

---

## PoE 选项卡

*（适用于支持以太网供电分配功能的设备）*

![SwOS PoE](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-07.webp)

* 支持配置供电设置（`auto`、`on`、`off`），并在功率受限事件期间建立端口优先级。

---

## SFP 选项卡

为连接的 SFP/SFP+ 光模块提供可视化诊断。

![Swos sfp1 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-08.webp)

* 监控内部诊断信息，如工作温度、激光器供电电压、TX/RX 功率水平以及硬件序列号字符串。

---

## 转发与端口隔离

管理整个交换架构中的二层数据包转发表。

![Swos forw css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-09.webp)
![Swos ivl system](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-10.webp)

### 端口隔离与隔离组

端口隔离在内部划分广播域，无需增加子网层级即可控制客户端通信。

![SwOS Isolated Groups](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-11.webp)
![SwO isolation example3](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-12.webp)

---

## LAG（链路聚合）

将物理接口捆绑为单个高吞吐量通道，可使用动态 LACP 链路或静态阵列。

![Swos lag css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-13.webp)

---

## RSTP（快速生成树协议）

提供环路避免架构和结构冗余参数。

![Swos rstp css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-14.webp)

* 支持使用经典短路径或现代长路径评估结构配置自定义桥接路径开销。

---

## VLAN 与 VLAN 矩阵配置

VLAN 路由规则将入站数据包分类行为与出站格式表分离。

### VLAN 选项卡（入站控制）

处理入站流量流的端口行为。

![Swos vlan css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-15.webp)

* **VLAN 模式**：在 `disabled`、`optional`、`enabled` 和 `strict` 模式下配置入口约束。

![Swos strict vlans](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-16.webp)

* **默认 VLAN ID**：设置分配给入站未标记流量的端口 VLAN ID（PVID）。

![Default vlan id](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-17.webp)

### VLANs 选项卡（出站映射）

定义跨目标中继端口的广播成员资格和处理方式。

![Swos vlans css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-18.webp)
![Swos vlans menu](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-19.webp)

#### 传统模式模板

* **接入接口**：将标准未标记端点配对到特定目标 VLAN 标签。

  ![Access ports](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-20.webp)

* **中继与混合选项**：在主要核心上行链路上混合多个带标记的流量流，并可选配未标记的本征路由路径。

  ![Hybrid ports](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-21.webp)
  ![Swos hybrid](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-22.webp)
  ![Swos hybrid vlan](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-23.webp)

---

## 私有 VLAN

在共享基础设施空间中强制执行安全的端口通信配置文件。

![SwOS Private VLAN](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-24.webp)

---

## 主机选项卡

显示通过入站源地址发现的活动硬件转发数据库（FDB）动态条目。

![Swos shost css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-25.webp)

---

## IGMP 侦听

过滤组播分发，跟踪活动组订阅以阻止组播泛洪。

![IGMP snooping](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-26.webp)
![CSSxx IGMP](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-27.webp)
![IGMP vlantab](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-28.webp)

---

## SNMP 选项卡

通过标准 SNMP 结构启用监控。

![Swos snmp2 1](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-29.webp)

---

## ACL 选项卡（访问控制列表）

执行硬件卸载的过滤规则，匹配 L2/L3/L4 帧头中的模式以丢弃或重定向数据包。

![CRS326 ACL table](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-30.webp)

---

## 诊断：统计、错误和直方图

跟踪接口计数器、丢弃帧、错误模式以及详细的结构化链路历史诊断。

![Swos stat1 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-31.webp)
![Swos stat2 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-32.webp)
![Swos stat3 css326](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-33.webp)

---

## 健康选项卡

监控硬件运行环境，跟踪系统核心温度和运行输入电压。

![SwOS CRS328 health](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-34.webp)

---

## 双启动操作

许多 CRS 硬件单元支持双启动设计，允许在 RouterOS 或 SwOS 之间切换运行。

![Router board settings](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-35.webp)
![Router board settings webfig](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-36.webp)
![Dual boot option](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-37.webp)

使用 RouterOS CLI 接口将操作系统切换到 SwOS 时，使用以下系统命令结构：

```bash
/system routerboard settings set boot-os=swos
```

## 重置与重新安装

可以使用系统菜单中的“重置配置”按钮重置 SwOS 配置。如果 SwOS Web 管理不可用，仍可通过其他选项重置配置。

CSS326-24G-2S+ 和 CSS318-16G-2S+IN 设备内置备份 SwOS 固件，可在标准固件损坏或升级失败时加载：

* 在 CSS326-24G-2S+ 和 CSS318-16G-2S+IN 启动时按住重置按钮几秒钟，可重置配置并加载备份固件。
* 加载备份固件后，可以使用 Web 浏览器连接到 192.168.88.1（或从 DHCP 服务器租用的地址）并安装新的 SwOS 固件。

双启动设备可以使用重置按钮启动 RouterOS。在按住重置按钮的同时为设备供电，等待用户 LED 开始闪烁（约 5 秒）。这将重置 RouterOS 配置，设备将启动进入 RouterOS。设备可通过 RouterOS 访问后，即可升级和重置 SwOS 配置。请参阅文章 - 使用 RouterOS 配置 SwOS。

带有串行控制台的 CRS3xx 设备具有其他选项。

要在 RouterOS 和 SwOS 之间切换，请按照以下步骤操作：

1. 使用串行控制台连接到设备
2. 进入 RouterBOOT 设置
3. 选择“j - boot os”
4. 选择 RouterOS 或 SwOS

在标准固件损坏或升级失败时，可以加载 SwOS 备份固件：

1. 使用串行控制台连接到设备
2. 启动 SwOS
3. 选择“p - boot primary SwOS”
4. 加载备份固件后，可以使用 Web 浏览器连接到 192.168.88.1（或从 DHCP 服务器租用的地址）并安装新的 SwOS 固件。

要重置 SwOS 配置：

1. 使用串行控制台连接到设备
2. 启动 SwOS
3. 选择“r - reset configuration”

![Swos reset](https://manual.mikrotik.com/docs/bridging-and-switching/swos/img/crs3-38.webp)