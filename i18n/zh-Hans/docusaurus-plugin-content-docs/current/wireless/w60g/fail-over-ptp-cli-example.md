# Fail-over PtP CLI 示例

> 本页提供逐步 CLI 示例，演示如何通过 bonding 在 60Ghz 和 5Ghz 无线链路之间配置自动故障切换，包括桥接设置以及 W60G 接口在桥接和站点模式下的配置。

# Fail-over PtP CLI 示例

### 概述

本示例展示如何在 CLI 中配置 60Ghz 设备与 5Ghz 链路相结合的自动故障切换（bonding）。
当 60Ghz 无线连接丢失时，将自动使用 bonded 接口。
本示例从空配置状态开始，使用 [[WinBox](https://mikrotik.com/download)] 工具进行操作。

### 逐步连接设备

- 配置重置后 - 仅支持 MAC-telnet 连接。
   通过设备的 MAC 地址连接设备，或使用 WinBox 新终端查找 W60G 设备的 MAC 地址，执行以下命令：

```ros
/ip/neighbor/print
```

- 要连接 W60G 设备，请执行以下命令：

```ros
/tool/mac-telnet <MAC-ADDRESS>
```

- 输入用户名和密码。默认用户名为 **admin**，密码为空或印在设备标签上：

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
[admin@MikroTik] > /interface/bridge/print
Flags: X - disabled, R - running
 0 R name="bridge" mtu=auto actual-mtu=1500 l2mtu=65535 arp=enabled arp-timeout=auto mac-address=1A:7F:BB:41:B0:94 protocol-mode=rstp  fast-forward=yes igmp-snooping=no auto-mac=yes ageing-time=5m priority=0x8000 max-message-age=20s forward-delay=15s transmit-hold-count=6  vlan-filtering=no dhcp-snooping=no
```

### 设置 60Ghz 无线连接

之前所有步骤对于桥接和站点设备均相同。配置无线接口时需要使用不同的模式。

#### 桥接设备

- 选择 SSID、密码、频率，并选择将作为**桥接**模式的选项。请参考示例。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=bridge frequency=auto ssid=MySSID password=choosepassword isolate-stations=yes
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=bridge ssid="MySSID"  frequency=auto default-scan-list=58320,60480,62640,64800 password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1
```

#### 站点设备

- 选择与桥接设备相同的 SSID、密码和频率，并选择将作为**站点**的 station-bridge 模式选项，请参考示例。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/w60g/set wlan60-1 mode=station-bridge frequency=auto ssid=MySSID password=choosepassword
[admin@MikroTik] > /interface/w60g/print
Flags: X - disabled, R - running
0 X name="wlan60-1" mtu=1500 l2mtu=1600 mac-address=C4:AD:34:84:EE:5E arp=enabled arp-timeout=auto region=no-region-set mode=station-bridge ssid="MySSID" frequency=auto default-scan-list=58320,60480,62640,64800password="choosepassword" tx-sector=auto put-stations-in-bridge=bridge isolate-stations=yes
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```

### 设置 5Ghz 无线连接

#### 桥接设备

- 选择 SSID、密码、频率，并选择将作为**桥接**模式的选项，请参考示例。
- 设置所需参数后启用 5GHz 接口。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

#### 站点设备

- 选择与桥接设备相同的 SSID、密码和频率，并选择将作为**站点**的 station-bridge 模式选项。请参考示例。
- 设置所需参数后启用 W60G 接口。

```ros
[admin@MikroTik] > /interface/wireless/security-profiles/set [ find default=yes ] supplicant-identity=MikroTik authentication-types=wpa2-psk mode=dynamic-keys wpa2-pre-shared-key=choosepassword
[admin@MikroTik] > /interface/wireless/set wlan1 frequency=auto scan-list=default installation=outdoor mode=station-bridge ssid=MikroTik1 channel-width=20/40/80mhz-Ceee wireless-protocol=any security-profile=default band=5ghz-a/n/ac
[admin@MikroTik] > /interface/wireless/enable wlan1 
```

### 配置桥接和 bonding

- 配置 bonding 并分配从属接口。在此设置中，选择内置的 wlan1 接口，但在其他类型的设置中也可以是以太网接口。

   对于 *bridge* 设备，请将 **bonding** 设置为：

```ros
[admin@MikroTik] > /interface/bonding/add comment=bondingbackup mode=active-backup name=bond1 primary=wlan60-station-1 slaves=wlan60-station-1,wlan1
```

&emsp;&emsp; 对于 *station-bridge* 设备，请将 **bonding** 设置为：

```ros
[admin@MikroTik] > /interface/bonding/add comment=defconf mode=active-backup name=bond1 primary=wlan60-1 slaves=wlan60-1,wlan1
```

- 将接口成员（ether1 和 bond1）添加到新创建的桥接中。

```ros
[admin@MikroTik] > /interface/bridge/port/add interface=ether1 bridge=bridge
[admin@MikroTik] > /interface/bridge/port/add interface=bond1  bridge=bridge
[admin@MikroTik] > /interface/bridge/port/print
Flags: X - disabled, I - inactive, D - dynamic, H - hw-offload
#     INTERFACE                              BRIDGE                              HW   PVID PRIORITY  PATH-COST INTERNAL-PATH-COST    HORIZON
0     ether1                                 bridge                             yes     1     0x80         10                 10       none
1     bond1                                  bridge                             yes     1     0x80         10                 10       none |
```

### 附加配置

完成上述所有步骤后，链路应已建立。建议在两台设备上设置管理员密码。

### 故障排除

通过执行以下命令检查设备设置（如序列号和型号名称），确保连接到正确的设备：

```ros
[admin@MikroTik] > /system/routerboard/print
```

如果桥接设置中的 wlan60-1 接口处于非活动状态，且配置正确，请在设备上启用该接口，执行以下命令：

```ros
[admin@MikroTik] > /interface/w60g/enable wlan60-1 
```