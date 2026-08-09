# 速度测试

> 速度测试工具通过可配置属性（如地址、连接数、密码、测试时长和用户凭据）测量 MikroTik 设备之间的 ping、抖动以及 TCP/UDP 吞吐量。它提供详细的性能指标，包括测试期间的 CPU 利用率。

# 速度测试

速度测试是一款简易测试工具，用于测量从一台 MikroTik 设备到另一台设备的 ping、抖动、TCP 和 UDP 吞吐量。“speed-test”命令基于 Ping 工具和带宽测试。要使用此命令，需要能够访问带宽测试服务器。

## 通用接口属性

速度测试基于五个可配置属性：

- address - 主机 IP 地址。
- connection-count - 如果设备拥有超过 20 个核心，则使用核心数（默认值为 20）。
- password - 远程设备的密码。
- test-duration - 每次测试的持续时间（*默认情况下：5 次测试 * 10 秒持续时间 + 每次测试之间 1 秒暂停 = 54 秒*）。
- user - 远程设备的用户名。

## 配置示例

带宽和速度测试应通过设备进行，而非在设备上进行，以确保模拟真实场景，并避免因流量生成过程而使被测设备（DUT）的 CPU 过载。

要从设备 A（192.168.88.1）向设备 B（192.168.88.2）运行简单测试：

```ros
[admin@MikroTik] > /tool/speed-test address=192.168.88.2
              status: done
      time-remaining: 0s
    ping-min-avg-max: 541us / 609us / 3.35ms
  jitter-min-avg-max: 0s / 76us / 2.76ms
                loss: 0% (0/100)
        tcp-download: 921Mbps local-cpu-load:30%
          tcp-upload: 920Mbps local-cpu-load:30% remote-cpu-load:25%
        udp-download: 917Mbps local-cpu-load:6% remote-cpu-load:21%
          udp-upload: 916Mbps local-cpu-load:20% remote-cpu-load:6%
```

如果测试期间任何设备的 CPU 利用率达到 100%，将出现警告消息：

```ros
[admin@MikroTik]] > /tool/speed-test address=192.168.88.2
                  ;;; 结果可能受 CPU 限制，请注意流量生成/终止
                      性能可能不代表转发性能
              status: done
      time-remaining: 0s
    ping-min-avg-max: 541us / 609us / 3.35ms
  jitter-min-avg-max: 0s / 76us / 2.76ms
                loss: 0% (0/100)
        tcp-download: 721Mbps local-cpu-load:78%
          tcp-upload: 820Mbps local-cpu-load:100% remote-cpu-load:84%
        udp-download: 906Mbps local-cpu-load:10% remote-cpu-load:54%
          udp-upload: 895Mbps local-cpu-load:55% remote-cpu-load:12%
```

“test-duration”参数允许更改全部 5 项测试的持续时间：

1) 带 50ms 延迟的 Ping 测试。
2) TCP 接收。
3) TCP 发送。
4) UDP 接收。
5) UDP 发送。