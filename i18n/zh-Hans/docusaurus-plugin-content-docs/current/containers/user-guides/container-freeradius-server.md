# 容器 - FreeRADIUS 服务器

> 本页面介绍 MikroTik RouterOS 中的容器功能，用于在路由器内运行 RADIUS 等服务器，详细说明设置步骤，包括容器模式激活、网络配置以及 FreeRADIUS 服务器部署的镜像拉取。

# 容器 - FreeRADIUS 服务器

## 引言

RouterOS 引入容器功能后，可以在路由器内部运行各种类型的服务器，执行各类任务。这对于希望减少网络中设备数量的用户尤其重要。与其在单独的设备/机器上运行服务器，为何不直接在路由器内部运行呢？

[RADIUS](../../authentication-authorization-accounting/radius.md) 是远程认证拨号用户服务（Remote Authentication Dial-In User Service）的缩写。RouterOS 具有 RADIUS 客户端功能，可为 HotSpot、[PPP](../../mobile-networking/ppp.md)、[PPPoE](../../virtual-private-networks/pppoe/index.md)、[PPTP](../../virtual-private-networks/pptp.md)、[L2TP](../../virtual-private-networks/l2tp/index.md) 和 ISDN 连接进行认证。基本上，此功能允许您将 RouterOS 连接到 RADIUS 服务器，然后利用服务器上的用户数据库进行客户端认证。

在我们的示例中，我们将演示 **[freeradius/freeradius-server](https://hub.docker.com/r/freeradius/freeradius-server/tags)** 镜像的安装。

## 摘要

**子菜单：** `/container`

***注意**：* 需要 **container** 软件包。

在继续配置之前，请务必研究我们的 [container](../) 指南。请务必查看 [免责声明](../#disclaimer) 和 [要求](../#requirements) 部分，以了解所有风险以及您可能需要执行的必要步骤。

在本指南发布时，该镜像仅适用于 Linux/**amd64** 操作系统/架构（适用于 CHR 和 x86 设备）。对于 arm64 设备，您需要从 [FreeRADIUS 源代码](https://github.com/FreeRADIUS/freeradius-server) 自行构建容器。对于 arm64 和 arm32 设备，您也可以使用 **[freeradius/freeradius-server-dev](https://hub.docker.com/r/freeradius/freeradius-dev)** 镜像，**风险自负**（因为它是该镜像的“实验性/开发版”）。

为帮助您在 [Virtual Box](https://www.virtualbox.org/) 中设置 CHR，请查看我们的 [YouTube 教程](https://www.youtube.com/watch?v=oHXkaHkSVVo)，或 [打造您自己的 x86 路由器](https://www.youtube.com/watch?v=JpccW9tYOkQ)。

:::warning
本指南演示的是一个基础示例！测试在本地环境中进行！本指南仅用于基本的 RADIUS“测试”目的！并非所有“freeradius”功能都经过测试！
:::

## 配置

### 容器模式

启用容器模式：

```ros
/system/device-mode/update container=yes
```

如果在 X86 上使用容器，您需要通过冷重启来确认设备模式。

### 网络配置

为容器添加 veth 接口：

```ros
/interface/veth/add name=veth3 address=172.17.0.2/24 gateway=172.17.0.1
```

为容器创建桥接，为其分配 IP 网络，并将 veth 添加到桥接中：

```ros
/interface/bridge/add name=dockerfreeradius
/ip/address/add address=172.17.0.1/24 interface=dockerfreeradius
/interface/bridge/port/add bridge=dockerfreeradius interface=veth3
```

如有需要，为出站流量设置 NAT：

```ros
/ip/firewall/nat/add chain=srcnat action=masquerade src-address=172.17.0.0/24
```

### 获取镜像

为简化配置，我们将从外部库获取镜像，但您也可以通过 [.tar](../#option-b-import-image-from-pc) 文件导入。

确保已正确设置“Registry URL”，限制 RAM 使用量（如有必要），并为镜像设置目录：

```ros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=pull
```

使用以下命令拉取镜像：

```ros
/container/add remote-image=freeradius/freeradius-server:latest interface=veth3 root-dir=freeradius logging=yes cmd="-X"
```

其中 `cmd="-X"` 启用调试日志（根据“freeradius”文档）。

运行命令后，RouterOS 应开始“解压”软件包。检查“文件系统”中新建的文件夹，并使用 `/container/print` 命令监控容器状态。

### 启动容器

在使用 `/container/print` 确认容器已添加且状态变为 `status=stopped` 后，您可以启动它：

```ros
/container/start 0
```

### 修改服务器配置文件

要访问服务器的配置文件（**clients.conf** 和 **authorize**），我们需要使用 SFTP（基于 SSH 的文件传输）协议，因此请确保 SSH [服务](../../system-information-and-utilities/services.md) 已启用。

打开您的命令终端（Windows 用户以管理员身份打开“CMD”，Linux 用户打开“Linux Shell 或命令终端”），并导航到您想要下载配置文件的目录。例如，桌面上的“radius”文件夹：

```powershell
C:\WINDOWS\system32>cd C:\Users\Administrator\Desktop\radius
 
C:\Users\Administrator\Desktop\radius>
```

向设备的 IP 地址发起 SFTP 连接：

```powershell
C:\Users\Administrator\Desktop\radius>sftp admin@10.55.8.53
admin@10.55.8.53's password:
Connected to 10.55.8.53.
sftp>
```

进入服务器的配置文件目录（使用 `dir` 或 `ls` 命令查看当前目录内容，使用 `cd` 命令进入所需目录）。

第一个文件“clients.conf”允许您定义 RADIUS 客户端。根据“freeradius”文档，它应位于 `/etc/freeradius` 目录下……因此，导航到该目录并使用 `get` 命令下载它：

```powershell
sftp> dir
freeradius          pub                     pull                    skins                   
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> get clients.conf
Fetching /freeradius/etc/freeradius/clients.conf to clients.conf
/freeradius/etc/freeradius/clients.conf                                               100% 8323     1.2MB/s   00:00
```

使用您喜欢的文本编辑器（记事本或其他）打开“**clients.conf**”。您可以研究该文件以了解所有可用选项（此外，请查看 [freeradius.org](https://wiki.freeradius.org/config/Configuration-files)）。本示例展示了一个基本配置，因此我们将用以下行覆盖整个文件：

```text
client new {
    ipaddr = 0.0.0.0/0
    secret = client_password
}
```

其中我们指定 RADIUS 客户端可以使用任何可能的 IP 地址连接（**ipaddr=0.0.0.0/0** 确保这一点，但如果您需要，也可以将其更改为 RADIUS 客户端的实际 IP 地址/掩码），并且我们的密钥是“client\_password”（您可以将其更改为任何其他密钥）。

保存/覆盖该文件。

第二个文件“authorize”允许您设置用户。根据“freeradius”文档，它应位于 `/etc/freeradius/mods-config/files` 目录下。导航到该目录并 `get` 该文件：

```powershell
sftp> dir
freeradius          pub                     pull                    skins                    
sftp> cd freeradius/etc/freeradius/mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> get authorize
Fetching /freeradius/etc/freeradius/mods-config/files/authorize to authorize
/freeradius/etc/freeradius/mods-config/files/authorize                                100% 6594     1.1MB/s   00:00
```

使用您喜欢的文本编辑器（记事本或其他）打开“**authorize**”。本示例展示了一个基本配置，因此我们只需取消注释（删除“#”符号）下面显示的行（其余配置/行保持不变）：

```text
bob	Cleartext-Password := "hello"
```

这将创建用户名“bob”并将密码设置为“hello”（您可以更改用户名和密码）。

保存/覆盖该文件。

使用 `put` 命令将两个文件上传回去，覆盖默认文件：

```powershell
sftp> dir
freeradius          pub                     pull                    skins      
sftp> cd freeradius/etc/freeradius
sftp> dir
README.rst          certs               clients.conf        dictionary          experimental.conf   hints               
huntgroups          mods-available      mods-config         mods-enabled        panic.gdb           policy.d            
proxy.conf          radiusd.conf        sites-available     sites-enabled       templates.conf      trigger.conf        
users
sftp> put clients.conf
Uploading clients.conf to /freeradius/etc/freeradius/clients.conf
clients.conf                                                                          100%   67    22.3KB/s   00:00
sftp> cd mods-config/files
sftp> dir
accounting  authorize   dhcp        pre-proxy
sftp> put authorize
Uploading authorize to /freeradius/etc/freeradius/mods-config/files/authorize
authorize                                                                             100% 6626     1.6MB/s   00:00
```

重启容器：

```ros
/container/stop 0
/container/start 0
```

在再次启动之前，请务必等待容器停止（使用 `/container/print` 命令后应显示 `status=stopped`）。

## 结果验证

在 RouterOS 中，添加新的 RADIUS 客户端配置：

```ros
/radius/add service=login address=172.17.0.2 secret="client_password"
```

其中 `address` 是 veth3 接口的 IP 地址，`secret` 是我们在 **clients.conf** 文件中配置的密钥，`service` 是您希望使用的允许服务。

通过以下命令允许使用 RADIUS 用户进行“login”：

```ros
/user/aaa/set use-radius=yes
```

我们已允许 RADIUS 的“login”服务，可以使用 ssh/winbox/webfig 连接进行测试。对于 SSH 测试，执行以下命令（您需要指定设备的管理 IP，并在之后输入 bob 的密码“hello”）：

```ros
/system/ssh 10.55.8.53 user=bob
```

您应该能够验证终端用户已从“admin@MikroTik”更改为“bob@MikroTik”：

```ros
[admin@MikroTik] > /system/ssh 10.55.8.53 user=bob
password:hello                                                                                                                                                                 
 

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.8alpha173 (c) 1999-2023       https://www.mikrotik.com/

按 F1 获取帮助
  
[bob@MikroTik] > 
```

如果执行 `/user/active/print` 命令：

```ros
/user/active/print
Flags: R - RADIUS
Columns: WHEN, NAME, ADDRESS, VIA
#   WHEN                  NAME   ADDRESS     VIA    
0   2023-02-16 16:31:21  admin  xx.xx.xx.xx  winbox 
1   2023-02-16 16:38:46  admin  xx.xx.xx.xx  console
2 R 2023-02-16 16:38:53  bob    10.55.8.53  ssh  
```

您将能够验证新用户“bob”处于“active”状态，并分配了标志“R”，这表示它是 RADIUS 用户。