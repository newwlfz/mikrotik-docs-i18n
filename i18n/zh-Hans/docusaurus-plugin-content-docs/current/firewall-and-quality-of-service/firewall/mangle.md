# Mangle

> RouterOS 中的 Mangle 用于为数据包打上特殊标记，以便进行高级处理，从而支持队列树和 NAT 等功能。它通过修改 IP 头部字段，并利用五个预定义链（PREROUTING、INPUT、OUTPUT、FORWARD、POSTROUTING）来根据数据包标记或连接状态应用规则。

# Mangle

Mangle 是一种“标记器”，它通过特殊标记为数据包做标记，以便后续处理。RouterOS 中的许多其他功能（如队列树、NAT、路由）都会利用这些标记。它们根据数据包的标记来识别数据包，并据此进行处理。Mangle 标记仅存在于路由器内部，不会通过网络传输。

此外，Mangle 功能还用于修改 IP 头部中的某些字段，例如 TOS（DSCP）和 TTL 字段。

防火墙 Mangle 规则由五个预定义链组成，这些链无法删除：

![](https://manual.mikrotik.com/docs/firewall-and-quality-of-service/firewall/img/mangle-01.webp)

- **PREROUTING** 链：此链中的规则适用于刚到达网络接口的数据包。
- **INPUT** 链：此链中的规则适用于即将交付给本地进程的数据包。
- **OUTPUT** 链：此链中的规则适用于进程刚生成的数据包。
- **FORWARD** 链：此链中的规则适用于通过当前主机路由的任何数据包。
- **POSTROUTING** 链：此链中的规则适用于刚离开网络接口的数据包。

## 配置示例

### 修改 MSS

众所周知，由于封装开销，VPN 链路的报文大小较小。如果数据包的 MSS 超过 VPN 链路的 MSS，则在通过此类连接发送之前应进行分片。但是，如果数据包设置了 *Don't Fragment* 标志，则无法分片，应将其丢弃。在路径 MTU 发现（PMTUD）功能异常的链路上，这可能会导致许多问题，包括 FTP 和 HTTP 数据传输以及电子邮件服务的问题。

在 PMTUD 功能异常的链路情况下，减小通过 VPN 链路的数据包的 MSS 可以解决该问题。以下示例演示了如何通过 Mangle 减小 MSS 值：

```ros
/ip/firewall/mangle/add out-interface=pppoe-out protocol=tcp tcp-flags=syn action=change-mss new-mss=1300 chain=forward tcp-mss=1301-65535
```

### 标记连接

有时需要对属于特定连接的数据包执行某些操作（例如，为来自/发往特定主机的数据包打标记以用于队列），但检查每个数据包的 IP 头部是一项相当耗费资源的任务。我们可以使用连接标记来优化配置。

```ros
/ip/firewall/mangle
add chain=forward in-interface=local src-address=192.168.88.123 connection-state=new action=mark-connection new-connection-mark=client_conn
add chain=forward connection-mark=client_conn action=mark-packet new-packet-mark=client_p
```

:::danger
警告：数据包标记最多只能有 4096 个唯一条目。超过此限制将导致错误“bad new packet mark”。
:::