# BG77 调制解调器 AT 命令

> 本简短指南将帮助您了解如何排查 CAT-M/NB-IoT 连接的问题。通过调制解调器的“AT”命令可以获取大量与连接相关的信息。根据定义，“AT”意为“注意”。每条命令字符串均以“AT”为前缀，并且可以在“AT”之后连接多个独立的命令。

#

# 概述

本简短指南将帮助您了解如何排查 CAT-M/NB-IoT 连接的问题。通过调制解调器的“AT”命令可以获取大量与连接相关的信息。根据定义，“AT”意为“注意”。每条命令字符串均以“AT”为前缀，并且可以在“AT”之后连接多个独立的命令。

请参考以下示例，以更好地理解如何发起这些命令以及通过它们可以获取哪些信息。

:::info
移动网络由 ISP 管理。如果连接出现任何问题，我们建议您事先联系 ISP，并确认他们首先支持/允许该连接或相关设置。如果您决定（在不咨询 ISP 的情况下）使用 AT 命令更改配置，风险自负。
:::

## 发起 AT 命令

### 选项 A

要发送命令，您必须使用 CLI。

打开终端并输入以下内容：

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2
```

请注意所使用的端口和通道。选择 PPP-OUT 接口所使用的端口和通道。在我们的示例中，端口为“modem”，数据通道为“2”。

命令发起后，应显示以下输出，您可以在其中输入 AT 命令：

```ros
[admin@MikroTik] > system serial-terminal port=modem channel=2

[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

在上面的示例中，使用了 AT 命令“at+cpin?”，并收到了应答“+CPIN: READY”。

### 选项 B

发送 AT 命令的第二种方式是通过 ppp-client 接口：

```ros
[admin@MikroTik] > interface ppp-client at-chat input="AT+CPIN\?"
number: 0
  output: +CPIN: READY
```

您可以得到与**选项 A** 相同的结果。

## AT 命令

### at

简单的 ***at*** 命令用于检查模块（设备）与应用程序之间的通信。

```ros
[Ctrl-A is the prefix key]

at

OK 
```

当返回“OK”时，表示模块已成功响应。

### at+cpin?

此命令用于检查 SIM 卡的状态。

```ros
[Ctrl-A is the prefix key]

at+cpin?
+CPIN: READY

OK 
```

状态“+CPIN: READY”表示 SIM 卡已正确安装。

如果使用了 SIM PIN 码，您应收到应答“+CPIN: SIM PIN”→ 在这种情况下，您可以通过命令 ***at+cpin="xxxx"*** 解锁，其中 ***xxxx*** 是 PIN 码。

如果您收到响应“+CME ERROR: SIM not inserted”→ 请仔细检查 SIM 卡是否正确安装在 SIM 卡槽中。

### at+cfun?

“CFUN”命令用于检查功能模式。此命令可能有不同的响应。

```ros
[Ctrl-A is the prefix key]   

at+cfun?
+CFUN: 1

OK
```

当状态为“+CFUN: 1”时，表示设备设置为全功能模式。建议使用此模式。

在其他许多响应中，例如，您可能会得到“+CFUN: 4”，这表示设备设置为飞行模式，其中 Tx、Rx、LTE 和 GNSS 服务均被禁用。

您可以使用命令 ***at+cfun=1*** 手动将模式设置为全功能模式。

### at+cops?

**at+cops?** 命令用于检查当前网络连接。

```ros
[Ctrl-A is the prefix key]      

at+cops?
+cops: 0,0,"LMT",8

OK
```

以上面的示例为参考，我们可以看到响应为“0,0,"LMT",8”。

响应中的第一个值表示使用的是“自动”还是“手动”模式。当 ISP 连接设置为“自动”时，该值将显示“0”。当 ISP 连接设置为“手动”时，该值将显示“1”。

响应中的第二个值表示 ISP 名称的格式。如果为“0”，则表示 ISP 名称采用“长格式字母数字”。如果为“1”，则表示 ISP 名称采用“短格式字母数字”。

响应的第三部分是 ISP 名称本身。

响应的第四部分表示所使用的技术。“8”代表 eMTC (CAT-M)，“9”代表 NB-IoT。

### at+cops=?

**at+cops=?** 用于获取所有可用 ISP 的列表。此命令可能需要一些时间（约 1 分钟）才能显示结果。

```ros
[Ctrl-A is the prefix key]      

at+cops=?
+cops: (1,"LMT","LMT","24701",9),(2,"LMT","LMT","24701",8),,(0,1,2,3,4),(0,1,2)

OK
```

您可以通过命令 ***at+cops=mode,format,"provider"*** 手动设置您希望连接的 ISP，其中 ***mode*** 是使用的模式（0→ 自动网络选择；1→ 手动网络选择），**format** 是 ISP 名称格式（0→ 长字母数字格式；1→ 短字母数字格式；2→ 数字格式），而“***provider***”是 ISP 名称（采用所选格式）。例如，要从列表中手动选择网络，请使用命令 ***at+cops=1,1,"LMT"***。

要自动选择 ISP，请使用命令 ***at+cops=0***。

### at+creg?

***at+creg?*** 命令用于检查网络的注册状态。

```ros
[Ctrl-A is the prefix key]              

at+creg?
+CREG: 0,1

OK
```

第一个值表示网络注册主动结果代码是启用还是禁用（0→ 禁用，1→ 启用；2→ 启用 + 位置信息）。第二个值表示电路域注册状态（0→ 未注册/设备未在搜索要注册的运营商；1→ 已注册/归属网络；2→ 未注册，但正在尝试搜索要注册的运营商；3→ 注册被拒绝；4→ 未知；5→ 已注册且正在漫游）。

如果返回的值超过 2 个，则表示网络注册和位置信息主动结果代码已启用。第二个值将显示十六进制格式的两位位置区码，第三个值将显示十六进制格式的四位 GERANE/E-UTRAN 小区 ID，最后一个值将显示服务小区的接入技术（“8”代表 CAT-M，“9”代表 NB-IoT）。

### at+csq

***at+csq*** 命令返回接收信号强度指示（RSSI）和信道误码率（BER）值。此命令仅在网络注册完成后才会返回正确的值。

```ros
[Ctrl-A is the prefix key]           

at+csq
+csq: 25,99

OK
```

第一个值是 RSSI (dBm)：

| 值 | RSSI |
| --- | --- |
| 0 | -113 dBm 或更低 |
| 1 | -111 dBm |
| 2-30 | -109 至 -53 dBm |
| 31 | -51 dBm 或更高 |
| 99 | 未知/不可检测（未找到网络） |

第二个值是 BER (%)：

| 值 | BER |
| --- | --- |
| 0 | &lt; 0,2 % |
| 1 | 0,2 % &lt; 0,4 % |
| 2 | 0,4 % &lt; 0,8 % |
| 3 | 0,8 % &lt; 1,6 % |
| 4 | 1,6 % &lt; 3,2 % |
| 5 | 3,2 % &lt; 6,4 % |
| 6 | 6,4 % &lt; 12,8 % |
| 7 | 12,8 % &lt; |
| 99 | 未知/不可检测 |

根据示例/输出“***+csq: 25,99***”，结果转换为 RSSI~63 dBm，BER 参数不可检测。

### at+qnwinfo

该命令返回有关接入技术、ISP 和所选频段的信息。此命令仅在网络注册完成后才会返回正确的信息。

```ros
[Ctrl-A is the prefix key]              

at+qnwinfo
+QNWINFO: "eMTC","24701","LTE BAND 20",6300

OK
```

根据上面的示例，您可以看到当前模块使用“eMTC”（CAT-M），ISP 为“24701”（数字格式，代表“LMT”），LTE Band 20，信道 ID 为“6300”。

### at+qcsq

**at+qcsq** 命令返回当前 ISP 连接的信号强度以及所使用的技术信息。

```ros
[Ctrl-A is the prefix key]                 

at+qcsq
+QCSQ: "eMTC",-62,-87,111,-12

OK
```

返回的第一个参数是“eMTC”，它显示了模块所使用的技术（CAT-M）。如果无法确定网络（不确定）→ 将返回“NOSERVICE”。

其余参数显示连接的信号强度。

当技术被识别为“NBIoT”或“eMTC”（CAT-M）时：

- 第一个数值显示接收信号强度（LTE RSSI）；
- 第二个数值显示参考信号接收功率（LTE RSRP）；
- 第三个数值显示信号与干扰加噪声比（LTE SINR）→ 该值显示为 SINR 的对数值，该值是 1/5 dB（结果范围在 0-250 之间，转换为 -20 dB 至 +30 dB 的范围）；
- 第四个数值显示参考信号接收质量（LTE RSRQ）。
根据上面的示例，RSSI=-62 dBm，RSRP=-87 dBm，SINR=111(111/5-20)~2 dB，RSRQ=-12 dB。

### at+qcfg="iotopmode"?

该命令用于检查用于连接 ISP 的技术。调制解调器可以仅工作在 CAT-M 模式、仅工作在 NB-IoT 模式，或同时工作在两种模式。

```ros
[Ctrl-A is the prefix key]   

at+qcfg="iotopmode"?
+QCFG: "iotopmode",2

OK
```

您可以使用命令 ***at+qcfg="iotopmode"****,****mode***,***effect*** 将 SIM 卡锁定为仅工作在特定模式，其中*** mode*** 是模式（0→ 仅 CAT-M；1→ 仅 NB-IoT；2→ 两者），***effect*** 是生效时间（0→ 重启后生效；1→ 立即生效）。

为了加快网络搜索速度，建议先执行命令 ***at+cfun=0***（关闭射频），然后使用所述命令。之后，执行 ***at+cfun=1,1***（重新打开射频并重置模块以使更改生效）。

### at+qcfg="band"?

此命令用于检查当前接受的频段/频率。

```ros
[Ctrl-A is the prefix key]   

at+qcfg="band"?
+QCFG: "band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f

OK
```

“qcfg”响应中的第一个值是一个十六进制值，指定了 **GSM 频段**。此值与 Quectel BG77 模块无关。可以忽略此值。

第二个十六进制值指定 **CAT-M 频段**（即 0x100002000000000f0e189f）。如果设置为 0，则表示不更改频段。例如，如果为 0x15，则表示 → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5)。

| 值 | 频段 |
| --- | --- |
| 0 | 不更改 |
| 0x1 | LTE Band 1 |
| 0x2 | LTE Band 2 |
| 0x4 | LTE Band 3 |
| 0x8 | LTE Band 4 |
| 0x10 | LTE Band 5 |
| 0x80 | LTE Band 8 |
| 0x800 | LTE Band 12 |
| 0x1000 | LTE Band 13 |
| 0x20000 | LTE Band 18 |
| 0x40000 | LTE Band 19 |
| 0x80000 | LTE Band 20 |
| 0x1000000 | LTE Band 25 |
| 0x2000000 | LTE Band 26 |
| 0x4000000 | LTE Band 27 |
| 0x8000000 | LTE Band 28 |
| 0x20000000000000000 | LTE Band 66 |
| 0x1000000000000000000000 | LTE Band 85 |
| 0x100002000000000F0E189F | 上述所有支持的频段 |

最后一个十六进制值指定 **NB-IoT 频段**（即 0x10004200000000090e189f）。如果设置为 0，则表示不更改频段。例如，如果为 0x15，则表示 → 0x01(LTE Band 1)+0x04(LTE Band 3)+0x10(LTE Band 5)。

| 值 | 频段 |
| --- | --- |
| 0 | 不更改 |
| 0x1 | LTE Band 1 |
| 0x2 | LTE Band 2 |
| 0x4 | LTE Band 3 |
| 0x8 | LTE Band 4 |
| 0x10 | LTE Band 5 |
| 0x80 | LTE Band 8 |
| 0x800 | LTE Band 12 |
| 0x1000 | LTE Band 13 |
| 0x20000 | LTE Band 18 |
| 0x40000 | LTE Band 19 |
| 0x80000 | LTE Band 20 |
| 0x1000000 | LTE Band 25 |
| 0x8000000 | LTE Band 28 |
| 0x20000000000000000 | LTE Band 66 |
| 0x400000000000000000 | LTE Band 71 |
| 0x1000000000000000000000 | LTE Band 85 |
| 0x10004200000000090E189F | 上述所有支持的频段 |

您可以使用命令 ***at+qcfg="band",GSM_band,CAT_M_band,NB_IoT_band,effect*** 更改频段，其中 ***GSM_band*** 是 GSM 频段（可保留为 0x0），***CAT_M_band*** 是 CAT-M 频段，***NB_IoT_band*** 是 NB-IoT 频段，***effect*** 是立即生效（1）还是模块重启后生效（0）。

要将模块设置为支持所有频段，请使用命令：

```ros
[Ctrl-A is the prefix key]     

at+qcfg="band",0x0,0x100002000000000f0e189f,0x10004200000000090e189f,1

OK
```

为了加快网络搜索速度，建议先执行命令 ***at+cfun=0***（关闭射频），然后使用所述命令。之后，执行 ***at+cfun=1,1***（重新打开射频并重置模块以使更改生效）。

### at+qgpscfg="priority",(0-1)

需要理解的是，通过 CAT-M/NB-IoT 进行的数据传输和 GNSS 无法同时工作（BG77 模块中的 WWAN 和 GNSS 接收链共享某些硬件模块，这意味着该模块不支持 WWAN 和 GNSS 的并发操作）。这就是引入 ***at+qgpscfg="priority",(0-1)*** 命令的原因。

可以通过以下命令更改优先级：

```ros
[Ctrl-A is the prefix key]    

at+qgpscfg="priority",0

OK

at+qgpscfg="priority",1

OK
```

***at+qgpscfg="priority",0*** 命令设置 **GNSS 为最高优先级**。

***at+qgpscfg="priority",1*** 命令设置 **LTE (WWAN) 为最高优先级**。

当设备处于 **LTE (WWAN) 优先模式**时，仅当 RRC 被释放（无线资源控制协议具有多种功能，但主要负责连接建立及其释放功能）且 LTE (WWAN) 进入空闲休眠模式时，GNSS 定位请求才能成功通过。只有在 eDRX 受支持且未被 ISP 阻止的情况下，LTE (WWAN) 和 GNSS 才能在 **LTE (WWAN) 优先模式**下共存。如果网络连接已建立（RRC 处于连接状态）并且数据开始流向服务器 → GNSS 将被推迟，直到数据传输结束且 RRC 被释放。如果 eDRX 受支持且模块进入此模式（数据传输结束）→ 将发送 GNSS 坐标。一旦数据再次开始流向服务器，GNSS 将被推迟，直到设备再次进入 eDRX 模式。

当设备处于 **GNSS 优先模式**时，GNSS 定位请求在所有 WWAN 状态下均能成功。如果设备处于 RRC 连接状态 → 它将释放 RRC 连接并启动 GNSS 会话。之后，如果有 WWAN 数据需要发送 → 将再次发起 RRC 连接。