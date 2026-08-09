# 身份标识

> 本文档介绍了如何在 MikroTik RouterOS 中配置系统身份标识，该标识为网络通信及 DHCP 等服务提供唯一识别名称。文中说明了如何通过 CLI 或 SNMP 设置身份标识，并提醒注意 64 字符的长度限制。

# 身份标识

设置系统身份标识可为系统在网络中向其他路由器自我识别，以及访问 DHCP、邻居发现和默认无线 SSID 等服务时提供唯一识别名称。默认系统身份标识设置为“MikroTik”。

:::warning
系统身份标识的最大字符长度为 64
:::

## 配置

在 RouterOS 中设置系统身份标识：

```ros
[admin@MikroTik] > /system/identity/set name=New_Identity 
[admin@New_Identity] >
```

当前系统身份标识始终显示在登录账户名之后，并可通过 print 命令查看：

```ros
[admin@New_Identity] /system/identity>print
name: New_Identity
[admin@New_Identity] /system/identity>

```

### SNMP

也可以通过 SNMP 设置命令更改路由器系统身份标识：

```ros
snmpset -c public -v 1 192.168.0.0 1.3.6.1.2.1.1.5.0 s New_Identity
```

*snmpset* - 基于 Linux 的 SNMP 应用程序，用于发送 SNMP SET 请求以设置网络实体上的信息；

- *public* - 路由器的共同体名称；
- *192.168.0.0* - 路由器的 IP 地址；
- *1.3.6.1.2.1.1.5.0* - 路由器身份标识的 SNMP 值；