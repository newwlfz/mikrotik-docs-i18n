# 容器

> 本文档介绍 MikroTik RouterOS 的容器支持，涵盖配置、虚拟接口、存储和安全注意事项。它详细说明了重启间隔、DNS 设置、CPU 分配和内存限制等属性，用于运行容器化服务，同时提醒相关安全风险。

# 容器

import DocCardList from '@theme/DocCardList';

本节涵盖 RouterOS 容器支持，包括容器配置、虚拟以太网接口、存储和应用示例。用于在 RouterOS 设备上运行受支持的容器化服务。

<DocCardList />

**所需软件包：** `container`

容器是 MikroTik 对 Linux 容器的实现，允许用户在 RouterOS 中运行容器化环境。容器功能适用于最新的 MikroTik RouterOS v7.x 版本。容器兼容来自 Docker Hub、GCR、Quay 或其他提供商的镜像，以及在其他设备上构建的镜像，使用这些提供商支持的相同格式。虽然 RouterOS 使用的语法与 Docker 不同，但实现了类似的功能。

## 免责声明

:::danger
您需要物理访问 RouterOS 设备才能启用容器功能支持；该功能默认处于禁用状态；

- 一旦容器功能被启用，容器可以被远程添加/配置/启动/停止/移除！
- 如果您的 RouterOS 设备被入侵，容器可被用来轻松地在您的 RouterOS 设备上及通过网络安装恶意软件；
- 您的 RouterOS 设备的安全性等同于您在容器中运行的任何内容；
- 如果您运行容器，不提供任何形式的安全保证；
- 在您的 RouterOS 设备上运行第三方容器镜像可能会打开安全漏洞/攻击向量/攻击面；
- 精通漏洞利用构建的专家将能够越狱/提权至 root；

:::

### 安全风险

- 当安全专家发布其漏洞研究时，任何人都可以利用该漏洞。
- 有人可以构建一个能够利用该漏洞并提供 Linux root shell 的容器镜像。
- 通过使用 root shell，即使容器镜像被移除且容器功能被禁用，攻击者也可能在您的 RouterOS 系统中留下永久后门/漏洞。
- 如果漏洞被注入到主或次 RouterBOOT（或供应商预加载器）中，即使 Netinstall 也可能无法修复。

## 要求

容器软件包兼容 **arm、arm64** 和 **x86** 架构。使用远程镜像（类似于 docker pull）功能需要主内存中有大量可用空间，16MB SPI 闪存板可以使用 USB 或其他磁盘介质上的预构建镜像。

:::danger

- 建议使用至少支持 100MB/s 顺序读写速度和 10K 随机 IOPS 的外部磁盘。使用较慢的磁盘时，容器解压时间可能会变长。
- 需要安装容器软件包
- 对于使用 EN7562CT CPU 的设备（如 hEX Refresh），仅支持 [arm32v5](https://hub.docker.com/u/arm32v5) 容器镜像，这意味着可运行的容器数量有限。

:::

**子菜单：** `/container`

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **restart-interval** (*字符串*; 默认值: ) | 指定容器失败时重启的时间间隔。示例：10s |
| **cmd** (*字符串*; 默认值: ) | CMD 的主要目的是为正在执行的容器提供默认值。这些默认值可以包含可执行文件，也可以省略可执行文件，在这种情况下，您还必须指定 ENTRYPOINT 指令。 |
| **comment** (*字符串*; 默认值: ) | 简短描述 |
| **dns** (*字符串*; 默认值: ) | 如果容器需要不同的 DNS，可以在此处配置 |
| **domain-name** (*字符串*; 默认值: ) | 设置容器的域名 |
| **entrypoint** (*字符串*; 默认值: ) | ENTRYPOINT 允许您指定启动容器时要运行的可执行文件。示例：`/bin/sh` |
| **envlist** (*字符串*; 默认值: ) | 要与容器一起使用的环境变量列表（在 *`/container/envs`* 下配置） |
| **file** (*字符串*; 默认值: ) | 如果容器是从文件导入的，则为容器 \*tar.gz tarball |
| **hostname** (*字符串*; 默认值: ) | 为容器分配主机名有助于更轻松地识别和管理容器 |
| **interface** (*字符串*; 默认值: ) | 要与容器一起使用的 veth 接口 |
| **logging** (*字符串*; 默认值: ) | 如果设置为 yes，容器生成的所有输出将显示在 RouterOS 日志中 |
| **start-on-boot** (*字符串*; 默认值: ) | 如果设置为 yes，容器将在设备启动时自动启动。 |
| **mountlists** (*字符串*; 默认值: ) | 来自 /container/mounts/ 子菜单的挂载，用于此容器 |
| **mount** (*字符串*; 默认值: ) | 指定要用作挂载的目录 |
| **remote-image** (*字符串*; 默认值: ) | 如果使用外部注册表（在 `/container/config/set` registry-url=... 下配置），则为要安装的容器镜像名称 |
| **root-dir** (*字符串*; 默认值: ) | 用于将容器存储保存在主内存之外 |
| **stop-signal** (*字符串*; 默认值: 15) | 定义在 10 秒后容器仍在运行时发送哪个 Linux 信号来终止容器。不同的信号可能允许优雅关闭、立即终止或触发特定于应用程序的操作 |
| **workdir** (*字符串*; 默认值: ) | cmd entrypoint 的工作目录 |
| **devices** (*字符串*; 默认值: ) | 将物理设备直通给容器 |
| **cpu-list** (*字符串*; 默认值: ) | 指定容器允许在哪些 CPU 核心上运行 |
| **user** (*字符串*; 默认值: ) | 设置容器进程在执行前运行的用户和组。 |
| **memory-high** (*整数*; 默认值: ) | 特定容器的“软”RAM 使用限制（字节）。如果使用量超过高水位线，进程将被限制并置于回收压力之下。 |
| **memory-max** (*整数*; 默认值: ) | 每个容器的最大 RAM 使用限制（字节）（如果 memory-max 值小于容器 memory-current，容器进程将被终止）从 7.23 开始，此参数不能设置为低于 1MB，以避免容器在启动过程中过早被终止 |
| **swap-max** (*整数*; 默认值: ) | 容器可以使用的最大交换空间量（字节）。要求设备上已启用交换（参见 [交换空间](../hardware/disks/index.md)）。 |
| **stop-time** (*字符串*; 默认值: ) | 在发送 stop-signal 之前，容器优雅停止的时间限制。 |
| **tmpfs** (*字符串*; 默认值: ) | 容器的临时文件系统挂载点。格式：`size@dir`，例如 `64M@/tmp`。 |
| **layer-dir** (*字符串*; 默认值: ) | 用于存储容器镜像层的目录，用于容器之间的共享层存储。 |
| **shm-size** (*整数*; 默认值: ) | 容器的 `/dev/shm` 共享内存文件系统大小（字节）。 |
| **default-dns** (*字符串*; 默认值: ) | 从系统 `/ip/dns` 配置继承的默认 DNS 服务器。 |
| **hosts** (*字符串*; 默认值: ) | 容器的自定义主机名到 IP 地址映射。格式：`host=ip`。 |
| **restart-policy** (*字符串*; 默认值: ) | 定义容器的重启策略：`no`（永不重启）、`on-failure`（仅在非零退出码时重启）或 `always`（始终重启）。 |
| **restart-max-count** (*整数*; 默认值: ) | 在 restart-interval 时间范围内允许的最大重启尝试次数。 |
| **stop-on-unhealthy** (*字符串*; 默认值: ) | 如果设置为 `yes`，当健康检查状态变为不健康时，容器将自动停止。 |

:::warning
默认情况下，容器使用与 `/ip/dns` 子菜单中配置的相同 DNS。如果此处未配置 DNS 且未指定容器的 `dns` 参数，容器将无法启动！
:::

### 菜单特定命令

| 属性 | 描述 |
| :-- | :-- |
| **update** | 更新容器镜像。自动从容器仓库拉取并解压，替换原始镜像。 |
| **kill** | 终止指定的正在运行的容器。 |
| **restart** | 重启指定的正在运行的容器。 |
| **repull** | 重新拉取/解压容器镜像。 |
| **shell** | 进入正在运行的容器的 shell。 |
| **run** | 启动容器并进入其 shell。如果容器运行后关闭，此命令很有用。 |

## 容器配置

**子菜单：** `/container/config`

| 属性 | 描述 |
| :-- | :-- |
| **registry-url** | 从中下载容器的外部注册表 URL（默认值：`https://lscr.io/`） |
| **tmpdir** | 容器解压目录 |
| **layer-dir** | 用于存储容器镜像层的目录，用于容器之间的共享层存储 |
| **memory-high** | 特定容器的全局“软”RAM 使用限制（字节）。如果使用量超过高水位线，进程将被限制并置于回收压力之下。 |
| **memory-max** | 每个容器的全局最大 RAM 使用限制（字节）（如果 memory-max 值小于容器 memory-current，容器进程将被终止）从 7.23 开始，此参数不能设置为低于 1MB，以避免容器在启动过程中过早被终止 |
| **swap-max** (*整数*; 默认值: ) | 每个容器最大交换空间量的全局默认值（字节）。单个容器可以使用自己的 `swap-max` 设置覆盖此值。要求设备上已启用交换（参见 [交换空间](../hardware/disks/index.md)）。 |
| **username** | 指定用于认证的用户名（从 ROS 7.8 开始） |
| **password** *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 指定用于认证的密码（从 ROS 7.8 开始） |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **assumed-registry-url** | 自动检测到的注册表 URL。 |
| **memory-current** | 所有容器当前的总内存使用量（字节）。 |

## 示例

### 运行 Pi-hole

#### 前提条件

   1. 运行 RouterOS v7.4beta 或更高版本且**已安装容器软件包**的 RouterOS 设备 - [如何安装软件包](../getting-started/installation-and-upgrade/packages.md)
   2. 物理访问设备以启用容器模式 - 将在下面说明
   3. 连接用于存储的 HDD、SSD 或 USB 驱动器 - 使用 RouterOS 支持的文件系统格式化 - [如何格式化/管理磁盘](../hardware/disks/index.md)

#### 运行 Pi-hole 的步骤

1. 启用容器模式并按照命令给出的说明操作（了解更多关于 [设备模式](../system-information-and-utilities/device-mode.md) 的信息。您需要按下 [重置按钮](../getting-started/configuration-management/routeros-configuration-reset.md) 或冷重启（如果在 x86 上使用容器）来确认设备模式：

   ```routeros
   /system/device-mode/update container=yes 
   ```

   :::danger
   [设备模式](../system-information-and-utilities/device-mode.md) 默认限制容器使用，在授予容器模式访问权限之前 - 确保您的设备完全安全。
   :::
2. 创建一个新的 veth 接口，并在网络中唯一的范围内分配 IP 地址：

   ```routeros
   /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
   ```

   :::info
   以下配置等同于其他容器引擎（如 Docker）中的“桥接”网络模式。也可以创建“主机”等效配置。

   **重要提示：** 一个 veth 接口可用于多个容器。您可以创建多个 veth 接口来为不同的容器创建 [隔离](./index.md#isolated-containers) 网络。
   :::
3. 创建一个新的 [桥接](../bridging-and-switching/index.md)，用于您的容器，并分配与 veth 接口网关相同的 IP 地址：

   ```routeros
   /interface/bridge/add name=containers
   /ip/address/add address=172.17.0.1/24 interface=containers
   ```

4. 将 veth 接口添加到您新创建的桥接中：

   ```routeros
   /interface/bridge/port/add bridge=containers interface=veth1
   ```

5. 为出站流量创建 NAT：

   ```routeros
   /ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
   ```

6. 为容器创建环境变量：

   ```routeros
   /container/envs/add list=ENV_PIHOLE key=TZ value="Europe/Riga"
   /container/envs/add list=ENV_PIHOLE key=FTLCONF_webserver_api_password value="mysecurepassword"
   /container/envs/add list=ENV_PIHOLE key=DNSMASQ_USER value="root"
   ```

7. 为容器创建挂载卷：

   ```routeros
   /container/mounts/add list=MOUNT_PIHOLE_PIHOLE src=disk1/volumes/pihole/pihole dst=/etc/pihole
   /container/mounts/add list=MOUNT_PIHOLE_DNSMASQD src=disk1/volumes/pihole/dnsmasq.d dst=/etc/dnsmasq.d
   ```

   :::warning
   `src=` 指向 RouterOS 位置（例如，如果您决定将配置文件放在外部 USB 介质上，也可以是 `src=disk1/etc_pihole`），`dst=` 指向定义的位置（请查阅容器的手册/维基/GitHub 以了解指向何处）。如果 `src` 目录在首次使用时不存在，则将使用容器在 `dst` 位置的内容填充。
   :::

   :::warning
   强烈建议将任何容器卷放置在连接到 RouterOS 设备的磁盘上。避免将容器卷放在内置存储上。
   :::
8. 配置使用特定的容器仓库，例如使用 Docker.io：

   ```routeros
   /container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
   ```

9. 添加容器：

   ```routeros
   /container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

   :::tip
   如果您希望在 `/log/print` 中查看容器输出，则在创建容器时添加 `logging=yes`，root-dir 应指向外部驱动器。不建议将内部存储用于容器。

   **重要提示：** 有多种方式可以获取容器镜像，如果您需要其他添加容器镜像的方式，请查看 [添加容器镜像](./index.md#adding-a-container-image) 部分。

   **重要提示：** 添加容器将开始下载或解压它，容器本身在添加后不会启动，您需要在下载/解压完成后手动启动它。
   :::
10. 检查容器的状态，等待下载/解压完成且 `status=stopped`：

    ```routeros
    /container/print
    ```

11. 启动容器：

    ```routeros
    /container/start pihole
    ```

12. 为您的容器创建端口转发：

    ```ros
    /ip/firewall/nat
    add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
    ```

13. 您应该能够通过在 Web 浏览器中导航到 `http://192.168.88.1/admin/` 来访问 Pi-hole Web 面板。
14. 要在您的设备上开始使用 Pi-hole，请将其 DNS 配置更改为使用 `192.168.88.1` 作为 DNS 服务器。

### 添加容器镜像

有多种方式可以让容器镜像在您的 RouterOS 设备上运行。请查看下面的示例。

#### 选项 A：从外部库获取镜像

设置 registry-url（用于从 Docker 注册表下载容器）并将解压目录（tmpdir）设置为连接的 USB 介质：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=disk1/tmp
```

拉取镜像：

```ros
/container/add remote-image=pihole/pihole interface=veth1 root-dir=disk1/images/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

镜像将自动拉取并解压到 root-dir。可以使用以下命令检查状态：

```ros
/container/print
```

#### 选项 B：从 PC 导入镜像

您可以使用运行 Docker 或 Podman 的 PC 下载所需的容器镜像并将其保存到归档文件中。我们建议使用 [Podman](https://podman.io/docs/installation)，因为使用 Podman 更容易为特定架构构建和下载容器。

1. 根据您的 RouterOS 设备的架构下载所需的镜像。

   ```routeros
   # 对于 ARM64
   podman pull --arch=arm64 docker.io/pihole/pihole

   # 对于 ARM
   podman pull --arch=arm docker.io/pihole/pihole

   # 对于 AMD64
   podman pull --arch=amd64 docker.io/pihole/pihole
   ```

2. 将容器镜像保存到归档文件。

   ```routeros
   podman save pihole > pihole.tar
   ```

3. 将归档文件上传到您的 RouterOS 设备，例如：

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   您也可以使用 Winbox 上传文件！
   :::
4. 使用上传的容器镜像归档文件在 RouterOS 设备上创建容器。

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

#### 选项 C：在 PC 上构建镜像

您可以构建自己的容器并在 RouterOS 设备上使用。虽然您可以使用 Docker 构建容器，但我们建议使用 [Podman](https://podman.io/docs/installation)，因为使用 Podman 更容易为特定架构构建容器。

1. 获取所需容器镜像的源文件，例如使用 git。

   ```routeros
   git clone https://github.com/pi-hole/docker-pi-hole.git
   cd docker-pi-hole
   ```

2. 通过指定 Dockerfile 或 Containerfile 以及目标架构来构建容器镜像。

   ```routeros
   # 对于 ARM64
   podman build --platform linux/arm64 --tag pihole -f ./src/Dockerfile

   # 对于 ARM
   podman build --platform linux/arm --tag pihole -f ./src/Dockerfile

   # 对于 AMD64
   podman build --platform linux/amd64 --tag pihole -f ./src/Dockerfile
   ```

3. 将容器镜像保存到归档文件。

   ```routeros
   podman save pihole > pihole.tar
   ```

4. 将归档文件上传到您的 RouterOS 设备，例如。

   ```routeros
   rsync -av pihole.tar admin@192.168.88.1:/data/disk1/
   ```

   :::tip
   您也可以使用 Winbox 上传文件！
   :::
5. 使用上传的容器镜像归档文件在 RouterOS 设备上创建容器。

   ```routeros
   /container/add file=disk1/pihole.tar interface=veth1 root-dir=disk1/pihole mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
   ```

##### 替代方案：使用 Docker 构建容器镜像

要使用 Dockerfile 并制作自己的 docker 软件包 - 需要安装 docker 以及 buildx 或其他构建工具包。

安装后检查是否有额外的架构可用：

```bash
docker buildx ls
```

应返回：

```bash
NAME/NODE DRIVER/ENDPOINT STATUS  PLATFORMS
default * docker
  default default         running linux/amd64, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/arm/v7, linux/arm/v6
```

如果没有 - 安装额外的架构：

```bash
docker run --privileged --rm tonistiigi/binfmt --install all
```

拉取或创建包含 Dockerfile 的项目并构建、提取镜像（如有需要调整 --platform）：

```bash
git clone https://github.com/pi-hole/docker-pi-hole.git
cd docker-pi-hole
docker buildx build  --no-cache --platform arm64 --output=type=docker -t pihole .
docker save pihole > pihole.tar
```

将 *pihole.tar* 上传到您的 RouterOS 设备。

Linux 系统上的镜像和对象可以被 `pruned`

从 tar 镜像创建容器

```ros
/container/add file=pihole.tar interface=veth1 mountlists=MOUNT_PIHOLE_PIHOLE,MOUNT_PIHOLE_DNSMASQD envlist=ENV_PIHOLE name=pihole
```

### 网络示例

#### 带 NAT 的桥接

在此网络设置中，所有容器使用相同的 veth 接口，并且可以在没有任何防火墙限制的情况下相互通信，但您需要转发端口以允许访问容器的端口。

例如，一个数据库容器需要与一个 Web 应用程序容器通信；Web 应用程序需要将端口 `80` 暴露给外部世界，但数据库容器不需要向外部世界暴露任何端口。

- 网络配置：

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/bridge/add name=containers
  /ip/address/add address=172.17.0.1/24 interface=containers
  /interface/bridge/port/add bridge=containers interface=veth1
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  ```

- 数据库容器配置：

  ```routeros
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_DB value="webapp"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_USER value="webapp"
  /container/envs/add list=ENV_POSTGRES key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES src=disk1/volumes/postgres/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres mountlists=MOUNT_POSTGRES envlist=ENV_POSTGRES name=postgres start-on-boot=yes logging=yes
  ```

- Web 应用程序容器配置：

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin` 的端口 80 对所有人可访问，但 `postgres` 的端口 5432 不对所有人开放；它只能通过 `pgadmin` 作为 `127.0.0.1` 访问，或通过运行容器的 RouterOS 设备作为 `172.17.0.2` 访问。

#### 隔离容器

在此网络设置中，您有多个容器，并且希望确保其中一些可以在没有防火墙限制的情况下通信，但有些需要与其他容器隔离。例如，您可能希望创建两个数据库容器并将它们隔离。

- 网络配置。

  ```routeros
  /interface/veth/add name=veth1 address=172.17.0.2/24 gateway=172.17.0.1
  /interface/veth/add name=veth2 address=172.18.0.2/24 gateway=172.18.0.1
  /interface/bridge/add name=containers1
  /interface/bridge/add name=containers2
  /ip/address/add address=172.17.0.1/24 interface=containers1
  /ip/address/add address=172.18.0.1/24 interface=containers2
  /interface/bridge/port/add bridge=containers1 interface=veth1
  /interface/bridge/port/add bridge=containers2 interface=veth2
  /ip/firewall/nat
  add chain=srcnat action=masquerade src-address=172.17.0.0/24
  add chain=srcnat action=masquerade src-address=172.18.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=81 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=82 protocol=tcp to-addresses=172.18.0.2 to-ports=80
  ```

- 第一个和第二个数据库容器配置。

  ```routeros
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_DB value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_USER value="webapp1"
  /container/envs/add list=ENV_POSTGRES1 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES1 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES1 src=disk1/volumes/postgres1/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth1 root-dir=disk1/images/postgres1 mountlists=MOUNT_POSTGRES1 envlist=ENV_POSTGRES1 name=postgres1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_DB value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_PASSWORD value="<changeme>"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_USER value="webapp2"
  /container/envs/add list=ENV_POSTGRES2 key=PGDATA value="/var/lib/postgresql/data/pgdata"
  /container/envs/add list=ENV_POSTGRES2 key=POSTGRES_INITDB_ARGS value="--encoding='UTF8' --lc-collate='C' --lc-ctype='C'"
  /container/mounts/add list=MOUNT_POSTGRES2 src=disk1/volumes/postgres2/data dst=/var/lib/postgresql/data
  /container/add remote-image=postgres:15 interface=veth2 root-dir=disk1/images/postgres2 mountlists=MOUNT_POSTGRES2 envlist=ENV_POSTGRES2 name=postgres2 start-on-boot=yes logging=yes
  ```

- 第一个和第二个 Web 应用程序容器配置。

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin1 name=pgadmin1 start-on-boot=yes logging=yes
  ```

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth2 root-dir=disk1/images/pgadmin2 name=pgadmin2 start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin1` 能够访问 `postgres1`，但无法访问 `postgres2`。同样，`pgadmin2` 能够访问 `postgres2`，但无法访问 `postgres1`。

#### 二层网络中的容器

在此网络设置中，您的容器直接连接到与其他物理网络设备相同的二层网络。此网络设置等同于其他容器引擎（如 Docker）上的“主机”网络模式。

:::danger
在此网络设置中，容器上的所有端口都是暴露的。这被认为是不安全的，但确实略微提高了容器的网络性能。
:::

- 网络配置。

  ```routeros
  /interface/veth/add name=veth1 address=192.168.88.2/24 gateway=192.168.88.1
  /interface/bridge/port/add bridge=bridge interface=veth1
  ```

- 如果您的 RouterOS 设备在同一端口上运行服务，您需要禁用它们。

  ```routeros
  /ip/service/disable [find where name=www]
  ```

- Web 应用程序配置。

  ```routeros
  /container/add remote-image=dpage/pgadmin4 interface=veth1 root-dir=disk1/images/pgadmin name=pgadmin start-on-boot=yes logging=yes
  ```

在此示例中，`pgadmin` 容器不需要端口转发，但容器使用的所有其他端口现在对同一二层网络上的其他设备可访问。这种类型的设置只应在您的应用程序要求容器具有同一二层网络中的 IP 地址时使用，例如使用广播流量进行服务发现的应用程序（在大多数情况下，此类要求仍然可以通过使用 NAT 来绕过）。

### 容器的 IPv4 和 IPv6

在此网络设置中，您的容器将能够通过 IPv4 和 IPv6 进行通信。该解决方案基于 [带 NAT 的桥接](./index.md#bridge-with-nat) 网络设置。

- 网络配置。

  ```routeros
  /ip/address
  add address=172.17.0.1/24 interface=containers
  /ip/firewall/nat
  add action=masquerade chain=srcnat src-address=172.17.0.0/24
  add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=80 protocol=tcp to-addresses=172.17.0.2 to-ports=80
  /ipv6/address
  add address=fd8d:5ad2:24:2::1 interface=containers
  /ipv6/firewall/nat
  add action=masquerade chain=srcnat src-address=fd8d:5ad2:24:2::/64
  add action=dst-nat chain=dstnat dst-address=fd8d:5ad2:24:2::1 dst-port=80 protocol=tcp to-addresses=fd8d:5ad2:24:2::2 to-ports=80
  /interface/veth
  add address=172.17.0.2/24,fd8d:5ad2:24:2::2/64 gateway=172.17.0.1 gateway6=fd8d:5ad2:24:2::1 name=veth1
  /interface/bridge/port/add bridge=containers interface=veth1
  ```

- Web 应用程序容器配置。

  ```routeros
  /container/add remote-image=nginx interface=veth1 root-dir=disk1/images/nginx name=nginx start-on-boot=yes logging=yes
  ```

## 健康检查

从 RouterOS 7.23 开始，RouterOS 中已实现健康检查支持。
健康检查是一种有助于验证容器内应用程序是否正常运行（healthy）的机制。

健康检查依赖于标准的退出代码。用于健康检查的命令应在应用程序健康时返回 0，在不健康时返回非零退出代码。

在大多数情况下，对于运行 Web 界面的容器，向 localhost 发送一个简单的 HTTP GET 请求就足以验证应用程序是否正常响应。

| 属性 | 描述 |
| :-- | :-- |
| **healthcheck-cmd** (*字符串*; *默认值*:)| 用于健康检查的命令 |
| **healthcheck-interval** (*时间*; *默认值*: 00:00:30)| 时间间隔，格式为 HH:MM:SS |
| **healthcheck-retries** (*整数*; *默认值*: 3)| 在检查失败的情况下 - 在容器应用程序被视为不健康之前的重试次数 |
| **healthcheck-start-interval** (*时间*; *默认值*: 00:00:05)| 启动期间健康检查之间的时间 |
| **healthcheck-start-period** (*时间*; *默认值*: 00:00:00) | 为容器启动提供时间。启动期间内的任何失败都不会计入重试计数器 |
| **healthcheck-status** (*字符串*)| 容器的当前健康状态。显示容器内应用程序的当前状态以及探测输出 |
| **healthcheck-timeout** (*时间*; *默认值*: 00:00:30)| 如果健康检查探测时间超过指定时间，则该检查将被视为失败 |

### 健康检查示例

在此示例中，我们将设置一个 HomeAssistant 容器并为其配置一个简单的健康检查。

有关设置 HomeAssistant 容器的指南，请参阅我们的 [HomeAssistant 设置指南](./user-guides/container-homeassistant.md)

要设置电子邮件工具，请参阅我们的 [电子邮件文档页面](../system-information-and-utilities/e-mail.md)

1. 检查您的容器名称

    ```ros
    [admin@ROSE] > container print 
    Flags: S - STOPPED, R - RUNNING
    Columns: NAME, ROOT-DIR, INTERFACE, MEMORY-CURRENT, CPU-USAGE, CONTAINER-SIZE, DATA-SIZE, TAG
    #   NAME                ROOT-DIR                                        INTERFACE                MEMORY-CURRENT  CPU-USAGE  CONTAINER-SIZE  DATA-SIZE  TAG                                                                   
    1 S home-assistant  /nvme1/apps/home-assistant/home-assistant_root  veth-home-assistant                          0  2201.9MiB       471.9KiB   docker.io/homeassistant/home-assistant:latest
    ```

2. 创建容器后，我们可以通过设置健康检查命令来启用健康检查。对于这个特定的容器，我们可以增加 healthcheck-interval 并指定一个 start-period，因为 HomeAssistant 是一个重量级容器，在某些设备上可能启动较慢。

    ```ros
    /container/set home-assistant healthcheck-cmd="curl -f http://localhost:8123" healthcheck-interval="00:01:00" healthcheck-start-period="00:02:00"
    ```

    如果成功且容器启动 - 您应该看到容器以“Healthy”状态运行。
    此外，healthcheck-status 字段会填充容器的当前状态以及 curl 命令的输出。

    ```ros
    [admin@ROSE] > container print proplist=name,healthcheck-status
    Flags: S - STOPPED, R - RUNNING, H - HEALTHY
    Columns: NAME, HEALTHCHECK-STATUS
   