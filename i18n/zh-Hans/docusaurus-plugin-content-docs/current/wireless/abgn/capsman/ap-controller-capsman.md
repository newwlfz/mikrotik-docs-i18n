# AP 控制器 (CAPsMAN)

> CAPsMAN（受控接入点系统管理器）通过允许 RouterOS 服务器配置多个接入点，处理客户端认证和数据转发，实现无线网络管理的集中化。它支持无限数量的 CAP（受特定硬件限制），使用 DTLS 确保管理连接的安全，并提供集中式或本地数据转发选项。

# AP 控制器 (CAPsMAN)

:::info
本页面描述的是运行 `wireless` 软件包（`/interface/wireless`）的设备的传统 CAPsMAN（`/caps-man`）。如果您的设备使用 `/interface/wifi` 菜单（`wifi-qcom` / `wifi-qcom-ac` 软件包），请参阅 [WiFi CAPsMAN](../../wifi/capsman.md)。
:::

---

CAPsMAN 允许从中央配置界面将无线设置应用于多个 MikroTik AP 设备。

更具体地说，受控接入点系统管理器（CAPsMAN）允许集中化无线网络管理，并在必要时进行数据处理。使用 CAPsMAN 功能时，网络将由多个提供无线连接的“受控接入点”（CAP）和一个管理 AP 配置的“系统管理器”（CAPsMAN）组成。它还负责客户端认证以及可选的数据转发。

当 CAP 受 CAPsMAN 控制时，它只需要最少的配置即可与 CAPsMAN 建立连接。传统上由 AP 执行的功能（如访问控制、客户端认证）现在由 CAPsMAN 执行。CAP 设备现在只需提供无线链路层的加密/解密。

根据配置，数据要么转发给 CAPsMAN 进行集中处理（*默认*），要么在 CAP 本地转发（本地转发模式）。

## 要求

- 任何 RouterOS 设备都可以作为受控无线接入点（CAP），只要它至少具有 Level 4 RouterOS 许可证。
- CAPsMAN 服务器可以安装在任何 RouterOS 设备上，即使设备本身没有无线接口。
- CAPsMAN 支持无限数量的 CAP（接入点）。
- 每个 CAP 最多支持 32 个无线接口。
- 每个主无线接口最多支持 32 个虚拟接口。
- 无法使用 Nv2 和 NStreme 专有协议。

---

## CAPsMAN 系统的简单设置

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-01.webp)

在深入探讨 CAPsMAN 操作的细节之前，让我们快速说明如何设置最基本的系统，即您有一个 MikroTik 路由器管理两个 MikroTik AP 设备。CAPsMAN 的好处在于 CAP 单元无需配置；所有设置都在 CAPsMAN 服务器上完成。

CAPsMAN 设置包括定义配置模板，然后将其推送到可控 AP 设备（CAP）。假设您的主路由器已连接到互联网并且工作正常，您可以按以下步骤操作。

在中央设备（即您的 CAPsMAN 服务器）上，创建一个新的“配置”模板，仅包含基本设置（网络名称、国家、本地 LAN 桥接接口、无线密码）：

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-02.webp)添加一个新的配置配置文件：
![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-03.webp)
![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-04.webp)

然后创建一个新的“配置”规则，该规则会将创建的配置模板分配给 CAP 设备：

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-05.webp)

在 CAPsMAN 上剩下的就是启用它：

![](https://manual.mikrotik.com/docs/wireless/abgn/capsman/img/ap-controller-capsman-06.webp)

大多数 MikroTik AP 设备开箱即支持 CAP 模式，您只需确保它们与 CAPsMAN 在同一网络上，然后按住重置按钮启动它们。

例如，在 CAP 设备关闭时将其连接到 CAPsMAN 设备的某个 LAN 端口，然后按住重置按钮并给 CAP 设备上电。持续按住按钮直到用户 LED 变为常亮，然后松开以开启 CAP 模式。设备现在将寻找 CAPsMAN 服务器（按住按钮的总时间约为 10 秒）。

设备现在将出现在 CAPsMAN 的“远程 CAP”菜单中，并将根据配置设置使用配置模板进行“配置”。有关如何手动调整所有设置的更多详细信息，请继续阅读本文档。

### CAP 到 CAPsMAN 的连接

为使 CAPsMAN 系统正常运行并提供无线连接，CAP 必须与 CAPsMAN 建立管理连接。管理连接可以使用 MAC 或 IP 层协议建立，并使用“DTLS”进行保护。

CAP 也可以将客户端数据连接传递给管理器，但数据连接不受保护。如果认为有必要，则需要使用其他数据安全手段，例如 IPSec 或加密隧道。

CAP 到 CAPsMAN 的连接可以使用 2 种传输协议（通过第 2 层和第 3 层）建立。

- MAC 层连接特性：
  - CAP 上无需 IP 配置。
  - CAP 和 CAPsMAN 必须位于同一第 2 层网段 - 物理或虚拟（通过 L2 隧道）。
- IP 层（UDP）连接特性：
  - 如有必要，可以穿越 NAT。
  - CAP 必须能够使用 IP 协议访问 CAPsMAN。
  - 如果 CAP 与 CAPsMAN 不在同一 L2 网段，则必须配置 CAPsMAN IP 地址，因为基于 IP 多播的发现无法在第 3 层上工作。

为了与 CAPsMAN 建立连接，CAP 执行发现过程。在发现期间，CAP 尝试联系 CAPsMAN 并构建可用 CAPsMAN 列表。CAP 尝试通过以下方式联系可用的 CAPsMAN：

- 配置的管理器 IP 地址列表。
- 从 DHCP 服务器获取的 CAPsMAN IP 地址列表。
- 在配置的接口上使用 IP 和 MAC 层协议进行广播。

构建可用 CAPsMAN 列表后，CAP 根据以下规则选择 CAPsMAN：

- 如果 **caps-man-names** 参数指定了允许的管理器名称（CAPsMAN 的 `/system/identity`），CAP 将优先选择列表中较早的 CAPsMAN；如果列表为空，它将连接到任何可用的管理器。
- 具有 MAC 层连接性的合适管理器优先于具有 IP 连接性的管理器。

选择管理器后，CAP 尝试建立 DTLS 连接。有以下可能的认证模式：

- CAP 和 CAPsMAN 上均无证书 - 无认证。
- 仅管理器配置了证书 - CAP 检查 CAPsMAN 证书，但如果其没有适当的受信任 CA 证书，则不会失败，CAPsMAN 必须配置 **require-peer-certificate=no** 才能与没有证书的 CAP 建立连接。
- CAP 和 CAPsMAN 均配置了证书 - 相互认证。

DTLS 连接建立后，CAP 可以选择检查 CAPsMAN 提供的证书的 CommonName 字段。**caps-man-certificate-common-names** 参数包含允许的 CommonName 值列表。如果此列表不为空，则 CAPsMAN 必须配置证书。如果此列表为空，则 CAP 不检查 CommonName 字段。

如果 CAPsMAN 或 CAP 与网络断开连接，CAP 和 CAPsMAN 之间的连接丢失将在约 10-20 秒内被检测到。

#### CAP 自动锁定到 CAPsMAN

CAP 可以配置为自动锁定到特定的 CAPsMAN 服务器。锁定是通过记录 CAP 锁定的 CAPsMAN 的证书 CommonName，并在所有后续连接中检查此 CommonName 来实现的。由于此功能是使用证书 CommonName 实现的，因此使用证书是锁定工作的必要条件。

通过以下命令启用锁定：

```
[admin@CAP] > /interface/wireless/cap/set lock-to-caps-man=yes
```

一旦 CAP 连接到合适的 CAPsMAN 并锁定到它，就会如下所示：

```
[admin@wtp] > /interface/wireless/cap/print
...
        locked-caps-man-common-name: CAPsMAN-000C424C30F3
```

从现在开始，CAP 将仅连接到具有此 CommonName 的 CAPsMAN，直到通过设置 **lock-to-caps-man=no** 清除锁定要求。如果需要强制 CAP 锁定到另一个 CAPsMAN，则需要使用此方法 - 首先设置 **lock-to-caps-man=no**，然后设置 **lock-to-caps-man=yes**。

请注意，可以通过设置 **caps-man-certificate-common-names** 手动将 CAP“锁定”到 CAPsMAN。

#### 自动证书

为了在需要证书时（例如自动锁定功能）简化 CAPsMAN 和 CAP 配置，CAPsMAN 可以配置为自动生成必要的证书，CAP 可以配置为向 CAPsMAN 请求证书。

**自动证书不提供完整的公钥基础设施**，仅用于简单设置。如果需要更复杂的 PKI - 支持适当的证书有效期、多级 CA 证书、证书续期 - 必须使用其他方式，例如手动证书分发或 SCEP。

CAPsMAN 具有以下证书设置：

- **certificate** - 这是 CAPsMAN 证书，必须为此证书提供私钥。如果设置为 **none**，CAPsMAN 将以无证书模式运行，并且所有需要证书的功能都将无法工作。如果设置为 **auto**，CAPsMAN 将尝试使用 CA 证书为自己签发证书（参见 **ca-certificate** 描述）。请注意，自动签发证书的 CommonName 将是 `CAPsMAN-<mac address>`，有效期将与 CA 证书相同。
- **ca-certificate** - 这是 CAPsMAN 在必要时为自己签发证书（参见 **certificate** 描述）以及签署来自 CAP 的证书请求时使用的 CA 证书。如果设置为 **none**，CAPsMAN 将无法为自己签发证书或签署来自 CAP 的证书请求。如果设置为 **auto**，CAPsMAN 将生成自签名 CA 证书用作 CA 证书。此证书的 CommonName 将采用 `CAPsMAN-CA-<mac address>` 形式，有效期将从 1970-01-01 到 2038-01-18。

当 CAPsMAN 自动生成证书时，将如下所示：

```
[admin@CM] /caps-man/manager> pr
                   enabled: yes
               certificate: auto
            ca-certificate: auto
  require-peer-certificate: no
     generated-certificate: CAPsMAN-000C424C30F3
  generated-ca-certificate: CAPsMAN-CA-000C424C30F3
```

以及证书：

```
[admin@CM] /certificate> print detail
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, 
A - authority, I - issued, R - revoked, E - expired, T - trusted 
 0 K   A T name="CAPsMAN-CA-000C424C30F3" common-name="CAPsMAN-CA-000C424C30F3" key-size=2048 
           days-valid=24854 trusted=yes 
           key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign 
           serial-number="1" fingerprint="69d77bbb45c50afd2d6c1785c2a3d72596b8a5f6" 
           invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 

 1 K   I   name="CAPsMAN-000C424C30F3" common-name="CAPsMAN-000C424C30F3" key-size=2048 
           days-valid=24854 trusted=no key-usage=digital-signature,key-encipherment 
           ca=CAPsMAN-CA-000C424C30F3 serial-number="1" 
           fingerprint="e853ddb9d41fc139083a176ab164331bc24bc5ed" 
           invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 
```

CAP 可以配置为向 CAPsMAN 请求证书。为此，CAP 必须配置设置 **certificate=request**，并且 CAPsMAN 必须具有可用的 CA 证书（在 **ca-certificate** 设置中指定或自动生成）。

CAP 将首先生成私钥和 CommonName 为 `CAP-<mac address>` 形式的证书请求。当 CAP 与 CAPsMAN 建立连接时，CAP 将请求 CAPsMAN 签署其证书请求。如果成功，CAPsMAN 将发送 CA 证书和新签发的证书给 CAP。CAP 将这些证书导入其证书库：

```
[admin@CAP] > /interface/wireless/cap/print
...
              requested-certificate: cert_2
        locked-caps-man-common-name: CAPsMAN-000C424C30F3
[admin@CAP] > /certificate/print detail 
Flags: K - private-key, D - dsa, L - crl, C - smart-card-key, 
A - authority, I - issued, R - revoked, E - expired, T - trusted 
 0       T name="cert_1" issuer=CN=CAPsMAN-CA-000C424C30F3 common-name="CAPsMAN-CA-000C424C30F3" 
            key-size=2048 days-valid=24837 trusted=yes 
            key-usage=digital-signature,key-encipherment,data-encipherment,key-cert-sign,crl-sign 
            serial-number="1" fingerprint="69d77bbb45c50afd2d6c1785c2a3d72596b8a5f6" 
            invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 

 1 K     T name="cert_2" issuer=CN=CAPsMAN-CA-000C424C30F3 common-name="CAP-000C4200C032" 
            key-size=2048 days-valid=24837 trusted=yes 
            key-usage=digital-signature,key-encipherment serial-number="2" 
            fingerprint="2c85bf2fbc9fc0832e47cd2773a6f4b6af35ef65" 
            invalid-before=1970-01-01 00:00:01 invalid-after=2038-01-18 03:14:07 
```

在后续与 CAPsMAN 的连接中，CAP 将使用生成的证书。

---

## CAP 配置

当 AP 配置为由 CAPsMAN 控制时，AP 上受管无线接口的配置将被忽略 *（例外：antenna-gain、antenna-mode）*。相反，AP 接受来自 CAPsMAN 的受管接口配置。

:::warning
由 CAPsMAN 管理且其流量被转发到 CAPsMAN 的 CAP 无线接口（即它们不处于 *本地转发* 模式）将显示为 *禁用*，并带有 **由 CAPsMAN 管理** 的注释。那些处于 *本地转发* 模式（流量由 CAP 本地管理，仅管理由 CAPsMAN 完成）的接口不会显示为禁用，但会显示 **由 CAPsMAN 管理** 的注释。
:::

AP 的 CAP 行为在 `/interface/wireless/cap` 菜单中配置。在那里您可以：

- 禁用或启用设备上的 CAP 功能。
- 设置由管理器控制的无线接口列表。
- 设置 CAP 应尝试发现管理器的接口列表。
- 设置 CAP 在发现期间将尝试联系的管理器 IP 地址列表。
- 设置 CAP 将尝试连接的管理器名称列表。
- 设置 CAP 将连接的管理器证书 CommonName 列表。
- 设置使用本地转发模式时接口应添加到的桥接。

CAP 上受 CAPsMAN 控制的每个无线接口在 CAPsMAN 上显示为虚拟接口。这提供了使用常规 RouterOS 功能（如路由、桥接、防火墙等）进行数据转发控制的最大灵活性。

## CAPsMAN 配置概念

许多无线接口设置可以分组为命名组（“配置文件”），以简化配置的复用 - 例如，通用配置设置可以在“配置配置文件”中配置，多个接口可以引用该配置文件。同时，任何配置文件设置都可以直接在接口配置中覆盖，以实现最大的灵活性。

目前有以下设置组：

- channel - 信道相关设置，如频率和宽度。
- datapath - 数据转发相关设置，如特定接口应自动添加为端口的桥接。
- security - 安全相关设置，如允许的认证类型或密码短语。
- configuration - 主要无线设置组，包括 SSID 等设置，并另外绑定其他设置组 - 即配置配置文件可以引用信道、安全等命名设置组。此外，任何设置都可以直接在配置配置文件中覆盖。

接口设置绑定所有设置组，但任何设置也可以直接在接口设置中覆盖。

通过设置组，配置以层次结构组织，接口（配置的实际使用者）为根。为了确定某个设置的有效值，会以较高级别的设置值覆盖较低级别值的方式查阅此结构。

例如，当需要查找特定接口使用的 WPA2 密码短语时，会查阅以下位置，第一个配置了 WPA2 密码短语的位置指定了有效的密码短语。“->”表示引用设置配置文件（如果已配置）：

- interface passphrase
- interface->security passphrase
- interface->configuration passphrase
- interface->configuration->security passphrase

CAPsMAN 上有 2 种类型的接口 - “主”和“从”。主接口保存实际无线接口（无线电）的配置，而从接口链接到主接口，旨在保存 Virtual-AP（多 SSID 支持）的配置。有些设置仅对主接口有意义，即主要是硬件设置相关设置，如无线电信道设置。请注意，为了使无线电接受客户端，其主接口需要启用。从接口只有在启用且主接口启用时才会运行。

CAPsMAN 上的接口可以是静态的或动态的。静态接口存储在 RouterOS 配置中，将在重启后保留。动态接口仅在特定 CAP 连接到 CAPsMAN 时存在。

### CAPsMAN 全局配置

启用 CAPsMAN 功能的设置位于 `/caps-man/manager` 菜单中：

| 属性 | 描述 |
| :-- | :-- |
| **enabled** (*yes \| no*; 默认值: **no**) | 禁用或启用 CAPsMAN 功能 |
| **certificate** (*auto \| certificate name \| none*; 默认值: **none**) | 设备证书 |
| **ca-certificate** (*auto \| certificate name \| none*; 默认值: **none**) | 设备 CA 证书 |
| **require-peer-certificate** (*yes \| no*; 默认值: **no**) | 要求所有连接的 CAP 都具有有效证书 |
| **package-path** (*string \|*; 默认值: ) | RouterOS 软件包的文件夹位置。例如，使用 "/upgrade" 指定文件部分中的升级文件夹。如果设置为空字符串，CAPsMAN 可以使用内置的 RouterOS 软件包，请注意在这种情况下，只有与 CAPsMAN 架构相同的 CAP 才会被升级。 |
| **upgrade-policy** (*none \| require-same-version \| suggest-same-version*; 默认值: **none**) | 升级策略选项none - 不执行升级require-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败则不会配置 CAP。（手动配置仍然可能）suggest-same-version - CAPsMAN 建议升级 CAP RouterOS 版本，如果失败仍会进行配置 |

### 无线电配置

CAPsMAN 根据标识符区分 CAP。标识符根据以下规则生成：

- 如果 CAP 提供了证书，则标识符设置为证书中的 Common Name 字段。
- 否则，标识符基于 CAP 提供的 Base-MAC，形式为：'[XX:XX:XX:XX:XX:XX]'。

当与 CAP 的 DTLS 连接成功建立（这意味着 CAP 标识符已知且有效）时，CAPsMAN 确保没有使用相同标识符的过时连接。当前连接的 CAP 列在 `/caps-man/remote-cap` 菜单中：

```
[admin@CM] /caps-man> remote-cap print
 # ADDRESS                                    IDENT           STATE               RADIOS
 0 00:0C:42:00:C0:32/27044                    MT-000C4200C032 Run                      1
```

CAPsMAN 根据其内置 MAC 地址（radio-mac）区分实际无线接口（无线电）。这意味着无法在一个 CAPsMAN 上管理两个具有相同 MAC 地址的无线电。当前由 CAPsMAN 管理的无线电（由连接的 CAP 提供）列在 `/caps-man/radio` 菜单中：

```
[admin@CM] /caps-man> radio print
Flags: L - local, P - provisioned 
 #    RADIO-MAC         INTERFACE                               REMOTE-AP-IDENT
 0  P 00:03:7F:48:CC:07 cap1                                    MT-000C4200C032
```

当 CAP 连接时，CAPsMAN 首先尝试根据 radio-mac 将每个 CAP 无线电绑定到 CAPsMAN 主接口。如果找到合适的接口，则使用主接口配置以及引用该特定主接口的从接口配置来设置无线电。此时，接口（主接口和从接口）被视为绑定到无线电，无线电被视为已配置。

如果找不到与无线电匹配的主接口，CAPsMAN 将执行“配置规则”。配置规则是一个有序规则列表，包含指定匹配哪个无线电的设置以及指定如果无线电匹配则采取什么操作的设置。

用于匹配无线电的配置规则在 `/caps-man/provisioning` 菜单中配置：

| 属性 | 描述 |
| :-- | :-- |
| **action** (*create-disabled \| create-enabled \| create-dynamic-enabled \| none*; 默认值: **none**) | 如果规则匹配，则采取以下设置指定的操作：create-disabled - 为无线电创建禁用的静态接口。即，接口将绑定到无线电，但在手动启用接口之前，无线电不会运行；create-enabled - 创建启用的静态接口。即，接口将绑定到无线电，并且无线电将运行；create-dynamic-enabled - 创建启用的动态接口。即，接口将绑定到无线电，并且无线电将运行；none - 不执行任何操作，将无线电留在未配置状态； |
| **comment** (*string*; 默认值: ) | 配置规则的简短描述 |
| **common-name-regexp** (*string*; 默认值: ) | 用于按通用名称匹配无线电的正则表达式 |
| **hw-supported-modes** (*a\|a-turbo\|ac\|an\|b\|g\|g-turbo\|gn*; 默认值: ) | 按支持的无线模式匹配无线电 |
| **identity-regexp** (*string*; 默认值: ) | 用于按路由器身份匹配无线电的正则表达式 |
| **ip-address-ranges** (*IpAddressRange[,IpAddressRanges] 最多 100 个*; 默认值: **""**) | 匹配 IP 在配置地址范围内的 CAP。 |
| **master-configuration** (*string*; 默认值: ) | 如果 **action** 指定创建接口，则将创建一个新的主接口，其配置设置为此配置配置文件 |
| **name-format** (*cap \| identity \| prefix \| prefix-identity*; 默认值: **cap**) | 指定 CAP 接口名称创建的语法cap - 默认名称identity - CAP 板的 `/system/identity` 名称prefix - 来自 name-prefix 值的名称prefix-identity - 来自 name-prefix 值和 CAP 板的 `/system/identity` 名称 |
| **name-prefix** (*string*; 默认值: ) | 可用于 name-format 中创建 CAP 接口名称的名称前缀 |
| **radio-mac** (*MAC address*; 默认值: **00:00:00:00:00:00**) | 要匹配的无线电 MAC 地址，空 MAC（00:00:00:00:00:00）表示匹配所有 MAC 地址 |
| **slave-configurations** (*string*; 默认值: ) | 如果 **action** 指定创建接口，则为列表中的每个配置配置文件创建一个新的从接口。 |

:::warning
如果没有规则匹配无线电，则执行一个隐式默认规则，其操作 **create-enabled** 且未设置配置。
:::

要获取活动的配置匹配器：

```
[admin@CM] /caps-man/provisioning> print
Flags: X - disabled 
 0   radio-mac=00:00:00:00:00:00 action=create-enabled master-configuration=main-cfg 
     slave-configurations=virtual-ap-cfg name-prefix=""
```

为了方便用户，有一些命令允许对某个无线电或某个 AP 提供的所有无线电重新执行配置过程：

```
[admin@CM] > /caps-man/radio/provision 0
```

以及：

```
[admin@CM] > /caps-man/remote-cap/provision 0
```

### 接口配置

CAPsMAN 接口在 `/caps-man/interface` 菜单中管理：

```
[admin@CM] > /caps-man/interface/print          
Flags: M - master, D - dynamic, B - bound, X - disabled, I - inactive, R - running 
 #      NAME                                 RADIO-MAC         MASTER-INTERFACE                               
 0 M BR cap2                                 00:0C:42:1B:4E:F5 none                                           
 1   B  cap3                                 00:00:00:00:00:00 cap2                   

```

### 主配置配置文件

配置配置文件允许将预定义的“顶级”主设置应用于正在配置的 CAP 无线电。

配置配置文件在 `/caps-man/configuration` 菜单中配置：

| 属性 | 描述 |
| :-- | :-- |
| **channel** (*list*; 默认值: ) | 用户定义的取自信道名称的列表（`/caps-man/channels`） |
| **channel.band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-only-ac*; 默认值: ) | 定义一组使用的信道。 |
| **channel.control-channel-width** (*40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*; 默认值: ) | 定义一组使用的信道宽度。 |
| **channel.extension-channel** (*Ce \| Ceee \| eC \| eCee \| eeCe \| eeeC \| xx \| xxxx \| disabled*; 默认值: ) | 扩展信道配置。（例如 Ce = 扩展信道在控制信道之上，eC = 扩展信道在控制信道之下） |
| **channel.frequency** (*integer [0..4294967295]*; 默认值: ) | AP 运行的信道频率值（MHz）。如果留空，CAPsMAN 将自动确定占用最少的最佳频率。 |
| **channel.reselect-interval** (*time [00:00:00]*; *[00:00:00..00:00:00];* 默认值: ) | 选择占用最少频率的间隔，可以定义为随机间隔，例如 "30m..60m"。仅在 **channel.frequency** 留空时有效。 |
| **channel.save-selected** (*yes \| no*; 默认值: **no**) | 如果自动选择信道频率并使用 **channel.reselect-interval**，则保存最后选择的频率。 |
| **channel.secondary-frequency** (*integer [0..4294967295]*; 默认值: **auto**) | 指定用于 80+80MHz 配置的第二频率。将其设置为 **Disabled** 以禁用 80+80MHz 功能。 |
| **channel.skip-dfs-channels** (*yes \| no*; 默认值: **no**) | 如果 **channel.frequency** 留空，选择将跳过 DFS 信道 |
| **channel.tx-power** (*integer [-30..40]*; 默认值: ) | CAP 接口的 TX 功率（整个接口，不是单个链）以 dBm 为单位。不能设置为高于国家法规或接口允许的值。默认使用国家或接口允许的最大值。 |
| **channel.width** (; 默认值: ) | 以 MHz 为单位设置信道宽度。 |
| **comment** (*string*; 默认值: ) | 配置配置文件的简短描述 |
| **country** (*国家名称 \| no\_country\_set*; 默认值: **no\_country\_set**) | 限制可用的频段、频率和每个频率的最大发射功率。还指定 **scan-list** 的默认值。值 *no\_country\_set* 是符合 FCC 的信道集。 |
| **datapath** (*list*; 默认值: ) | 用户定义的取自数据路径名称的列表（`/caps-man/datapath`） |
| **datapath.bridge** (*list*; 默认值: ) | 特定接口应自动添加为端口的桥接 |
| **datapath.bridge-cost** (*integer [1..*200000000*]*; 默认值: ) | 添加为桥接端口时使用的桥接端口开销 |
| **datapath.bridge-horizon** (*integer [0..4294967295]*; 默认值: ) | 添加为桥接端口时使用的桥接水平 |
| **datapath.client-to-client-forwarding** (*yes \| no*; 默认值: **no**) | 控制是否允许连接到接口的无线客户端之间的客户端到客户端转发，在本地转发模式下，此功能由 CAP 执行；否则由 CAPsMAN 执行 |
| **datapath.interface-list** (; 默认值: ) |  |
| **datapath.l2mtu** (; 默认值: ) | 设置第 2 层 MTU 大小 |
| **datapath.local-forwarding** (*yes \| no*; 默认值: **no**) | 控制转发模式 |
| **datapath.mtu** (; 默认值: ) | 设置 MTU 大小 |
| **datapath.openflow-switch** (; 默认值: ) | OpenFlow 交换机端口（启用时）以添加接口 |
| **datapath.vlan-id** (*integer [1..4095]*; 默认值: ) | 如果 vlan-mode 启用 VLAN 标记，则分配给接口的 VLAN ID |
| **datapath.vlan-mode** (*use-service-tag \| use-tag*; 默认值: ) | 启用并指定要分配给接口的 VLAN 标签类型（导致所有接收到的数据都带有 VLAN 标签，并允许接口仅发送带有给定标签的数据） |
| **disconnect-timeout** (; 默认值: ) |  |
| **distance** (; 默认值: ) |  |
| **frame-lifetime** (; 默认值: ) |  |
| **guard-interval** (*any \| long*; 默认值: **any**) | 是否允许使用短保护间隔（请参阅 802.11n MCS 规范以了解这可能如何影响吞吐量）。“any”将根据数据速率使用短或长，“long”将仅使用长。 |
| **hide-ssid** (*yes \| no*; 默认值: ) | yes - AP 不在信标帧中包含 SSID，并且不回复具有广播 SSID 的探测请求。no - AP 在信标帧中包含 SSID，并回复具有广播 SSID 的探测请求。此属性仅在 AP 模式下有效。将其设置为 *yes* 可以将此网络从某些客户端软件显示的无线网络列表中移除。更改此设置不会提高无线网络的安全性，因为 SSID 包含在 AP 发送的其他帧中。 |
| **hw-protection-mode** (; 默认值: ) |  |
| **hw-retries** (; 默认值: ) |  |
| **installation** (*any \| indoor \| outdoor*; 默认值: **any**) |  |
| **keepalive-frames** (*enabled \| disabled*; 默认值: **enabled**) |  |
| **load-balancing-group** (*string*; 默认值: ) | 将接口标记到负载均衡组。对于客户端连接到此组中的接口，该接口应具有与组中所有其他接口相同或更少的已连接客户端数。在 CAP 范围大部分重叠的设置中很有用。 |
| **max-sta-count** (*integer [1..2007]*; 默认值: ) | 最大关联客户端数。 |
| **mode** (; 默认值: **ap**) | 设置操作模式。目前仅支持 ap。 |
| **multicast-helper** (*default \| disabled \| full*; 默认值: **default**) | 设置为 full 时，多播数据包将使用单播目标 MAC 地址发送，解决无线链路上的多播问题。此选项应仅在接入点上启用；客户端应配置为 **station-bridge** 模式。disabled - 禁用助手，并使用多播目标 MAC 地址发送多播数据包full - 在发送之前将所有多播数据包 MAC 地址更改为单播 MAC 地址default - 当前设置为 disabled 的默认选择。此值可能在将来版本中更改。 |
| **name** (*string*; 默认值: ) | 配置配置文件的描述性名称 |
| **rates** (; 默认值: ) | 用户定义的取自速率名称的列表（`/caps-man/rates`） |
| **rates.basic** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*; 默认值: ) |  |
| **rates.supported** (*1Mbps \| 2Mbps \| 5.5Mbps \| 6Mbps \| 9Mbps \| 11Mbps \| 12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps*; 默认值: ) |  |
| **rates.ht-basic-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值: **mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每个连接客户端必须支持的[调制和编码方案](https://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有关 MCS 规范，请参阅 802.11n。 |
| **rates.ht-supported-mcs** (*list of (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值: **mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此设备通告为支持的[调制和编码方案](https://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。有关 MCS 规范，请参阅 802.11n。 |
| **rates.vht-basic-mcs** (*none \| MCS 0-7