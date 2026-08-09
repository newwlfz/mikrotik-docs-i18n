# 使用 GPIO 作为来自计量设备的脉冲输入

> 利用 MikroTik 设备的 GPIO 作为脉冲输入，通过 RouterOS 脚本计数脉冲，以读取水表、电表或其他计量表的数据。

某些水表、电表或其他计量设备具有脉冲输出功能。计量设备的规格说明会描述多少个脉冲代表一个整数计量单位。例如，我们编写本手册时使用的电表每产生 1000 个脉冲代表 1kWh，因此每个脉冲相当于 1Wh。您可以使用 KNOT 的数字 GPIO 输入（引脚5）来读取这些脉冲，并计算电表后消耗的电能。为此，需要搭建一个简单的 MOSFET 电路，并按照下图连接所有部件：

![](https://manual.mikrotik.com/docs/internet-of-things/gpio/img/circuit.png)

下一步是编写一个 RouterOS 脚本，该脚本在每次接收到脉冲时执行：

```bash
/iot gpio digital
set pin5 script=":global scriptRunning; :global pulse;\
:if (\$scriptRunning!=true) do={\
:set \$scriptRunning true;\
:set \$pulse (\$pulse+1);\
:log info message=(\"GPIO pulse No. \".\$pulse);\
:delay 1s;\
:set \$scriptRunning false;\
}"
```

当 GPIO 配置完成后，上述脚本将在每次脉冲时创建一条日志记录：

```bash
15:32:22 script,info GPIO pulse No. 1 
15:38:01 script,info GPIO pulse No. 2 
15:43:38 script,info GPIO pulse No. 3 
15:49:15 script,info GPIO pulse No. 4 
15:54:51 script,info GPIO pulse No. 5 
16:00:27 script,info GPIO pulse No. 6 
16:06:02 script,info GPIO pulse No. 7 
16:11:37 script,info GPIO pulse No. 8 
16:17:12 script,info GPIO pulse No. 9 
16:22:48 script,info GPIO pulse No. 10 
```