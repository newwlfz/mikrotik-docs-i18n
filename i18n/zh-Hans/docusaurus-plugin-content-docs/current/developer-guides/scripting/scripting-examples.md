# 脚本示例

> 本页提供 MikroTik RouterOS 的脚本示例，演示如何使用 RouterOS 脚本命令创建和修改文件、追加文本、检查 IP 变化、去除子网掩码以及解析主机名。

# 脚本示例

无法直接创建文件；但可以使用以下变通方法：

```ros
/file print file=myFile
/file set myFile.txt contents=""
```

## 在新行中向文件追加文本

没有直接向文件追加文本的方法；您可以存储旧内容并追加包含附加文本的新行：

```ros
:local oldText [/file get myFile.txt contents as-string]
:local addText "test append"
:local newText ($oldText."\n".$addText)
/file set myFile.txt contents=$newText
```

## 检查接口上的 IP 是否已更改

某些提供商分配动态 IP 地址。此脚本将新地址与当前地址进行比较。

```ros
:global currentIP;

:local newIP [/ip address get [find interface="ether1"] address];

:if ($newIP != $currentIP) do={
    :put "ip address $currentIP changed to $newIP";
    :set currentIP $newIP;
}
```

## 去除子网掩码

当您需要不带子网掩码的 IP 地址（例如，用于防火墙）时，此脚本非常有用，因为 `/ip address get [id] address` 会同时返回地址及其子网掩码。

```ros
:global ipaddress 10.1.101.1/24

:for i from=( [:len $ipaddress] - 1) to=0 do={
	:if ( [:pick $ipaddress $i] = "/") do={
		:put [:pick $ipaddress 0 $i]
	}
}
```

更简单的方法是：

```ros
:global ipaddress 10.1.101.1/24
:put [:pick $ipaddress 0 [:find $ipaddress "/"]]
```

## 解析主机名

许多用户希望能够在 RADIUS 服务器、防火墙规则等中使用 DNS 名称而不是 IP 地址。

以下是一个解析 RADIUS 服务器 IP 的示例。

假设 RADIUS 服务器配置如下：

```ros
/radius
add address=3.4.5.6 comment=myRad
```

以下脚本解析服务器的 IP 地址，将结果与配置值进行比较，并在不同时替换它：

```ros
/system script add name="resolver" source= {

:local resolvedIP [:resolve "server.example.com"];
:local radiusID [/radius find comment="myRad"];
:local currentIP [/radius get $radiusID address];

:if ($resolvedIP != $currentIP) do={
   /radius set $radiusID address=$resolvedIP;
   /log info "radius ip updated";
}

}
```

将此脚本添加到计划任务中，例如每五分钟运行一次。

```ros
/system scheduler add name=resolveRadiusIP on-event="resolver" interval=5m
```

## 将简单队列统计信息写入多个文件

假设队列名称使用 `some text.1` 格式，以便您可以根据点后的数字进行搜索。

```ros
:local entriesPerFile 10;
:local currentQueue 0;
:local queuesInFile 0;
:local fileContent "";
# 确定所需的文件数量
:local numQueues [/queue simple print count-only] ;
:local fileCount ($numQueues / $entriesPerFile);
:if ( ($fileCount * $entriesPerFile) != $numQueues) do={
   :set fileCount ($fileCount + 1);
}

# 删除旧文件
/file remove [find name~"stats"];

:put "fileCount=$fileCount";

:for i from=1 to=$fileCount do={
# 创建文件
   /file print file="stats$i.txt";
# 清空内容
   /file set [find name="stats$i.txt"] contents="";

   :while ($queuesInFile < $entriesPerFile) do={
     :if ($currentQueue < $numQueues) do={
         :set currentQueue ($currentQueue +1);
         :put $currentQueue ;
         /queue simple
         :local internalID [find name~"\\.$currentQueue\$"];
         :put "internalID=$internalID";
         :set fileContent ($fileContent . [get $internalID target-address] . \
           " " . [get $internalID total-bytes] . "\r\n");
     }
     :set queuesInFile ($queuesInFile +1);

   }
   /file set "stats$i.txt" contents=$fileContent;
   :set fileContent "";
   :set queuesInFile 0;

}

```

## 生成备份并通过电子邮件发送

此脚本生成备份文件并将其发送到指定的电子邮件地址。邮件主题包含路由器名称、当前日期和时间。

请注意，使用此脚本前必须配置 SMTP 服务器。有关配置选项，请参阅 [/tool e-mail](../../system-information-and-utilities/e-mail.md)。

```ros
/system backup save name=email_backup
/tool e-mail send file=email_backup.backup to="me@test.com" body="See attached file" \
   subject="$[/system identity get name] $[/system clock get time] $[/system clock get date] Backup"
```

:::warning
备份文件包含敏感信息，如密码。因此，脚本或计划任务必须具有 'sensitive' 策略才能访问生成的备份文件。
:::

## 将字符串用作函数

```ros
:global printA [:parse ":local A; :put \$A;" ];
$printA
```

## 检查带宽并添加限制

此脚本检查接口上的下载是否超过 512 kbps；如果超过，脚本会添加一个将速度限制为 256 kbps 的队列。

```ros
:foreach i in=[/interface find] do={
    /interface monitor-traffic $i once do={
        :if ($"received-bits-per-second" > 0 ) do={
            :local tmpIP [/ip address get [/ip address find interface=$i] address] ;
#            :log warning $tmpIP ;
            :for j from=( [:len $tmpIP] - 1) to=0 do={
                :if ( [:pick $tmpIP $j] = "/") do={
                    /queue simple add name=$i max-limit=256000/256000 dst-address=[:pick $tmpIP 0 $j] ;
                }
            }
        }
    }
}
```

## 阻止访问特定网站

当您想在不使用 Web 代理的情况下阻止某些网站时，此脚本非常有用。

此示例查看 DNS 缓存中的“Rapidshare”和“youtube”条目，并将 IP 添加到名为“restricted”的地址列表中。在开始之前，您必须设置路由器以捕获所有 DNS 请求：

```ros
/ip firewall nat
add action=redirect chain=dstnat comment=DNS dst-port=53 protocol=tcp to-ports=53
add action=redirect chain=dstnat dst-port=53 protocol=udp to-ports=53
```

然后添加防火墙规则：

```ros
/ip firewall filter
add chain=forward dst-address-list=restricted action=drop
```

编写脚本并安排每 30 秒运行一次。

脚本代码：

```ros
:foreach i in=[/ip dns cache find] do={
    :local bNew "true";
    :local cacheName [/ip dns cache all get $i name] ;
#    :put $cacheName;

    :if (([:find $cacheName "rapidshare"] >= 0) || ([:find $cacheName "youtube"] >= 0)) do={

        :local tmpAddress [/ip dns cache get $i address] ;
#	:put $tmpAddress;

# 如果地址列表为空，则不检查
        :if ( [/ip firewall address-list find list="restricted" ] = "") do={
            :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
            /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
        } else={
            :foreach j in=[/ip firewall address-list find list="restricted"] do={
                :if ( [/ip firewall address-list get $j address] = $tmpAddress ) do={
                    :set bNew "false";
                }
            }
            :if ( $bNew = "true" ) do={
                :log info ("added entry: $[/ip dns cache get $i name] IP $tmpAddress");
                /ip firewall address-list add address=$tmpAddress list=restricted comment=$cacheName;
            }
        }
    }
}
```

## 解析文件以添加 ppp secrets

此脚本要求文件中的条目采用以下格式：

username,password,local\_address,remote\_address,profile,service

例如：

```ros
janis,123,1.1.1.1,2.2.2.1,ppp_profile,myService
juris,456,1.1.1.1,2.2.2.2,ppp_profile,myService
aija,678,1.1.1.1,2.2.2.3,ppp_profile,myService
```

```ros
:global content [/file get [/file find name=test.txt] contents] ;
:global contentLen [ :len $content ] ;

:global lineEnd 0;
:global line "";
:global lastEnd 0;

:do {
       :set lineEnd [:find $content "\r\n" $lastEnd ] ;
       :set line [:pick $content $lastEnd $lineEnd] ;
       :set lastEnd ( $lineEnd + 2 ) ;

       :local tmpArray [:toarray $line] ;
	:if ( [:pick $tmpArray 0] != "" ) do={
	:put $tmpArray;
         /ppp secret add name=[:pick $tmpArray 0] password=[:pick $tmpArray 1] \
             local-address=[:pick $tmpArray 2] remote-address=[:pick $tmpArray 3] \
             profile=[:pick $tmpArray 4] service=[:pick $tmpArray 5];
}
} while ($lineEnd < $contentLen)
```

## 检测新的日志条目

此脚本检查特定缓冲区中是否添加了新的日志条目。

在此示例中，使用 PPPoE 日志：

```ros
/system logging action
add name="pppoe"
/system logging
add action=pppoe topics=pppoe,info,!ppp,!debug
```

日志缓冲区如下所示：

```ros
[admin@mainGW] > /log print where buffer=pppoe
13:11:08 pppoe,info PPPoE connection established from 00:0C:42:04:4C:EE
```

以下脚本检测何时添加新条目。

```ros
:global lastTime;

:global currentBuf [ :toarray [ /log find buffer=pppoe  ] ] ;
:global currentLineCount [ :len $currentBuf ] ;
:global currentTime [ :totime [/log get [ :pick $currentBuf ($currentLineCount -1) ] time   ] ];

:global message "";

:if ( $lastTime = "" ) do={
	:set lastTime $currentTime ;
	:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];

} else={
	:if ( $lastTime < $currentTime ) do={
		:set lastTime $currentTime ;
		:set message [/log get [ :pick $currentBuf ($currentLineCount-1) ] message];
	}
}
```

检测后，新条目保存在 `message` 变量中；您可以稍后解析此变量以获取详细信息，例如 PPPoE 客户端的 MAC 地址。

## 允许使用 [ntp.org](http://ntp.org) 池服务进行 NTP

此脚本解析两个 NTP 服务器的主机名，将结果与当前 NTP 设置进行比较，并在不同时更改地址。由于 RouterOS 不允许在 NTP 配置中使用主机名，因此需要此脚本。使用两个脚本。第一个定义系统变量，供执行工作的第二个脚本使用：

```ros
# 系统配置脚本 - "GlobalVars"

:put "Setting system globals";

# 系统名称
:global SYSname [/system identity get name];

# 用于发送通知的电子邮件地址
:global SYSsendemail "mail@my.address";

# 用于发送通知的电子邮件地址（发件人）
:global SYSmyemail "routeros@my.address";

# 要使用的邮件服务器
:global SYSemailserver "1.2.3.4";

# 要使用的 NTP 池（请查看 www.pool.ntp.org）
:global SYSntpa "0.uk.pool.ntp.org";
:global SYSntpb "1.uk.pool.ntp.org";
```

```ros
# 检查并设置 NTP 服务器 - "setntppool"

# 我们需要使用以下全局变量，这些变量必须在此处定义，即使
# 它们也在我们调用以设置它们的脚本中定义。
:global SYSname;
:global SYSsendemail;
:global SYSmyemail;
:global SYSemailserver;
:global SYSntpa;
:global SYSntpb;

# 使用系统默认值加载全局变量
/system script run GlobalVars

# 解析两个 ntp 池主机名
:local ntpipa [:resolve $SYSntpa];
:local ntpipb [:resolve $SYSntpb];

# 获取当前设置
:local ntpcura [:pick [/system/ntp/client/get servers] 0];
:local ntpcurb [:pick [/system/ntp/client/get servers] 1];

# 定义一个变量以了解是否有任何更改。
:local bChange 0;

# 调试输出
:put ("Old: " . $ntpcura . " New: " . $ntpipa);
:put ("Old: " . $ntpcurb . " New: " . $ntpipb);

# 如果需要，更改服务器
:if ($ntpipa != $ntpcura || $ntpipb != $ntpcurb) do={
    :put "Changing NTP servers";
    /system/ntp/client/set servers="$ntpipa,$ntpipb";
    :set bChange 1;
    }

# 如果我们进行了更改，请发送电子邮件说明。
:if (($bChange = 1)) do={
    :put "Sending e-mail.";
    /tool e-mail send \
        to=$SYSsendemail \
        subject=($SYSname . " NTP change") \
        from=$SYSmyemail \
        server=$SYSemailserver \
        body=("Your NTP servers have just been changed:\n\nPrimary:\nOld: " . $ntpcura . "\nNew: " \
          . $ntpipa . "\n\nSecondary\nOld: " . $ntpcurb . "\nNew: " . $ntpipb);
    }
```

计划任务条目：

```ros
/system scheduler add \
  comment="Check and set NTP servers" \
  disabled=no \
  interval=12h \
  name=CheckNTPServers \
  on-event=setntppool \
  policy=read,write,test \
  start-date=1970-01-01 \
  start-time=16:00:00
```