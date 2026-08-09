# PPP

> RouterOS 中的 PPP 支持点对点协议通信，用于传输多协议数据报，包含 LCP 和 NCP 组件。它支持 PPP 客户端和服务器配置，并提供了诸如按需拨号设置以及兼容调制解调器的固件升级等示例。

# PPP

## 概述

点对点协议（PPP）提供了一种在点对点链路上传输多协议数据报的标准方法。RouterOS 中的 PPP 基于 [RFC 1661 标准](https://tools.ietf.org/html/rfc1661)。

## 简介

PPP 在此阶段的基本目的是在数据链路层的点对点链路上传输第三层数据包。两个对等体之间的数据包假定按顺序交付。

PPP 由三个主要组件组成：

1. 一种封装多协议数据报的方法。
2. 用于建立、配置和测试数据链路连接的链路控制协议（LCP）。
3. 用于建立和配置不同网络层协议的网络控制协议（NCP）家族。

关于 RouterOS 中详细的 PPP 数据包处理流程，您可以参阅 [数据包流程图](../firewall-and-quality-of-service/packet-flow-in-routeros.md)。

### PPP 客户端

**子菜单：** `/interface/ppp-client`

### PPP 客户端示例

以下是如何使用 LTE 调制解调器暴露的串行端口添加客户端的示例。

```ros
/interface/ppp-client/add apn=yourapn dial-on-demand=no disabled=no port=usb2
```

对于持续连接，应将按需拨号（dial-on-demand）设置为“no”。

### PPP 服务器

**子菜单：** `/interface/ppp-server`

## KNOT RB924i-2nD-BT5&BG77

如果您看到消息“*有更新版本的调制解调器固件可用！*”并且想要升级您的 BG77 调制解调器固件，请使用以下命令：

```routeros
/interface/ppp-client/firmware-upgrade [find] upgrade=yes
```