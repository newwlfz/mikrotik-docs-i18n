# GPS

> 本文档介绍 MikroTik RouterOS 中 GPS 的配置与监控，涵盖频道选择、坐标格式、GPS 初始化字符串等属性，以及带日期时间、纬度/经度、海拔、卫星数和数据时效等参数的监控命令。

import DocCardList from '@theme/DocCardList';

# GPS

本章节涵盖 GPS 追踪示例，用于将 RouterOS GPS 数据发送至 HTTP 端点、MQTT 代理及 IoT 平台。

<DocCardList />

### 概述

**软件包要求：** `gps`
**子菜单：** `/system/gps`
**标准：** `GPS, NMEA 0183, Simple Text Output Protocol`

全球定位系统（GPS）用于确定 GPS 接收器的精确位置。

### 配置属性

| 属性 | 说明 |
| :-- | :-- |
| **channel** (*整数 [0..4294967295]*；默认值：**0**) | 设备使用的端口通道 |
| **coordinate-format** (*dd \| dms \| ddmm*；默认值：**dms**) | 使用的坐标格式："十进制度"、"度分秒"或"NMEA 格式 DDDMM.MM[MM]" |
| **enabled** (*yes \| no*；默认值：**no**) | 是否启用 GPS |
| **gps-antenna-select** (*external \| internal*；默认值：**internal**) | 取决于设备型号。如果设备内置天线，可选择使用内部天线。 |
| **init-channel** (*整数 [0..4294967295]*；默认值：) | 执行初始化字符串的通道 |
| **init-string** (*字符串*；默认值：) | GPS 初始化的 AT 初始化字符串 |
| **port** (*字符串*；默认值：) | GPS 接收器所连接的 USB/串口名称 |
| **set-system-time** (*yes \| no*；默认值：**no**) | 是否将路由器的日期和时间设置为 GPS 接收到的值。 |

### 监控状态

**命令：** `/system/gps/monitor`

此命令用于监控从 GPS 接收器接收到的数据。

**参数：**

:::warning
从 7.1rc3 固件版本开始，新增了一个名为 "data-age"（以秒为单位）的参数。该参数显示自设备收到最后一条 NMEA 消息以来经过的时间。
:::

| 属性 | 说明 |
| :-- | :-- |
| **date-and-time** (*日期*) | 从 GPS 接收到的日期和时间 |
| **latitude** (*none \| 字符串*) | 以 DM（十进制度分）格式表示的纬度 |
| **longitude** (*none \| 字符串*) | 以 DM（十进制度分）格式表示的经度 |
| **altitude** (*none \| 字符串*) | 基于 GPS 数据的海拔高度 |
| **speed** (*none \| 字符串*) | GPS 设备当前的移动速度 |
| **destination-bearing** (*none \| 字符串*) | 从当前位置朝向已配置目的地航点的方位角 |
| **true-bearing** (*none \| 字符串*) | 相对于真北的当前航向 |
| **magnetic-bearing** (*none \| 字符串*) | 相对于磁北的当前航向 |
| **valid** (*yes \| no*) |  |
| **satellites** (*整数*) | 设备可见的卫星数量。 |
| **fix-quality** (*整数*) | 信号质量 |
| **horizontal-dilution** (*小数*) | 水平精度因子（HDOP）； |
| **data-age** (整数) | 自设备收到最后一条 NMEA 消息以来经过的时间 |

### 基本示例

检查端口使用情况，因为同一时间只能有一个实例使用串口：

```ros
[admin@MikroTik] /port/print
Flags: I - inactive 
 #   DEVICE NAME                     CHANNELS USED-BY                   BAUD-RATE
 0          serial0                         1 Serial Console            auto    
```

如果只有一个端口且被控制台占用，请从控制台菜单中释放它：

```ros
[admin@MikroTik] > /system/console/print 
Flags: X - disabled, U - used, F - free
 #   PORT                                                                       TERM                                                                     
 0 U serial0                                                                    vt102 

[admin@MikroTik] > /system/console/disable 0   
```

根据您的设备调整端口设置（LtAP mini 请保留 "auto"）：

```ros
[admin@MikroTik] /port> set 0 baud-rate=4800 parity=odd
[admin@MikroTik] /port> print detail 
Flags: I - inactive 
 0   name="usb1" used-by="" channels=1 baud-rate=4800 data-bits=8 parity=odd stop-bits=1 flow-control=none
```

启用 GPS：

```ros
[admin@MikroTik] /system/gps> set enabled=yes port=usb1
[admin@MikroTik] /system/gps> print 
          enabled: yes
             port: usb1
          channel: 0
     init-channel: 0
      init-string:
  set-system-time: no
```

监控状态：

```ros
[admin@MikroTik] /system/gps> monitor  
        date-and-time: 2021-09-07 08:26:26
             latitude: 56.969689
            longitude: 24.162471
              altitude: 25.799999 m
                speed: 0.759320 km/h
  destination-bearing: none
         true-bearing: 185.500000 deg. True
     magnetic-bearing: 0.000000 deg. Mag
                valid: yes
           satellites: 6
          fix-quality: 1
  horizontal-dilution: 1.3
```

## **LtAP** 的端口和 GPS 设置

```ros
/port/set serial1 baud-rate=115200
```

```ros
/system/gps/set port=serial1 channel=0 enabled=yes
```

我们还编写了一篇关于使用脚本和 Web 服务器进行实时 GPS 追踪的深入文章：[GPS-tracking](./gps-tracking-using-http-post.md)。

### 故障排除

请注意，有时为了让 GPS 模块在 RouterOS 中被识别，您需要在 `/port` 菜单中更改波特率设置。

[LtAP mini](https://mikrotik.com/product/ltap_mini) 内置低增益 GPS 天线，为获得更好的体验，我们建议使用额外的[外置天线](https://mikrotik.com/product/acgpsa)。

在 GPS 菜单下切换内部和外部天线：

```ros
[admin@MikroTik] > /system/gps/set gps-antenna-select=external
```

在某些支持 GPS 的调制解调器上，您需要发送多条初始化命令以实现持续 GPS 监控，例如，对于华为网卡，您需要发送 "AT^WPDST=1,AT^WPDGP" 初始化字符串以获得持续监控。