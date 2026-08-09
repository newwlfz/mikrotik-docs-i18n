# container

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# container

**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="S" typ="stopped"></ArgTableRow>
<ArgTableRow arg="N" typ="starting"></ArgTableRow>
<ArgTableRow arg="R" typ="running"></ArgTableRow>
<ArgTableRow arg="T" typ="stopping"></ArgTableRow>
<ArgTableRow arg="E" typ="downloading/extracting"></ArgTableRow>
<ArgTableRow arg="D" typ="deleting"></ArgTableRow>
<ArgTableRow arg="F" typ="download/extract failed"></ArgTableRow>
<ArgTableRow arg="C" typ="starting-with-healthcheck"></ArgTableRow>
<ArgTableRow arg="H" typ="healthy"></ArgTableRow>
<ArgTableRow arg="U" typ="unhealthy"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="remote-image" typ="string"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="interface" typ="multi { iface_enum
 }" mandatory="1"></ArgTableRow>
<ArgTableRow arg="env" typ="object { super { !
, composite { ,  } { ,  }
 } { !
, composite { ,  } { ,  }
 }
 }"></ArgTableRow>
<ArgTableRow arg="envlists" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="entrypoint" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="cmd" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="shell" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
<ArgTableRow arg="stop-time" typ="time"></ArgTableRow>
<ArgTableRow arg="root-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="mount" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="tmpfs" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="mountlists" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="shm-size" typ="num"></ArgTableRow>
<ArgTableRow arg="dns" typ="multi { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="default-dns" typ="multi { address (flags=46)
 }"></ArgTableRow>
<ArgTableRow arg="hostname" typ="string"></ArgTableRow>
<ArgTableRow arg="domain-name" typ="string"></ArgTableRow>
<ArgTableRow arg="workdir" typ="string"></ArgTableRow>
<ArgTableRow arg="logging" typ="bool"></ArgTableRow>
<ArgTableRow arg="start-on-boot" typ="bool"></ArgTableRow>
<ArgTableRow arg="stop-on-unhealthy" typ="bool"></ArgTableRow>
<ArgTableRow arg="restart-policy" typ="enum (no | on-failure | always)"></ArgTableRow>
<ArgTableRow arg="restart-max-count" typ="num"></ArgTableRow>
<ArgTableRow arg="restart-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu-list" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="num"></ArgTableRow>
<ArgTableRow arg="devices" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="hosts" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-cmd" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="healthcheck-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-period" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-start-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="healthcheck-retries" typ="num"></ArgTableRow>
<ArgTableRow arg="healthcheck-status" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="tag" typ="string"></ArgTableRow>
<ArgTableRow arg="os" typ="string"></ArgTableRow>
<ArgTableRow arg="arch" typ="string"></ArgTableRow>
<ArgTableRow arg="env-current" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="default-entrypoint" typ="string"></ArgTableRow>
<ArgTableRow arg="default-cmd" typ="string"></ArgTableRow>
<ArgTableRow arg="default-shell" typ="string"></ArgTableRow>
<ArgTableRow arg="default-stop-signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
<ArgTableRow arg="default-workdir" typ="string"></ArgTableRow>
<ArgTableRow arg="restart-count" typ="num"></ArgTableRow>
<ArgTableRow arg="default-user" typ="string"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num"></ArgTableRow>
<ArgTableRow arg="container-size" typ="num"></ArgTableRow>
<ArgTableRow arg="data-size" typ="num"></ArgTableRow>
<ArgTableRow arg="image-id" typ="string"></ArgTableRow>
<ArgTableRow arg="config-json" typ="string"></ArgTableRow>
<ArgTableRow arg="layers" typ="multi { enum
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-cmd" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-period" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-start-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="default-healthcheck-retries" typ="num"></ArgTableRow>
</ArgTable>

## container/config

**Package:** container
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="registry-url" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="file"></ArgTableRow>
<ArgTableRow arg="tmpdir" typ="file"></ArgTableRow>
<ArgTableRow arg="memory-high" typ="num"></ArgTableRow>
<ArgTableRow arg="memory-max" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-registry-url" typ="string"></ArgTableRow>
<ArgTableRow arg="memory-current" typ="num"></ArgTableRow>
</ArgTable>

## container/envs

**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="key" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1"></ArgTableRow>
</ArgTable>

## container/kill

**Package:** container
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="signal" typ="enum (1-SIGHUP | 2-SIGINT | 3-SIGQUIT | 4-SIGILL | 5-SIGTRAP | 6-SIGABTR | 7-SIGBUS | 8-SIGFPE | 9-SIGKILL | 10-SIGUSR1 | 11-SIGSEGV | 12-SIGUSR2 | 13-SIGPIPE | 14-SIGALRM | 15-SIGTERM | 16-SIGSTKFLT | 17-SIGCHLD | 18-SIGCONT | 19-SIGSTOP | 20-SIGTSTP | 21-SIGTTIN | 22-SIGTTOU | 23-SIGURG | 24-SIGXCPU | 25-SIGXFSZ | 26-SIGVTALRM | 27-SIGPROF | 28-SIGWINCH | 29-SIGIO | 30-SIGPWR | 31-SIGSYS)"></ArgTableRow>
</ArgTable>

## container/layers

**Package:** container
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="layer-dir" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="alt { num
, enum (unavailable | pending | done) { unavailable:container::LAYER_SIZE_STATE_NONE, pending:container::LAYER_SIZE_STATE_PENDING, done:container::LAYER_SIZE_STATE_DONE }
 }"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (layer | root-dir)"></ArgTableRow>
<ArgTableRow arg="containers" typ="multi { enum
 }"></ArgTableRow>
</ArgTable>

## container/log

**Package:** container
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="time" typ="date"></ArgTableRow>
<ArgTableRow arg="container" typ="enum"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
</ArgTable>

## container/mounts

**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="src" typ="file"></ArgTableRow>
<ArgTableRow arg="dst" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="mode" typ="enum (rw | ro | rw,noexec | ro,noexec)"></ArgTableRow>
</ArgTable>

## container/repull

**Package:** container
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="remote-image" typ="string"></ArgTableRow>
</ArgTable>

## container/restart

**Package:** container
**Type:** Command

## container/start

**Package:** container
**Type:** Command

## container/stop

**Package:** container
**Type:** Command

## container/update

**Package:** container
**Type:** Command
