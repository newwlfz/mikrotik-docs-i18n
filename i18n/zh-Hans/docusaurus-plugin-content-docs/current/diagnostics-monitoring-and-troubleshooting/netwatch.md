# Netwatch

> Netwatch 使用多种探测类型（包括 ICMP、TCP、HTTP、DNS 和简单 ping）来监控网络主机。它允许为状态变化自定义脚本，并支持 VRF 和链路本地 IPv6 地址，且具有可配置的阈值和间隔设置。

# Netwatch

[*Netwatch CLI 参考*](../cli-reference/tool/netwatch)

Netwatch 监控网络中主机的状态。监控可通过以下探测类型完成：
1) [**简单 (Simple)**](#simple-probe) - 使用 ping，不采用高级指标
2) [**ICMP**](#icmp-probe) - 向指定 IP 地址（主机）发送 ping，并可调整阈值
3) [**TCP-conn**](#tcp-conn-probe) - 测试 TCP 连接
4) [**HTTP-GET**](#http-get-probe) - 向被监控的服务器发送请求
5) [**HTTPS-GET**](#https-get-probe) - 向被监控的服务器发送请求
6) [**DNS**](#dns-probe) - 向 DNS 服务器发送 DNS 查询并检查响应。

## 通用配置信息

本节涵盖与所有 Netwatch 探测类型相关的信息。

* 始终使用 Netwatch 默认值 - **即使未由用户定义**。可配置变量列表（含默认值）及只读/统计变量可在 [Netwatch CLI 参考页面](../cli-reference/tool/netwatch) 查看。请务必检查默认变量是否适用于您的使用场景。

* 对于所有探测类型，`host` 变量为必填项，因为它定义了应被监控设备的地址。

* Netwatch 探测可根据探测状态变化执行脚本，允许 RouterOS 动态调整路由器配置或发送通知（*更多信息，请参阅 [脚本编写文档](../developer-guides/scripting)*）。Netwatch 支持三种脚本类型，每种在不同条件下执行：

  * `up-script` 在状态从 **未知 (Unknown)**（*取决于 `ignore-initial-up` 变量；更多信息请参阅 [CLI 参考](../cli-reference/tool/netwatch)*）或 **Down** 变为 **Up** 时执行；
  * `down-script` 在状态从 **未知 (Unknown)**（*取决于 `ignore-initial-down` 变量；更多信息请参阅 [CLI 参考](../cli-reference/tool/netwatch)*）或 **Up** 变为 **Down** 时执行；
  * `test-script` 在每次探测测试期间执行。

* 如果未为探测指定脚本，仍可在日志中观察探测状态变化。当启用 `info` 主题的 [日志](../diagnostics-monitoring-and-troubleshooting/log) 时，探测标识信息和状态变化会打印到日志中。详细的探测统计和配置会打印到 `debug` 主题级别。

* 您可以查看统计信息并在脚本中使用这些变量。请注意，包含 "-" 的变量必须这样书写，例如，"done-tests" 应写为 $"done-tests"

* Netwatch 以 *sys 用户身份执行脚本，因此 Netwatch 脚本中定义的任何全局变量将无法被例如 [调度器](../system-information-and-utilities/scheduler) 或其他用户读取。

* Netwatch 仅限于 *read,write,test,reboot* [脚本策略](../developer-guides/scripting)。如果脚本所有者没有足够权限执行脚本中的某个命令，则该脚本将不会被执行。如果脚本具有比 *read,write,test,reboot* 更高的策略，则该脚本同样不会被执行。请确保您的脚本不超过上述策略。

* 可以在 *`/system/scripts`* 菜单下禁用 RouterOS 脚本的权限检查（[脚本编写文档](../developer-guides/scripting)）。当 Netwatch 没有足够权限执行脚本时，这很有用，但这会降低整体安全性。建议为脚本分配适当的权限。

* 简单 (Simple)、ICMP、HTTP 和 TCP-connect 探测在发送时会设置“不分片 (don't fragment)”标志。使用 ICMP 探测时，您可以设置 `packet-size`，结合 DF 标志，可用于辅助 [路径 MTU 发现](../hardware/mtu-in-routeros)。

## 简单探测 (Simple probe)

定期发送简单的 ICMP ping 请求以检查主机可用性。仅通用探测参数适用于此探测类型。

### 配置示例

检查 Google DNS 服务的简单探测配置，包含记录探测状态变化的脚本。

```ros
/tool/netwatch/add host=8.8.8.8 up-script=":log info \"Ping to 8.8.8.8 successful\"" down-script=":log info \"Ping to 8.8.8.8 failed\""
```

在此示例中，配置了一个简单探测来检查 8.8.8.8 是否可通过 ping 访问。当探测状态变化时，会根据状态变化的类型创建日志条目。

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_01_simple_probe_example_winbox](img/netwatch_01_simple_probe_example.webp)

在日志部分，您可以看到 Netwatch 执行了脚本。下面的示例显示了 `up-script` 的执行和 Netwatch 状态变化。在这种情况下，必须启用 `info` 主题的日志记录，这些日志条目才会出现。

```ros
[admin@MikroTik] > /log/print where message~"8.8.8.8"
 2026-06-10 14:48:17 netwatch,info event up [ type: simple, host: 8.8.8.8 ]
 2026-06-10 14:48:17 script,info Ping to 8.8.8.8 successful
```

## ICMP 探测

`simple` 探测类型的更高级版本，也使用 ICMP 数据包检查主机状态。与 `simple` 探测类型相比，`ICMP` 允许更复杂的阈值配置，并且可以发送多个 ICMP ping 数据包，而不仅仅是一个。

### 配置示例

此示例展示如何使用 `ICMP` 探测阈值，此示例使用 `thr-avg` 阈值来监控到服务器的平均往返时间。

```ros
/tool/netwatch/add host=8.8.8.8 type=icmp thr-avg=10ms up-script=":log info \"rtt average is \$\"rtt-avg\", threshold passed, ping to 8\
    .8.8.8 successful\"" down-script=":if (\$\"loss-percent\" < 85) do={ :log info \"rtt average i\
    s \$\"rtt-avg\", which is higher then threshold, please check connection\" } else={ :\
    log info \"Ping to 8.8.8.8 failed\"}"
```

该探测检查 8.8.8.8 是否可通过 ping 访问，并额外验证 `rtt-avg` 值是否小于 10 毫秒。`up-script` 和 `down-script` 在执行时都会记录 `rtt-avg` 值，除非 `down-script` 是由 85% 或更高的数据包丢失触发。这可以区分由数据包丢失引起的探测失败和由未达到配置阈值引起的失败。

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_02_ICMP_probe_example_winbox](img/netwatch_02_ICMP_probe_example.webp)

下面的示例显示了 `up-script` 的执行和 Netwatch 状态变化。如图所示，平均 RTT 值以微秒为单位的原始值传递，因此在编写 Netwatch 脚本时请务必考虑到这一点。

```ros
 2026-06-17 10:31:01 netwatch,info event up [ type: icmp, host: 8.8.8.8 ]
 2026-06-17 10:31:01 script,info rtt average is 7686, threshold passed, ping to 8.8.8.8 successful
```

## TCP-conn 探测

`tcp-conn` 探测类型检查路由器是否能在特定 TCP 端口上与主机建立 TCP 连接。这允许监控设备上的特定服务，而不是通过 ICMP 监控设备的整体可用性。

### 配置示例

此示例使用 `tcp-conn` 探测类型检查 8.8.8.8 的 DNS 端口是否正常运行。

```ros
/tool/netwatch/add host=8.8.8.8 type=tcp-conn port=53 up-script=":log info \"TCP handshake to 8.8.8.8:53 successful\"" down-script=":log info \"TCP handshake to 8.8.8.8:53 failed\""
```

`tcp-conn` 探测专门检查 TCP 端口 53（DNS 端口）是否能够与路由器完成 TCP 握手。

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_03_TCP_probe_example_winbox](img/netwatch_03_TCP_probe_example.webp)

## HTTP-GET 探测

`http-get` 探测向指定主机执行 HTTP-GET 请求，并验证返回的 HTTP 状态码和响应时间。与 ICMP 或 TCP 探测不同，它验证应用层可用性，确保 Web 服务实际响应。当响应代码在配置的 `http-codes` 范围内且响应时间在配置的阈值内时，探测被视为成功。常用于监控网站或 API 的可用性。

### 配置示例

在此示例中，探测尝试从位于 159.148.172.205 的 mikrotik.com 获取 HTTP 响应，并记录响应代码。

 ```ros
 /tool/netwatch/add host=159.148.172.205 type=http-get down-script=":log info \"Probe down, response code: \$\"http-status-code\"\"" up-script=":log info \"Probe up, response code: \$\"http-status-code\"\""
 ```

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_04_httpget_probe_example_winbox](img/netwatch_04_httpget_probe_example.webp)

在此日志示例中，您可以看到探测进入 down 状态，因为它未达到 100-299 的状态码阈值并收到了代码 302，因为 mikrotik.com 试图将探测重定向到 HTTPS。

```ros
 2026-06-19 14:09:26 netwatch,info event down [ type: http_get, host: 159.148.172.205 ]
 2026-06-19 14:09:26 script,info Probe down, response code: 302
```

## HTTPS-GET 探测

`https-get` 探测类型与 `http-get` 探测类型相同，唯一区别在于它使用 HTTPS 而非 HTTP。例如，这允许探测执行额外的 [TLS/SSL 证书](../authentication-authorization-accounting/certificates) 验证检查。

### 配置示例

在此示例中，探测监控路由器自身的 `www-ssl` 服务。`www-ssl` 服务用于通过 [WebFig](../management-tools/webfig) 提供对路由器的 HTTPS 访问。（[更多信息](../system-information-and-utilities/services)）

```ros
 /tool/netwatch/add host=127.0.0.1 type=https-get down-script=":log info \"HTTPS WebFig is disabled\"" up-script=":log info \"HTTPS WebFig is enabled\""
```

该探测尝试从路由器的本地地址 (`127.0.0.1`) 获取 HTTPS 响应。为使此探测正常工作，请确保 `www-ssl` 服务配置了有效的 [TLS/SSL 证书](../authentication-authorization-accounting/certificates)。

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_05_httpsget_probe_example_winbox](img/netwatch_05_httpsget_probe_example.webp)

## DNS 探测

`dns` 探测类型检查指定域名是否可以被 DNS 服务器解析。如果 DNS 服务器为请求的域名返回有效记录，则探测被视为 `Up`。

### 配置示例

在此配置示例中，探测使用 Google 的公共 DNS 服务器检查 mikrotik.com 的 A 记录。

```ros
 /tool/netwatch/add host=mikrotik.com type=dns dns-server=8.8.8.8 record-type=A down-script=":log info \"No A type record found\"" up-script=":log info \"A type record found: \$ip\""
```

如图所示，`host` 设置为 `mikrotik.com`，`dns-server` 配置为 `8.8.8.8` 以覆盖在 [`/ip/dns`](../network-management/dns) 中配置的 DNS 服务器，`record-type` 设置为 `A` 以查询 IPv4 地址记录。

下面，您可以在 [WinBox](../management-tools/winbox) 视图中看到相同的配置示例，而非 CLI。

![netwatch_06_dns_probe_example_winbox](img/netwatch_06_dns_probe_example.webp)

下面的示例显示了 up-script 的执行和 Netwatch 状态变化。

```ros
 2026-06-29 10:10:55 netwatch,info event up [ type: dns, host: mikrotik.com ]
 2026-06-29 10:10:55 script,info A type record found: 159.148.172.205
```