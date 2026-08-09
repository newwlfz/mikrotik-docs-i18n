# 文件共享

> 文件共享功能使 MikroTik 路由器能够通过 HTTPS 安全地提供互联网可访问的存储服务，允许将 USB/NVME 驱动器共享给外部用户，并支持可选的文件上传功能，同时使用自动生成的域名和证书。

# 文件共享

文件共享功能允许您使用路由器的外部存储设备，与互联网上的任何人共享文件。只需将 USB、nVME 或任何受支持的驱动器连接到您的设备，然后将整个目录路径添加到文件共享菜单中。路由器将使用 MikroTik 云服务为您的路由器签发 HTTPS 证书和域名。您可以分发给任何人的 URL 将显示在文件共享菜单中。您还可以启用允许任何人向您的路由器上传文件的功能。URL 是随机生成的，因此虽然任何知道链接的人都可以访问，但如果您妥善保管，只有拥有链接的人才能使用它。

### 添加共享

首先，连接您的 USB 驱动器并确定要共享的目录的文件路径：

```shell
[user@RouterOS] > /file/print
 # NAME                                                                           TYPE             SIZE LAST-MODIFIED
 0 web                                                                            directory             2025-01-23 09:29:42
 1 usb1                                                                           disk                  2025-01-22 09:45:57
 2 pub                                                                            directory             2025-01-23 09:24:41
 3 skins                                                                          directory             2024-12-10 08:19:27
 4 pub/index.html                                                                 .html file        670 2025-01-23 09:24:41
 5 skins/default.json                                                             .json file        151 2024-07-15 10:20:11
 6 usb1/Secret Files                                                        	  directory             2024-03-18 09:01:41
 7 usb1/forum                                                                     directory             2025-01-22 10:58:20
 8 usb1/Secret Files/Home Video.srt                 							                .srt file         267 2020-06-01 11:29:14
 9 usb1/Secret Files/Home Video.mp4                 							                .mp4 file   1584.4MiB 2020-06-01 11:34:33
10 usb1/forum/cat.jpeg                                                            .jpeg file  4307.7KiB 2025-01-22 09:38:55
11 usb1/forum/cat1.jpeg                                                           .jpeg file   231.8KiB 2025-01-22 10:58:20
12 usb1/forum/cat2.jpeg                                                           .jpeg file   129.6KiB 2025-01-22 10:58:20
13 usb1/forum/cat3.jpeg                                                           .jpeg file   263.8KiB 2025-01-22 10:58:20
14 usb1/forum/cat4.jpeg                                                           .jpeg file   438.4KiB 2025-01-22 10:58:20
15 web/index.html                                                                 .html file       1473 2025-01-23 09:29:42
```

导航至 `/ip/cloud/back-to-home-file`。共享**目录**时，您必须指定**路径**和**过期日期**，并且还可以授予**上传权限**。共享**文件**时，只需**路径**和**过期日期**即可。

```shell
[user@RouterOS] /ip/cloud/back-to-home-file> add path="usb1/Secret Files/" expires=never allow-uploads=yes
[user@RouterOS] /ip/cloud/back-to-home-file> add path="usb1/Secret Files/Home Video.mp4" expires=never
[user@RouterOS] /ip/cloud/back-to-home-file> print
Columns: PATH, URL, DIRECT-URL, EXPIRES, DOWNLOADS
# PATH                      URL                                                        DIRECT-URL                                                    EXPIRES  DOWNLOADS
0 /usb1/Secret Files  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp  https://acf017skgys.routingthecloud.net/s/4MPgHbEZCZYGVtp?dl        never            5
1 /usb1/Secret Files/Home Video.mp4      https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0  https://acf017skgys.routingthecloud.net/s/K8zkh1UjKuqtEQ0?dl         never            2
[user@RouterOS] /ip/cloud/back-to-home-file>
```

现在，如果您复制“URL”，您可以将其分享给其他人，无论他们身在何处，也无论您的路由器是否具有公网 IP。

当您将 URL 发送给朋友时，他们可以看到共享目录中的所有文件并下载。如果您在创建共享时启用了上传功能，他们还可以向您的路由器上传文件。请妥善保管此 URL，或指定“过期”日期以避免其他人访问这些文件。

![](https://manual.mikrotik.com/docs/network-management/cloud/img/file-share_01.png)

| 属性 | 描述 |
| :-- | :-- |
| **enable** (默认) | 启用文件共享功能。添加第一个共享时，文件共享服务将被激活。如果没有共享，文件共享服务将保持禁用状态。 |
| **disabled** (*yes \| no;* 默认: **no**) | 禁用文件共享功能。 |
| **allow-uploads** (*yes \| no;* 默认: **no**) | 启用允许任何人向您的路由器上传文件的选项。 |
| **expires** (默认: **never**) | 共享过期日期。格式：ISO 8601 (2025-01-25 00:00:00) 示例：`/ip/cloud/back-to-home-file/set` 0 expires="2025-01-25 07:15:00" |
| **path** | 设置要共享的文件的路径。示例："/ip/cloud/back-to-home-file/add path=mypath/myfile" |

### WinBox 图形界面

要共享文件，请访问 IP → Cloud “配置”部分下的“文件共享”菜单。

![](https://manual.mikrotik.com/docs/network-management/cloud/img/file-share_02.png)

要创建新的共享，请设置“路径”、“过期时间”和“自动上传”选项。

![](https://manual.mikrotik.com/docs/network-management/cloud/img/file-share_03.png)

```ros
[admin@MikroTik] > /ip/cloud/back-to-home-file/print detail 
Flags: X - disabled; I - invalid 
 0    path=/mypath/myfile allow-uploads=no expires=2025-01-25 07:15:00 key="*********" 
      url="https://*********.routingthecloud.net/s/*********" direct-url="https://*********.routingthecloud.net/s/*********" 
      downloads=0
```

:::info
安全警告

URL 是随机生成的，因此虽然任何知道链接的人都可以访问，但如果您妥善保管，只有拥有链接的人才能使用它。
:::

文件共享使用 HTTPS（TCP 端口 443），但如果您手动配置了 WebFig 也使用 HTTPS，则文件共享将自动仅通过我们的云中继服务工作，因为同一设备上不能有两个东西使用同一端口。默认情况下，www-ssl 未启用，因此文件共享默认直接工作，无需使用中继进行下载。启用文件共享不会以任何方式影响您的 WebFig 配置，也不会将其暴露给外部网络。

对于文件共享功能，当用户想要与某人共享文件时，如果您的路由器可以直接从互联网访问（由中继服务器检查），操作顺序如下：

- 路由器本地生成私钥和证书。
- 证书签名在路由器上使用标准 ACME 协议执行（使用 LetsEncrypt 后端的 DNS-01 挑战）。
- DNS-01 挑战通过临时添加 DNS TXT 记录（标准流程）发送到 MikroTik 云 DNS 服务器。
- DNS 名称解析到路由器。
- 使用私有证书打开安全的 443 端口。

### 中继服务

如果设备无法直接从互联网访问，它将选择使用 MikroTik 托管的中继服务。

- 路由器检查其从互联网的可达性。
- 如果需要中继连接，则 DNS 更新为中继 IP。
- 路由器根据延迟选择最近的中继。
- 如果路由器使用中继，则与中继保持连接打开。yyyyyy.routingthecloud.net 解析到中继。当客户端通过中继建立连接时，会解析 TLS Client Hello 以获取目标路由器，然后将整个 HTTPS 请求直接转发到路由器。
- 中继无法解密您的数据，因为带有私钥的证书仅存在于路由器上。