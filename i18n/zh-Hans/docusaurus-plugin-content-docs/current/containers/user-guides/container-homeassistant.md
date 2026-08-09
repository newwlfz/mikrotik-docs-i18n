# 容器 - HomeAssistant

> 本页介绍 MikroTik RouterOS 中的容器功能，使用户能够直接在路由器上运行 HomeAssistant 等服务器。文中提供了启用容器模式、配置网络、设置挂载与环境变量以及获取 HomeAssistant Docker 镜像的分步说明。

# 容器 - HomeAssistant

RouterOS 中引入的 **容器** 功能，使得直接在路由器上运行各种服务器成为可能。这对于希望尽量减少网络中设备数量的用户尤其有价值。无需在独立机器上部署服务器，您现在可以直接将其托管在路由器内部。

在本指南中，我们将演示如何在 RouterOS 上安装并运行 **Home‑Assistant** 服务器。

Home‑Assistant 是一个流行的平台，用于收集来自众多传感器的数据，并广泛支持各种 **集成**。

## 摘要

在继续配置之前，请确保您已阅读我们的 [容器](../) 指南。此外，请查阅 [免责声明](../#disclaimer) 和 [要求](../#requirements) 部分，以了解所有相关风险以及您可能需要采取的必要步骤。

您可以在 [链接](https://hub.docker.com/r/homeassistant/home-assistant/tags) 中找到支持的架构。

在本指南发布时，**home-assistant** 镜像可用于 ARM64 和 AMD64（CHR 和 x86）设备。

根据 [Home Assistant 网站](https://www.home-assistant.io/installation/linux/) 的信息，推荐的要求如下：

- 2 GB 内存
- 32 GB 存储空间

但我们将尝试在较低规格的设备上运行它。

## 容器配置

**子菜单：** `/container`

***注意***：需要 **container** 软件包。

### 容器模式

启用容器模式：

```ros
/system/device-mode/update container=yes
```

您需要按下重置按钮确认设备模式，或者如果在 X86 上使用容器，则需进行冷重启。

### 网络配置

添加 veth 接口：

```ros
/interface/veth/add name=veth2 address=172.19.0.2/24 gateway=172.19.0.1
```

为容器创建桥接，并将 veth 接口添加到其中：

```ros
/interface/bridge/add name=ha
/ip/address/add address=172.19.0.1/24 interface=ha
/interface/bridge/port/add bridge=ha interface=veth2
```

如果需要 NAT，则转发 TCP 8123 端口用于 home-assistant 管理（其中 192.168.88.1 是设备的局域网 IP 地址）（可选）：

```ros
/ip/firewall/nat/add action=dst-nat chain=dstnat dst-address=192.168.88.1 dst-port=8123 protocol=tcp to-addresses=172.19.0.2 to-ports=8123
```

### 环境变量与挂载

根据 home-assistant 文档，为配置文件定义挂载（其中 `/usb1` 是我们的外部 USB 存储文件夹）：

```ros
/container/mounts/add dst=/config list=ha_config src=/usb1/ha_config
```

为 home-assistant 创建环境变量：

```ros
/container/envs/add key=TZ list=ha_env value=America/Los_Angeles
```

### 获取镜像

为简化配置，我们将从外部库获取镜像。

确保已正确设置“Registry URL”，限制内存使用（如有必要），并为镜像设置目录：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=/usb1/pull
```

拉取 home-assistant 镜像并等待其解压：

```ros
/container/add remote-image=homeassistant/home-assistant:latest interface=veth2 root-dir=/usb1/ha mountlists=ha_config envlists=ha_env logging=yes
```

运行命令后，RouterOS 应开始“解压”软件包。检查“文件系统”中新建的文件夹，并使用命令 `/container/print` 监控容器状态。

### 启动容器

在确保容器已添加且使用 `/container/print` 后状态已变为 `status=stopped` 后，您可以启动它：

```ros
/container/start 0
```

### Home-Assistant 设置

打开您首选的网页浏览器，通过指定管理端口“:8123”访问 Home-Assistant 管理门户：

![](https://manual.mikrotik.com/docs/containers/user-guides/img/container-homeassistant-01.webp)

继续进行设置。更多信息请参阅 [Home-Assistant 入门指南](https://www.home-assistant.io/getting-started/onboarding/)。

## 资源

仅运行 **Home Assistant**（无任何负载/流量）大约占用 300-400 MB 内存：

```ros
/system/resource/print
                   uptime: 4m27s
                  version: 7.13.3 (stable)
               build-time: 2024-01-24 13:16:46
         factory-software: 7.10
              free-memory: 143.0MiB
             total-memory: 448.0MiB
```