# Tmpfs

> Tmpfs 允许将 RAM 用作文件系统，可配置最大大小，但重启或断电后会清空。

# Tmpfs

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

Tmpfs 允许将部分 RAM 用作文件系统。它不能用作块设备。

:::warning

tmpfs 在重启或断电后会清空。

:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **tmpfs-max-size** | tmpfs 文件系统的最大大小 |

## 配置示例

```ros
add type=tmpfs tmpfs-max-size=10G
```