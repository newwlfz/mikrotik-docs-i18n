# Wake on LAN

> Wake on LAN（WoL）是一种通过网络功能，通过向目标设备的MAC地址发送UDP魔术包来实现远程开机，这要求接口和硬件配置正确。

# Wake on LAN

[*Wake on LAN CLI参考*](../cli-reference/tool/wol)

**子菜单：** `/tool/wol`

Wake on LAN（WoL）是一种网络功能，通过向广播地址发送UDP魔术包来实现远程开机。该数据包包含目标设备的MAC地址。如果目标设备支持Wake on LAN（即具备所需的硬件和软件配置），它将从休眠或关机状态被唤醒。不支持安全WoL。

## Wake-on-LAN命令

`/tool/wol` 命令需要MAC地址参数和接口才能正常工作。

:::warning
如果未指定接口，魔术包将从默认网关接口以IP广播形式发送。
:::

```ros
/tool/wol mac=FE:4B:71:05:EA:8B interface=ether1
```

以下示例展示了 [WinBox](../management-tools/winbox) 中的Wake on LAN工具。

![WinBox中的Wake on LAN工具](img/wake_on_lan_01.webp)