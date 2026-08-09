# 设备模式

> 设备模式功能用于限制路由器访问并限制配置选项以增强安全性，可根据设备类型和 RouterOS 版本选择高级、家庭、基础或 ros 模式。更改需要通过断电或按键进行物理确认，并限制更新尝试次数以防止未经授权的模式更改。

# 设备模式

## 描述

**设备模式**是一项功能，用于对设备设置特定限制，或限制对特定配置选项的访问。它有助于保护您的路由器和网络免受攻击者的侵害，这些攻击者可能未经授权访问并将其用作攻击其他网络的网关。

可用的设备模式为 *advanced*（高级）、*home*（家庭）、*basic*（基础）和 *ros*。设备模式配置在路由器上出厂预装（适用于 MikroTik RouterOS v7.17 或更高版本的设备）。*advanced*（以前称为 enterprise）模式适用于 CCR 和 1100 系列设备，*home* 模式适用于家用路由器，*basic* 模式适用于任何其他类型的设备。对于运行 RouterOS 7.17 之前版本的设备，所有设备均使用 *advanced/enterprise* 模式。

```ros
[admin@MikroTik] > /system/device-mode/print 
                 mode: advanced     
     allowed-versions: 7.13+,6.49.8+
              flagged: no           
     flagging-enabled: yes          
            scheduler: yes          
                socks: yes          
                fetch: yes          
                 pptp: yes          
                 l2tp: yes          
       bandwidth-test: yes          
          traffic-gen: no           
              sniffer: yes          
                ipsec: yes          
                romon: yes          
                proxy: yes          
              hotspot: yes          
                  smb: yes          
                email: yes          
             zerotier: yes          
            container: no           
  install-any-version: no           
           partitions: no           
          routerboard: yes          
        attempt-count: 0   
```

设备模式可由授权的 RouterOS 用户更改，但更改时需要物理访问设备。更改设备模式后，您需要按下设备本身的按钮或执行“冷重启”（即拔掉电源）来确认更改。无论采用何种确认方式，一旦更改被确认，**设备将重新启动**！

## 更改设备模式

```ros
[admin@MikroTik] > /system/device-mode/update mode=home 
  update: please activate by turning power off or pressing reset or mode button 
          in 5m00s
-- [Q quit|D dump|C-z pause]
```

如果在指定时间内未执行断电或按钮按下操作，则模式更改将被取消。如果同时运行另一个 update 命令，则两者都将被取消。

:::danger
有若干 EOL（生命周期结束）产品不支持通过按下重置按钮来“确认”模式更改。这些路由器只能通过断电重启来确认模式更改。
:::

为了防止攻击者静默访问您的路由器、通过脚本滥用它并试图等待您重启路由器，而您甚至不知道在重启时正在接受入侵者请求的更改，您只能“更新”模式三次。有一个计数器会计算尝试更新的次数，并且不允许超过此限制。只有当管理员在模式设置更新尝试时看到此类警告并执行断电重启或按下按钮时，此计数器才会重置（与接受任何更新时的操作相同）。

## 使用 Netinstall 或 FlashFig 更改设备模式设置

从 RouterOS 7.22 开始，可以配置 **device-mode**、**protected-routerboot** 和其他设置。

有关更多信息，请参阅 [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) 和 [FlashFig](../management-tools/flashfig.md) 文档。

## 启用设备模式功能

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```

在 /**system/device-mode** 菜单中可使用以下命令：

| 属性 | 描述 |
| :-- | :-- |
| get | 返回一个值，您可以将其分配给变量或打印在屏幕上。 |
| print | 显示活动模式及其属性。 |
| update | 将更改应用于指定属性，请参见下文。 |

## 可用的设备模式

有四种设备模式可供配置（mode=advanced 是默认模式），每种模式都有一组在使用时不允许启用的功能子集。请注意，没有任何模式启用了所有功能。即使您启用了“advanced”模式，某些功能也需要单独启用。ROSE 设备模式与 advanced 模式非常相似，但它是为 RDS 及类似设备设计的，这些设备具有更广泛的磁盘使用选项，因此支持从出厂时就安装容器。有关每个选项含义的更多详细信息，请参阅“功能说明”部分。因此，根据下表可以看出，“traffic-gen、container、partitions、routerboard”功能始终处于禁用状态，除非由管理员用户专门启用。

| **功能 / 属性** | **Home** | **Basic** | **Advanced** | **ROSE** |
| :-- | :-- | :-- | :-- | :-- |
| **带宽测试** (/tool/bandwidth-test) | 否 | 否 | 是 | 是 |
| **容器** (/container) | 否 | 否 | 否 | 是 |
| **电子邮件** (/tool/e-mail) | 否 | 是 | 是 | 是 |
| **Fetch** (/tool/fetch) | 否 | 是 | 是 | 是 |
| **热点** (/ip/hotspot) | 否 | 否 | 是 | 是 |
| **安装任意版本** (`install-any-version`) | 否 | 否 | 否 | 否 |
| **IPsec** (/ip/ipsec) | 是 | 是 | 是 | 是 |
| **L2TP** (/interface/l2tp) | 是 | 是 | 是 | 是 |
| **分区** (/`partitions`) | 否 | 否 | 否 | 否 |
| **PPTP** (/interface/pptp) | 是 | 是 | 是 | 是 |
| **代理** (/ip/proxy) | 否 | 否 | 是 | 是 |
| **RoMon** (/tool/romon) | 否 | 是 | 是 | 是 |
| **Routerboard 设置** (/system/routerboard) | 否 | 否 | 否 | 否 |
| **调度器** (`scheduler`) | 否 | 是 | 是 | 是 |
| **SMB** (/ip/smb) | 是 | 是 | 是 | 是 |
| **嗅探器** (/tool/sniffer) | 否 | 是 | 是 | 是 |
| **SOCKS 代理** (/ip/socks) | 否 | 否 | 是 | 是 |
| **流量生成器** (/tool/traffic-gen) | 否 | 否 | 否 | 否 |
| **ZeroTier** (`zerotier`) | 否 | 否 | 是 | 是 |

## 可用属性列表

| 属性 | 描述 |
| :-- | :-- |
| **scheduler, socks, fetch, pptp, l2tp, bandwidth-test, traffic-gen, sniffer, ipsec, romon, proxy, hotspot, smb, email, zerotier, container, install-any-version****, partitions, routerboard** (*yes \| no*) | 可通过 **device-mode** 选项控制的功能列表。有关每个选项含义的更多详细信息，请参阅“功能说明”部分。 |
| **activation-timeout** (默认值: **5m**); | 重置按钮或断电激活超时时间可设置在 00:00:10 .. 1d00:00:00 范围内。如果在此时间间隔内未按下重置按钮（或未执行冷重启），则更新将被取消。 |
| **flagging-enabled** (*yes \| no*; 默认值: **yes**) | 设备将执行配置分析，如果发现可疑代码的痕迹，将触发 flagged 模式，设置 **flagged=yes**，并启用 **flagged=yes** 中描述的 restrictions。请参阅“[Flagged 状态](./device-mode.md#flagged-status)”段落。 |
| **flagged** (*yes \| no*; 默认值: **no**) | RouterOS 采用多种机制来检测其系统文件是否被篡改。如果系统检测到对 RouterOS 的未经授权访问，则“flagged”状态设置为 yes。如果“flagged”设置为 yes，为了您的安全，将实施某些限制。有关更多信息，请参阅下文章节。 |
| **mode:** (basic, home, advanced, ros; 默认值: **advanced**); | 允许从可用模式中选择将限制设备功能的模式。默认情况下，**advanced** 模式允许除 **traffic-gen、container、partitions、install-any-version、routerboard** 之外的所有选项。因此，要使用这些功能，您需要通过执行设备模式更新来启用它们。默认情况下，**home** 模式禁用以下功能：**scheduler、socks、fetch、bandwidth-test、traffic-gen、sniffer、romon、proxy、hotspot、email、zerotier、container、install-any-version、partitions、routerboard。** |

可以对可用功能进行更具体的控制。设备模式控制的每个功能都可以专门打开或关闭。

例如，**scheduler** 将不允许在 `/system/scheduler` 中执行任何操作。所使用的设备模式会禁用所有列出的功能，例如，如果使用 **mode**=home，但您的设置需要 **zerotier**，则需要执行设备模式更新 `/system/device-mode/update` zerotier=yes，并且需要物理访问设备以按下按钮或切断电源。

#### 更改设备模式的高级示例

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes
[admin@MikroTik] > /system/device-mode/update mode=advanced zerotier=no
```

如果 update 命令指定了任何模式参数，则此更新将替换整个设备模式配置。在这种情况下，所有“按功能”的设置都将丢失，除非使用此命令指定。例如：

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes fetch=yes
[admin@MikroTik] > /system/device-mode/print config
   mode: home
  fetch: yes
  email: yes
[admin@MikroTik] > /system/device-mode/update mode=advanced sniffer=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no

```

我们看到 fetch = yes 和 email = yes 丢失了，因为它们被模式更改覆盖了。但是，仅指定“按功能”的设置将只更改这些设置：

```ros
[admin@MikroTik] > /system/device-mode/update hotspot=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
```

如果某项功能被禁用，交互式命令会显示错误消息：

```ros
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
[admin@MikroTik] > /tool/sniffer/quick 
failure: not allowed by device-mode
```

但是，可以向已禁用的功能添加配置，但设备模式中会显示一条注释，表明该功能已禁用：

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## 功能说明

| 功能 | 哪些菜单将变得不可更改的说明 |
| :-- | :-- |
| [带宽测试](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | *`/tool/bandwidth-test`* *`/tool/bandwidth-server`*  *`/tool/speed-test`* |
| [Routerboard](../hardware/routerboard.md) | *`/system/routerboard/settings`* (auto-upgrade 选项除外) |
| [容器](../containers/index.md) | 所有容器功能 |
| install-any-version | RouterOS 将不再允许您安装低于“allowed-versions”属性下列出的版本的 RouterOS。 |
| [电子邮件](./e-mail.md) | *`/tool/e-mail`* |
| [Fetch](./fetch.md) | *`/tool/fetch`* |
| [热点](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | *`/ip/hotspot`* |
| [IPsec](../virtual-private-networks/ipsec/index.mdx) | *`/ip/ipsec`* |
| [L2TP](../virtual-private-networks/l2tp/index.md) | *`/interface/l2tp-server`*  *`/interface/l2tp-client`* |
| [分区](./partitions.md) | */partitions* 不允许更改分区数量。如果您的路由器无法启动，它仍然能够启动到您的其他分区。对崩溃恢复没有限制。 |
| [PPTP](../virtual-private-networks/pptp.md) | *`/interface/pptp-server`*  *`/interface/pptp-client`* |
| [代理](../network-management/proxy/index.md) | *`/ip/proxy`* |
| [RoMon](../management-tools/romon.md) | *`/tool/romon`* |
| [调度器](./scheduler.md) | *`/system/scheduler`* |
| [SMB](../storage/smb.md) | *`/ip/smb`* |
| [嗅探器](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | *`/tool/sniffer`* |
| [SOCKS](../network-management/socks/index.md) | *`/ip/socks`* |
| [流量生成器](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | *`/tool/traffic-generator`*  *`/tool/flood-ping`*  *`/tool/ping-speed`* |
| [ZeroTier](../virtual-private-networks/zerotier.md) | */zerotier* |

## 允许的版本

设备模式在其参数中列出了一个名为“allowed-versions”的参数。这是 MikroTik 认为安全且不包含任何可能被攻击者利用的严重漏洞的版本列表。

此设置不依赖于已安装的 RouterOS 版本，并作为独立的保护层，以防止攻击者逐步降级版本以达到任何已知存在漏洞的 RouterOS 版本。当您将 RouterOS 升级到包含更新“allowed-versions”列表的版本时，最旧的列表将被覆盖。如果您降级 RouterOS，“allowed-versions”列表不会更改，并将保持更新到最新列表。如果启用了设备模式“install-any-version”，则忽略此列表。

## Flagged 状态

除了设备模式功能外，RouterOS 现在可以在系统启动时分析整个配置，以确定是否有任何未经授权访问路由器的迹象。如果检测到可疑配置，可疑配置将被禁用，并且 **flagged** 参数将设置为“yes”。设备现在处于 Flagged 状态并强制执行某些限制。

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

如果系统具有此 flagged 状态，则当前配置可以工作，但无法执行以下操作：

bandwidth-test、traffic-generator、sniffer，以及针对以下程序的配置操作（启用或创建新配置条目，但仍可禁用或删除）：*system scheduler、SOCKS proxy、pptp、l2tp、ipsec、proxy、smb*。

当路由器处于 flagged 状态时执行上述操作，您将收到错误消息：

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

要退出 flagged 状态，您必须执行命令“/system/device-mode/update flagged=no”。系统将要求您按下按钮或执行硬重启（物理切断电源或对虚拟机执行硬重启）。

**重要！** 尽管系统已禁用任何触发 flagged 状态的恶意规则，但在退出 flagged 状态之前，必须检查所有配置中是否有其他未知内容。如果您的系统已被标记，请假定您的系统已被入侵，并在重新启用系统之前对所有设置进行全面审计。完成审计后，更改所有系统密码并升级到最新的 RouterOS 版本。

:::warning
从 RouterOS 7.17 版本开始，设备模式限制双启动的 SwOS/RouterOS 转换；要启用，请执行：`/system/device-mode/update` routerboard=yes
:::