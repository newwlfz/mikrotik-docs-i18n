# tr069-client

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# tr069-client

**软件包：** tr069-client
**类型：** 设置目录

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="acs-url" typ="string"></ArgTableRow>
<ArgTableRow arg="username" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="periodic-inform-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="periodic-inform-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="connection-request-username" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-request-password" typ="string"></ArgTableRow>
<ArgTableRow arg="connection-request-port" typ="num"></ArgTableRow>
<ArgTableRow arg="provisioning-code" typ="string"></ArgTableRow>
<ArgTableRow arg="client-certificate" typ="enum (none)"></ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum (yes | no)"></ArgTableRow>
</ArgTable>

<ArgTable c1="只读参数" c2="类型" c3="描述">
<ArgTableRow arg="status" typ="enum (disabled | initializing | error | waiting-url | running)"></ArgTableRow>
<ArgTableRow arg="last-session-error" typ="string"></ArgTableRow>
<ArgTableRow arg="retry-count" typ="num"></ArgTableRow>
</ArgTable>

## tr069-client/reset-tr069-config

**软件包：** tr069-client
**类型：** 命令