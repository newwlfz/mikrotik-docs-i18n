# Resource

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/resource

**Conditions:** !powerpc, !smips
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="string"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="irq" typ="num"></ArgTableRow>
<ArgTableRow arg="disk" typ="num"></ArgTableRow>
</ArgTable>

### system/resource/hardware

**Conditions:** !powerpc, !smips, i386
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="I" typ="inactive"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Conditions:** !powerpc, !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="allow" typ="bool"></ArgTableRow>
</ArgTable>

#### system/resource/hardware/usb-power-reset

**Conditions:** !powerpc, !smips, i386
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="bus" typ="num"></ArgTableRow>
<ArgTableRow arg="slot" typ="num"></ArgTableRow>
</ArgTable>

#### system/resource/hardware/usb-settings

**Conditions:** !powerpc, !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="authorization" typ="bool"></ArgTableRow>
</ArgTable>

### system/resource/irq

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="o" typ="read-only"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu" typ="num"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
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

**Syscap:** rps
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="iface_enum"></ArgTableRow>
</ArgTable>

### system/resource/monitor

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="cpu-used" typ="num"></ArgTableRow>
<ArgTableRow arg="cpu-used-per-core" typ="multi { num
 }" syscap="smp"></ArgTableRow>
<ArgTableRow arg="free-memory" typ="num"></ArgTableRow>
</ArgTable>
