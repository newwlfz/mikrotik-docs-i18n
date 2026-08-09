# 备份

> RouterOS 备份功能支持保存和恢复路由器配置（包括 MAC 地址），并提供加密或非加密存储选项。它支持将备份保存到文件，并重新加载到同一设备上，同时会提示版本兼容性和敏感数据处理相关警告。

# 备份

RouterOS 备份功能允许以二进制格式文件保存路由器配置，该文件随后可重新应用于同一设备。系统备份文件还包含设备的 MAC 地址，加载备份文件时会一并恢复。

我们建议在相同版本的 RouterOS 上恢复备份。

:::danger
如果路由器上安装了 The Dude 或 User-manager，则系统备份不会包含这些服务的配置，因此需要额外注意保存这些服务的配置。如果您想保存配置，请使用提供的工具机制来保存/导出配置。

**警告：** 系统备份包含有关您设备及其配置的敏感信息；请始终考虑加密备份文件，并将其存放在安全位置。
:::

## 保存备份

**子菜单：** `/system/backup/save`

| 属性 | 描述 |
| :-- | :-- |
| **dont-encrypt** (*yes \| no*；默认值：**no**) | 禁用备份文件加密。请注意，自 RouterOS v6.43 起，若未提供密码，备份文件将不加密。 |
| **encryption** (*aes-sha256 \| rc4*；默认值：**aes-sha256**) | 用于加密备份文件的加密算法。请注意，`rc4` 不被视为安全的加密方法，仅出于与旧版 RouterOS 的兼容性考虑而提供。 |
| **name** (*字符串*；默认值：**[identity]-[date]-[time].backup**) | 备份文件的文件名。 |
| **password** (*字符串*；默认值：) *[敏感参数](./list-of-menus-with-sensitive-parameters.md)* | 加密备份文件的密码。请注意，自 RouterOS v6.43 起，若未提供密码，备份文件将不加密。 |

:::danger
在早于 v6.43 的 RouterOS 版本中，如果未提供密码，则备份文件将使用当前用户的密码进行加密，除非使用了 *dont-encrypt* 属性或当前用户的密码为空。
:::

备份文件将在 `/file` 菜单下可用，可通过 FTP 或 Winbox 下载。

## 加载备份

无密码加载备份：

```ros
[admin@MikroTik] > /system/backup/load name=auto-before-reset.backup password=""
```

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串*；默认值：) | 备份文件的文件名。 |
| **password** (*字符串*；默认值：) *[敏感参数](./list-of-menus-with-sensitive-parameters.md)* | 加密备份文件的密码。 |

## 示例

将路由器配置保存到文件 test 并设置密码：

```ros
[admin@MikroTik] > /system/backup/save name=test password=<YOUR_PASSWORD> 
Configuration backup saved 
```

查看路由器上存储的文件：

```ros
[admin@MikroTik] > /file/print 
# NAME TYPE SIZE CREATION-TIME 
0 test.backup backup 12567 2018-09-08 21:07:50 
[admin@MikroTik] >
```

加载已保存的备份文件 test：

```ros
[admin@MikroTik] > /system/backup/load name=test 
password: <YOUR_PASSWORD> 
Restore and reboot? [y/N]: y 
Restoring system configuration 
System configuration restored, rebooting now
```

## 云备份

自 RouterOS v6.44 起，可以将设备的备份文件安全地存储在 MikroTik 的云服务器上。有关此功能的更多信息，请参阅 [IP/Cloud](../../network-management/cloud/index.md) 页面。