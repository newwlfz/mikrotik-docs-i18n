# Reset Configuration

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/reset-configuration

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="keep-users" typ="bool"></ArgTableRow>
<ArgTableRow arg="keep-apps" typ="bool"></ArgTableRow>
<ArgTableRow arg="no-defaults" typ="bool"></ArgTableRow>
<ArgTableRow arg="caps-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="wps-sync-mode" typ="bool" syscap="wpssync"></ArgTableRow>
<ArgTableRow arg="skip-backup" typ="bool"></ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool"></ArgTableRow>
<ArgTableRow arg="shutdown" typ="bool"></ArgTableRow>
<ArgTableRow arg="run-after-reset" typ="file {  }">.rsc file</ArgTableRow>
</ArgTable>
