# Ramdisk

> RAMdisk enables using RAM as a block device for storage, supporting RAID configurations and requiring the Storage package. It is cleared on reboot or power loss, with a configurable size via ramdisk-size property.

# Ramdisk

:::info
This feature requires the [Storage](./index.md) package.
:::

RAMdisk allows using part of RAM as an attached device (block device). Compared to tmpfs, this allows using RAM as part of a RAID, or in any other configuration where a device — rather than a folder — is required.

:::warning

A RAMdisk is cleared on reboot or power loss.

:::

## Properties

| Property | Description |
| :-- | :-- |
| **ramdisk-size** | Size of the block device you want to create |

## Configuration example

```ros
/disk/add type=ramdisk ramdisk-size=500M
```

Format the ramdisk before using it:

```routeros
/disk/format ramdisk1
```
