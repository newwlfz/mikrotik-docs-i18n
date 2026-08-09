# Btrfs 子卷与快照

> 本页面指导用户如何在 MikroTik RouterOS 上创建 Btrfs 子卷和快照，解释如何组织数据、格式化磁盘、设置如 Documents 和 Photos 等子卷，以及创建快照以实现高效备份而无需重复数据。

# Btrfs 子卷与快照

:::info
此功能需要 [Storage](../index.md) 软件包。
:::

## 创建子卷

创建子卷的主要好处是组织 Btrfs 主（根）子卷上的数据。可以将子卷视为具有分区功能的文件夹，同时所有子卷之间仍共享总磁盘空间。您之后可以将这些子卷用于更高级的任务，建议在拥有大量不同类型数据时创建子卷，尤其是需要频繁备份的数据。按照指南设置几个示例子卷：

:::tip
子卷在与快照结合使用时最为有用。请务必同时查看快照功能。

:::

1. 找到您要用作 Btrfs 磁盘的磁盘名称：

   ```routeros
   /disk/print
   ```

   :::warning
   在此示例中，使用的磁盘将被称为 `<disk-name-1>`，请确保用您实际的磁盘名称替换该占位符！
   :::
2. 将磁盘格式化为 Btrfs，此处为 `<disk-name-1>`：

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. 为 Btrfs 磁盘添加标签以便识别：

   ```routeros
   /disk/btrfs/filesystem/set [find where present-devs=<disk-name-1>] label=BtrfsDisk
   ```

4. 您也可以更改 Btrfs 磁盘的挂载点以便识别：

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsDisk
   ```

5. 在 `BtrfsDisk` 上创建一个名为 `Documents` 的新子卷：

   ```routeros
   /disk/btrfs/subvolume/add name=Documents fs=BtrfsDisk
   ```

   :::info
   子卷也是快照。您可能会在各种菜单中遇到这两个名称。简单来说，快照是在特定时间创建的子卷，包含该时间点的数据。
   :::
6. 在 `BtrfsDisk` 上创建另一个名为 `Photos` 的子卷：

   ```routeros
   /disk/btrfs/subvolume/add name=Photos fs=BtrfsDisk
   ```

7. 您可以查看当前可用的子卷：

   ```routeros
   /disk/btrfs/subvolume/print
   ```

8. 您现在可以通过 `/BtrfsDisk/Documents` 和 `/BtrfsDisk/Photos` 访问这些子卷。

## 创建快照

快照是一种节省空间的数据备份方式。通过创建快照，您可以保存数据的当前状态，之后可以随时访问。

:::warning

快照不会创建数据的副本，它们保存数据的当前状态，同时允许您对当前数据进行更改。快照包含如何将当前数据恢复到创建快照时状态的信息。快照不会像完整备份那样创建数据的多个副本。

:::

:::note

虽然您可以创建根子卷的快照，但建议为数据创建新的子卷，然后使用快照功能。这只是在管理多个快照时的一种偏好。

:::

1. 创建子卷（或使用根子卷，见上文）并将数据放入这些子卷中，例如：

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos 
    3 BtrfsDisk/Documents/document1.txt
    4 BtrfsDisk/Photos/photo1.jpg
   ```

2. 在此示例中，我们创建了 `/BtrfsDisk/Documents` 和 `/BtrfsDisk/Photos/` 子卷，您可以通过以下命令查看它们：

   ```routeros
   /disk/btrfs/subvolume/print
   ```

3. 为了使快照更有组织性，创建一个名为 `Snapshots` 的新子卷：

   ```routeros
   /disk/btrfs/subvolume/add name=Snapshots fs=BtrfsDisk
   ```

4. 为 `Documents` 和 `Photos` 创建快照：

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-22012025
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-22012025
   ```

5. 您现在应该拥有只读的新子卷，其中包含您的文件：

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME      
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Photos/photo1.jpg
    6 BtrfsDisk/Snapshots/Documents-22012025
    7 BtrfsDisk/Snapshots/Photos-22012025
    8 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
    9 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

6. 出于测试目的，您可以向子卷添加更多数据，您应该会注意到新添加的文件不会出现在快照中，而只会出现在子卷中：

   ```routeros
   [admin@infra1.mikrotikls.lv] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg 
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-22012025/document1.txt
   11 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   ```

7. 您现在可以创建新的快照：

   ```routeros
   /disk/btrfs/subvolume/add read-only=yes parent=Documents fs=BtrfsDisk  name=Snapshots/Documents-23012025 
   /disk/btrfs/subvolume/add read-only=yes parent=Photos fs=BtrfsDisk  name=Snapshots/Photos-23012025 
   ```

8. 创建新快照后，每个子卷将有 2 个快照。一个包含较旧的文件，另一个包含较旧和较新的文件：

   ```routeros
   [admin@MikroTik] > /file/print 
    # NAME   
    0 BtrfsDisk
    1 BtrfsDisk/Documents
    2 BtrfsDisk/Photos
    3 BtrfsDisk/Snapshots
    4 BtrfsDisk/Documents/document1.txt
    5 BtrfsDisk/Documents/document2.txt
    6 BtrfsDisk/Photos/photo1.jpg
    7 BtrfsDisk/Photos/photo2.jpg
    8 BtrfsDisk/Snapshots/Photos-22012025
    9 BtrfsDisk/Snapshots/Documents-22012025
   10 BtrfsDisk/Snapshots/Documents-23012025
   11 BtrfsDisk/Snapshots/Photos-23012025
   12 BtrfsDisk/Snapshots/Documents-22012025/document1.txt 
   13 BtrfsDisk/Snapshots/Documents-23012025/document1.txt
   14 BtrfsDisk/Snapshots/Documents-23012025/document2.txt
   15 BtrfsDisk/Snapshots/Photos-22012025/photo1.jpg
   16 BtrfsDisk/Snapshots/Photos-23012025/photo1.jpg
   17 BtrfsDisk/Snapshots/Photos-23012025/photo2.jpg
   ```

   :::note

   多个快照不会创建每个文件的多个副本，但如果某个文件已被删除且仍存在于快照中，则该已删除的文件将占用空间。如果某个文件存在于多个快照中，则仅占用 1 个文件的空间。

   :::
9. 如果您不再需要较旧的快照，可以将其删除：

   ```routeros
   /disk/btrfs/subvolume/remove [find where name=Documents-22012025]
   /disk/btrfs/subvolume/remove [find where name=Photos-22012025]
   ```

## 传输您的快照

Btrfs 允许您轻松地在两个使用 Btrfs 的设备之间发送快照。在此示例中，我们将使用两台运行 Storage 软件包的 RouterOS 设备。包含需要备份的快照的 RouterOS 设备将被称为 `RouterA`，接收备份的 RouterOS 设备将被称为 `RouterB`。

:::info

本指南仅展示如何在 RouterOS 设备之间使用 Btrfs 传输的示例，但您也可以在 RouterOS 和 Linux 设备之间传输快照。如果您需要此类功能，请务必查看您的 Linux 发行版文档，了解如何在其上使用 Btrfs 传输。

:::

:::tip

本指南将在同一台 RouterOS 设备上使用 SSH 主机密钥作为 SSH 用户密钥。如果您希望为 SSH 用户使用自己的密钥，则可以在 Linux 计算机上使用以下命令，然后通过 `/user/ssh-keys` 导入密钥对：

```routeros
openssl genpkey -outform PEM -out btrfstransfer_key.pem -algorithm ED25519
openssl pkey -in btrfstransfer_key.pem -pubout -out btrfstransfer_key_pub.pem
```

:::

1. 可选：提高 SSH 服务器的安全级别，在 `RouterA` 和 `RouterB` 上运行以下命令：

   ```routeros
   /ip/ssh/set host-key-type=ed25519 strong-crypto=yes
   /ip/ssh/regenerate-host-key
   ```

   :::warning

   重新生成主机密钥后，下次尝试通过 SSH 连接到 RouterOS 设备时会出现错误消息。您需要调整 SSH 客户端的配置（通常在 `~/.ssh/known_hosts` 中）以信任新的主机密钥。

   :::
2. 在 `RouterA` 上导出 SSH 私钥和公钥：

   ```routeros
   /ip/ssh/export-host-key key-file-prefix=admin
   ```

3. 在 `RouterA` 上为用户 `admin` 导入 SSH 私钥：

   ```routeros
   /user/ssh-keys/private/import private-key-file=admin_ed25519.pem user=admin
   ```

4. 将 `RouterA` 的 SSH 公钥上传到 `RouterB`：

   ```routeros
   /file/sync/add local-path=admin_ed25519_pub.pem remote-address=RouterB user=admin mode=upload
   /file/sync/remove [find where local-path=admin_ed25519_pub.pem]
   ```

5. 在 `RouterB` 上创建一个新用户，例如 `btrfstransfer`，并为其设置安全密码：

   ```routeros
   /user/add name=btrfstransfer group=write
   ```

   :::warning

   虽然密码不会用于 Btrfs 传输功能，但您仍然需要使用安全密码以防止未经授权访问您的设备。

   :::
6. 在 `RouterB` 上导入上传的 SSH 公钥，并将其设置为用户 `btrfstransfer`：

   ```routeros
   /user/ssh-keys/import public-key-file=admin_ed25519_pub.pem user=btrfstransfer
   ```

7. 在 `RouterA` 上设置类型为 `send`：

   ```routeros
   /disk/btrfs/transfer/add type=send fs=BtrfsDisk ssh-address=RouterB send-subvolumes=Documents-23012025 ssh-user=btrfstransfer ssh-receive-mount=BackupBtrfsDisk/Snapshots
   ```

   其中：
   - `BtrfsDisk` 是在 `RouterA` 上通过 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁盘标签。
   - `Documents-23012025` 是快照名称（不是路径）。
   - `btrfstransfer` 是 `RouterB` 上的 SSH 用户。
   - `BackupBtrfsDisk` 是在 `RouterB` 上通过 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁盘标签。
   - `Snapshots` 是 `BackupBtrfsDisk` 下用于存放快照的子卷。
8. 在 `RouterB` 上设置类型为 `receive`：

   ```routeros
   /disk/btrfs/transfer/add fs=BackupBtrfsDisk type=receive file=BackupBtrfsDisk/Snapshots
   ```

   其中：
   - `BackupBtrfsDisk` 是在 `RouterB` 上通过 `/disk/btrfs/filesystem/print` 找到的 Btrfs 磁盘标签。
   - `BackupBtrfsDisk/Snapshots` 是 `Snapshots` 子卷的挂载路径。