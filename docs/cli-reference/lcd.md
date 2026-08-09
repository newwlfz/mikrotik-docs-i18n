# lcd

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# lcd

**Conditions:** !smips
**Syscap:** lcd
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="touch-screen" typ="bool"></ArgTableRow>
<ArgTableRow arg="backlight-timeout" typ="alt { enum (never) { never:0 }
, time [30s .. 2h]
 }"></ArgTableRow>
<ArgTableRow arg="read-only-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="time-interval" typ="enum (min | hour | daily | weekly)"></ArgTableRow>
<ArgTableRow arg="default-screen" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="color-scheme" typ="enum (dark | light)"></ArgTableRow>
<ArgTableRow arg="flip-screen" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/backlight

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="state" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/interface

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="I" typ="inactive">inactive</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="displayed">displayed</ArgTableRow>
<ArgTableRow arg="W" typ="default-wireless">default-wireless</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="max-speed" typ="num" mandatory="1"></ArgTableRow>
</ArgTable>

### lcd/interface/default-wireless

**Conditions:** !smips
**Type:** Command

### lcd/interface/display

**Conditions:** !smips
**Type:** Command

### lcd/interface/pages

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interfaces" typ="multi { array-id, iface_enum
 }" mandatory="1"></ArgTableRow>
</ArgTable>

## lcd/pin

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="pin-number" typ="string"></ArgTableRow>
<ArgTableRow arg="hide-pin-number" typ="bool"></ArgTableRow>
</ArgTable>

## lcd/recalibrate

**Conditions:** !smips
**Type:** Command

## lcd/screen

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">default</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
</ArgTable>

## lcd/show

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="screen" typ="enum ()"></ArgTableRow>
</ArgTable>

## lcd/take-screenshot

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
</ArgTable>
