# DLNA 媒体服务器

> 本页介绍 MikroTik RouterOS 中的 DLNA 媒体服务器功能，说明其如何利用 UPnP 协议使网络设备能够共享数字媒体。文中详细介绍了服务器设置，如允许的主机、IP 限制和友好名称，并提供了配置多个实例并设置访问限制的示例。

# DLNA 媒体服务器

DLNA（数字生活网络联盟）是一组网络协议，使设备能够共享数字媒体，如视频、照片和音乐。DLNA 基于 UPnP（通用即插即用）架构构建，该架构提供设备发现和控制能力。

UPnP 允许设备在网络中相互发现并交换控制消息。它使用 SSDP（简单服务发现协议）进行发现，使用 SOAP（简单对象访问协议）进行控制消息，并使用 XML 描述设备和服务的详细信息。这使得电视、计算机和移动设备等设备能够无缝连接并共享媒体内容。

在 RouterOS 中，您可以启用媒体服务器，与家庭设备（如电视）或计算机上的播放器应用程序（如 VLC）共享电影或音乐。

:::danger
SMIPS 设备不支持媒体共享（DLNA）。
:::

## 服务器设置

| 属性 | 描述 |
| :-- | :-- |
| **allowed-hostname** | 用于限制对特定主机名的访问。 |
| **allowed-ip** | 用于限制对指定 IP 地址的访问。 |
| **friendly-name** | 网络上显示的 DLNA 服务器名称。 |
| **interface** | 指定 DLNA 服务器将使用的网络接口。 |
| **path** | 媒体内容存储并提供服务的文件路径。 |
| **disabled** | 指定条目是否已禁用。 |

### 创建 DLNA 服务器

要在 MikroTik 路由器上启用 DLNA 媒体流功能，请使用 `/ip media add` 命令。此命令配置一个媒体服务器，使网络上的 DLNA 兼容设备能够发现并访问存储在已连接 USB 存储设备上的媒体文件。将 `Mikrotik` 替换为您的媒体服务器的描述性名称，将 `bridge1` 替换为您要用于媒体发现的桥接接口，将 `usb1` 替换为媒体文件所在的 USB 存储路径。

```ros
/ip/media/add friendly-name=Mikrotik interface=bridge1 path=usb1
```

### 创建具有访问限制的多个 DLNA 服务器实例

此示例演示如何配置具有特定访问限制的独立 DLNA 服务器实例。使用场景：限制儿童电视仅访问存储在 "usb1/kids" 文件夹中的适合儿童的媒体内容。

```ros
/ip/media/add friendly-name=adults interface=bridge1 path=usb1/adults allowed-hostname=ADULTS_TV
/ip/media/add friendly-name=kids interface=bridge1 path=usb1/kids allowed-hostname=KIDS_TV
```