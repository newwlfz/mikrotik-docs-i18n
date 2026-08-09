# 带宽测试

> MikroTik RouterOS 中的带宽测试功能允许使用 TCP 或 UDP 协议测量路由器之间的网络吞吐量，并详细说明其行为与限制。该功能包含带宽服务器的配置选项，如端口范围、认证和会话限制，并提供了无需客户端认证即可启用服务器的示例。

# 带宽测试

**子菜单：** `/tool` **所需软件包：** `system`

带宽测试器可用于测量到另一台 MikroTik 路由器（有线或无线）的吞吐量，从而帮助发现网络“瓶颈”。

TCP 测试使用带有确认的标准 TCP 协议，并根据延迟、丢包以及 TCP 算法中的其他特性，遵循 TCP 算法决定发送多少数据包。有关其内部速度设置及如何分析其行为的详细信息，请参阅 TCP 协议文档。吞吐量统计基于整个 TCP 数据流的大小计算。由于确认是 TCP 的内部工作机制，其大小和链路占用不包含在吞吐量统计中。因此，在估算吞吐量时，该统计不如 UDP 统计可靠。

UDP 测试器发送的数据包数量比链路另一端当前报告接收到的数量多 110% 或更多。要查看链路的最大吞吐量，应将数据包大小设置为链路允许的最大 MTU，通常为 1500 字节。UDP 不需要确认；这种实现方式意味着可以观察到最接近实际吞吐量的近似值。

:::warning
带宽测试会占用所有可用带宽和系统资源，可能影响网络可用性。如果要测试路由器的真实吞吐量，应通过被测路由器运行带宽测试，而不是从该路由器本身发起或向其本身发起。为此，您需要至少 3 台路由器串联连接：带宽服务器、被测路由器和带宽客户端。
:::

:::note
如果使用 UDP 协议，则带宽测试统计 IP 头 + UDP 头 + UDP 数据。如果使用 TCP，则带宽测试仅统计 TCP 数据（不包含 TCP 头和 IP 头）。
:::

## 带宽测试服务器

|  |  |
| :-- | :-- |
**子菜单：** `/tool/bandwidth-server`

| 属性 | 说明 |
| :-- | :-- |
| **allocate-udp-ports-from** (*整数 1000..64000*；默认值：**2000**) | UDP 端口范围的起始值 |
| **authenticate** (*yes \| no*；默认值：**yes**) | 仅与经过认证的客户端通信 |
| **enabled** (*yes \| no*；默认值：**yes**) | 定义带宽服务器是否启用 |
| **max-sessions** (*整数 1..1000*；默认值：**100**) | 最大同时测试数量 |

### 示例

带宽服务器：

```ros
[admin@MikroTik] /tool/bandwidth-server> print                                  
                  enabled: yes                                                  
             authenticate: yes                                                  
  allocate-udp-ports-from: 2000                                                 
             max-sessions: 100                                                  
[admin@MikroTik] /tool/bandwidth-server>
```

活动会话：

```ros
[admin@MikroTik] /tool/bandwidth-server/session> print
  # CLIENT          PROTOCOL DIRECTION USER
  0 35.35.35.1      udp      send      admin
  1 25.25.25.1      udp      send      admin
  2 36.36.36.1      udp      send      admin
[admin@MikroTik] /tool/bandwidth-server/session>
```

启用 **bandwidth-test** 服务器且无需客户端认证：

```ros
[admin@MikroTik] /tool/bandwidth-server> set enabled=yes authenticate=no        
[admin@MikroTik] /tool/bandwidth-server> print                                  
                  enabled: yes                                                  
             authenticate: no                                                   
  allocate-udp-ports-from: 2000                                                 
             max-sessions: 100                                                  
[admin@MikroTik] /tool/bandwidth-server>
```

## 带宽测试客户端

**子菜单：** `/tool/bandwidth-test`

| 属性 | 说明 |
| :-- | :-- |
| **address** (*IP 地址 \| IPv6 前缀[%接口]*；默认值：) | 主机 IP 地址 |
| **direction** (*both \| receive \| transmit*；默认值：**receive**)  | 数据流方向 |
| **duration** (*时间*；默认值：) | 测试持续时间 |
| **interval** (*时间：20ms..5s*；默认值：**1s**) | 报告间隔（秒） |
| **local-tx-speed** (*整数 0..18446744073709551615*；默认值：) | 发送测试最大速度（比特/秒） |
| **local-udp-tx-size** (*整数：28..64000*) | 本地发送数据包大小（字节） |
| **password** (*字符串*；默认值：**""**) | 远程用户密码 |
| **protocol** (*udp \| tcp*；默认值：**udp**) | 使用的协议 |
| **random-data** (*yes \| no*；默认值：**no**) | 如果 random-data 设置为 yes，带宽测试数据包的负载将包含不可压缩的随机数据流，以避免使用数据压缩的链路扭曲测试结果（此选项会占用大量 CPU，对于低性能 CPU 应将 random-data 设置为 no） |
| **remote-tx-speed** (*整数 0..18446744073709551615*；默认值：) | 接收测试最大速度（比特/秒） |
| **remote-udp-tx-size** (*整数：28..64000*) | 远程发送数据包大小（字节） |
| **connection-count** (*整数 1..255*；默认值：) | 使用的 TCP 连接数 |
| **user** (*字符串*；默认值：**""**) | 远程用户 |

### 示例

对 **10.0.0.32** 主机运行 15 秒带宽测试，发送和接收 **1000** 字节 UDP 数据包，并使用用户名 **admin** 连接：

```ros
[admin@MikroTik] /tool> bandwidth-test 10.0.0.32 duration=15s \
\... direction=both local-udp-tx-size=1000 protocol=udp \
\... remote-udp-tx-size=1000 user=admin
                status: done testing
              duration: 15s
            tx-current: 272.8Mbps
  tx-10-second-average: 200.3Mbps
      tx-total-average: 139.5Mbps
            rx-current: 169.6Mbps
  rx-10-second-average: 164.8Mbps
      rx-total-average: 117.0Mbps
          lost-packets: 373
           random-data: no
             direction: both
               tx-size: 1000
               rx-size: 1000
[admin@MikroTik] /tool>
```

### 链路本地 IPv6 示例

```ros
[admin@MikroTik] > /tool/bandwidth-test fe80::34:23ff:fe6a:570c%local
                status: running
              duration: 5s
            rx-current: 23.9Mbps
  rx-10-second-average: 15.1Mbps
      rx-total-average: 15.1Mbps
          lost-packets: 0
           random-data: no
             direction: receive
               rx-size: 1500
```