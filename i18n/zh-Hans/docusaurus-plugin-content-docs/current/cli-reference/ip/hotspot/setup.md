# 设置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### ip/hotspot/setup

**软件包：** hotspot
**类型：** 命令

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="interface" typ="alt { iface_enum
, iface_enum
 }"></ArgTableRow>
<ArgTableRow arg="address" typ="composite { ,  }"></ArgTableRow>
<ArgTableRow arg="masq" typ="bool"></ArgTableRow>
<ArgTableRow arg="pool" typ="multi { , , composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="ssl-cert" typ="enum (import-other-certificate | none)"></ArgTableRow>
<ArgTableRow arg="passphrase" typ="string"></ArgTableRow>
<ArgTableRow arg="smtp-server" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="use-dnscache" typ="bool"></ArgTableRow>
<ArgTableRow arg="dns-server" typ="multi { , ipAddr
 }"></ArgTableRow>
<ArgTableRow arg="dns-name" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>