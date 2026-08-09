# 检测互联网

> 检测互联网是 RouterOS 的一项工具，用于将受监控的接口分类为互联网、WAN、LAN 和未知等状态，并针对 DHCP 客户端安装及基于链路状态和云可达性的状态转换提供警告。

# 检测互联网

检测互联网是一种工具，可将受监控的接口分类为以下状态 - **互联网**、**WAN**、**LAN**、**未知**、**从属** 和 **无链路**。

:::warning
请注意，检测互联网可以安装 DHCP 客户端、默认路由、DNS 服务器，并可能影响其他功能。
请谨慎使用，并在启用该服务后，检查它如何干扰您的其他配置。
:::

### 状态

此子菜单显示由 *detect-interface-list* 参数定义的所有受监控接口的状态：

```ros
/interface/detect-internet/state/print
```

### LAN

所有二层接口初始状态均为该状态。

### WAN

所有三层隧道和 LTE 接口初始状态均为该状态。二层接口在满足以下条件时可获得该状态：

- 接口在主路由表中具有通往 8.8.8.8 的活动路由。
- 接口可以从 DHCP 获取（创建动态 DHCP 客户端）或已获取地址（如果 DHCP 服务器也在 DHCP 服务器接口上运行检测互联网，则不适用）。

:::warning
WAN 接口仅在链路状态变化时才能回退到 LAN 状态。LAN 接口在 1 小时后锁定为 LAN，之后仅在链路状态变化时才会改变。
:::

### 互联网

能够使用 UDP 协议端口 30000 访问 cloud.mikrotik.com 的 *WAN* 接口可获得该状态。可达性每 2 分钟检查一次。默认情况下，如果 4 分钟内未到达云，状态将回退为 **WAN**。

## 配置

**子菜单：** `/interface/detect-internet`

| 属性 | 描述 |
| :-- | :-- |
| **detect-interface-list** (*接口列表*；默认值：**无**) | 列表中的所有接口将由检测互联网监控 |
| **internet-interface-list** (*接口列表*；默认值：**无**) | 状态为互联网的接口将动态添加到此列表 |
| **lan-interface-list** (*接口列表*；默认值：**无**) | 状态为 LAN 的接口将动态添加到此列表 |
| **wan-interface-list** (*接口列表*；默认值：**无**) | 状态为 WAN 的接口将动态添加到此列表 |
| **request-interval** (*时间*；默认值：**2m**) | 接口状态检查的时间间隔 |

```ros
[admin@MikroTik] > /interface/detect-internet/print 
detect-interface-list: none
lan-interface-list: none
wan-interface-list: none
internet-interface-list: none
[admin@MikroTik] > /interface/detect-internet/set internet-interface-list=all wan-interface-list=all lan-interface-list=all detect-interface-list=all 
[admin@MikroTik] > /interface/detect-internet/state/print 
Columns: NAME, STATE, STATE-CHANGE-TIME, CLOUD-RTT
# NAME STATE STATE-CHANGE-TIME CLO
0 ether1 internet 2020-12-22 13:46:18 5ms
```