# 包含敏感参数菜单列表

> 本页面列出了 MikroTik RouterOS 中配置敏感参数（如密码、密钥和机密）的菜单，并附有每个菜单的详细文档链接。

# 包含敏感参数菜单列表

以下菜单中可以配置敏感参数（仅在使用了 [show-sensitive 参数](./index.md#configuration-export) 时显示，或者在 WinBox 设置中启用了“隐藏密码”时被隐藏）。如需更详细信息，请参阅相应的菜单文档页面。

| 菜单 | 参数名称 | 页面链接 |
| :-- | :-- | :-- |
| `/container` | password | [Container#Containerconfiguration](../../containers/index.md) |
| `/ip/hotspot` | mac-auth-password, password, otp-secret | [HotSpot - Captive portal#HotSpotUsers](../../authentication-authorization-accounting/hotspot-captive-portal/index.md) |
| `/iot` | password, key | password - [MQTT#Brokers](../../internet-of-things/mqtt/index.md)  key - [Lora#Servers](../../internet-of-things/lora/general-properties.md#servers)|
| `/interface/gre`  `/interface/gre6` | ipsec-secret | [GRE#Properties](../../virtual-private-networks/gre.md) |
| `/interface/ipip`  `/interface/ipipv6` | ipsec-secret | [IPIP#Properties](../../virtual-private-networks/ipip.md) |
| `/interface/eoip`  `/interface/eoipv6` | ipsec-secret | [EoIP#PropertyDescription](../../virtual-private-networks/eoip.md) |
| `/interface/6to4` | ipsec-secret | [6to4#6to4-PropertyDescription](../../virtual-private-networks/6to4.md) |
| `/interface/ppp-client` | password, pin | 待完善 [PPP](../../mobile-networking/ppp.md) |
| `/interface/sstp-client` | password | [SSTP#Properties](../../virtual-private-networks/sstp.md) |
| `/interface/l2tp-server`  `/interface/l2tp-client`  `/interface/l2tp-ether` | ipsec-secret, password | ipsec-secret, password - [L2TP#L2TPClient](../../virtual-private-networks/l2tp/index.md#l2tp-client)  ipsec-secret - [L2TP#L2TPServer](../../virtual-private-networks/l2tp/index.md#l2tp-server)  ipsec-secret - [L2TP#L2TPEther](../../virtual-private-networks/l2tp/index.md#l2tp-ether)|
| `/interface/ovpn-client` | password | [OpenVPN#OVPNClient](../../virtual-private-networks/openvpn.md) |
| `/interface/pptp-client` | password | [PPTP#PPTPClient](../../virtual-private-networks/pptp.md) |
| `/interface/pppoe-client` | password | [PPPoE#PPPoEClient](../../virtual-private-networks/pppoe/index.md) |
| `/ppp/secret` | password | [PPP AAA#UserDatabase](../../authentication-authorization-accounting/ppp-aaa.md) |
| `/ppp/l2tp-secret` | secret | 待完善 |
| `/ip/ssh/export-host-key`  `/ip/ssh/import-host-key` | passphrase | [SSH#SSHServer](../../management-tools/ssh.md) |
| `/ip/ipsec` | auth-key, enc-key, ppk-secret, secret, password, passphrase, key | auth-key, enc-key - [IPsec#InstalledSAs](../../virtual-private-networks/ipsec/index.mdx#installed-sas)  secret, password - [IPsec#Identities](../../virtual-private-networks/ipsec/index.mdx#identities)  ppk-secret - 待完善 [IPsec#Peers](../../virtual-private-networks/ipsec/index.mdx#peers)  key, passphrase - 待完善 [IPsec#Keys](../../virtual-private-networks/ipsec/index.mdx#keys)|
| `/system/ssh-exec` | password | [SSH#SSHexec](../../management-tools/ssh.md) |
| `/user` | password, passphrase | [User](../../authentication-authorization-accounting/user.md) |
| `/disk` | nvme-tcp-server-password, nvme-tcp-password, smb-server-password, smb-password, self-encryption-password, encryption-key, sshfs-password | nvme-tcp-server-password, nvme-tcp-password - [NVMe over TCP](../../storage/nvme-over-tcp.md)  sshfs-password - 待完善  smb-server-password, smb-password - [SMB](../../storage/smb.md)  self-encryption-password, encryption-key - [Self-Encrypting Drives](../../storage/self-encrypting-drives.md)|
| `/interface/vrrp` | password | [VRRP#Parameters](../../high-availability-solutions/vrrp.md) |
| `/interface/dot1x` | password | [Dot1X#Client](../../authentication-authorization-accounting/dot1x.md) |
| `/interface/macsec` | cak | [MACsec#PropertyReference](../../bridging-and-switching/macsec.md) |
| `/interface/wireguard` | private-key, preshared-key, \**show-client-config* | [WireGuard](../../virtual-private-networks/wireguard.md) |
| `/interface/lte` | pin, password | [LTE/5G#LTEClient](../../mobile-networking/lte-5g.md#lte-client) |
| `/socks/users` | password | [SOCKS](../../network-management/socks/index.md) |
| `/ip/cloud` | vpn-private-key, vpn-peer-private-key, private-key | [Back To Home#Propertyreference](../../network-management/cloud/back-to-home.md) |
| `/ip/smb` | password | [SMB#Usersetup](../../storage/smb.md) |
| `/password` | old-password, new-password, confirm-new-password | 密码修改命令；无专门文档页面。 |
| `/radius` | secret | [RADIUS#RADIUSClient](../../authentication-authorization-accounting/radius.md) |
| `/routing` | password, tcp-md5-key, auth-key, key | password,key - [/routing/rip](../../cli-reference/routing/rip.md)  tcp-md5-key - [/routing/bgp/connection](../../cli-reference/routing/bgp.md#routingbgpconnection)  auth-key - [/routing/ospf](../../cli-reference/routing/ospf.md#routingospfinterface-template)|
| `/snmp/community` | authentication-password, encryption-password | [SNMP#CommunityProperties](../../diagnostics-monitoring-and-troubleshooting/snmp.md) |
| `/system/backup` | password | [Backup](./backup.md) |
| `/system/ntp/key` | key-val | 待完善 [NTP](../../system-information-and-utilities/ntp.md) |
| `/system/swos/password` | new-password, confirm-new-password | SwOS 密码修改命令；无专门文档页面。 |
| `/system/package/local-update` | password | [Packages#LocalUpdate](../installation-and-upgrade/packages.md) |
| `/system/license` | password | [RouterOS license keys#CHRLicenseLevels](../routeros-licensing/chr/chr-licensing.md#chr-license-levels) |
| `/tool/romon` | secrets | [RoMON#Configuration](../../management-tools/romon.md) |
| `/tool/sms` | sim-pin, secret | [SMS#Receiving](../../mobile-networking/sms.md) |
| `/tool/email` | password | [E-mail](../../system-information-and-utilities/e-mail.md) |
| `/tr069-client` | connection-request-password, password | [TR-069#ConfigurationSettings](../../management-tools/tr-069.md) |
| `/user-manager` | web-private-password, paypal-password, shared-secret, password, otp-secret | shared-secret - [User Manager#Routers](../../authentication-authorization-accounting/user-manager.md#routers)  paypal-password, web-private-password - [User Manager#Advanced](../../authentication-authorization-accounting/user-manager.md#advanced)  password, otp-secret - [User Manager#Users](../../authentication-authorization-accounting/user-manager.md#users)|
| `/interface/wifi` | passphrase, eap-password | [WiFi#SecurityProperties](../../wireless/wifi/index.md) |
| `/caps-man` | private-passphrase, passphrase | private-passphrase - [CAPsMAN#CAPsMANAccess-list](../../wireless/abgn/capsman/index.md#capsman-access-list)  passphrase - [CAPsMAN#CAPsMANconfiguration](../../wireless/abgn/capsman/index.md#capsman-configuration)|
| `/interface/wireless` | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key, management-protection-key, nv2-preshared-key, private-key, private-pre-shared-key, wpa-pre-shared-key, wpa2-pre-shared-key, mschapv2-password | static-key-0, static-key-1, static-key-2, static-key-3, static-sta-private-key - [Wireless Interface#WEPproperties](../../wireless/index.md)  management-protection-key, private-key, private-pre-shared-key - [Wireless Interface#Properties](../../wireless/index.md)  wpa-pre-shared-key, wpa2-pre-shared-key - [Wireless Interface#WPAproperties](../../wireless/index.md)  mschapv2-password - [Wireless Interface#WPAEAPproperties](../../wireless/index.md)  nv2-preshared-key - [Wireless Interface#Generalinterfaceproperties](../../wireless/index.md) |
| `/interface/w60g` | password | [W60G#Generalinterfaceproperties](../../wireless/w60g/index.md) |
| `/zerotier` | identity | [ZeroTier#Parameters](../../virtual-private-networks/zerotier.md) |
| `/certificate` | export-passphrase, passphrase, challenge-password, pin, key-passphrase, challenge-passphrase | pin - 用于 card-reinstall 和 card-verify 命令，无专门文档页面。  export-passphrase - [Certificates#ExportCertificate](../../authentication-authorization-accounting/certificates.md#export-certificate)  passphrase - [Certificates#ImportCertificate](../../authentication-authorization-accounting/certificates.md#import-certificate)  challenge-password, key-passphrase, challenge-passphrase - 待完善 |