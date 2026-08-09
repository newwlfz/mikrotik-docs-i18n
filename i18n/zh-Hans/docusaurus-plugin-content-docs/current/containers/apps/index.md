# 应用

> “应用”菜单提供了一个预配置应用目录，可通过容器进行部署，并自动完成 RouterOS 配置，同时支持多个容器注册表。它需要安装容器包，初始设置需物理访问设备，并包含证书验证和硬件设备管理等安全考量。

# 应用

#### 概述

**子菜单:** `/app`  
**所需软件包:** `container`

应用菜单提供了一个应用目录，可通过几次点击完成部署。每个应用可由一个或多个预配置的容器组成，并且必要的 RouterOS 配置（如防火墙规则和地址转换）将自动应用。该目录由 MikroTik 准备和维护，但容器镜像来源于多个注册表，如 Docker Hub、GCR 和 Quay。

然而，配置参数可以在启用应用前进行编辑，并且应用的 YAML 文件始终可以查看。

#### 要求

应用系统继承了容器包的相同要求：

- **架构支持：** arm64 和 x86 架构。
- **容器包：** 必须安装。
- **设备模式：** 必须启用容器模式（需要物理访问和设备重置）。
- **外部存储：** 强烈推荐用于最佳性能。
- **内存要求：** 足够的 RAM 用于容器操作（16MB SPI 闪存设备可能需要外部存储来存放镜像）。
- **架构限制：** 具有 EN7562CT CPU 的设备（如 hEX Refresh）不受支持。

#### 安全考量

与底层容器系统一样，应用菜单继承了安全影响：

- 需要物理访问才能初始启用容器支持。
- 一旦启用，容器可以远程管理。
- 被入侵的设备可以使用容器安装恶意软件。
- 设备安全等同于运行容器的安全性。
- 第三方容器镜像可能引入安全漏洞。

## 属性

| 属性 | 类型 | 默认值 | 描述 |
| :-- | :-- | :-- | :-- |
| **auto-update** | *yes* &#124; *no* | *no* | 启用或禁用有新容器镜像版本可用时的自动更新。 |
| **check-certificate** | *yes* &#124; *no* | *yes* | 在拉取容器镜像前，根据路由器的[证书存储](../../authentication-authorization-accounting/certificates.md)验证注册表证书。 |
| **container-command-lines** | *string* | *(空)* | 指定启动容器时传递给应用程序的命令行参数。 |
| **devices** | *string* | *(空)* | 指定要透传给容器应用程序的额外硬件设备。 |
| **environment** | *string* | *(空)* | 定义可供运行中应用程序使用的环境变量。指定为键值对列表。 |
| **extra-mounts** | *string* | *(空)* | 指定要附加到容器的额外挂载点。 |
| **firewall-redirects** | *string* | *(空)* | 配置从主机设备到容器的端口重定向。 |
| **network** | *default* &#124; *lan* &#124; *internal* | *default* | 指定容器将使用的网络：**internal**（位于 NAT 后）、**lan**（位于 LAN 网络上）或 **default**（因应用而异；可以是 internal 或 lan）。 |
| **network-outgoing-access** | *yes* &#124; *no* | *yes* | 允许特定容器应用的网络出站访问，当设置为 `no` 时，会创建一条 mangle drop 规则。 |
| **pvid** | *integer* | *1* | 在桥接中为容器的虚拟以太网接口设置端口 VLAN ID（PVID）。 |
| **required-hw-devices** | *string* | *(空)* | 容器启动时主机上必须存在的硬件设备。此属性仅在添加 YAML 配置后可配置。**Compose 格式：**`[主机硬件设备]:[应用内设备]` |
| **required-mounts** | *string* | *(空)* | 容器启动所需的挂载目录。此属性仅在添加 YAML 配置后可配置。**Compose 格式：**`[主机目录]:[应用内目录]` |
| **use-https** | *yes* &#124; *no* | *yes* | 为应用程序 URL 使用 HTTPS。此选项在不支持云服务的设备上无效。 |
| **yaml** | *string* | *(空)* | 提供应用程序的 YAML 组合配置。有关配置示例，请参阅文档。 |

## 只读属性

| 属性 | 类型 | 默认值 | 描述 |
| :-- | :-- | :-- | :-- |
| **app-size** | | | 应用程序的总大小。 |
| **app-store-url** | *string* | | 安装应用程序的应用商店的 URL。 |
| **cpu-usage** | | | 应用程序当前使用的 CPU 百分比。 |
| **custom** | *yes* &#124; *no* | | 指示应用程序是否是由用户创建的自定义应用程序。 |
| **data-size** | | | 应用程序存储的数据大小。 |
| **default-credential** | *string* | | 应用程序所需的默认凭据。 |
| **default-network** | *lan* &#124; *internal* | | 应用程序使用的默认网络。有效值为 `lan` 或 `internal`。 |
| **description** | *string* | | 应用程序描述，如 YAML 配置的 `descr` 参数中所定义。 |
| **from-app-store** | *yes* &#124; *no* | | 指示应用程序是否从自定义应用商店安装。 |
| **interface** | *string* | | 应用程序使用的 VETH 接口。 |
| **ip-address** | *IP* | | 分配给 VETH 接口的 IP 地址。 |
| **memory-current** | | | 应用程序当前使用的内存量。 |
| **name** | *string* | | 应用程序名称，如 YAML 配置的 `name` 参数中所定义。 |
| **project-page** | *string* | | 应用程序项目页面 URL，如 YAML 配置的 `page` 参数中所定义。 |
| **running** | | | 指示应用程序当前是否正在运行。 |
| **status** | *acquire veth* &#124; *configuring container(s)* &#124; *downloading/extracting* &#124; *starting* | | 应用程序的当前状态。可能的值表示应用程序正在获取 VETH 接口、配置容器、下载/解压或正在启动。 |
| **ui-url** | *string* | | 应用程序 Web 界面的生成 URL（如果可用）。 |
| **variables-to-be-used-in-environment** | | | 应用程序环境中存在的所有变量列表。 |

#### 设置向导

应用菜单包含一个设置向导（GUI 中的“设置”按钮，或命令 `/app/setup`）。此向导自动完成所有网络、存储和注册表设置，否则这些设置需要多个手动步骤。

##### 第 1 步：存储选择

选择用于安装应用程序的存储磁盘。系统自动检测可用的已格式化磁盘驱动器（如 nvme1、usb1、disk1 及类似设备）。如果列表中没有合适的磁盘，您必须首先使用 ext4 或 btrfs 文件系统格式化磁盘，然后通过 `/disk` 菜单挂载它。

**要求：**

- 建议最低 100 MB/s 的顺序读写速度。
- 建议最低 10,000 随机 IOPS（每秒输入/输出操作数）。
- 在继续之前，使用 `/disk/test` 命令验证存储性能。
- 强烈推荐使用外部存储设备以获得最佳性能。

##### 第 2 步：桥接配置

选择用于容器网络的 LAN 桥接接口。此配置可实现自动端口转发和本地网络上的应用自动发现。设置向导自动配置以下内容：

- 虚拟以太网（veth）接口创建
- 将 veth 接口添加到已配置的桥接
- 用于出站连接的 NAT 规则

##### 第 3 步：IP 配置

定义路由器的 IP 地址以启用应用程序访问。系统自动检测主 IP 地址；但是，对于复杂的网络设置，支持手动配置。指定的 IP 地址用于以下目的：

- 生成应用程序 UI URL。
- 创建自动端口转发规则。
- 提供 WebFig 集成链接。

##### 完成

完成设置向导后，应用系统即可立即使用。您可以直接通过界面启用应用程序。系统自动处理所有底层容器配置。

#### 配置

应用配置可通过 `/app/settings` 访问，与手动容器配置相比，提供了简化的设置。

## 属性

| 属性 | 类型 | 默认值 | 描述 |
| :-- | :-- | :-- | :-- |
| **app-store-urls** | *string* | *(空)* | 自定义应用商店的 URL。该 URL 必须指向一个 YAML 数组，其中每个应用程序都是数组中的一个元素。 |
| **auto-update** | *yes* &#124; *no* | *no* | 全局设置，为所有已安装的应用程序包启用自动更新。 |
| **disk** | *string* | *(空)* | 全局设置，指定用于存储操作的磁盘。 |
| **download-path** | *string* | *(空)* | 手动指定所有下载内容的存储目录路径。 |
| **lan-bridge** | *string* | *(空)* | 手动指定代表局域网的桥接接口。 |
| **media-path** | *string* | *(空)* | 手动指定所有媒体文件的存储目录路径。 |
| **registry-mirrors** | *string* | *(空)* | 指定一个或多个用于容器镜像获取的注册表镜像 URL 地址。 |
| **router-ip** | *IP* | *(空)* | 手动指定当前 RouterOS 设备可达的 IP 地址。 |
| **show-in-webfig** | *yes* &#124; *no* | *yes* | 控制是否在 WebFig 登录页面上显示已启用应用程序的链接。 |

### 自动配置设置

某些参数最初根据网络检测自动配置。如果需要，这些值始终可以手动覆盖。

| 属性 | 类型 | 默认值 | 描述 |
| :-- | :-- | :-- | :-- |
| **assumed-router-ip** | *IP* | *(检测到的)* | 自动检测到的 RouterOS 设备的网络 IP 地址。 |
| **assumed-lan-bridge** | *string* | *(检测到的)* | 自动检测到的用于 LAN 连接的桥接接口。 |
| **assumed-media-path** | *string* | *disk/media* | 默认媒体存储路径，通常位于系统磁盘上。 |
| **assumed-download-path** | *string* | *disk/media/downloads* | 默认下载目录路径，通常位于媒体存储区域内。 |

#### 应用程序管理

应用程序通过 `/app` 接口管理，提供状态监控和生命周期控制，类似于底层的 `/container` 系统：

```
/app> print 
Flags: X - DISABLED, R - RUNNING
Columns: NAME, UI-URL, MEMORY-CURRENT, APP-SIZE, DATA-SIZE, CATEGORY, DESCRIPTION
```

##### 状态指示器和元数据

- **标志：**
  - X（已禁用） - 可以表示两种状态：未下载/未安装（APP-SIZE 和 DATA-SIZE 将为空），或已下载但已禁用（APP-SIZE 和 DATA-SIZE 显示存储使用情况）。
  - R（运行中） - 应用程序正在积极运行且可访问。
- **UI-URL：** 应用程序运行时的直接 Web 界面访问 URL。
- **MEMORY-CURRENT：** 实时内存消耗（以 MiB 为单位）（仅在运行时显示）。
- **APP-SIZE：** 容器镜像存储消耗（以 MiB 为单位）（下载后显示占用的空间）。
- **DATA-SIZE：** 应用程序持久数据大小（以 KiB/MiB 为单位）（显示配置和用户数据）。
- **CATEGORY：** 应用程序功能分类。
- **DESCRIPTION：** 应用程序功能描述。

##### 应用程序生命周期管理

### 部署过程

与需要多个配置步骤（veth 接口、桥接设置、环境变量、挂载和防火墙规则）的手动容器部署不同，应用部署自动化了整个流程：

1. **选择：** 通过 CLI 或 WebFig 从目录中选择一个应用程序。
2. **下载：** 自动下载和解压容器镜像。
3. **网络设置：** 自动配置 veth 接口和桥接。
4. **端口转发：** 自动创建用于 Web 访问的防火墙规则。
5. **启动：** 使用预配置的设置初始化容器。
6. **访问：** UI-URL 变为可用，可立即访问 Web 界面。

#### 清理命令

清理命令提供完整的应用程序移除，包括所有相关数据。此操作具有破坏性且不可逆：

```
/app> cleanup pihole 
App data will be lost, continue? [y/N]:
```

**清理过程：**

1. 停止正在运行的容器。
2. 移除所有应用程序数据和配置文件。
3. 从存储中删除容器镜像。
4. 将应用程序重置为未安装状态（APP-SIZE 和 DATA-SIZE 为空）。
5. 移除特定于应用程序的网络配置。

:::warning

所有用户数据、配置设置和应用程序状态将永久丢失。应用程序将恢复到其原始目录状态，如果被清理，则需要完全重新配置。

:::

#### 用户可添加应用

从 RouterOS v7.22 开始，您可以使用 compose YAML 文件创建自己的自定义应用。这使经验丰富的用户能够构建适合其特定网络需求的解决方案。

工作原理：

- 您编写一个 compose YAML 文件来定义应用的结构和行为
- RouterOS 处理此文件以构建可工作的应用程序包
- 您的自定义应用可以与 RouterOS 功能和 API 协同工作

为什么使用它：

- 为您的网络精确构建所需内容
- 无需等待官方应用发布
- 非常适合自动化、自定义路由或专业服务
- 声明式设置使管理更轻松

## 使用 YAML 创建自定义应用

您可以使用 YAML 配置文件创建自定义容器应用程序。此示例演示如何设置一个运行 iperf3 服务器以进行网络性能测试的 Alpine Linux 容器。

### YAML 配置示例

```routeros
name: alpine-iperf
descr: Alpine Linux container running iperf3 server
page: https://iperf.fr/
category: network
default-credential: none
services:
  iperf:
    image: docker.io/alpine:latest
    ports:
      - 5201:5201:tcp
      - 5201:5201:udp
    command: /bin/sh -c "apk add --no-cache iperf3 && iperf3 -s"
```

:::warning
端口 `80` 默认被假定为 Web 端口，除非明确命名（例如，`888:80:web`）。健康检查会探测此端口——如果没有服务在监听，应用将看起来卡在 `starting` 状态。当端口 `80` 未被映射时，将使用第一个定义的端口。为避免歧义，请明确命名您使用的端口：

```
9000:9000:api
9001:9001:api-secure
```

:::

### 配置字段参考

| 字段 | 描述 |
|---|---|
| `name` | 自定义应用的唯一标识符 |
| `descr` | 应用功能的人类可读描述 |
| `page` | 项目官方文档或网站的 URL |
| `category` | 分类组（例如，network、system、utilities） |
| `default-credential` | 认证要求（none，或指定用户名/密码） |
| `services` | 容器服务定义 |
| `image` | 用于容器的 Docker 镜像 |
| `volumes` | 挂载位置 `RouterOS:Container` |
| `ports` | 端口映射，格式为 `host:container:protocol` |
| `environment` | 环境变量 |
| `command` | 在容器内执行的启动命令 |
| `networks` | 应用网络配置 |

### 此示例的工作原理

1. **基础镜像**：使用来自 Docker Hub 的官方 Alpine Linux 镜像
2. **软件包安装**：安装 iperf3 网络性能测试工具
3. **服务器模式**：以服务器模式运行 iperf3（`-s` 标志）以接受客户端连接
4. **端口暴露**：将 TCP 和 UDP 端口 5201（iperf3 的默认端口）映射到主机

此配置创建了一个充当网络吞吐量测试服务器的容器，允许您测量客户端与此容器之间的带宽。

## 添加自定义应用

有两种创建自定义应用的方法：导入 .yml 文件，或创建空白应用并直接编辑其 YAML。

在此示例中，我们将添加使用 compose 文件创建的 alpine-iperf 应用。为方便使用，我们将其放置在 LAN 桥接中，以便我们网络上的设备无需 NAT 即可轻松访问它。

### 方法 1：创建空白应用并编辑 YAML

首先，创建应用并将其分配到 LAN 网络：

```routeros
/app/add network=lan
```

默认情况下，应用将被命名为“app”。

接下来，添加 YAML 配置。在终端中运行：

```routeros
/app/edit app yaml
```

这将打开一个文本编辑器，您可以在其中粘贴 YAML。粘贴后，按 <kbd>Control</kbd>+<kbd>O</kbd> 保存更改。最后，启用应用以使其开始运行。

### 方法 2：从文件导入

或者，将您的 compose 文本保存到文件中并上传到设备。然后，使用以下命令将文件设置为应用的 YAML：

```routeros
/app/add yaml=[/file/get alpine-iperf.yml contents]
```

当您有预配置的 YAML 文件准备导入时，此方法非常有用。

#### 提示和最佳实践

- **存储：** 为获得最佳性能和更大容量，请考虑使用外部存储设备，如 USB 驱动器、SATA 驱动器或 NVMe SSD。

- **内存：** 通过在终端中运行 `/app/print` 命令来跟踪应用程序的内存消耗。

- **更新：** 仅在需要且认为必要时更新您的系统。虽然自动更新可以提供安全补丁和新功能，但在启用或应用更新之前，评估您的特定用例是否需要更新非常重要。

- **网络：** 应用程序自动管理端口转发并生成外部访问所需的 URL。

- **数据持久性：** 您的应用程序数据存储在指定的存储路径中，即使在应用程序重启或系统重启后也会保持完整。