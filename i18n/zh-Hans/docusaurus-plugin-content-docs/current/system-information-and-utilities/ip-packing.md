# IP 打包

> IP 打包功能可在 RouterOS 的网络链路上实现数据包聚合与压缩，要求两端对称配置并启用发现协议。它支持多种操作，如简单聚合或对头部及负载进行压缩，同时需注意可能增加的延迟。

# IP 打包

IP 打包为网络链路提供数据包封装服务。它支持将简单数据包聚合为更大的数据包，并对数据包内容进行压缩。

## 要求

数据包打包属于系统包的一部分，且必须在接口上启用发现协议。

### 配置

**子菜单：** `/ip/packing`

配置需在两处进行，两台路由器应对称设置：

- `/ip/packing` - 用于在接口上启用数据包聚合和/或压缩。
- `/ip/neighbor/discovery-settings` - 用于在接口上启用发现协议。

### 打包配置

| 属性 | 描述 |
| :-- | :-- |
| aggregated-size（*20 .. 16384 默认值：**1500***） | 打包在发送数据包前尝试达到的聚合数据包大小 |
| disabled（*yes\|no*） | 打包规则的状态，若值为 *yes*，该规则将被忽略，不参与活动配置 |
| interface（*接口名称*） | 打包将尝试聚合和/或压缩来自此接口的数据包 |
| packing（*simple\|compress-all\|compress-headers\|none*） | 当数据包离开配置了打包规则的接口时应执行的操作：<code>simple</code> - 仅聚合数据包<code>compress-all</code> - 执行聚合并尝试压缩数据包的头部和负载<code>compress-headers</code> - 执行聚合并尝试压缩头部，保持数据包负载不变<code>none</code> - 按原样发送数据包 |
| unpacking（*simple\|compress-all\|compress-headers\|none*） | 当在配置了打包规则的接口上接收到数据包时应执行的操作：<code>simple</code> - 从接口接收的聚合数据包中解包数据包<code>compress-all</code> - 解包聚合数据包并解压缩数据包的头部和负载<code>compress-headers</code> - 解包聚合数据包并解压缩数据包的头部<code>none</code> - 对接收的数据包不执行任何操作 |

:::danger
路由器应被视为在您要启用打包的接口上的邻居路由器。如果邻居列表中没有指示打包的条目，则打包未生效！

**警告：** 打包可能会增加所配置链路上的延迟。
:::

## 示例

Router-A 和 Router-B 通过线缆连接，Router-A 使用 ether1 接口，Router-B 使用 ether3 接口。本示例将聚合来自 Router-A 的数据包，但保持来自 Router-B 的数据包不变。在 Router-A 上：

确保已启用发现：

```ros
 /ip/neighbor/discovery/set ether1 discover=yes 
```

为接口添加打包规则：

```ros
 /ip/packing/add interface=ether1 aggregated-size=1500 packing=simple unpacking=none 
```

在 Router-B 上：

确保已启用发现：

```ros
 /ip/neighbor/discovery/set ether3 discover=yes 
```

为接口添加打包规则：

```ros
 /ip/packing/add interface=ether3 aggregated-size=1500 packing=none unpacking=simple
```