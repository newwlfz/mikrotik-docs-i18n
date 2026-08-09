# Fail-over PtMP CLI 示例

> 本页提供了一份逐步 CLI 指南，用于配置 60Ghz 与 5Ghz 无线链路之间的自动故障切换，涵盖桥接设置、接口绑定及 W60G 设备连接说明，基于 MikroTik RouterOS。

# Fail-over PtMP CLI 示例

### 概述

本示例演示如何在 CLI 中配置 60Ghz 设备与 5Ghz 链路的自动故障切换（绑定）。  
当 60Ghz 无线连接中断时，系统将自动使用绑定接口。  
本示例从空配置状态开始，并使用 [[WinBox](https://mikrotik.com/download)] 工具进行操作。

### 逐步连接设备

- 配置重置后，仅支持 MAC 远程登录（mac-telnet）。
   通过设备的 MAC 地址进行连接，或使用 WinBox 新终端查找 W60G 设备的 MAC 地址，执行以下命令：

```ros
/ip/neighbor/print
```

- 要连接 W60G 设备，请执行以下命令：

```ros
/tool/mac-telnet/mac-address
```

- 输入用户名和密码。默认用户名为 **admin**，密码为空或印在设备标签上。

```ros
[admin@KD_GW] > /tool/mac-telnet C4:AD:34:84:EE:5D
 Login: admin
 Password:  
 Trying C4:AD:34:84:EE:5D...
 Connected to C4:AD:34:84:EE:5D 
```

### 配置桥接

- 添加新桥接并分配桥接成员，执行以下命令：

```ros
/interface/bridge/add name=bridge 
```

检查桥接是否已创建，执行以下命令：

```ros
admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
 0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

### 设置 60Ghz 无线连接

此前所有步骤对于桥接设备和站点设备均相同。配置无线接口时需使用不同的模式。  
  
#### 对于 ap-bridge 设备

- 选择 SSID、密码、频率，并选择将作为 **ap-bridge** 的桥接模式选项，请参见示例。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=ap-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=ap-bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=none isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```

#### 对于站点设备

- 选择与桥接设备相同的 SSID、密码和频率，并选择将作为 **station** 的 station-bridge 模式选项，请参见示例。
- 单个 AP 最多可连接 8 个站点设备以作为故障切换。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=no
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=no
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

### 设置 5Ghz 无线连接

#### 对于 ap-bridge 设备

- 选择 SSID、密码、频率，并选择将作为 **bridge** 的桥接模式选项，请参见示例。
- 设置所需参数后启用 5GHz 接口。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=ap-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

#### 对于站点设备

- 选择与桥接设备相同的 SSID、密码和频率，并选择将作为 **station** 的 station-bridge 模式选项。请参见示例。
- 单个 AP 最多可连接 8 个站点设备以作为故障切换。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1
```

### 为接入点配置桥接

- 为 AP 配置桥接，确保 5ghz 作为故障切换链路正常工作。需要将 **wlan1**、**ether1** 以及所有 60ghz **站点接口** 桥接起来。
   *示例中仅显示 2 个站点设备，但最多可添加 8 个设备。*  

   对于 ap-bridge 设备，请按如下方式设置 **configuration**：

```ros
[admin@MikroTik] > /interface/bridge/port/
add bridge=bridge hw=no interface=ether1
add bridge=bridge interface=wlan1
add bridge=bridge interface=wlan60-station-1
add bridge=bridge interface=wlan60-station-2
[admin@MikroTik] > interface/bridge/port/pr
# INTERFACE         BRIDGE  HW  PVID  PRIORITY  PATH-COST  INTERNAL-PATH-COST  HORIZON
0 ether1            bridge      no     1  0x80             10                  10  none
1 wlan1             bridge             1  0x80             10                  10  none
2 wlan60-station-1  bridge             1  0x80             10                  10  none
3 wlan60-station-2  bridge             1  0x80             10                  10  none 
```

### 为站点设备配置桥接和绑定

- 配置绑定并分配从属接口。在此设置中，选择内置的 wlan1 接口，但在其他类型的设置中也可以是以太网接口。

   对于 station-bridge 设备，请按如下方式设置 **bonding**：

```ros
[admin@MikroTik] > /interface/bonding/add mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```

- 将接口成员（ether1 和 bond1）添加到新创建的桥接中。

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=bond1  bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1     bond1                                  bridge                             yes     1     0x80         10                 10       none
```

### 附加配置

完成上述所有步骤后，链路应已建立。建议在两台设备上设置管理员密码。

### 故障排查

通过执行以下命令检查设备设置（如序列号和型号名称），确保连接到正确的设备：

```ros
[admin@MikroTik] > /system/routerboard/print
```

如果桥接设置中的 wlan60-1 接口处于非活动状态，且配置正确，请在设备上启用该接口，执行以下命令：

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```