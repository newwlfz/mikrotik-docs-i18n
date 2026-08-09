# Kid Control（儿童控制）

> Kid Control 是 RouterOS 的一项功能，通过设置每日互联网访问时间表、带宽限制以及基于配置文件和防火墙规则的设备特定限制，实现对局域网设备的家长控制。

# Kid Control（儿童控制）

**子菜单：** `/ip/kid-control`

“儿童控制”是一项家长控制功能，用于限制局域网设备的互联网连接。

## 属性说明

在此菜单中，可以为每个孩子创建配置文件并限制其互联网访问权限。

| 属性 | 说明 |
| :-- | :-- |
| **name** (*字符串*) | 孩子配置文件的名称 |
| **mon,tue,wed,thu,fri,sat,sun** (*时间*) | 一周中的每一天。允许互联网访问的每日时间段 |
| **disabled** (*是 \| 否*) | 配置文件是否被禁用 |
| **rate-limit** (*字符串*) | 流的最大可用数据速率 |
| **tur-mon,tur-tue,tur-wed,tur-thu,tur-fri,tur-sat,tur-sun** (*时间*) | 不限速时间段。互联网访问不受限制的每日时间段 |

不限速时间参数优先级高于 rate-limit 参数。

## 设备

**子菜单：** `/ip/kid-control/device`

此子菜单包含有关是否有多个设备连接到互联网（手机、平板电脑、游戏机、电视等）的信息。设备通过从 ARP 表中获取的 MAC 地址进行识别，相应的 IP 地址也从该表中获取。

| 属性 | 说明 |
| :-- | :-- |
| **name** (*字符串*) | 设备名称 |
| **mac-address** (*字符串*) | 设备的 MAC 地址 |
| **user** (*字符串*) | 要将设备附加到的配置文件 |
| **reset-counters** (*[id, name]*) | 重置 bytes-up 和 bytes-down 计数器。 |

## 应用示例

通过以下示例，我们将限制 Peter 手机的访问权限：

- 在周一、周三和周五禁用互联网访问
- 允许不限速的互联网访问：
  - 周二
  - 周四 11:00-22:00
  - 周日 15:00-21:00
- 在周六 18:30-22:00 将 Peter 手机的带宽限制为 3Mbps

```ros
[admin@MikroTik] > /ip/kid-control/add name=Peter mon="" tur-tue="00:00-24h" wed="" tur-thu="11:00-22:00" fri="" sat="18:30-22:00" tur-sun="15h-21h" rate-limit=3M
[admin@MikroTik] > /ip/kid-control/device/add name=Mobile-phone user=Peter mac-address=FF:FF:FF:ED:83:63
```

互联网访问限制是通过添加动态防火墙过滤规则或简单队列规则来实现的。以下是防火墙过滤规则示例：

```ros
[admin@MikroTik] > /ip/firewall/filter/print

1  D ;;; Mobile-phone, kid-control
      chain=forward action=reject src-address=192.168.88.254 

2  D ;;; Mobile-phone, kid-control
      chain=forward action=reject dst-address=192.168.88.254
```

动态创建的简单队列：

```ros
[admin@MikroTik] > /queue/simple/print
Flags: X - disabled, I - invalid, D - dynamic 

 1  D ;;; Mobile-phone, kid-control
      name="queue1" target=192.168.88.254/32 parent=none packet-marks="" priority=8/8 queue=default-small/default-small limit-at=3M/3M max-limit=3M/3M burst-limit=0/0 
      burst-threshold=0/0 burst-time=0s/0s bucket-size=0.1/0.1  
```

可以监控特定设备使用了多少数据：

```ros
[admin@MikroTik] > /ip/kid-control/device/print stats

Flags: X - disabled, D - dynamic, B - blocked, L - limited, I - inactive 
 #    NAME                                                                                                                 IDLE-TIME    RATE-DOWN   RATE-UP   BYTES-DOWN     BYTES-UP
 1 BI Mobile-phone                                                                                                               30s         0bps      0bps    3438.1KiB       8.9KiB
```

还可以**暂停**已创建孩子的互联网访问；这将限制所有访问，直到使用**恢复**功能，之后将按照配置的设置继续执行：

```ros
[admin@MikroTik] > /ip/kid-control/pause Peter 
[admin@MikroTik] > /ip/kid-control/print
Flags: X - disabled, P - paused, B - blocked, L - rate-limited 
 #   NAME                                                                                                                    SUN      MON      TUE      WED      THU      FRI      SAT     
 0 PB Peter                                                                                                                 15h-21h                             11h-22h          18:30h-22h  
```