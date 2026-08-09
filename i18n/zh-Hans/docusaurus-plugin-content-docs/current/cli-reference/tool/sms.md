# 短信

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## tool/sms

**条件：** !smips
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="receive-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="port" typ="alt { enum
, iface_enum { none:nv::BADID } { none:nv::BADID }
 }"></ArgTableRow>
<ArgTableRow arg="channel" typ="num"></ArgTableRow>
<ArgTableRow arg="secret" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-number" typ="multi { array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="sim-pin" typ="string"></ArgTableRow>
<ArgTableRow arg="sms-storage" typ="enum (modem | sim | combined)">用于读取、写入、发送和接收操作的存储器（ETSI TS 127 005中的`<mem1>`、`<mem2>`和`<mem3>`），将在后续的+CPMS命令中使用（该设置仅在仅使用AT命令时生效）</ArgTableRow>
<ArgTableRow arg="polling" typ="bool">每5秒轮询一次新短信。建议仅在通过其他方式接收新短信出现问题时才启用轮询。</ArgTableRow>
<ArgTableRow arg="remove-sent-sms-after-send" typ="bool">当调制解调器自动存储已发送短信时非常有用</ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="bool"></ArgTableRow>
<ArgTableRow arg="last-ussd" typ="string"></ArgTableRow>
</ArgTable>

### tool/sms/inbox

**条件：** !smips
**类型：** 目录

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="source" typ="string"></ArgTableRow>
<ArgTableRow arg="phone" typ="string"></ArgTableRow>
<ArgTableRow arg="type" typ="enum (class-0)"></ArgTableRow>
<ArgTableRow arg="timestamp" typ="string"></ArgTableRow>
<ArgTableRow arg="message" typ="string"></ArgTableRow>
<ArgTableRow arg="pdu" typ="string"></ArgTableRow>
</ArgTable>

### tool/sms/send

**条件：** !smips
**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
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