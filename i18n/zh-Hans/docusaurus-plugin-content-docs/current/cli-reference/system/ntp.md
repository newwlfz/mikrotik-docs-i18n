# NTP

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/ntp

**类型：** 目录

### system/ntp/client

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="mode" typ="枚举（单播 | 广播 | 组播 | 多播）"></ArgTableRow>
<ArgTableRow arg="servers" typ="多值 { address (flags=46D)
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="枚举"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="freq-drift" typ="数值"></ArgTableRow>
<ArgTableRow arg="status" typ="枚举（已停止 | 等待中 | 已同步 | 使用本地时钟）"></ArgTableRow>
<ArgTableRow arg="synced-server" typ="地址 (flags=46D)"></ArgTableRow>
<ArgTableRow arg="synced-stratum" typ="数值"></ArgTableRow>
<ArgTableRow arg="system-offset" typ="数值"></ArgTableRow>
</ArgTable>

#### system/ntp/client/reset-freq-drift

**类型：** 命令

#### system/ntp/client/servers

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
<ArgTableRow arg="D" typ="动态"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="address" typ="地址 (flags=46D)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="min-poll" typ="数值"></ArgTableRow>
<ArgTableRow arg="max-poll" typ="数值"></ArgTableRow>
<ArgTableRow arg="iburst" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="枚举（无）"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="resolved-address" typ="地址 (flags=46)"></ArgTableRow>
</ArgTable>

### system/ntp/key

**类型：** 目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="key-id" typ="数值" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key-val" typ="字符串" mandatory="1"></ArgTableRow>
</ArgTable>

### system/ntp/monitor-peers

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="type" typ="字符串"></ArgTableRow>
<ArgTableRow arg="address" typ="地址 (flags=46)"></ArgTableRow>
<ArgTableRow arg="refid" typ="字符串"></ArgTableRow>
<ArgTableRow arg="stratum" typ="数值"></ArgTableRow>
<ArgTableRow arg="hpoll" typ="数值"></ArgTableRow>
<ArgTableRow arg="ppoll" typ="数值"></ArgTableRow>
<ArgTableRow arg="root-delay" typ="数值"></ArgTableRow>
<ArgTableRow arg="root-disp" typ="数值"></ArgTableRow>
<ArgTableRow arg="offset" typ="数值"></ArgTableRow>
<ArgTableRow arg="delay" typ="数值"></ArgTableRow>
<ArgTableRow arg="disp" typ="数值"></ArgTableRow>
<ArgTableRow arg="jitter" typ="数值"></ArgTableRow>
</ArgTable>

### system/ntp/server

**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="broadcast" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="multicast" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="manycast" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="broadcast-addresses" typ="多值 { ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="vrf" typ="枚举"></ArgTableRow>
<ArgTableRow arg="use-local-clock" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="local-clock-stratum" typ="数值"></ArgTableRow>
<ArgTableRow arg="auth-key" typ="枚举（无）"></ArgTableRow>
</ArgTable>