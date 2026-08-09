# 端口敲门

> 端口敲门是一种保护公共IP地址的安全方法，要求在进行特定顺序的端口连接后才授予访问权限。本文档提供了设置示例，包括用于将IP添加到可信列表和阻止可疑端口的防火墙规则配置，并附有关于资源使用的警告。

# 端口敲门

所有可用的公共IP地址都不断受到机器人和诸如shodan.io等服务的端口扫描，任何人都可以利用这些信息进行暴力破解攻击或执行已知漏洞利用。端口敲门是一种经济有效的防御方式，它不暴露任何端口，仅监听连接尝试——如果客户端按正确顺序进行了端口连接尝试，则被视为安全，并被添加到绕过WAN防火墙规则的安全地址列表中。

### 设置示例

我们假设您已经设置了一个防火墙，用于丢弃来自WAN端口的所有连接尝试，因此您需要在此之前添加额外的规则。
首先，创建一个防火墙规则，监听指定端口并将连接的源IP添加到地址列表中——这是第一次敲门。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=888 address-list-timeout=30s chain=input dst-port=888 in-interface-list=WAN protocol=tcp
```

然后添加一条规则，在另一个端口上执行相同操作，但仅批准已在第一个列表中的IP。您可以根据需要重复此步骤多次。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=555 address-list-timeout=30s chain=input dst-port=555 in-interface-list=WAN protocol=tcp src-address-list=888
```

最后，最后一次敲门将添加到一个受信任的IP列表中，并接受任何输入。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=secured address-list-timeout=30m chain=input dst-port=222 in-interface-list=WAN protocol=tcp src-address-list=555
/ip/firewall/filter/add action=accept chain=input in-interface-list=WAN src-address-list=secured
```

### 敲门以获取访问权限

要从WAN访问设备，可以使用端口敲门客户端，但一个简单的bash单行命令配合nmap即可完成此任务。

```bash
for x in 888 555 222; do nmap -p $x -Pn xx.xx.xx.xx; done
```

### 黑名单

除非您使用大量敲门，否则简单的端口扫描可能会意外触发正确顺序的正确端口，因此建议同时添加黑名单。

在防火墙堆栈的最顶部，为黑名单添加一条丢弃规则。

```ros
/ip/firewall/filter/add action=drop chain=input disabled=yes in-interface-list=WAN src-address-list=blacklist
```

然后将可疑IP添加到黑名单中。

不良端口——这些端口永远不会被可信用户使用，因此具有较高的超时惩罚。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=blacklist address-list-timeout=1000m chain=input disabled=yes dst-port=666 in-interface-list=WAN protocol=tcp
```

这些端口会显著减慢端口扫描过程，使其变得毫无意义，但不会将真实用户锁定过长时间。这可以包括除“敲门”端口之外的每一个端口。关键在于源IP尚未在安全列表中，因此在成功敲门后可以使用这些端口。

```ros
/ip/firewall/filter/add action=add-src-to-address-list address-list=blacklist address-list-timeout=1m chain=input disabled=yes dst-port=21,22,23,8291,10000-60000 in-interface-list=WAN protocol=tcp src-address-list=!secured
```

:::warning
本节中的黑名单规则以 **disabled=yes** 添加，以避免锁定用户。在备用访问可用后启用过滤规则，或使用 `<安全模式>`
:::

### 为每次敲门使用口令

您还可以更进一步，为每次敲门发送一个口令。

:::info
警告

Layer7规则非常消耗资源。除非您了解自己在做什么，否则不要使用它们。
:::

<details>
<summary>点击打开代码块</summary>

然后创建一个layer7正则表达式检查，可以在敲门规则上请求。

`/ip/firewall/layer7-protocol/add` name=pass regexp="^passphrase/$"
`/ip/firewall/filter`
add action=add-src-to-address-list address-list=888 address-list-timeout=30s chain=input dst-port=888 in-interface-list=WAN protocol=udp layer7-protocol=pass

</details>

:::warning
如需额外的安全层，请参阅暴力破解防护文章：[暴力破解防护](./bruteforce-prevention.md)
:::