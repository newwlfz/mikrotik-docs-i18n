# disk

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# disk

**条件:** !smips
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled">已禁用</ArgTableRow>
<ArgTableRow arg="A" typ="acquired">已获取</ArgTableRow>
<ArgTableRow arg="E" typ="empty">空</ArgTableRow>
<ArgTableRow arg="B" typ="block-device">块设备</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">已挂载</ArgTableRow>
<ArgTableRow arg="F" typ="formatting">正在格式化</ArgTableRow>
<ArgTableRow arg="S" typ="swap-enabled">已启用交换</ArgTableRow>
<ArgTableRow arg="f" typ="raid-member-failed">RAID成员故障</ArgTableRow>
<ArgTableRow arg="r" typ="raid-member">RAID成员</ArgTableRow>
<ArgTableRow arg="c" typ="encrypted">已加密</ArgTableRow>
<ArgTableRow arg="g" typ="guid-partition-table">GPT分区表</ArgTableRow>
<ArgTableRow arg="p" typ="partition">分区</ArgTableRow>
<ArgTableRow arg="t" typ="nvme-tcp-export">NVMe-TCP导出</ArgTableRow>
<ArgTableRow arg="i" typ="iscsi-export">iSCSI导出</ArgTableRow>
<ArgTableRow arg="s" typ="smb-sharing">SMB共享</ArgTableRow>
<ArgTableRow arg="n" typ="nfs-sharing">NFS共享</ArgTableRow>
<ArgTableRow arg="m" typ="media-sharing">媒体共享</ArgTableRow>
<ArgTableRow arg="L" typ="self-encrypted-and-locked">自加密且已锁定</ArgTableRow>
<ArgTableRow arg="O" typ="self-encryption-enabled">已启用自加密</ArgTableRow>
<ArgTableRow arg="o" typ="self-encryption-supported">支持自加密</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="枚举 (raid | nvme-tcp | iscsi | nfs | smb | partition | tmpfs | ramdisk | crypted | sshfs | file | hardware)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="slot" typ="字符串"></ArgTableRow>
<ArgTableRow arg="parent" typ="枚举 ()"></ArgTableRow>
<ArgTableRow arg="mount-point-template" typ="字符串"></ArgTableRow>
<ArgTableRow arg="mount-filesystem" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="mount-read-only" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="compress" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="partition-number" typ="数字"></ArgTableRow>
<ArgTableRow arg="partition-offset" typ="数字"></ArgTableRow>
<ArgTableRow arg="partition-size" typ="数字"></ArgTableRow>
<ArgTableRow arg="raid-type" typ="枚举 (0 | 1 | 4 | 5 | 6 | linear | faulty)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-device-count" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-max-component-size" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-chunk-size" typ="枚举 (64K | 128K | 256K | 512K | 1M | 2M | 4M)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-master" typ="枚举 (none)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-role" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-member-failed" typ="布尔值 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-export" typ="布尔值" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-port" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-nqn" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-allow-host-name" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-password" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-address" typ="IP地址 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-nqn" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-host-name" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-password" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-port" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-export" typ="布尔值" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-server-port" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-server-iqn" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-port" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-address" typ="IP地址 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-iqn" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-sharing" typ="布尔值" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-address" typ="IP地址 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-share" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="smb-sharing" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="smb-server-user" typ="枚举 ()"></ArgTableRow>
<ArgTableRow arg="smb-server-password" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="smb-server-encryption" typ="布尔值 {  }"></ArgTableRow>
<ArgTableRow arg="smb-address" typ="IP地址 {  }"></ArgTableRow>
<ArgTableRow arg="smb-share" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="smb-user" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="smb-password" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="smb-encryption" typ="布尔值 {  }"></ArgTableRow>
<ArgTableRow arg="media-sharing" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="media-interface" typ="接口枚举 { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="tmpfs-max-size" typ="数字 {  }"></ArgTableRow>
<ArgTableRow arg="ramdisk-size" typ="数字 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="crypted-backend" typ="枚举 (none)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="encryption-key" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="self-encryption-password" typ="字符串" syscap="storage"></ArgTableRow>
<ArgTableRow arg="sshfs-address" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-port" typ="数字 {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-user" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-password" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-path" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="swap" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="file-path" typ="文件 {  }"></ArgTableRow>
<ArgTableRow arg="file-size" typ="数字 {  }"></ArgTableRow>
<ArgTableRow arg="file-offset" typ="数字 {  }"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="slot-default" typ="字符串"></ArgTableRow>
<ArgTableRow arg="fs-label" typ="字符串"></ArgTableRow>
<ArgTableRow arg="fs-uuid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="fs" typ="枚举 (fat32 | ext4 | btrfs | xfs | nfs | smb | wipe | wipe-quick | tmpfs | exfat | ntfs | sshfs | squashfs | iso | discard | discard-secure | -)"></ArgTableRow>
<ArgTableRow arg="model" typ="字符串"></ArgTableRow>
<ArgTableRow arg="serial" typ="字符串"></ArgTableRow>
<ArgTableRow arg="fw-version" typ="字符串"></ArgTableRow>
<ArgTableRow arg="size" typ="数字"></ArgTableRow>
<ArgTableRow arg="free" typ="数字"></ArgTableRow>
<ArgTableRow arg="total-inodes" typ="数字"></ArgTableRow>
<ArgTableRow arg="free-inodes" typ="数字"></ArgTableRow>
<ArgTableRow arg="use" typ="数字"></ArgTableRow>
<ArgTableRow arg="mount-point" typ="字符串"></ArgTableRow>
<ArgTableRow arg="sector-size" typ="数字"></ArgTableRow>
<ArgTableRow arg="interface" typ="字符串"></ArgTableRow>
<ArgTableRow arg="interface-speed" typ="数字"></ArgTableRow>
<ArgTableRow arg="raid-member-state" typ="字符串" syscap="storage"></ArgTableRow>
<ArgTableRow arg="state" typ="字符串"></ArgTableRow>
<ArgTableRow arg="raid-uuid" typ="字符串" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-secret" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-secret" typ="字符串 {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="sshfs-local-user" typ="字符串 {  }"></ArgTableRow>
<ArgTableRow arg="io-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="io-errors" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-rate" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="write-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-rate" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="active-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="wait-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="discard-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="flush-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="flush-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="temperature" typ="数字"></ArgTableRow>
<ArgTableRow arg="temperatures" typ="多值 { 数组ID, 数字
 }"></ArgTableRow>
<ArgTableRow arg="critical-warning" typ="位域 (spare-space, temperature, reliability-degraded, read-only, volatile-backup-failed)"></ArgTableRow>
<ArgTableRow arg="available-spare" typ="数字"></ArgTableRow>
<ArgTableRow arg="available-spare-threshold" typ="数字"></ArgTableRow>
<ArgTableRow arg="percentage-used" typ="数字"></ArgTableRow>
<ArgTableRow arg="host-read-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="host-write-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="host-read-cmds" typ="数字"></ArgTableRow>
<ArgTableRow arg="host-write-cmds" typ="数字"></ArgTableRow>
<ArgTableRow arg="controller-busy-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="power-cycles" typ="数字"></ArgTableRow>
<ArgTableRow arg="power-on-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="unsafe-shutdowns" typ="数字"></ArgTableRow>
<ArgTableRow arg="unrecovered-integrity-errors" typ="数字"></ArgTableRow>
<ArgTableRow arg="warning-temperature" typ="数字"></ArgTableRow>
<ArgTableRow arg="warning-temperature-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="critical-temperature" typ="数字"></ArgTableRow>
<ArgTableRow arg="critical-temperature-time" typ="时间"></ArgTableRow>
</ArgTable>

## disk/blink

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="slots" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
</ArgTable>

## disk/btrfs

**条件:** !smips
**系统能力:** storage
**类型:** 目录

### disk/btrfs/filesystem

**条件:** !smips
**系统能力:** storage
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="missing-devs">缺失设备</ArgTableRow>
<ArgTableRow arg="b" typ="balancing">正在平衡</ArgTableRow>
<ArgTableRow arg="r" typ="replacing">正在替换</ArgTableRow>
<ArgTableRow arg="s" typ="scrubbing">正在巡检</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="label" typ="字符串"></ArgTableRow>
<ArgTableRow arg="default-subvolume" typ="枚举"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="uuid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="total-devs" typ="数字"></ArgTableRow>
<ArgTableRow arg="dev-ids" typ="多值 { 数组ID, 数字
 }"></ArgTableRow>
<ArgTableRow arg="devs" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="spaces" typ="多值 { 数组ID, 字符串
 }"></ArgTableRow>
<ArgTableRow arg="balance-status" typ="字符串"></ArgTableRow>
<ArgTableRow arg="replace-status" typ="字符串"></ArgTableRow>
<ArgTableRow arg="scrub-status" typ="字符串"></ArgTableRow>
<ArgTableRow arg="write-errors" typ="多值 { 数字
 }"></ArgTableRow>
<ArgTableRow arg="read-errors" typ="多值 { 数字
 }"></ArgTableRow>
<ArgTableRow arg="flush-errors" typ="多值 { 数字
 }"></ArgTableRow>
<ArgTableRow arg="corruption-errors" typ="多值 { 数字
 }"></ArgTableRow>
<ArgTableRow arg="generation-errors" typ="多值 { 数字
 }"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/add-device

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="枚举"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/balance-cancel

**条件:** !smips
**类型:** 命令

#### disk/btrfs/filesystem/balance-start

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="data-profile" typ="枚举 ()"></ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="枚举 ()"></ArgTableRow>
<ArgTableRow arg="system-profile" typ="枚举 ()"></ArgTableRow>
<ArgTableRow arg="data-usage" typ="范围"></ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="范围"></ArgTableRow>
<ArgTableRow arg="system-usage" typ="范围"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/remove-device

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="device" typ="枚举"></ArgTableRow>
<ArgTableRow arg="device-id" typ="数字"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/replace-cancel

**条件:** !smips
**类型:** 命令

#### disk/btrfs/filesystem/replace-device

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="device-to-remove" typ="枚举"></ArgTableRow>
<ArgTableRow arg="device-to-remove-id" typ="数字"></ArgTableRow>
<ArgTableRow arg="device-to-add" typ="枚举"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/reset-counters

**条件:** !smips
**类型:** 命令

#### disk/btrfs/filesystem/scrub-cancel

**条件:** !smips
**类型:** 命令

#### disk/btrfs/filesystem/scrub-start

**条件:** !smips
**类型:** 命令

### disk/btrfs/subvolume

**条件:** !smips
**系统能力:** storage
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="*" typ="default">默认</ArgTableRow>
<ArgTableRow arg="S" typ="snapshot">快照</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">只读</ArgTableRow>
<ArgTableRow arg="D" typ="dead">失效</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">已挂载</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="fs" typ="枚举" mandatory="1"></ArgTableRow>
<ArgTableRow arg="parent" typ="枚举"></ArgTableRow>
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="read-only" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="mount" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="mountpoint" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="top-level" typ="枚举"></ArgTableRow>
<ArgTableRow arg="fullname" typ="字符串"></ArgTableRow>
<ArgTableRow arg="uuid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="received-uuid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="creation-time" typ="日期"></ArgTableRow>
<ArgTableRow arg="subvolume-id" typ="数字"></ArgTableRow>
<ArgTableRow arg="generation" typ="数字"></ArgTableRow>
<ArgTableRow arg="dead" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="snapshot" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="send-trans-id" typ="数字"></ArgTableRow>
<ArgTableRow arg="send-time" typ="日期"></ArgTableRow>
<ArgTableRow arg="recv-trans-id" typ="数字"></ArgTableRow>
<ArgTableRow arg="recv-time" typ="日期"></ArgTableRow>
<ArgTableRow arg="snapshots" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="字符串"></ArgTableRow>
</ArgTable>

### disk/btrfs/transfer

**条件:** !smips
**系统能力:** storage
**类型:** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="枚举 (receive | send)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="fs" typ="枚举"></ArgTableRow>
<ArgTableRow arg="send-parent" typ="枚举"></ArgTableRow>
<ArgTableRow arg="send-subvolumes" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="file" typ="文件"></ArgTableRow>
<ArgTableRow arg="ssh-address" typ="字符串"></ArgTableRow>
<ArgTableRow arg="ssh-receive-mount" typ="字符串"></ArgTableRow>
<ArgTableRow arg="ssh-port" typ="数字"></ArgTableRow>
<ArgTableRow arg="ssh-user" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="status" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/check

**条件:** !smips
**系统能力:** storage
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/copy

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="src" typ="枚举"></ArgTableRow>
<ArgTableRow arg="dst" typ="枚举"></ArgTableRow>
<ArgTableRow arg="src-offset" typ="数字"></ArgTableRow>
<ArgTableRow arg="dst-offset" typ="数字"></ArgTableRow>
<ArgTableRow arg="size" typ="数字"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/eject

**条件:** !smips
**类型:** 命令

## disk/format

**条件:** !smips
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file-system" typ="枚举 (fat32 | ext4 | btrfs | xfs | wipe | wipe-quick | exfat | discard | discard-secure)"></ArgTableRow>
<ArgTableRow arg="label" typ="字符串"></ArgTableRow>
<ArgTableRow arg="mbr-partition-table" typ="布尔值"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/monitor-traffic

**条件:** !smips
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="io-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="io-errors" typ="数字"></ArgTableRow>
<ArgTableRow arg="slot" typ="字符串"></ArgTableRow>
<ArgTableRow arg="read-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-rate" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="read-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="write-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-rate" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="write-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="active-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="wait-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="discard-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-merges" typ="数字"></ArgTableRow>
<ArgTableRow arg="discard-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="flush-ops" typ="数字"></ArgTableRow>
<ArgTableRow arg="flush-time" typ="时间"></ArgTableRow>
</ArgTable>

## disk/nvme-discover

**条件:** !smips
**系统能力:** storage
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="IP地址"></ArgTableRow>
<ArgTableRow arg="port" typ="数字"></ArgTableRow>
<ArgTableRow arg="host-name" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="nqn" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/raid-scrub

**条件:** !smips
**系统能力:** storage
**类型:** 命令

## disk/raid-scrub-cancel

**条件:** !smips
**系统能力:** storage
**类型:** 命令

## disk/repair

**条件:** !smips
**系统能力:** storage
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/reset-counters

**条件:** !smips
**类型:** 命令

## disk/scan

**条件:** !smips
**类型:** 命令

## disk/settings

**条件:** !smips
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="default-mount-point-template" typ="字符串"></ArgTableRow>
<ArgTableRow arg="auto-smb-sharing" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="auto-smb-user" typ="枚举"></ArgTableRow>
<ArgTableRow arg="auto-media-sharing" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="auto-media-interface" typ="接口枚举 { none:nv::BADID }"></ArgTableRow>
</ArgTable>

## disk/smart-info

**条件:** !smips
**系统能力:** storage
**类型:** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="output" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/test

**条件:** !smips
**类型:** 命令

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="N" typ="initializing">初始化中</ArgTableRow>
<ArgTableRow arg="R" typ="running">运行中</ArgTableRow>
<ArgTableRow arg="F" typ="failed">失败</ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="disk" typ="多值 { 数组ID, 枚举
 }"></ArgTableRow>
<ArgTableRow arg="block-size" typ="数字"></ArgTableRow>
<ArgTableRow arg="thread-count" typ="数字"></ArgTableRow>
<ArgTableRow arg="direction" typ="枚举 (read | write)"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举 (device | filesystem)"></ArgTableRow>
<ArgTableRow arg="pattern" typ="枚举 (sequential | random)"></ArgTableRow>
<ArgTableRow arg="entries-to-show" typ="数字"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="seq" typ="枚举 (TOT)"></ArgTableRow>
<ArgTableRow arg="rate" typ="数字"></ArgTableRow>
<ArgTableRow arg="iops" typ="数字"></ArgTableRow>
<ArgTableRow arg="bytes" typ="数字"></ArgTableRow>
<ArgTableRow arg="disk" typ="枚举 (TOT)"></ArgTableRow>
<ArgTableRow arg="thread" typ="枚举 (TOT)"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举 (device | filesystem)"></ArgTableRow>
<ArgTableRow arg="pattern" typ="枚举 (sequential | random)"></ArgTableRow>
<ArgTableRow arg="dir" typ="枚举 (read | write)"></ArgTableRow>
<ArgTableRow arg="bsize" typ="数字"></ArgTableRow>
<ArgTableRow arg="state" typ="字符串"></ArgTableRow>
</ArgTable>

## disk/trim

**条件:** !smips
**类型:** 命令