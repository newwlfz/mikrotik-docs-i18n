# 基于架构的功能支持

> 本页概述了 MikroTik RouterOS 各架构间的功能支持差异，列出了各平台（如 ARM、MIPS 和 PPC）不支持或独有的功能。同时，也提供了关于 WiFi、L3 卸载、PTP 及交换芯片能力的额外资源参考。

# 基于架构的功能支持

## 各架构功能支持

大多数功能在所有设备架构上均保持一致支持，仅有少数例外。下表明确了各架构不支持或独有的功能：

| 架构 | 不支持 | 独有支持 |
| :-- | :-- | :-- |
| **ARM (ARM32)** | — | ZeroTier、Container、BTH |
| **ARM64** | — | ZeroTier、Container、BTH |
| **MIPSBE** | ZeroTier、Dude Server | — |
| **MMIPS** | ZeroTier | — |
| **SMIPS** | ZeroTier、DOT1X、BGP、MPLS、PIMSM、Dude Server、User Manager | — |
| **TILE** | ZeroTier | BTH |
| **PPC** | ZeroTier、Dude Server | — |
| **x86 PC** | ZeroTier、Cloud | Container |
| **CHR（云托管路由器）** | — | Container |

除功能差异外，硬件能力也因设备型号而异。更多信息，请参阅以下资源：

- **WiFi** — 针对 802.11ax 设备的新驱动实现及支持的旧设备
- **L3 硬件卸载** — 设备支持详情
- **PTP（精确时间协议）** — 概述与配置
- **交换芯片功能** — 能力与限制