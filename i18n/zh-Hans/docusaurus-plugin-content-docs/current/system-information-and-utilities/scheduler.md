# 调度器

> MikroTik RouterOS 调度器支持脚本的定时执行，从而精确控制任务的运行时间与频率。它支持基于时间间隔或单次执行模式，并具备开始时间、时间间隔时长及脚本事件名称等属性。

# 调度器

### 概述

调度器可以在特定时间点、指定时间间隔之后，或同时满足两者条件时触发脚本执行。

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **days** (*always* \| *sun* \| *mon* \| *tue* \| *wed* \| *thu* \| *fri* \| *sat*; 默认值: **always**) | 任务可以运行的一周中的日期。多个日期用逗号分隔（例如，`mon,wed,fri`）。使用 `always` 表示每天运行。 |
| **interval** (*time*; 默认值: **0s**) | 两次脚本执行之间的时间间隔。设置为零时，脚本仅在开始时间运行一次。 |
| **name** (*string*; 默认值: ) | 任务的名称。 |
| **on-event** (*string*; 默认值: ) | 要执行的脚本。 |
| **policy** (*ftp \| reboot \| read \| write \| policy \| test \| password \| sniff \| sensitive \| romon*; 默认值: ) | 应用于计划脚本的策略，控制执行期间的权限。 |
| **start-date** (*date*; 默认值: ) | 首次执行脚本的日期。 |
| **start-time** (*time \| startup*; 默认值: ) | 首次执行脚本的时间。使用 `startup` 在系统启动后 3 秒执行。 |
| **run-count** (*只读: integer*) | 每次脚本运行时递增的计数器。重启后重置。 |

## 备注

重启路由器将重置 run-count 计数器。

如果多个脚本需要同时执行，它们将按照在调度器配置中出现的顺序执行。如果某个计划脚本用于禁用另一个脚本，这一点可能很重要。

如果需要更复杂的执行模式，通常可以通过调度多个脚本，并让它们相互启用和禁用来实现。

当同时设置了 `days`、特定的 `start-time` 和 `interval` 时，任务将在匹配日期的指定开始时间启动，并按给定间隔重复，直到当天结束。

:::note
如果调度器条目的 start-time 设置为 startup，其行为就像 start-time 和 start-date 被设置为控制台启动后 3 秒的时间一样。`start-time=startup` 且 `interval=0` 的脚本将在路由器每次启动时执行一次。如果 interval 设置为非 0 的值，调度器将**不会**在启动时运行。
:::

### 示例

我们将添加一个任务，每小时执行一次脚本 log-test：

```ros
[admin@MikroTik] /system/script> add name=log-test source=":log info message=test" 
[admin@MikroTik] /system/script> print 
Flags: I - invalid 
0 name="log-test" owner="admin" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon dont-require-permissions=no run-count=0 
source=:log info message=test 
[admin@MikroTik] /system/script> .. /scheduler 
[admin@MikroTik] /system/scheduler> add name=run-1h interval=1h 
on-event=log-test 
[admin@MikroTik] /system/scheduler> print 
Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 run-1h log-test 2004-03-30 06:11:35 1h 0 
[admin@MikroTik] /system/scheduler>
```

以下示例仅在业务日运行任务：

```ros
[admin@MikroTik] /system/script> add name=business-log source=":log info message=workday"
[admin@MikroTik] /system/script> .. scheduler
[admin@MikroTik] /system/scheduler> add name=workday-task interval=1d on-event=business-log days=mon,tue,wed,thu,fri start-time=8:00:00
[admin@MikroTik] /system/scheduler> print
Flags: X - disabled
# NAME ON-EVENT START-DATE START-TIME INTERVAL DAYS RUN-COUNT
0 workday-task business-log 2026-07-16 08:00:00 1d mon,tue,wed,thu,fri 0
[admin@MikroTik] /system/scheduler>
```

在另一个示例中，将添加两个脚本，用于更改队列规则 "Cust0" 的带宽设置。每天上午 9 点，队列将设置为 64Kb/s，下午 5 点，队列将设置为 128Kb/s。队列规则、脚本和调度器任务如下：

```ros
[admin@MikroTik] /queue/simple> add name=Cust0 interface=ether1 \ 
\... dst-address=192.168.0.0/24 limit-at=64000
 [admin@MikroTik] /queue/simple> print
 Flags: X - disabled, I - invalid 0 name="Cust0" target-address=0.0.0.0/0 dst-address=192.168.0.0/24
 interface=ether1 limit-at=64000 queue=default priority=8 bounded=yes 
[admin@MikroTik] /queue/simple> /system/script 
[admin@MikroTik] /system/script> add name=start_limit source={/queue/simple/set \
 \... Cust0 limit-at=64000} 
[admin@MikroTik] /system/script> add name=stop_limit source={/queue/simple/set \ 
\... Cust0 limit-at=128000} 
[admin@MikroTik] /system/script> print 
0 name="start_limit" source="/queue/simple/set Cust0 limit-at=64000" 
owner=admin run-count=0 
1 name="stop_limit" source="/queue/simple/set Cust0 limit-at=128000" 
owner=admin run-count=0 
[admin@MikroTik] /system/script> .. scheduler 
[admin@MikroTik] /system/scheduler> add interval=24h name="set-64k" \ 
\... start-time=9:00:00 on-event=start_limit 
[admin@MikroTik] /system/scheduler> add interval=24h name="set-128k" \
 \... start-time=17:00:00 on-event=stop_limit 
[admin@MikroTik] /system/scheduler> print
 Flags: X - disabled 
# NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT
 0 set-64k start... 2008-10-30 09:00:00 1d 0 
1 set-128k stop_... 2008-10-30 17:00:00 1d 0 
[admin@MikroTik] /system/scheduler>
```

以下示例调度一个脚本，每周通过电子邮件发送路由器配置的备份。

```ros
[admin@MikroTik] /system/script> add name=e-backup source={/system/backup 
{... save name=email; /tool/e-mail/send to="root@host.com" subject=([/system 
{... /identity/get name] . " Backup") file=email.backup} 
[admin@MikroTik] /system/script> print 
0 name="e-backup" source="/system/backup/save name=ema... owner=admin run-count=0 

[admin@MikroTik] /system/script> ../scheduler 
[admin@MikroTik] /system/scheduler> add interval=7d name="email-backup" \
 \... on-event=e-backup 
[admin@MikroTik] /system/scheduler> print
 Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 email-... e-backup 2008-10-30 15:19:28 7d 1 
[admin@MikroTik] /system/scheduler>
```

不要忘记设置电子邮件设置，即 `/tool/e-mail` 下的 SMTP 服务器和发件人地址。例如：

```ros
[admin@MikroTik] /tool/e-mail> set server=159.148.147.198 from=SysAdmin@host.com 
[admin@MikroTik] /tool/e-mail> print
 server: 159.148.147.198 
from: SysAdmin@host.com 
[admin@MikroTik] /tool/e-mail>
```

下面的示例将从午夜到中午每小时在日志中记录 'x'：

```ros
[admin@MikroTik] /system/script> add name=enable-x source={/system/scheduler 
{... enable x} 
[admin@MikroTik] /system/script> add name=disable-x source={/system/scheduler 
{... disable x} 
[admin@MikroTik] /system/script> add name=log-x source={:log info message=x} 
[admin@MikroTik] /system/script> .. scheduler 
[admin@MikroTik] /system/scheduler> add name=x-up start-time=00:00:00 \ 
\... interval=24h on-event=enable-x 
[admin@MikroTik] /system/scheduler> add name=x-down start-time=12:00:00
 \... interval=24h on-event=disable-x 
[admin@MikroTik] /system/scheduler> add name=x start-time=00:00:00 interval=1h \ 
\... on-event=log-x 
[admin@MikroTik] /system/scheduler> print 
Flags: X - disabled
 # NAME ON-EVENT START-DATE START-TIME INTERVAL RUN-COUNT 
0 x-up enable-x 2008-10-30 00:00:00 1d 0 
1 x-down disab... 2008-10-30 12:00:00 1d 0 
2 x log-x 2008-10-30 00:00:00 1h 0 
[admin@MikroTik] /system/scheduler>
```