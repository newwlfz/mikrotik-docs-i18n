# task

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# task

**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="T" typ="terminated">terminated</ArgTableRow>
<ArgTableRow arg="C" typ="current">current</ArgTableRow>
<ArgTableRow arg="A" typ="autosave">autosave</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="term-pid" typ="num"></ArgTableRow>
<ArgTableRow arg="task-id" typ="num"></ArgTableRow>
<ArgTableRow arg="user" typ="string"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="source" typ="string"></ArgTableRow>
<ArgTableRow arg="file-name" typ="string"></ArgTableRow>
<ArgTableRow arg="save-interval" typ="time"></ArgTableRow>
<ArgTableRow arg="append" typ="switch"></ArgTableRow>
</ArgTable>

## task/add

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="source" typ="string">command that should be executed in the background</ArgTableRow>
<ArgTableRow arg="switch-to" typ="switch">switch to background view immediately</ArgTableRow>
<ArgTableRow arg="append" typ="switch">append output to file</ArgTableRow>
<ArgTableRow arg="file-name" typ="file">default filename for output</ArgTableRow>
<ArgTableRow arg="save-interval" typ="time">autosave interval for when filename is set</ArgTableRow>
<ArgTableRow arg="max-lines" typ="num">maximum buffer lines</ArgTableRow>
<ArgTableRow arg="save-timestamp" typ="switch">add a timestamp to the saved file</ArgTableRow>
<ArgTableRow arg="no-header-paging" typ="switch">don't page header to output</ArgTableRow>
<ArgTableRow arg="max-size" typ="num">maximum save file size</ArgTableRow>
</ArgTable>

## task/next

**Type:** Command

## task/terminate

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="id" typ="num"></ArgTableRow>
</ArgTable>
