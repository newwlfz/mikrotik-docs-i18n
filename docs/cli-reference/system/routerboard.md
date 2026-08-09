# Routerboard

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/routerboard

**Conditions:** !i386, !i386, !mipsel, !powerpc
**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="routerboard" typ="bool"></ArgTableRow>
<ArgTableRow arg="board-name" typ="string"></ArgTableRow>
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="revision" typ="string"></ArgTableRow>
<ArgTableRow arg="serial-number" typ="string"></ArgTableRow>
<ArgTableRow arg="firmware-type" typ="string"></ArgTableRow>
<ArgTableRow arg="factory-firmware" typ="string"></ArgTableRow>
<ArgTableRow arg="current-firmware" typ="string"></ArgTableRow>
<ArgTableRow arg="upgrade-firmware" typ="string"></ArgTableRow>
</ArgTable>

### system/routerboard/mode-button

**Conditions:** !i386
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

### system/routerboard/reset-button

**Conditions:** !i386
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>

### system/routerboard/settings

**Conditions:** !i386, !i386
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="auto-upgrade" typ="bool"></ArgTableRow>
<ArgTableRow arg="baud-rate" typ="enum (115200 | 57600 | 38400 | 19200 | 9600 | 4800 | 2400 | 1200)"></ArgTableRow>
<ArgTableRow arg="boot-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="init-delay" typ="time"></ArgTableRow>
<ArgTableRow arg="enter-setup-on" typ="enum (any-key | delete-key)"></ArgTableRow>
<ArgTableRow arg="boot-device" typ="enum"></ArgTableRow>
<ArgTableRow arg="preboot-etherboot" typ="alt { enum (disabled) { disabled:0 }
, time [1 .. 30]
 }"></ArgTableRow>
<ArgTableRow arg="preboot-etherboot-server" typ="alt { enum (any) { any:0 }
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="etherboot-port" typ="enum (ether1 | ether2)"></ArgTableRow>
<ArgTableRow arg="boot-os" typ="enum (router-os | swos)"></ArgTableRow>
<ArgTableRow arg="regulatory-domain-ce" typ="bool"></ArgTableRow>
<ArgTableRow arg="cpu-mode" typ="enum (power-save | regular)"></ArgTableRow>
<ArgTableRow arg="cpu-frequency" typ="enum"></ArgTableRow>
<ArgTableRow arg="memory-frequency" typ="enum"></ArgTableRow>
<ArgTableRow arg="memory-data-rate" typ="enum"></ArgTableRow>
<ArgTableRow arg="preferred-architecture" typ="enum (arm32 | arm64)"></ArgTableRow>
<ArgTableRow arg="boot-protocol" typ="enum (bootp | dhcp)"></ArgTableRow>
<ArgTableRow arg="enable-jumper-reset" typ="bool"></ArgTableRow>
<ArgTableRow arg="force-backup-booter" typ="bool"></ArgTableRow>
<ArgTableRow arg="silent-boot" typ="bool"></ArgTableRow>
<ArgTableRow arg="disable-pci" typ="bool"></ArgTableRow>
<ArgTableRow arg="gpio-function" typ="ubit (serial1)"></ArgTableRow>
<ArgTableRow arg="protected-routerboot" typ="bool"></ArgTableRow>
<ArgTableRow arg="reformat-hold-button" typ="time"></ArgTableRow>
<ArgTableRow arg="reformat-hold-button-max" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="safe-cpu-frequency" typ="enum"></ArgTableRow>
</ArgTable>

#### system/routerboard/settings/keep-frequency

**Conditions:** !i386, mipsel
**Type:** Command

### system/routerboard/upgrade

**Conditions:** !i386
**Type:** Command

### system/routerboard/usb

**Conditions:** !i386, !i386, !mipsel, !powerpc
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (USB-type-A | mini-PCIe | auto)"></ArgTableRow>
<ArgTableRow arg="usb-mode" typ="enum (automatic | force-host)"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="auto-type" typ="enum (USB-type-A | mini-PCIe)"></ArgTableRow>
<ArgTableRow arg="bootstrap" typ="enum (host-mode | device-mode)"></ArgTableRow>
</ArgTable>

#### system/routerboard/usb/power-reset

**Conditions:** !i386, !i386, !mipsel, !powerpc
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="duration" typ="time"></ArgTableRow>
<ArgTableRow arg="bus" typ="num"></ArgTableRow>
</ArgTable>

### system/routerboard/wps-button

**Conditions:** !i386
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="hold-time" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="on-event" typ="alt { , string
 }"></ArgTableRow>
</ArgTable>
