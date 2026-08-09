# SMB

> RouterOS 内置了 **SMB 服务器**，用于通过 SMB/CIFS 协议共享路由器文件夹。此外，[ROSE 软件包](./index.md) 增加了 **SMB 客户端**，使 RouterOS 能够将远程 SMB 共享挂载为磁盘。

## SMB 服务器

**子菜单：** `/ip/smb` **所需软件包：** `system`

SMB 服务器提供对路由器已配置文件夹的文件共享访问，允许网络客户端通过 SMB/CIFS 协议浏览、读取、写入和管理存储在路由器存储介质上的文件。这使得路由器能够充当简单的网络附加存储（NAS）设备，用于在本地网络中共享文件、备份数据或路由器配置备份文件。

:::warning
RouterOS 仅支持 SMB2.1、SMB3.0 和 SMB3.1.1。由于安全漏洞，不支持 SMB1。

**注意：** SMIPS 设备不支持 SMB。
:::

### 服务器设置

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*；默认值：**MikrotikSMB**) | 为服务器设置注释 |
| **domain** (*字符串*；默认值：**MSHOME**) | Windows 工作组名称 |
| **enabled** (*yes \| no \| auto* 默认值：**auto**) | 默认值为“auto”。这意味着当在 `/ip/smb/share` 下配置第一个非禁用 SMB 共享时，SMB 服务器将自动启用 |
| **interface** (*字符串*；默认值：**all**) | SMB 服务将运行的接口列表。all - SMB 将在所有接口上可用。 |

:::warning
从版本 7.14 开始，“allow-guest”选项已被 `/ip/smb/users` 中的默认访客用户所取代。现在可以在本节中禁用或启用此默认访客用户。
:::

### 共享设置

**子菜单：** `/ip/smb/shares`

允许配置 SMB 可访问的共享名称和目录。

如果配置中提供的目录不存在，将自动创建。

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*；默认值：**default share**) | 为共享设置注释 |
| **disabled** (*yes \| no*；默认值：**no**) | 如果禁用，共享将不可访问。 |
| **valid-users**（*字符串*列表；\| 默认值：） | 指定允许访问 Samba 共享的用户。如果留空，所有用户都将能够访问该共享。一旦在此处定义了一个或多个用户，则只有他们能够访问该共享 |
| **invalid-users**（*字符串*列表；\| 默认值：） | 用于指定被明确拒绝访问 Samba 共享的用户。 |
| **require-encryption** (*yes*\| *no*；默认值：***no***) | 强制对特定 Samba 共享的所有连接使用加密。建议将其更改为“Yes”以确保与 macOS 客户端更好的稳定性。 |
| **name** (*字符串*；默认值：) | SMB 共享的名称 |
| **directory** (*字符串*；默认值：) | 分配给 SMB 共享的路由器上的目录。如果留空，将使用根文件夹中 *name* 参数的值。 |

### 用户设置

**子菜单：** `/ip/smb/users`

设置可以访问路由器 SMB 共享的用户。

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*；默认值：) | 为用户设置描述 |
| **disabled** (*yes \| no*；默认值：**no**) | 定义用户是启用还是禁用 |
| **name** (*字符串*；默认值：) | SMB 服务用户的登录名 |
| **password** (*字符串*；默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SMB 用户连接到 SMB 服务的密码 |
| **read-only** (*yes \| no*；默认值：**yes**) | 设置用户访问共享时仅具有只读权限还是完全访问权限。 |

### 示例

要使 RouterOS 文件夹可通过 SMB 服务使用，请执行以下步骤：

- 创建用户。

```ros
/ip/smb/users/add read-only=no name=mtuser password=mtpasswd
```

- 添加共享文件夹。

```ros
/ip/smb/shares/add directory=backup name=backup
```

- 启用 SMB 服务：

```ros
# 此步骤为可选，因为默认值为“enabled=auto”
/ip/smb/set enabled=yes
```

现在检查结果：

- 检查常规服务设置。

```ros
/ip/smb/print
      enabled: yes
       domain: MSHOME
      comment: MikrotikSMB
   interfaces: all
```

- SMB 用户设置

```ros
/ip/smb/users/print
Flags: X - DISABLED; * - DEFAULT; r - READ-ONLY
Columns: NAME, PASSWORD
#     NAME    PASSWORD
0 X*r guest          
1     mtuser  mtpasswd
```

- 最后是 SMB 共享设置。

```ros
/ip/smb/shares/print
Flags: X - DISABLED; * - DEFAULT
Columns: NAME, DIRECTORY, REQUIRE-ENCRYPTION
#    NAME    DIRECTORY  REQUIRE-ENCRYPTION
;;; default share
0 X* pub     /pub       no               
1    backup  backup     no
```

现在，可以进行其他配置更改，例如禁用默认用户和共享等。

## SMB 客户端

**子菜单：** `/disk` **所需软件包：** [`rose-storage`](./index.md)

ROSE 软件包增加了 SMB 客户端，可将远程 SMB 共享挂载为路由器上的本地磁盘。ROS 软件包目前支持 SMB2.1、SMB3.0 和 SMB3.1.1 方言（由于安全漏洞，不支持 SMB1）。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **smb-address** | SMB 服务器的 IP 地址 |
| **smb-password***[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SMB 密码 |
| **smb-share** | 要连接的共享名称 |
| **smb-user** | SMB 用户 |

### 配置示例

客户端

```ros
add smb-address=10.155.145.11 smb-share=share1 smb-user=user smb-password=password type=smb
```