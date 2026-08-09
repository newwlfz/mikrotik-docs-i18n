# MAC 服务器

> RouterOS 中的 MAC 服务器部分允许配置 MAC Telnet、WinBox 和 Ping 服务器，以便在没有 IP 地址的情况下访问路由器。它允许限制对特定接口的访问，并提供管理会话的工具，示例展示了如何启用/禁用 MAC Telnet 以及通过客户端进行连接。

# MAC 服务器

MAC 服务器部分允许您在 RouterOS 设备上配置 MAC Telnet 服务器、MAC WinBox 服务器和 MAC Ping 服务器。

MAC Telnet 用于为未设置 IP 地址的路由器提供访问。它的工作方式与 IP Telnet 类似。MAC Telnet 仅可在两台 MikroTik RouterOS 路由器之间使用。

MAC WinBox 用于通过 MAC 地址为路由器提供 WinBox 访问。

MAC Ping 用于允许对路由器的 MAC 地址进行 MAC Ping 操作。

:::info
**MAC-server** 设置包含在“system”软件包中。

:::

### MAC Telnet 服务器

可以将 MAC Telnet 访问权限设置为仅允许 [接口列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md) 中的特定接口：

```ros
[admin@device] /tool/mac-server/set allowed-interface-list=listBridge
[admin@device] /tool/mac-server/print
  allowed-interface-list: listBridge
```

在上述示例中，MAC Telnet 配置为仅允许接口列表“listBridge”中的接口，因此 MAC Telnet 将仅通过该列表中的接口工作（您可以将多个接口添加到列表中）。

要禁用 MAC Telnet 访问，请执行以下命令（将“allowed-interface-list”设置为“none”）：

```ros
[admin@device] /tool/mac-server/set allowed-interface-list=none
[admin@device] /tool/mac-server/print
  allowed-interface-list: none
```

您可以使用以下命令检查活动的 MAC Telnet 会话（设备已接受的会话）：

```ros
[admin@device] > /tool/mac-server/sessions/print
Columns: INTERFACE, SRC-ADDRESS, UPTIME
#  INTERFACE  SRC-ADDRESS        UPTIME
0  ether5     64:D1:54:FB:E3:E6  17s 
```

#### MAC Telnet 客户端

当 MAC Telnet 服务器启用时，您可以使用另一台 RouterOS 设备通过 mac-telnet 客户端连接到服务器：

```ros
[admin@device2] > tool mac-telnet B8:69:F4:7F:F2:E7    
Login: admin
Password: 
Trying B8:69:F4:7F:F2:E7...
Connected to B8:69:F4:7F:F2:E7

  MMM      MMM       KKK                          TTTTTTTTTTT      KKK
  MMMM    MMMM       KKK                          TTTTTTTTTTT      KKK
  MMM MMMM MMM  III  KKK  KKK  RRRRRR     OOOOOO      TTT     III  KKK  KKK
  MMM  MM  MMM  III  KKKKK     RRR  RRR  OOO  OOO     TTT     III  KKKKK
  MMM      MMM  III  KKK KKK   RRRRRR    OOO  OOO     TTT     III  KKK KKK
  MMM      MMM  III  KKK  KKK  RRR  RRR   OOOOOO      TTT     III  KKK  KKK

  MikroTik RouterOS 7.1rc3 (c) 1999-2021       https://www.mikrotik.com/

Press F1 for help
  
[admin@device] > 
```

根据您的配置更改 MAC 地址，您应该能够进入服务器的 CLI（如上例所示）。

:::tip
默认情况下，MAC Telnet 客户端会尝试通过所有活动接口到达目的地。这可能会产生不必要的流量。要将 MAC Telnet 客户端限制到特定接口，请使用 `interface` 属性（自 RouterOS v7.22 起可用）。例如：`/tool/mac-telnet 00:11:22:33:44:55 interface=ether1`

:::

#### MAC 扫描

MAC 扫描功能可发现给定网络上所有支持 MAC Telnet 协议的设备。该命令要求您选择要扫描的接口：

```ros
[admin@Sw_Denissm] > /tool/mac-scan interface=all           
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            26
2C:C8:1B:FD:F2:C3 192.168.69.3            56
```

在上述示例中，选择了所有接口，扫描将持续运行，除非手动停止（按“q”键）。

您还可以添加“duration”参数来指定扫描持续的时间：

```ros
[admin@Sw_Denissm] > /tool/mac-scan interface=all duration=1
MAC-ADDRESS       ADDRESS                AGE
B8:69:F4:7F:F2:E7 192.168.69.1            48
2C:C8:1B:FD:F2:C3 192.168.69.3            17
```

在上述示例中，我们将“duration”参数设置为 1 秒。

### MAC WinBox 服务器

与 MAC Telnet 相同，可以将 MAC WinBox 访问权限设置为仅允许 [接口列表](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md) 中的特定接口：

```ros
[admin@device] > /tool/mac-server/mac-winbox/set allowed-interface-list=listBridge 
[admin@device] > /tool/mac-server/mac-winbox/print                   
  allowed-interface-list: listBridge
```

在上述示例中，MAC WinBox 访问配置为仅允许接口列表“listBridge”中的接口，因此 MAC WinBox 将仅通过该列表中的接口工作。

要禁用 MAC WinBox 访问，请执行以下命令（将“allowed-interface-list”设置为“none”）：

```ros
[admin@device] > /tool/mac-server/mac-winbox/set allowed-interface-list=none
[admin@device] > tool mac-server mac-winbox print                   
  allowed-interface-list: none
```

### MAC Ping 服务器

MAC Ping 服务器可以设置为“disabled”（禁用）或“enabled”（启用）：

```ros
[admin@device] > /tool/mac-server/ping/print
  enabled: yes
```

您可以使用以下命令启用或禁用 MAC Ping（**enable=yes** → 启用该功能；**enable=no** → 禁用该功能）：

```ros
[admin@device] > /tool/mac-server/ping/set enabled=yes
[admin@device] > /tool/mac-server/ping/set enabled=no
```

当 MAC Ping 启用时，同一广播域中的其他主机可以使用 ping 工具对 MAC 地址进行 ping 操作。例如，您可以执行以下命令来检查 MAC Ping 结果：

```ros
[admin@device] > /ping 00:0C:42:72:A1:B0
HOST                                    SIZE  TTL TIME  STATUS                                         
00:0C:42:72:A1:B0                       56        0ms  
00:0C:42:72:A1:B0                       56        0ms  
    sent=2 received=2 packet-loss=0% min-rtt=0ms avg-rtt=0ms max-rtt=0ms 
```

:::warning
如果您禁用了 **MAC 服务器 ping** 功能，主机的 **ARP ping** 功能也将被禁用。

:::

:::tip
默认情况下，MAC Ping 会尝试通过所有活动接口到达目的地。如果目的地可通过多个接口访问，这可能会产生不必要的流量和重复回复。要将 MAC Ping 限制到特定接口，请使用接口选择器（在 MAC 地址后附加 `%` 和接口名称）。例如：`/ping 00:11:22:33:44:55%ether1`

:::