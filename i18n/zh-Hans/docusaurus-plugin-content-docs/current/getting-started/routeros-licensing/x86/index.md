# x86 许可

> 本文介绍 MikroTik RouterOS 的 x86 系统许可，涵盖许可证密钥获取、软件 ID 要求、系统先决条件，以及包括试用版、免费演示版、WISP 和控制器许可证的功能与定价在内的许可级别详情。

import WideTable from '@site/src/components/WideTable';

# x86 许可

## 许可基础

对于 x86 系统（基于 PC 的安装），必须获取许可证密钥。每个系统都有一个唯一标识符，称为 **软件 ID**，用于许可目的。

许可证密钥以字符块形式提供。您可以从 MikroTik 账户或购买后收到的电子邮件中复制该密钥，然后粘贴到路由器中。您可以直接将密钥粘贴到终端，或使用 WinBox 许可菜单中的 **粘贴密钥** 选项。许可证生效需要重启。

:::info
**x86 软件 ID** 绑定到存储设备（例如 NAND、SSD、HDD、NVMe）的 MBR。
:::

在购买许可证之前，请确认软件 ID 在重启后保持不变。

:::danger
如果底层存储或配置不稳定，软件 ID 可能会发生变化。例如，在以下情况下可能发生：

- 使用有缺陷或即将故障的存储设备（SSD、HDD、NVMe 等）。
- RAID 配置设置不正确或不持久。
- 不同启动之间使用了不同的存储控制器或适配器。

:::

### 系统要求

- **软件包版本：** RouterOS v6.34 或更新版本。
- **主机 CPU：** x86-64 架构（64 位）。
- **内存：** 512 MB 或更多。
- **磁盘：** 128 MB 或更多。
- **RouterOS v6：** 支持的最大硬盘大小为 16 GB。
- **RouterOS v7：** 最大内存和磁盘空间受 Linux 内核 5.6.3 限制，并取决于具体硬件。

所需最小内存取决于接口数量和 CPU 数量。使用以下公式计算近似值：

- **RouterOS v6：** `RAM = 128 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`
- **RouterOS v7：** `RAM = 512 + [ 8 × (CPU_COUNT) × (INTERFACE_COUNT - 1) ]`

## RouterOS 许可证密钥级别

许可信息可以从 CLI 系统控制台检索：

```text
[admin@MikroTik] > /system/license/print
    software-id: "ABCD-1234"
         nlevel: 6
       features:
[admin@MikroTik] >
```

也可以从等效的 [WinBox](../../../management-tools/winbox.md) 或 [WebFig](../../../management-tools/webfig.md) 菜单中查看。

x86 系统安装后，RouterOS 以 **试用模式** 运行，无任何限制。您有 24 小时的时间注册 **级别 1（免费演示版）** 许可证，或购买级别 4、5 或 6 的许可证并应用有效密钥。

```text
[admin@MikroTik] /system/license/print 
  software-id: TRPC-YYR2
   expires-in: 23h48m24s
```

各许可证级别之间的差异如下表所示：

<WideTable>

| **级别编号** | **0（试用模式）** | **1（免费演示版）** | **4（WISP）** | **5（WISP）** | **6（控制器）** |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **价格** | [无需密钥](https://www.mikrotik.com/download.html) | [免费（需注册）](https://mikrotik.com/client/) | $45 | $95 | $250 |
| **Wireless4 AP 模式（PtMP）** | 24 小时试用 | - | 是 | 是 | 是 |
| **Wireless6 AP 模式** | - | - | 是 | 是 | 是 |
| **PPPoE 隧道** | 24 小时试用 | 1 | 200 | 500 | 无限制 |
| **PPTP 隧道** | 24 小时试用 | 1 | 200 | 500 | 无限制 |
| **L2TP 隧道** | 24 小时试用 | 1 | 200 | 500 | 无限制 |
| **OVPN 隧道** | 24 小时试用 | 1 | 200 | 无限制 | 无限制 |
| **HotSpot 活跃用户** | 24 小时试用 | 1 | 200 | 500 | 无限制 |
| **User Manager 活跃会话** | 24 小时试用 | 1 | 20 | 50 | 无限制 |

</WideTable>

:::info
如果某项功能未列出，则不受许可证限制。
:::

:::note
级别 2 是旧版（2.8 之前）许可证格式的过渡许可证。这些许可证已不再提供。现有的级别 2 许可证将继续有效，但升级需要购买新许可证。级别 3 许可证仅用于无线站点（客户端/CPE）。*对于 x86 PC，级别 3 不可单独购买。*
:::

### 所有许可证

- 永不过期 — 运行中的已授权路由器可以无限期使用。
- 支持无限数量的接口。
- 每个许可证仅对单次安装有效。
- 包含无限次软件升级（例外：从 7.8 版本开始，演示版许可证不允许 RouterOS 版本升级）。

### 预付密钥

预付密钥是一种可以提前为 MikroTik 产品购买的许可证类型。它允许您在不立即将其分配给特定设备的情况下获取许可证。获取后，预付密钥可用于升级 CHR 实例，或使用目标软件 ID 转换为 x86 系统或 RouterBOARD 设备的许可证密钥。

## 如何购买 RouterOS 许可证密钥

1. 前往 [mikrotik.com](https://mikrotik.com) 并登录您的账户。
2. 导航至 **"购买 RouterOS 许可证密钥"** 部分。
3. 选择所需的许可证密钥级别。
4. 将密钥类型设置为 **"许可证密钥"**。
5. 在许可证密钥信息字段中，粘贴您设备的软件 ID。
6. 选择部署所需的任何可选密钥功能。
7. 点击 **"将密钥加入购物车"** 按钮。
8. 点击 **"前往结账"** 完成购买。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/purchase-prepaid-01.png)

## 审核并完成购买

仔细审核您的订单详情，然后使用 **信用卡**（CC）或 **PayPal** 进行付款。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/purchase-prepaid_02.png)

恭喜！您已成功购买 RouterOS 许可证密钥。

## 如何将预付密钥转换为 x86 的许可证密钥

1. **购买 RouterOS [预付密钥](./index.md#prepaid-key)。**

   - 登录您的 [mikrotik.com](https://mikrotik.com) 账户。
   - 如果您尚未购买 RouterOS 预付密钥，请购买。

2. **访问"从预付密钥生成密钥"部分。**

   - 在您的账户中导航至"从预付密钥生成密钥"部分。

3. **选择并转换预付密钥。**

   - 从列表中选择所需的预付密钥。
   - 输入您要授权的 x86 设备的 **软件 ID**，或您要升级许可证级别的路由器的 **软件 ID**。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/convert-prepaid_01.png)

1. **生成许可证密钥。**

   - 按下"生成"。
   - 将出现确认消息："成功将预付密钥转换为新许可证！"。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/convert-prepaid_02.png)

1. **应用许可证密钥。**

   - 复制生成的许可证密钥。
   - 将其粘贴到 x86 设备中以应用许可证。

您已成功将预付密钥转换为 x86 设备的许可证密钥。

## 替换密钥

替换密钥是 MikroTik 支持团队在 x86 存储设备故障或运行 RouterOS 的 x86 实例丢失许可证时签发的特殊许可证密钥。其价格为 $10，每个原始密钥只能签发一次。

在签发替换密钥之前，MikroTik 支持人员可能要求提供原始驱动器已故障的证明。在某些情况下，这包括将故障驱动器物理寄送至 MikroTik。

## 替换密钥申请

1. **登录并提交申请**
   - 登录您在 [mikrotik.com](https://mikrotik.com) 的账户。
   - 使用"[支持联系表单](https://help.mikrotik.com/servicedesk/servicedesk/)"提交申请，或直接发送电子邮件至 [support@mikrotik.com](mailto:support@mikrotik.com)。
   - 在申请中包含以下信息：
     - **清晰说明需要替换密钥的原因。**
     - **旧软件 ID 及其注册所在的账户。**

2. **等待确认并应用密钥**
   - 一旦 MikroTik 支持团队确认替换密钥已添加到您的账户，请登录并导航至 **"从替换密钥生成密钥"** 部分。
   - 继续执行激活操作。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/Replacement_license_1.png)

1. **选择许可证级别**
   - 选择您希望应用替换的许可证级别。

2. **输入新软件 ID**
   - 输入目标设备的 **新软件 ID**。

3. **完成购买**
   - 点击 **"将许可证替换添加到购物车"** 以进入结账并完成付款。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/Replacement_license_2.png)

1. **获取您的密钥**
   - 包含新许可证密钥的确认电子邮件将发送至您账户的注册电子邮件地址。
   - 新生成的密钥也可以在 **"搜索并查看所有密钥"** 部分中找到，位于 **"已购买 YYYY"** 文件夹下，其中 **"YYYY"** 代表当前年份。

:::warning
*每个原始密钥只能签发一个替换密钥。同一密钥不能使用两次替换密钥流程。如果需要第二次替换，则必须为 RouterOS 设备购买新密钥。*
:::

## 获取和管理许可证

### 我在哪里可以购买 RouterOS 许可证密钥？

要为 **x86 PC 安装** 购买许可证，您需要在[我们的网站](https://www.mikrotik.com/client)上注册[账户](https://www.mikrotik.com/client)，并使用账户门户中提供的 [购买 RouterOS 许可证密钥](#how-to-purchase-a-routeros-license-key) 选项。

### 我可以升级 x86 许可证级别吗？

要升级 x86 许可证级别，您必须以全价购买所需的许可证密钥。

### 如果我从其他渠道购买了密钥

如果您的许可证是通过第三方供应商购买的，请直接联系该供应商寻求支持，因为他们负责协助处理其销售的许可证。

### 如果我拥有许可证并希望将其转移到另一个账户

一旦 x86 许可证密钥被应用，它即与您的 MikroTik 账户绑定，无法转移到其他账户。唯一可以在账户之间转移的许可证类型是未使用的预付密钥。作为培训礼物收到的预付密钥不可转移。要转移已购买的预付密钥，请导航至 MikroTik 账户中 **ROUTEROS KEYS** 部分下的 **转移预付密钥**。

### 如果我的设备上的许可证丢失了

如果您的路由器上的许可证因任何原因丢失，请将路由器升级到最新的 RouterOS 版本，并使用您在 [mikrotik.com](https://mikrotik.com) 账户中的 **"申请许可证密钥"** 选项。提交申请时，请使用 RouterOS 中 `/system/license` 菜单下找到的软件 ID 和序列号。收到后，将许可证密钥应用到您的设备。如果申请功能无法使用，请联系 [support@mikrotik.com](mailto:support@mikrotik.com) 寻求帮助。

:::warning
*如果许可证丢失是由于非经销商在保修期内进行的维修造成的，您将需要以全价购买新的 RouterOS 许可证。*
:::

## 使用许可证

### 我可以格式化或重新刷写驱动器吗？

使用非 MikroTik 工具（如 `dd` 或 `fdisk`）格式化或重新镜像存储设备将销毁您的许可证。

请极度谨慎，并在尝试此操作前联系 MikroTik 支持。不建议执行此类操作，替换许可证申请可能会被拒绝。

要安全地重新安装 RouterOS，请使用官方 MikroTik 工具，如 **Netinstall**，或通过创建可启动安装介质（例如 USB 闪存驱动器）从磁盘镜像安装。

### 我可以在多少台计算机上使用该许可证？

RouterOS 许可证只能用于单个设备/系统。

在 x86 系统上，许可证绑定到 **软件 ID**，该 ID 绑定到存储设备（MBR）。这允许您将同一存储设备移动到另一台计算机而不会丢失许可证。但是，许可证不能转移到不同的存储设备。

格式化或覆盖存储设备将永久擦除许可证，需要购买新许可证。

:::danger
**重要提示：** 在移动或修改存储时，请谨慎执行所有操作。使用不同的存储控制器或适配器、修改 BIOS/UEFI 设置等更改可能会改变软件 ID 并导致许可证丢失。
:::

为遵循最佳实践，请在硬件更改前后生成并保存 `supout.rif` 文件。如果软件 ID 发生变化，可以将这些文件提供给 MikroTik 支持进行审查。

如果软件 ID 已更改，您可以申请替换密钥。

### 我可以临时将存储设备用于 RouterOS 以外的其他用途吗？

如上所述，不可以。

### 我可以将许可证转移到另一个存储设备（例如 SSD、HDD、NVMe）吗？

如果您当前的存储设备损坏或无法使用，可以通过申请替换密钥将许可证转移到新设备。

替换密钥的费用为 $10。

### 我必须将整个密钥输入到路由器中吗？

不需要，只需复制密钥并将其粘贴到 **系统** → **许可证** → **粘贴密钥** 中，然后确认重启即可。

![](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/x86/img/manual_x86_key_01.png)

或者，将密钥直接粘贴到 CLI 中，然后按 **Y** 重启。

### 我可以在驱动器上安装其他操作系统，然后再重新安装 RouterOS 吗？

不可以。如果您使用格式化、分区工具或任何其他修改 MBR 的工具，您将丢失许可证，并且需要获取新许可证。此过程并非免费（请参阅上文 [替换密钥](#replacement-key)）。

### 我的 RouterBOARD 丢失了 — 我可以将许可证转移到另一个系统吗？

MikroTik 硬件包含一个永久绑定到设备的嵌入式许可证。该许可证在任何情况下都不能转移到其他系统。此限制也适用于路由器运行期间应用的所有许可证升级。

### 从经销商处购买的许可证

您从其他供应商和经销商处购买的密钥不在您的账户中。您的 [mikrotik.com](https://mikrotik.com) 账户仅包含直接从 MikroTik 购买的许可证。

### 我没有使用该软件，可以终止我的许可证吗？

许可证是独立的密钥，MikroTik 无法远程控制您的设备。因此，无法验证许可证是否正在被积极使用。出于这个原因，MikroTik 无法终止任何已签发的许可证。

### 是否可以将 x86 许可证升级或转换为 CHR 许可证？

将 x86 或 RouterBOARD 许可证升级或转换为 CHR 许可证，反之亦然，是不可能的。必须为 CHR 单独购买许可证。

### 如果我在购买密钥时输入了错误的软件 ID 怎么办？

如果使用不正确的软件 ID 生成了许可证密钥（例如，输入 `1` 而不是 `I` 之类的笔误），可以在不联系支持人员的情况下更正密钥上的软件 ID。此功能允许修正软件 ID 的 1-2 个字符：

1. 登录您的 [mikrotik.com](https://mikrotik.com) 账户。
2. 导航至 **"搜索并查看所有密钥"**。
3. 打开购买年份的文件夹 — **"已购买 YYYY"**，其中 **"YYYY"** 代表当前年份。
4. 选择相关密钥并点击 **"编辑"**。
5. 点击 **"修复软件 ID"**。
6. 更正软件 ID 字段中的字符并保存。

## x86 安装

涵盖 RouterOS x86 系统要求和安装方法，包括 USB 和 Netinstall 部署。

[x86 安装指南](../../installation-and-upgrade/install/x86-installation)