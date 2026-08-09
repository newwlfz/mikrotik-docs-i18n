# 连接

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/firewall/connection

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="E" typ="expected">预期</ArgTableRow>
<ArgTableRow arg="S" typ="seen-reply">已见回复</ArgTableRow>
<ArgTableRow arg="A" typ="assured">已确认</ArgTableRow>
<ArgTableRow arg="C" typ="confirmed">已确认</ArgTableRow>
<ArgTableRow arg="D" typ="dying">即将消亡</ArgTableRow>
<ArgTableRow arg="F" typ="fasttrack">快速通道</ArgTableRow>
<ArgTableRow arg="H" typ="hw-offload">硬件卸载</ArgTableRow>
<ArgTableRow arg="s" typ="srcnat">源NAT</ArgTableRow>
<ArgTableRow arg="d" typ="dstnat">目标NAT</ArgTableRow>
<ArgTableRow arg="h" typ="uses-helper">使用辅助</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="protocol" typ="enum ()">连接协议。</ArgTableRow>
<ArgTableRow arg="src-address" typ="ipAddr">连接的源IP地址。</ArgTableRow>
<ArgTableRow arg="src-port" typ="num">连接的源端口。</ArgTableRow>
<ArgTableRow arg="dst-address" typ="ipAddr">连接的目标IP地址。</ArgTableRow>
<ArgTableRow arg="dst-port" typ="num">连接的目标端口。</ArgTableRow>
<ArgTableRow arg="reply-src-address" typ="ipAddr">回复源IP地址。</ArgTableRow>
<ArgTableRow arg="reply-src-port" typ="num">回复源端口。</ArgTableRow>
<ArgTableRow arg="reply-dst-address" typ="ipAddr">回复目标IP地址。</ArgTableRow>
<ArgTableRow arg="reply-dst-port" typ="num">回复目标端口。</ArgTableRow>
<ArgTableRow arg="tcp-state" typ="enum (none | syn-sent | syn-recv | established | fin-wait | close-wait | last-ack | time-wait | close | listen)">TCP连接状态。</ArgTableRow>
<ArgTableRow arg="icmp-type" typ="num">ICMP类型。</ArgTableRow>
<ArgTableRow arg="icmp-code" typ="num">ICMP代码。</ArgTableRow>
<ArgTableRow arg="icmp-id" typ="num">ICMP标识符。</ArgTableRow>
<ArgTableRow arg="gre-protocol" typ="num">GRE协议。</ArgTableRow>
<ArgTableRow arg="gre-version" typ="num">GRE版本。</ArgTableRow>
<ArgTableRow arg="gre-key" typ="num">GRE密钥。</ArgTableRow>
<ArgTableRow arg="connection-type" typ="string">连接类型。</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">连接超时时间。</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="string">连接标记。</ArgTableRow>
<ArgTableRow arg="orig-packets" typ="num">原始方向数据包数量。</ArgTableRow>
<ArgTableRow arg="orig-bytes" typ="num">原始方向字节数。</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-packets" typ="num">原始方向快速通道数据包数量。</ArgTableRow>
<ArgTableRow arg="orig-fasttrack-bytes" typ="num">原始方向快速通道字节数。</ArgTableRow>
<ArgTableRow arg="repl-packets" typ="num">回复方向数据包数量。</ArgTableRow>
<ArgTableRow arg="repl-bytes" typ="num">回复方向字节数。</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-packets" typ="num">回复方向快速通道数据包数量。</ArgTableRow>
<ArgTableRow arg="repl-fasttrack-bytes" typ="num">回复方向快速通道字节数。</ArgTableRow>
<ArgTableRow arg="orig-rate" typ="num">原始方向速率。</ArgTableRow>
<ArgTableRow arg="repl-rate" typ="num">回复方向速率。</ArgTableRow>
</ArgTable>