# Watchdog

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/watchdog

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="watch-address" typ="alt { ipAddr
, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="watchdog-timer" typ="bool"></ArgTableRow>
<ArgTableRow arg="ping-start-after-boot" typ="time"></ArgTableRow>
<ArgTableRow arg="ping-timeout" typ="time"></ArgTableRow>
<ArgTableRow arg="automatic-supout" typ="bool"></ArgTableRow>
<ArgTableRow arg="auto-send-supout" typ="bool"></ArgTableRow>
<ArgTableRow arg="send-email-to" typ="string"></ArgTableRow>
<ArgTableRow arg="send-email-from" typ="string"></ArgTableRow>
<ArgTableRow arg="send-smtp-server" typ="alt { ipAddr
, string
 }"></ArgTableRow>
</ArgTable>
