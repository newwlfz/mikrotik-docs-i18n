# Media

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## ip/media

**Conditions:** !smips
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="path" typ="file"></ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="friendly-name" typ="string"></ArgTableRow>
<ArgTableRow arg="allowed-ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="allowed-hostname" typ="string">Only IP address of this hostname (as known to DHCP server) will be allowed to access content</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### ip/media/settings

**Conditions:** !smips
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="thumbnails" typ="string">Comma separated list of filenames (should end with .jpg). If name of a file in a directory matches any filename in the list, that file is treated as a thumbnail to any media file in that directory.</ArgTableRow>
</ArgTable>
