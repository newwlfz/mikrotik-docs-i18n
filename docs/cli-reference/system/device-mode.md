# Device Mode

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/device-mode

**Type:** Settings Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="allowed-versions" typ="string"></ArgTableRow>
<ArgTableRow arg="flagged" typ="bool"></ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool"></ArgTableRow>
<ArgTableRow arg="socks" typ="bool"></ArgTableRow>
<ArgTableRow arg="fetch" typ="bool"></ArgTableRow>
<ArgTableRow arg="pptp" typ="bool"></ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool"></ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool"></ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool"></ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool"></ArgTableRow>
<ArgTableRow arg="romon" typ="bool"></ArgTableRow>
<ArgTableRow arg="proxy" typ="bool"></ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool"></ArgTableRow>
<ArgTableRow arg="smb" typ="bool"></ArgTableRow>
<ArgTableRow arg="email" typ="bool"></ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool"></ArgTableRow>
<ArgTableRow arg="container" typ="bool"></ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool"></ArgTableRow>
<ArgTableRow arg="partitions" typ="bool"></ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool"></ArgTableRow>
<ArgTableRow arg="attempt-count" typ="num"></ArgTableRow>
</ArgTable>

### system/device-mode/update

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="mode" typ="enum"></ArgTableRow>
<ArgTableRow arg="flagged" typ="bool"></ArgTableRow>
<ArgTableRow arg="flagging-enabled" typ="bool"></ArgTableRow>
<ArgTableRow arg="scheduler" typ="bool"></ArgTableRow>
<ArgTableRow arg="socks" typ="bool"></ArgTableRow>
<ArgTableRow arg="fetch" typ="bool"></ArgTableRow>
<ArgTableRow arg="pptp" typ="bool"></ArgTableRow>
<ArgTableRow arg="l2tp" typ="bool"></ArgTableRow>
<ArgTableRow arg="bandwidth-test" typ="bool"></ArgTableRow>
<ArgTableRow arg="traffic-gen" typ="bool"></ArgTableRow>
<ArgTableRow arg="sniffer" typ="bool"></ArgTableRow>
<ArgTableRow arg="ipsec" typ="bool"></ArgTableRow>
<ArgTableRow arg="romon" typ="bool"></ArgTableRow>
<ArgTableRow arg="proxy" typ="bool"></ArgTableRow>
<ArgTableRow arg="hotspot" typ="bool"></ArgTableRow>
<ArgTableRow arg="smb" typ="bool"></ArgTableRow>
<ArgTableRow arg="email" typ="bool"></ArgTableRow>
<ArgTableRow arg="zerotier" typ="bool"></ArgTableRow>
<ArgTableRow arg="container" typ="bool"></ArgTableRow>
<ArgTableRow arg="install-any-version" typ="bool"></ArgTableRow>
<ArgTableRow arg="partitions" typ="bool"></ArgTableRow>
<ArgTableRow arg="routerboard" typ="bool"></ArgTableRow>
<ArgTableRow arg="activation-timeout" typ="time"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="update" typ="string"></ArgTableRow>
</ArgTable>
