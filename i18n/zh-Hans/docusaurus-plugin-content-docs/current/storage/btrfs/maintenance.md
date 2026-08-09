# Btrfs 维护

> 本页涵盖 Btrfs 维护任务，包括定期清理（scrubbing）以检测并纠正 RAID 阵列中的数据损坏、平衡（balancing）以优化存储空间使用，以及创建快照用于数据恢复。文中提供了建议的执行间隔、示例命令以及关于存储设备健康的警告。

# Btrfs 维护

:::info
此功能需要 [Storage](../index.md) 软件包。
:::

与其他功能丰富的文件系统类似，Btrfs 也需要定期维护。本页涵盖与 Btrfs 相关的常规任务。

## 定期清理（Scrubbing）

在 RAID 阵列中，您的数据存储在多个磁盘上，或者多个磁盘包含如何重新组装数据的信息。如果没有 RAID，磁盘在极少数情况下可能会损坏您数据的几个字节，而您甚至可能不会注意到数据已被损坏。使用 RAID 阵列时，当您读取文件时，数据会与其他数据副本进行比较（或在组装时进行检查），并会提醒您数据已损坏。对于[常规 RAID](../raid/index.md)，例如在 RAID1 配置中，RAID 阵列无法判断哪个文件副本是正确的。它只会通知您检测到了数据损坏。而使用 Btrfs RAID，您不仅能检测到数据损坏，还能通过校验和区分哪个文件副本是正确的，并自动恢复它。

清理（Scrubbing）是一个重新读取整个 RAID 阵列的过程，在 Btrfs RAID 的情况下，它会纠正任何数据损坏。虽然 Btrfs RAID 会在文件读取操作时纠正数据（例如，当您想从 RouterOS 设备下载文件时），但强烈**不**建议避免清理。在极少数情况下，例如在 RAID1 配置中，两个磁盘都可能包含损坏的数据，而 Btrfs RAID 可能无法恢复数据。为避免此类情况并保护重要数据，请考虑定期运行清理。

:::warning

检测到过多数据损坏通常表明存储设备正在出现故障。当您注意到大量数据损坏警告时，请考虑检查存储设备。

:::

清理运行的频率取决于具体的使用场景。清理对存储设备来说是一项高负载任务。它会重新读取整个 RAID 阵列并执行额外检查。在清理期间，您可能会注意到磁盘性能明显下降，直到清理完成。如果您担心清理期间的性能，请考虑降低清理频率。如果您更担心数据完整性，请考虑提高清理频率。

- 摘要：用于检测并纠正数据损坏
- 建议间隔：1 周
- [工作示例](./raid.md#creating-btrfs-raid-check)

示例命令：

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/scrub-start 0
```

您也可以使用以下命令取消清理：

```routeros
/disk/btrfs/filesystem/scrub-cancel
```

## 定期平衡（Balance）

在 Btrfs 中，数据存储在已分配的块（chunks）中，这些块随后允许将数据存储在数据块中。随着时间的推移，由于各种数据活动，块可能会变得部分已满，并以次优方式分布在多个块之间。平衡 Btrfs 文件系统意味着重新排列这些块中的数据，并恢复未分配的空间。这样，您可以恢复丢失的可用空间并提升 Btrfs 文件系统的性能。这与其他文件系统上的碎片整理操作有些类似。

平衡的一个重要参数是 `data-usage` 参数。这是一个过滤器，可防止平衡功能处理使用率超过特定百分比的块。例如，`data-usage=50` 将仅处理使用率为 50% 或更低的块。您可以使用不同的值多次运行平衡命令，从而减少每次平衡操作所需的时间。平衡可能是一项高负载任务，具体取决于您的可用空间以及自上次平衡操作以来数据的写入方式，因此，您可能会受益于使用不同的 `data-usage` 值分别运行平衡命令，以减少平衡因密集磁盘读写而导致性能下降的时间窗口。

如果您想分别运行平衡命令，应使用 `data-usage` 值为 25、50、75 和 90。不建议超过 90%。对于大多数用户来说，无需分别运行平衡命令，每个间隔使用 `data-usage` 为 50% 运行一次即可。

- 摘要：用于恢复可用空间并提升性能。
- 建议间隔：每月两次。
- 建议 `data-usage`：50。
- [工作示例](./raid.md#creating-btrfs-raid-check)。

示例命令：

```routeros
/disk/btrfs/filesystem/print
/disk/btrfs/filesystem/balance-start data-usage=50 0
```

您也可以使用以下命令取消平衡：

```routeros
/disk/btrfs/filesystem/balance-cancel
```

## 定期快照

快照可用于按设定间隔保存文件更改。当您有可靠的数据复制间隔时，快照最为有用，这样您可以随时将数据恢复到之前的状态。以下是一个可直接使用的脚本，用于创建定期快照：

```routeros
/system/scheduler
add interval=1d name=BraidSnapshotStartCall on-event=BraidSnapshotStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:15:00
add interval=1d name=BraidSnapshotCleanUpStartCall on-event=BraidSnapshotCleanUpStart policy=ftp,read,write,policy,test,sniff start-date=1970-01-01 start-time=23:00:00
add interval=3m name=SystemBackupStartCall on-event=SystemBackupStart policy=ftp,read,write,policy,test,sniff start-time=startup

/system/script
add dont-require-permissions=no name=SystemBackupStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global systembackupstatuscheck;\
    \n:global systembackupdirectoryname; \
    \n:local sysadmin;\
    \n\
    \n:set \$sysadmin ( \$sysadmin \"servername@domain.tld\" );\
    \n:set \$systembackupdirectoryname (\$systembackupdirectoryname \"Braid17-20/@system-backup/\");\
    \n\
    \n if (\$systembackupstatuscheck != \"started\") do={\
    \n         :set \$systembackupstatuscheck (\$systembackupstatuscheck \"started\");\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n               :local servername ([/system/identity/get name]);\
    \n               /system/backup/save name=\"\$systembackupdirectoryname\$servername-\$datentime\";\
    \n\
    \n        :set \$systembackupstatuscheck (\$systembackupstatuscheck \"done\");\
    \n} else={\
    \n         /log/info message=\"ERROR: Cannot create  \$systembackupdirectoryname\$servername-\$datentime. Set manually :set systembackupstatuscheck (systembackupstatuscheck \\\"done\\\");\";\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxusedspace;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxusedspace ( \$maxusedspace 80 );\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local valueofusedspace [/disk/print count-only where use>=\$maxusedspace and fs-label=\$temp];\
    \n           if ( \$valueofusedspace=0) do={\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level!=\$snapshotdirectoryname and fullname!=\$snapshotdirectoryname ] do={\
    \n               :local parentvar [ /disk/btrfs/subvolume/get value-name=name \$j; ];\
    \n               :local datentime ([/system/clock/get date].\"-\".[/system/clock/get time]);\
    \n                  /disk/btrfs/subvolume/add read-only=yes fs=\"\$temp\" parent=\"\$parentvar\" name=\"\$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                   /log/info message=\"INFO: Braid snapshot created for  \$temp subvolume \$parentvar snapshotname  \$snapshotdirectoryname/\$temp-\$parentvar-\$datentime\";\
    \n                :delay 1;\
    \n            }\
    \n          } else={\
    \n                   /log/info message=\"ERROR: Snapshot was not created for safety reason.  Braid array \$temp used space exceeded \$maxusedspace %. Add more disks or cleanup storage.\"; \
    \n                   /tool/e-mail/send to= \$sysadmin  subject=([/system/identity/get name].\" ERROR: Braid snapshot was not created \") body=(\"Snapshot was not created for safety reason.  Braid array \" .\$temp. \" used space exceeded \" .\$max\
    usedspace. \" % Add more disks or cleanup storage. \" );\
    \n          }\
    \n\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotstatuscheck (\$btrfssnapshotstatuscheck \"done\");\
    \n}\
    \n"
add dont-require-permissions=no name=BraidSnapshotCleanUpStart owner=admin policy=ftp,read,write,policy,test,sniff source=":global btrfssnapshotcleanupstatuscheck;\
    \n:global snapshotdirectoryname; \
    \n:local maxsnapshotstokeep;\
    \n:local maxdaysoldsnapshotstokeep;\
    \n:local sysadmin;\
    \n\
    \n:set \$maxsnapshotstokeep ( \$maxsnapshotstokeep 10);\
    \n:set \$maxdaysoldsnapshotstokeep (\$maxdaysoldsnapshotstokeep \"10d\");\
    \n:set \$sysadmin ( \$sysadmin \"<servername@domain.tld>\" );\
    \n:set \$snapshotdirectoryname (\$snapshotdirectoryname \"@snapshots\");\
    \n\
    \n if (\$btrfssnapshotcleanupstatuscheck != \"started\") do={\
    \n         :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"started\");\
    \n         foreach i in=[/disk/btrfs/filesystem/find] do={ \
    \n           :local temp [ /disk/btrfs/filesystem/get value-name=label \$i;]\
    \n           :local currenttimestamp; :set  \$currenttimestamp ( \$currenttimestamp [/system/clock/get date ] );\
    \n          :set  \$currenttimestamp ( \$currenttimestamp  -\$maxdaysoldsnapshotstokeep);\
    \n            foreach j in=[/disk/btrfs/subvolume/find  where fs=\$temp and top-level=\$snapshotdirectoryname ] do={\
    \n               :local parentname [ /disk/btrfs/subvolume/get value-name=name \$j;];\
    \n               :local parentsubvol [ /disk/btrfs/subvolume/get value-name=parent \$j; ];\
    \n               :local creationtimeofsnapshot; :set \$creationtimeofsnapshot (\$creationtimeofsnapshot [/disk/btrfs/subvolume/get value-name=creation-time \$j; ]);\
    \n               :local countparentsnapshots;  :set \$countparentsnapshots (\$countparentsnapshots [/disk/btrfs/subvolume/print count-only  where fs=\$temp and top-level=\$snapshotdirectoryname and parent=\$parentsubvol]);\
    \n               if ([:len \$parentsubvol]=0) do={\
    \n                   :local parentfullname [ /disk/btrfs/subvolume/get value-name=fullname \$j;];\
    \n                    /log/info message=\"INFO: SnapshotCleanup found snapshot of completely deleted subvolume. Location of snapshot \$temp/\$snapshotdirectoryname/\$parentname. This can only be removed manually.\";\
    \n               } else={\
    \n                if (\$currenttimestamp>=\$creationtimeofsnapshot or  \$countparentsnapshots>\$maxsnapshotstokeep ) do={\
    \n                   /log/info message=\"INFO: Braid snapshot  \$snapshotdirectoryname/\$parentname deleted. SnapshotCleanUp keeps  \$maxsnapshotstokeep snapshots or snapshots not older than \$maxdaysoldsnapshotstokeep days.\";\
    \n                  /disk/btrfs/subvolume/remove \$parentname;\
    \n                :delay 1;\
    \n               }\
    \n             }\
    \n            }\
    \n          :delay 3; \
    \n         }\
    \n        :set \$btrfssnapshotcleanupstatuscheck (\$btrfssnapshotcleanupstatuscheck \"done\");\
    \n}\
    \n"
```

## 可用空间

在 Btrfs 中，由于数据存储在块中的方式，确保有足够的可用空间不仅对于常规维护任务的正常运行很重要，而且对于文件系统的最佳性能也很重要。为确保您的 Btrfs 文件系统正常工作，请考虑检查 Btrfs 文件系统上是否有足够的可用空间。可用空间的最佳值为 10%，但您不应让 Btrfs 文件系统的可用空间降至 5% 以下。

- 摘要：不要让 Btrfs 文件系统完全占满。
- 建议可用空间：5-10%。

## 示例命令

```routeros
/disk/btrfs/filesystem/print
```

:::tip

如果您需要更多空间，请考虑将磁盘添加到包含一个或多个磁盘的 Btrfs RAID 阵列中。

:::