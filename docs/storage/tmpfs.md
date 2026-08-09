# Tmpfs

> Tmpfs enables using RAM as a filesystem, with configurable maximum size but cleared on reboot or power loss.

# Tmpfs

:::info
This feature requires the [Storage](./index.md) package.
:::

Tmpfs allows using part of RAM as a filesystem. It cannot be used as a block device.

:::warning

A tmpfs is cleared on reboot or power loss.

:::

## Properties

| Property | Description |
| :-- | :-- |
| **tmpfs-max-size** | Maximum size of the tmpfs filesystem |

## Configuration example

```ros
add type=tmpfs tmpfs-max-size=10G
```
