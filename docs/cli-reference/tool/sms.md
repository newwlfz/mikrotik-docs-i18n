# Sms

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/sms

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="receive-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { enum
, iface_enum { none:nv::BADID } { none:nv::BADID }
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-number" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="sim-pin" typ="string"></ArgTableRow>
<ArgTableRow arg="sms-storage" typ="enum (modem | sim | combined)">Memory for reading, writing, sending and receiving operations (`<mem1>`, `<mem2>` and `<mem3>` in ETSI TS 127 005), will be used in further +CPMS commands (setting effective when using AT commands only)</ArgTableRow>
<ArgTableRow arg="polling" typ="bool">Poll new SMS every 5s. It's recommended to enable polling only when there are problems with receiving new SMS otherwise.</ArgTableRow>
<ArgTableRow arg="remove-sent-sms-after-send" typ="bool">Useful when modem automatically stores sent SMS</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-ussd" typ="string"></ArgTableRow>
</ArgTable>

### tool/sms/inbox

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="source" typ="string"></ArgTableRow>
<ArgTableRow arg="phone" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (class-0)"></ArgTableRow>
<ArgTableRow arg="timestamp" typ="string"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
<ArgTableRow arg="pdu" typ="string"></ArgTableRow>
</ArgTable>

### tool/sms/send

**Conditions:** !smips
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="alt { enum
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="phone-number" typ="string"></ArgTableRow>
<ArgTableRow arg="smsc" typ="string"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (class-1 | class-0 | ussd)"></ArgTableRow>
<ArgTableRow arg="status-report-request" typ="bool"></ArgTableRow>
</ArgTable>
