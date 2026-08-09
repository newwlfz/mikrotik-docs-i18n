# WWAN 与 GNSS 优先级自动化

> 蜂窝连接与 GNSS 无法同时工作（BG77 模块中的 WWAN 和 GNSS 接收链路共享某些硬件模块，这意味着该模块不支持 WWAN 和 GNSS 的并发操作）。因此引入了 ***at+qgpscfg="priority",(0-1)*** 命令。借助该命令，您可以手动更改其中一方的优先级。

# 概述

蜂窝连接与 GNSS 无法同时工作（BG77 模块中的 WWAN 和 GNSS 接收链路共享某些硬件模块，这意味着该模块不支持 WWAN 和 GNSS 的并发操作）。因此引入了 ***at+qgpscfg="priority",(0-1)*** 命令。借助该命令，您可以手动更改其中一方的优先级。

***at+qgpscfg="priority",0*** 命令设置 **GNSS 为最高优先级**。

***at+qgpscfg="priority",1*** 命令设置 **LTE (WWAN) 为最高优先级**。

在实际应用中，手动更改优先级并不方便，因此为了实现自动更改优先级，我们建议使用以下方法。

:::info
 从 7.1rc3 固件版本开始，可以检查设备上次获取 NMEA 数据（GPS 数据）的时间。此信息可用于故障排除。您可以在 CLI 中使用命令 "system gps monitor once" 检查此参数。"data-age" 参数表示设备上次收到 NMEA 消息的时间。
:::

## 检测到无出站流量时自动切换至 GNSS

自动化可以通过 ppp profile 的 "**on-down**" 脚本、"**idle-timeout**" 功能以及 PPP 接口的 "**dial on demand**" 设置来实现。

实施后，当存在互联网流量时，BG77 调制解调器将使用蜂窝数据（在此期间不会接收 GNSS 坐标），并在检测不到互联网流量时自动启用 GPS 接收。

**Idle-timeout** 参数指定在没有活动的情况下链路将被终止的时间。

**On-down** 脚本字段允许您配置一个脚本，该脚本将在 PPP 接口每次关闭时运行（包括在 **idle-timeout** 不活动之后）。该脚本将设置调制解调器的优先级为 GNSS 接收。

**Dial-on-demand** 将确保 PPP 接口仅在存在出站流量时才尝试建立连接（此外，调制解调器将自动设置 WWAN/蜂窝连接优先级）。这将确保在 **idle-timeout** 发生后，除非检测到出站数据包，否则不会自动重新建立连接。

通过结合这三个功能，您可以实现以下场景：

- 如果有出站流量，PPP 接口将处于启用状态（因为 "**dial on demand**"），并且优先级将设置为蜂窝连接。PPP 接口的调制解调器初始化 AT 命令（在 PPP 接口的 `modem-init="AT+QGPSCFG="priority",1"` 设置下配置）用于 WWAN 优先级将被发送。在此期间，不会接收 GPS 坐标。
- 如果在 "**idle-timeout**" 不活动窗口后未检测到流量，PPP 接口将关闭，并且由于 "**dial on demand**" 设置，在检测到出站数据包之前不会建立连接。此时将运行 "**on-down**" 脚本，将 WWAN 优先级切换为 GNSS 优先级。
为了实现此功能，只需添加一个新的 PPP profile：

```ros
/ppp profile add idle-timeout=30s name=BG77 on-down="/interface ppp-client at-chat [find where modem-init=\"AT+QGPSCFG=\\\"priority\\\",1\"] input=\"AT+QGPSCFG=\\\"priority\\\",0\""
```

上述示例创建了一个名为 "BG77" 的新 profile，将 **idle-timeout** 设置为 30 秒，并启用了 **on-down** 脚本，该脚本将发送 GNSS 优先级 AT 命令。

之后，确保将此新创建的 profile 应用到 PPP 接口上：

```ros
/interface ppp-client set profile=BG77 0
```

并确认其已应用（`profile=BG77`）：

```ros
/interface ppp-client print
Flags: X - disabled; R - running 
0 R name="ppp-out1" max-mtu=1500 max-mru=1500 mrru=disabled port=modem data-channel=2 info-channel=2 
apn="internet" pin="" user="" password="" profile=BG77 phone="" dial-command="ATDT" 
modem-init="AT+QGPSCFG="priority",1" null-modem=no dial-on-demand=yes add-default-route=yes 
default-route-distance=1 use-peer-dns=yes keepalive-timeout=30 allow=pap,chap,mschap1,mschap2 
```

## 使用脚本和调度器切换至 GNSS

以下脚本应通过调度器进行配置。调度器将确保脚本每隔 ***x*** 小时/分钟（根据您的需求）启动一次。

```
:global lat
:global lon
:global spd
:global alt
/interface ppp-client set ppp-out1 disabled=yes
log info ("disabling WWAN to get GPS coordinates")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",0"
log info ("enabling priority for GPS")
###the time in the delay below is the time that the device will wait for to get the coordinate fix
delay 32000ms
log info ("reading GPS coordinates")
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
if ($lat != "none") do={\
log info ("enabling priority back to WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
log info ("enabling WWAN")
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
#the delay below waits for 5 seconds for the ppp connection to get established - this time can differ based on the signal strength
delay 5000ms
log info ("posting coordinates via fetch")
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
else={
log info ("could not read GPS coordinates...enabling back WWAN")
/interface ppp-client at-chat ppp-out1 input="AT+QGPSCFG=\"priority\",1"
/interface ppp-client set ppp-out1 disabled=no
delay 1000ms
###if dial on demand is enabled
###/ping 1.1.1.1 count=1
}
```

如果启用了 "dial on demand"，请取消注释（删除 "###"）脚本中的 ping 行 "/ping 1.1.1.1 count=1"，因为没有出站流量 → ppp 接口将不会建立连接。

此脚本将执行以下操作：禁用 ppp 接口，发送 GNSS 优先级命令，并等待 32 秒直到设备获取坐标（这是建议 Quectel 调制解调器获取坐标定位的时间）。您可以根据自己的偏好和信号强度调整此时间。每种情况可能各不相同。在 32 秒延迟后，如果成功接收到坐标（如果纬度不等于 "none" 而等于任何其他值），脚本将发送 WWAN 优先级命令，重新启用 ppp 接口，并使用 "/tool fetch" 将坐标发布到配置的 HTTP 服务器。如果在 32 秒延迟后未接收到坐标（如果纬度将为 "none"），脚本将发送 WWAN 优先级命令并重新启用 ppp 接口，而不发布任何结果。

不要忘记根据您的 HTTP 服务器配置/要求修改脚本中的 "/tool fetch" 部分。

您也可以使用 MQTT 代替 HTTP post。为此，请将配置中的 "/tool fetch" 部分从：

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

改为 MQTT：

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="{\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                
  }"}\
```

根据您的需要修改 broker、topic 和 message。您可以点击链接了解更多关于如何配置 MQTT 的信息。

例如，如果 MQTT 服务器/broker 是 AWS，发布的结果将如下所示：

![](https://manual.mikrotik.com/docs/mobile-networking/bg77-modem-at-commands/img/image2021-8-30_14-8-26.webp)

## 使用脚本和调度器在检测到无出站流量时切换至 GNSS

第一个脚本用于检查是否有流量，并根据此情况来回切换优先级。

第二个脚本可用于启用 WWAN 优先级并将 GPS 坐标发布到您选择的服务器。您可以使用任何支持的协议，如 HTTPS post (fetch) 或 MQTT 来发布坐标。

### 第一个脚本

以下脚本将自动创建一个调度器：

```
/system scheduler
add name="GPS/WWAN enabler" on-event=":delay 30s\r\
    \n\r\
    \n:local pppName ppp-out1\r\
    \n:local pppModemInitInit \"AT+QGPSCFG=\\\"priority\\\",1\"\r\
    \n:local gpsCmd \"AT+QGPSCFG=\\\"priority\\\",0\"\r\
    \n:local idleCount 5\r\
    \n\r\
    \n\r\
    \n:local pppStats\r\
    \n:local pppStatsPrev\r\
    \n:local pppStatsReset\r\
    \n:local idleCounter\r\
    \n\r\
    \n:while (true) do={\r\
    \n\r\
    \n:if ( \\\r\
    \n  [/interface ppp-client get \$pppName running] \\\r\
    \n  && [/system gps get enabled] \\\r\
    \n  && [/interface ppp-client get \$pppName dial-on-demand] \\\r\
    \n  && \$pppModemInitInit=[/interface ppp-client get \$pppName modem-init]\
    \_) \\\r\
    \n  do={\r\
    \n    :set pppStats [:toarray ([/interface print stats as-value where name\
    =ppp-out1]->0)] \r\
    \n    :if ( \\\r\
    \n      \$pppStats->\"rx-packet\"=\$pppStatsPrev->\"rx-packet\" \\\r\
    \n      && \$pppStats->\"tx-packet\"=\$pppStatsPrev->\"tx-packet\" ) \\\r\
    \n      do={\r\
    \n        :set idleCounter (\$idleCounter+1)\r\
    \n:put (\"debug: idle \".\$idleCounter)\r\
    \n        :if ( \\\r\
    \n          \$idleCounter>=\$idleCount \\\r\
    \n          && \$pppStats->\"rx-packet\"!=\$pppStatsReset->\"rx-packet\" \
    \\\r\
    \n          && \$pppStats->\"tx-packet\"!=\$pppStatsReset->\"tx-packet\" )\
    \_\\\r\
    \n          do={\r\
    \n            :set pppStatsReset \$pppStats\r\
    \n            :set idleCounter 0\r\
    \n            :log info (\$pppName.\" idling - reseting dial-on-demand, pr\
    ioritizing GPS\")\r\
    \n            /interface ppp-client set \$pppName disabled=yes\r\
    \n            :do { /interface ppp-client at-chat \$pppName input=\$gpsCmd\
    \_} \\\r\
    \n                on-error={\r\
    \n:put (\"debug: GPS at-chat error\")                \r\
    \n                  :set idleCounter 0\r\
    \n                  :set pppStatsReset ({})\r\
    \n                  }\r\
    \n            /interface ppp-client set \$pppName disabled=no\r\
    \n            }\r\
    \n          :delay 1s\r\
    \n        } \\\r\
    \n      else={\r\
    \n:put (\"debug: no idle\")      \r\
    \n        :set idleCounter 0\r\
    \n        :set pppStatsPrev \$pppStats\r\
    \n        :delay 1s \r\
    \n        }\r\
    \n    } \\\r\
    \n  else={\r\
    \n:put (\"debug: unsupported config\")\r\
    \n    :set idleCounter 0\r\
    \n    :set pppStatsReset ({})\r\
    \n    :delay 1s\r\
    \n    }\r\
    \n}" policy=\
    ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon \
    start-time=startup
```

复制以上所有行并粘贴到一个新脚本中。运行该脚本，您将创建一个 "scheduler"。您可以在 System>Scheduler>"GPS/WWAN enabler" 下检查该 "scheduler"。

原始脚本如下所示：

```
:local pppName ppp-out1
:local pppModemInitInit "AT+QGPSCFG=\"priority\",1"
:local gpsCmd "AT+QGPSCFG=\"priority\",0"
:local idleCount 5
:local pppStats
:local pppStatsPrev
:local pppStatsReset
:local idleCounter
:while (true) do={
:if ( \
  [/interface ppp-client get $pppName running] \
  && [/system gps get enabled] \
  && [/interface ppp-client get $pppName dial-on-demand] \
  && $pppModemInitInit=[/interface ppp-client get $pppName modem-init] ) \
  do={
    :set pppStats [:toarray ([/interface print stats as-value where name=ppp-out1]->0)] 
    :if ( \
      $pppStats->"rx-packet"=$pppStatsPrev->"rx-packet" \
      && $pppStats->"tx-packet"=$pppStatsPrev->"tx-packet" ) \
      do={
        :set idleCounter ($idleCounter+1)
:put ("debug: idle ".$idleCounter)
        :if ( \
          $idleCounter>=$idleCount \
          && $pppStats->"rx-packet"!=$pppStatsReset->"rx-packet" \
          && $pppStats->"tx-packet"!=$pppStatsReset->"tx-packet" ) \
          do={
            :set pppStatsReset $pppStats
            :set idleCounter 0
            :log info ($pppName." idling - reseting dial-on-demand, prioritizing GPS")
            /interface ppp-client set $pppName disabled=yes
            :do { /interface ppp-client at-chat $pppName input=$gpsCmd } \
                on-error={
:put ("debug: GPS at-chat error")                
                  :set idleCounter 0
                  :set pppStatsReset ({})
                  }
            /interface ppp-client set $pppName disabled=no
            }
          :delay 1s
        } \
      else={
:put ("debug: no idle")      
        :set idleCounter 0
        :set pppStatsPrev $pppStats
        :delay 1s 
        }
    } \
  else={
:put ("debug: unsupported config")
    :set idleCounter 0
    :set pppStatsReset ({})
    :delay 1s
    }
}
```

为了使脚本正常工作，必须满足几个条件。

第一个条件是 ppp 接口（Interfaces>Interface）和 GPS（System>GPS）都必须启用并同时工作。您可能需要在启用 GPS 之前禁用 ppp，因为它们使用相同的串行端口。当 GPS 和 ppp 都启用后，请确保满足第二个条件。

第二个条件是在 ppp 接口的 "Modem Init" 字段下配置 AT 命令 "***AT+QGPSCFG="priority",1***"：

![](https://manual.mikrotik.com/docs/mobile-networking/bg77-modem-at-commands/img/image2021-8-30_12-10-52.webp)

这将实现：每当 ppp 连接成功建立时，发送 WWAN 优先级命令。

最后，第三个条件是 ppp 接口启用了 "dial on demand"：

![](https://manual.mikrotik.com/docs/mobile-networking/bg77-modem-at-commands/img/image2021-8-30_12-27-59.webp)

这是必需的，因为否则，当 "dial on demand" 被禁用时 → ppp 接口将在端口重新启用时自动发送带有 WWAN 优先级设置的 AT 命令（尝试建立连接）。当 "dial on demand" 启用时 → 在接口重新启用后，ppp 连接将不会建立，并且 WWAN 优先级的 AT 命令将不会发送，直到检测到出站数据包。

当所有 3 个条件都满足时 → 脚本将执行以下操作：

脚本将比较 "counters" 以判断是否存在流量（基于 ppp 接口的 Tx 数据包和 Rx 数据包）。如果没有流量，"counter" 将增加，当达到 "idleCount" 时，ppp 接口被禁用，然后重新启用，并发送 GNSS 优先级命令。在此期间，如果仍然没有出站流量，GPS 坐标应被更新（在 System>GPS 下）。一旦检测到任何流量，"counter" 将被重置，并通过建立 ppp 连接发送 WWAN 优先级命令。

一旦所有 3 个条件都满足且调度器准备就绪，请重新启动设备以使脚本生效。

### 第二个脚本

第二个脚本用于收集 GPS 坐标并将其发送到服务器。

```
:global lat
:global lon
:global spd
:global alt
/system gps monitor once do={
:set $lat $("latitude")
:set $lon $("longitude")
:set $spd $("speed")
:set $alt $("altitude")
}
:set $spd [:pick $spd 0 [find $spd " km"]]
:set $alt [:pick $alt 0 [find $alt "m"]]
:if ($lat != "none") do={
/ping 1.1.1.1 count=1
:delay 3000ms;
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL"}\
else={log info ("could not read GPS coordinates")}
```

该脚本将 "读取" GPS 坐标，如果纬度能被成功 "读取"（如果纬度不等于 "none" 而等于任何其他值），则 ping "1.1.1.1" 一次（以产生出站流量），等待 3 秒让 ppp 连接建立，然后发起 "/tool fetch"（HTTP post）。否则，如果无法确定纬度（当脚本启动时），则不会发生任何事情（您将看到一条日志消息，表明设备无法读取 GPS 坐标）。

您可以将脚本中的 "delay" 行更改为您的设备成功与 ISP 建立 ppp (CAT-M/NB-IoT) 连接所需的实际时间。

您可以设置一个调度器，随时运行该脚本。

脚本中的 "/tool fetch" 部分应根据您的服务器设置进行相应配置。

您也可以使用 MQTT 代替 HTTP post。如果您希望这样做，请将 "/tool fetch" 部分从：

```
/tool fetch http-method=post output=user http-header-field="content-type:application/json" http-data="[\
{\
                \"payload\":{\
                             \"lat\":$lat,\
                              \"lng\":$lon,\
                               \"speed\":$spd,\
                                \"altitude\":$alt\
                                    }\
    }\
]" url="https://change-this-URL-accordingly"}\
```

改为：

```
/iot mqtt publish broker="AWS" topic="my/test/topic" message="&#123;\
                                 \"lat\":$lat,\
                                  \"lng\":$lon,\
                                   \"speed\":$spd,\
                                    \"altitude\":$alt \                                  
  }"}\
```

不要忘记根据您的需要修改 broker、topic 和 message。您可以点击链接了解更多关于如何配置 MQTT 的信息。

例如，如果 MQTT 服务器是 AWS，结果将如下所示：

![](https://manual.mikrotik.com/docs/mobile-networking/bg77-modem-at-commands/img/image2021-8-30_14-8-26.webp)