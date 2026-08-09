# 反向代理

> MikroTik RouterOS 上的反向代理服务允许通过简单的 URL（而非 NAT 规则）将 HTTPS 流量路由到服务器或应用，并支持可配置的 IP/端口和 SNI 设置，但需要禁用 443 端口上的默认 www-ssl 服务。

# 反向代理

反向代理是一项服务，允许路由器将 HTTPS 流量发送到服务器，或发送到 RouterOS 容器/应用（当应用设置中启用了“use-https”参数时），这些服务器或应用位于路由器后方，通过简单的 URL 而非 IP 地址进行访问，无需创建单独的目的 NAT 规则。

:::danger
请注意，默认情况下，反向代理服务使用 HTTPS 端口 443，与默认的 www-ssl 服务端口相同。为使反向代理正常运行，您需要确保 www-ssl 服务已禁用或使用不同的 TCP 端口。（参见 [/ip/service 文档](../../system-information-and-utilities/services.md)）
:::

### 属性说明

**子菜单：** `/ip/reverse-proxy`

| 属性 | 说明 |
| :-- | :-- |
| **disabled**（*yes* \| *no*；默认值：**yes**） | 反向代理记录是否处于活动状态。 |
| **ip-address**（IPv4/IPv6；默认值：**0.0.0.0**） | 需要被代理连接的服务器 IP 地址。 |
| **port**（整数：0..65535；默认值：**0**） | 服务器的监听端口。 |
| **sni**（字符串；默认值：） | 服务器的服务器名称指示（SNI）。 |
| **certificate**（证书；默认值：**none**） | 特定反向代理实例所使用的[证书](../../authentication-authorization-accounting/certificates.md)名称。当设置为 **none** 时，反向代理实例将使用在 `/ip/service` 菜单中设置的反向代理服务证书。 |
| **vrf**（名称；默认值：main） | 要使用的虚拟路由转发（VRF）实例。 |
| **comment**（字符串；默认值：） | 项目的描述性名称。 |