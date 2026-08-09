# CHR：许可

> CHR 提供四个许可级别——Free、P1（永久-1）、P10（永久-10）和 P-Unlimited——付费选项均提供试用期。许可为永久性，与 CHR 系统 ID 绑定，并需通过 MikroTik 账户服务器定期续期。试用许可可在到期前升级，而已过期的实例

# CHR：许可

## 概述

云托管路由器（CHR）提供四个许可级别。许可是永久性的，即一次性购买即可无限期使用。如有需要，永久许可也可以转移到另一个 CHR 实例。
CHR 默认包含完整的 RouterOS 功能集。然而，与其他 RouterOS 版本相比，它采用了不同的许可模式。

### CHR 许可级别

CHR 是 RouterOS 的一个版本，专为作为虚拟机运行而设计。它有四个许可级别，以及一个 Trial（试用）选项，允许您免费测试任何付费许可级别 60 天。

所有付费许可级别均提供 60 天免费试用。要获取试用许可，您必须在 [MikroTik.com](https://mikrotik.com/) 上注册账户，因为所有 CHR 许可管理均通过 MikroTik 账户系统处理。

永久许可是终身许可——一次购买，无限期使用。如有需要，这些许可也可以转移到另一个 CHR 实例。

许可直接与 CHR 系统 ID 绑定。

运行中的 CHR 实例会定期连接到 MikroTik 账户服务器以续期其许可状态。系统会显示必须完成续期的截止时间。如果 CHR 实例无法在截止时间前续期其许可，它将表现得如同试用期已过，并且不再允许将 RouterOS 升级到更新版本。

要在运行 Free 许可级别的 CHR 实例上激活试用许可，您**必须**手动运行 `/system/license/renew` 命令，并将该 CHR 实例注册到您的 MikroTik.com 账户。

| 许可 | 速度限制 | 价格 | 描述 |
| :-- | :-- | :-- | :-- |
| Free | 1Mbit | 免费 | Free 许可级别允许 CHR 无限期运行，每个接口的上传限制为 1 Mbps。所有其他 RouterOS 功能均无限制可用。要开始使用，请下载磁盘镜像并将其部署为虚拟机或云实例。|
| P1（永久-1） | 1Gbit | $45 | P1（永久-1）允许 CHR 无限期运行。每个接口的上传限制为 1 Gbps。所有其他 RouterOS 功能均无限制可用。可以从 P1 升级到 P10 或 P-Unlimited。当以全价购买升级时，之前的许可将在您的 MikroTik 账户中重新可用。|
| P10（永久-10） | 10Gbit | $95 | P10（永久-10）允许 CHR 无限期运行。每个接口的上传限制为 10 Gbps。所有其他 RouterOS 功能均无限制可用。P10 可以升级到 P-Unlimited。当以全价购买升级时，之前的许可将在您的 MikroTik 账户中重新可用。|
| P-Unlimited | 无限制 | $250 | P-Unlimited（永久-无限制）允许 CHR 无限期运行。它是最高级别的许可，没有强制限制。|
| 60 天试用 | | 免费 | 除了 Free 许可之外，您还可以使用 60 天试用期来评估更高性能级别（P1、P10 或 P-Unlimited）。需要一个已注册的 [MikroTik.com](https://mikrotik.com) 账户。您可以从 CHR 实例请求试用许可。这会将实例的系统 ID 与您的 MikroTik 账户关联，并启用许可管理和购买。所有付费许可级别均可试用。试用期自激活之日起 60 天内有效。到期后，许可状态将变为 **"Limited upgrades"**（有限升级），这意味着无法再升级 RouterOS。**注意：** 如果您打算购买许可，请在试用期到期前完成购买。如果在到期后 2 个月内未进行购买，该 CHR 实例将从您的 MikroTik 账户中移除。在这种情况下，需要重新安装 CHR。要请求试用许可，请在 CHR 实例上运行以下命令：`/system license renew` 系统将提示您输入 MikroTik.com 账户用户名和密码。（*[敏感参数](../../configuration-management/list-of-menus-with-sensitive-parameters.md)*）。|

:::warning
如果您想将永久许可升级到更高级别，请先将现有许可转移到另一个 CHR 实例。这可以防止许可在升级过程中丢失。
:::

### 许可说明

您可以克隆或复制正在运行的 CHR 系统，但克隆的实例会保留原始的试用状态。这意味着无法通过创建副本来延长试用期。但是，每个系统仍然可以独立获得许可。

要开始新的试用期，请执行全新的 CHR 安装并重新配置 RouterOS。

## 系统 ID 与克隆注意事项

当从同一磁盘镜像部署多个 CHR 实例时，某些云提供商（例如 Linode）可能会为多台机器分配相同的系统 ID。
为防止这种情况，请在首次启动后、请求试用许可之前运行以下命令：`/system/license/generate-new-id`

:::warning
此命令只能在运行 Free 许可级别的 CHR 上使用。在应用试用或许可后请勿使用，因为它可能会阻止后续的许可更新。
:::

## 部署多个实例

要运行多个 CHR 实例：

1. 从 MikroTik 网站下载 CHR 磁盘镜像。
2. 为每个虚拟机创建镜像的单独副本。
3. 将每个副本作为独立的虚拟机部署在您的虚拟机管理程序或云平台中。

确保在**启动**或注册镜像**之前**创建副本。

## 永久许可要求

运行中的 CHR 实例必须定期连接到 MikroTik 账户服务器以续期其许可状态。系统会指示必须完成此操作的时间。

> **重要提示：** 如果 CHR 实例无法在截止时间前联系到账户服务器，它将表现得如同试用期已过。在此状态下，您将无法将 RouterOS 升级到更新版本或修改软件包（例如，启用或禁用它们）。

## IP/Cloud 要求

IP/Cloud 功能需要**付费的永久 CHR 许可**。

## 许可过期

当 CHR 实例未能在 "deadline-at" 时间之前通过联系 MikroTik 服务器续期其许可，或者 60 天试用期结束时，就会发生 CHR 许可过期。

当许可过期时，路由器将继续以相同的级别运行，但软件更新和软件包更改将被禁用。

**为过期的 CHR 实例获取许可：** 您必须使用 Prepaid key（预付密钥）。

如果过期的实例在一定时间内未连接到许可服务器，它们将自动从您的 MikroTik 账户中移除。

## 为 CHR 许可购买预付密钥

### 什么是预付密钥？

预付密钥是您为 MikroTik 产品（包括云托管路由器（CHR））预先购买的许可密钥。此密钥允许您购买许可而无需立即将其分配给特定设备。

一旦您拥有预付密钥，您就可以使用它来升级现有的 CHR 系统 ID，或通过提供设备的软件 ID 将其转换为完整的许可密钥。

### 购买预付密钥

按照以下步骤购买预付密钥：

1. 前往 [mikrotik.com](https://mikrotik.com/) 并登录您的账户。
2. 导航到 **Purchase a RouterOS License Key**（购买 RouterOS 许可密钥）部分。
3. 选择所需的许可级别。
4. 选择 **Prepaid key**（预付密钥）作为密钥类型。
5. 输入您要购买的预付密钥数量。
6. （可选）为您的密钥选择所需的任何附加功能。
7. 点击 **Place key in the cart**（将密钥加入购物车）。
8. 点击 **Proceed to checkout**（前往结账）以完成购买。

![预付密钥购买](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/purchase-prepaid_01.png)

### 完成购买

1. 查看您的订单详情。
2. 使用**信用卡**（CC）或 **PayPal** 完成付款。

![预付密钥购买完成](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/purchase-prepaid_02.png)

恭喜！您已成功购买预付密钥。

![预付密钥](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/prepaid_key_01.png)

## 注册 CHR 实例

当您首次设置云托管路由器（CHR）实例时，它会自动获得 Free 许可。要获取更高的许可级别，您必须将 CHR 实例注册到您的 MikroTik 账户。

此注册会将 CHR 系统 ID 与您的 MikroTik.com 账户关联，并为所选许可级别激活 60 天试用期。

### 启动试用许可

#### 使用 WinBox

1. 打开 WinBox 并连接到您的 CHR 实例。
2. 导航到 `/system/license` 并点击 **Renew License**（续期许可）。

![Free 到 Trial 升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_free_to_trial_01.png)
![Free 到 Trial 升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_free_to_trial_02.png)

1. 输入您的 MikroTik.com 账户凭据并选择所需的许可级别。

![Free 到 Trial 升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_free_to_trial_03.png)

1. 确认升级。

![Free 到 Trial 升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_free_to_trial_04_1.png)

#### 使用命令行界面（CLI）

1. 检查您当前的许可状态：

```
[admin@MikroTik] > /system/license/print
  system-id: HDlXorQ3f7L
      level: free
```

1. 使用您的账户凭据和所需级别运行续期命令：

```
[admin@MikroTik] > /system/license/renew
account: mymikrotikcomaccount
password: *********************
level: p1
  status: done
```

1. 验证升级是否成功：

```
[admin@MikroTik] > /system/license/print
         system-id: HDlXorQ3f7L        
             level: p1                 
  limited-upgrades: no                 
   next-renewal-at: 2026-06-11 10:55:29
       deadline-at: 2026-07-11 10:55:29
```

>输出确认您的许可已升级到 P1，并显示了下次续期日期和试用截止时间。

#### 验证 CHR 注册

1. 前往 [mikrotik.com/client](https://mikrotik.com/client/) 并使用您的 mikrotik.com 凭据登录。
2. 在 **CHR LICENCES**（CHR 许可）部分，选择 **All CHR keys**（所有 CHR 密钥）。
3. 将显示您的 CHR 实例列表及其对应的许可级别。

注册后，CHR 系统 ID 将出现在您 MikroTik.com 账户的 **All CHR keys**（所有 CHR 密钥）部分。

### 获取更高级别的试用

:::warning
无法在同一实例上升级试用许可级别。
:::

要试用更高级别的许可，请部署一个新的 CHR 实例，并在注册期间选择所需的试用许可级别。

## 将试用许可升级为付费许可

### 付款与许可升级

要将试用许可升级为付费许可：

1. 前往 [MikroTik 账户服务器](https://www.mikrotik.com/client)。
2. 在 **CHR LICENCES**（CHR 许可）部分，选择 **All CHR keys**（所有 CHR 密钥）。

![所有 CHR 密钥](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/payment01.png)

1. 将显示您的 CHR 实例列表及其对应的许可级别。

![试用转付费升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_trial_to_paid_02.png)

1. 点击要升级的实例旁边的 **Upgrade**（升级）。

2. 选择所需的许可级别（此级别可以与您当前的试用许可级别不同）。

![试用转付费升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/payment02.png)

1. 点击 **Upgrade**（升级）以确认。

### 使用预付密钥

如果您有**预付密钥**可用，您可以使用它们来支付 CHR 许可费用：

1. 点击 **Pay using Prepaid key**（使用预付密钥支付）。

![试用转付费升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/payment03.png)

1. 如果您没有预付密钥或不想使用它们，请点击 **Proceed to checkout**（前往结账）。

### 付款方式

您可以使用以下任一方式付款：

- 信用卡（CC）。
- PayPal。

![试用转付费升级](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/payment04.png)

## 升级永久许可级别

### 前提条件

在开始升级之前，请确保您具备：

- 有效的 MikroTik.com 账户（用户名和密码）。
- 已购买您想要获取的所需许可级别的预付密钥。

:::warning
如果您想将永久许可升级到更高级别，请先将现有许可转移到另一个 CHR 实例。这可以防止许可在升级过程中丢失。
:::

您可以将云托管路由器（CHR）的**永久**许可升级到更高级别。支持以下升级：

- **P1 → P10** 或 **P1 → P-Unlimited**。
- **P10 → P-Unlimited**。

当您以全价购买升级时，您之前的许可仍可在您的账户上使用。

:::info
P-Unlimited（永久-无限制）许可是可用的最高级别。它允许 CHR 无限期运行，且没有强制限制。
:::

### 升级付费的永久 CHR 许可级别

1. 登录您的 MikroTik 账户并导航到 **All CHR keys**（所有 CHR 密钥）。
2. 选择您要升级的 CHR 实例。
3. 点击 **Upgrade**（升级）。

    ![许可升级级别](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_upgade_level_01.png)

4. 选择所需的许可级别（P10 或 P-Unlimited）并点击 **Upgrade**（升级）。

    ![许可升级级别选择目标](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_upgrade02.png)

5. 选择付款选项：

- **Pay using Prepaid key**（使用预付密钥支付）——如果您有可用的预付密钥

    ![许可升级级别](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_upgade_level_03.png)

- **Proceed to checkout**（前往结账）——如果您希望通过其他方式付款

    ![许可升级级别](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_upgade_level_04.png)

1. 选择您的付款方式：

- 信用卡（CC）。
- PayPal。
    ![许可升级级别](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/license_upgade_level_05.png)

1. 完成付款流程。

您的 CHR 许可将升级到所选级别，并且您之前的许可将保留在您的账户上以供将来使用。

:::warning
您可以升级到除 *p-unlimited* 之外的任何许可级别。该级别代表可用的最高级别，无法进一步升级。
:::

## 许可转移

每个云托管路由器（CHR）安装都直接与您的 MikroTik 账户绑定。您可以将永久许可转移到另一个 CHR 实例，前提是两个实例都在**同一**账户下注册。

### 转移限制

| 许可类型 | 可转移？ | 备注 |
|---|---|---|
| 永久许可 | 是 | 仅限转移到**同一**账户下的另一个 CHR 实例 |
| 预付密钥（已购买） | 是 | 可通过"Transfer prepaid keys"（转移预付密钥）转移到不同的账户 |
| 预付密钥（来自培训） | 否 | 这些密钥不可转移 |

:::warning
无法将永久许可转移到已过期的实例。要为过期的 CHR 实例获取许可，必须使用预付密钥。
:::

:::info
从中转移出许可的实例将保留相同的许可级别，但状态为 **Limited upgrades**（有限升级）（已过期）。它将继续以该许可级别运行，但 RouterOS 升级将不再可用。
:::

### 前提条件：所需的 CHR 实例

在转移永久许可之前，您必须拥有：

- 带有您要转移的许可的原始 CHR 实例。
- 在**同一** MikroTik 账户下注册的目标 CHR 实例。

如果您没有第二个 CHR 实例，请先创建一个，然后将其添加到您的账户中。

### 转移许可

按照以下步骤转移您的许可：

1. **注册新实例**

  在您的旧 CHR 注册的同一 MikroTik 账户下注册新的 CHR 实例。使用 CLI 命令：

   ```
   /system/license/renew
   ```

1. **验证两个实例都出现在您的账户中**

  确认新旧 CHR 机器都可见于您 MikroTik 账户的 **All CHR keys**（所有 CHR 密钥）部分。

2. **发起转移**

- 前往您账户的 **All CHR keys**（所有 CHR 密钥）部分。

    ![转移按钮位置](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_transfer01.png)

  - 点击您要转移的系统 ID 旁边的 **Transfer**（转移）按钮。

1. **选择目标实例**

  从列表中选择您要将许可转移到的系统 ID。

   ![选择目标实例](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_transfer02.png)

2. **确认转移**

  点击 **Transfer subscription**（转移订阅）以完成该过程。

   ![确认转移](https://manual.mikrotik.com/docs/getting-started/routeros-licensing/chr/img/chr_transfer03.png)

### 转移错误排查

如果您收到错误：
:::danger
*"This key is not eligible for transfer as there is no other valid CHR key that could be upgraded to the license level of this key."*
（此密钥不符合转移条件，因为没有其他有效的 CHR 密钥可以升级到此密钥的许可级别。）
:::
这意味着您没有处于 Trial 模式的 CHR 实例来接收该许可。

:::tip
**解决方案：** 创建一个新的 CHR 实例并将其添加到您的账户中。添加后，您可以将现有许可转移到新实例。
:::

## 许可续期

CHR 许可需要定期与 MikroTik 许可服务器通信以维持许可有效性。

在 **System > License**（系统 > 许可）菜单中，路由器显示两个重要的时间戳：

- **next-renewal-at** — 路由器下次尝试联系 MikroTik 许可服务器的时间。
- **deadline-at** — 必须与许可服务器成功通信的最晚时间。

CHR 实例与许可服务器通信的地址为：

`licence.mikrotik.com`

### 续期流程

- 在 **next-renewal-at** 时间过后，路由器每小时尝试一次许可续期。
- 续期尝试将持续进行，直到服务器成功响应。

### 许可过期

如果路由器无法在 **deadline-at** 时间之前联系到许可服务器：

- 许可进入过期状态。
- 不再允许 RouterOS 升级。
- 不再允许软件包更改（启用/禁用/安装/移除）。
- 路由器继续以当前的许可级别运行。

### 成功续期

与许可服务器成功通信后：

- **next-renewal-at** 时间戳被更新。
- **deadline-at** 时间戳被更新。