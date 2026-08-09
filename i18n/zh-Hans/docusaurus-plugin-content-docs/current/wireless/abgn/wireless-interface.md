# 无线接口

> RouterOS 无线接口支持 IEEE 802.11 标准，具备多种模式（客户端、AP、桥接）、加密协议、信道宽度调整以及高级传输设置等全面功能，以实现最佳的无线网络性能。

# 无线接口

---

## 概述

**软件包：** wireless

RouterOS 无线功能符合 IEEE 802.11 标准。它完全支持 802.11a、802.11b、802.11g、802.11n 和 802.11ac，并提供 WPA、WEP、AES 加密、无线分布式系统（WDS）、动态频率选择（DFS）、虚拟接入点、Nstreme 和 Nv2 专有协议等附加功能。

无线接口可在多种模式下运行：客户端（station）、接入点、无线桥接等。客户端/station 也可以在不同的模式下运行。支持模式的完整列表请参见 [无线 Station 模式](../user-guides/wireless-station-modes.md)。

## 通用接口属性

**子菜单：** `/interface/wireless`

| 属性 | 描述 |
| :-- | :-- |
| **adaptive-noise-immunity** (*ap-and-client-mode \| client-mode \| none*; 默认值：**none**) | 此属性仅对基于 Atheros 芯片组的网卡有效。 |
| **allow-sharedkey** (*yes \| no*; 默认值：**no**) | 允许 WEP 共享密钥客户端连接。请注意，这些客户端不会进行身份验证（WEP 共享密钥不与任何内容进行比较）——只要访问列表允许，它们就会被立即接受。 |
| **ampdu-priorities** (*整数列表 [0..7]*; 默认值：**0**) | 应协商并使用 AMPDU 发送（聚合帧并使用块确认发送）的帧优先级。使用 AMPDU 将提高吞吐量，但可能增加延迟，因此对于实时流量（语音、视频）可能不理想。因此，默认情况下 AMPDU 仅对尽力而为的流量启用。 |
| **amsdu-limit** (*整数 [0..8192]*; 默认值：**8192**) | 协商后设备允许准备的最大 AMSDU。AMSDU 聚合可以显著提高吞吐量，尤其是对于小帧，但在聚合帧重传的情况下可能会增加延迟。发送和接收 AMSDU 也会增加 CPU 使用率。 |
| **amsdu-threshold** (*整数 [0..8192]*; 默认值：**8192**) | 允许包含在 AMSDU 中的最大帧大小。 |
| **antenna-gain** (*整数 [0..4294967295]*; 默认值：**0**) | 天线增益，单位 dBi，用于根据**国家**法规计算最大发射功率。 |
| **antenna-mode** (*ant-a \| ant-b \| rxa-txb \| txa-rxb*; 默认值：) | 选择用于发送和接收的天线。*ant-a* - 仅使用 'a' 天线。*ant-b* - 仅使用 'b' 天线。*txa-rxb* - 使用天线 'a' 发送，天线 'b' 接收。*rxa-txb* - 使用天线 'b' 发送，天线 'a' 接收。 |
| **area** (*字符串*; 默认值：) | 标识无线网络组。此值由 AP 通告，并可在 [connect-list](./wireless-interface.md#connect-list) 中通过 **area-prefix** 进行匹配。这是一个专有扩展。 |
| **arp** (*disabled \| enabled \| proxy-arp \| reply-only*; 默认值：**enabled**) | [ARP](../../network-management/arp.md) |
| **arp-timeout** (*auto \| 整数*; 默认值：**auto**) | ARP 超时是指在没有从 IP 收到数据包后，ARP 记录在 ARP 表中保留的时间。值 **auto** 等于 **/ip/settings** 中 **arp-timeout** 的值，默认值为 30 秒。 |
| **band** (*2ghz-b \| 2ghz-b/g \| 2ghz-b/g/n \| 2ghz-onlyg \| 2ghz-onlyn \| 5ghz-a \| 5ghz-a/n \| 5ghz-onlyn \| 5ghz-a/n/ac \| 5ghz-onlyac \| 5ghz-n/ac*; 默认值：) | 定义所使用的数据速率、信道频率和宽度的集合。 |
| **basic-rates-a/g** (*12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps \| 6Mbps \| 9Mbps*; 默认值：**6Mbps**) | 类似于 **basic-rates-b** 属性，但用于 5ghz、5ghz-10mhz、5ghz-5mhz、5ghz-turbo、2.4ghz-b/g、2.4ghz-onlyg、2ghz-10mhz、2ghz-5mhz 和 2.4ghz-g-turbo 频段。 |
| **basic-rates-b** (*11Mbps \| 1Mbps \| 2Mbps \| 5.5Mbps*; 默认值：**1Mbps**) | 基本速率列表，用于 2.4ghz-b、2.4ghz-b/g 和 2.4ghz-onlyg 频段。客户端只有在支持 AP 通告的所有基本速率时才能连接到 AP。AP 只有在支持另一个 AP 的所有基本速率时才会建立 WDS 链路。此属性仅在 AP 模式以及配置了 **rate-set** 值时生效。 |
| **bridge-mode** (*disabled \| enabled*; 默认值：**enabled**) | 允许使用 station-bridge 模式。[无线 Station 模式](../user-guides/wireless-station-modes.md) |
| **burst-time** (*整数 \| disabled*; 默认值：**disabled**) | 用于不间断发送数据的时间（微秒）。请注意，在该 burst-time 微秒内，网络中的其他无线网卡将无法传输数据。此设置仅适用于基于 AR5000、AR5001X 和 AR5001X+ 芯片组的网卡。 |
| **channel-width** (*20/40/80/160mhz-Ceeeeeee \| 20/40/80/160mhz-XXXXXXXX \| 20/40/80/160mhz-eCeeeeee \| 20/40/80/160mhz-eeCeeeee \| 20/40/80/160mhz-eeeCeeee \| 20/40/80/160mhz-eeeeCeee \| 20/40/80/160mhz-eeeeeCee \| 20/40/80/160mhz-eeeeeeCe \| 20/40/80/160mhz-eeeeeeeC \| 20/40/80mhz-Ceee \| 20/40/80mhz-eCee \| 20/40/80mhz-eeCe \| 20/40/80mhz-eeeC \| 20/40/80mhz-XXXX \| 20/40mhz-Ce \| 20/40mhz-eC \| 20/40mhz-XX \| 40mhz-turbo \| 20mhz \| 10mhz \| 5mhz*; 默认值：**20mhz**) | 使用扩展信道（例如 Ce、eC 等）允许额外的 20MHz 扩展信道，并指定其应位于控制（主）信道下方还是上方。扩展信道允许 802.11n 设备使用高达 40MHz（802.11ac 高达 160MHz）的总频谱，从而提高最大吞吐量。带有 XX 和 XXXX 扩展的信道宽度会根据每个频率上运行的并发设备数量自动扫描拥挤程度较低的控制信道频率，并自动选择“C”控制信道频率。 |
| **comment** (*字符串*; 默认值：) | 接口的简短描述 |
| **compression** (*yes \| no*; 默认值：**no**) | 将此属性设置为 *yes* 将允许使用硬件压缩。无线接口必须支持硬件压缩。与不使用压缩的设备连接仍然可以工作。 |
| **country** (*国家名称 \| no\_country\_set*; 默认值：**etsi**) | 限制每个频率的可用频段、频率和最大发射功率。同时指定 **scan-list** 的默认值。值 *no\_country\_set* 是符合 FCC 要求的信道集合。 |
| **default-ap-tx-limit** (*整数 [0..4294967295]*; 默认值：**0**) | 这是针对不匹配 [access-list](./wireless-interface.md#access-list) 中任何条目的客户端的 **ap-tx-limit** 值。0 表示无限制。 |
| **default-authentication** (*yes \| no*; 默认值：**yes**) | 对于 AP 模式，这是针对不匹配 [access-list](./wireless-interface.md#access-list) 中任何条目的客户端的 **authentication** 值。对于 station 模式，这是针对不匹配 [connect-list](./wireless-interface.md#connect-list) 中任何条目的 AP 的 **connect** 值。 |
| **default-client-tx-limit** (*整数 [0..4294967295]*; 默认值：**0**) | 这是针对不匹配 [access-list](./wireless-interface.md#access-list) 中任何条目的客户端的 **client-tx-limit** 值。0 表示无限制。 |
| **default-forwarding** (*yes \| no*; 默认值：**yes**) | 这是针对不匹配 [access-list](./wireless-interface.md#access-list) 中任何条目的客户端的 **forwarding** 值。 |
| **disable-running-check** (*yes \| no*; 默认值：**no**) | 设置为 **yes** 时，接口将始终具有 running 标志。如果值设置为 **no**，路由器将判断网卡是否已启动并运行——对于 AP，必须有一个或多个客户端注册到它；对于 station，它必须连接到 AP。 |
| **disabled** (*yes \| no*; 默认值：**yes**) | 接口是否被禁用 |
| **disconnect-timeout** (*时间 [0s..15s]*; 默认值：**3s**) | 此时间间隔从最低数据速率下的第三次发送失败开始计算。此时，在最低数据速率下已有 3 \* (**hw-retries** + 1) 次帧传输失败。在 **disconnect-timeout** 期间，将按照 **on-fail-retry-time** 间隔重试数据包传输。如果在 **disconnect-timeout** 期间没有帧能够成功传输，则连接关闭，此事件记录为“extensive data loss”。成功的帧传输会重置此计时器。 |
| **distance** (*整数 \| dynamic \| indoors*; 默认值：**dynamic**) | 在认为传输失败之前等待单播帧确认（**ACKs**）的时间，或简称为 **ACK-Timeout**。距离值具有以下行为：*Dynamic* - 使 AP 检测并使用对所有已连接客户端都有效的最小超时。*Indoor* - 使用硬件芯片制造商设置的默认 ACK 超时值。*Number* - 在公式中使用输入值：ACK-timeout = ((**distance** * 1000) + 299) / 300 us；Nstreme/Nv2 协议不使用确认。 |
| **frame-lifetime** (*整数 [0..4294967295]*; 默认值：**0**) | 丢弃排队发送时间超过 **frame-lifetime** 的帧。默认情况下，当此属性值为 *0* 时，仅在连接关闭后丢弃帧。 |
| **frequency** (*整数 [0..4294967295]*; 默认值：) | AP 运行的信道频率值，单位 MHz。允许的值取决于所选的频段，并受 **country** 设置和无线网卡能力限制。如果接口处于任何 **station** 模式、*wds-slave* 模式或 DFS 激活状态，此设置**无效**。*注意*：如果使用模式 "superchannel"，网卡支持的任何频率都将被接受，但在 RouterOS 客户端上，任何非标准频率都必须配置在 [scan-list](./wireless-interface.md#scan-list) 中，否则将不会在非标准范围内扫描。在 WinBox 中，扫描列表频率以*粗体*显示，任何其他频率意味着客户端需要配置 scan-list。 |
| **frequency-mode** (*manual-txpower \| regulatory-domain \| superchannel*; 默认值：**regulatory\_domain**) | 有三种频率模式可用：*regulatory-domain* - 根据 **country** 的值限制可用信道和每个信道的最大发射功率。*manual-txpower* - 与上述相同，但不限制最大发射功率。*superchannel* - 一致性测试模式。允许网卡支持的所有信道。每个频段的可用信道列表可以在 **/interface/wireless/info/allowed-channels** 中查看。此模式允许您测试默认扫描列表和/或监管域之外的无线信道。此模式只能在受控环境中使用，或者如果您在所在地区拥有特殊许可才能使用。 |
| **frequency-offset** (*整数 [-2147483648..2147483647]*; 默认值：**0**) | 如果使用的无线网卡以与 RouterOS 显示不同的频率运行（例如网卡中使用了频率转换器），则允许指定偏移量。因此，如果您的网卡工作在 4000MHz，但 RouterOS 显示 5000MHz，请将偏移量设置为 1000MHz，它将正确显示。该值以 MHz 为单位，可以是正数或负数。 |
| **guard-interval** (*any \| long*; 默认值：**any**) | 是否允许使用短保护间隔（请参阅 802.11n MCS 规范以了解这可能如何影响吞吐量）。“any”将根据数据速率使用短或长间隔，“long”将使用长间隔。 |
| **hide-ssid** (*yes \| no*; 默认值：**no**) | *yes* - AP 不在信标帧中包含 SSID，并且不回复具有广播 SSID 的探测请求。*no* - AP 在信标帧中包含 SSID，并回复具有广播 SSID 的探测请求。此属性仅在 AP 模式下生效。将其设置为 *yes* 可以将此网络从某些客户端软件显示的无线网络列表中移除。更改此设置不会提高无线网络的安全性，因为 SSID 包含在 AP 发送的其他帧中。 |
| **ht-basic-mcs** (*列表 (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7**) | 每个连接客户端必须支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。MCS 规范请参阅 802.11n。 |
| **ht-supported-mcs** (*列表 (mcs-0 \| mcs-1 \| mcs-2 \| mcs-3 \| mcs-4 \| mcs-5 \| mcs-6 \| mcs-7 \| mcs-8 \| mcs-9 \| mcs-10 \| mcs-11 \| mcs-12 \| mcs-13 \| mcs-14 \| mcs-15 \| mcs-16 \| mcs-17 \| mcs-18 \| mcs-19 \| mcs-20 \| mcs-21 \| mcs-22 \| mcs-23)*; 默认值：**mcs-0; mcs-1; mcs-2; mcs-3; mcs-4; mcs-5; mcs-6; mcs-7; mcs-8; mcs-9; mcs-10; mcs-11; mcs-12; mcs-13; mcs-14; mcs-15; mcs-16; mcs-17; mcs-18; mcs-19; mcs-20; mcs-21; mcs-22; mcs-23**) | 此设备通告为支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11n-2009#Data_rates)。MCS 规范请参阅 802.11n。 |
| **hw-fragmentation-threshold** (*整数[256..3000] \| disabled*; 默认值：**disabled**) | 指定通过无线介质传输时的最大分片大小（字节）。802.11 标准数据包（802.11 术语中的 MSDU）分片允许数据包在通过无线介质传输前进行分片，以提高成功传输的概率（只有未正确传输的分片才会被重传）。请注意，由于协议开销以及发送和接收双方资源使用的增加，传输分片数据包的效率低于传输未分片数据包。 |
| **hw-protection-mode** (*cts-to-self \| none \| rts-cts*; 默认值：**none**) | 帧保护支持属性 [帧保护支持](./wireless-interface.md#frame-protection-support-rtscts) |
| **hw-protection-threshold** (*整数 [0..65535]*; 默认值：**0**) | 帧保护支持属性 [帧保护支持](./wireless-interface.md#frame-protection-support-rtscts) |
| **hw-retries** (*整数 [0..15]*; 默认值：**7**) | 在不视为传输失败的情况下重试发送帧的次数。失败时降低数据速率并重新发送帧。在最低支持速率下连续三次失败将暂停向此目的地的传输，持续时间为 **on-fail-retry-time**。之后，再次发送帧。帧将一直重传，直到传输成功，或者直到客户端在 **disconnect-timeout** 后被断开。如果超过 **frame-lifetime**，帧可能在此期间被丢弃。 |
| **installation** (*any \| indoor \| outdoor*; 默认值：**any**) | 调整扫描列表，以使用所设置国家的室内、室外或所有频率。 |
| **interworking-profile** (*enabled \| disabled*; 默认值：**disabled**) |  |
| **keepalive-frames** (*enabled \| disabled*; 默认值：**enabled**) | 仅当无线接口处于 mode=**ap-bridge** 时适用。如果客户端大约 20 秒未通信，AP 会发送“keepalive-frame”。**注意：** 禁用此功能可能导致注册表中出现“幽灵”客户端。 |
| **l2mtu** (*整数 [0..65536]*; 默认值：**1600**) |  |
| **mac-address** (*MAC*; 默认值：) |  |
| **master-interface** (*字符串*; 默认值：) | 具有 *virtual-ap* 能力的无线接口名称。仅当主接口处于 *ap-bridge*、*bridge*、*station* 或 *wds-slave* 模式时，虚拟 AP 接口才能工作。此属性仅适用于虚拟 AP 接口。 |
| **max-station-count** (*整数 [1..2007]*; 默认值：**2007**) | 最大关联客户端数。WDS 链路也计入此限制。 |
| **mode** (*station \| station-wds \| ap-bridge \| bridge \| alignment-only \| nstreme-dual-slave \| wds-slave \| station-pseudobridge \| station-pseudobridge-clone \| station-bridge*; 默认值：**station**) | 在不同的 station 和接入点（AP）模式之间选择。[Station 模式](../user-guides/wireless-station-modes.md)：*station* - 基本 station 模式。查找并连接到可接受的 AP。*station-wds* - 与 *station* 相同，但使用专有扩展与 AP 建立 WDS 链路。AP 配置必须允许与此设备的 WDS 链路。请注意，此模式不使用 wds 中的条目。*station-pseudobridge* - 与 *station* 相同，但额外对所有流量执行 MAC 地址转换。允许接口被桥接。*station-pseudobridge-clone* - 与 *station-pseudobridge* 相同，但使用 **station-bridge-clone-mac** 地址连接到 AP。station-bridge - 在 station 设备上提供透明的、独立于协议的 L2 桥接支持。当通过 bridge-mode 参数启用时，RouterOS AP 接受处于 station-bridge 模式的客户端。在此模式下，AP 维护一个转发表，其中包含哪些 MAC 地址可通过哪个 station 设备到达的信息。仅适用于 RouterOS AP。使用 station-bridge 模式时，无法连接到 CAPsMAN 控制的 CAP。🛑 **重要提示：** `wireless` station-bridge 模式与运行较新 `wifi` 软件包的 AP 不兼容，反之亦然。AP 模式：*ap-bridge* - 基本接入点模式。*bridge* - 与 *ap-bridge* 相同，但仅限于一个关联客户端。*wds-slave* - 与 *ap-bridge* 相同，但扫描具有相同 **ssid** 的 AP 并建立 WDS 链路。如果此链路丢失或无法建立，则继续扫描。如果 **dfs-mode** 为 *radar-detect*，则在扫描期间将找不到启用了 **hide-ssid** 的 AP。特殊模式：*alignment-only* - 将接口置于连续发射模式，用于对准远程天线。*nstreme-dual-slave* - 允许此接口用于 nstreme-dual 设置。伪桥接模式中的 MAC 地址转换通过检查数据包并建立相应的 IP 和 MAC 地址表来实现。所有数据包都使用伪桥接使用的 MAC 地址发送到 AP，接收数据包的 MAC 地址从地址转换表中恢复。对于所有非 IP 数据包，地址转换表中只有一个条目，因此桥接网络中的多个主机不能可靠地使用非 IP 协议。**注意：** IPv6 无法通过伪桥接工作。 |
| **mtu** (*整数 [0..65536]*; 默认值：**1500**) |  |
| **multicast-buffering** (*disabled \| enabled*; 默认值：**enabled**) | 对于具有省电功能的客户端，将组播数据包缓冲到下一个信标时间。客户端应唤醒以接收信标，通过接收信标它看到有待处理的组播数据包，并且应等待组播数据包被发送。 |
| **multicast-helper** (*default \| disabled \| full*; 默认值：**default**) | 设置为 **full** 时，组播数据包将使用单播目的 MAC 地址发送，解决无线链路上的组播问题。此选项应仅在接入点上启用，客户端应配置为 **station-bridge** 模式。disabled - 禁用助手，并使用组播目的 MAC 地址发送组播数据包。dhcp - 在发送 DHCP 数据包之前，将其 MAC 地址更改为单播 MAC 地址。full - 在发送所有组播数据包之前，将其 MAC 地址更改为单播 MAC 地址。default - 当前设置为 *dhcp* 的默认选择。该值可能在未来的版本中更改。 |
| **name** (*字符串*; 默认值：) | 接口名称 |
| **noise-floor-threshold** (*default \| 整数 [-128..127]*; 默认值：**default**) | 仅供高级使用，因为它可能严重影响接口的性能。可以手动设置噪声底限阈值。默认情况下，它是动态计算的。此属性也影响接收信号强度。此属性仅对非 AC 芯片有效。 |
| **nv2-cell-radius** (*整数 [10..200]*; 默认值：**30**) | 此设置影响 AP 为客户端发起连接而分配的竞争时隙大小，以及用于估计到客户端距离的时隙大小。当设置太小时，较远的客户端可能难以连接和/或以“ranging timeout”错误断开。虽然在正常操作期间此设置的影响应可忽略不计，但为了保持最大性能，建议在非必要情况下不要增加此设置，这样 AP 就不会保留从未实际使用的时间，而是将其分配给实际数据传输。在 AP 上：到最远客户端的距离（公里）。在 station 上：无影响。 |
| **nv2-noise-floor-offset** (*default \| 整数 [0..20]*; 默认值：**default**) |  |
| **nv2-preshared-key** (*字符串*; 默认值：) *[敏感](../../getting-started/configuration-management/list-of-menus-with-sensitive-parameters.md)* |  |
| **nv2-qos** (*default \| frame-priority*; 默认值：**default**) | 设置数据包优先级机制，首先发送高优先级队列的数据，然后发送较低队列优先级的数据，直到达到 0 队列优先级。当链路被高优先级队列数据占满时，较低优先级的数据不会被发送。请非常小心地使用，此设置作用于 AP。**frame-priority** - 可通过 Mangle 规则调整的手动设置。**default** - 默认设置，小数据包获得优先级以获得最佳延迟。 |
| **nv2-queue-count** (*整数 [2..8]*; 默认值：**2**) |  |
| **nv2-security** (*disabled \| enabled*; 默认值：**disabled**) |  |
| **on-fail-retry-time** (*时间 [100ms..1s]*; 默认值：**100ms**) | 在最低数据速率下第三次发送失败后，等待指定的时间间隔再重试。 |
| **periodic-calibration** (*default \| disabled \| enabled*; 默认值：**default**) | 设置 *default* 会在 [info](./wireless-interface.md#info) **default-periodic-calibration** 属性为 *enabled* 时启用周期性校准。该属性的值取决于无线网卡的类型。此属性仅对基于 Atheros 芯片组的网卡有效。 |
| **periodic-calibration-interval** (*整数 [1..10000]*; 默认值：**60**) | 此属性仅对基于 Atheros 芯片组的网卡有效。 |
| **preamble-mode** (*both \| long \| short*; 默认值：**both**) | 短前导码模式是 802.11b 标准的一个选项，可减少每帧开销。在 AP 上：*long* - 不使用短前导码。*short* - 通告短前导码能力。不接受不具备此能力的客户端的连接。*both* - 通告短前导码能力。在 station 上：*long* - 不使用短前导码。*short* - 如果 AP 不支持短前导码，则不连接。*both* - 如果 AP 支持，则使用短前导码。 |
| **prism-cardtype** (*100mW \| 200mW \| 30mW*; 默认值：) | 指定已安装的 Prism 无线网卡类型。 |
| **proprietary-extensions** (*post-2.9.25 \| pre-2.9.25*; 默认值：**post-2.9.25**) | RouterOS 在管理帧的信息元素中包含专有信息。此参数控制这些信息的包含方式。*pre-2.9.25* - 这是较旧的方法。它可以与更新版本的 RouterOS 互操作。此方法与某些客户端不兼容，例如基于 Centrino 的客户端。*post-2.9.25* - 这使用标准化的方式来包含供应商特定信息，与较新的无线客户端兼容。 |
| **radio-name** (*字符串*; 默认值：**接口的 MAC 地址**) | 设备的描述性名称，显示在远程设备的注册表条目中。这是一个专有扩展。 |
| **rate-selection** (*advanced \| legacy*; 默认值：**advanced**) | 默认值为 **advanced**；**legacy** 模式效率低下，仅为向后兼容而保留。 |
| **rate-set** (*configured \| default*; 默认值：**default**) | 有两个选项可用：*default* - 使用默认的基本和受支持速率集。**basic-rates** 和 **supported-rates** 参数的值无效。*configured* - 使用 **basic-rates**、**supported-rates**、**basic-mcs**、**mcs** 中的值。[基本和 MCS 速率表](./wireless-interface.md#basic-and-mcs-rate-table)。 |
| **rx-chains** (*整数列表 [0..3]*; 默认值：**0**) | 用于接收的天线。在当前的 MikroTik 路由器中，必须同时启用 RX 和 TX 链，该链才会被启用。 |
| scan-list (*逗号分隔的频率和频率范围列表 \| default. 类型也支持 range:step 选项*; 默认值：**default**) | *default* 值是由网卡支持且被 **country** 和 **frequency-mode** 设置允许的所选频段中的所有信道（此列表可以在 [info](./wireless-interface.md#info) 中查看）。对于 *5ghz* 频段的默认扫描列表，信道以 20MHz 步进获取；在 *5ghz-turbo* 频段中，以 40MHz 步进获取；对于所有其他频段，以 5MHz 步进获取。如果手动指定 **scan-list**，则获取所有匹配的信道。（示例：**scan-list**=*default,5200-5245,2412-2427* - 这将使用当前频段的默认扫描列表值，并向其中添加 5200-5245 或 2412-2427 范围内支持的频率。）在 WinBox 或 Webfig 中，将每个频率或频率范围作为单独的 scan-list 条目输入；那里不支持逗号分隔的列表。scan-list 还支持步进，您可以手动指定扫描步进。示例：**scan-list**=*5500-5600:20* 将生成这样的扫描列表值 *5500,5520,5540,5560,5580,5600*。 |
| **security-profile** (*字符串*; 默认值：**default**) | 来自 [安全配置文件](./wireless-interface.md#security-profiles) 的配置文件名称 |
| **secondary-channel** (*整数*; 默认值：**""**) | 指定辅助信道，启用 80+80MHz 传输所需。要禁用 80+80MHz 功能，请将 secondary-channel 设置为 "" 或通过 CLI/GUI 取消设置该值。 |
| **ssid** (*字符串 (0..32 字符)*; 默认值：**[/system/identity](../../system-information-and-utilities/identity.md) 的值**) | SSID（服务集标识符）是标识无线网络的名称。 |
| **skip-dfs-channels** (*字符串 \| 10min-cac \| all \| disabled*; 默认值：**disabled**) | 这些值用于跳过所有 DFS 信道，或专门跳过 5600-5650MHz 范围内的 DFS CAC 信道，其检测可能需要长达 10 分钟。 |
| **station-bridge-clone-mac** (*MAC*; 默认值：) | 此属性仅在 *station-pseudobridge-clone* 模式下生效。连接到 AP 时使用此 MAC 地址。如果此值为 *00:00:00:00:00:00*，station 将最初使用无线接口的 MAC 地址。一旦需要传输具有另一个设备 MAC 地址的数据包，station 将使用该地址重新连接到 AP。 |
| **station-roaming** (*disabled \| enabled*; 默认值：**disabled**) | Station 漫游功能仅适用于 802.11 无线协议，且仅适用于 station 模式。[Station 漫游](./wireless-interface.md#station-roaming) |
| **supported-rates-a/g** (*速率列表 [12Mbps \| 18Mbps \| 24Mbps \| 36Mbps \| 48Mbps \| 54Mbps \| 6Mbps \| 9Mbps]*; 默认值：**6Mbps; 9Mbps; 12Mbps; 18Mbps; 24Mbps; 36Mbps; 48Mbps; 54Mbps**) | 支持的速率列表，用于除 *2ghz-b* 之外的所有频段。 |
| **supported-rates-b** (*速率列表 [11Mbps \| 1Mbps \| 2Mbps \| 5.5Mbps]*; 默认值：**1Mbps; 2Mbps; 5.5Mbps; 11Mbps**) | 支持的速率列表，用于 *2ghz-b*、*2ghz-b/g* 和 *2ghz-b/g/n* 频段。两个设备将仅使用双方都支持的速率进行通信。此属性仅在 **rate-set** 值为 *configured* 时生效。 |
| **tdma-period-size** (*整数 [1..10]*; 默认值：**2**) | 指定 TDMA 周期（毫秒）。它可能有助于更长距离的链路，可以略微增加带宽，但延迟也会增加。 |
| **tx-chains** (*整数列表 [0..3]*; 默认值：**0**) | 用于发送的天线。在当前的 MikroTik 路由器中，必须同时启用 RX 和 TX 链，该链才会被启用。 |
| **tx-power** (*整数 [-30..40]*; 默认值：) | 对于 802.11ac 无线接口，这是总功率；但对于 802.11a/b/g/n，这是每链功率。 |
| **tx-power-mode** (*default, card-rates, all-rates-fixed, manual-table*; 默认值：**default**) | 设置无线网卡的 tx-power 模式。default - 使用存储在网卡中的值。all-rates-fixed - 对所有数据速率使用相同的发射功率。如果发射功率设置高于网卡对于所用速率的额定值，可能会损坏网卡。manual-table - 为每个速率单独定义发射功率。如果发射功率设置高于网卡对于所用速率的额定值，可能会损坏网卡。card-rates - 根据 **tx-power** 参数的值，为每个速率计算发射功率。旧模式仅与当前已停产的产品兼容。 |
| **update-stats-interval** (; 默认值：) | 多久向客户端请求更新信号强度和 ccq 值。访问 [registration-table](./wireless-interface.md#registration-table) 也会触发这些值的更新。这是专有扩展。 |
| **vht-basic-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 默认值：**MCS 0-7**) | 每个连接客户端必须支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.11ac#Data_rates_and_speed)。MCS 规范请参阅 802.11ac。您可以为每个空间流设置 MCS 间隔。*none* - 不使用选定的空间流。*MCS 0-7* - 客户端必须支持 MCS-0 到 MCS-7。*MCS 0-8* - 客户端必须支持 MCS-0 到 MCS-8。*MCS 0-9* - 客户端必须支持 MCS-0 到 MCS-9。 |
| **vht-supported-mcs** (*none \| MCS 0-7 \| MCS 0-8 \| MCS 0-9*; 默认值：**MCS 0-9**) | 此设备通告为支持的[调制和编码方案](http://en.wikipedia.org/wiki/IEEE_802.