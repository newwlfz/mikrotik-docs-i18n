# 日志

> 本节概述了 MikroTik RouterOS 的日志记录功能，涵盖如何使用 `/log` 菜单实时查看和过滤日志消息，以及通过 `/system/logging` 将日志转发到外部系统的详细配置选项。

import DocCardList from '@theme/DocCardList';

# 日志

本节涵盖日志导出和集成示例。使用它将 RouterOS 日志转发到外部系统，例如 Elasticsearch。

<DocCardList />

RouterOS 能够记录各种系统事件和状态信息。日志可以保存在路由器内存（RAM）、磁盘、文件中，通过电子邮件发送，甚至发送到远程 syslog 服务器。

[视频：日志记录基础](http://youtube.com/watch?v=E-QAhaWtsnU)

## 日志消息

**子菜单：** `/log`

存储在路由器本地内存中的所有消息都可以从 `/log` 菜单中打印出来。每条记录包含事件发生的时间和日期、该消息所属的主题以及消息本身。

```ros
[admin@MikroTik] /log> print 
1970-01-02 02:00:09 system,info router rebooted 
sep/15 09:54:33 system,info,account user admin logged in from 10.1.101.212 via winbox 
sep/15 12:33:18 system,info item added by admin 
sep/15 12:34:26 system,info mangle rule added by admin 
sep/15 12:34:29 system,info mangle rule moved by admin 
sep/15 12:35:34 system,info mangle rule changed by admin 
sep/15 12:42:14 system,info,account user admin logged in from 10.1.101.212 via telnet 
sep/15 12:42:55 system,info,account user admin logged out from 10.1.101.212 via telnet 
01:01:58 firewall,info input: in:ether1 out:(none), src-mac 00:21:29:6d:82:07, proto UDP, 
10.1.101.1:520->10.1.101.255:520, len 452
```

如果日志是在添加日志条目的同一天打印的，则只显示时间。在上面的示例中，您可以看到第二条消息是在当前年份的 sep/15 添加的（未添加年份），而最后一条消息是今天添加的，因此只显示时间。

*Print* 命令接受多个参数，允许检测新的日志条目、仅打印必要的消息等。

例如，以下命令将打印所有主题为 info 的日志消息，并持续检测新的日志条目，直到按下 <kbd>Control</kbd>+<kbd>C</kbd>。

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script
-- Ctrl-C to quit.
```

在此示例中，它将仅打印 dhcp 信息消息：

```ros
[admin@MikroTik] /log/print where topics~"dhcp.info"
11:42:32 dhcp,info defconf deassigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
11:42:32 dhcp,info defconf assigned 192.168.88.37 for B0:E4:5C:27:EF:F2 Samsung
```

如果 print 处于跟随模式，您可以按键盘上的 'space' 键插入分隔符：

```ros
[admin@MikroTik] /log > print follow where topics~".info"
12:52:24 script,info hello from script

= = = = = = = = = = = = = = = = = = = = = = = = = = =

-- Ctrl-C to quit.
```

## 日志记录配置

**子菜单：** `/system/logging`

| 属性 | 描述 |
| :--- | :--- |
| **action** (*名称*; 默认值：**memory**) | 指定系统默认操作之一或操作菜单中列出的用户自定义操作。 |
| **prefix** (*字符串*; 默认值：无) | 添加在日志消息开头的前缀。 |
| **regex** (*字符串*; 默认值：无) | 用于匹配日志消息的正则表达式。如果正则表达式不匹配，即使主题已配置为记录日志，也不会执行该操作。 |
| **topics** (*account, acme-client, amt, async, backup, bfd, bgp, bridge, calc, caps, certificate, clock, container, critical, ddns, debug, dhcp, discover, disk, dns, dot1x, dude, e-mail, error, event, evpn, fetch, firewall, gps, gsm, health, hotspot, igmp-proxy, info, interface, ipsec, iscsi, isdn, isis, kvm, l2tp, lora, ldp, lte, manager, mme, mpls, mqtt, mvrp, natpmp, netwatch, ntp, ospf, ovpn, packet, pim, poe-in, poe-out, ppp, pppoe, pptp, ptp, queue, radvd, radius, raw, read, rip, route, rpki, rproxy, rsvp, script, sertcp, simulator, smb, snmp, socksify, ssh, ssld, sstp, state, store, stp, system, telephony, tftp, timer, tr069, update, upnp, ups, vpls, vrrp, warning, watchdog, web-proxy, wiliot, wireguard, wireless, write, zerotier*; 默认值：**info**) | 记录所有匹配指定主题或主题列表的消息。在主题前使用 **!** 字符可排除匹配的消息。例如，要记录 NTP 调试消息但不包含数据包详细信息：`/system/logging/add topics=ntp,debug,!packet` |

### 操作

**子菜单：** `/system/logging/action`

| 属性 | 描述 |
| :--- | :--- |
| **add-topics-string** (*yes\|no*; 默认值：**no**) |  |
| **cef-event-delimiter** (字符串; 默认值：**\r\n**) | 该选项帮助远程 syslog 区分发送批次中的单个事件 |
| **check-certificate** (*yes\|no*; 默认值：no) | 是否在远程操作使用 TLS 类型日志记录时检查服务器证书。 |
| **disk-file-count** (*整数 [1..65535]*; 默认值：**2**) | 指定用于存储日志消息的文件数量，仅适用于 action=disk |
| **disk-file-name** (*字符串*; 默认值：**log**) | 用于存储日志消息的文件名，仅适用于 action=disk |
| **disk-lines-per-file** (*整数 [1..65535]*; 默认值：**100**) | 指定文件的最大行数，仅适用于 action=disk |
| **disk-stop-on-full** (*yes\|no*; 默认值：**no**) | 在达到指定的 disk-lines-per-file 和 disk-file-count 数量后，是否停止将日志消息保存到磁盘，仅适用于 action=disk |
| **email-cc (*字符串*; 默认值：)** | 日志抄送发送到的电子邮件地址，仅适用于 action=email |
| **email-start-tls** (*yes \| no*; 默认值：**no**) | 发送电子邮件时是否使用 TLS，仅适用于 action=email |
| **email-to** (*字符串*; 默认值：) | 日志发送到的电子邮件地址，仅适用于 action=email |
| **memory-lines** (*整数 [1..65535]*; 默认值：**1000**) | 本地内存缓冲区中的记录数，仅适用于 action=memory |
| **memory-stop-on-full** (*yes\|no*; 默认值：**no**) | 在达到指定的 memory-lines 数量后，是否停止在本地缓冲区中保存日志消息 |
| **name** (*字符串*; 默认值：) | 操作的名称。当 target=memory 时，此名称也用作特定内存缓冲区的标识符。可以创建多个 target=memory 的操作，每个操作将其日志存储在各自独立的缓冲区中。 |
| **remember** (*yes\|no*; 默认值：) | 是否保留尚未在控制台中显示的日志消息，适用于 action=echo |
| **remote-log-format** (*cef, default, syslog*; 默认值：**default**) | 发送到远程实例的日志格式：cef - 以 CEF 格式发送日志；default - 按原样发送日志；syslog - 以 BSD-syslog 格式发送日志 |
| **remote-port** (*整数 [1..65535]*; 默认值：**514**) | 远程日志服务器的 UDP 端口（地址通过 **remote** 属性配置）。 |
| **remote-protocol** (*tcp / udp / tls*; 默认值：**udp**) | 远程日志消息的协议，TCP 和 TLS 仅适用于 CEF remote-log-format，对于 syslog 格式，即使设置了 TCP / TLS，也始终使用 UDP |
| **script** |  |
| **src-address** (*IP 地址*; 默认值：**0.0.0.0**) | 发送数据包到远程服务器时使用的源地址 |
| **syslog-facility** (*auth, authpriv, cron, daemon, ftp, kern, local0, local1, local2, local3, local4, local5, local6, local7, lpr, mail, news, ntp, syslog, user, uucp*; 默认值：**daemon**) |  |
| **syslog-severity** (*alert, auto, critical, debug, emergency, error, info, notice, warning*; 默认值：**auto**) | RFC 3164 中定义的严重性级别指示符：Emergency：系统不可用Alert：必须立即采取行动Critical：严重条件Error：错误条件Warning：警告条件Notice：正常但重要的条件Informational：信息性消息Debug：调试级别消息 |
| **syslog-time-format** (*bsd-syslog, iso8601*; 默认值：**bsd-syslog**) | 消息的时间日志格式 |
| **target** (*disk, echo, email, memory, remote, script*; 默认值：**memory**) | 日志消息的存储设施或目标disk - 日志保存到硬盘echo - 日志显示在控制台屏幕上email - 日志通过电子邮件发送memory - 日志存储在本地内存缓冲区或多个独立缓冲区（RAM 文件）中。remote - 日志发送到远程主机script - 当日志消息匹配规则时，执行 /system/script/ 中的脚本。脚本接收两个变量：topics（日志主题字符串）和 message（日志消息内容）。 |
| **vrf** (*名称*; 默认值：**main**) | 设置远程日志记录进行出站连接的 VRF，仅适用于 target=remote。该设置自 RouterOS 版本 7.19 起可用。 |

### 创建独立的内存日志缓冲区

就像为不同的笔记使用不同的文本文件一样，这些独立的内存缓冲区允许您将特定类型的日志消息（基于主题）定向到内存中不同的存储区域。

- **隔离性：** 发送到 `buffer_A` 的日志与发送到 `buffer_B` 的日志完全分离。
- **独立查看：** 您可以使用 `/log/print where buffer=buffer_name` 一次仅查看一个缓冲区的内容。
- **定向清除：** 您可以使用 `/system/logging/action/clear action=buffer_name` 清除特定缓冲区的内容，而不会影响存储在任何其他内存缓冲区中的日志。

这为存储在内存中的日志提供了更好的组织性和控制力，尤其是在调试或监控时，而不会将它们全部混合到单个默认内存日志中。

**子菜单：** `/system/logging/action/clear`

从 7.20\_ab244 开始，可以使用命令清除内存日志（target=memory）：**`/system/logging/action/clear`** action=\<`logging` 操作名称>

主题

每个日志条目都有一个描述日志消息来源的主题。一条日志消息可以分配多个主题。例如，OSPF 调试日志有四个不同的主题：route、ospf、debug 和 raw。

```ros
11:11:43 route,ospf,debug SEND: Hello Packet 10.255.255.1 -> 224.0.0.5 on lo0 
11:11:43 route,ospf,debug,raw PACKET: 
11:11:43 route,ospf,debug,raw 02 01 00 2C 0A FF FF 03 00 00 00 00 E7 9B 00 00 
11:11:43 route,ospf,debug,raw 00 00 00 00 00 00 00 00 FF FF FF FF 00 0A 02 01 
11:11:43 route,ospf,debug,raw 00 00 00 28 0A FF FF 01 00 00 00 00 
```

#### 设施无关主题列表

| 主题 | 描述 |
| :-- | :-- |
| **critical** | 标记为关键的日志条目；这些日志条目在您每次登录时都会打印到控制台。 |
| **debug** | 调试日志条目 |
| **error** | 错误消息 |
| **info** | 信息性日志条目 |
| **packet** | 显示接收/发送数据包内容的日志条目 |
| **raw** | 显示接收/发送数据包原始内容的日志条目 |
| **warning** | 警告消息。 |

#### 各种 RouterOS 设施使用的主题

| 主题 | 描述 |
| :-- | :-- |
| **account** | 由计费设施生成的日志消息。 |
| **async** | 由异步设备生成的日志消息 |
| **backup** | 由备份创建设施生成的日志消息。 |
| **bfd** | 由 BFD 协议生成的日志消息 |
| **bgp** | 由 BGP 协议生成的日志消息 |
| **calc** | 路由计算日志消息。 |
| **caps** | CAPsMAN 无线设备管理 |
| **certificate** | 安全证书 |
| **clock** | 由时钟、IP Cloud 时间更改生成的日志消息。 |
| **dns** | 名称服务器查找相关信息 |
| **ddns** | 由动态 DNS 工具生成的日志消息 |
| **dude** | 与 Dude 服务器包和 The Dude 工具相关的消息 |
| **dhcp** | DHCP 客户端、服务器和中继日志消息 |
| **e-mail** | 由电子邮件工具生成的消息。 |
| **event** | 在路由事件时生成的日志消息。例如，新路由已安装到路由表中。 |
| **firewall** | 当防火墙规则中设置 **action=log** 时生成的防火墙日志消息 |
| **gsm** | 由 GSM 设备生成的日志消息 |
| **hotspot** | 与热点相关的日志条目 |
| **igmp-proxy** | 与 IGMP 代理相关的日志条目 |
| **ipsec** | IPSec 日志条目 |
| **iscsi** |  |
| **isdn** |  |
| **interface** |  |
| **kvm** | 与 KVM 虚拟机功能相关的消息 |
| **l2tp** | 由 L2TP 客户端和服务器生成的日志条目 |
| **lte** | 与 LTE/4G 调制解调器配置相关的消息 |
| **ldp** | LDP 协议相关消息 |
| **manager** | User Manager 日志消息。 |
| **mme** | MME 路由协议消息 |
| **mpls** | MPLS 消息 |
| **ntp** | sNTP 客户端生成的日志条目 |
| **ospf** | OSPF 路由协议消息 |
| **ovpn** | OpenVPN 隧道消息 |
| **pim** | 组播 PIM-SM 相关消息 |
| **ppp** | ppp 设施消息 |
| **pppoe** | PPPoE 服务器/客户端相关消息 |
| **pptp** | PPTP 服务器/客户端相关消息 |
| **radius** | 由 RADIUS 客户端生成的日志条目 |
| **radvd** | IPv6 radv 守护进程日志消息。 |
| **read** | SMS 工具消息 |
| **rip** | RIP 路由协议消息 |
| **route** | 路由设施日志条目 |
| **rsvp** | 资源预留协议生成的消息。 |
| **script** | 从脚本生成的日志条目 |
| **sertcp** | 与负责 "/port remote-access" 的设施相关的日志消息 |
| **simulator** |  |
| **state** | DHCP 客户端和路由状态消息。 |
| **store** | 由 Store 设施生成的日志条目 |
| **smb** | 与 SMB 文件共享系统相关的消息 |
| **snmp** | 与简单网络管理协议（SNMP）配置相关的消息 |
| **system** | 通用系统消息 |
| **telephony** | *已过时！以前由 IP 电话包使用* |
| **tftp** | TFTP 服务器生成的消息 |
| **timer** | 与 RouterOS 中使用的定时器相关的日志消息。例如 bgp keepalive 日志`12:41:40 route,bgp,debug,timer KeepaliveTimer expired``12:41:40 route,bgp,debug,timer     RemoteAddress=2001:470:1f09:131::1` |
| **ups** | 由 UPS 监控工具生成的消息 |
| **vrrp** | 由 VRRP 生成的消息 |
| **watchdog** | 看门狗生成的日志条目 |
| **web-proxy** | 由 Web 代理生成的日志消息 |
| **wireless** | 无线日志条目。 |
| **write** | SMS 工具消息。 |

## 示例

### 创建独立的内存日志缓冲区

创建新的内存日志缓冲区，将指定的日志与默认内存日志分开存储。

```ros
/system/logging/action/add name=dhcpMemoryLog target=memory memory-lines=300
/system/logging/action/add name=wirelessLog target=memory memory-lines=500
```

将主题分配给创建的缓冲区。此规则将所有 DHCP 日志发送到 dhcpMemoryLog，将无线日志发送到 wirelessLog 缓冲区。

```ros
/system/logging/add topics=dhcp action=dhcpMemoryLog
/system/logging/add topics=wireless action=wirelessLog
```

```ros
# 仅查看存储在其专用缓冲区中的 DHCP 相关日志
/log/print where buffer=dhcpMemoryLog

# 仅查看存储在其专用缓冲区中的非信息性无线日志
/log/print where buffer=wirelessLog
```

```ros
/system/logging/action/clear action=dhcpMemoryLog
```

### 记录到文件

要将所有内容记录到文件，请添加新的日志操作：

```ros
/system/logging/action/add name=file target=disk disk-file-name=log
```

然后使所有内容使用此新操作进行记录：

```ros
/system/logging/add action=file
```

您可以通过执行以下命令仅将错误记录到其中：

```ros
/system/logging/add topics=error action=file 
```

这将记录到文件 **log.0.txt** 和 **log.1.txt** 中。

您可以通过指定 *disk-lines-per-file* 来指定文件的最大行数。**\<file>.0.txt** 是活动文件，新日志将追加到其中，一旦其大小达到最大值，它将变为 **\<file>.1.txt**，并创建新的空 **\<file>.0.txt**。

您可以通过在文件名前指定其目录名称来记录到 USB 闪存盘或 *MicroSD/CF*（在 Routerboards 上）。例如，如果您在 */files* 下有一个可访问的 USB 闪存盘作为 **usb1** 目录，则应执行以下命令：

```ros
/system/logging/action/add name=usb target=disk disk-file-name=usb1/log
```

:::warning
重启后，文件中的日志条目将重新存储到内存中。
:::