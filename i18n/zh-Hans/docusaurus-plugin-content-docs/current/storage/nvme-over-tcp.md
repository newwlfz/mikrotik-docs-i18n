# NVMe over TCP

> NVMe over TCP 为发起端（initiator）和目标端（target）提供基于网络的 NVMe 存储访问，支持可配置的 IP 地址、端口、密码以及基于主机的访问控制。示例演示了如何将 RouterOS 客户端上的磁盘挂载到服务器，包括 Linux 客户端的设置步骤。

# NVMe over TCP

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

nvme-tcp 允许在发起端通过网络将存储作为 NVMe 块设备进行访问。在目标端，该设备可以是 hdd/ssd/nvme，甚至是 RAID 阵列。

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **nvme-tcp-address** | NVMe over TCP 目标端的 IP 地址。（主机设备 IP） |
| **nvme-tcp-export** | 在主机设备上禁用/启用 NVMe over TCP |
| **nvme-tcp-host-name** | 此属性指定 NVMe over TCP 发起端的主机名。可用于标识和认证目的 |
| **nvme-tcp-name** | 此属性指定 NVMe over TCP 目标端的名称或用于引用目的的连接名称（需与主机插槽名称相同） |
| **nvme-tcp-password** *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 此属性用于指定 NVMe over TCP 连接的认证密码，确保安全访问。 |
| **nvme-tcp-port** | 此属性指定 NVMe over TCP 目标端用于监听发起端传入连接的网络端口。NVMe over TCP 流量的默认端口为 4420。 |
| **nvme-tcp-server-allow-host-name** | 此属性指定 NVMe over TCP 服务器是否允许来自特定主机名的连接，提供基于主机的访问控制机制。 |
| **nvme-tcp-server-password** *[敏感](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 此属性指定 NVMe over TCP 服务器的密码，用于对连接到目标端的发起端进行认证。 |
| **nvme-tcp-server-port** | 此属性指定 NVMe over TCP 服务器用于接受发起端连接的网络端口。 |

## 示例

### 挂载磁盘

在此示例中，一台 RouterOS 设备用作存储服务器（**Host**），另一台 RouterOS 设备需要通过网络挂载存储设备（**Client**）。

1. 在 **Host** 上使用以下命令：

   ```ros
   /disk/set disk1 nvme-tcp-export=yes nvme-tcp-port=4420
   ```

2. 在 **Client** 上使用以下命令：

   ```ros
   /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=disk1
   ```

3. 您的 **Client** 现在将看到一个实际通过 NVMe over TCP 网络挂载的磁盘。

#### Linux 客户端

使用以下命令在 Linux **Client** 上设置 NVMe over TCP。

1. 加载内核模块。

    ```bash
    modprobe nvme_tcp
    ```

2. 发现现有的 NVMe over TCP 挂载。

   ```bash
   nvme discover -t tcp -a 192.168.1.1 -s 4420
   ```

   ```routeros
   #输出：
   Discovery Log Number of Records 1, Generation counter 2
   =====Discovery Log Entry 0======
   trtype:  tcp
   adrfam:  ipv4
   subtype: nvme subsystem
   treq:    not specified, sq flow control disable supported
   portid:  4420
   trsvcid: 4420
   subnqn:  disk1
   traddr:  10.155.166.7
   sectype: none
   ```

3. 连接到 NVMe over TCP 挂载。

   ```bash
   nvme connect -t tcp -a 192.168.1.1 -s 4420 -n disk1
   ```

4. 块设备现在应该可用。

   ```bash
   ls /dev/nvme*

   ```

    ```bash
    #输出：
    /dev/nvme0  /dev/nvme0n1  /dev/nvme-fabrics
    ```

5. 您现在可以将挂载的块设备像 Linux **Client** 上的任何其他块设备一样使用。

如果您想断开挂载的块设备：

```bash
nvme disconnect -d /dev/nvme0
```

### 将文件挂载为块设备

在此示例中，一台 RouterOS 设备用作存储服务器（**Host**），另一台 RouterOS 设备需要通过网络挂载存储设备（**Client**）。

:::warning

当您不想将整个磁盘委托给 **Client**，而是希望将磁盘大小的一部分提供给 **Client** 时，这种设置非常有用。与使用 NVMe over TCP 挂载磁盘（或分区）相比，挂载文件而非磁盘的性能会较低。

:::

1. 在 **Host** 上使用以下命令创建一个将用作块设备的文件：

   ```routeros
   /disk/add type=file file-path=disk1/BIGFILE.img file-size=10G slot=blockdevice1
   /disk/set blockdevice1 nvme-tcp-export=yes 
   ```

2. 在 **Client** 上使用以下命令将文件挂载为块设备：

   ```routeros
   /disk/nvme-discover 192.168.1.1
   /disk/add nvme-tcp-address=192.168.1.1 nvme-tcp-name=blockdevice1 type=nvme-tcp
   /disk/format blockdevice1 file-system=ext4
   ```

3. 您的 **Client** 现在将看到一个名为 `blockdevice1` 的新磁盘，尽管在 **Server** 上存储设备实际上是一个文件。

:::tip

如果您想在 Linux **Client** 上挂载块设备，请查看 [Linux 客户端](#linux-client) 部分。

:::

### 挂载 RAID 阵列

在此示例中，一台 RouterOS 设备用作存储服务器（**Host**），另一台 RouterOS 设备需要通过网络挂载存储设备（**Client**），同时提供数据冗余。

1. 在 **Host** 上设置 [RAID](./raid/index.md)，例如：

   ```routeros
   /disk/add raid-device-count=8 raid-type=6 slot=RAID6_array type=raid
   /disk/set disk1 raid-master=RAID6_array raid-role=0
   /disk/set disk2 raid-master=RAID6_array raid-role=1
   /disk/set disk3 raid-master=RAID6_array raid-role=2 
   /disk/set disk4 raid-master=RAID6_array raid-role=3
   /disk/set disk5 raid-master=RAID6_array raid-role=4
   /disk/set disk6 raid-master=RAID6_array raid-role=5
   /disk/set disk7 raid-master=RAID6_array raid-role=6 
   /disk/set disk8 raid-master=RAID6_array raid-role=7
   /disk/set RAID6_array nvme-tcp-export=yes
   ```

2. 在 **Client** 上使用以下命令：

    ```ros
    /disk/add type=nvme-tcp nvme-tcp-address=192.168.1.1 nvme-tcp-name=RAID6_array
    ```

3. 您的 **Client** 现在将看到一个单独的磁盘，但它实际上是一个高度冗余的 RAID 阵列。

:::tip

如果您想在 Linux **Client** 上挂载块设备，请查看 [Linux 客户端](#linux-client) 部分。

:::

:::danger

不要在 Linux Client 上挂载来自不同 RouterOS 设备的多个磁盘，并将其配置为软件 RAID（例如 mdadm）。虽然这种配置确实提供了一定的冗余，但您可能会遇到异常延迟问题甚至超时。建议在 RouterOS 上创建 RAID 阵列，并将 RAID 阵列作为块设备导出到 Linux Client。

:::