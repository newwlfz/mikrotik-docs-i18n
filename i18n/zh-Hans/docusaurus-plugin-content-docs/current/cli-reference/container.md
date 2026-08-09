# container

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# container

**软件包:** container
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="S" typ="已停止"></ArgTableRow>
<ArgTableRow arg="N" typ="启动中"></ArgTableRow>
<ArgTableRow arg="R" typ="运行中"></ArgTableRow>
<ArgTableRow arg="T" typ="停止中"></ArgTableRow>
<ArgTableRow arg="E" typ="下载/解压中"></ArgTableRow>
<ArgTableRow arg="D" typ="删除中"></ArgTableRow>
<ArgTableRow arg="F" typ="下载/解压失败"></ArgTableRow>
<ArgTableRow arg="C" typ="启动并执行健康检查"></ArgTableRow>
<ArgTableRow arg="H" typ="健康"></ArgTableRow>
<ArgTableRow arg="U" typ="不健康"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file" typ="文件 {  }"></ArgTableRow>
<ArgTableRow arg="remote-image" typ="字符串"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="interface" typ="多选 { iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="env" typ="对象 { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="envlists" typ="多选 { 枚举
 }"></ArgTableRow>
<ArgTableRow arg="entrypoint" typ="多选 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="cmd" typ="多选 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="shell" typ="多选 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="stop-signal" typ="枚举 (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
<ArgTableRow arg="stop-time" typ="时间"></ArgTableRow>
<ArgTableRow arg="root-dir" typ="文件"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="文件"></ArgTableRow>
<ArgTableRow arg="mount" typ="对象 { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tmpfs" typ="对象 { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="mountlists" typ="多选 { 枚举
 }"></ArgTableRow>
<ArgTableRow arg="shm-size" typ="数值"></ArgTableRow>
<ArgTableRow arg="dns" typ="多选 { 地址 (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="default-dns" typ="多选 { 地址 (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="hostname" typ="字符串"></ArgTableRow>
<ArgTableRow arg="domain-name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="workdir" typ="字符串"></ArgTableRow>
<ArgTableRow arg="logging" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="start-on-boot" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="stop-on-unhealthy" typ="布尔值"></ArgTableRow>
<ArgTableRow arg="restart-policy" typ="枚举 (no | on-failure | always)"></ArgTableRow>
<ArgTableRow arg="restart-max-count" typ="数值"></ArgTableRow>
<ArgTableRow arg="restart-interval" typ="时间"></ArgTableRow>
<ArgTableRow arg="user" typ="字符串"></ArgTableRow>
<ArgTableRow arg="cpu-list" typ="多选 { 枚举
 }"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="数值"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="数值"></ArgTableRow>
<ArgTableRow arg="devices" typ="对象 { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="hosts" typ="对象 { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-cmd" typ="多选 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-interval" typ="时间"></ArgTableRow>
<ArgTableRow arg="healthcheck-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-period" typ="时间"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-interval" typ="时间"></ArgTableRow>
<ArgTableRow arg="healthcheck-retries" typ="数值"></ArgTableRow>
<ArgTableRow arg="healthcheck-status" typ="字符串"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="tag" typ="字符串"></ArgTableRow>
<ArgTableRow arg="os" typ="字符串"></ArgTableRow>
<ArgTableRow arg="arch" typ="字符串"></ArgTableRow>
<ArgTableRow arg="env-current" typ="对象 { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="default-entrypoint" typ="字符串"></ArgTableRow>
<ArgTableRow arg="default-cmd" typ="字符串"></ArgTableRow>
<ArgTableRow arg="default-shell" typ="字符串"></ArgTableRow>
<ArgTableRow arg="default-stop-signal" typ="枚举 (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
<ArgTableRow arg="default-workdir" typ="字符串"></ArgTableRow>
<ArgTableRow arg="restart-count" typ="数值"></ArgTableRow>
<ArgTableRow arg="default-user" typ="字符串"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="数值"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="数值"></ArgTableRow>
<ArgTableRow arg="container-size" typ="数值"></ArgTableRow>
<ArgTableRow arg="data-size" typ="数值"></ArgTableRow>
<ArgTableRow arg="image-id" typ="字符串"></ArgTableRow>
<ArgTableRow arg="config-json" typ="字符串"></ArgTableRow>
<ArgTableRow arg="layers" typ="多选 { 枚举
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-cmd" typ="多选 { 字符串
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-interval" typ="时间"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-timeout" typ="时间"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-period" typ="时间"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-interval" typ="时间"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-retries" typ="数值"></ArgTableRow>
</ArgTable>

## container/config

**软件包:** container
**类型:** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="registry-url" typ="字符串"></ArgTableRow>
<ArgTableRow arg="username" typ="字符串"></ArgTableRow>
<ArgTableRow arg="password" typ="字符串"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="文件"></ArgTableRow>
<ArgTableRow arg="tmpdir" typ="文件"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="数值"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="数值"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="assumed-registry-url" typ="字符串"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="数值"></ArgTableRow>
</ArgTable>

## container/envs

**软件包:** container
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="枚举" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="字符串" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="字符串" mandatory="1"></ArgTableRow>
</ArgTable>

## container/kill

**软件包:** container
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="signal" typ="枚举 (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
</ArgTable>

## container/layers

**软件包:** container
**类型:** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="字符串"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="字符串"></ArgTableRow>
<ArgTableRow arg="size" typ="可选 { 数值
, 枚举 (unavailable | pending | done) { unavailable:container::LAYER_SIZE_STATE_NONE, pending:container::LAYER_SIZE_STATE_PENDING, done:container::LAYER_SIZE_STATE_DONE }
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="枚举 (layer | root-dir)"></ArgTableRow>
<ArgTableRow arg="containers" typ="多选 { 枚举
 }"></ArgTableRow>
</ArgTable>

## container/log

**软件包:** container
**类型:** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="time" typ="日期"></ArgTableRow>
<ArgTableRow arg="container" typ="枚举"></ArgTableRow>
<ArgTableRow arg="message" typ="字符串"></ArgTableRow>
</ArgTable>

## container/mounts

**软件包:** container
**类型:** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="已禁用"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="list" typ="枚举" mandatory="1"></ArgTableRow>
<ArgTableRow arg="src" typ="文件"></ArgTableRow>
<ArgTableRow arg="dst" typ="字符串" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="枚举 (rw | ro | rw,noexec | ro,noexec)"></ArgTableRow>
</ArgTable>

## container/repull

**软件包:** container
**类型:** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="file" typ="文件 {  }"></ArgTableRow>
<ArgTableRow arg="remote-image" typ="字符串"></ArgTableRow>
</ArgTable>

## container/restart

**软件包:** container
**类型:** 命令

## container/start

**软件包:** container
**类型:** 命令

## container/stop

**软件包:** container
**类型:** 命令

## container/update

**软件包:** container
**类型:** 命令