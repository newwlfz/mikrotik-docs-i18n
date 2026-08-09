# 电子邮件

> RouterOS 中的电子邮件工具支持通过 SMTP 协议（支持明文认证或 TLS 加密）直接从设备发送电子邮件，可用于定时发送配置备份和自定义邮件内容。通过 `/tool/e-mail` 子菜单，可配置 SMTP 服务器、认证信息、加密设置及附件处理。

# 电子邮件

电子邮件工具是 RouterOS 内置的实用程序，使路由器能够直接从设备发送电子邮件消息。它可用于按计划自动将配置备份和导出文件发送给网络管理员。

电子邮件工具支持明文认证和 TLS 加密。不支持其他认证或加密方式。

## 属性

**子菜单：** `/tool/e-mail`

该子菜单用于设置将要使用的 SMTP 服务器。

| 属性 | 说明 |
| :-- | :-- |
| **address**（*IP/IPv6 地址*；默认值：**0.0.0.0**） | SMTP 服务器的 IP 地址。 |
| **certificate-verification**（*yes* \| *yes-without-crl* \| *no*；默认值：**no**） | 启用来自本地证书存储的信任链验证。*yes-without-crl* 验证证书但不执行 CRL（证书吊销列表）检查。 |
| **from**（*字符串*；默认值：**\<>**） | 将显示为发件人的名称或电子邮件地址。 |
| **password**（*字符串*；默认值：**""**）*[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于向 SMTP 服务器进行认证的密码。 |
| **port**（*整数[0..65535]*；默认值：**25**） | SMTP 服务器的端口。 |
| **tls**（*no\|yes\|starttls*；默认值：**no**） | 是否使用 TLS 加密：yes - 发送 STARTTLS，如果服务器不支持 TLS 则终止会话no - 不发送 STARTTLSstarttls - 发送 STARTTLS，如果服务器响应不支持 TLS 则继续无 TLS 连接 |
| **user**（*字符串*；默认值：**""**） | 用于向 SMTP 服务器进行认证的用户名。 |
| **vrf**（*VRF 名称*；默认值：**main**） | 设置服务创建出站连接所使用的 VRF。 |

:::warning
**注意：** 所有服务器配置（如果已指定）均可被 send 命令覆盖。
:::

---

## 发送电子邮件

**子菜单：** `/tool/e-mail`

Send 命令接受以下参数：

| 属性 | 说明 |
| :-- | :-- |
| **body**（*字符串*；默认值：） | 电子邮件消息的实际正文 |
| **cc**（*字符串*；默认值：） | 向列出的收件人发送副本。允许多个地址，使用“,”分隔条目 |
| **certificate-verification**（*yes* \| *yes-without-crl* \| *no*；默认值：**no**） | 启用来自本地证书存储的信任链验证。*yes-without-crl* 验证证书但不执行 CRL（证书吊销列表）检查。 |
| **file**（*文件[,文件]*；默认值：） | 将附加到邮件中的文件名列表，以逗号分隔。 |
| **from**（*字符串*；默认值：） | 将显示为发件人的名称或电子邮件地址。如果未指定，则使用服务器配置中的值。 |
| **password**（*字符串*；默认值：）*[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用于向 SMTP 服务器进行认证的密码。如果未指定，则使用服务器配置中的值。 |
| **port**（*整数[0..65535]*；默认值：） | SMTP 服务器的端口。如果未指定，则使用服务器配置中的值。 |
| **server**（*IP/IPv6 地址*；默认值：） | SMTP 服务器的 IP 或 IPv6 地址。如果未指定，则使用服务器配置中的值。 |
| **tls**（*yes\|no\|starttls*；默认值：**no**） | 是否使用 TLS 加密：yes - 发送 STARTTLS，如果服务器不支持 TLS 则终止会话no - 不发送 STARTTLSstarttls - 发送 STARTTLS，如果服务器响应不支持 TLS 则继续无 TLS 连接 |
| **subject**（*字符串*；默认值：） | 消息的主题。 |
| **to**（*字符串*；默认值：） | 目标电子邮件地址。仅允许单个地址。 |
| **user**（*字符串*；默认值：） | 用于向 SMTP 服务器进行认证的用户名。如果未指定，则使用服务器配置中的值。 |

---

## 基本示例

**以下示例演示如何每 24 小时发送一次包含配置导出的电子邮件。**

1. 配置 SMTP 服务器。

```ros
[admin@MikroTik] /tool/e-mail> set server=10.1.1.1 port=25 from="router@mydomain.com"
```

1. 添加一个名为“export-send”的新脚本：

```ros
/export file=export 
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name] export" \ 
body="$[/system/clock/get date] configuration file" file=export.rsc
```

1. 添加调度器以运行我们的脚本。

```ros
/system/scheduler/add on-event="export-send" start-time=00:00:00 interval=24h
```

**使用 TLS/SSL 加密向服务器发送电子邮件。**

:::info
Google Mail 不允许第三方设备使用标准 Gmail 密码进行认证。必须生成并使用应用专用密码。

要生成应用专用密码，请导航至**安全 > 您如何登录 Google**，启用两步验证，然后生成应用专用密码。在下方所示的 `set password=mypassword` 设置中使用生成的值。
:::

1. 配置客户端以连接到正确的服务器。

```ros
/tool/e-mail 
set address=smtp.gmail.com
set port=587
set tls=yes 
set from=myuser@gmail.com 
set user=myuser 
set password=mypassword
```

1. 使用 send 命令发送电子邮件。

```ros
/tool/e-mail/send to=myuser@anotherdomain.com subject="email test" body="email test" 
```