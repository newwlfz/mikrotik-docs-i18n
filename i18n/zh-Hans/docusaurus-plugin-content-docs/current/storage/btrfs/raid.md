# Btrfs RAID

> 本页面提供在 MikroTik RouterOS 中使用两块磁盘设置 Btrfs RAID1 阵列的分步说明，涵盖磁盘准备、格式化、添加设备、数据平衡以及确保 RAID 配置一致性等内容。

# Btrfs RAID

:::info
此功能需要 [Storage](../index.md) 软件包。
:::

## 双磁盘 Btrfs-RAID（RAID1）

如果您希望仅使用两块磁盘（例如 NAS）创建可靠的数据存储解决方案，可以按照以下步骤成功创建 Btrfs RAID1 阵列：

1. 查找您要用于设置 Btrfs-RAID 的磁盘名称。

   ```routeros
   /disk/print
   ```

   :::warning
   在本示例中，所使用的磁盘将被称为 `<disk-name-1>` 和 `<disk-name-2>`，请确保将这些占位符替换为您实际的磁盘名称！
   :::
2. 将其中一块磁盘格式化为 Btrfs，此处为 `<disk-name-1>`。

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

3. 您可以使用以下命令检查 Btrfs 磁盘的当前状态。

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   如果您的磁盘上存在旧的 RAID 配置，并且希望简化操作以移除任何过时的配置，则可以使用 `/disk/format <disk-name-x> file-system=wipe-quick` 擦除磁盘。当 `/disk/btrfs/filesystem/print` 下存在不需要的条目时，此操作非常有用。
   :::
4. 为 Btrfs 驱动器添加标签以简化操作。

   ```routeros
   /disk/btrfs/filesystem/set [find where present-devs=<disk-name-1>] label=BtrfsRAID
   ```

5. 向现有的 Btrfs 磁盘添加一块磁盘。

   ```routeros
   /disk/btrfs/filesystem/add-device [find where present-devs=<disk-name-1>] device=<disk-name-2>
   ```

6. 启动 Btrfs 平衡过程，以创建具有 RAID1 配置的 Btrfs-RAID。

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid1 metadata-profile=raid1 system-profile=raid1
   ```

7. **重要提示：** 仔细检查所有磁盘的 Btrfs 配置是否匹配。在这种情况下，您需要确保 `data`、`meta` 和 `system` 配置均为 `raid1`。

   ```routeros
   /disk/btrfs/filesystem/print
   ```

    :::danger
    如果您在输出中注意到例如 `data,single:1`，则需要重新执行 `/disk/btrfs/filesystem/balance-start` 命令。
    :::

   :::info
    理想状态是输出类似于以下内容，其中 `data`、`system` 和 `meta` 的 Btrfs 配置均设置为 `raid1`：

   ```routeros
   > /disk/btrfs/filesystem/print
   ...
   data,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%                                                                                                       
   system,raid1:33.6MB disk1:33.6MB disk2:33.6MB, used:0%                                                                                                     
   meta,raid1:1.07GB disk1:1.07GB disk2:1.07GB, used:0%    
   ```

   :::

   :::tip
   使用 [BtrfsRAIDCheck](#creating-btrfs-raid-check) 脚本提醒您 Btrfs 配置不一致的情况！
   :::
8. 为第二块磁盘设置 `mount-filesystem=no`，以防止文件重复显示。

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   ```

   :::info
   Btrfs 具有一项功能，允许您挂载任何 Btrfs-RAID 成员，并且仍然可以访问整个 Btrfs-RAID 阵列。此功能的一个缺点是，如果您将同一阵列挂载两次，则文件也会出现两次。为防止这种情况，您可以简单地禁用其中一个 Btrfs-RAID 成员的自动挂载。
   :::
9. 您也可以更改挂载点的名称以简化操作。

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

10. 您新创建的 Btrfs-RAID 阵列现在可以通过 `/BtrfsRAID/` 文件夹访问。

在拥有 Btrfs-RAID 等可靠存储解决方案后，请考虑按照以下建议指南为您的 RouterOS 设备添加实用功能：

- 运行您自己的 [Containers](../../containers/index.md)
- [DLNA 媒体服务器](../dlna.md)
- [SMB 服务器](../smb.md)
- [NFS 服务器](../nfs.md)

:::warning
当常规 [RAID](../raid/index.md) 与 Btrfs 文件系统一起使用时，您的 RAID 阵列将无法从 Bitrot 中自愈，常规 RAID 只能检测 Bitrot。建议在可能的情况下使用 Btrfs-RAID（本节所述的配置）。
:::

## 四磁盘 Btrfs-RAID（RAID10）

如果您希望使用 Btrfs 创建冗余且高容量的 RAID10 阵列，请按照以下命令操作：

1. 查找您要用于设置 Btrfs-RAID 的磁盘名称。

```routeros
/disk/print
```

   :::warning
   在本示例中，所使用的磁盘将被称为 `<disk-name-1>,``<disk-name-2>, <disk-name-3> 和 <disk-name-4>`，请确保将这些占位符替换为您实际的磁盘名称！
   :::

1. 将其中一块磁盘格式化为 Btrfs，此处为 `<disk-name-1>`：

   ```routeros
   /disk/format <disk-name-1> file-system=btrfs
   ```

2. 您可以使用以下命令检查 Btrfs 磁盘的当前状态：

   ```routeros
   /disk/btrfs/filesystem/print
   ```

   :::info
   如果您的磁盘上存在旧的 RAID 配置，并且希望简化操作以移除任何过时的配置，则可以使用 `/disk/format <disk-name-x> file-system=wipe-quick` 擦除磁盘。当 `/disk/btrfs/filesystem/print` 下存在不需要的条目时，此操作非常有用。
   :::
3. 为 Btrfs 驱动器添加标签以简化操作：

   ```routeros
   /disk/btrfs/filesystem/set [find where present-devs=<disk-name-1>] label=BtrfsRAID
   ```

4. 向现有的 Btrfs 磁盘添加其他磁盘：

   ```routeros
   /disk/btrfs/filesystem/add-device [find where present-devs=<disk-name-1>] device=<disk-name-2>
   /disk/btrfs/filesystem/add-device [find where present-devs=<disk-name-1>] device=<disk-name-3>
   /disk/btrfs/filesystem/add-device [find where present-devs=<disk-name-1>] device=<disk-name-4>
   ```

5. 启动 Btrfs 平衡过程，以创建具有 RAID10 配置的 Btrfs-RAID：

   ```routeros
   /disk/btrfs/filesystem/balance-start [find where label=BtrfsRAID] data-profile=raid10 metadata-profile=raid1c4 system-profile=raid1c4
   ```

   :::info
   `data-profile`、`metadata-profile` 和 `system-profile` 有许多可能的配置。对于 RAID10 阵列，建议对 `system-profile` 和 `metadata-profile` 使用 `raid1c3` 或 `raid1c4`。`raid1c4` 配置将在不同磁盘上存储 4 份数据副本。这使得数据更加冗余，但会占用更多磁盘空间。
   :::

   :::danger
   不支持 Btrfs RAID5 和 RAID6。如果您需要此类 RAID 配置，请使用 [常规 RAID](../raid/index.md)。请注意，在 Btrfs 上使用 [常规 RAID](../raid/index.md) 时，您将无法获得 bit-rot 保护。
   :::

   :::warning
   对于大多数使用场景，请将 `metadata-profile` 设置为与 `system-profile` 相同的值。避免为这两个配置使用不同的值。
   :::
6. 为其他磁盘设置 `mount-filesystem=no`，以防止文件重复显示：

   ```routeros
   /disk/set <disk-name-2> mount-filesystem=no
   /disk/set <disk-name-3> mount-filesystem=no
   /disk/set <disk-name-4> mount-filesystem=no
   ```

7. 您也可以更改挂载点的名称以简化操作：

   ```routeros
   /disk/set <disk-name-1> mount-point-template=BtrfsRAID
   ```

8. 您新创建的 Btrfs-RAID 阵列现在可以通过 `/BtrfsRAID/` 文件夹访问。

## 替换 Btrfs RAID 阵列中的磁盘

如果发生磁盘故障或您需要替换现有 Btrfs RAID 阵列中的磁盘，请按照以下步骤操作：

1. 确保您确定需要替换的正确磁盘。使用 `/disk/print detail` 和 `/disk/blink` 来确定正确的磁盘。我们假设故障磁盘为 `disk2`。
2. 弹出故障磁盘：

   ```routeros
   /disk/eject disk2
   ```

3. 物理移除故障磁盘。
4. 打印当前 Btrfs RAID 阵列的状态：

   ```routeros
   /disk/btrfs/filesystem/print
   ```

5. 在命令输出中查找缺失磁盘的 `DEV-ID`：

   ```routeros
   [admin@MikroTik] /disk> /disk/btrfs/filesystem/print
   Flags: I - MISSING-DEVS
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   #   LABEL      DEV-IDS  DEVS     DEFAULT-SUBVOLUME  SPACES                                     BALANCE-STATUS  UUID                                  W  R  F  C  G
   0 I BtrfsRAID        1  disk1    <FS_ROOT>          disk1:480GB, used:0%                       done            9246dfaa-be9f-4e08-a560-53cb8e82023b  0  0  0  0  0
                        2  missing                     data,raid1:1.07GB disk1:1.07GB, used:0%                                                          0  0  0  0  0
                                                       data,single:1.07GB, used:0%                                                                                   
                                                       system,raid1:33.6MB disk1:33.6MB, used:0%                                                                     
                                                       meta,raid1:1.07GB disk1:1.07GB, used:0%                                                                       
                                                       global-reserve:3.41MB, used:0%                                                                                

   ```

   :::info
   在这种情况下，缺失磁盘的 `DEV-ID` 为 "2"。
   :::
6. 插入新磁盘。
7. 确定新磁盘的名称：

   ```routeros
   /disk/print
   ```

   :::info
   在这种情况下，新磁盘的名称为 `disk3`
   :::
8. 运行以下命令以替换 Btrfs RAID 阵列中的磁盘：

   ```routeros
   /disk/btrfs/filesystem/replace-device device-to-remove-id=2 device-to-add=disk3 BtrfsRAID
   ```

   :::warning
   确保您将正确的 `device-to-remove-id` 设置为之前确定的 `DEV-ID`！
   :::
9. 检查替换状态，并确保 `REPLACE-STATUS` 标记为 `done`。

   ```routeros
   > /disk/btrfs/filesystem/print
   Columns: LABEL, DEV-IDS, DEVS, DEFAULT-SUBVOLUME, SPACES, BALANCE-STATUS, REPLACE-STATUS, UUID, WRITE-ERRORS, READ-ERRORS, FLUSH-ERRORS, CORRUPTION-ERRORS, GENERATION-ERRORS
   # LABEL   DEV-IDS  DEVS   DEFAULT-SUBVOLUME  SPACES                                                 BALANCE-STATUS  REPLACE-STATUS  UUID                                  WRITE-ERRORS  READ-ERRORS  F  C  G
   0 BtrfsRAID     1  disk1  <FS_ROOT>          disk1:480GB, used:9%                                   done            done            9246dfaa-be9f-4e08-a560-53cb8e82023b             0            0  0  0  0
                   2  disk3                     disk3:480GB, used:9%                                                                                                                    0            0  0  0  0
                                                data,raid1:40.8GB disk1:40.8GB disk3:40.8GB, used:72%                                                                                                          
                                                system,raid1:101MB disk1:101MB disk3:101MB, used:0%                                                                                                            
                                                meta,raid1:3.22GB disk1:3.22GB disk3:3.22GB, used:1%                                                                                                           
                                                global-reserve:30.7MB, used:0%                                                 
   ```

   :::info
   确保您的 Btrfs RAID 阵列在 `data`、`system` 或 `meta` 方面没有不一致的 Btrfs 配置。所需的配置将取决于您的具体设置。对于 RAID1 设置，您很可能希望这些配置匹配，但在 RAID10 设置中，这些值可以不同。在任何 RAID 设置中，`data`、`system` 或 `meta` 都不应存在 `single` 配置。
   :::

## 创建 Btrfs-RAID 检查

监控 Btrfs-RAID 阵列的健康状况至关重要。您可以使用以下脚本作为工作示例来实现此目的：

```routeros
/system/scheduler
add interval=1w30s name=BraidBalanceStartCall on-event=BraidBalanceStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=01:00:00
add interval=1w30s name=BraidScrubStartCall on-event=BraidScrubStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=02:00:00
add interval=2m name=BraidBalanceStatusCheckCall on-event=BraidBalanceStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidScrubStatusCheckCall on-event=BraidScrubStatus policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=30s name=BraidHealthCheckCall on-event=BraidHealthCheck policy=ftp,read,write,policy,test,sniff start-time=startup
add interval=2m name=BraidReplaceStatusCheckCall on-event=BraidReplaceStatus policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=BraidScrubStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck != \"started\") do={\
    \n  :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"started\");\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/scrub-start \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs scrub process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}\
    \n"
add dont-require-permissions=no name=BraidBalanceStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck != \"started\") do={\
    \n:set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n:local percentage;\
    \n:set \$percentage (\$percentage 50);\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ /disk/btrfs/filesystem/balance-start data-usage=\$percentage \$i;\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    /log/info message=\"INFO: Btrfs balance process started on  \$temp\";\
    \n    :delay 3; \
    \n  }\
    \n}"
add dont-require-permissions=no name=BraidBalanceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsbalancestatuscheck;\
    \nif (\$btrfsbalancestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=balance-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n        /log/info message=\"INFO: Btrfs current balance status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsbalancestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs balancing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt) do={\
    \n      /log/info message=\"INFO: Btrfs array balance status on  \$temp is \$barray \";\
    \n      :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidScrubStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsscrubstatuscheck;\
    \nif (\$btrfsscrubstatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=scrub-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    if ( \$barray != \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current scrub status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsscrubstatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs scrubbing already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array scrub status on  \$temp is \$barray \";\
    \n      :set \$btrfsscrubstatuscheck (\$btrfsscrubstatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}"
add dont-require-permissions=no name=BraidReplaceStatus owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfsreplacestatuscheck;\
    \nif (\$btrfsreplacestatuscheck = \"started\") do={\
    \n:local arraycnt [/disk/btrfs/filesystem/print count-only as-value];\
    \n:local counter [:set \$counter (\$counter 0)];\
    \n:local counterdiff [:set \$counterdiff (\$counterdiff 0)];\
    \n  foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n    :local barray [ /disk/btrfs/filesystem/get value-name=replace-status  \$i;]\
    \n    :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n    :local multipleprofiles [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n    if ( \$barray ~ \"working\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      /log/info message=\"INFO: Btrfs current replace status on  \$temp is \$barray\";\
    \n    }\
    \n    if ( \$barray ~ \"done\" and \$btrfsreplacestatuscheck = \"started\" and \$multipleprofiles~\"single\" ) do={\
    \n      /log/info message=\"INFO: Braid balance after replace-device  started on  \$temp\";\
    \n         if (\$btrfsbalancestatuscheck!=\"started\") do={\
    \n             /disk/btrfs/filesystem/balance-start \$temp;\
    \n             :set \$btrfsbalancestatuscheck (\$btrfsbalancestatuscheck \"started\");\
    \n         }\
    \n    }\
    \n    if ( \$barray = \"done\" and \$btrfsreplacestatuscheck = \"started\") do={\
    \n      :set \$counter (\$counter +1);\
    \n      :set \$counterdiff (\$arraycnt - \$counter);\
    \n      if (\$counterdiff =1) do={\
    \n        /log/info message=\"INFO: Btrfs replace already done on \$counter arrays\";\
    \n      }\
    \n    }\
    \n    if ( \$counter = \$arraycnt ) do={\
    \n      /log/info message=\"INFO: Btrfs array replace status on  \$temp is \$barray \";\
    \n      :set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"done\");\
    \n    }\
    \n  } \
    \n}\
    \n:set \$btrfsreplacestatuscheck (\$btrfsreplacestatuscheck \"started\");"
add dont-require-permissions=no name=BraidHealthCheck owner=admin policy=ftp,read,write,policy,test,sniff source="foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n:local sysadmin; \
    \n\
    \n:set  \$sysadmin \"<servername@domain.tld>\";\
    \n\
    \n:local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n:local haserror [/disk/btrfs/filesystem/get value-name=about \$i; ]\
    \n:local hasmissing [ /disk/btrfs/filesystem/get value-name=devs \$i; ]\
    \n:local hasmultiprofile [ /disk/btrfs/filesystem/get value-name=spaces \$i; ]\
    \n:local replacestatus [ /disk/btrfs/filesystem/get value-name=replace-status \$i; ]\
    \n:local multiplediskarray [:len [/disk/btrfs/filesystem/find where label=\$temp and dev-ids~\"2\"];]\
    \n\
    \n  if ( \$hasmissing~\"missing\" and ([:len \$replacestatus]=0)) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found missing array member on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found missing array member\") body=(\"Btrfs array where found missing array member on \" .\$temp . \"   \");\
    \n   :delay 19; \
    \n  }\
    \n\
    \n  if ( \$multiplediskarray > 0 and \$hasmultiprofile~\"single\") do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found multiprofile on \$temp array. To start balance process, run  /disk/btrfs/filesystem/balance-start \$temp command \";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found multiprofile on \" .\$temp. \" array.\") body=(\"Btrfs array where found with multiprofile status on \" .\$temp . \"To start balance process, run once\
    \_ /disk/btrfs/filesystem/balance-start \" .\$temp. \" command \");\
    \n   :delay 19; \
    \n  }  \
    \n\
    \n  if (([:len \$haserror]) > 0 ) do= {\
    \n    /log/info message=\"ERROR: BtrfsHealthCheck found errors on \$temp\";\
    \n    /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" BtrfsHealthCheck found errors\") body=(\"Btrfs array where found errors on \" .\$temp . \"   \");\
    \n    :delay 20; \
    \n  }\
    \n}\
    \n"
```

您还需要在 RouterOS 设备上调整电子邮件服务器设置：

```routeros
/tool/e-mail
set from=<raidcheck@domain.tld> port=587 server=smtp.domain.com tls=starttls
```

:::warning
确保您根据电子邮件服务器的要求调整电子邮件设置。请记得调整上述脚本中的电子邮件地址。
:::