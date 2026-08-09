# 返回首页

> 返回首页功能使您能够从任何地方安全地VPN访问您的路由器，即使路由器没有公网IP或位于NAT之后。它利用MikroTik中继服务器进行间接连接，确保端到端加密且不暴露密钥。该功能支持智能手机应用和手动RouterOS配置，包括与访客共享隧道或通过WireGuard供计算机使用。

# 返回首页

**子菜单：** `/ip/cloud` **所需软件包：** `routeros`  
**所需RouterOS版本：** v7.12及更新版本  
**硬件要求：** ARM/ARM64/TILE架构设备

返回首页是一项便捷功能，可配置您的设备，使您能够从世界任何地方安全地VPN访问您的路由器和网络，即使您的路由器没有公网IP地址、位于NAT或防火墙之后。

配置通过MikroTik返回首页应用完成（[Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn)，[iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)）。

如果VPN服务器（您的家庭路由器）具有公网IP地址，VPN应用将在手机和路由器之间创建直接VPN连接。但是，如果路由器无法从互联网直接访问，连接将通过MikroTik中继服务器建立。连接始终是端到端加密的。中继服务器或任何其他设备无法访问加密密钥。实质上，中继仅帮助您的设备到达路由器。连接将显示为从您的路由器发出，而非从中继发出。*如果通过中继传输，速度可能会受到限制。*

此功能是访问家庭网络或查看您所在国家/地区内容的便捷选项，适用于某些内容在特定位置不可用的情况。它并非用于匿名；而是用于一键简单访问您的家庭网络。如需更细粒度的安全控制，我们建议您使用高级RouterOS选项手动配置并保护VPN连接。

#### 使用应用启用BTH

要设置返回首页，您应拥有一部安装了BTH应用的智能手机，并且位于家中，连接到路由器的WiFi网络。

- 使用手机连接到路由器的Wi-Fi。
- 打开返回首页应用（[Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn)，[iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198)）。
- 点击“创建新”。
- 输入您的本地路由器IP地址（很可能是`192.168.88.1`）、用户名和密码，然后点击“连接”。
- 为隧道命名，然后点击“创建隧道”。
- 您的手机将请求添加新VPN设置的权限。使用手机PIN码批准。
- 设置完成。您现在可以断开与路由器Wi-Fi的连接，并连接到任何其他网络，如LTE/5G，或者现在直接离开家。
- 点击“连接”按钮以切换所选隧道的连接状态。

| ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_01.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_02.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_03.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_04.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_05.png) |
| :-- | :-- | :-- | :-- | :-- |
| 点击“创建新” | 提供您的路由器凭据 | 连接已建立 | 允许添加VPN | 如果设备不受支持，将显示错误 |

#### 与另一手机用户共享BTH连接

可以为您的朋友和家人创建访客隧道。您甚至可以指定这些人是仅通过您的路由器访问互联网，还是也可以访问您的本地网络。创建共享隧道后，您可以通过手机上的任何聊天应用发送邀请链接，或当面给朋友展示QR码（在这两种情况下，朋友也需要安装BTH应用）。如果您想通过另一部手机或计算机上的WireGuard(TM)应用连接到您的路由器，也是可以的。只需选择共享WireGuard(TM)配置文件，并在WireGuard(TM)应用中打开该文件即可。

| ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_06.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_07.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_08.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_17.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_09.jpg) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_10.jpg) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 管理共享 | 首先连接到您的隧道 | 连接后，创建共享 | 提供名称和访问级别 | 共享面板打开 | 通过WhatsApp、Signal等发送邀请链接 |

要与某人共享您的隧道：

- 作为所有者，连接到您的BTH隧道。
- 点击隧道旁边的“...”图标，然后点击“管理共享”。
- 输入路由器的管理密码，因为您将修改路由器配置。
- 在共享管理器中点击“创建”。
- 在“隧道名称”中输入您朋友的名字，因为将为他们创建新隧道。
- 指定此新访客隧道的到期日期。
- 指定用户是否需要访问您的家庭内部网络。如果他们只想将此隧道用于互联网访问，请不要勾选此项。
- 按下“创建隧道”后，手机共享面板将打开。选择发送邀请链接的方式。
- 对方点击此链接后，将被引导安装BTH应用，或者BTH应用将打开并允许他们在手机上设置此新访客隧道。

#### 通过WireGuard(TM)应用与计算机共享BTH隧道

由于没有适用于PC的BTH应用，您可以使用[WireGuard(TM)应用](https://www.wireguard.com/install/)连接到共享隧道。您甚至可以与自己共享连接，通过“邀请”您的计算机进行连接。

让我们创建一个新的共享，这次是为您自己，供PC使用。

| ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_13.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_14.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_15.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_16.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_16.png) | ![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_18.png) |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 创建 | 指定名称和访问级别 | 您现在有两个共享 | 点击“...”发送邀请 | 选择“共享WireGuard配置文件” | AirDrop到您的macOS或通过电子邮件发送文件 |

在您的计算机上安装WireGuard应用，然后点击“从文件导入隧道”

![](https://manual.mikrotik.com/docs/network-management/cloud/img/back-to-home_19.jpg)

---

#### 在RouterOS中手动配置BTH（可选，如果您没有智能手机）

:::info
重要提示

需要特别注意的是，**使用返回首页功能无需在RouterOS中进行任何配置**。只需使用BTH应用（见上文）即可启用。返回首页的全部意义在于避免使用Winbox或命令行。以下说明仅供调试或经验丰富的管理员参考。
:::

1. 连接到路由器
2. 启用DDNS云服务：``/ip/cloud/set ddns-enabled=yes``
3. 启用返回首页：``/ip/cloud/set back-to-home-vpn=enabled``
4. 打印隧道配置：``/ip/cloud/print``
5. 扫描QR码（``vpn-wireguard-client-config-qrcode``）或复制配置（``vpn-wireguard-client-config``）并输入到首选的WireGuard客户端中。同一时间仅有一个客户端可以使用此配置。  

   :::warning
   配置返回首页后 - 会自动添加一个额外的对等条目，可通过运行命令 *`/ip/cloud/print`* 查看。这是为了让VPN在设备无法访问公网IP地址并选择通过MikroTik的中继服务器建立连接时正常工作。  
   如果您的设备可以访问公网IP地址，生成的对等条目将被忽略：

   ```
   [Peer]
   PublicKey = //////////////////////////////////////////8=
   AllowedIPs = 0.0.0.0/32
   Endpoint = example.com:12345
   PersistentKeepalive = 15 
   ```

   :::

#### 移除和禁用连接

在智能手机应用中，VPN配置被添加到系统VPN设置中。在这方面，返回首页应用仅充当向导。它向操作系统提供所需的配置（这就是iPhone会警告您修改系统配置的原因）。

要移除已创建的连接，请进入智能手机的设置应用，并从那里删除VPN连接。

在MikroTik路由器端，您应手动删除Wireguard菜单中添加的对等条目。请注意，“撤销并禁用”按钮不能用于“暂停”返回首页功能的使用。一旦您在RouterOS中执行撤销并禁用，所有对等条目将与云/中继服务器解除关联，您将需要从智能手机应用重新创建连接。因此，一旦您在RouterOS IP云菜单中使用了“撤销并禁用”选项，您还需要从Wireguard菜单中删除对等条目，因为它们无法重新使用。

## 属性参考

### IP云

**子菜单：** `/ip/cloud`

返回首页与IP云共享菜单。返回首页参数：

| 属性 | 描述 |
| :-- | :-- |
| **back-to-home-vpn** (*enabled \| revoked-and-disabled*；默认值：**revoked-and-disabled**) | 启用或撤销并禁用返回首页服务。ddns-enabled不能设置为no，BTH才能正常工作。 |
| **vpn-dns-name** (*只读：字符串*) | 显示分配给设备的DNS名称。该名称由产品序列号后接*.vpn.mynetname.net*组成。此字段仅在至少一次ddns请求成功完成后可见。 |
| **vpn-port** (*只读：整数*) | BTH VPN使用的端口。 |
| **vpn-status** (*只读：字符串*) | 包含描述当前BTH状态的文本字符串。 |
| **vpn-relay-rtts** (*只读；* "区域 (ip4: 时间(**ms**), ip6: 时间 (**ms**)" ) | 每个可用中继的往返时间（毫秒），同时显示IPv4和IPv6的值。 |
| **vpn-relay-ipv4-status** (*只读：字符串*) | 与中继的连接状态及中继的详细信息 |
| **vpn-relay-ipv6-status** (*只读：字符串*) | 与中继的连接状态及中继的详细信息 |
| **vpn-relay-regions** (*只读：字符串*) | 可用的VPN中继区域，可在vpn-prefer-relay-code中引用。所有可用的中继将在此显示。 |
| **vpn-relay-addressess** (*只读：字符串*) | 中继的IPv4地址 |
| **vpn-relay-addressess-ipv6** (*只读：字符串*) | 中继的IPv6地址 |
| **vpn-private-key** (*只读：字符串*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | BTH的私钥 |
| **vpn-public-key** (*只读：字符串*) | BTH的公钥 |
| **vpn-peer-private-key** (*只读：字符串*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 对等私钥 |
| **vpn-peer-public-key** (*只读：字符串*) | 对等公钥 |
| **vpn-prefer-relay-code** (*字符串；*) | 您可以输入一个中继代码，该中继将被优先用于BTH连接，如果未设置，将选择RTT最小的中继。 |
| **vpn-interface** (*只读：字符串*) | 为返回首页WireGuard隧道创建的接口名称。 |
| **vpn-wireguard-client-config** (*只读：字符串*) | 可在您首选的WireGuard客户端中输入的配置。同一时间仅有一个客户端可以使用此配置。 |
| **vpn-wireguard-client-config-qrcode** (*只读*) | 适用于您首选WireGuard客户端的可扫描QR码。同一时间仅有一个客户端可以使用此配置。 |

:::info
使用vpn-wireguard-client-config或vpn-wireguard-client-config-qrcode时，两个选项是等效的；您只需将其中一个导入到您的WireGuard客户端设备即可。
:::

### 返回首页用户

**子菜单：** `/ip/cloud/back-to-home-user`

自RouterOS 7.14起，在菜单`/ip/cloud/back-to-home-user`中提供了新的返回首页专用用户管理器，您可以查看由返回首页移动应用添加的所有用户，更改其防火墙偏好，并添加新用户。

```
[boss@mikrotik-ax] /ip/cloud/back-to-home-user> print detail   
Flags: X - disabled; A - active   
  
 0  A name="user1" slot=3 expires=never client-address=192.168.216.3/32,fc00:0:0:216::3/128 allow-lan=no   
      private-key="OHqR2BZXJp0N6//3JzzoJhBJVb0rrSxV0dxQL/2UdXY=" public-key="Na7oEq9XLdeK8ouCUX+tC4FIM51vEnZ7mLiFqG9xiUQ="   
  
[boss@mikrotik-ax] /ip/cloud/back-to-home-user>
```

在此菜单中添加用户时，您可以使用以下命令查看其Wireguard配置和QR码：`/interface/wireguard/peers/show-client-config user1`

`Allow-lan=no`会将用户添加到仅允许互联网访问的防火墙地址列表中，但阻止用户访问您的内部网络。请注意，用户添加后，到期日期无法更改。

| 属性 | 描述 |
| :-- | :-- |
| **name** (*字符串*) | BTH用户的信息性名称 |
| **expires** (*字符串；never \| 日期：*"YYYY-MM-DD HH:MM:SS"*；默认值：**never***) | 用户的到期时间和日期。用户创建后无法更改 |
| **client-address** (*字符串：IPv4 \| IPv6*) | 客户端地址。如果未指定，将自动生成一个 |
| **allow-lan** (*字符串：yes \| no；默认值：**no**) | 将用户添加到仅允许互联网访问的防火墙地址列表中，但阻止用户访问您的内部网络 |
| **private-key** (*字符串；*) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 用户的私钥，如果未手动设置，将由系统生成 |
| **public-key** (*字符串；*) | 用户的公钥，如果未手动设置，将由系统生成 |