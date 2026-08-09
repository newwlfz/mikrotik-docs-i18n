# SSH

> RouterOS 内置了SSH服务器，支持自定义设置，如密码配置、密钥类型和转发选项。它支持密码和公钥认证，并提供命令来导出/导入主机密钥及重新生成它们。通过为用户导入公钥，可以启用PKI认证。

# SSH

## SSH服务器

RouterOS 内置了SSH（SSH v2）服务器，默认启用并监听TCP/22端口的传入连接。可以在[服务](../system-information-and-utilities/services.md)菜单中更改端口或禁用服务器。

### 属性

**子菜单：** `/ip/ssh`

| 属性 | 描述 |
| :-- | :-- |
| **password-authentication** (*yes-if-no-key* \| *yes \| no*; 默认值：**yes-if-no-key**) | 当为用户配置了公钥授权时，是否同时允许密码登录。 |
| **ciphers** (*3des-cbc *\| aes-cbc \| aes-ctr \| aes-gcm \| auto \| null*;* 默认值：**auto**) | 允许配置SSH加密算法。 |
| **forwarding-enabled** (*both \| local \| no \| remote*; 默认值：**no**) | 控制允许哪种SSH转发方法：no - 禁用SSH转发；local - 允许SSH客户端从服务器（路由器）发起连接，此设置也控制动态转发；remote - 允许SSH客户端在服务器（路由器）上监听并转发传入连接；both - 允许本地和远程转发方法。 |
| **host-key-size** (*1024 \| 1536 \| 2048 \| 4096 \| 8192*; 默认值：**2048**) | 重新生成主机密钥时的RSA密钥大小。 |
| **host-key-type** (*ed25519* \| *rsa*; 默认值：**rsa**) | 选择主机密钥类型。 |
| **publickey-authentication-options** (*none* \| *touch-required* \| *verify-required*; 默认值：**none**) | 设置公钥认证选项。touch-required选项使使用FIDO认证器算法的公钥认证始终要求签名证明物理存在的用户明确确认认证（通常通过触摸认证器）。verify-required选项要求FIDO密钥签名证明用户已验证，例如通过PIN码。 |
| **strong-crypto** (*yes \| no*; 默认值：**no**) | 使用更强的加密、HMAC算法，使用更大的DH素数并禁止较弱的算法：使用256和192位加密代替128位；禁用null加密；使用sha256代替sha1进行哈希；禁用md5；使用2048位素数进行Diffie-Hellman交换代替1024位。 |

### 命令

**export-host-key** (*key-file-prefix*)

将公钥和私钥RSA/Ed25519导出到文件。命令接受两个参数：

- **key-file-prefix** - 用于生成文件的前缀，例如，前缀'my'将生成文件'my_rsa'、'my_rsa.pub'等。
- **passphrase** - 私钥密码短语 [敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)

:::info
主机密钥以PKCS#8格式导出。

**警告：** 导出SSH主机密钥需要“敏感”用户策略。
:::

---

**import-host-key** (*private-key-file*)

从指定文件导入并替换私钥RSA/Ed25519。命令接受两个参数：

- **private-key-file** - 私钥RSA/Ed25519文件名
- **passphrase** - 私钥密码短语 [敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)

:::info
私钥支持PEM或PKCS#8格式。
:::

---

**regenerate-host-key** ()

生成新的密钥并替换路由器上当前的私钥集（RSA/Ed25519）。请注意，之前导入的密钥可能失效。

### 启用PKI认证

为用户 **admin** 导入公钥的示例

[在客户端设备上获取SSH密钥对](#log-in-using-ssh-key)（您将从中连接的设备）。将公钥SSH密钥上传到路由器并导入。

有关支持的SSH密钥的更多信息，请参阅[用户SSH密钥](../authentication-authorization-accounting/user.md#ssh-keys)部分。

```ros
/user/ssh-keys/import public-key-file=id_rsa.pub user=admin
```

### SSH密钥对生成

RouterOS 不支持直接生成SSH密钥对，这在Linux系统上是可用的。

要获取SSH密钥对（SSH密钥对在首次SSH连接时自动生成），必须[导出](#commands)设备的SSH主机密钥。

## SSH客户端

**子菜单：** `/system/ssh`

### **简单登录远程主机**

能够连接到远程主机并启动SSH会话。IP地址支持IPv4和IPv6。

```ros
/system/ssh 192.168.88.1
/system/ssh 2001:db8:add:1337::beef
```

在这种情况下，提供给远程主机的用户名是登录到路由器的用户名。如果需要其他值，则必须使用 *user=\<username>*。

```ros
/system/ssh 192.168.88.1 user=lala
/system/ssh 2001:db8:add:1337::beef user=lala
```

### **从路由器的特定IP地址登录**

出于测试或安全原因，可能需要使用特定的源地址连接到另一台主机。在这种情况下，必须使用 *src-address=\<ip address>* 参数。请注意，此处的IP地址支持IPv4和IPv6。

```ros
/system/ssh 192.168.88.1 src-address=192.168.89.2
/system/ssh 2001:db8:add:1337::beef src-address=2001:db8:bad:1000::2
```

在这种情况下，SSH客户端将尝试绑定到指定的地址，然后启动与远程主机的SSH连接。

### **使用SSH密钥登录**

为用户 *admin* 导入RSA私钥的示例。

首先，将当前生成的SSH密钥导出到文件：

```ros
/ip/ssh/export-host-key key-file-prefix=admin
```

将生成两个文件 *admin\_rsa* 和 *admin\_rsa.pub*。pub文件需要在SSH服务器端受信任（[如何在RouterOS上启用SSH PKI](./ssh.md#enabling-pki-authentication)）。私钥必须添加到特定用户。

```ros
/user/ssh-keys/private/import user=admin private-key-file=admin_rsa
```

:::danger
只有具有路由器完全权限的用户才能更改 *`/user/ssh-keys/private`* 下的'user'属性值。
:::

在公钥安装并在SSH服务器上受信任后，可以创建PKI SSH会话。

```ros
/system/ssh 192.168.1.1
```

观看如何：

使用[RSA密钥](http://youtube.com/watch?v=8tt7fSvdFRM)登录。

使用[Ed25519](http://youtube.com/watch?v=be-pBwhjRWA)登录。

### **执行远程命令**

要执行远程命令，必须在登录行末尾提供该命令

```ros
/system/ssh 192.168.88.1 "/ip/address/print"
/system/ssh 192.168.88.1 command="/ip/address/print"
/system/ssh 2001:db8:add:1337::beef "/ip/address/print"
/system/ssh 2001:db8:add:1337::beef command="/ip/address/print"
```

:::danger
*如果服务器不支持伪终端（ssh -T 或 ssh host command），如MikroTik ssh服务器，则无法通过SSH发送多行命令*
:::

例如，向MikroTik路由器发送命令 `"/ip/address \n add address=1.1.1.1/24"` 将失败。

:::warning
如果您希望通过**脚本**或**调度器**执行远程命令，请使用命令**ssh-exec**。
:::

## SSH执行

**子菜单：** `/system/ssh-exec`

命令 *ssh-exec* 是一个非交互式SSH命令，允许通过脚本和调度器在设备上远程执行命令。

### **检索信息**

该命令将返回两个值：

- **exit-code**：如果命令执行成功则返回0
- **output**：返回远程执行命令的输出

**示例：** 以下代码将从设备10.10.10.1检索ether1的接口状态，并将结果输出到“日志”

```ros
:local Status ([/system/ssh-exec address=10.10.10.1 user=remote command=":put ([/interface/ethernet/monitor [find where name=ether1] once as-value]->\"status\")" as-value]->"output")
:log info $Status
```

:::warning
出于安全原因，不应在命令行中使用明文密码参数“password”。为确保远程安全执行命令，强烈建议在双方使用SSH PKI认证。

**注意：** 执行命令的用户组和脚本策略需要**测试**权限。
:::

观看如何[通过SSH执行命令](http://youtube.com/watch?v=JfGfPSicTzs)。