# Logging

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/logging

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="topics" typ="multi { array-id, array-id, super { !
, enum
 } { !
, enum
 }
 }"></ArgTableRow>
<ArgTableRow arg="prefix" typ="string"></ArgTableRow>
<ArgTableRow arg="regex" typ="string"></ArgTableRow>
<ArgTableRow arg="action" typ="enum"></ArgTableRow>
</ArgTable>

### system/logging/action

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default"></ArgTableRow>
<ArgTableRow arg="Y" typ="managed"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1"></ArgTableRow>
<ArgTableRow arg="target" typ="enum (memory | disk | echo | remote | email | script | cmr)" mandatory="1"></ArgTableRow>
<ArgTableRow arg="memory-lines" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="memory-stop-on-full" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="disk-file-name" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="disk-lines-per-file" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="disk-file-count" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="disk-stop-on-full" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="remote" typ="alt { , ip6Addr
, ipAddr
, string
 }"></ArgTableRow>
<ArgTableRow arg="remote-port" typ="num {  }"></ArgTableRow>
<ArgTableRow arg="src-address" typ="alt { , ip6Addr
, ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="remote-log-format" typ="enum (default | syslog | cef)"></ArgTableRow>
<ArgTableRow arg="remote-protocol" typ="enum (udp | tcp | tls)"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="cef-event-delimiter" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="syslog-time-format" typ="enum (bsd-syslog | iso8601)"></ArgTableRow>
<ArgTableRow arg="syslog-facility" typ="enum (kern | user | mail | daemon | auth | syslog | lpr | news | uucp | cron | authpriv | ftp | ntp | local0 | local1 | local2 | local3 | local4 | local5 | local6 | local7)"></ArgTableRow>
<ArgTableRow arg="syslog-severity" typ="enum (auto | emergency | alert | critical | error | warning | notice | info | debug)"></ArgTableRow>
<ArgTableRow arg="email-to" typ="string {  }"></ArgTableRow>
<ArgTableRow arg="email-cc" typ="multi { , array-id, string
 }"></ArgTableRow>
<ArgTableRow arg="email-start-tls" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="remember" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="add-topics-string" typ="bool {  }"></ArgTableRow>
<ArgTableRow arg="script" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="vrf" typ="enum ()"></ArgTableRow>
</ArgTable>

#### system/logging/action/clear

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="action" typ="enum"></ArgTableRow>
</ArgTable>
