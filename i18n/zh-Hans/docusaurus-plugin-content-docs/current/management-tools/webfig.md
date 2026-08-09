# WebFig

> WebFig 是一款基于 Web 的 RouterOS 工具，无需额外软件即可实现监控、配置和故障排除。它支持带证书管理（包括通配符证书）的 HTTPS，并通过 SSL/TLS 为路由器配置提供安全访问。

# WebFig

## 简介

WebFig 是一款基于 Web 的 RouterOS 管理工具，允许您配置、监控和排查路由器故障。它是 WinBox 的替代方案，提供类似的布局，并可访问几乎所有 RouterOS 功能。

作为一款跨平台工具，WebFig 可从任何装有 Web 浏览器的设备管理路由器，无需安装特定平台的软件。

WebFig 支持三项主要功能：

- **配置** - 查看和修改当前路由器配置。
- **监控** - 监控路由器状态、路由信息、接口统计、日志及其他运行数据。
- **故障排除** - 访问并使用 RouterOS 内置诊断工具，如 Ping、Traceroute、Packet Sniffer、Traffic Generator 等。

## 连接路由器

如 [首次配置](../getting-started/first-time-configuration.md) 部分所述，设备默认使用用户名 **admin** 访问，密码为空或使用设备标签上提供的默认密码（取决于型号）。打开 Web 浏览器，在地址栏中输入设备 IP 地址；默认地址为 `192.168.88.1`。请确保管理设备配置了同一子网内的 IP 地址（例如 `192.168.88.2`），否则将无法建立三层连通性。

只需打开 Web 浏览器，在搜索栏中输入设备 IP 地址，默认为 **192.168.88.1**。请确保您的设备具有同一网络的 IP 地址，例如 192.168.88.2，否则三层通信将无法工作。

![](https://manual.mikrotik.com/docs/management-tools/img/webfig_01.png)

## 启用 HTTPS

WebFig 通常仅在本地网络中使用：默认情况下，防火墙会阻止 WAN 端口上的路由器 Web 服务，您通过路由器的 LAN 地址（例如 `192.168.88.1`）访问路由器。启用 HTTPS 可加密此管理流量，确保凭据和配置不会以明文形式在 LAN 中传输。

使用哪种证书取决于您访问路由器的方式：

- **通过 LAN IP 地址或内部主机名（通常情况）** — 使用在路由器上生成的自签名证书。公共证书颁发机构无法为 `192.168.88.1` 等私有地址签发证书，因此这是默认方法。
- **通过真实的公共域名** — 您可以使用 Let's Encrypt 提供的公共可信证书，无需分发 CA 即可避免浏览器警告。这仅在您实际使用该域名打开 WebFig 时有效，因此主要适用于通过公共名称而非 LAN IP 管理的路由器（如下所述）。

### 使用自签名证书

自签名证书可立即加密连接。浏览器在首次使用时不会信任该证书，但您可以通过导出路由器的根 CA 并将其导入用于管理路由器的计算机的受信任存储中来消除警告。

:::tip
WebFig 支持通配符证书。您可以通过在 common-name 属性中指定通配符来生成，例如 `common-name=*.mikrotik.com`。
:::

要生成自己的证书并启用 HTTPS 访问，您必须配置以下内容：

#### 在路由器上创建自己的根 CA 并签名

```ros
[admin@MikroTik] > certificate add name=local-cert common-name=local-cert key-usage=key-cert-sign,crl-sign 
[admin@MikroTik] > /certificate/sign local-cert 
  progress: done
```

:::warning
如果您已有证书颁发机构或使用外部服务签署证书，请在外部创建并签署证书，然后将其导入路由器。导入证书时，请确保将其标记为受信任。
:::

#### 为 WebFig 创建证书（终端实体证书）

```ros
[admin@MikroTik] > certificate add name=WebFig common-name=192.168.88.1
[admin@MikroTik] > certificate sign WebFig 
  progress: done
```

示例证书列表：

```ros
[admin@MikroTik] > /certificate/print
Flags: K - private-key; A - authority; T - trusted
Columns:NAME        COMMON-NAME     FINGERPRINT                                                     
0  KAT  local-cert  local-cert      9b6363d033c4b2e6893c340675cfb8d1e330977526dba347a440fabffd983c5d
1  KAT  WebFig      192.168.88.1    9f84ac2979bea65dccd02652056e5559bcdf866f8da5f924139d99453402bd02
```

#### 启用 HTTPS 服务并分配证书

```ros
[admin@MikroTik] > ip service
set www-ssl certificate=WebFig disabled=no
```

您现在可以通过 **`https://192.168.88.1`** 访问 WebFig。

:::warning
大多数 Web 浏览器默认不信任自签名证书，因此首次连接时您需要接受警告或手动信任该证书。或者，导出根 CA 证书并将其导入操作系统或浏览器的信任存储中。请注意，浏览器维护自己的信任存储，可能与操作系统的不同——在操作系统层面信任证书可能不会影响浏览器。
:::

### 使用公共可信证书（Let's Encrypt）

如果您通过真实的公共域名而非 LAN IP 访问路由器，则可以使用 [Let's Encrypt](https://letsencrypt.org/) 提供的浏览器可信证书，无需分发根 CA。RouterOS 内置了 [ACME 客户端](/docs/authentication-authorization-accounting/certificates#acme-client) 用于此目的。

在选择此选项之前，请注意它与纯 LAN 设置的交互方式：

- 公共 CA 不会为私有 IP 地址签发证书，因此这**不会**消除您在 `https://192.168.88.1` 打开 WebFig 时看到的警告。
- 证书仅对其域名有效，因此您必须通过该名称访问 WebFig。要使该名称在 LAN 内解析到路由器，您通常需要一条本地（split-horizon）DNS 记录将其指向 LAN 地址。
- DNS-01 挑战——用于 [IP Cloud](/docs/network-management/cloud#ddns) `<id>.sn.mynetname.net` 名称——无需入站 WAN 端口，因此即使防火墙阻止从 WAN 访问 WebFig，它仍然可以工作。

为路由器的 IP Cloud DDNS 名称请求证书：

```ros
/ip/cloud/set ddns-enabled=yes
/certificate/add-acme domain-names=[/ip/cloud/get dns-name]
```

或为您自己的域名：

```ros
/certificate/add-acme domain-names=router.example.com
```

签发的证书以域名命名，并在 `/certificate/print` 中显示 `a`（acme-manage）标志。将其分配给 `www-ssl` 服务，然后通过该域名打开 WebFig：

```ros
/ip/service/set www-ssl certificate=router.example.com disabled=no
```

证书将在其有效期过去 80% 后自动续期。

## 终端

WebFig 中的 **终端**（命令行界面，CLI）位于右上角。它提供与 WinBox 界面中 New Terminal 相同的功能。

![WebFig 终端](https://manual.mikrotik.com/docs/management-tools/img/webfig-terminal_01.png)

## 皮肤

WebFig **设计皮肤** 是一种用于自定义界面外观以提升可用性的工具。它不是安全功能。具有足够权限的用户仍可通过其他方式（包括直接 CLI 访问）访问所有可用的配置选项。

### 设计皮肤

如果用户具有足够的权限（用户组启用了 `policy` 和 `sensitive` 策略），则 **设计皮肤** 按钮可用。启用此选项将打开界面自定义工具。

要限制对 **设计皮肤** 菜单的访问，请在用户组配置中禁用 `policy` 和 `sensitive` 权限。

**可用操作包括：**

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-design-skin_01.png)

- **隐藏菜单** - 隐藏菜单及其所有子菜单。
- **隐藏子菜单** - 隐藏特定子菜单。
- **隐藏选项卡** - 在多选项卡视图中隐藏单个选项卡。
- **重命名菜单和项目** - 更改菜单标签，例如用于本地化或清晰性。
- **为项目添加注释** - 在详细视图中添加注释。
- **将项目设为只读** - 出于安全考虑，阻止编辑所选字段。
- **隐藏标志** - 在列表视图和详细视图中隐藏标志。

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-design-skin_02.png)

- **添加字段限制** - 限制详细视图中的允许值：
  - **数字区间 (..)** - 定义允许的范围，例如数字字段（如 **MTU**）的 `1..10`。
  - **字段前缀限制** - 限制基于文本字段的允许前缀。尾随 `$` 强制执行精确前缀匹配。例如，`station$` 将值限制为仅 **station**。

  ![](https://manual.mikrotik.com/docs/management-tools/img/webfig-design-skin_03.png)

- **添加选项卡** - 在字段前插入带标签的分节符。
- **添加分隔符** - 在字段前插入水平分隔线。

:::note
数字区间不能超出 RouterOS 为给定字段定义的限制。
:::

:::note
集合字段表示可选项的集合（复选框组），例如用户组策略或 RADIUS 服务设置。
:::

:::note
应用于组合框字段的限制也会限制可用的下拉选项。
:::

### 皮肤设计示例

要限制用户使用特定服务，请在 RADIUS Service 字段中添加限制。

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-01.webp)

生成的配置将仅允许 **Limit** 字段中指定的服务。

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-02.webp)

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-03.webp)

### 自定义皮肤

可用于皮肤 `*.json` 文件的 **Status page** 结构示例可在此处获取：[status_main_example.json](pathname:///assets/297795616_status_main_example.json)

状态内容遵循以下结构：
`{"Status": {"Status": {}}}`

状态记录按顺序显示，例如：

```json
"7": {
  "alias": (记录路径),
  "note": (可选；显示在记录下方的自由格式文本),
  "name": (可选；记录的替代名称),
  "tab": (可选；此记录及后续记录所属的选项卡名称),
  "separator": 1 (可选；是否在此记录上方放置分隔线)
},
```

**路径（别名）结构**

别名路径（例如：**`"IP:Firewall:Filter Rules:*17:Statistics:Packet Rate Graph"`** 以及对应的 URL：**`router_IP/WebFig/#IP:Firewall.Filter_Rules.17`**）由冒号分隔的组件组成：

- **组**（如有）→ `IP:`
- **服务或名称** → `Firewall:`
- **容器或选项卡名称** → `Filter Rules:`
- **星号 (\*) 和对象 ID** → 取自所打开项目的 URL（例如 `17`）
- **选项卡名称**（如适用）→ `Statistics`
- **字段名称** → `Packet Rate Graph`

![](https://manual.mikrotik.com/docs/management-tools/img/webfig-design-skin_04.png)

### 使用皮肤

要应用皮肤，请将其分配给用户组。分配后，该组中的所有用户在登录 WebFig 或 WinBox 时将自动使用所选皮肤。

```ros
/user/group/set your_group_name skin=your_skin
```

要在另一台路由器上使用皮肤，请将皮肤文件复制到目标设备的 skins 目录中。复制后，在该路由器上将皮肤分配给用户组以启用它。