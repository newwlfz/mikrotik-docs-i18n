# MikroTik 硬件授权

> 运行 RouterOS 的 MikroTik 硬件路由器预装了授权，这些授权决定了隧道限制和用户会话等功能特性。授权级别从试用模式到无限制功能不等，价格随级别不同而变化。用户可以通过 CLI 或管理工具查看授权，并通过预付费密钥或绑定设备 ID 的直接购买方式进行升级。

import WideTable from '@site/src/components/WideTable';

# MikroTik 硬件授权

## 授权基础

运行 RouterOS 的 MikroTik 硬件路由器预装了授权。如果您已购买基于 RouterOS 的设备，则无需额外操作。

## RouterOS 授权密钥级别

授权信息可以通过 CLI 系统控制台获取：

```text
[admin@MikroTik] > /system/license/print
    software-id: "ABCD-1234"
         nlevel: 6
       features:
[admin@MikroTik] >
```

相同的信息也可以在 [WinBox](../../../management-tools/winbox.md) 或 [WebFig](../../../management-tools/webfig.md) 中查看。

```text
[admin@MikroTik] /system/license/print 
  software-id: TRPC-YYR2
   expires-in: 23h48m24s
```

各授权级别之间的差异如下表所示：

:::info
Level 2 是从旧版（2.8 之前）授权格式过渡而来的临时授权。这些授权已不再提供。现有的 Level 2 授权将继续正常运行，但升级需要购买新的授权。Level 3 授权仅用于无线站点（客户端/CPE）用途。
:::

<WideTable>

| **级别编号** | **0（试用模式）** | **1（免费演示）** | **3（WISP CPE）** | **4（WISP）** | **5（WISP）** | **6（控制器）** |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **价格** | [无需密钥](https://www.mikrotik.com/download.html) | [免费（需注册）](https://mikrotik.com/client/) | 不对外销售 | $45 | $95 | $250 |
| **Wireless4 AP 模式（PtMP）** | 24小时试用 | - | 否 | 是 | 是 | 是 |
| **Wireless6 AP 模式** | - | - | 是 | 是 | 是 | 是 |
| **PPPoE 隧道** | 24小时试用 | 1 | 200 | 200 | 500 | 无限制 |
| **PPTP 隧道** | 24小时试用 | 1 | 200 | 200 | 500 | 无限制 |
| **L2TP 隧道** | 24小时试用 | 1 | 200 | 200 | 500 | 无限制 |
| **OVPN 隧道** | 24小时试用 | 1 | 200 | 200 | 无限制 | 无限制 |
| **HotSpot 活跃用户** | 24小时试用 | 1 | 1 | 200 | 500 | 无限制 |
| **User Manager 活跃会话** | 24小时试用 | 1 | 10 | 20 | 50 | 无限制 |

</WideTable>

:::info
如果某项功能未在表中列出，则不受授权限制。
:::

:::info
**RouterBOARD 软件 ID** 与设备存储绑定。
:::

### 所有授权

- 永不过期 — 运行中的已授权路由器可以无限期使用。
- 支持无限数量的接口。
- 每个授权仅对单个安装有效。
- 包含无限次软件升级。

:::warning
**wifi-qcom** 驱动支持 PTMP 操作，不受授权级别限制。**Mode: AP** 在所有 **wifi-qcom** 设备上均可使用，支持多个客户端站点的连接。
:::

## 升级设备授权级别

如果您需要升级设备授权级别，必须购买更高级别的授权，可以是 [预付费密钥](#prepaid-key) 或直接购买绑定设备 **软件 ID** 的 [RouterOS 授权](#how-to-purchase-a-routeros-license-key)。

授权密钥以字符块形式提供。您可以从 MikroTik 账户或购买后收到的电子邮件中复制，然后粘贴到路由器中。您可以将密钥直接粘贴到终端中，或使用 WinBox 授权菜单中的 **Paste Key** 选项。授权生效需要重启设备。

### 预付费密钥

预付费密钥是一种可以提前为 MikroTik 产品购买的授权类型。它允许您在不立即分配给特定设备的情况下获取授权。获得预付费密钥后，它可以用于升级 CHR 实例，或使用目标软件 ID 转换为 x86 系统或 RouterBOARD 设备的授权密钥。

## 如何购买 RouterOS 授权密钥

1. 访问 [mikrotik.com](https://mikrotik.com) 并登录您的账户。
2. 导航至 **"Purchase a RouterOS License Key"** 部分。
3. 选择所需的授权密钥级别。
4. 将密钥类型设置为 **"License key"**。
5. 在授权密钥信息字段中，粘贴您设备的软件 ID。
6. 选择部署所需的任何可选密钥功能。
7. 点击 **"Place key in the cart"** 按钮。
8. 点击 **"Proceed to checkout"** 完成购买。

![购买 RouterOS 授权密钥](../x86/img/purchase-prepaid-01.png)

## 审核并完成购买

仔细审核您的订单详情，然后使用 **信用卡**（CC）或 **PayPal** 完成付款。

![购买 RouterOS 授权密钥](../x86/img/purchase-prepaid_02.png)

恭喜！您已成功购买 RouterOS 授权密钥。

## 自定义无线信道（仅适用于 Atheros 92xx 设备）

高级信道功能为无线接口配置提供了更多扩展能力：

- **扩展扫描列表：** 同时覆盖多个频段和信道宽度，实现全面的无线接口配置。
- **精确频率自定义：** 支持非标准信道中心频率（以 kHz 精度指定），适用于兼容硬件。
- **灵活的信道宽度：** 允许在硬件支持的情况下配置非标准信道宽度（以 kHz 精度指定）。

## 如何将预付费密钥转换为 RouterOS 授权密钥

1. **购买 RouterOS [预付费密钥](#prepaid-key)。**

   - 登录您的 [mikrotik.com](https://mikrotik.com) 账户。
   - 如果尚未购买，请购买 RouterOS 预付费密钥。

2. **访问"Make a Key from Prepaid Key"部分。**

   - 在您的账户中导航至"Make a key from prepaid key"部分。

3. **选择并转换预付费密钥。**

   - 从列表中选择所需的预付费密钥。
   - 输入您要升级授权级别的路由器的**软件 ID**。

![](../x86/img/convert-prepaid_01.png)

1. **生成授权密钥。**

   - 点击"Generate"。
   - 将出现确认消息："Successfully converted prepaid key to a new licence!"。

![](../x86/img/convert-prepaid_02.png)

1. **应用授权密钥。**

   - 复制生成的授权密钥。
   - 将其粘贴到设备中以应用授权。

您已成功将预付费密钥转换为路由器的授权密钥。

## 获取和管理授权

### 我在哪里可以购买 RouterOS 授权密钥？

所有 MikroTik 硬件设备均包含预装的 RouterOS 授权。

### 如果设备上的授权丢失

如果您的路由器因任何原因丢失了授权，请将路由器升级到最新的可用 RouterOS 版本，并使用 [mikrotik.com](https://mikrotik.com) 账户中的 **"Request license key"** 选项。提交请求时，请使用 RouterOS 中 `/system/license` 菜单下找到的软件 ID 和序列号。收到授权密钥后，将其应用到您的设备。如果请求功能无法使用，请联系 [support@mikrotik.com](mailto:support@mikrotik.com) 寻求帮助。

### 我的路由器丢失了授权，可以申请替换密钥吗？

不可以，替换密钥仅适用于 x86 系统。

:::warning
*如果授权丢失是由于非经销商在保修期内进行的维修造成的，您将需要按全价购买新的 RouterOS 授权。*
:::

## 使用授权

### 我可以转让 MikroTik 硬件授权吗？

MikroTik 硬件包含嵌入式授权，该授权永久绑定到设备。在任何情况下，此授权都不能转让给其他系统。此限制同样适用于路由器运行期间应用的所有授权升级。

### 是否可以将路由器授权升级或转让给 x86 系统或 CHR 授权？

设备授权不可转让。

## 相关指南

### x86 安装

涵盖 RouterOS x86 系统要求和安装方法，包括 USB 和 Netinstall 部署。

[x86 安装指南](../../installation-and-upgrade/install/x86-installation)