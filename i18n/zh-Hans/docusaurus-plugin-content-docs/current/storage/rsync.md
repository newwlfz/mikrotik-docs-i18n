# Rsync

> RouterOS 中的 Rsync 允许系统之间利用 IPsec 加密进行高效的文件同步，并支持可配置的本地/远程路径以及上传/下载模式。当设置密码时，会创建动态 IPsec 条目，确保通过 TCP/8291 和 UDP/500 进行安全传输。

# Rsync

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

`rsync`（远程同步）是一款功能强大的文件同步和文件传输程序，广泛应用于基于 Unix 的系统中。它能够在不同系统之间或同一系统内部高效地传输和同步文件及目录。

如果您对文件进行了修改，则只会传输更改的部分，从而减少数据传输量。RouterOS 的 RSYNC 实现使用 IPsec 进行数据传输（如果设置了密码）。配置完成后，您将看到动态的 IPsec 条目。

Rsync 设置可以在 `file/sync` 菜单中找到。

:::warning

TCP/873 端口用于 rsync 控制连接（如果状态中未开放该端口（*file sync print*），您将卡在向 *192.168.88.2* 建立控制连接的阶段）

UDP/500 端口和协议 50（ipsec-esp）用于创建安全连接并启动传输（如果状态中未开放这些端口（*file sync print*），您将卡在初始化传输的阶段）

:::

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **local-path** | 文件/文件夹路径。用于 *上传* 模式，设置要上传到设备的文件/文件夹路径 |
| **mode** | 设置您是要下载还是上传文件（同步的方向） |
| **password** | 目标设备密码 |
| **remote-address** | 目标设备 IP |
| **remote-path** | 文件/文件夹路径。与 *下载* 模式配合使用，设置目标设备上要下载的路径 |
| **user** | 目标设备用户名 |

## 配置示例

基本配置非常简单。在主机设备上，您需要添加要同步到另一设备的文件、IP、用户名/密码以及模式。

```ros
/file/sync
add local-path=/ipv6route.txt.rsc mode=upload remote-address=192.168.88.2 remote-path=RAID/

```

如果配置正确，您将在主机设备上看到：

```ros
0 192.168.88.2  upload  /ipv6route.txt.rsc  RAID/        in sync
```

在客户端设备上：

```ros
#   REMOTE-ADDRESS   MODE      LOCAL-PATH  REMOTE-PATH         STATUS 
0 D 192.168.88.1 download  RAID/       /ipv6route.txt.rsc  in sync
```

### IPSec 动态条目

当 rsync 配置了密码时，它会为安全传输创建动态的 IPSec 条目：

```ros
#     PEER                     TUNNEL  SRC-ADDRESS       DST-ADDRESS       PROTOCOL  ACTION   LEVEL    PH2-COUNT
;;; file-sync-10.155.145.11
1  D  file-sync-10.155.145.11  no      10.155.145.17/32  10.155.145.11/32  tcp       encrypt  require          1

/ip/ipsec/peer> print
 0  D  name="file-sync-10.155.145.11" address=10.155.145.11/32 local-address=10.155.145.17 profile=default exchange-mode=main send-initial-contact=yes
/ip/ipsec/identity> print
 0 D  ;;; file-sync-10.155.145.11
      peer=file-sync-10.155.145.11 auth-method=pre-shared-key secret="secret" generate-policy=no
```