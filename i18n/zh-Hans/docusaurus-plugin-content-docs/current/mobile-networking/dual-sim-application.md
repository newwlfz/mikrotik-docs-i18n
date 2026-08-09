# 双SIM卡应用

> 本文档介绍如何在 MikroTik RouterOS 中为双 SIM 卡 LTE 设备配置和自动化 SIM 卡切换，包括初始设置步骤、漫游状态检查以及根据 LTE 连接状态在家庭/漫游网络之间切换的示例脚本。

# 双SIM卡应用

### 概述

第一个脚本示例演示了如何在 LtAP mini 设备检测到移动漫游时切换 SIM 卡槽。这对于移动车载应用非常有用，例如汽车、公交车或火车在跨境行驶时，应使用两张 SIM 卡（一张用于家庭网络，另一张用于漫游网络）。由于 RouterOS 在 LTE 监视器中提供漫游状态（仅在漫游时显示），我们可以在 RouterOS 脚本中利用此状态来相应地切换 SIM 卡。

第二个脚本示例演示了如何在当前选定的 SIM 卡失去移动连接时切换 SIM 卡。

**注意：** 请记住，这些只是如何利用双 SIM 卡槽的示例。对于实际生产环境，应进行充分测试，因此请根据您的需求优化这些脚本并添加新功能。

### 初始设置

首先，请确保您已为每张 SIM 卡正确设置了 LTE 网络参数（由移动网络运营商提供）。您可以使用默认 APN 配置文件或创建两个独立的配置文件，请参考此链接 - [LTE/5G#快速设置示例](./lte-5g.md#quick-setup-example)。本示例使用默认 APN 配置文件。

之后，使用以下命令启用数据漫游以连接其他国家的数据提供商。这使我们能够跟踪漫游状态。

```
/interface/lte/set [find name=lte1] allow-roaming=yes

```

然后，选择哪些 SIM 卡槽将用于家庭网络和漫游网络。在本示例中，我们使用“down”卡槽用于家庭网络，“up”卡槽用于漫游网络。某些设备型号（如 SXT）的 SIM 卡槽命名为“a”和“b”，而不是“up”和“down”。使用以下命令在活动卡槽之间切换。

### RouterOS v6 版本中的命令

```
/system/routerboard/modem/set sim-slot=down

```

### RouterOS v7 版本中的命令

```
/interface/lte/settings/set sim-slot=down

```

更改 SIM 卡槽后，LTE 调制解调器将重新启动。完全初始化可能需要一些时间（取决于调制解调器和主板，大约 30 秒），因此请务必测试您的调制解调器。

### 漫游脚本示例

现在创建一个将由调度器运行的脚本。此脚本将涵盖几个关键点：

- 检查 LTE 接口是否已初始化（显示在 `/interface/lte` 中），否则，尝试电源重置。
- 检查 LTE 连接是否已建立（接口处于“运行”状态），否则，创建日志条目并等待下一次调度。
- 读取当前使用的 LTE 卡槽，并根据漫游状态决定是否更换 SIM 卡。

我们将此脚本命名为“roamingScript”，源代码如下：

```
{
# 设置并读取当前值，“up” SIM 卡槽用于漫游，“down” 用于家庭网络
:global simSlot [/interface/lte/settings/get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60

# 等待 LTE 初始化，最长等待 “timeoutLTE” 秒
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface/lte/find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}

# 检查 LTE 是否已初始化，否则尝试电源重置调制解调器
:if ($isLTEinit=true) do={
    # 等待 LTE 接口连接到移动网络，最长等待 “timeoutConnect” 秒
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface/lte/get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # 检查 LTE 是否已连接
    if ($isConnected=true) do={
        :local Info [/interface/lte/monitor lte1 once as-value]
        :local isRoaming ($Info->"roaming")
        # 检查当前使用的 SIM 卡槽
        :if ($simSlot="down") do={
            # 如果使用 “down”（家庭）卡槽，检查漫游状态
            :if ($isRoaming=true) do={
                :log info message="检测到漫游，切换到 SIM UP（漫游）"
                /interface/lte/settings/set sim-slot=up
            }
        } else={
            # 否则使用 “up”（漫游）卡槽，检查漫游状态
            :if (!$isRoaming=true) do={
                :log info message="未漫游，切换到 SIM DOWN（家庭）"
                /interface/lte/settings/set sim-slot=down
            }
        }
    } else={
        :log info message="LTE 接口未连接到网络，等待下一次调度"
    }
} else={
    :log info message="LTE 调制解调器未出现，尝试电源重置"
    /system/routerboard/usb/power-reset duration=5s
}
}

```

### 故障转移脚本示例

现在创建一个将由调度器运行的脚本。此脚本将涵盖几个关键点：

- 检查 LTE 接口是否已初始化（显示在 `/interface/lte` 中），否则，尝试电源重置。
- 检查 LTE 连接是否已建立（接口处于“运行”状态），否则，创建日志条目并等待下一次调度。
- 读取当前使用的 LTE 卡槽，并根据接口状态决定是否更换 SIM 卡。

**注意：** 请记住，仅当当前 SIM 卡无法连接到网络时才会更换卡槽。如果您需要切换回主 SIM 卡，则需要安排另一个操作在特定时间执行此操作。如果不切换回另一张 SIM 卡，则无法知道其是否在服务中。

我们将此脚本命名为“failoverScript”，源代码如下：

```
{
# 设置并读取当前值
:global simSlot [/interface/lte/settings/get sim-slot]
:global timeoutLTE 60
:global timeoutConnect 60

# 等待 LTE 初始化，最长等待 “timeoutLTE” 秒
:local i 0
:local isLTEinit false
:while ($i<$timeoutLTE) do={
    :foreach n in=[/interface/lte/find] do={:set $isLTEinit true}
    :if ($isLTEinit=true) do={
        :set $i $timeoutLTE
    }
    :set $i ($i+1)
    :delay 1s
}

# 检查 LTE 是否已初始化，否则尝试电源重置调制解调器
:if ($isLTEinit=true) do={
    # 等待 LTE 接口连接到移动网络，最长等待 “timeoutConnect” 秒
    :local isConnected false
    :set $i 0
    :while ($i<$timeoutConnect) do={
        :if ([/interface/lte/get [find name="lte1"] running]=true) do={
            :set $isConnected true
            :set $i $timeoutConnect
        }
        :set $i ($i+1)
        :delay 1s
    }
    # 检查 LTE 是否已连接
    if ($isConnected=false) do={
    # 检查当前使用的 SIM 卡槽
        :if ($simSlot="down") do={
            # 如果使用 “down” 卡槽，切换到 “up”
        :log info message="LTE 断开，切换卡槽到 UP"
            /interface/lte/settings/set sim-slot=up
    }
        :if ($simSlot="up") do={
            # 如果使用 “up” 卡槽，切换到 “down”
        :log info message="LTE 断开，切换卡槽到 DOWN"
            /interface/lte/settings/set sim-slot=down
            }
        } else={
            # 否则 “运行” 状态
            :if ($isConnected=true) do={
                :log info message="LTE 已连接"
            } else={
        :log info message="LTE 接口未连接到网络，等待下一次调度"
        }
    } 
    } else={
    :log info message="LTE 调制解调器未出现，尝试电源重置"
    /system/routerboard/usb/power-reset duration=5s
}
}
```

### 设置调度器

最后，创建您的调度器以运行先前创建的脚本。选择合适的调度间隔，以确保两个或多个事件不会相互重叠。对于上述示例，3 分钟就足够了。

```
/system/scheduler/add interval=3m on-event=roamingScript name=Roaming

```

```
/system/scheduler/add interval=3m on-event=failoverScript name=Failover

```

请记住，“家庭” SIM 卡会消耗一些漫游数据，因为 SIM 卡槽的切换并非即时完成。