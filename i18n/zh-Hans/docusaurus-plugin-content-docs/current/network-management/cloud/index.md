# Cloud

> MikroTik Cloud 部分提供了 Back To Home、DDNS、文件共享及其他云辅助服务的配置说明，包括启用/禁用 DDNS、触发更新以及管理用于远程访问的 IP 地址的详细指南。

import DocCardList from '@theme/DocCardList';

# Cloud

本节涵盖 MikroTik Cloud 功能。使用它来配置 Back To Home、Cloud 通信、文件共享及其他云辅助服务。

<DocCardList />

MikroTik 为连接到互联网的 RouterBOARD 设备提供多种服务。这些服务旨在简化配置、设置、控制、维护或监控设备时的不便。IP/Cloud 可提供的可用服务详细列表如下。

## 服务

:::danger
请注意，如果路由器有多个公网 IP 地址和/或多个互联网网关，用于与 MikroTik Cloud 服务器通信的确切 IP 可能并非预期！

**警告：** IP/Cloud 需要 Cloud Hosted Router (CHR) 的付费永久许可证。

**警告：** x86 系统不支持云服务。
:::

### DDNS

DDNS 或动态域名系统是一种定期更新 A 记录的 IPv4 地址和 AAAA 记录的 IPv6 地址的服务。当您的 ISP 提供了定期变化的动态 IP 地址，但您始终需要一个可用于远程连接设备的地址时，此类服务非常有用。以下是与 IP/Cloud 的 DDNS 服务相关的操作细节：

- 检查出站 IP 地址变化：每 60 秒一次。
- 等待 MikroTik Cloud 服务器响应：15 秒。
- DDNS 记录 TTL：60 秒。
- 使用 UDP 端口 15252 向 **cloud2.mikrotik.com** 发送加密数据包。

自 RouterOS v6.43 起，如果您的设备能够通过 IPv6 访问 **cloud2.mikrotik.com**，则会为您的公网 IPv6 地址创建 DNS **AAAA** 记录。如果您的设备只能通过 IPv4 访问 cloud2.mikrotik.com，则只会为您的公网 IPv4 地址创建 DNS **A** 记录。cloud.mikrotik.com 用于 6.44 之前的旧版 RouterOS。

启用 DDNS 服务：

```ros
[admin@MikroTik] /ip/cloud/set ddns-enabled=yes
[admin@MikroTik] /ip/cloud/print
         ddns-enabled: yes
 ddns-update-interval: none
          update-time: yes
       public-address: 159.148.147.196
  public-address-ipv6: 2a02:610:7501:1000::2
             dns-name: 529c0491d41c.sn.mynetname.net
               status: updated
```

:::warning
启用该服务后，DNS 名称将永久存储在 MikroTik Cloud 服务器上，该 DNS 名称将解析为您 RouterOS 实例发送到 MikroTik Cloud 服务器的最后一个 IP。
:::

禁用 DDNS 服务：

```ros
/ip/cloud/set ddns-enabled=auto
```

:::warning
在 7.17 之前，ddns-enabled 的默认值为 "no"。在包含 7.17 及更高版本的版本中，如果您想禁用 DDNS，请确保先禁用 [Back To Home](./back-to-home.md) 功能（如果已启用），然后设置 "ddns-enabled=auto"。

**警告：** 一旦您禁用该服务，您的设备会向 MikroTik Cloud 服务器发送命令以删除存储的 DNS 名称。
:::

手动触发 DNS 更新：

```ros
[admin@MikroTik] > /ip/cloud/force-update
```

:::warning
要实际使用云服务器提供的 DNS 名称连接到设备，用户必须配置路由器的防火墙以允许从 WAN 端口进行此类访问。（默认的 MikroTik 配置不允许从 WAN 端口访问 WebFig、WinBox 等服务）。
:::

### 更新时间

设备上正确的时间很重要，时间错误会导致系统日志问题、HTTPS 连接中断、隧道连接中断及其他问题。要更新系统时钟，您可以使用 [NTP](../../system-information-and-utilities/ntp.md) 或 [SNTP](../../system-information-and-utilities/ntp.md)，但这需要您指定 NTP 服务器的 IP 地址。在大多数情况下，仅为了在设备上设置正确时间并不需要 NTP/SNTP，为简便起见，您可以使用 IP Cloud 的更新时间服务。以下是与 IP/Cloud 的更新时间服务相关的操作细节：

- 近似时间（精度为几秒，取决于 UDP 数据包延迟）。
- 重启后及每次 DDNS 更新时更新时间（当路由器的 WAN IP 地址变化或使用 force-update 命令后）。
- 使用 UDP/15252 端口向 **cloud2.mikrotik.com** 发送加密数据包。
- 根据路由器的公网 IP 地址和我们的商业数据库检测时区。

启用时间更新服务：

```ros
[admin@MikroTik] > /ip/cloud/set update-time=yes 
```

启用自动时区检测：

```ros
[admin@MikroTik] > /system/clock/set time-zone-autodetect=yes 
```

:::warning
如果 `/ip/cloud/update-time` 设置为 `auto`，则设备时钟将使用 MikroTik Cloud 服务器时间进行更新（如果未启用 [NTP](../../system-information-and-utilities/ntp.md) 或 [SNTP](../../system-information-and-utilities/ntp.md) 客户端）。
:::

### 备份

可以将设备的 [备份](../../getting-started/configuration-management/backup.md) 存储在 MikroTik Cloud 服务器上。备份服务允许您上传加密的备份文件、下载并将备份文件应用到您的设备，只要您的设备能够访问 MikroTik Cloud 服务器。以下是与 IP/Cloud 的备份服务相关的操作细节：

- 每台设备 1 个免费备份槽位。
- 允许的备份大小：15MB。
- 使用 UDP/15252 和 TCP/15252 端口向 **cloud2.mikrotik.com** 发送加密数据包。

创建新备份并上传到 MikroTik Cloud 服务器：

```ros
[admin@MikroTik] > /system/backup/cloud/upload-file action=create-and-upload password=test123!!!
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-162649" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:26:49 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890" 
```

:::warning
`create-and-upload` 操作命令将创建新的系统备份文件，使用提供的密码通过 AES 加密备份文件并上传。对于 `upload` 操作命令，password 属性无效，因为 `upload` 操作命令仅上传已创建的系统备份文件。
:::

下载已上传的备份文件并保存到设备内存：

```ros
[admin@MikroTik] > /system/backup/cloud/download-file action=download number=0
### 或
[admin@MikroTik] > /system/backup/cloud/download-file action=download secret-download-key=AbCdEfGhIjKlM1234567890
```

:::warning
**警告：** secret-download-key 是唯一标识符，可用于将加密备份下载到其他设备。由于您可以使用 secret-download-key 从任何位置和任何设备下载加密备份，因此应尽量保密此标识符。下载的备份仍使用 AES 加密；但请确保使用强密码！
:::

删除已上传的备份：

```ros
/system/backup/cloud/remove-file number=0
```

用新的备份文件替换现有文件，使用以下命令：

```ros
/system/backup/cloud/upload-file action=create-and-upload replace=_您之前创建的备份文件_ password=test123!!!
```

上传现有备份文件（之前创建的）：

```ros
[admin@MikroTik] > /system/backup/save encryption=aes-sha256 name=old_backup password=test123!!!
[admin@MikroTik] > /system/backup/cloud/upload-file action=upload src-file=old_backup.backup
[admin@MikroTik] > /system/backup/cloud/print 
 0 name="cloud-20180921-164044" size=13.2KiB ros-version="6.44beta9" date=2018-09-21 16:40:44 status="ok" secret-download-key="AbCdEfGhIjKlM1234567890"
```

:::warning
确保备份使用 AES 加密，否则 IP/Cloud 将拒绝备份上传。由于每台设备只有 1 个免费备份槽位，上传新备份前需要删除现有备份。
:::

### Back to Home

有关 Back to Home (BTH) 服务的更多信息，请参阅单独的 [文档页面](./back-to-home.md)。

### 文件共享

有关文件共享服务的更多信息，请参阅单独的 [文档页面](./file-share.md)。

### 中继服务

Back to Home 和文件共享均部分依赖 MikroTik 云中继服务。通过中继服务的所有传输均为端到端加密，中继纯粹用于促进连接，设计上无需解密用户数据或元数据。有关每个服务如何使用中继的详细信息，请参阅相应手册。

## 属性

**子菜单：** `/ip/cloud`

| 属性 | 描述 |
| :-- | :-- |
| **ddns-enabled** (*yes \| auto*; 默认值：**auto**) | 如果设置为 `yes`，设备将向 MikroTik Cloud 服务器发送加密消息。服务器将解密消息并验证发送方是否为真实的 MikroTik 设备。如果一切正常，MikroTik Cloud 服务器将为此设备创建 DDNS 记录并向设备发送响应。路由器上的 IP/Cloud 服务每分钟检查 WAN IP 地址是否与发送到 MikroTik Cloud 服务器的地址匹配，如果 IP 地址变化则向云服务器发送加密更新。如果设置为 auto，则仅当 [Back To Home](./back-to-home) 启用时 DDNS 才会启用。**重要：** 在 7.17 版本之前，默认值为 "no"。 |
| **ddns-update-interval** (*时间，最小 60 秒*; 默认值：**none**) | 如果设置，DDNS 将按设定间隔尝试连接 IP Cloud 服务器。如果设置为 **none**，将继续在内部检查 IP 地址更新并根据需要连接 IP Cloud 服务器。当使用的 IP 地址不在路由器本身时很有用，因为无法在路由器内部检查该值。 |
| **update-time** (*yes \| no*; 默认值：**yes**) | 如果设置为 `yes`，则路由器时钟将设置为云服务器提供的时间 **如果** 未启用 [NTP](../../system-information-and-utilities/ntp) 或 [SNTP](../../system-information-and-utilities/ntp) 客户端。如果设置为 `no`，则 IP/Cloud 服务将永远不会更新设备时钟。如果 update-time 设置为 `yes`，即使 ddns-enabled 设置为 auto，时钟也会更新。 |
| **public-address** (*只读：地址*) | 显示发送到云服务器的设备 IPv4 地址。此字段仅在至少一次 IP Cloud 请求成功完成后可见。 |
| **public-address-ipv6** (*只读：地址*) | 显示发送到云服务器的设备 IPv6 地址。此字段仅在至少一次 IP Cloud 请求成功完成后可见。 |
| **warning** (*只读：字符串*) | 如果设备发送的 IP 地址与 MikroTik Cloud 服务器在 UDP 数据包头中看到的 IP 地址不同，则显示警告消息。通常发生在设备位于 NAT 后面时。示例："DDNS server received a request from IP `123.123.123.123` but your local IP was `192.168.88.23`; DDNS service might not work" |
| **dns-name** (*只读：名称*) | 显示分配给设备的 DNS 名称。名称由 12 个字符的序列号后跟 *.sn.mynetname.net* 组成。此字段仅在至少一次 ddns-request 成功完成后可见。 |
| **status** (*只读：字符串*) | 包含描述当前 dns-service 状态的文本字符串。消息不言自明：updating...updatedError: no Internet connectionError: request timed outError: REJECTED. Contact MikroTik supportError: internal error - should not happen. One possible cause is if the router runs out of memory |

### 高级

**子菜单：** `/ip/cloud/advanced`

| 属性 | 描述 |
| :-- | :-- |
| **use-local-address** (*yes \| no*; 默认值：**no**) | 默认情况下，DNS 名称将分配给检测到的公网地址（来自 UDP 数据包头）。如果您希望发送"本地"或"内部"IP 地址，则将此设置为 `yes`。 |

### 云备份

**子菜单：** `/system/backup/cloud`

以下是与特定命令相关的命令和属性，其他属性将不会生效：

- download-file

| 属性 | 描述 |
| :-- | :-- |
| **action** (*download*) | 从 MikroTik Cloud 服务器下载已上传的备份文件。 |
| **number** (*整数*) | 指定 MikroTik Cloud 服务器上的备份槽位。免费备份槽位始终位于 `0th` 槽位。 |
| **secret-download-key** (*字符串*) | 可用于下载已上传备份文件的唯一标识符。下载已上传的备份文件时，您不必使用上传备份的同一设备。在部署备份到新设备时非常有用。 |

- remove-file

| 属性 | 描述 |
| :-- | :-- |
| **number** (*整数*) | 删除指定备份槽位中的备份文件。免费备份槽位始终位于 `0th` 槽位。 |

- upload-file

| 属性 | 描述 |
| :-- | :-- |
| **action** (*create-and-upload*) | 将备份文件上传到 MikroTik Cloud 服务器。<code>create-and-upload</code> - 使用指定密码创建新备份文件并上传<code>upload</code> - 上传已创建的系统备份文件。 |
| **name** (*字符串*) | 指定将显示在上传备份列表中的备份名称。这**不是**源备份的名称，此名称仅用于视觉表示。 |
| **src-file** (*文件*) | 使用 `/system/backup` 创建的备份文件名以上传。此属性仅在 action 设置为 `upload` 时生效。 |
| **password** (*字符串*) | 使用指定密码创建、加密并上传备份文件。此属性仅在 action 设置为 `create-and-upload` 时生效。 |