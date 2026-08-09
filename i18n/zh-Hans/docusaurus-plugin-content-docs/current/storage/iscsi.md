# iSCSI

> iSCSI 支持基于 IP 的存储访问，RouterOS 同时支持目标端（Target）和发起端（Initiator）模式，具备 iSCSI 地址、IQN 标识符以及可配置端口等属性，适用于客户端和服务器角色。

# iSCSI

:::info
此功能需要 [Storage](./index.md) 软件包。
:::

iSCSI 允许通过基于 IP 的网络访问存储。在发起端，iSCSI 设备将显示为块设备。RouterOS 同时支持目标端和发起端模式。

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **iscsi-address** | iSCSI 目标端的 IP 地址。（主机设备 IP） |
| **iscsi-export** | 在主机设备上禁用/启用 iSCSI |
| **iscsi-iqn** | 用于命名 iSCSI 目标端的唯一标识符。 |
| **iscsi-port** | iSCSI 目标端用于监听来自发起端传入连接的网络端口。iSCSI 流量的默认端口为 3260。 |
| **iscsi-server-iqn** | iSCSI 服务器使用的唯一标识符。默认情况下，IQN 格式为 iqn.2000-02.com.mikrotik:*slot*（自 7.21beta2 起） |
| **iscsi-server-port** | iSCSI 服务器使用的网络端口。（自 7.21beta2 起） |

## 配置示例

主机端

```ros
/disk
set pcie1-nvme1 iscsi-export=yes
```

客户端

```ros
/disk
add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=iqn.2000-02.com.mikrotik:pcie1-nvme1
```