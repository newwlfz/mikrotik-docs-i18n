# 看门狗（Watchdog）

> RouterOS 配置中的看门狗页面允许设置系统在 IP 地址无响应或软件锁定时自动重启，并提供 ping 监控及通过电子邮件自动发送支持输出文件的选项。

# 看门狗

**子菜单:** `/system/watchdog`

此菜单允许配置系统在特定 IP 地址无响应或检测到软件锁定时进行重启。检测通过两种方式进行：

- 软件看门狗定时器（多由硬件故障引起）：设备可通过重启自行恢复。
- Ping 看门狗可监控与特定 IP 地址的连通性，并触发重启功能。

:::info
**注意：** 这是两个不同的看门狗功能，且各有其独立设置。默认情况下，软件看门狗已启用，而 ping 看门狗处于禁用状态。您可以通过指定 IP 地址来启用 ping 看门狗，也可以通过取消设置看门狗定时器选项来禁用软件看门狗。

**重要提示：** **注意：** 看门狗重启并非系统故障。此类重启也不会生成自动支持输出文件（autosupout）。看门狗重启是操作系统在某个服务响应速度未达预期时自动触发的 `/system/reboot`。其原因可能包括硬件损坏、某些服务的软件实现缓慢、DDoS 攻击、错误配置等。
:::

## 属性

| 属性 | 说明 |
| :-- | :-- |
| **auto-send-supout** (*是 \| 否*; 默认值：**否**) | 支持输出文件自动生成后，可通过电子邮件发送。 |
| **automatic-supout** (*是 \| 否*; 默认值：**是**) | 当软件故障发生时，自动生成名为 "autosupout.rif" 的文件。之前的 "autosupout.rif" 文件将重命名为 "autosupout.old.rif"。 |
| **no-ping-delay** (*时间*; 默认值：5m) | 指定在尝试访问监控地址之前等待的时间。 |
| **ping-timeout** (*时间*; 默认值：60s) | 指定在“无 ping 延迟”之后，设备将被 ping 6 次的时间间隔。 |
| **send-email-from** (*字符串*; 默认值：) | 发送支持输出文件所用的电子邮件地址。若未设置，则使用 `/tool/e-mail` 中设置的值。 |
| **send-email-to** (*字符串*; 默认值：) | 接收支持输出文件的电子邮件地址。 |
| **send-smtp-server** (*字符串*; 默认值：) | 用于发送支持输出文件的 SMTP 服务器地址。若未设置，则使用 `/tool/e-mail` 中设置的值。 |
| **watch-address** (*IP*; 默认值：) | 若对指定 IP 地址的 6 次连续 ping 均失败，系统将重启。若设置为 none，则此功能禁用。默认情况下，如果设置了监控地址且无法访问，路由器将每 6 分钟重启一次。 |
| **watchdog-timer** (*是 \| 否*; 默认值：**是**) | 系统无响应达一分钟时是否重启。 |

## 快速示例

要使系统在软件崩溃时生成支持输出文件，并通过 192.0.2.1 自动发送至 support@example.com：

```ros
[admin@MikroTik] /system/watchdog/set auto-send-supout=yes \
\... send-email-to=support@example.com send-smtp-server=192.0.2.1
[admin@MikroTik] /system/watchdog> print
      watch-address: none
     watchdog-timer: yes
      no-ping-delay: 5m
   automatic-supout: yes
   auto-send-supout: yes
   send-smtp-server: 192.0.2.1
      send-email-to: support@example.com
```