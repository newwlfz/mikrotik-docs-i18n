# 重置配置

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/reset-configuration

**类型：** 命令

<ArgTable c1="参数" c2="类型" c3="描述">
<ArgTableRow arg="keep-users" typ="bool"></ArgTableRow>
<ArgTableRow arg="keep-apps" typ="bool"></ArgTableRow>
<ArgTableRow arg="no-defaults" typ="bool"></ArgTableRow>
<ArgTableRow arg="caps-mode" typ="bool"></ArgTableRow>
<ArgTableRow arg="wps-sync-mode" typ="bool" syscap="wpssync"></ArgTableRow>
<ArgTableRow arg="skip-backup" typ="bool"></ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool"></ArgTableRow>
<ArgTableRow arg="shutdown" typ="bool"></ArgTableRow>
<ArgTableRow arg="run-after-reset" typ="file {  }">.rsc 文件</ArgTableRow>
</ArgTable>