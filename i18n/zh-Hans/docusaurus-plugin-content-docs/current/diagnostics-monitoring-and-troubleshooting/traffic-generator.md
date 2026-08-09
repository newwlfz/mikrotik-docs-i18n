# 流量生成器

> 流量生成器是 MikroTik RouterOS 的一款工具，用于通过端口生成和发送原始数据包来评估设备性能，并收集延迟、抖动、吞吐量和数据包丢失数据。它支持乱序检测和 PCAP 注入等高级功能，并提供可配置属性和命令以快速设置。

# 流量生成器

流量生成器是一款允许评估 DUT（被测设备）或 SUT（被测系统）性能的工具。

该工具可以通过特定端口生成并发送原始数据包。它还会收集延迟和抖动值、TX/RX 速率、统计丢失的数据包，并检测乱序（OOO）数据包。

流量生成器的使用方式类似于 [带宽测试](./bandwidth-test.md) 工具，也可以生成将被路由回数据包生成器的数据包，以进行高级状态收集。

:::info
在生成数据包的设备上，将无法使用嗅探器工具、torch 或防火墙在出接口上捕获由流量生成器生成的数据包。

由于此工具可能被恶意使用，可以通过输入命令 `/system/device-mode/update traffic-gen=no` 并随后按住重置按钮来锁定此功能。
:::

## 常规

**子菜单：** `/tool/traffic-generator`

此菜单允许设置常规的流量生成器属性，并包含用于快速启动和停止该工具的命令。

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **latency-distribution-max** (*时间*; 默认值：**100us**) | 延迟分布测量的最大延迟范围。基于此值，RouterOS 将决定使用哪个延迟范围作为 latency-distribution-measure-interval 属性 |
| **measure-out-of-order** (*是 \| 否*; 默认值：) | 是否测量乱序数据包。默认值基于 CPU 类型（多核 CPU 默认 **否**；单核 CPU 默认 **是**）。在多核设备上启用此属性时，单个流将仅使用单个 CPU 核心 |
| **stats-samples-to-keep** (*整数*; 默认值：**100**) | 要收集的数据样本数量 |
| **test-id** (*整数 [0..255]*; 默认值：**0**) |  |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **latency-distribution-samples** (*整数*) | 显示 latency-distribution-measure-interval 被划分成的独立时间段数量 |
| **latency-distribution-measure-interval** (*时间*) | 显示总延迟测量范围 |
| **running** (*是 \| 否*) | 显示流量生成器工具是否已启动。 |

### 命令

| 属性 | 描述 |
| :-- | :-- |
| **quick** () | 此命令允许您快速启动数据包生成器并将统计输出打印到终端。该命令还接受多个参数，这些参数会覆盖数据包模板和流设置中的配置。接受的参数包括 **duration、entries-to-show、freeze-frame-interval、id、interface、mbps、measure-out-of-order、packet-count、packet-size、port、pps、stream、test-id、tx-template**。tx-template - 用于生成流量的数据包模板（最多 16 个模板）duration - 测试运行时长entries-to-show - 打印到终端的状态行数freeze-frame-interval - 状态更新到终端的频率其余参数非命令特有，将在其他部分描述。运行 quick 命令时指定的参数会覆盖已配置的值。如果某个参数仅为某个头部指定，则该值会（在需要时）乘以所有其他头部的数量。 |
| **start** () | 命令在后台启动流量生成器工具。它接受一个参数 **test-id** |
| **stop** () | 命令停止由 **start** 命令启动的流量生成器工具。 |
| **inject** () | 将原始数据注入接口。 |
| **inject-pcap** () | 直接从 PCAP 或 PCAPNG 文件注入原始数据。**重要提示：** 从 RouterOS 7.20 开始，[嗅探器工具](./packet-sniffer.md) 以 PCAPNG 格式保存捕获的数据包。流量生成器的 inject-pcap 功能从 RouterOS 7.21 开始支持 PCAPNG 格式。 |

## 数据包模板

**子菜单：** `/tool/traffic-generator/packet-template`

此子菜单允许根据提供的参数构建数据包。基于这些参数，您可以构建带有 VLAN 标签的 IP 数据包并设置 UDP 端口。根据提供的参数生成原始数据包模板。

如果您需要更底层的报文或希望充分利用流量生成器，请使用原始数据包模板构建器来构建报文。

如果同一类型的头部在数据包中出现多次，则头部字段值以逗号分隔的列表形式传递。（例如，如果有两个 IP 头部，则源地址表示为 "IP-src=1.1.1.1,2.2.2.2"）。

为加快头部构建速度，许多头部字段值会被自动假定。例如，如果头部堆栈是 "mac, IP"，则流量生成器可以假定 mac-protocol 值为 "IP"。或者，如果指定了 "port" 或 "interface" 设置，流量生成器可以假定 "mac-src" 为接口的 MAC 地址。假定的值具有以 "assumed-" 开头的不同名称，并且是只读的。手动指定的值会覆盖假定的值。

:::info
假定的值不会自动更新。在模板编辑后会假定新值。执行 "packet-template set 0" 足以触发新假定值的生成。
:::

| 属性 | 描述 |
| :-- | :-- |
| **comment** (*字符串*; 默认值：) | 对您正在构建的数据包的简短描述。 |
| **compute-checksum-from-offset** (*无校验和 \| 整数[0..4294967295]*; 默认值：) | 指定从数据包中哪个字节偏移量开始计算 2 字节校验和（示例：设置为 14，以在计算校验和时跳过数据包的以太网头部） |
| **data** (*递增 \| 随机 \| 特定字节 \| 未初始化*; 默认值：**未初始化**) | 指定数据包负载的填充方式：uninitialized - 数据包数据（头部之后）未初始化，但不为零。最快。specific-byte - 与设置 data-byte 配合使用incrementing - 数据包数据填充为 "00 01 02 03" 等random - 数据包数据填充为随机字节。最慢。 |
| **data-byte** (*十六进制 [0..FF]*; 默认值：**0**) | 用于填充数据包负载的字节。 |
| **interface** (*字符串*; 默认值：) | 数据包模板的可选参数。这与 "port" 设置互斥。指定 "interface" 允许用户无需在端口菜单中为接口创建端口条目。实际上，端口条目是动态创建的。这对于运行快速测试非常有用。 |
| **ip-dscp** (*整数[0..255] 列表（最多 16 次）*; 默认值：) | 将在 IP 头部中设置的单个或列表 DS 字段（DS 字段包含 DSCP 值和 ECN 值） |
| **ip-dst** (*IP/网络掩码 列表（最多 16 次）*; 默认值：) | 生成 IP 头部时使用的目标 IP 地址列表。 |
| **ip-frag-off** (*整数[0..65535] 列表（最多 16 次）*; 默认值：) | IP 头部中的分片偏移列表。 |
| **ip-gateway** (*IP*; 默认值：) | 在发送方和接收方为同一设备的情况下，无法根据 **ip-dst** 自动确定下一跳。如果指定了 ip-gateway，数据包模板将根据解析出的 ip-gateway 假定目标 MAC 地址。 |
| **ip-id** (*整数 [0..65535] 列表*; 默认值：) |  |
| **ip-protocol** (*IP 协议列表（最多 16 次）*; 默认值：) |  |
| **ip-src** (*IP/掩码 列表（最多 16 次）*; 默认值：) |  |
| **ip-ttl** (*整数 [0..255] 列表（最多 16 次）*; 默认值：) |  |
| **mac-dst** (*MAC/掩码 列表（最多 16 次）*; 默认值：) |  |
| **mac-protocol** (*MAC 协议列表（最多 16 次）*; 默认值：) |  |
| **mac-src** (*MAC/掩码 列表（最多 16 次）*; 默认值：) |  |
| **name** (*字符串*; 默认值：) | 模板的描述性名称。 |
| **port** (*字符串*; 默认值：) | 数据包模板的可选参数。这建议了使用此模板生成的数据包应通过哪个端口发送。端口也可以在其它地方（如流设置中）指定。这与 interface 设置互斥。 |
| **raw-header** (*字符串（最多 16 次）*; 默认值：) | 十六进制格式的原始数据包头部字符串。 |
| **udp-dst-port** (*端口 [0..65535]/掩码 [0..FFFF] 列表（最多 16 次）*; 默认值：) |  |
| **udp-src-port** (*端口 [0..65535]/掩码 [0..FFFF] 列表（最多 16 次）*; 默认值：) |  |
| **vlan-id** (; 默认值：) |  |
| **vlan-priority** (; 默认值：) |  |
| **vlan-protocol** (; 默认值：) |  |
| **header-stack** (*ip \| mac \| raw \| udp \| vlan 列表（最多 16 次）*; 默认值：**ip**) | 生成的数据包应具有的头部序列。目前支持：mac - 以太网头部（14 字节）vlan - 以太网 VLAN 标签（4 字节）ip - IPv4 头部（20 字节）udp - UDP 头部（8 字节）raw - 指定为十六进制字符串的任意字节大多数头部类型可以在数据包中出现多次。每个数据包只能有 2 个 IP 头部和 1 个 UDP 头部。根据我们在网络协议方面的实践经验，对可能的头部序列施加了一些限制（例如，VLAN 头部只能跟在 MAC 头部或另一个 VLAN 头部之后）。流量生成器会为数据包模板建议第一个头部（在端口菜单中）。但这并非强制性的。 |

## 端口配置

**子菜单：** `/tool/traffic-generator/port`

此菜单允许配置与特定接口关联的端口，这些端口将用于接收/发送生成的数据包。

**属性**

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*是 \| 否*; 默认值：**否**) | 端口是否被禁用，不参与接收/发送数据包 |
| **name** (*字符串*; 默认值：) | 端口的描述性名称 |
| **interface** (*字符串*; 默认值：) | 与端口关联的接口名称。 |

### 只读属性

| 属性 | 描述 |
| :-- | :-- |
| **dynamic** (*是 \| 否*) | 端口配置是否自动生成。 |
| **first-header** (*ip \| mac \| raw \| udp \| vlan*) | 显示从指定接口发送数据包的建议第一个头部。此信息可用于创建数据包模板时。 |
| **inactive** (*是 \| 否*) | 端口是否处于非活动状态，无法参与数据包的 tx/rx。 |

## 统计

**子菜单：** `/tool/traffic-generator/stats`

如果流量生成器未以 **quick** 模式运行，则有关测试的所有统计信息都存储在此菜单中。

### 延迟分布

**子菜单：** `/tool/traffic-generator/stats/latency-distribution`

此子菜单显示在特定延迟范围内接收到的数据包数量。可以按流或按序列查看延迟范围（例如，**print stream-num=3**，**print seq=10**）

以下是延迟图表的示例输出：

```ros
[admin@test-host] /tool/traffic-generator/stats/latency-distribution> print            
 # LATENCY                 COUNT        SHARE GRAPH                                               
 0 0-15.5us                    0           0%
 1 15.5us-31us                 0           0%
 2 31us-46.5us                 0           0%
 3 46.5us-62.1us               0           0%
 4 62.1us-77.6us               0           0%
 5 77.6us-93.1us               0           0%
 6 93.1us-109us                0           0%
 7 109us-124us                 0           0%
 8 124us-140us                 0           0%
 9 140us-155us                 0           0%
10 155us-171us                 0           0%
11 171us-186us                 4           0% *                                                   
12 186us-202us                29           0% *                                                   
13 202us-217us                90       0.001% *                                                   
14 217us-233us               302       0.004% *                                                   
15 233us-248us               630       0.009% *                                                   
16 248us-264us               789       0.011% *                                                   
17 264us-279us             1 384       0.021% -*                                                  
18 279us-295us             1 990        0.03% --*                                                 
19 295us-310us             2 966       0.045% ---*                                                
20 310us-326us             4 089       0.062% -----*                                              
21 326us-341us             4 958       0.075% ------*                                             
22 341us-357us             6 059       0.091% -------*                                            
23 357us-372us             6 660       0.101% --------*                                           
24 372us-388us             8 320       0.126% ----------*                                         
25 388us-403us             9 988       0.151% -------------*                                      
26 403us-419us            11 781       0.178% ---------------*                                    
27 419us-434us            12 512       0.189% ----------------*                                   
28 434us-450us            13 836        0.21% -----------------*                                  
29 450us-465us            15 681       0.238% --------------------*                               
30 465us-481us            17 740       0.269% ----------------------*                             
31 481us-496us            19 913       0.302% --------------------------*                         
32 496us-512us            21 106        0.32% ---------------------------*                        
33 512us-528us            22 848       0.346% -----------------------------*                      
34 528us-543us            25 059        0.38% --------------------------------*                   
35 543us-559us            26 593       0.403% ----------------------------------*                 
36 559us-574us            27 663       0.419% -----------------------------------*                
37 574us-590us            29 351       0.445% -------------------------------------*              
38 590us-605us            31 265       0.474% ----------------------------------------*           
39 605us-621us            33 224       0.504% -------------------------------------------*        
40 621us-636us            34 464       0.523% --------------------------------------------*       
41 636us-652us            35 630        0.54% ----------------------------------------------*     
42 652us-667us            37 245       0.565% ------------------------------------------------*   
43 667us-683us            38 158       0.579% -------------------------------------------------*  
44 683us-698us            38 626       0.586% --------------------------------------------------* 
45 698us-714us            38 985       0.591% --------------------------------------------------* 
46 714us-729us            39 061       0.592% --------------------------------------------------* 
47 729us-745us            39 750       0.603% ---------------------------------------------------*
48 745us-760us            39 145       0.594% --------------------------------------------------* 
49 760us-776us            39 162       0.594% --------------------------------------------------* 
50 776us-791us            38 197       0.579% -------------------------------------------------*  
51 791us-807us            37 811       0.573% -------------------------------------------------*  
52 807us-822us            37 364       0.567% ------------------------------------------------*   
53 822us-838us            36 770       0.558% -----------------------------------------------*    
54 838us-853us            35 831       0.543% ----------------------------------------------*     
55 853us-869us            35 380       0.536% ----------------------------------------------*     
56 869us-884us            34 472       0.523% --------------------------------------------*       
57 884us-900us            33 672       0.511% -------------------------------------------*        
58 900us-915us            33 799       0.513% --------------------------------------------*       
59 915us-931us            32 754       0.497% ------------------------------------------*         
60 931us-946us            32 339        0.49% ------------------------------------------*         
61 946us-962us            32 419       0.492% ------------------------------------------*         
62 962us-977us            32 107       0.487% -----------------------------------------*          
63 977us-993us            31 552       0.478% -----------------------------------------*          
64 0-993us             1 221 523       18.54%
```

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **count** (*整数*) | 当前延迟范围内的数据包数量 |
| **graph** (*字符串*) | share 的图形化表示 |
| **latency** (*字符串*) | 延迟范围 |
| **share** (*百分比*) | 落在此延迟范围内的数据包百分比。 |

### 流统计

**子菜单：** `/tool/traffic-generator/stats/stream`

此子菜单存储按流排序的统计信息。输出与 **quick** 模式相同。

```ros
[admin@test-host] /tool/traffic-generator/stats/stream> print 
 # SEQ    NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
 0 1      3          43 064 499.5Mbps        25 180 292.0Mbps        17 884 207.4Mbps
 1 1      4          43 062 499.5Mbps        39 946 463.3Mbps         3 116  36.1Mbps
 2 1      TOT        86 126 999.0Mbps        65 126 755.4Mbps        21 000 243.6Mbps
 3 2      3          43 544 505.1Mbps        30 449 353.2Mbps        13 095 151.9Mbps
 4 2      4          43 543 505.0Mbps        42 982 498.5Mbps           561   6.5Mbps
 5 2      TOT        87 087 1010.2...        73 431 851.7Mbps        13 656 158.4Mbps

... 

59 20     TOT        87 277 1012.4...        73 755 855.5Mbps        13 522 156.8Mbps
60 21     3          43 546 505.1Mbps        30 605 355.0Mbps        12 941 150.1Mbps
61 21     4          43 546 505.1Mbps        42 682 495.1Mbps           864  10.0Mbps
62 21     TOT        87 092 1010.2...        73 287 850.1Mbps        13 805 160.1Mbps
63 TOT    3         913 942 504.8Mbps       629 210 347.5Mbps       284 732 157.2Mbps
64 TOT    4         913 939 504.8Mbps       898 374 496.2Mbps        15 565   8.5Mbps
65 TOT    TOT     1 827 881 1009.6...     1 527 584 843.8Mbps       300 297 165.8Mbps
```

### 端口统计

**子菜单：** `/tool/traffic-generator/stats/port`

此子菜单存储按 rx/tx 端口排序的统计信息。

```ros
[admin@test-host] /tool/traffic-generator/stats/port> print 
 # SEQ    PORT        RX-UNK-PACKET    RX-UNK-BYTE RX-UNK...     TX-PACKET   TX-RATE     RX-PACKET
 0 1      port0:et...             0              0      0bps        43 064 499.5Mbps        39 946
 1 1      port1:et...             0              0      0bps        43 062 499.5Mbps        25 180
 2 1      TOT                     0              0      0bps        86 126 999.0Mbps        65 126
 3 2      port0:et...             0              0      0bps        43 544 505.1Mbps        42 982
 4 2      port1:et...             0              0      0bps        43 543 505.0Mbps        30 449
 5 2      TOT                     0              0      0bps        87 087 1010.2...        73 431
 6 3      port0:et...             0              0      0bps        43 540 505.0Mbps        42 615
 7 3      port1:et...             0              0      0bps        43 540 505.0Mbps        30 191
 8 3      TOT                     0              0      0bps        87 080 1010.1...        72 806
```

### 原始统计

**子菜单：** `/tool/traffic-generator/stats/raw`

此子菜单存储原始统计数据。

```ros
[admin@test-host] /tool/traffic-generator/stats/raw> print 
 # SEQ    PORT       NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE   LOST-PACKET LOST-RATE
 0 1      port0:e... 3          43 064 499.5Mbps             0      0bps        43 064 499.5Mbps
 1 1      port1:e... 3               0      0bps        25 180 292.0Mbps       -25 180 292.0Mbps
 2 1      TOT        3          43 064 499.5Mbps        25 180 292.0Mbps        17 884 207.4Mbps
 3 1      port0:e... 4               0      0bps        39 946 463.3Mbps       -39 946 463.3Mbps
 4 1      port1:e... 4          43 062 499.5Mbps             0      0bps        43 062 499.5Mbps
 5 1      TOT        4          43 062 499.5Mbps        39 946 463.3Mbps         3 116  36.1Mbps
 6 1      port0:e... TOT        43 064 499.5Mbps        39 946 463.3Mbps         3 118  36.1Mbps
 7 1      port1:e... TOT        43 062 499.5Mbps        25 180 292.0Mbps        17 882 207.4Mbps
 8 2      port0:e... 3          43 544 505.1Mbps             0      0bps        43 544 505.1Mbps
 9 2      port1:e... 3               0      0bps        30 449 353.2Mbps       -30 449 353.2Mbps
10 2      TOT        3          43 544 505.1Mbps        30 449 353.2Mbps        13 095 151.9Mbps
```

## 流

### 属性

| 属性 | 描述 |
| :-- | :-- |
| **disabled** (*是 \| 否*; 默认值：**否**) | 流是否被禁用 |
| **mbps** (*整数 [0..4294967295]*; 默认值：**0**) | 流将尝试生成的速率，单位为兆比特每秒。 |
| **name** (*字符串*; 默认值：) | 流的描述性名称。 |
| **num** (*整数 [0..15]*; 默认值：**0**) |  |
| **packet-size** (*整数[1..65535] [-整数[1..65535]]*; 默认值：**0**) | 生成的数据包大小（字节）。可以设置为随机数据包大小生成的范围。 |
| **port** (*字符串*; 默认值：) | 将用于传输数据包的端口菜单中的端口名称。 |
| **pps** (*整数 [0..4294967295]*; 默认值：**0**) | 流将尝试生成的每秒数据包数。 |
| **tx-template** (*字符串*; 默认值：) | 用作数据包内容来源的数据包模板或原始数据包模板菜单中的数据包模板名称。 |

## 配置示例

### IPsec 隧道性能测试

考虑以下测试设置

![](https://manual.mikrotik.com/docs/diagnostics-monitoring-and-troubleshooting/img/traffic-generator-01.webp)

被测系统（SUT）由连接到流量生成器服务器的两台路由器组成。两台 SUT 路由器之间的连接是 IPSec 加密的。

流量生成器将运行两个流：

- 从 1.1.1.0/24 网络到 2.2.2.0/24 网络的方向。
- 从 2.2.2.0/24 网络到 1.1.1.0/24 网络的方向。

#### R1 路由和 IPsec 设置

```ros
/ip/address
add address=192.168.33.1/30 interface=ether1
add address=1.1.1.2/24 interface=ether2

/ip/route 
add dst-address=2.2.2.0/24 gateway=192.168.33.2

/ip/ipsec/proposal
set default enc-algorithms=aes-128

/ip/ipsec/peer
add address=192.168.33.2 secret=123

/ip/ipsec/policy
add sa-src-address=192.168.33.1 sa-dst-address=192.168.33.2 \
    src-address=1.1.1.0/24 dst-address=2.2.2.0/24 tunnel=yes
```

#### R2 路由和 IPsec 设置

```ros
/ip/address
add address=192.168.33.2/30 interface=ether1
add address=2.2.2.2/24 interface=ether2

/ip/route 
add dst-address=1.1.1.0/24 gateway=192.168.33.1

/ip/ipsec/proposal
set default enc-algorithms=aes-128

/ip/ipsec/peer
add address=192.168.33.1 secret=123

/ip/ipsec/policy
add sa-src-address=192.168.33.2 sa-dst-address=192.168.33.1 \
    src-address=2.2.2.0/24 dst-address=1.1.1.0/24 tunnel=yes
```

#### 流量生成器服务器设置

```ros
/ip/address
add address=1.1.1.1/24 interface=ether2
add address=2.2.2.1/24 interface=ether3
```

首先，我们将定义哪些端口将用作流量生成器的 tx/rx 端口。

```ros
/tool/traffic-generator/port
add disabled=no interface=ether2 name=port0
add disabled=no interface=ether3 name=port1
```

为了构建将生成的实际数据包，需要使用 packet-template。

```ros
/tool/traffic-generator/packet-template
add header-stack=mac,ip,udp ip-dst=2.2.2.1/32 ip-gateway=1.1.1.2 ip-src=1.1.1.1/32 \
    name=routing-1 port=port0
add header-stack=mac,ip,udp ip-dst=1.1.1.1/32 ip-gateway=2.2.2.2 ip-src=2.2.2.1/32 \
    name=routing-2 port=port1
```

请注意，未指定 MAC 地址，因为模板生成器可以通过发送 ARP 消息自动假定下一跳 MAC 地址。由于我们正在进行路由，且目标 IP 不可直接到达，我们设置了 **ip-gateway** 参数来确定下一跳 MAC 地址。

运行 **print** 时，您可以看到所有假定（检测到）的值，包括 MAC 地址。

```ros
[admin@test-host] /tool/traffic-generator/packet-template> print 
 0 name="routing-1" header-stack=mac,ip,udp port=port0 
   assumed-mac-dst=00:0C:42:00:38:9D assumed-mac-src=00:0C:42:40:94:25 
   assumed-mac-protocol=ip assumed-ip-dscp=0 assumed-ip-id=0 
   assumed-ip-frag-off=0 assumed-ip-ttl=64 assumed-ip-protocol=udp 
   ip-src=1.1.1.1/32 ip-dst=2.2.2.1/32 assumed-udp-src-port=100 
   assumed-udp-dst-port=200 ip-gateway=1.1.1.2 data=uninitialized data-byte=0 

 1 name="routing-2" header-stack=mac,ip,udp port=port1 
   assumed-mac-dst=00:0C:42:00:38:D1 assumed-mac-src=00:0C:42:40:94:26 
   assumed-mac-protocol=ip assumed-ip-dscp=0 assumed-ip-id=0 
   assumed-ip-frag-off=0 assumed-ip-ttl=64 assumed-ip-protocol=udp 
   ip-src=2.2.2.1/32 ip-dst=1.1.1.1/32 assumed-udp-src-port=100 
   assumed-udp-dst-port=200 ip-gateway=2.2.2.2 data=uninitialized data-byte=0
```

例如，如果 SUT 中的任何路由器发生变化，假定的 MAC 地址不会自动更新。要更新数据包模板，只需发出命令：

```ros
/tool/traffic-generator/packet-template/set [find]
```

最后一部分是配置流

```ros
/tool/traffic-generator/stream
add disabled=no mbps=500 name=str1 id=3 packet-size=1450 port=port0 pps=0 \
    tx-template=routing-1
add disabled=no mbps=500 name=str3 id=4 packet-size=1450 port=port1 pps=0 \
    tx-template=routing-2
```

请注意，每个流都有一个唯一的 **id** 值。此值用于标识流的数据包，否则流量生成器将无法工作。

现在我们准备运行测试。在这种情况下，将使用 **quick** 模式：

```ros
[admin@test-host] /tool/traffic-generator> quick mbps=450
SEQ    NUM     TX-PACKET   TX-RATE     RX-PACKET   RX-RATE        RX-OOO   LOST-PACKET LOST-RATE 
37     4          39 488 458.0Mbps        39 270 455.5Mbps        15 509           218   2.5Mbps 
37     TOT        78 976 916.1Mbps        76 485 887.2Mbps        22 529         2 491  28.8Mbps 
38     3          38 957 451.9Mbps        37 657 436.8Mbps         7 078         1 300  15.0Mbps 
38     4          38 958 451.9Mbps        38 402 445.4Mbps        14 763           556   6.4Mbps 
38     TOT        77 915 903.8Mbps        76 059 882.2Mbps        21 841         1 856  21.5Mbps 
39     3          38 816 450.2Mbps        37 893 439.5Mbps         7 307           923  10.7Mbps 
39     4          38 815 450.2Mbps        38 642 448.2Mbps        15 110           173   2.0Mbps 
39     TOT        77 631 900.5Mbps        76 535 887.8Mbps        22 417         1 096  12.7Mbps 
40     3          39 779 461.4Mbps        37 415 434.0Mbps         7 136         2 364  27.4Mbps 
40     4          39 780 461.4Mbps        39 567 458.9Mbps        15 908           213   2.4Mbps 
40     TOT        79 559 922.8Mbps        76 982 892.9Mbps        23 044         2 577  29.8Mbps 
41     3          39 218 454.9Mbps        37 089 430.2Mbps         7 075         2 129  24.6Mbps 
41     4          39 218 454.9Mbps        38 663 448.4Mbps        15 752           555   6.4Mbps 
41     TOT        78 436 909.8Mbps        75 752 878.7Mbps        22 827         2 684  31.1Mbps 
42     3          39 188 454.5Mbps        37 906 439.7Mbps         6 729         1 282  14.8Mbps 
42     4          39 187 454.5Mbps        38 954 451.8Mbps        15 565           233   2.7Mbps 
42     TOT        78 375 909.1Mbps        76 860 891.5Mbps        22 294         1 515  17.5Mbps 
TOT    3       1 645 468 454.4Mbps     1 568 201 433.1Mbps       280 174        77 267  21.3Mbps 
TOT    4       1 645 464 454.4Mbps     1 626 896 449.3Mbps       627 480        18 568   5.1Mbps 
TOT    TOT     3 290 932 908.9Mbps     3 195 097 882.4Mbps       907 654        95 835  26.4Mbps
```

统计信息显示每个流的吞吐量以及两个流的总吞吐量、乱序数据包计数、丢包率、延迟和抖动。