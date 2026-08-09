# NordVPN 与 RouterOS 之间的 IKEv2 EAP 配置

> 本页面指导用户在 RouterOS v6.45+ 中，使用 EAP 认证配置到 NordVPN 服务器的 IKEv2 安全隧道，涵盖根 CA 安装、服务器主机名查询、带 Phase 1/2 配置文件和策略的 IPsec 隧道设置、EAP 认证的模式配置，以及对端/身份凭据设置。

# NordVPN 与 RouterOS 之间的 IKEv2 EAP 配置

从 RouterOS v6.45 开始，可以使用 EAP 认证建立到 NordVPN 服务器的 IKEv2 安全隧道。本手册页面将说明如何进行配置。

![](https://manual.mikrotik.com/docs/virtual-private-networks/ipsec/img/ikev2-eap-between-nordvpn-and-routeros-01.webp)

### 安装根 CA

首先，下载并导入 NordVPN 根 CA 证书。

```
/tool/fetch url="https://downloads.nordvpn.com/certificates/root.der"
/certificate/import file-name=root.der

```

现在，在 System/Certificates 菜单中应该可以看到受信任的 NordVPN Root CA 证书。

```
[admin@MikroTik] > /certificate/print where name~"root.der"
Flags: K - private-key, L - crl, C - smart-card-key, A - authority, I - issued, R - revoked, E - expired, T - trusted 
 #         NAME            COMMON-NAME            SUBJECT-ALT-NAME                                         FINGERPRINT           
 0       T root.der_0      NordVPN Root CA                                                                 8b5a495db498a6c2c8c...

```

### 查询服务器主机名

访问 [https://nordvpn.com/servers/tools/](https://nordvpn.com/servers/tools/) 并查询推荐服务器的主机名。在本例中，主机名为 lv20.nordvpn.com。

![](https://manual.mikrotik.com/docs/virtual-private-networks/ipsec/img/ikev2-eap-between-nordvpn-and-routeros-02.webp)

### 设置 IPsec 隧道

建议创建独立的 Phase 1 配置文件和 Phase 2 提案配置，以避免与任何现有或未来的 IPsec 配置冲突。

```
/ip/ipsec/profile
add name=NordVPN
/ip/ipsec/proposal
add name=NordVPN pfs-group=none

```

虽然可以使用默认的策略模板来生成策略，但最好创建一个新的策略组和模板，以将此配置与其他 IPsec 配置分离。

```
/ip/ipsec/policy/group
add name=NordVPN
/ip/ipsec/policy
add dst-address=0.0.0.0/0 group=NordVPN proposal=NordVPN src-address=0.0.0.0/0 template=yes

```

创建一个新的 mode config 条目，设置 responder=no，以向服务器请求配置参数。

```
/ip/ipsec/mode-config
add name=NordVPN responder=no

```

最后，创建对端和身份配置。在 username 和 password 参数中指定您的 NordVPN 凭据。

```
/ip/ipsec/peer
add address=lv20.nordvpn.com exchange-mode=ike2 name=NordVPN profile=NordVPN
/ip/ipsec/identity
add auth-method=eap certificate="" eap-methods=eap-mschapv2 generate-policy=port-strict mode-config=NordVPN peer=NordVPN policy-template-group=NordVPN username=support@mikrotik.com password=secret

```

验证连接是否成功建立。

```
/ip/ipsec
active-peers print
installed-sa print

```

### 选择通过隧道发送的内容

如果查看生成的动态策略，我们会发现只有具有特定（通过 mode config 接收的）源地址的流量才会通过隧道发送。但在大多数情况下，路由器需要将特定设备或网络通过隧道路由。在这种情况下，我们可以使用源 NAT 将数据包的源地址更改为与 mode config 地址匹配。由于 mode config 地址是动态的，因此无法创建静态的源 NAT 规则。在 RouterOS 中，可以为 mode config 客户端生成动态的源 NAT 规则。

#### 选项 1：通过隧道发送所有流量

在此示例中，路由器后面有一个本地网络 10.5.8.0/24，我们希望该网络的所有流量都通过隧道发送。首先，我们必须创建一个新的 IP/Firewall/Address list，其中包含我们的本地网络。

```
/ip/firewall/address-list
add address=10.5.8.0/24 list=local
```

也可以只指定单个主机，其所有流量将通过隧道发送。示例：

```
/ip/firewall/address-list
add address=10.5.8.120 list=local
add address=10.5.8.23 list=local

```

完成后，我们可以将新创建的 IP/Firewall/Address list 分配给 mode config 配置。

```
/ip/ipsec/mode-config
set [ find name=NordVPN ] src-address-list=local
```

验证隧道建立时是否正确生成了动态源 NAT 规则。

```
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; ipsec mode-config
      chain=srcnat action=src-nat to-addresses=192.168.77.254 src-address-list=local dst-address-list=!local

```

:::info
警告

确保动态 mode config 地址不属于本地网络的一部分。

**重要提示：** 也可以组合使用选项 1 和选项 2，以仅允许特定本地地址/网络访问特定地址。
:::

#### 选项 2：通过隧道访问特定地址

也可以使用 Mangle 防火墙中的 connection-mark 参数，仅通过隧道发送特定流量。其工作原理与选项 1 类似——根据 mode config 下配置的 connection-mark 参数生成动态 NAT 规则。

首先，在 mode config 配置下设置 connection-mark。

```
/ip/ipsec/mode-config
set [ find name=NordVPN ] connection-mark=NordVPN

```

完成后，将使用服务器提供的动态地址生成 NAT 规则：

```
[admin@MikroTik] > /ip/firewall/nat/print 
Flags: X - disabled, I - invalid, D - dynamic 
 0  D ;;; ipsec mode-config
      chain=srcnat action=src-nat to-addresses=192.168.77.254 connection-mark=NordVPN 

```

之后，可以使用 Mangle 防火墙将此 connection-mark 应用于任何流量。在此示例中，通过隧道授予了对 [mikrotik.com](http://mikrotik.com) 和 8.8.8.8 的访问权限。

创建新的地址列表：

```
/ip/firewall/address-list
add address=mikrotik.com list=VPN
add address=8.8.8.8 list=VPN

```

将 connection-mark 应用于匹配所创建地址列表的流量：

```
/ip/firewall/mangle
add action=mark-connection chain=prerouting dst-address-list=VPN new-connection-mark=NordVPN passthrough=yes

```

:::info
也可以组合使用选项 1 和选项 2，以仅允许特定本地地址/网络访问特定地址。
:::