# CHR：Hyper-V 安装

> 本文档介绍如何在 Microsoft Hyper-V 上安装 MikroTik RouterOS CHR，详细说明支持的网络适配器（合成与旧版）和磁盘控制器（系统磁盘使用 IDE，辅助磁盘使用 SCSI），并提供 Hyper-V 文档链接。

# CHR：Hyper-V 安装

## 支持的网络与磁盘接口

### Microsoft Hyper-V

**网络适配器：**

- 网络适配器（合成）
- 旧版网络适配器

**磁盘控制器：**

- IDE
- SCSI

> **注意：** 在 Hyper-V 上，SCSI 控制器类型仅支持辅助磁盘。系统磁盘映像必须连接到 IDE 控制器。

#### Hyper-V

**Hyper-V 文档：**

- https://technet.microsoft.com/en-us/library/cc816585(v=ws.10).aspx#Anchor_2