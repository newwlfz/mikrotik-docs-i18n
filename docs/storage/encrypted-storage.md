# Encrypted storage (dm-crypt)

> Encrypted storage (dm-crypt) enables transparent disk encryption using `dm_crypt` for block devices, with properties like slot name, encryption key, and backend drive. Examples show creating encrypted file systems on USB or RAID1 arrays with formatting instructions.

# Encrypted storage (dm-crypt)

:::info
This feature requires the [Storage](./index.md) package.
:::

Drive or device used together with `type=crypted` to make `dm_crypt` encrypted storage. `dm-crypt` is a transparent disk encryption subsystem designed to provide encryption of block devices.

## Properties

| Property | Description |
| :-- | :-- |
| **slot** *(string;* Default: ) | Name of the  file system |
| **encryption-key** *(string;* Default: ) | key used to decrypt |
| **crypted-backend** *(string;* Default: ) | Drive or partition to encrypt |

## Examples

### Simple crypted file system

To create an encrypted file-system:

```ros
/disk
add crypted-backend=usb1 encryption-key=<secret_key> slot=crypted-usb1 type=crypted
```

After it's created, format the file system and it's ready to go.

```ros
/disk/format crypted-usb1 file-system=ext4 
```

### Crypted RAID1 array with integrity check

Create a RAID1 array and create a encrypted-file system on top of it:

```routeros
/disk
add raid-device-count=2 raid-type=1 slot=raid1 type=raid
set nvme3 raid-master=raid1 raid-role=0
set nvme4 raid-master=raid1 raid-role=1
add crypted-backend=raid1 encryption-key=<secret_key> slot=crypted-raid1 type=crypted  crypt-mode=encryption-and-integrity

```

Format the encrypted file-system to Btrfs:

```routeros
/disk
 format crypted-raid1 file-system=btrfs  
```
