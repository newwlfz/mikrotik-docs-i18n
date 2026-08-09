# 动态DNS

> 动态DNS更新工具能够使用符合RFC标准的算法，对动态IP地址的域名记录进行安全更新，仅支持hmac-md5算法。它需要BIND DNS服务器，并支持IP、DNS服务器、密钥和TTL等指定属性。

# 动态DNS

**子菜单：** `/tool/dns-update`

**标准：** `RFC 2136, RFC 3007`

动态DNS更新工具提供了一种保持域名指向动态IP地址的方法。它通过向名称服务器发送域名系统更新请求来实现，该服务器具有需要更新的区域。同时支持安全DNS更新。

DNS更新工具仅支持一种算法 - **hmac-md5**。这是唯一用于签署DNS消息的提议算法。

:::warning
DNS更新工具仅适用于BIND服务器；它不适用于DynDNS、EveryDNS或任何其他类似服务。
:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **address** (*IP*; 默认值：) | 定义与域名关联的IP地址。 |
| **dns-server** (*IP*; 默认值：) | 接收更新的DNS服务器。 |
| **key** (*字符串*; 默认值：) | 访问服务器的授权密钥。 |
| **key-name** (*字符串*; 默认值：) | 访问服务器的授权密钥名称（类似于用户名）。 |
| **name** (*字符串*; 默认值：) | 附加到IP地址的名称。 |
| **ttl** (*整数*; 默认值：) | 项目的生存时间（以秒为单位）。 |
| **zone** (*字符串*; 默认值：) | 要更新域名的DNS区域。 |

:::warning
路由器上的系统时钟时间与DNS服务器的时间相差不能超过5分钟。否则，DNS服务器将忽略此请求。
:::

## 示例

要告知23.34.45.56 DNS服务器将myzone.com区域中的mydomain名称（重新）关联到68.42.14.4 IP地址，并指定密钥名称为dns-update-key且实际密钥为update：

```ros
[admin@MikroTik] tool> dns-update dns-server=23.34.45.56 name=mydomain \
\... zone=myzone.com address=68.42.14.4 key-name=dns-update-key key=update
```