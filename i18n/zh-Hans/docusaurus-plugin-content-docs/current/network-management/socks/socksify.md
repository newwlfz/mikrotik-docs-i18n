# Socksify

> Socksify 允许将特定流量通过 SOCKS 代理服务器进行路由，使不支持原生代理的应用程序也能使用代理。它支持多个服务，并可配置防火墙过滤器以实现精确的流量管理，包括使用 TOR 的示例。

# Socksify

[*Socksify CLI 参考*](../../cli-reference/ip/socksify)

Socksify 是一项服务，允许路由器将特定流量通过 SOCKS 代理服务器发送，即使应用程序本身不支持代理连接。  
它会拦截网络调用，并将其重定向到配置的 SOCKS 代理。

Socksify 服务与 [NAT](../../firewall-and-quality-of-service/firewall/nat.md) 中的 `socksify` 动作结合使用。所有可用的防火墙过滤器均可用于精确选择仅需通过 SOCKS 代理重定向的按应用程序/源流量。

可以同时配置多个 Socksify 服务，从而允许连接到多个 SOCKS 服务器，以实现更好的流量管理。

### 属性说明

**子菜单：** `/ip/socksify`

| 属性 | 说明 |
| :-- | :-- |
| **disabled** (*yes* \| *no*；默认值：yes) | Socksify 记录是否处于活动状态。 |
| **socks5-password** (*string*；默认值：) | 用于访问 SOCKS5 代理服务器的密码。 |
| **socks5-user** (*string*；默认值：) | 用于访问 SOCKS5 代理服务器的用户名。 |
| **connection-timeout** (*integer:* 0..3000；默认值：60) | 以秒为单位的时间，指定在连接建立期间等待 SOCKS 代理或目标响应的时间，超时后将以错误中止。将此值设置为 0 可禁用连接超时。 |
| **name** (*string*；默认值：) | Socksify 服务的名称。 |
| **socks5-port** (*integer*: 1..65535；默认值：1080) | SOCKS5 代理服务器的监听端口。 |
| **socks5-server** (*IPv4;* 默认值：0.0.0.0) | SOCKS5 代理服务器的 IP 地址。（仅支持 IPv4 地址） |
| **port** (*integer*: 1..65535；默认值：952) | Socksify 服务将使用的 TCP 端口。 |

## 配置示例

### 与 TOR SOCKS5 代理服务器结合使用

Socksify 可以与 TOR 结合使用，为没有集成 SOCKS 支持的应用程序提供更好的隐私和匿名性。  
以下配置将允许您通过 TOR SOCKS5 代理服务器转发 HTTP/s 流量。  
首先，您需要配置 socksify 服务。

```ros
/ip/socksify 
add connection-timeout=10 disabled=no name=TOR_socksify socks5-port=9050 socks5-server=<TOR_SOCKS_proxy_IP>
```

之后，您需要配置防火墙，以确保正确的流量被 socksify 处理，并允许 SOCKS 流量通过。

```ros
/ip/firewall/filter
add action=accept chain=input dst-port=952 protocol=tcp src-address=<SOCKS_client_IP> 
/ip/firewall/nat
add action=socksify chain=dstnat dst-port=80,443 protocol=tcp socksify-service=TOR_socksify src-address=<SOCKS_client_IP> 
```

### TOR 容器和安全 DNS 教程

由于 RouterOS 支持运行容器，您也可以在容器中设置 Tor 代理。此外，如果您打算使用 Tor 进行网页浏览，应考虑保护您的 DNS 请求。

有关详细的分步说明，请观看 [此处](https://www.youtube.com/watch?v=ECRjxpb5IgE&lc=Ugy6V6EEAwyu2UC8ZJB4AaABAg) 的视频。