# GPIO

> GPIO 允许在 MikroTik 路由器上配置数字和模拟输入/输出引脚，用于电压测量、干接点感应和继电器控制等任务。设置通过 `/iot/gpio` 下的 CLI 进行管理，包含模拟和数字引脚的子菜单，并支持电压偏移调整。

# GPIO

***注意**：要访问 GPIO 设置，请确保已提前安装 **iot** [软件包](../../getting-started/installation-and-upgrade/packages)。*

您可以通过以下[链接](https://en.wikipedia.org/wiki/General-purpose_input/output)了解更多关于 GPIO 的信息。

GPIO 代表通用输入/输出。它是路由器板上的数字信号引脚，允许您发送/接收信号。它在不同场景中非常有用，例如：

1. 通过 ADC 输入测量电压。
2. 读取从另一设备接收到的 0 和 1 信号 - “干接点”。
3. 通过向引脚发送逻辑 0 或 1 信号来控制连接的继电器。

:::info
[KNOT](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77)、[KNOT Embedded LTE4](https://mikrotik.com/product/knot_embedded_lte4) 和 [RBM33G](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G) 支持 GPIO 功能。

- [KNOT 引脚定义可在此处找到](https://help.mikrotik.com/docs/spaces/UM/pages/41680915/RB924i-2nD-BT5+BG77#RB924i2nDBT5%26BG77-GPIOpinout)。
- [KNOT Embedded LTE 4 引脚定义，请点击此处。](https://help.mikrotik.com/docs/spaces/UM/pages/366477381/KNOT+Embedded+LTE4+EC25-EU+KNe#KNOTEmbeddedLTE4EC25EU%26KNe-GPIOpinout)
- [RBM33G 引脚定义，请点击此处](https://help.mikrotik.com/docs/spaces/UM/pages/14222434/RBM33G#RBM33G-GPIOpinout)。

:::

### RouterOS 配置

**GPIO 设置仅可通过 CLI 使用。**

**子菜单：** `/iot/gpio`

GPIO 设置分为：

- 模拟（/iot/gpio/analog）
- 数字（/iot/gpio/digital）

:::warning
在我们的示例中，我们使用 [KNOT](https://mikrotik.com/product/knot) 作为参考设备（具有 x2 个模拟输入引脚、x2 个数字输出引脚和 x1 个数字输入引脚）。其他设备可能具有不同的引脚定义，但原理相同。
:::

#### 模拟引脚

**子菜单：** `/iot/gpio/analog`

***注意**：请在产品页面上检查您的硬件是否支持模拟输入。

在“analog”设置中，您可以测量模拟输入/ADC 输入引脚上的电压：

```ros
[admin@device] /iot/gpio/analog> print
 # NAME                                                                                     VALUE       OFFSET
 0 pin2                                                                                       0mV          0mV
 1 pin3                                                                                      32mV          0mV
```

“OFFSET”可用于手动补偿导线上的电压降。“VALUE”通过 `value = adc_input + offset` 计算，其中 adc\_input 是引脚上的电压。

“OFFSET”配置示例如下：

```ros
[admin@device] /iot/gpio/analog> set pin2 offset  

Offset ::= [-]Num[mV]
  Num ::= -2147483648..2147483647    (整数)

[admin@device] /iot/gpio/analog> set pin2 offset 2   
[admin@device] /iot/gpio/analog> print            
 # NAME                                                                                           VALUE       OFFSET
 0 pin2                                                                                             2mV          2mV
 1 pin3                                                                                             0mV          0mV 
```

#### 数字引脚

**子菜单：** `/iot/gpio/digital`

在“digital”部分，您可以使用数字输出/输入引脚发送/接收逻辑 0 或 1 信号（输出引脚为“开漏”）：

```ros
[admin@device] /iot/gpio/digital> print             
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                   
 0   pin5                                        input     0      0    
 1   pin4                                        output    0     
 2   pin6                                        output    0     
```

引脚的“DIRECTION”可以是“input”（可以接收信号的引脚）或“output”（可以发送信号的引脚）。

:::info
[KNOT](https://mikrotik.com/product/knot) 的 pin4 和 pin6 的“DIRECTION”无法更改。这两个引脚仅设计用作“output”引脚。
:::

当引脚方向设置为“output”时，您可以配置“OUTPUT”值。更改“OUTPUT”值会向引脚发送信号。

```ros
[admin@device] /iot/gpio/digital> set pin4 output=

Output ::= 0 | 1

[admin@device] /iot/gpio/digital> set pin4 output=1        
[admin@device] /iot/gpio/digital> print            
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0    
 1   pin4                                        output    1     
 2   pin6                                        output    0     
```

“script”字段允许您配置一个脚本，该脚本将在“INPUT”或“OUTPUT”值发生变化时（从 0 到 1 或从 1 到 0）被触发。

```ros
[admin@device] /iot/gpio/digital> set pin4 script=script1
[admin@device] /iot/gpio/digital> set pin5 script="/system .."   
[admin@device] /iot/gpio/digital> print                       
Flags: X - disabled 
 #   NAME                                        DIRECTION OUTPUT INPUT SCRIPT                                      
 0   pin5                                        input     0      0     /system ..                                  
 1   pin4                                        output    1            script1                                     
 2   pin6                                        output    0     
```

### 不同场景

#### 控制继电器

GPIO 实现的一个场景是使用数字输出引脚“控制其他继电器”。基本上，向连接到引脚的设备发送“0”或“1”信号。为了自动化该过程，您可以使用[调度器](../../system-information-and-utilities/scheduler)，它将在特定时间运行脚本。

例如，您可以添加第一个[脚本](../../developer-guides/scripting/)（如下所示单行）并将其命名为“output=0”：

```ros
/iot/gpio/digital set pin4 output=0
```

然后添加第二个脚本（如下所示单行）并将其命名为“output=1”：

```ros
/iot/gpio/digital set pin4 output=1
```

拥有这两个脚本后，您可以配置一个调度计划：

```ros
[admin@device] /system/scheduler> add name=run-30s interval=30s on-event="output=0"
```

上述调度配置将每 30 秒运行名为“output=0”的脚本。

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="output=1"
```

上述调度配置将每 45 秒运行名为“output=1”的脚本。

因此，设备将自动每 30 秒向第 4 个引脚（数字输出引脚）发送一个输出值=0 的信号，每 45 秒发送一个输出值=1 的信号。

您可以根据需要（取决于要求）更改调度时间。

#### 监控输入信号

另一个场景是使用数字输入引脚“监控输入信号”。您需要一个脚本，当方向为“input”的引脚的“INPUT”值发生变化时（即 RouterOS 设备从连接到引脚的另一设备接收到“0 或 1”信号时），该脚本将触发电子邮件通知或 MQTT/HTTPS（fetch）发布。

*电子邮件通知脚本：*

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="$[/iot/gpio/digital/get pin5 input]"
```

创建脚本后，将其应用/设置到“input”引脚：

```ros
[admin@device] /iot/gpio/digital> set pin5 script=script1 
[admin@device] /iot/gpio/digital> print                  
Flags: X - disabled 
 #   NAME                     DIRECTION OUTPUT INPUT SCRIPT                    
 0   pin5                     input     0      0     script1                   
 1   pin4                     output    0            script1                   
 2   pin6                     output    0     
```

在上面的示例中，电子邮件通知脚本被命名为“script1”。

因此，每当输入值发生变化（从 0 到 1 或从 1 到 0）时，脚本会自动触发一封电子邮件通知，该通知将在邮件正文中显示输入值。

不要忘记更改脚本行并相应地配置电子邮件设置（[/tool/e-mail](../../system-information-and-utilities/e-mail)：

```ros
/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="$[/iot/gpio/digital/get pin5 input]"
```

配置您实际使用的电子邮件地址。您也可以根据需要更改邮件的主题和正文。

*MQTT 发布脚本：*

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"inputVALUE\":$[/iot/gpio/digital/get pin5 input]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

此脚本的工作方式与“*电子邮件通知*”脚本相同，只是当输入值发生变化时，脚本会触发 MQTT 发布（而不是电子邮件通知），并以 JSON 格式发送引脚上接收到的输入值。

不要忘记提前设置 MQTT 代理（*`/iot/mqtt/brokers/add` ..*）并修改几行脚本：

```ros
:local broker "name"
```

代理的“name”应相应更改（您可以使用 CLI 命令 `/iot/mqtt/brokers/print` 检查所有已创建的代理及其名称）。

```ros
:local topic "topic"
```

主题也应更改。主题本身在服务器端配置，因此请确保使用正确的主题。

不要忘记将脚本应用/设置到 pin5（/iot/gpio/digital/set pin5 script=script\_name），如上面的“电子邮件通知”示例所示。

如果使用机械开关向 GPIO 引脚发送信号，建议改用以下脚本（以防在引脚接收到信号时脚本被触发多次）：

```ros
:global gpioscriptrunning;  
if (!$gpioscriptrunning) do=\{:set $gpioscriptrunning true;  
:log info "script started - GPIO changed";  
:do \{if ([/iot/gpio/digital/get pin5 input] = "0") do=\{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]" body="pin5 received logical 0"} else \{/tool/e-mail/send to="config@mydomain.com" subject="$[/system/identity/get name]"  body="pin5 received logical 1"};  
:delay 1s;  
:set $gpioscriptrunning false} on-error=\{:set $gpioscriptrunning false;  
:log info "e-mail error, resetting script state..."}}
```

如果 GPIO 引脚状态在毫秒/微秒内变化多次 - 上述脚本将确保电子邮件通知不会发送多次。

#### 监控电压

最后但同样重要的是使用模拟引脚“监控电压”。您需要一个脚本，按计划读取/监控电压，然后通过电子邮件、MQTT 或 HTTPS（fetch）发送数据。

创建一个脚本，如下所示。在此示例中，我们将使用 MQTT 发布（但您可以创建类似的脚本，使用“/tool/e-mail ..”来使用电子邮件通知）：

```ros
:local broker "name"
:local topic "topic"
:local message "\{\"voltage(mV)\":$[/iot/gpio/analog/get pin3 value]}"  
/iot/mqtt/publish broker=$broker topic=$topic message=$message
```

该脚本将读取/测量 pin3 上的电压并将数据发布到 MQTT 代理。

不要忘记提前设置 MQTT 代理（*`/iot/mqtt/brokers/add` ..*）并修改几行脚本：

```ros
:local broker "name"
```

代理的“name”应相应更改（您可以使用 CLI 命令 `/iot/mqtt/brokers/print` 检查所有已创建的代理及其名称）。

```ros
:local topic "topic"
```

主题也应更改。主题本身在服务器端配置，因此请确保使用正确的主题。

保存脚本并将其命名为，例如，“voltagepublish”。为了自动化该过程，您可以使用[调度器](../../system-information-and-utilities/scheduler)。

```ros
[admin@device] /system/scheduler> add name=run-45s interval=45s on-event="voltagepublish"
```

上述调度配置将每 45 秒运行该脚本。