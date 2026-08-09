# PWR Line

> PWR-Line 页面描述了 MikroTik RouterOS 设备，这些设备利用 HomePlug AV 标准，通过电力线实现类似以太网的连接，并详细介绍了接口属性（如 ARP 模式和带宽限制）以及用于网络密钥管理和设备配对的配置命令。

# PWR Line

PWR-Line 系列设备允许在普通电力线上，于受支持的设备之间建立类似以太网的连接。当插入同一电路时，PWR-Line 设备将通过使用 HomePlug AV 标准来建立连接。

## 属性

|  |  |
| :-- | :-- |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | 地址解析协议模式：disabled - 接口将不使用 ARP；enabled - 接口将使用 ARP；proxy-arp - 接口将使用 ARP 代理功能；reply-only - 接口将仅回复来自 `/ip/arp` 表中静态条目匹配的 IP 地址/MAC 地址组合的请求。ARP 表中不会自动存储动态条目。因此，为了通信成功，必须已存在有效的静态条目。 |
| **bandwidth** (*integer/integer*; 默认值：**unlimited/unlimited**) | 设置接口将处理的最大 rx/tx 带宽（以 kbps 为单位）。TX 限制在所有 Atheros [交换芯片](../bridging-and-switching/switch-chip-features.md) 端口上受支持。RX 限制仅在 Atheros8327/QCA8337 交换芯片端口上受支持。 |
| **comment** (*string*; 默认值：) | 项目的描述性名称 |
| **l2mtu** (*integer [0..65536]*; 默认值：) | 二层最大传输单元。[RouterOS 中的 MTU](../hardware/mtu-in-routeros.md) |
| **mac-address** (*MAC*; 默认值：) | 接口的媒体访问控制号码。 |
| **mtu** (*integer [0..65536]*; 默认值：**1500**) | 三层最大传输单元 |
| **name** (*string*; 默认值：) | 接口名称 |
| **orig-mac-address** (*MAC*; 默认值：) |  |
| **rx-flow-control** (*on \| off \| auto*; 默认值：**off**) | 设置为 on 时，端口将处理接收到的暂停帧，并在需要时暂停传输。**auto** 与 **on** 相同，除非 auto-negotiation=yes，此时流控状态通过考虑对端通告的内容来确定。该功能在 AR724x、AR9xxx 和 QCA9xxx CPU 端口、所有 CCR 端口以及所有 Atheros 交换芯片端口上受支持。 |
| **tx-flow-control** (*on \| off \| auto*; 默认值：**off**) | 设置为 on 时，当达到特定缓冲区使用阈值时，端口将发送暂停帧。**auto** 与 **on** 相同，除非 auto-negotiation=yes，此时流控状态通过考虑对端通告的内容来确定。该功能在 AR724x、AR9xxx 和 QCA9xxx CPU 端口、所有 CCR 端口以及所有 Atheros 交换芯片端口上受支持。 |

## 菜单特定命令

| 属性 | 描述 |
| :-- | :-- |
| **configure** () | 该命令配置所连接的 PWR-Line 设备的网络密钥、网络密码、plc-cco-selection-mode。 |
| **join** () | 启动配对序列，该序列将寻找同一电路中同样处于配对模式的其他 PWR-Line 设备。此模式持续 120 秒。 |
| **leave** () | 启动离开序列，该序列实质上会随机化设备的网络密钥。 |
| **monitor** () | 实时输出与 PWR-Line 相关的状态。 |
| **upgrade-firmware** () | 使用指定的固件文件和 pib 文件升级 PWR-Line 设备。 |

## 配置示例

为了使两个或多个设备能够相互连接，它们必须共享相同的网络密钥值。当前配置的网络密钥可以使用 monitor 命令查看，显示为 plc-actual-network-key。

```ros
[admin@MikroTik] > /interface/pwr-line/monitor pwr-line1 
name: pwr-line1
connection-to-plc: ok
tx-flow-control: no
rx-flow-control: no
plc-actual-network-key: c973947c200e1540b0f84b571d92bebe
plc-hw-platform: QCA7420
plc-sw-platform: MAC
plc-fw-version: 1.4.0(24-20180515-CS)
plc-line-freq: 50Hz
plc-zero-crossing: detected
plc-mac: B8:69:F4:C4:34:68
```

### 方法 1

有两种方法可以在不同设备上设置相同的网络密钥。您可以使用 network-key 参数（它是 network-password 参数的哈希版本），或者使用 network-password 参数并让路由器对可读字符串应用哈希。

例如：

```ros
/interface/pwr-line/configure pwr-line1 network-password=mynetwork
```

等同于：

```ros
/interface/pwr-line/configure pwr-line1 network-key=cb01fcc6167bf3d1edb1433c2ebde4b3
```

您必须在所有希望相互通信的设备上设置相同的密钥或密码。

### 方法 2

可以使用 join 和 leave 命令，使 PWR-Line 设备自动同步网络密钥值。建议在使用 join 命令之前使用 leave 命令，以确保生成新的随机网络密钥，并且设备不属于任何旧网络。

```ros
/interface/pwr-line/leave pwr-line1
```

然后我们可以发出 join 命令。这样做时，配对序列将启用 120 秒，这意味着您必须在 120 秒内在另一台设备上启用配对模式，它们才能成功配对。

```ros
/interface/pwr-line/join pwr-line1
```

### 方法 3

还可以使用 plc-cco-selection-mode 参数为 PWR-Line 设备设置指定角色（主设备或从设备）。

| 属性 | 描述 |
| :-- | :-- |
| **plc-cco-selection-mode** (*auto \| always \| never*; 默认值：**auto**) | 设置 PWR-Line 设备模式：auto - PWR-Line 将根据情况自动决定在加入 PWR-Line 网络时承担何种角色。always - PWR-Line 将始终被强制充当“中央协调器”或主设备。never - PWR-Line 将始终被强制充当从设备。 |

示例：

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=auto
```

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=always
```

```ros
/interface/pwr-line/configure pwr-line1 plc-cco-selection-mode=never
```

## 同步按钮使用

- 按住 0.5 – 3 秒以开启同步模式。在 120 秒内，它将尝试与另一台 PWR-LINE 设备通信。闪烁的橙色 LED 灯表示其处于搜索模式。您还需要在另一台 PWR-LINE 设备上执行相同操作，以便它们能够同步。再次按下按钮可取消搜索。您也可以在 RouterOS 设置中手动设置安全密钥。

- 按住 5 – 8 秒以生成新的安全密钥。这用于将 PWR-LINE 设备从现有的 PWR-LINE 网络中移除。

- 按住 10 – 15 秒以重置所有与 PWR-LINE 相关的设置。

## 支持的硬件

该设备与我们的 PWR-LINE AP 完全兼容，并且具有 MicroUSB 端口的最新产品修订版（如 hAP lite、hAP lite tower、hAP mini、mAP 和 mAP lite）具有 pwr-line 接口。简单的软件升级至 v6.44+ 即可启用此功能（由上述序列号以 /9xx 结尾的设备支持）。PWR-LINE 功能也受一些先前制造的单元支持 - 如果您的单元序列号以 /8xx 结尾，请升级至 6.44+ 并查看 pwr-line 接口是否出现。