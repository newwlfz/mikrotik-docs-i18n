# 接口统计与流量监控

> 本文档介绍 MikroTik RouterOS 的接口统计与 monitor-traffic 工具，用于实时监控物理及虚拟接口的网络利用率、硬件性能、数据包速率和比特率。内容包括查看接口计数器、Fast Path 指标、链路稳定性以及排查带宽瓶颈的相关命令。

# 接口统计与流量监控

每个 RouterOS 接口都包含各种计数器，例如接收和发送的数据包数量、[Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 字节数以及链路中断次数。这些统计数据可实时反映物理及虚拟接口的网络利用率和硬件性能。若要分析实时吞吐量和数据包速率，monitor-traffic 工具可提供连续的数据流，用于故障排查和带宽验证。

## 统计信息

接口统计功能可实时监控所有物理及虚拟接口的数据流和硬件性能。使用 `stats` 或 `stats-detail` 命令可打印接口计数器，这些计数器跟踪数据包吞吐量、字节数以及链路稳定性指标（如运行时间和中断次数）。以 "fp" 开头的值表示 [Fast Path](../firewall-and-quality-of-service/packet-flow-in-routeros.md#fast-path) 计数器，而 "tx-queue-drop" 通过显示被[接口队列](../firewall-and-quality-of-service/queues/index.md#interface-queue)丢弃的数据包数量来指示潜在的拥塞情况。

监控这些计数器有助于通过跟踪 `link-downs` 计数和流量的意外下降来识别物理层问题。同时，通过将 `rx-byte` 和 `tx-byte` 值与特定链路的预期吞吐量进行比较，也有助于排查带宽瓶颈。

```ros
[admin@MikroTik] > /interface/print stats 
Flags: R - RUNNING
Columns: NAME, RX-BYTE, TX-BYTE, RX-PACKET, TX-PACKET, TX-QUEUE-DROP
#   NAME        RX-BYTE      TX-BYTE  RX-PACKET  TX-PACKET  TX-QUEUE-DROP
0 R ether1  205 149 015  147 887 338    158 132    150 015              2
1 R ether2   32 400 148  335 690 764         19    216 509              0
2 R ether3  944 043 040   32 392 350    617 271         17              0
3 R ether4    7 038 417   32 398 973          9          4              0
4 R ether5    7 036 903   32 502 437          5          9              0
5   sfp1              0            0          0          0              0
[admin@MikroTik] > /interface/print stats-detail  
Flags: D - dynamic; X - disabled, R - running; S - slave; P - passthrough 
 0  R   name="ether1" last-link-down-time=2022-07-19 12:37:06 last-link-up-time=2022-07-19 12:37:09 link-downs=2 
        rx-byte=205 164 277 tx-byte=147 977 500 rx-packet=158 254 tx-packet=150 156 tx-queue-drop=2 
        fp-rx-byte=199 271 067 fp-tx-byte=0 fp-rx-packet=1 473 603 fp-tx-packet=0 

 1  R   name="ether2" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:07 link-downs=10 
        rx-byte=32 400 148 tx-byte=335 690 764 rx-packet=19 tx-packet=216 509 tx-queue-drop=0 
        fp-rx-byte=33 718 434 fp-tx-byte=67 fp-rx-packet=60 037 fp-tx-packet=1 

 2  R   name="ether3" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:08 link-downs=11 
        rx-byte=944 043 040 tx-byte=32 392 350 rx-packet=617 271 tx-packet=17 tx-queue-drop=0 fp-rx-byte=6 860 921 
        fp-tx-byte=0 fp-rx-packet=46 671 fp-tx-packet=0 

 3  R   name="ether4" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:07 link-downs=10 
        rx-byte=7 038 417 tx-byte=32 398 973 rx-packet=9 tx-packet=4 tx-queue-drop=0 fp-rx-byte=6 852 283 
        fp-tx-byte=0 fp-rx-packet=46 586 fp-tx-packet=0 

 4  R   name="ether5" last-link-down-time=2022-07-19 12:46:06 last-link-up-time=2022-07-19 12:46:08 link-downs=10 
        rx-byte=7 036 903 tx-byte=32 502 437 rx-packet=5 tx-packet=9 tx-queue-drop=0 fp-rx-byte=6 850 637 
        fp-tx-byte=178 fp-rx-packet=46 568 fp-tx-packet=2 

 5      name="sfp1" link-downs=0 rx-byte=0 tx-byte=0 rx-packet=0 tx-packet=0 tx-queue-drop=0 fp-rx-byte=0 
        fp-tx-byte=0 fp-rx-packet=0 fp-tx-packet=0 
```

## 流量监控

可以使用 `monitor-traffic` 命令监控通过任何接口的流量。

该工具提供实时吞吐量统计信息，包括接收和发送数据的数据包速率和比特率。它对于验证接口活动以及直接从命令行界面识别高带宽消耗者至关重要。

例如，使用此命令可通过观察特定 WAN 接口上的每秒比特数来排查疑似网络瓶颈。它还可用于确认流量是否正确流经新配置的 VLAN 或桥接成员。

```ros
[admin@MikroTik] > /interface/monitor-traffic [find]
                         name:     ether1 ether2 ether3 ether4 ether5 sfp1
        rx-packets-per-second:         19      0      0      0      0    0
           rx-bits-per-second:   27.8kbps   0bps   0bps   0bps   0bps 0bps
     fp-rx-packets-per-second:         29      0      0      0      0    0
        fp-rx-bits-per-second:   26.8kbps   0bps   0bps   0bps   0bps 0bps
        tx-packets-per-second:         21      0      0      0      0    0
           tx-bits-per-second:  149.4kbps   0bps   0bps   0bps   0bps 0bps
     fp-tx-packets-per-second:          0      0      0      0      0    0
        fp-tx-bits-per-second:       0bps   0bps   0bps   0bps   0bps 0bps
    tx-queue-drops-per-second:          0      0      0      0      0    0

```

:::info
其他 [以太网统计信息](../wired-connections/ethernet.md#stats) 可在 `/interface/ethernet` 菜单中查看。
:::