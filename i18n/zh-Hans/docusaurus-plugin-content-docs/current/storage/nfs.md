# NFS

> NFS 使 RouterOS 能够通过 NFS v4 实现网络目录共享，需要 Storage 软件包。它使用端口 2049，并包含如 nfs-address、nfs-share 和 nfs-sharing 等配置属性。配置示例展示了如何在主机设备上启用 NFS，以及如何从 Linux 客户端挂载 NFS 共享。

# NFS

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

NFS 允许通过网络共享本地目录。RouterOS 目前仅支持 NFS v4 模式。

:::warning

NFS 使用 TCP/2049 端口。如果该端口不可用，在 `disk print detail` 中你会看到状态卡在 `nfs-state="mounting"`。

:::

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **nfs-address** | NFS 目标的 IP 地址。（主机设备 IP） |
| **nfs-share** | 指定要挂载的文件夹（客户端参数） |
| **nfs-sharing** | 在主机设备上禁用/启用 NFS |

## 配置示例

主机

```ros
/disk
set pcie1-nvme1 nfs-sharing=yes
```

客户端

```ros
/disk
add type=nfs nfs-address=192.168.1.1
```

Linux 客户端

```bash
mkdir /mnt/files
mount -t nfs 192.168.1.1:/ /mnt/files
```