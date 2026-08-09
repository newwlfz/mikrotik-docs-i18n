# disk

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# disk

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="A" typ="acquired">acquired</ArgTableRow>
<ArgTableRow arg="E" typ="empty">empty</ArgTableRow>
<ArgTableRow arg="B" typ="block-device">block-device</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">mounted</ArgTableRow>
<ArgTableRow arg="F" typ="formatting">formatting</ArgTableRow>
<ArgTableRow arg="S" typ="swap-enabled">swap-enabled</ArgTableRow>
<ArgTableRow arg="f" typ="raid-member-failed">raid-member-failed</ArgTableRow>
<ArgTableRow arg="r" typ="raid-member">raid-member</ArgTableRow>
<ArgTableRow arg="c" typ="encrypted">encrypted</ArgTableRow>
<ArgTableRow arg="g" typ="guid-partition-table">guid-partition-table</ArgTableRow>
<ArgTableRow arg="p" typ="partition">partition</ArgTableRow>
<ArgTableRow arg="t" typ="nvme-tcp-export">nvme-tcp-export</ArgTableRow>
<ArgTableRow arg="i" typ="iscsi-export">iscsi-export</ArgTableRow>
<ArgTableRow arg="s" typ="smb-sharing">smb-sharing</ArgTableRow>
<ArgTableRow arg="n" typ="nfs-sharing">nfs-sharing</ArgTableRow>
<ArgTableRow arg="m" typ="media-sharing">media-sharing</ArgTableRow>
<ArgTableRow arg="L" typ="self-encrypted-and-locked">self-encrypted-and-locked</ArgTableRow>
<ArgTableRow arg="O" typ="self-encryption-enabled">self-encryption-enabled</ArgTableRow>
<ArgTableRow arg="o" typ="self-encryption-supported">self-encryption-supported</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (raid | nvme-tcp | iscsi | nfs | smb | partition | tmpfs | ramdisk | crypted | sshfs | file | hardware)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="slot" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="mount-point-template" typ="string"></ArgTableRow>
<ArgTableRow arg="mount-filesystem" typ="bool"></ArgTableRow>
<ArgTableRow arg="mount-read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="compress" typ="bool"></ArgTableRow>
<ArgTableRow arg="partition-number" typ="num"></ArgTableRow>
<ArgTableRow arg="partition-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="partition-size" typ="num"></ArgTableRow>
<ArgTableRow arg="raid-type" typ="enum (0 | 1 | 4 | 5 | 6 | linear | faulty)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-device-count" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-max-component-size" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-chunk-size" typ="enum (64K | 128K | 256K | 512K | 1M | 2M | 4M)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-master" typ="enum (none)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-role" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="raid-member-failed" typ="bool {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-export" typ="bool" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-port" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-nqn" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-allow-host-name" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-password" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-address" typ="ipAddr {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-nqn" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-host-name" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-password" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-port" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-export" typ="bool" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-server-port" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-server-iqn" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-port" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-address" typ="ipAddr {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="iscsi-iqn" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-sharing" typ="bool" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-address" typ="ipAddr {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nfs-share" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="smb-sharing" typ="bool"></ArgTableRow>
<ArgTableRow arg="smb-server-user" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="smb-server-password" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="smb-server-encryption" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="smb-address" typ="ipAddr {  }"></ArgTableRow>
<ArgTableRow arg="smb-share" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="smb-user" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="smb-password" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="smb-encryption" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="media-sharing" typ="bool"></ArgTableRow>
<ArgTableRow arg="media-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="tmpfs-max-size" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="ramdisk-size" typ="num {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="crypted-backend" typ="enum (none)" syscap="storage"></ArgTableRow>
<ArgTableRow arg="encryption-key" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="self-encryption-password" typ="string" syscap="storage"></ArgTableRow>
<ArgTableRow arg="sshfs-address" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-port" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-user" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-password" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="sshfs-path" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="swap" typ="bool"></ArgTableRow>
<ArgTableRow arg="file-path" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="file-size" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="file-offset" typ="num {  }"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="slot-default" typ="string"></ArgTableRow>
<ArgTableRow arg="fs-label" typ="string"></ArgTableRow>
<ArgTableRow arg="fs-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="fs" typ="enum (fat32 | ext4 | btrfs | xfs | nfs | smb | wipe | wipe-quick | tmpfs | exfat | ntfs | sshfs | squashfs | iso | discard | discard-secure | -)"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="string"></ArgTableRow>
<ArgTableRow arg="fw-version" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="free" typ="num"></ArgTableRow>
<ArgTableRow arg="total-inodes" typ="num"></ArgTableRow>
<ArgTableRow arg="free-inodes" typ="num"></ArgTableRow>
<ArgTableRow arg="use" typ="num"></ArgTableRow>
<ArgTableRow arg="mount-point" typ="string"></ArgTableRow>
<ArgTableRow arg="sector-size" typ="num"></ArgTableRow>
<ArgTableRow arg="interface" typ="string"></ArgTableRow>
<ArgTableRow arg="interface-speed" typ="num"></ArgTableRow>
<ArgTableRow arg="raid-member-state" typ="string" syscap="storage"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
<ArgTableRow arg="raid-uuid" typ="string" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-server-secret" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="nvme-tcp-secret" typ="string {  }" syscap="storage"></ArgTableRow>
<ArgTableRow arg="sshfs-local-user" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="io-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="io-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="read-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="read-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="read-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="read-time" typ="time"></ArgTableRow>
<ArgTableRow arg="write-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="write-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="write-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="write-time" typ="time"></ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="active-time" typ="time"></ArgTableRow>
<ArgTableRow arg="wait-time" typ="time"></ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-time" typ="time"></ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="flush-time" typ="time"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="temperatures" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="critical-warning" typ="ubit (spare-space, temperature, reliability-degraded, read-only, volatile-backup-failed)"></ArgTableRow>
<ArgTableRow arg="available-spare" typ="num"></ArgTableRow>
<ArgTableRow arg="available-spare-threshold" typ="num"></ArgTableRow>
<ArgTableRow arg="percentage-used" typ="num"></ArgTableRow>
<ArgTableRow arg="host-read-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="host-write-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="host-read-cmds" typ="num"></ArgTableRow>
<ArgTableRow arg="host-write-cmds" typ="num"></ArgTableRow>
<ArgTableRow arg="controller-busy-time" typ="time"></ArgTableRow>
<ArgTableRow arg="power-cycles" typ="num"></ArgTableRow>
<ArgTableRow arg="power-on-time" typ="time"></ArgTableRow>
<ArgTableRow arg="unsafe-shutdowns" typ="num"></ArgTableRow>
<ArgTableRow arg="unrecovered-integrity-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="warning-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="warning-temperature-time" typ="time"></ArgTableRow>
<ArgTableRow arg="critical-temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="critical-temperature-time" typ="time"></ArgTableRow>
</ArgTable>

## disk/blink

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="slots" typ="multi { array-id, enum
 }"></ArgTableRow>
</ArgTable>

## disk/btrfs

**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

### disk/btrfs/filesystem

**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="missing-devs">missing-devs</ArgTableRow>
<ArgTableRow arg="b" typ="balancing">balancing</ArgTableRow>
<ArgTableRow arg="r" typ="replacing">replacing</ArgTableRow>
<ArgTableRow arg="s" typ="scrubbing">scrubbing</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="label" typ="string"></ArgTableRow>
<ArgTableRow arg="default-subvolume" typ="enum"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="total-devs" typ="num"></ArgTableRow>
<ArgTableRow arg="dev-ids" typ="multi { array-id, num
 }"></ArgTableRow>
<ArgTableRow arg="devs" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="spaces" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="balance-status" typ="string"></ArgTableRow>
<ArgTableRow arg="replace-status" typ="string"></ArgTableRow>
<ArgTableRow arg="scrub-status" typ="string"></ArgTableRow>
<ArgTableRow arg="write-errors" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="read-errors" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="flush-errors" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="corruption-errors" typ="multi { num
 }"></ArgTableRow>
<ArgTableRow arg="generation-errors" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/add-device

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/balance-cancel

**Conditions:** !smips
**Type:** Command

#### disk/btrfs/filesystem/balance-start

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="data-profile" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="metadata-profile" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="system-profile" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="data-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="metadata-usage" typ="range"></ArgTableRow>
<ArgTableRow arg="system-usage" typ="range"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/remove-device

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device" typ="enum"></ArgTableRow>
<ArgTableRow arg="device-id" typ="num"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/replace-cancel

**Conditions:** !smips
**Type:** Command

#### disk/btrfs/filesystem/replace-device

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="device-to-remove" typ="enum"></ArgTableRow>
<ArgTableRow arg="device-to-remove-id" typ="num"></ArgTableRow>
<ArgTableRow arg="device-to-add" typ="enum"></ArgTableRow>
</ArgTable>

#### disk/btrfs/filesystem/reset-counters

**Conditions:** !smips
**Type:** Command

#### disk/btrfs/filesystem/scrub-cancel

**Conditions:** !smips
**Type:** Command

#### disk/btrfs/filesystem/scrub-start

**Conditions:** !smips
**Type:** Command

### disk/btrfs/subvolume

**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="S" typ="snapshot">snapshot</ArgTableRow>
<ArgTableRow arg="r" typ="read-only">read-only</ArgTableRow>
<ArgTableRow arg="D" typ="dead">dead</ArgTableRow>
<ArgTableRow arg="M" typ="mounted">mounted</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="fs" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="read-only" typ="bool"></ArgTableRow>
<ArgTableRow arg="mount" typ="bool"></ArgTableRow>
<ArgTableRow arg="mountpoint" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="top-level" typ="enum"></ArgTableRow>
<ArgTableRow arg="fullname" typ="string"></ArgTableRow>
<ArgTableRow arg="uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="received-uuid" typ="string"></ArgTableRow>
<ArgTableRow arg="creation-time" typ="date"></ArgTableRow>
<ArgTableRow arg="subvolume-id" typ="num"></ArgTableRow>
<ArgTableRow arg="generation" typ="num"></ArgTableRow>
<ArgTableRow arg="dead" typ="bool"></ArgTableRow>
<ArgTableRow arg="snapshot" typ="bool"></ArgTableRow>
<ArgTableRow arg="send-trans-id" typ="num"></ArgTableRow>
<ArgTableRow arg="send-time" typ="date"></ArgTableRow>
<ArgTableRow arg="recv-trans-id" typ="num"></ArgTableRow>
<ArgTableRow arg="recv-time" typ="date"></ArgTableRow>
<ArgTableRow arg="snapshots" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="path" typ="string"></ArgTableRow>
</ArgTable>

### disk/btrfs/transfer

**Conditions:** !smips
**Syscap:** storage
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (receive | send)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="fs" typ="enum"></ArgTableRow>
<ArgTableRow arg="send-parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="send-subvolumes" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="file" typ="file"></ArgTableRow>
<ArgTableRow arg="ssh-address" typ="string"></ArgTableRow>
<ArgTableRow arg="ssh-receive-mount" typ="string"></ArgTableRow>
<ArgTableRow arg="ssh-port" typ="num"></ArgTableRow>
<ArgTableRow arg="ssh-user" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## disk/check

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

## disk/copy

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="src" typ="enum"></ArgTableRow>
<ArgTableRow arg="dst" typ="enum"></ArgTableRow>
<ArgTableRow arg="src-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="dst-offset" typ="num"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

## disk/eject

**Conditions:** !smips
**Type:** Command

## disk/format

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-system" typ="enum (fat32 | ext4 | btrfs | xfs | wipe | wipe-quick | exfat | discard | discard-secure)"></ArgTableRow>
<ArgTableRow arg="label" typ="string"></ArgTableRow>
<ArgTableRow arg="mbr-partition-table" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

## disk/monitor-traffic

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="io-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="io-errors" typ="num"></ArgTableRow>
<ArgTableRow arg="slot" typ="string"></ArgTableRow>
<ArgTableRow arg="read-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="read-ops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="read-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="read-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="read-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="read-time" typ="time"></ArgTableRow>
<ArgTableRow arg="write-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="write-ops-per-second" typ="num"></ArgTableRow>
<ArgTableRow arg="write-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="write-rate" typ="num"></ArgTableRow>
<ArgTableRow arg="write-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="write-time" typ="time"></ArgTableRow>
<ArgTableRow arg="in-flight-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="active-time" typ="time"></ArgTableRow>
<ArgTableRow arg="wait-time" typ="time"></ArgTableRow>
<ArgTableRow arg="discard-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-merges" typ="num"></ArgTableRow>
<ArgTableRow arg="discard-time" typ="time"></ArgTableRow>
<ArgTableRow arg="flush-ops" typ="num"></ArgTableRow>
<ArgTableRow arg="flush-time" typ="time"></ArgTableRow>
</ArgTable>

## disk/nvme-discover

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="port" typ="num"></ArgTableRow>
<ArgTableRow arg="host-name" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="nqn" typ="string"></ArgTableRow>
</ArgTable>

## disk/raid-scrub

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

## disk/raid-scrub-cancel

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

## disk/repair

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

## disk/reset-counters

**Conditions:** !smips
**Type:** Command

## disk/scan

**Conditions:** !smips
**Type:** Command

## disk/settings

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-mount-point-template" typ="string"></ArgTableRow>
<ArgTableRow arg="auto-smb-sharing" typ="bool"></ArgTableRow>
<ArgTableRow arg="auto-smb-user" typ="enum"></ArgTableRow>
<ArgTableRow arg="auto-media-sharing" typ="bool"></ArgTableRow>
<ArgTableRow arg="auto-media-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
</ArgTable>

## disk/smart-info

**Conditions:** !smips
**Syscap:** storage
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="output" typ="string"></ArgTableRow>
</ArgTable>

## disk/test

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="N" typ="initializing">initializing</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="F" typ="failed">failed</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="multi { array-id, enum
 }"></ArgTableRow>
<ArgTableRow arg="block-size" typ="num"></ArgTableRow>
<ArgTableRow arg="thread-count" typ="num"></ArgTableRow>
<ArgTableRow arg="direction" typ="enum (read | write)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)"></ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)"></ArgTableRow>
<ArgTableRow arg="entries-to-show" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="seq" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="rate" typ="num"></ArgTableRow>
<ArgTableRow arg="iops" typ="num"></ArgTableRow>
<ArgTableRow arg="bytes" typ="num"></ArgTableRow>
<ArgTableRow arg="disk" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="thread" typ="enum (TOT)"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (device | filesystem)"></ArgTableRow>
<ArgTableRow arg="pattern" typ="enum (sequential | random)"></ArgTableRow>
<ArgTableRow arg="dir" typ="enum (read | write)"></ArgTableRow>
<ArgTableRow arg="bsize" typ="num"></ArgTableRow>
<ArgTableRow arg="state" typ="string"></ArgTableRow>
</ArgTable>

## disk/trim

**Conditions:** !smips
**Type:** Command
