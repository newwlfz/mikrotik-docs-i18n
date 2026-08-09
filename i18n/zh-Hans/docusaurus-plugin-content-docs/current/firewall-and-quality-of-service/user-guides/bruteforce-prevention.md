# 暴力破解防护

> 本页说明如何通过防火墙过滤器在 MikroTik RouterOS 上配置暴力破解防护，在多次登录失败后阻止 SSH 登录尝试，每次尝试级别设置不同的超时时间，并为合法用户提供最终放行。

# 暴力破解防护

本示例演示如何防范针对 SSH 端口的暴力破解攻击。请注意，SSH 每个连接允许 3 次登录尝试，且地址列表在成功登录后不会清除。这意味着如果您触发了防护机制，可能会意外地将自己列入黑名单。

```
/ip/firewall/filter/add action=add-src-to-address-list address-list=bruteforce_blacklist address-list-timeout=1d chain=input comment="黑名单" connection-state=new dst-port=22 protocol=tcp src-address-list=connection3

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection3 address-list-timeout=1h chain=input comment="第三次尝试" connection-state=new dst-port=22 protocol=tcp src-address-list=connection2

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection2 address-list-timeout=15m chain=input comment="第二次尝试" connection-state=new dst-port=22 protocol=tcp src-address-list=connection1

/ip/firewall/filter/add action=add-src-to-address-list address-list=connection1 address-list-timeout=5m chain=input comment="第一次尝试" connection-state=new dst-port=22 protocol=tcp

/ip/firewall/filter/add action=accept chain=input dst-port=22 protocol=tcp src-address-list=!bruteforce_blacklist
```

如果三个连接列表均使用 1 分钟超时，攻击者每分钟可进行 9 次猜测。而采用上述结构后，每 5 分钟最多只能进行 3 次猜测。

:::warning
地址列表的命名遵循《端口敲门》文章中使用的约定。类似的命名方案中，受信任的地址列表被命名为“secured”。
:::