# 资源

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/resource

**适用条件：** !powerpc, !smips
**类型：** 设置目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="uptime" typ="time"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="build-time" typ="string"></ArgTableRow>
<ArgTableRow arg="factory-software" typ="string"></ArgTableRow>
<ArgTableRow arg="free-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="total-memory" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu" typ="string"></ArgTableRow>
<ArgTableRow arg="cpu-count" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-load" typ="num"></ArgTableRow>
<ArgTableRow arg="free-hdd-space" typ="num"></ArgTableRow>
<ArgTableRow arg="total-hdd-space" typ="num"></ArgTableRow>
<ArgTableRow arg="write-sect-since-reboot" typ="num"></ArgTableRow>
<ArgTableRow arg="write-sect-total" typ="num"></ArgTableRow>
<ArgTableRow arg="bad-blocks" typ="num"></ArgTableRow>
<ArgTableRow arg="architecture-name" typ="string"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="platform" typ="string"></ArgTableRow>
</ArgTable>

### system/resource/cpu

**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="cpu" typ="string"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="disk" typ="num"></ArgTableRow>
</ArgTable>

### system/resource/hardware

**适用条件：** !powerpc, !smips, i386
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="location" typ="string"></ArgTableRow>
<ArgTableRow arg="parent" typ="enum"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (usb | pci | scsi | serial)"></ArgTableRow>
<ArgTableRow arg="vendor" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="category" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="vendor-id" typ="string"></ArgTableRow>
<ArgTableRow arg="device-id" typ="string"></ArgTableRow>
<ArgTableRow arg="speed" typ="string"></ArgTableRow>
<ArgTableRow arg="ports" typ="num"></ArgTableRow>
<ArgTableRow arg="usb-version" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacturer-reported-max-power" typ="string"></ArgTableRow>
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="memory" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="io" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="owner" typ="string"></ArgTableRow>
<ArgTableRow arg="device-path" typ="multi { string
 }"></ArgTableRow>
</ArgTable>

#### system/resource/hardware/authorize

**适用条件：** !powerpc, !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="allow" typ="bool"></ArgTableRow>
</ArgTable>

#### system/resource/hardware/usb-power-reset

**适用条件：** !powerpc, !smips, i386
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="bus" typ="num"></ArgTableRow>
<ArgTableRow arg="slot" typ="num"></ArgTableRow>
</ArgTable>

#### system/resource/hardware/usb-settings

**适用条件：** !powerpc, !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="authorization" typ="bool"></ArgTableRow>
</ArgTable>

### system/resource/irq

**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="o" typ="read-only"></ArgTableRow>
</ArgTable>

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="users" typ="object { alt { iface_enum
, string
 } { iface_enum
, string
 }
 }"></ArgTableRow>
<ArgTableRow arg="active-cpu" typ="num"></ArgTableRow>
<ArgTableRow arg="count" typ="num"></ArgTableRow>
<ArgTableRow arg="per-cpu-count" typ="multi { num
 }"></ArgTableRow>
</ArgTable>

#### system/resource/irq/rps

**系统能力：** rps
**类型：** 目录

<ArgTable c1="标志" c2="名称" c3="描述">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="name" typ="iface_enum"></ArgTableRow>
</ArgTable>

### system/resource/monitor

**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="cpu-used" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-used-per-core" typ="multi { num
 }" syscap="smp"></ArgTableRow>
<ArgTableRow arg="free-memory" typ="num"></ArgTableRow>
</ArgTable>