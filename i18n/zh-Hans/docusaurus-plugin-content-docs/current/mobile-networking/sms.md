# SMS

> 本文档介绍 MikroTik RouterOS 中的 SMS 功能，支持通过 AT 命令利用 GSM 调制解调器发送和接收短信。内容涵盖发送方法、端口、电话号码、消息编码等参数，以及用于与网络运营商交互的 USSD 消息支持。

# SMS

## 概述

可以将 GSM 调制解调器连接到 RouterOS 设备，并使用其发送和接收短信。RouterOS 将此类调制解调器列为串行端口，显示在 `/port/print` 列表中。GSM 标准定义了用于发送短信的 AT 命令，并规定了这些命令中消息的编码方式。`'/tool/sms/send'` 使用标准的 GSM AT 命令发送短信。

## 发送

**子菜单：** `/tool/sms/send`

### **示例**

为 ppp 接口发送命令：

```ros
/tool/sms/send usb3 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#\$%^&*(){}[]\"'~"
```

对于 LTE 接口，请在端口字段中使用 LTE 接口名称：

```ros
/tool/sms/send lte1 "20000000" \ message="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#\$%^&*(){}[]\"'~"
```

| 参数 | 描述 |
| :-- | :-- |
| **port** (*字符串*) | GSM 调制解调器所连接的 `/port` 中的端口名称。 |
| **phone-number** (*字符串*) | 接收方电话号码。允许的字符为 "0123456789\*#abc"。如果第一个字符是 "+"，则电话号码类型设置为 *国际*，否则设置为 *未知*。 |
| **channel** (*整数*) | 用于发送的调制解调器通道。 |
| **message** (*字符串*) | 消息内容。使用 GSM 7 编码（目前不支持 UCS2），因此消息长度限制为 160 个字符。字符 `^{}\\[]~` 是扩展的 GSM 7 位字符，每个占用两个字符槽位，存在时会减少有效限制至 160 以下。 |
| **smsc** (*字符串*) |  |
| **type** (*字符串*) | 如果设置为 *class-0*，则发送类 0 短信。该消息会立即显示，不会存储在手机中。 |
| **sms-storage** (*字符串*) | 选择存储接收短信的位置（调制解调器/SIM 卡） |
| **status-report-request** (*是 \| 否*; 默认值：**是**) | 设置为 "否" 以不请求确认消息，该消息指示文本消息是否成功发送给接收方。 |

## USSD 消息

USSD（非结构化补充服务数据）消息可用于与移动网络运营商通信，以获取额外信息、启用附加服务或为预付费卡充值。USSD 消息可通过 AT 命令处理（命令可能因调制解调器而异，甚至在某些调制解调器上被阻止）。

**必须激活 3G 或 GSM 网络模式才能使用此功能**，因为 LTE 单独模式下不支持（**R11e-LTE** 调制解调器会自动切换到 3G 模式以发送 USSD 消息）。

PDU（协议数据单元）消息及其解密版本会在 LTE 调试日志中打印。

### **示例**

检查 LTE 调试日志是否激活：

```ros
/system/logging/print
Flags: X - disabled, I - invalid, * - default 
# TOPICS ACTION PREFIX 
0 * info memory 
1 * error memory 
2 * warning memory 
3 * critical echo 
```

如果没有日志条目，请运行以下命令添加：

```ros
/system/logging/add topics=lte,!raw

/system/logging/print
Flags: X - disabled, I - invalid, * - default 
# TOPICS ACTION PREFIX 
0 * info memory 
1 * error memory 
2 * warning memory 
3 * critical echo 
4 lte,!raw memory 
```

要从 **\*245#** 接收账户状态：

```ros
/interface/lte/at-chat lte1 input="AT+CUSD=1,\"*245#\",15"
output: OK
/log/print
11:51:20 lte,async lte1: sent AT+CUSD=1,"*245#",15 
11:51:20 lte,async lte1: rcvd OK 
11:51:23 lte,async,event +CUSD: 0,"EBB79B1E0685E9ECF4BADE9E03", 0 
11:51:23 gsm,info USSD: konta atlikums
```

## 接收

RouterOS 还支持接收短信，可以执行脚本，甚至回复发送者。

在路由器接收短信之前，需要在 `/tool/sms` 菜单中进行相关配置。以下参数可配置：

| 参数 | 描述 |
| :-- | :-- |
| **allowed-number** (*字符串*; 默认值：**""**) | 允许运行命令的发送者号码，必须指定国家代码，例如 +371XXXXXXX |
| **channel** (*整数*; 默认值：**0**) | 用于接收的调制解调器通道。 |
| **keep-max-sms** (*整数*; 默认值：**0**) | 将保存的最大消息数。如果设置的值大于 SIM 卡支持的数量，新消息将无法接收。从 RouterOS v6.44.6 开始，由 `auto-erase` 参数替代。 |
| **auto-erase** (*是 \| 否*; 默认值：**否**) | 自动读取 SIM 存储大小。当 `auto-erase=no` 时，如果存储已满，将不会接收新短信。设置 `auto-erase=yes` 可自动删除最旧的已接收短信以释放空间接收新短信。自 v6.44.6 起可用。 |
| **port** (*字符串*; 默认值：**未知**) | 调制解调器端口（调制解调器只能由一个进程使用 "/port> print"） |
| **receive-enabled** (*是 \| 否*; 默认值：**否**) | 必须开启才能接收消息 |
| **secret** (*字符串*; 默认值：**""**) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | 秘密密码，必填 |
| **polling** (*是 \| 否*; 默认值：**否**) | 每 10 秒检查调制解调器是否有新短信，而不是仅在收到调制解调器命令后更新收件箱。自 v7.16 起可用。 |
| **sim-pin** (*字符串*; 默认值：) *[敏感参数](../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* | SIM 卡的 PIN 码。 |

### 查看接收消息的基本示例配置

```ros
/tool/sms/set receive-enabled=yes port=lte1

/tool/sms/print 
           status: running
  receive-enabled: yes
             port: lte1
          channel: 0
           secret: 
   allowed-number: 
       auto-erase: no
          sim-pin: 
        last-ussd: 
```

### **收件箱**

**子菜单：** `/tool/sms/inbox`

如果已启用读取器，您将在此子菜单中看到传入消息：

只读属性：

| 属性 | 描述 |
| :-- | :-- |
| **phone** (*字符串*) | 发送者的电话号码。 |
| **message** (*字符串*) | 消息正文 |
| **timestamp** (*时间*) | 消息接收的时间。这是运营商发送的时间，而非路由器的本地时间。 |
| **type** (*字符串*) | 消息类型 |

### **语法**

```ros
 :cmd SECRET script NAME [[ VAR[=VAL] ] ... ]
```

- **SECRET** - 密码
- **NAME** - `/system/script` 中可用的脚本名称
- **VAR** - 传递给脚本的变量（可以作为 VAR 或 VAR=value 传递），以空格分隔。

其他注意事项：

- \*参数如有必要，可以放在引号中 "VAR"="VAL"。
- \*不支持值的转义（VAR="\""）。
- \*不支持合并短信，每条短信将被单独处理。
- \*不支持 16 位 Unicode 消息。
- \*短信使用标准 GSM7 字母表解码，因此不能使用其他编码发送，否则将被错误解码。

### **示例**

#### 错误

```ros
:cmd script mans_skripts
:cmd slepens script mans skripts
:cmd slepens script mans_skripts var=
:cmd slepens script mans_skripts var= a
:cmd slepens script mans_skripts var=a a
```

#### 正确

```ros
:cmd slepens script mans_skripts
:cmd slepens script "mans skripts"
:cmd slepens script mans_skripts var
:cmd slepens script mans_skripts var=a
:cmd slepens script mans_skripts var="a a" 
```

## 调试

`/tool/sms/send` 命令会记录写入和读取的数据。日志标签为 *gsm,debug,write* 和 *gsm,debug,read*。更多信息请参阅 `/system/logging`。

## 实现细节

使用 *AT+CMGS* 和 *AT+CMGF* 命令。端口在命令执行期间被占用，不能同时被其他 RouterOS 组件使用。消息发送过程可能需要较长时间。在初始 AT 命令交换期间，超时时间为 1 分钟，之后为 2 秒。