# TG-LR 设置指南

> 本页面为 MikroTik TG-LR82 和 TG-LR92 LoRaWAN 传感器标签的设置指南，涵盖激活、网络接入、遥测与传感器配置、磁簧开关命令、下行链路命令编码、数据帧及已知问题。

# TG-LR 设置指南

## 快速入门指南

- 在 LoRaWAN 网络服务器上注册设备。如果设备型号不受支持，请使用 [tg-lrx2-2.0-ul-dec.js](pathname:///assets/tg-lrx2-2.0-ul-dec.js) 负载解码器脚本。

- 可选：部署 Grafana + Influx（[telemetry_hub.zip](pathname:///assets/telemetry_hub.zip)）Docker 服务以评估设备功能。

- 将磁铁靠近磁簧开关并等待 2 次 LED 闪烁（约 1.5 秒）以激活设备。

## 功能

新设备处于 SHUTDOWN 模式。请使用磁簧开关命令进行激活。

**表 1 型号**

| 型号 | 描述 | 传感器 |
| --- | --- | --- |
| TG-LR82 | LoRaWAN 1.0.4 Class A、B，863.0 - 869.0 MHz 频段。 | TMP116N、HDC2010、LIS2DW12 |
| TG-LR92 | LoRaWAN 1.0.4 Class A、B，900.0 - 928.0 MHz 频段。 | TMP116N、HDC2010、LIS2DW12 |

**表 2 频段**

| 数字代码 | 名称 | 描述 |
| --- | --- | --- |
| 1 | BAND_1GHz | Sub-GHz 工作频段。频率范围取决于设备型号。 |
| 2 | BAND_2GHz | 2.4GHz ISM 频段。 |

**表 3 工作模式**

| 数字代码 | 模式 | 描述 |
| --- | --- | --- |
| 0 | SHUTDOWN | 设备处于低功耗模式，所有功能禁用。 |
| 1 | RUN | 设备接入网络并根据当前配置文件和设置发送上行链路。 |

**表 4 支持的区域**

| X-Y 代码 | 下行链路 | 通用名称 | TG-LR82 | TG-LR92 |
| --- | --- | --- | --- | --- |
| 1-1 | 1 | EU868 | 是 | |
| 2-1 | 2 | AS923_GRP1 | | 是 |
| 3-1 | 3 | US915 | | 是 |
| 4-1 | 4 | AU915 | | 是 |
| | | WW2G4 | 是 | 是 |
| 6-1 | 7 | AS923_GRP2 | | 是 |
| 7-1 | 8 | AS923_GRP3 | | 是 |
| 8-1 | 9 | IN865 | 是 | |
| 9-1 | 10 | KR920 | | 是 |

### LoRaWAN

设备支持 Class A 和 Class B，可在两个频段工作：BAND_1GHz 和 BAND_2GHz。用户可以配置周期性的链路检查、MAC 时间同步（DeviceTimeReq）和网络 ADR。

#### 接入流程

设备激活（RUN）后将尝试接入网络。设备在主频段发送 Join-Request，如果未收到 Join-Accept，将等待退避间隔后在辅助频段（如果启用）发送下一个 Join-Request，否则再次在主频段发送。

接入尝试间隔取决于上一次 Join-Request 的空中时间和总接入时间。参见 1 节第 7 部分。如果上一次接入请求使用了较慢的数据速率，则预期间隔会更长。

接入配置命令：`lora primary-band`、`lora second-band`、`lora join-cfg`。参见命令编码部分，了解如何将文本命令转换为下行链路的二进制编码。

#### 链路检查

设备接入网络后，可以执行可选的周期性链路检查。可以使用 `lora link-chk` 为每个频段单独配置链路检查。如果链路检查失败，设备将离开网络并重新启动接入流程。

任何网络下行链路都将重置链路检查计时器，以防止不必要的 LinkCheckReq。

#### 时间同步

设备支持使用 DeviceTimeReq MAC 命令进行可选的时间同步。参见 `lora clk-sync` 命令了解配置参数或请求立即同步。

#### Class B

设备支持 Class B 操作。可以使用 `lora class` 手动请求 Class B 操作，也可以使用 `lora cfg-class-b` 配置设备在网络接入时自动切换到 Class B。

#### ADR 配置

可以使用 `lora adr-cfg` 禁用网络 ADR 并设置固定数据速率。

#### 离开网络

如果链路检查或确认上行链路失败，设备将离开网络并重新启动接入流程。

#### 凭据

设备具有出厂配置的默认凭据，随每台设备提供：DevEUI、JoinEUI、AppKey。

DevEUI 和 JoinEUI 是 IEEE 64 位 EUI（2），以 MSB 优先写入。空中字节顺序为 LSB 优先。参见 1 节第 6.2.5 部分。

AppKey 是 16 字节 AES128 加密密钥，按设备内存中存储的方式写入。AppKey 必须保密！

要更改 JoinEUI 和 AppKey，请使用命令：`lora join-eui`、`lora net-key` 和 `lora cred`。命令 `lora join-eui` 和 `lora net-key` 可以按任意顺序多次发出，以写入新的待处理接入凭据。

写入新的待处理凭据后，可以执行 `lora cred 600,1` 或 `app reset 0` 以尝试使用新凭据接入。如果新凭据未通过接入接受确认，设备将恢复为之前的凭据。参见 LORA-275、LORA-276 了解已知问题！

写入 JoinEUI 和 AppKey 并尝试接入的示例序列：

```none
lora join-eui 87904163,0x00,0x16,0xC0,0x01,0xFF,0xFE,0x00,0x00
lora net-key 87904163,0x00,0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F
lora cred 600
app reset 0
// 设备重启并使用新凭据尝试接入，超时时间为 600 秒
```

上一个示例中的 JoinEUI 可以按原样复制/粘贴为 00 16 C0 01 FF FE 00 00 来注册新设备。`lora join-eui` 参数为 MSB 优先。

:::warning
执行 *lora cred &lt;confirm-timeout-s>,87904163* 将强制确认凭据，而无需验证接入尝试！您可能会失去对设备的访问权限！
:::

### 上行链路消息

每个 LoRaWAN 上行链路消息通过将待发送的数据帧 ID 及其内容放入 FPort 和 FRMPayload 字段中形成。所有待发送的帧按升序打包，ID 使用差分编码。

参见 tg-lrx2-2.0-ul-dec.js 脚本了解帧编码细节。此脚本可以直接用于应用服务器的负载解码器。

### 遥测

#### 设备配置文件

设备有 6 个可配置的配置文件。每个配置文件存储独立的传感器和上行链路发送配置。这使得设备能够快速更改工作特性，而无需发送昂贵的下行链路配置消息。可以使用设备命令、磁铁甚至基于评估的数据规则来切换配置文件。例如，在每天几次的周期性保活模式与每几分钟一次的更快速遥测之间切换。

MikroTik 可以支持您的特定用例，提供具有自定义默认配置的新设备。

设备预配置了评估配置，以展示一些可能的用例：

**表 5 默认配置文件配置**

| 配置文件编号 | 名称 | 描述 |
| --- | --- | --- |
| 0 | 传感器遥测 | 每 5 分钟发送 current-state、device-orientation。每 60 分钟发送其余遥测数据。 |
| 1 | 活动监控 | 每 60 分钟发送 activity、full-activity、current-state，并在活动空闲转换时发送 activity_state 事件。 |
| 2 | 磁簧开关 | 每 60 分钟发送 mag-switch、current-state、device-events，并在磁铁移除至少 15 秒时发送 mag_sw_cnt 事件。最多保存 10 个事件。 |
| 3 | 方向 | 每 60 分钟发送 current-state、device-events、device-orientation。在快速旋转 30 度且空闲约 30 秒后发送 device-orientation 帧。在特定方向 V=(0,1,1) 时发送 angle_1 事件。最多保存 3 个事件。 |
| 4 | 资产监控 | 每 3 小时发送资产健康信息，根据事件使用不同的帧。 |
| 5 | 空 | |

参见 default-cfg.txt 了解确切的出厂默认配置命令。

#### 配置传感器

##### 采样间隔

可以使用 `data poll-cfg` 命令为特定用例配置周期性的温度、湿度和电池电压采样。设备可以以高于上行链路帧发送频率的速率采样数据。这提供了发送平均值或执行基于规则的决策的机会。由于采样间隔影响设备功耗，因此可以利用这一点来提高使用寿命。

##### 平均值

设备还跟踪采样值的平均值，包括：temperature_ema、humidity_ema、battery_mv_ema、angle_ema。命令 `data ema-cfg` 配置指数移动平均（EMA）周期，如果启用了 *send-ema-**，还可以在 current-state、dev-health、device-orientation 中发送 EMA 值。

`data ema-cfg` 中的计数参数 *temp-cnt*、*humid-cnt*、*bat-cnt*、*orient-cnt* 决定用于移动平均计算的系数 *a*。移动 EMA 根据前一个值 *ema* 和新值 *sample* 计算如下：

```none
ema(t) = sample(t) * a + ema(t-1) * (1 - a)
```

要获得 EMA 的近似时间常数 *t*，需要使用 `data poll-cfg` 和 `data orient-cfg`（*interval*）配置的采样间隔以及相应的计数参数（*N*）：

```none
t ~ (N + 1) * interval / 2
```

要获得 `data ema-cfg` 所需的计数参数值：

```none
N ~ 2 * t / interval - 1
```

示例：

使用 `data poll-cfg` 将温度采样间隔 *th-poll-int* 配置为 30 秒。要配置时间常数 t ~ 60 分钟的 EMA：

```none
temp-cnt = 2 * 3600 / 30 - 1 = 239
```

假设使用配置文件 #0 并且不想更改其他参数，则需要发送命令：

```none
data ema-cfg 1,239
```

##### 直方图

所有周期性采样都会添加到温度和湿度直方图中。直方图可以作为常规遥测的补充，也可以单独用于监控温度和湿度分布。使用 `data temp-histo-cfg`、`data humid-histo-cfg` 命令配置分箱和周期间隔，和/或启用 temp-histogram、humid-histogram 帧。所有直方图帧都包含周期编号，以检测直方图计数器重置。由于帧大小限制为每个分箱 1B，如果内部分箱计数器值超过 255，直方图将在上行链路中归一化（概率类型）。

示例配置：

```none
data temp-histo-cfg 1,86400,0,0,1,1,-10,0,10,15,17.5,20,22.5,25.0,30
data humid-histo-cfg 1,86400,0,0,1,1,10,20,30,40,50,60,70,80,90
```

##### 方向

![](https://manual.mikrotik.com/docs/internet-of-things/lora/user-guides/img/tg-lrx2-axis.webp)

图 1 设备加速度计轴。

可以使用命令 `data orient-cfg` 配置设备相对于地球的周期性 3D 方向采样。此外，可以配置 3 个用户方向向量 ref-1、ref-2、ref-3 来检测特定的设备方向。用户变量 angle_1、angle_2、angle_3 包含设备上次采样的方向与用户定义向量之间的当前角度。这些变量可以在数据规则中使用，以触发特定方向。angle_ema 是上次采样的设备方向与样本 EMA 值之间的角度。此外，还可以使用 major_axis_orientation 变量获得粗略方向。

**表 6 major_axis_orientation 描述**

| 值 | 数字代码 | 描述 |
| --- | --- | --- |
| XH | 0 | X 向上 |
| HL | 1 | X 向下 |
| YH | 2 | Y 向上 |
| YL | 3 | Y 向下 |
| ZH | 4 | Z 向上 |
| ZL | 5 | Z 向下 |
| DISABLED | 7 | 传感器禁用 |

粗略方向的优点是它可以在 current-state 帧中发送。

##### 活动监控

设备具有基于加速度计的活动监控服务。该服务将自动管理一个简单的状态机来确定运动/活动。activity_s、high_activity_s、total_activity_s 统计每个状态中累积的时间，activity_state、activity_state_etm 保存状态信息。

命令 `data activity-cfg` 可用于配置活动监控的模式和阈值。`data activity-cal` 可用于自动执行特定模式的校准。

*level1-th* 和 *level2-th* 的单位是 *1/64 * 2G*，与其他加速度计设置（如 *data acc-cfg* 中的设置）无关。*level2-cnt* 是内部计算的，用户不可配置。*level2-cnt* 始终在 7..15 范围内，计算如下：

```none
level2-cnt = 7 + round((1 - ((level2-th - level1-th - 1) / 61)) * 8)
```

**表 7 activity_state 描述**

| 数字代码 | 值 |
| --- | --- |
| 0 | IDLE |
| 1 | LOW |
| 2 | HIGH |
| 3 | DISABLED |

###### 单级模式

`data activity-cfg` 中的模式设置为 single。

- 如果任何轴上的加速度计采样值高于 *level1-th*，设备从 IDLE 状态转换到 LOW 状态。

- 如果所有样本在至少 1.3 秒内低于 *level1-th*，设备从 LOW 状态转换到 IDLE 状态。

示例：将配置文件 #0 设置为单级模式，阈值为 0.25G：

```none
data activity-cfg 1,1,8,63
```

###### 双级模式

`data activity-cfg` 中的模式设置为 dual。

在双级模式下，LOW 状态有两个子状态：LOW1 和 LOW2，它们都表示 LOW。设备在这两种状态下都会报告 LOW 状态，并且活动计数器值的递增方式与在 LOW 状态下相同。唯一的区别是这些状态之间的转换逻辑。

**表 8 activity_state 双级模式状态转换**

| 当前 | 下一个 | 条件 |
| --- | --- | --- |
| IDLE | LOW2 | 采样值 > *level1-th* |
| LOW2 | LOW1 | 采样值 &lt; *level2-th* 至少 5 秒 |
| LOW1 | LOW2 | 采样值 > *level1-th* |
| LOW2 | HIGH | 采样值 > *level2-th* 至少 *level2-cnt* 次 |
| LOW1 | IDLE | 采样值 &lt; *level1-th* 至少 5 秒 |
| HIGH | LOW1 | 采样值 &lt; *level2-th* 至少 5 秒 |

示例：将配置文件 #0 设置为双级模式，阈值为 0.25G 和 0.5G：

```none
data activity-cfg 1,2,8,16
```

###### 校准

除了手动配置 *level1-th* 和 *level2-th* 之外，还有活动校准功能。执行命令 `data activity-cal` 将自动校准 *cal-level*。*level-one* 将校准 *level2-th*，*level-two* 将校准 *level2-th*，适用于 *profile-mask* 中选择的所有配置文件。对于双级模式，可以依次运行 *level-one* 和 *level-two*。校准时间为 15 秒。此功能主要适用于周期性运动/振动。

在校准过程或活动监控测试期间启用 LED 以确保正确操作可能很有用。

示例：校准配置文件 #0 并使用单级活动监控：

:::warning
在启用方向检测的情况下进行活动校准会导致故障和设备重启。请在校准前使用 `data orient-cfg` 禁用方向检测，并在完成后重新启用。参见 LORA-279。
:::

- 将设备放置在具有周期性运动/活动的环境中进行校准。

- 发送命令：

```none
data activity-cfg 1,1,,,1
data activity-cal 1,1,1
```

- 观察 LED 周期性闪烁 2 次/1.5 秒，持续约 15 秒。

- 测试运动检测。在 LOW 活动期间，设备将闪烁 LED 3 次/1 秒。

- 如果校准结果可接受，发送命令禁用 LED：

```none
data activity-cfg 1,,,,0
```

示例：校准配置文件 #0 并使用双级活动监控：

- 将设备放置在具有周期性运动/活动的环境中进行级别 1 校准。

- 发送命令：

```none
data activity-cfg 1,2,,,1
data activity-cal 1,1,1
```

- 观察 LED 周期性闪烁 2 次/1.5 秒，持续约 15 秒。

- 将设备放置在环境中进行级别 2 校准。

- 发送命令校准级别 2：

```none
data activity-cal 1,2,1
```

- 观察 LED 周期性闪烁 2 次/1.5 秒，持续约 15 秒。

- 测试运动检测。在 HIGH 活动期间，设备将闪烁 LED 6 次/1 秒。

- 如果校准结果可接受，发送命令禁用 LED：

```none
data activity-cfg 1,,,,0
```

校准后，可以使用命令 `data activity-cfg` 手动更改 *level1-th* 和 *level2-th*。

##### 冲击和自由落体

命令 `data acc-cfg` 可用于配置设备加速度计以进行基本的冲击和自由落体检测。帧：motion-events、impact-count 包含相关数据字段。current-state 包含指示新事件的 impact_evnt、free_fall_evnt 标志。如果更倾向于显式读取，可以使用这些标志。

变量 impact_cnt、impact_cnt_x、impact_cnt_y、impact_cnt_z、impact_etm、free_fall_cnt、free_fall_etm 允许基于规则的逻辑。

如果启用了活动监控，则无法使用冲击和自由落体检测，并将被忽略。

#### 数据规则

最多可配置 32 条自定义用户规则，使用命令：`data set-rule`、`data del-rule`。规则具有测试表达式、可选的输入规则和要执行的操作。

添加或覆盖规则的命令语法：

```none
data set-rule [<rule-num>],<test-expr>,[<input-expr>],[<switch-profile>],[<make-event-0>],[<make-event-1>], [<make-event-2>],[<make-event-3>],[<send-frame-0>],[<send-frame-1>],[<send-frame-2>],[<send-frame-3>],[<clr-timer-mask>]
```

##### 测试表达式

&lt;test-expr>: [^] variable-type &lt;operator> &lt;argument>

| [^] | 在表达式中使用变量绝对值 |
| --- | --- |
| variable-type | 变量名称或 ID |
| &lt;operator> | >、>=、&lt;、&lt;=、==、!=、% |
| &lt;argument> | 数值 |

示例：

```none
data set-rule 0,profile == 0
data set-rule 1,^temperature > 30.55
data set-rule 2,impact_etm < 60
```

可以使用用户变量的数字 ID 给出相同的规则：

```none
data set-rule 0,0 == 0
data set-rule 1,^8 > 30.55
data set-rule 2,24 < 60
```

##### 输入表达式

如果规则需要依赖于其他规则的结果，则使用输入表达式。这允许基于多个测试表达式构建复杂的逻辑。

&lt;input-expr>: [&][|][!]&lt;input-rule>[&lt;]

| [&] | &lt;rule-num> 和 &lt;input-rule> 的逻辑与 |
| --- | --- |
| [\|] | &lt;rule-num> 和 &lt;input-rule> 的逻辑或 |
| [!] | 输入值的逻辑非 |
| &lt;input-rule> | 作为输入添加的规则编号 |
| [&lt;] | 使用规则的组合状态作为输入值，否则使用本地状态。 |

以下配置将在磁簧开关状态改变不到 15 秒且温度或湿度超出范围（-5..55 和 10..90%）时发送 current-state 数据帧：

```none
data del-rule
data set-rule 0,temperature < -5
data set-rule 1,temperature > 55
data set-rule 2,humidity < 10
data set-rule 3,humidity > 90,|0|1|2
data set-rule 4,mag_sw_etm < 15,&3<,,,,,,current-state
```

无论 set-rule 命令中的顺序如何，输入规则都按数字顺序评估。

##### 操作

规则测试表达式的评估值代表数据规则的本地状态。使用可选输入规则评估的本地状态代表组合状态。

如果组合状态变为 TRUE 状态，则执行可选的规则操作：配置文件切换、事件生成、帧调度、用户计时器重置。

如果提供了 &lt;switch-profile> 参数，将更改当前配置文件。例如，如果温度降至 15 摄氏度以下，设备将切换到配置文件 5（设备配置文件）：

```none
data set-rule 1,temperature < 15,,5
```

每条规则最多可以调度 4 个不同的数据帧：

```none
data set-rule 0,impact_cnt % 10,,,,,,,current-state,device-orientation,dev-health,ema-temp
```

如果需要发送超过 4 个帧，可以使用规则链。

每条规则最多可以生成 4 个不同的事件：

```none
data set-rule 0,impact_cnt % 10,,,temperature_ema,humidity_ema,activity_state,timer_1
```

##### 事件

操作可以选择性地生成事件。事件是带时间戳的用户变量，在 device-events 帧中发送。可以使用 `data event-cfg` 命令配置事件存储。如果设备已通过时间同步接收到绝对时间，事件将具有 POSIX 时间戳。这允许收集特定的历史数据以供以后报告。事件上行链路可以周期性地、基于某些规则或使用下行链路命令手动触发。

### 磁簧开关

设备具有磁簧开关，可用于命令输入或作为磁场传感器。如果未使用，可以使用 `mag svc` 命令完全禁用命令输入或使用 PIN 保护。

每台设备都附带唯一的 PIN 码。

#### 命令输入

用户必须应用 1 到 4 位数字的命令序列。每位数字依次输入。空闲 2.5 秒后，执行有效的输入命令，设备使用 LED 指示结果。成功执行的命令以 3 次 0.2 秒的 LED 闪烁指示，失败则以 1 秒长的 LED 脉冲指示。无效命令将被忽略。

当磁场施加到设备时，LED 开始以 500ms 亮、500ms 灭的间隔闪烁（或根据 `mag cfg` 配置的 blink-mode）。当 LED 亮起时，内部计数器从 0 开始递增。当磁场移除时，计数器值被锁存为用户输入的数字。如果再次施加磁场，则开始输入序列中的下一位数字。如果施加数字后的间隔大于 2.5 秒，则评估该序列。

根据时间应用输入代码时，请确保遵循以下等式：T = N - 0.5，其中 N 是 1 到 9 的输入数字，T 是施加磁场的时间（秒）。数字之间的间隔必须小于 2.5 秒，但大于 200 毫秒。

某些命令需要进入 PIN 模式，某些命令可以选择性地受 PIN 模式保护。参见表 磁簧开关命令。要进入 PIN 模式，用户必须应用设备附带的 PIN 数字序列。进入 PIN 模式后，它将在可配置的时间后过期，设备将返回正常模式。

也可以完全禁用磁铁命令。重新启用的唯一方法是使用 LoRaWAN 下行链路命令。如果磁铁传感器仅用于检测外部信号，并且不希望或不允许用户命令，这可能很有用。

**表 9 磁簧开关命令**

| 序列 | PIN 模式 | 命令描述 |
| --- | --- | --- |
| 2 | 可选 | 激活 - 启用 RUN 模式。 |
| 3-1 | 可选 | 触发 current-state 帧上行链路。 |
| 4-1-X | 可选 | 切换设备配置文件，其中 X 是配置文件编号 + 1 [1..6]。 |
| 4-2-1 | 可选 | 将主频段设置为 BAND_1GHz。 |
| 4-2-2 | 可选 | 将主频段设置为 BAND_2GHz。 |
| 4-3-1 | 可选 | 启用辅助频段。 |
| 4-3-9 | 可选 | 禁用辅助频段。 |
| 6-1 | 可选 | 设备重启。 |
| 6-2-9 | 可选 | 停用设备 - SHUTDOWN 模式。 |
| 9-X-Y | 可选 | 根据支持的区域设置 sub-GHz 频段的区域。 |
| 6-9-9 | 强制 | 设备恢复出厂设置。 |
| 3-1-5 | 强制 | 退出 PIN 模式。 |
| A-B-C-D | – | 进入 PIN 模式。A-B-C-D 是设备出厂 PIN 码的数字。 |
| 5-3-1 | 可选 | 保留。 |

数字输入期间的 LED 指示可以根据设备配置进行更改。可以使用 `mag cfg` 更改或完全禁用 LED 指示。

#### 磁铁传感器

磁传感器始终工作（即使应用了命令）。该传感器可用于检测切换事件 mag_sw_flag 或计算这些事件的数量 mag_sw_cnt。设备可以报告当前开关状态、状态更改次数以及最后的时间戳（UNIX/运行时间）mag_switch_ts。此外，您可以根据这些属性创建规则。

### 命令编码

设备命令被二进制编码以减小下行链路消息大小。我们提供 Python 实用程序来验证、编码和发布命令作为 LoRaWAN 二进制下行链路消息。

[tg-lrx2-utils.zip](pathname:///assets/tg-lrx2-utils.zip) 或使用 *pip install tg-lrx2-utils* 安装

示例配置：设置 current-state 和 activity 帧每 600 秒上行链路，mag-switch 每 43200 秒上行链路，作为确认消息：

```none
# lora-script.txt
frame set-cfg 1,601,0,0,current-state,activity
frame set-cfg 1,43200,1,0,mag-switch
```

我们可以使用 *tg-lrx2-encode* 将文本命令转换为用于下行链路的二进制消息：

```none
tg-lrx2-encode --script ./lora-script.txt --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
```

[tg-lrx2-2.0-desc.yml](pathname:///assets/tg-lrx2-2.0-desc.yml) 包含完整的设备描述，供其他工具使用。确保为特定设备和 FW 版本使用正确的文件！

*lora-pub.yml* 将包含用于下行链路的序列化二进制负载。您可以手动使用可用的 Web 工具调度它们，或使用 *tg-lrx2-pub* 在 The Things Network 上调度它们：

```none
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

示例 TTN 凭据文件：

```none
# ttn-app.yml
app-id: "ttn-tag-demo@ttn"
host: "eu1.cloud.thethings.industries"
port: 1883
user: "ttn-tag-demo@ttn"
password: "NNSXS.5G..."
```

*tg-lrx2-encode* 也接受 CLI 上的命令字符串。这可用于单行或几行命令：

```none
tg-lrx2-encode --cmd $'frame send device-orientation\napp profile 1,0' --dev-desc ./tg-lrx2-2.0-desc.yml --max-len=50 --out ./lora-pub.yml
tg-lrx2-pub --host ./ttn-app.yml --dl-msg ./lora-pub.yml device-id
```

### 设备命令

所有设备命令由 *group-name* 和 *cmd-name* 组成。可选参数在方括号中给出。对于 *tg-lrx2-encode* 脚本，参数必须用逗号分隔。*group-name* 和 *cmd-name* 也可以用逗号分隔，但也接受空格。

示例：

```none
app factory-reset <key>,[<fw-def>],<delay-ms>
```

参数 &lt;key> 和 &lt;delay-ms> 是必需的，但 &lt;fw-def> 是可选的，可以省略：

```none
app factory-reset 984651411,,2500
```

每个参数都有有效的输入范围和格式。某些参数只允许在特定选项之间或范围之间进行选择。

大多数参数接受整数值。*%f* 表示参数接受小数值。使用这些值会导致更大的下行链路负载，因此如果可能，应优先使用整数值。variable-type 表示参数接受用户变量名称或相应的整数 ID。frame-type 表示参数接受数据帧名称或整数 ID。*tg-lrx2-encode* 会自动将这些名称转换为数字 ID。

#### app set-mode

| app set-mode &lt;mode> | | |
| --- | --- | --- |
| 设置设备工作模式 | | |
| 参数 | 范围 | 描述 |
| mode | 0 | SHUTDOWN |
| | 1 | RUN |

#### app profile

| app profile &lt;profile-num>,&lt;make-default> | | |
| --- | --- | --- |
| 切换活动配置文件并可选择设为默认 | | |
| 参数 | 范围 | 描述 |
| profile-num | 0..5 | |
| make-default | 0 | 否 |
| | 1 | 是 |

#### app reset

| app reset &lt;type> | | |
| --- | --- | --- |
| 系统重置 | | |
| 参数 | 范围 | 描述 |
| type | 0 | 主板 |
| | 1 | 仅应用 |

#### app factory-reset

| app factory-reset &lt;key>,[&lt;fw-def>],&lt;delay-ms> | | |
| --- | --- | --- |
| 重启设备，清除已保存的配置并设置为默认值（可选） | | |
| 参数 | 范围 | 描述 |
| key | 984651411 | |
| fw-def | 784565141 | 不应用默认配置 |
| delay-ms | 0..65535 | |

#### app led

| app led [&lt;enable>] | | |
| --- | --- | --- |
| 配置应用 LED 信号 | | |
| 参数 | 范围 | 描述 |
| enable | 0 | 否 |
| | 1 | 是 |

#### app set-time

| app set-time [&lt;unix-time-s>],&lt;uptime-s> | | |
| --- | --- | --- |
| 设置相对于设备运行时间的 UNIX 时间 | | |
| 参数 | 范围 | 描述 |
| unix-time-s | 0..4294967295 | |
| uptime-s | 0..4294967295 | |

#### lora set-region

| lora set-region &lt;region-code> | | |
| --- | --- | --- |
| 设置 sub-GHz 频段的 LoRaWAN 区域 | | |
| 参数 | 范围 | 描述 |
| region-code | 1 | EU868 |
| | 2 | AS923-1 |
| | 3 | US915 |
| | 4 | AU915 |
| | 7 | AS923-2 |
| | 8 | AS923-3 |
| | 9 | IN868 |
| | 10 | KR920 |

#### lora primary-band

| lora primary-band &lt;band> | | |
| --- | --- | --- |
| 选择主频段 | | |
| 参数 | 范围 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |

#### lora second-band

| lora second-band &lt;mode> | | |
| --- | --- | --- |
| 启用或禁用辅助频段 | | |
| 参数 | 范围 | 描述 |
| mode | 0 | 关闭 |
| | 1 | 开启 |

#### lora join-cfg

| lora join-cfg &lt;band>,&lt;duty> | | |
| --- | --- | --- |
| 配置频段的接入占空比 | | |
| 参数 | 范围 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| duty | 0 | 0.1% |
| | 1..254 | |
| | 255 | 1% |

#### lora link-chk

| lora link-chk &lt;band>,&lt;int-minutes> | | |
| --- | --- | --- |
| 设置频段特定的链路检查间隔和超时 | | |
| 参数 | 范围 | 描述 |
| band | 1 | &lt;1GHz |
| | 2 | 2.45GHz |
| int-minutes | 0 | 关闭 |
| | 5..500000 | |

#### lora adr-cfg

| lora adr-cfg &lt;en-netw-adr>,[&lt;fixed-data-rate>] | | |
| --- | --- | --- |
| 启用网络 ADR 或配置固定数据速率 | | |
| 参数 | 范围 | 描述 |
| en-netw-adr | 0 | 关闭 |
| | 1 | 开启 |
| fixed-data-rate | 0..6 | |

#### lora clk-sync

| lora clk-sync [&lt;int-minutes>],[&lt;leap-sec>],&lt;sync-now>,[&lt;retry-s>],[&lt;retry-cnt>] | | |
| --- | --- | --- |
| 绝对时间同步 | | |
| 参数 | 范围 | 描述 |
| int-minutes | 0 | 关闭 |
| | 1..65535 | |
| leap-sec | -128..127 | |
| sync-now | 0 | 否 |
| | 1 | 是 |
| retry-s | 0..255 | |
| retry-cnt | 0..255 | |

#### lora cfg-class-b

| lora cfg-class-b [&lt;auto-en>],[&lt;ping-slot-int-s>] | | |
| --- | --- | --- |
| 配置 LoRaWAN Class B | | |
| 参数 | 范围 | 描述 |
| auto-en | 0 | 关闭 |
| | 1 | 开启 |
| ping-slot-int-s | 1 | |
| | 2 | |
| | 4 | |
| | 8 | |
| |