# Backup

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/backup

**Type:** Directory

### system/backup/cloud

**Type:** Directory

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="size" typ="num"></ArgTableRow>
<ArgTableRow arg="ros-version" typ="string"></ArgTableRow>
<ArgTableRow arg="date" typ="date"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="secret-download-key" typ="string"></ArgTableRow>
</ArgTable>

#### system/backup/cloud/download-file

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="secret-download-key" typ="string"></ArgTableRow>
<ArgTableRow arg="action" typ="enum (download | download-and-apply)"></ArgTableRow>
<ArgTableRow arg="dst-file" typ="string"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### system/backup/cloud/remove-file

**Type:** Command

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

#### system/backup/cloud/upload-file

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="action" typ="enum (upload | create-and-upload)"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="replace" typ="enum"></ArgTableRow>
<ArgTableRow arg="src-file" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string"></ArgTableRow>
</ArgTable>

### system/backup/load

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="force-v6-to-v7-configuration-upgrade" typ="bool"></ArgTableRow>
</ArgTable>

### system/backup/save

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="file {  }"></ArgTableRow>
<ArgTableRow arg="password" typ="string"></ArgTableRow>
<ArgTableRow arg="dont-encrypt" typ="bool"></ArgTableRow>
<ArgTableRow arg="encryption" typ="enum (aes-sha256 | rc4)"></ArgTableRow>
</ArgTable>
