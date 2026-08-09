# WiFi CAPsMAN

> WiFi CAPsMAN（受控接入点系统管理器）用于 wifi-qcom / wifi-qcom-ac 软件包，集中管理多个 WiFi 接入点。涵盖 CAP 发现、无线电配置、数据通路/转发模式、VLAN 和 OWE 示例，以及 CAPsMAN/CAP/配置属性参考。

# WiFi CAPsMAN

:::info
本节介绍 wifi-qcom 和 wifi-qcom-ac 软件包中 CAPsMAN 功能的操作。对于使用旧版 "wireless" 软件包的设备，请参阅 [相应手册](../abgn/capsman/index.md)。在下文中，当提到 "WiFi" 时，我们指的是新的 WiFi 菜单，而非该技术本身。
:::

受控接入点系统管理器（CAPsMAN）允许从中央配置界面将无线设置应用于多个 MikroTik WiFi AP 设备，即实现无线网络管理的集中化。使用 CAPsMAN 时，网络将由多个提供无线连接的“受控接入点”（CAP）和一个管理 AP 配置并负责客户端认证的“系统管理器”（CAPsMAN）组成。

要求：

- 任何支持 WiFi 软件包的 RouterOS 设备，只要至少拥有 RouterOS Level 4 许可证，即可作为受控无线接入点（CAP）。
- WiFi CAPsMAN 服务器可以安装在任何支持 WiFi 软件包的 RouterOS 设备上，即使该设备本身没有无线接口。
- CAPsMAN 支持无限数量的 CAP（接入点）。

:::info
WiFi CAPsMAN 只能控制 WiFi 接口，且 WiFi CAP 只能加入 WiFi CAPsMAN。同样，常规 CAPsMAN 仅支持非 WiFi 的 CAP。

CAP 不会向 CAPsMAN 发送流量使用信息。
:::

### CAP 对 CAPsMAN 的发现

CAP 通过以下方式发现 CAPsMAN 地址/主机名：

- 二层发现。
- DHCP 选项 138（CAPsMAN 地址）。
- DHCP 选项 15（自定义域名）：`解析 _capsman._tcp.<domain>.`
- 默认 MikroTik 'lan' 域名：`解析 _capsman._tcp.lan.`

### 无线电配置

创建配置模板后，您可以选择哪些设备应使用每个模板进行配置。当然，在简单设置中，只需一条配置规则即可。但如果您希望将一种配置发送到 2.4GHz 接口，将另一种配置发送到 5GHz 接口，则可以创建两条配置规则，并使用 `supported-bands` 参数定义将哪个模板发送到何处。

CAPsMAN 根据无线接口的内置 MAC 地址（radio-mac）来区分实际的无线接口（无线电）。这意味着在同一个 CAPsMAN 上无法管理两个具有相同 MAC 地址的无线电。当前由 CAPsMAN 管理（由已连接的 CAP 提供）的无线电列在 `/interface/wifi/radio` 菜单中。如果 CAPsMAN 自身有内置 WiFi 接口，该列表也将包含这些接口：

```ros
[admin@c52i] > /interface/wifi/radio/print 
Flags: L - LOCAL
Columns: CAP, RADIO-MAC, INTERFACE
#   CAP                  RADIO-MAC          INTERFACE 
0 L                      18:FD:74:AF:F4:28  wifi1     
1 L                      18:FD:74:AF:F4:29  wifi2     
2   hapAX3@192.168.88.30  48:A9:8A:0B:F7:4B  cap1
```

当 CAP 连接时，CAPsMAN 首先尝试根据 radio-mac 将每个 CAP 无线电绑定到 CAPsMAN 主接口。如果找到合适的接口，则使用主接口配置以及引用该特定主接口的从接口配置来设置无线电。此时，接口（主接口和从接口）被视为已绑定到无线电，且无线电被视为已配置。这仅在 `/interface/wifi` 下已存在匹配的静态条目时发生，通常该条目是先前手动创建的，或由包含 "create-enabled" 或 "create-disabled" 操作的配置规则创建的。

如果未找到与无线电匹配的主接口，CAPsMAN 将执行在 `/interface/wifi/provisioning/` 下定义的“配置规则”。配置规则是一个有序列表，包含指定匹配哪个无线电的设置以及确定匹配后采取何种操作的设置。

当 CAP 加入 CAPsMAN 时，如果 `/interface/wifi` 下没有与其匹配的接口，将自动检查配置规则。一旦找到匹配项，CAP 的无线接口将出现在 `/interface/wifi` 下。这样的接口是“已配置的”，在此上下文中，已配置意味着该无线电存在一个 WiFi 接口，并且已为其分配了配置配置文件。

还有一个选项可以手动配置接口，这将使 CAPsMAN 开始针对特定接口评估配置规则，并在匹配时创建新接口。如果 `/interface/wifi/` 下已存在该无线电的条目，该条目将被删除并重新创建。手动配置会重新创建接口，并且**通常不需要**，因为配置规则会自动评估，如果您更改了与配置规则关联的配置配置文件，更改将应用于使用该配置的所有 WiFi 接口。如果您手动配置接口，接口 ID 或名称可能会更改，从而导致对其他对象的引用中断，例如桥接端口。

手动配置可以在 `/interface/wifi/capsman/remote-cap/provision` 下执行，以配置与特定 CAP 关联的所有无线电；也可以在 `/interface/wifi/radio/provision` 下执行，以配置特定的无线电。

CAPsMAN 无法使用 `configuration.manager=capsman` 管理其自身的 WiFi 接口，只需像使用配置规则一样在本地接口上手动设置相同的配置配置文件即可，最终结果与它们作为 CAP 时相同。话虽如此，也可以通过 `/interface/wifi/radio` 菜单配置本地接口，但应注意，要在配置后重新控制本地接口，您需要禁用匹配的配置规则并再次按下“provision”，这将使本地接口恢复到未配置状态。

:::info
配置必须仅在初始时进行，并且在 CAP 加入时，如果存在已启用的匹配配置规则，则会自动完成。
如果您调整了任何与已配置接口关联的配置配置文件，所有更改将在您应用更改后立即“推送”，无需重新创建现有接口。
配置本身并非用于发送配置，而是用于创建新接口。在大多数情况下，一旦您已有 CAP 接口在运行，就没有理由执行手动配置。
:::

### CAPsMAN 数据通路

数据通路设置控制与数据转发相关的方面。在 CAPsMAN 上，数据通路设置在数据通路配置文件菜单 **/interface/wifi/datapath/** 中配置，或直接在配置配置文件或接口菜单中使用带有 **datapath.** 前缀的设置进行配置。

有两种主要的转发/流量处理模式：

- 本地转发模式（`traffic-processing=on-cap`），其中 CAP 本地转发来自/去往无线接口的数据；
- CAPsMAN 转发模式（`traffic-processing=on-capsman`），其中 CAP 将通过无线接收的所有数据发送到 CAPsMAN，并且仅发送从 CAPsMAN 接收的无线数据。

:::info
CAPsMAN 转发仅从 **7.21beta2** 版本开始支持。**在旧版本上，仅支持 CAP 转发。**

**wifi-qcom-ac** 设备不支持 CAPsMAN 转发（wifi-qcom-ac 驱动仅**支持** **本地转发**）。
:::

### CAPsMAN - CAP 简单配置示例

WiFi 中的 CAPsMAN 使用与常规 WiFi 接口相同的菜单，这意味着当您向 CAP 传递配置时，您必须使用与常规 WiFi 接口相同的配置、安全、信道配置等。

:::info
您可以直接在 `/interface/wifi/configuration` 下配置子配置菜单，或在主配置配置文件中引用先前创建的配置文件。
:::

#### CAPsMAN

```ros
# 创建安全配置文件
/interface/wifi/security
add authentication-types=wpa3-psk name=sec1 passphrase=HaveAg00dDay

# 创建用于配置的配置配置文件
/interface/wifi/configuration
add country=Latvia name=5ghz security=sec1 ssid=CAPsMAN_5
add name=2ghz security=sec1 ssid=CAPsMAN2
add country=Latvia name=5ghz_v security=sec1 ssid=CAPsMAN5_v

# 配置配置规则，根据需要配置频段匹配
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=5ghz slave-configurations=5ghz_v supported-bands=\
    5ghz-n
add action=create-dynamic-enabled master-configuration=2ghz supported-bands=2ghz-n

# 启用 CAPsMAN 服务
/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

#### CAP

```ros
# 启用 CAP 服务，本例中 CAPsMAN 在同一 LAN 上，但您也可以在此处指定 "caps-man-addresses=x.x.x.x"
/interface/wifi/cap/set enabled=yes

# 在应充当 CAP 的 WiFi 接口上设置 configuration.manager=
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

:::warning
如果 CAP 是 hAP ax<sup>2</sup> 或 hAP ax<sup>3</sup>，强烈建议在 CAP 的桥接配置中启用 RSTP。

configuration.manager 应仅在 CAP 设备本身上设置，不要将其传递给 CAP 或您配置的配置配置文件。
:::

:::info
应充当 CAP 的接口需要在 `/interface/wifi/set wifi1 configuration.manager=` 下进行额外配置。
:::

### CAPsMAN - CAP VLAN 配置示例

在此示例中，我们将为我们的主 SSID 分配 VLAN10，并为访客网络添加 VLAN20，CAPsMAN 的 ether5 连接到 CAP。

:::info
使用 "wifi-qcom" 软件包的 CAP 可以通过 CAPsMAN 的数据通路获取 "vlan-id"，使用 "wifi-qcom-ac" 软件包的 CAP 将需要使用本示例末尾提供的配置。
:::

#### CAPsMAN

```ros
/interface/bridge
add name=br vlan-filtering=yes
/interface/vlan
add interface=br name=MAIN vlan-id=10
add interface=br name=GUEST vlan-id=20
/interface/wifi/datapath
add bridge=br name=MAIN vlan-id=10
add bridge=br name=GUEST vlan-id=20
/interface/wifi/security
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_MAIN passphrase=HaveAg00dDay
add authentication-types=wpa2-psk,wpa3-psk ft=yes ft-over-ds=yes name=Security_GUEST passphrase=HaveAg00dDay
/interface/wifi/configuration
add datapath=MAIN name=MAIN security=Security_MAIN ssid=MAIN_Network
add datapath=GUEST name=GUEST security=Security_GUEST ssid=GUEST_Network
/ip/pool
add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254
add name=dhcp_pool1 ranges=192.168.10.2-192.168.10.254
add name=dhcp_pool2 ranges=192.168.20.2-192.168.20.254
/ip/dhcp-server
add address-pool=dhcp_pool0 disabled=yes interface=br name=dhcp1
add address-pool=dhcp_pool1 interface=MAIN name=dhcp2
add address-pool=dhcp_pool2 interface=GUEST name=dhcp3
/interface/bridge/port
add bridge=br interface=ether5 
add bridge=br interface=ether4 
add bridge=br interface=ether3 
add bridge=br interface=ether2 
/interface/bridge/vlan
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=20
add bridge=br tagged=br,ether5,ether4,ether3,ether2 vlan-ids=10
/interface/wifi/capsman
set enabled=yes interfaces=br
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=5ghz-ax
add action=create-dynamic-enabled master-configuration=MAIN slave-configurations=GUEST supported-bands=2ghz-ax
/ip/address
add address=192.168.1.1/24 interface=br network=192.168.1.0
add address=192.168.10.1/24 interface=MAIN network=192.168.10.0
add address=192.168.20.1/24 interface=GUEST network=192.168.20.0
/ip/dhcp-server/network
add address=192.168.1.0/24 gateway=192.168.1.1
add address=192.168.10.0/24 gateway=192.168.10.1
add address=192.168.20.0/24 gateway=192.168.20.1
/system/identity
set name=cAP_Controller
```

#### 使用 "wifi-qcom" 软件包的 CAP

```ros
/interface/bridge
add name=bridgeLocal
/interface/wifi/datapath
add bridge=bridgeLocal comment=defconf disabled=no name=capdp
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman datapath=capdp disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman datapath=capdp disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-datapath=capdp
/ip/dhcp-client
add interface=bridgeLocal disabled=no
```

#### 使用 "wifi-qcom-ac" 软件包的 CAP

```ros
/interface/bridge
add name=bridgeLocal vlan-filtering=yes
/interface/wifi
set [ find default-name=wifi1 ] configuration.manager=capsman disabled=no
set [ find default-name=wifi2 ] configuration.manager=capsman disabled=no
/interface/bridge/port
add bridge=bridgeLocal comment=defconf interface=ether1
add bridge=bridgeLocal comment=defconf interface=ether2
add bridge=bridgeLocal comment=defconf interface=ether3
add bridge=bridgeLocal comment=defconf interface=ether4
add bridge=bridgeLocal comment=defconf interface=ether5
add bridge=bridgeLocal interface=wifi1 pvid=10
add bridge=bridgeLocal interface=wifi21 pvid=20
add bridge=bridgeLocal interface=wifi2 pvid=10
add bridge=bridgeLocal interface=wifi22 pvid=20
/interface/bridge/vlan
add bridge=bridgeLocal tagged=ether1 untagged=wifi1,wifi2 vlan-ids=10
add bridge=bridgeLocal tagged=ether1 untagged=wifi21,wifi22 vlan-ids=20
/interface/wifi/cap
set discovery-interfaces=bridgeLocal enabled=yes slaves-static=yes
```

:::info
检查动态创建的接口并将 PVID 分配给适当的接口。确保不要使用 `/interface/bridge/port/add bridge=bridgeLocal interface=all`，因为这会阻止您将 PVID 应用于 WiFi 接口。
:::

此外，必须将以下配置添加到 **CAPsMAN 配置**中：

```ros
/interface/wifi/datapath
add bridge=br name=DP_AC
/interface/wifi/configuration
add datapath=DP_AC name=MAIN_AC security=Security_MAIN ssid=MAIN_Network
add datapath=DP_AC name=GUEST_AC security=Security_GUEST ssid=GUEST_Network
/interface/wifi/provisioning
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=5ghz-ac
add action=create-dynamic-enabled master-configuration=MAIN_AC slave-configurations=GUEST_AC supported-bands=2ghz-n
```

:::info
将示例开头的数据通路 "MAIN/GUEST" 传递给 "wifi-qcom-ac" CAP 将是一个错误配置，请确保对此类设备使用未指定 "vlan-id" 的数据通路。

对于 wifi-qcom-ac 驱动，CAPsMAN 上的数据通路设置不是必需的。该示例仅用于说明必须省略 "vlan-id"。
:::

### CAPsMAN - OWE 配置示例

#### CAPsMAN

```ros
/interface/wifi/configuration
add country=Latvia disabled=no hide-ssid=yes name=OWE security.authentication-types=owe .owe-transition-interface=auto ssid=MikroTik_OWE
add country=Latvia disabled=no name=open security.owe-transition-interface=auto ssid=Mikrotik_open

/interface/wifi/provisioning
add action=create-dynamic-enabled disabled=no master-configuration=open slave-configurations=OWE

/interface/wifi/capsman
set ca-certificate=auto enabled=yes
```

#### CAP

```ros
/interface/wifi/cap/set enabled=yes
/interface/wifi/set wifi1,wifi2 configuration.manager=capsman-or-local
```

## 属性参考

### CAPsMAN 全局配置

菜单：`/interface/wifi/capsman`

| 属性 | 描述 |
| :-- | :-- |
| **ca-certificate** (*auto \| 证书名称*) | 设备 CA 证书，CAPsMAN 服务器需要证书，CAP 上的证书是可选的。 |
| **certificate** (*auto \| 证书名称 \| none*; 默认值：**none**) | 设备证书 |
| **enabled** *(no* \| *yes*) | 禁用或启用 CAPsMAN 功能 |
| **package-path** (*string*) | RouterOS 软件包的文件夹位置。例如，使用 "/upgrade" 指定文件部分中的升级文件夹。如果设置为空字符串，CAPsMAN 可以使用内置的 RouterOS 软件包。请注意，在这种情况下，只有与 CAPsMAN 具有相同架构的 CAP 才会被升级。 |
| **require-peer-certificate** (*yes \| no; 默认值：**no**)* | 要求所有连接的 CAP 都具有有效证书 |
| **upgrade-policy** *(none \| require-same-version \| suggest-same-upgrade; 默认值：**none**)* | 升级策略选项 none - 不执行升级require-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败，则不会配置该 CAP。（手动配置仍然可能）suggest-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败，仍将配置该 CAP |
| **interfaces** *(all \| 接口名称 \| none; 默认值：**all**)* | CAPsMAN 将监听二层 CAP 连接的接口 |

### CAPsMAN 配置

用于匹配无线电的配置规则在 `/interface/wifi/provisioning/` 菜单中配置：

| 属性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled \| create-enabled \| create-dynamic-enabled \| none; 默认值：**none**)* | 规则匹配时要采取的操作由以下设置指定：create-disabled - 为无线电创建禁用的静态接口。即，接口将绑定到无线电，但在手动启用接口之前，无线电不会运行；create-enabled - 创建启用的静态接口。即，接口将绑定到无线电，并且无线电将运行；create-dynamic-enabled - 创建启用的动态接口。即，接口将绑定到无线电，并且无线电将运行；none - 不执行任何操作，使无线电保持未配置状态；enabled 和 dynamic-enabled 之间的基本区别在于，动态接口无法手动编辑以覆盖设置，也无法在防火墙或其他菜单中被引用，因为它们将被重新创建。在这两种情况下，任何 `/interface/wifi/configuration` 更改都将自动推送到 CAP。 |
| **comment** (*string*) | 配置规则的简短描述 |
| **common-name-regexp** (*string*) | 用于按通用名称匹配无线电的正则表达式。每个 CAP 的通用名称标识符可以在 `/interface/wifi/radio` 下找到，值为 "REMOTE-CAP-NAME" |
| **supported-bands** (*2ghz-ax \| 2ghz-be \| 2ghz-g \| 2ghz-n \| 5ghz-a \| 5ghz-ac \| 5ghz-ax \| 5ghz-be \| 5ghz-n \| 60ghz-ad \| 6ghz-ax \| 6ghz-be*) | 按支持的无线模式匹配无线电。此参数接受一个或多个频段，以逗号分隔的列表形式（例如，*supported-bands=5ghz-ac,5ghz-ax*）。当指定多个频段时，设备必须支持所有列出的频段，匹配才能成功并应用定义的配置。 |
| **supported-hw-caps** (*beacon-protection \| channel-switch \| hw-protection-mode \| mlo \| qos-qualifier \| sniffer \| spectral*) | 按 `/interface/wifi/radio` 下 *hw-caps* 字段报告的无线电支持的附加功能进行匹配。接受一个或多个逗号分隔的值。无线电必须支持所有列出的功能才能匹配此配置规则。 |
| **identity-regexp** (*string*) | 用于按路由器身份匹配无线电的正则表达式 |
| **address-ranges** (*IpAddressRange[,IpAddressRanges] 最多 100 个*;) | 匹配 IP 在配置的地址范围内的 CAP。仅适用于使用 IP（而非 MAC 地址）加入 CAPsMAN 的 CAP。 |
| **master-configuration** (*string*) | 如果 **action** 指定创建接口，则将创建一个新的主接口，其配置设置为此配置配置文件 |
| **multi-link-mode** (*all \| auto \| disabled \| master; 默认值：**disabled**)* | 控制配置期间的 MLO（多链路操作）行为。all 或 auto - CAPsMAN 将自动分配已配置的 WiFi 接口作为 MLD 接口的关联链路。如果匹配的 MLD 接口尚不存在，将使用相应的配置创建一个。这适用于主接口和从接口；disabled - 配置期间不创建或分配 MLD 接口；master - 与 **all** 或 **auto** 行为相同，但仅将主接口添加为关联的 MLD 链路； |
| **name-format** (*string*) | 用于构造已配置接口名称的基本字符串。每个新接口将通过获取基本字符串并在其末尾附加一个数字来创建。仅当字符串不唯一时才会附加数字。如果字符串中包含字符序列 **%I**，它将被 cAP 的系统身份替换，**%C** 将被 cAP 的 TLS 证书的通用名称替换，**%R**（或小写 **%r**）将被 CAP 的无线电 MAC 地址替换。默认值："cap-wifi" |
| **slave-name-format** (*string*) | 用于构造虚拟接口名称的基本字符串。每个新接口将通过获取基本字符串并在其末尾附加一个数字来创建。仅当字符串不唯一时才会附加数字。如果字符串中包含字符序列 **%v**，它将被 "virtual" 替换，字符序列 **%m** 将被主接口的名称替换，如果字符串中包含字符序列 **%I**，它将被 cAP 的系统身份替换，**%C** 将被 cAP 的 TLS 证书的通用名称替换，**%R**（或小写 **%r**）将被 CAP 的无线电 MAC 地址替换。默认值："*主接口名称*-virtual" |
| **radio-mac** (*MAC 地址*) | 要匹配的无线电的 MAC 地址。无默认值。 |
| **slave-configurations** (*string*) | 如果 **action** 指定创建接口，则为该列表中的每个配置配置文件创建一个新的从接口。 |
| **disabled** (*yes* *\| no*) | 指定配置规则是否被禁用。 |

### CAP 配置

菜单：`/interface/wifi/cap`

| 属性 | 描述 |
| :-- | :-- |
| **caps-man-addresses** *(IP 地址或主机名列表; 默认值：*  \_capsman.\_tcp.lan) | CAP 在发现期间将尝试联系的逗号分隔的管理器 IP 地址或主机名列表 |
| **caps-man-names** () | CAP 将连接的有序 CAPs Manager 名称列表，如果为空 - CAP 不检查 Manager 名称 |
| **discovery-interfaces** (*接口列表*) | CAP 应尝试通过其发现管理器的接口列表 |
| **lock-to-caps-man** (*yes \| no; 默认值：**no***) | 设置 CAP 是否应锁定到其连接的第一个 CAPsMAN。 |
| **slaves-static** (*yes \| no; 默认值：**no***) | 创建静态虚拟接口，并允许为这些接口分配 IP 配置的可能性。应用来自 CAPsMAN 的配置时，使用 MAC 地址来记住每个静态接口。 |
| **mld-static** (*yes \| no; 默认值：**no***) | 设置为 yes 时，CAPsMAN 在 cAP 上创建的 MLD 接口是静态的；否则，它们是动态的。静态接口具有持久的内部 ID，可以手动操作、添加到桥接、在防火墙规则中引用等。动态接口在重启后不会保留。应为其分配适当的数据通路配置文件。 |
| **caps-man-certificate-common-names** () | CAP 将连接的管理器证书通用名称列表，如果为空 - CAP 不检查管理器证书通用名称 |
| **certificate** () | 用于认证的证书 |
| **enabled** (*yes \| no; 默认值：**no***) | 禁用或启用 CAP 功能 |
| **current-caps-man-address** () | 显示当前使用的 CAPsMAN 地址 |
| **current-caps-man-identity** () | 显示当前使用的 CAPsMAN 身份 |
| **slaves-datapath** *(数据通路配置文件)* | 应用于从接口的数据通路配置文件。主要用于指定从接口在 CAP 上自动添加到的桥接。使用本地转发（*traffic-processing=on-cap*）时需要，因为在该模式下，所有路由和转发决策都由 CAP 自身做出——CAPsMAN 不会将这些接口包含在其自身的桥接中，因此必须在此处或 CAP 上手动设置数据通路。 |
| **mld-datapath** *(数据通路配置文件)* | 应用于 CAPsMAN 创建的 MLD 接口的数据通路配置文件。确定流量如何在 MLD 接口上转发，包括将其添加到哪个桥接，以及转发是在 CAP 上本地处理还是由 CAPsMAN 集中处理。仅在启用 MLD 时生效。 |

### 远程 CAP

可以通过运行 `/interface/wifi/capsman/remote-cap/print detail` 命令查看远程 CAP 的信息。

| 属性 | 描述 |
| :-- | :-- |
| **address**(*IP 地址/MAC 地址%接口*) | CAP 的 IP 地址或用于连接 CAPsMAN 的 MAC 地址 |
| **identity** (*整数列表*) | CAP 的已配置系统身份 |
| **board-name** (*string*) | 描述型号名称 |
| **serial** (*string*) | CAP 的序列号 |
| **version** (*string*) | CAP 的 RouterOS 版本 |
| **base-mac** (*MAC 地址*) | CAP 提供的 Base-MAC，格式为：'[XX:XX:XX:XX:XX:XX]' |
| **common-name** (*string*) | CAP 的通用名称 |
| **connected-time** (*time*) | 自 CAP 连接到 CAPsMAN 以来经过的时间间隔 |
| **uptime** (*time*) | 自启动以来经过的时间间隔 |