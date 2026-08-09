# Ups

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/ups

**Package:** ups
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="port" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="offline-time" typ="time"></ArgTableRow>
<ArgTableRow arg="min-runtime" typ="alt { enum (never) { never:0xffffffff }
, time
 }"></ArgTableRow>
<ArgTableRow arg="alarm-setting" typ="enum (immediate | delayed | low-battery | none)"></ArgTableRow>
<ArgTableRow arg="check-capabilities" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="model" typ="string"></ArgTableRow>
<ArgTableRow arg="version" typ="string"></ArgTableRow>
<ArgTableRow arg="serial" typ="string"></ArgTableRow>
<ArgTableRow arg="manufacture-date" typ="string"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="on-line" typ="bool"></ArgTableRow>
<ArgTableRow arg="nominal-battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="offline-after" typ="time"></ArgTableRow>
</ArgTable>

### system/ups/beep

**Package:** ups
**Type:** Command

### system/ups/monitor

**Package:** ups
**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="on-line" typ="bool"></ArgTableRow>
<ArgTableRow arg="on-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="transfer-cause" typ="string"></ArgTableRow>
<ArgTableRow arg="rtc-running" typ="bool"></ArgTableRow>
<ArgTableRow arg="runtime-left" typ="time"></ArgTableRow>
<ArgTableRow arg="offline-after" typ="time"></ArgTableRow>
<ArgTableRow arg="battery-charge" typ="num"></ArgTableRow>
<ArgTableRow arg="battery-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="line-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="output-voltage" typ="num"></ArgTableRow>
<ArgTableRow arg="load" typ="num"></ArgTableRow>
<ArgTableRow arg="temperature" typ="num"></ArgTableRow>
<ArgTableRow arg="frequency" typ="num"></ArgTableRow>
<ArgTableRow arg="replace-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-boost" typ="bool"></ArgTableRow>
<ArgTableRow arg="smart-trim" typ="bool"></ArgTableRow>
<ArgTableRow arg="overload" typ="bool"></ArgTableRow>
<ArgTableRow arg="low-battery" typ="bool"></ArgTableRow>
<ArgTableRow arg="self-test" typ="string"></ArgTableRow>
<ArgTableRow arg="hid-self-test" typ="enum (done-and-passed | done-and-warning | done-and-error | aborted | in-progress | no-test-initiated)"></ArgTableRow>
</ArgTable>

### system/ups/rtc

**Package:** ups
**Type:** Command

### system/ups/self-test

**Package:** ups
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="hid-test-type" typ="enum (quick | deep | abort)"></ArgTableRow>
</ArgTable>
