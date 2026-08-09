# 用户

> MikroTik RouterOS 用户管理页面详细介绍了通过本地或 RADIUS 服务器进行的用户认证、密码复杂度设置、定义访问权限的用户组策略，以及路由器用户数据库属性，包括登录地址、非活动操作和密码管理。

# 用户

## 概述

MikroTik RouterOS 路由器用户功能用于管理通过任何管理工具连接到路由器的用户。用户使用本地数据库或指定的 RADIUS 服务器进行认证。每个用户被分配到一个用户组，该用户组表示该用户的权限。组策略是各个策略项的组合。

如果用户认证通过 RADIUS 执行，则应事先配置 [RADIUS](./radius.md) 客户端。

## 用户设置

设置子菜单允许控制路由器用户的密码复杂度要求。

| 属性 | 说明 |
| :-- | :-- |
| **minimum-password-length** (*整数*; 0..4294967295; 默认值: ) | 指定用户密码的最小字符长度 |
| **minimum-categories** (*整数*; 0..4; 默认值: ) | 指定密码的复杂度要求，类别包括 *大写字母、小写字母、数字、符号*。 |

## 用户组

路由器用户组提供了一种便捷的方式，为不同的用户类别分配不同的权限和访问权限。

### 属性

| 属性 | 说明 |
| :-- | :-- |
| **name** (*字符串*; 默认值: ) | 用户组的名称 |
| **policy** (*local \| telnet \| ssh \| ftp \| reboot \| read \| write \| policy \| test \| winbox \| password \| web \| sniff \| sensitive \| api \| rest-api \| romon*; 默认值: **none**) | 允许的策略列表：  登录策略： local - 授予通过控制台本地登录权限的策 略telnet - 授予通过 telnet 远程登录权限的策略ssh - 授予通过安全外壳协议远程登录权限的策略web - 授予通过 WebFig 远程登录权限的策略。winbox - 授予通过 WinBox 远程登录和带宽测试认证权限的策略password - 授予当前登录用户更改密码权限的策略（自己的密码） api - 授予通过 API 访问路由器权限。rest-api - 授予通过 REST API 访问路由器权限。ftp - 授予通过 FTP 远程登录完全权限的策略。允许读取/写入/删除文件以及从路由器传输文件。应与 read/write 策略一起使用。romon - 授予连接到 RoMon 服务器权限的策略。配置策略： reboot - 允许重启路由器的策略read - 授予读取路由器配置权限的策略。所有不改变路由器配置的控制台命令都允许。不影响 FTPwrite - 授予写入路由器配置权限的策略，用户管理除外。此策略不允许读取配置，因此请确保同时启用 read 策略policy - 授予用户管理权限的策略。应与 write 策略一起使用。还允许查看其他用户创建的全局变量（也需要 'test' 策略）。允许设计皮肤（也需要 "sensitive" 策略）。test - 授予运行 ping、traceroute、bandwidth-test、wireless scan、snooper、fetch、email 和其他测试命令权限的策略sensitive - 授予更改“隐藏敏感信息”选项的权限，如果禁用此策略，则不显示敏感信息。sniff - 授予使用数据包嗅探器工具、torch 工具、流量生成器权限的策略。 |
| **skin** (*名称*; 默认值: **default**) | WebFig 使用的皮肤 |

### 默认组

有三个无法删除的默认系统组：

```ros
[admin@MikroTik] > /user/group/print 
0 name="read" policy=local,telnet,ssh,reboot,read,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!write,!policy skin=default 

1 name="write" policy=local,telnet,ssh,reboot,read,write,test,winbox,password,web,sniff,sensitive,api,romon,rest-api,!ftp,!policy skin=default 

2 name="full" policy=local,telnet,ssh,ftp,reboot,read,write,policy,test,winbox,password,web,sniff,sensitive,api,romon,rest-api skin=default 
```

请注意，即使是 "*read*" 组也包含 *sensitive*、*reboot* 和其他重要策略，这意味着不应将此组授予不受信任的用户。对于真正受限的组，请创建自定义组，定义特定的策略。所有组都可以访问文件操作。策略项名称前的感叹号 '!' 表示 NOT（非）。

## 路由器用户

路由器用户数据库存储有关路由器管理人员的用户名、密码、允许的访问地址和组等信息。

### 属性

| 属性 | 说明 |
| :-- | :-- |
| **address** (*IP/掩码 \| IPv6 前缀*; 默认值: ) | 允许用户登录的主机或网络地址 |
| **group** (*字符串*; 默认值: ) | 用户所属组的名称 |
| **inactivity-policy** (*lockscreen* \| *logout* \| *none*; 默认值: ***none***) | 指定非活动操作 - logout（用户将被注销）或 lockscreen（会话将被锁定，需要输入密码才能继续）。仅适用于 CLI 会话。 |
| **inactivity-timeout** (*时间*; 默认值: ***10min***) | 指定用户将被注销或会话被锁定后的时间。最小超时 - 1 分钟，最大超时 - 24 小时。仅适用于 CLI 会话。 |
| **name** (*字符串*; 默认值: ) | 用户名。必须以字母数字字符开头和结尾，但可以包含 "\_"、"."、"#"、"-" 和 "@" 符号。但是，用户名中禁止使用 "\*" 符号。 |
| **password** (*字符串*; 默认值: ) *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用户密码。如果未指定，则留空（登录时按 <kbd>Enter</kbd>）。它符合标准的 Unix 密码特性，可以包含字母、数字、"\*" 和 "\_" 符号。 |
| **last-logged-in** (*时间和日期*; 默认值: **""**) | 只读字段。用户上次登录的时间和日期。 |

### 操作

对现有路由器用户的操作。

| 操作 | 说明 |
| :-- | :-- |
| **password** | 更改用户密码的选项。 |
| **expire-password** | 使该用户密码过期，下次登录时，路由器将提示更改密码。 |

### 备注

有一个预定义的用户具有完全访问权限：

```ros
[admin@MikroTik] /user> print
Flags: X - disabled
# NAME GROUP ADDRESS LAST-LOGGED-IN
0 ;;; system default user
admin full 0.0.0.0/0 2010-12-08 16:19:24

```

应始终至少有一个具有完全访问权限的用户。如果具有完全访问权限的用户是唯一一个，则无法将其删除。

## 监控活动用户

```ros
/user/active/print
```

 该命令显示当前活动用户以及相应的统计信息。

### 属性

所有属性均为只读。

| 属性 | 说明 |
| :-- | :-- |
| **address** (*IP/IPv6 地址/MAC 地址*) | 用户访问路由器的主机 IP/IPv6/MAC 地址。 |
| **group** (*字符串*) | 用户所属的组。 |
| **name** (*字符串*) | 用户名。 |
| **radius** (*true \| false*) | 用户是否由 RADIUS 服务器认证。 |
| **via** (*telnet \| ssh \| winbox \| api \| rest-api \| web \| ftp* ) | 用户的访问方式 |
| **by-romon**(MAC 地址) | RoMON 代理 MAC 地址 |
| **when** (*时间*) | 用户登录的时间和日期。 |

### 请求注销

可以使用请求注销功能关闭活动会话。

```routeros
 /user/active/request-logout ACTIVE_USER_SESSION_NUMBER
```

## 远程 AAA

路由器用户远程 AAA 支持通过 RADIUS 服务器进行用户认证和计费。仅当在本地用户数据库中找不到所需的用户名时，才会查询 RADIUS 用户数据库。

### 属性

| 属性 | 说明 |
| :-- | :-- |
| **accounting** (*yes \| no*; 默认值: **yes**) | 是否应向 RADIUS 服务器发送登录、注销的计费信息。带宽使用统计不属于 `/user` 计费的一部分 |
| **exclude-groups** (*组名列表*; 默认值: ) | exclude-groups 包含不应允许用于通过 radius 认证的用户的组。如果 radius 服务器提供了此列表中指定的组，则将改用 default-group。这是为了防止权限提升，即当某个用户（没有策略权限）可以更改 radius 服务器列表、设置自己的 radius 服务器并以管理员身份登录时。 |
| **default-group** (*字符串*; 默认值: **read**) | 通过 RADIUS 服务器认证的用户默认使用的用户组。 |
| **interim-update** (*时间*; 默认值: **0s**) | Interim-Update 时间间隔 |
| **use-radius** (*yes \|no*; 默认值: **no**) | 启用通过 RADIUS 进行用户认证 |

:::info
如果您使用 RADIUS，则需要在 RADIUS 服务器上启用 CHAP 支持才能使 WinBox 正常工作。
:::

## SSH 密钥

 此菜单允许导入用于 SSH 认证的私钥和公钥。

:::warning
默认情况下，如果为用户添加了 SSH 密钥，则不允许该用户通过 SSH 密码登录。更多详情请参阅 [SSH](../management-tools/ssh.md) 页面。
:::

### 公钥

此菜单用于导入（或添加）和列出已导入的公钥。公钥用于在使用 SSH 密钥登录路由器时验证另一设备的身份。

:::info
支持 PEM、PKCS#8 或 OpenSSH 格式的 RSA、Ed25519 和 Ed25519-sk 密钥。
:::

| 属性 | 说明 |
| :-- | :-- |
| **user** (只读*)* | 已分配 SSH 密钥的系统用户 |
| **info** (只读*)* | 密钥信息 |
| **key-type** (只读*)* | 密钥类型 |
| **bits** (只读*)* | 密钥长度 |
| **fingerprint** (只读*)* | SHA256 (Base64) 格式的密钥指纹 |

#### 导入公共 SSH 密钥

导入公共 SSH 密钥时，必须指定密钥文件、将分配 SSH 密钥的系统用户，可选地，可以指定密钥所有者。

| 属性 | 说明 |
| :-- | :-- |
| **user** (*字符串*; 默认值: ) | 已分配 SSH 密钥的系统用户 |
| **key-owner** (*字符串*) | SSH 密钥所有者 |
| **public-key-file** (*字符串*) | 路由器根目录中包含公钥的文件名 |

#### 添加公共 SSH 密钥

可以 *添加* 公共 SSH 密钥（粘贴 SSH 密钥字符串），您必须提供密钥字符串以及已分配 SSH 密钥的系统用户。

:::note
只能 *添加* OpenSSH 格式的密钥
:::

| 属性 | 说明 |
| :-- | :-- |
| **user** (*字符串*; 默认值: ) | 已分配 SSH 密钥的系统用户 |
| **key** (*字符串*) | 公钥 |

### 私钥

此菜单用于导入和列出已导入的私钥。私钥用于在使用 SSH 密钥登录另一设备时验证路由器的身份。

导入私钥时，可以指定 key-owner。

:::info
支持 PEM 或 PKCS#8 格式的 RSA 和 Ed25519 密钥。
:::

| 属性 | 说明 |
| :-- | :-- |
| **user** (*字符串*; 默认值: ) | 已分配 SSH 密钥的系统用户 |
| **key-owner** (*字符串*) | SSH 密钥所有者 |
| **key-type** (只读*)* | 密钥类型 |
| **bits** (只读*)* | 密钥长度 |

#### 导入私有 SSH 密钥

导入私有 SSH 密钥时，必须指定密钥文件、将分配 SSH 密钥的系统用户，可选地，可以提供密钥密码短语并指定密钥所有者。

| 属性 | 说明 |
| :-- | :-- |
| **user** (*字符串*; 默认值: ) | 已分配 SSH 密钥的系统用户 |
| **key-owner** (*字符串*) | SSH 密钥所有者 |
| **passphrase** *(字符串) [敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 密钥文件密码短语 |
| **private-key-file** (*字符串*) | 路由器根目录中包含私钥的文件名 |