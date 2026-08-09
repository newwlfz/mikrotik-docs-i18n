# console

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# console

**Type:** Directory

## console/inspect

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="request" typ="ubit (self, child, completion, highlight, syntax, error)"></ArgTableRow>
<ArgTableRow arg="path" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="input" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (self | child | completion | highlight | syntax | error)"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="node-type" typ="enum (path | dir | cmd | arg)"></ArgTableRow>
<ArgTableRow arg="completion" typ="string"></ArgTableRow>
<ArgTableRow arg="style" typ="enum ()"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="preference" typ="num"></ArgTableRow>
<ArgTableRow arg="show" typ="bool"></ArgTableRow>
<ArgTableRow arg="highlight" typ="multi { , enum () {  }
 }"></ArgTableRow>
<ArgTableRow arg="symbol" typ="string"></ArgTableRow>
<ArgTableRow arg="symbol-type" typ="enum (collection | explanation | definition)"></ArgTableRow>
<ArgTableRow arg="nested" typ="num"></ArgTableRow>
<ArgTableRow arg="nonorm" typ="bool"></ArgTableRow>
<ArgTableRow arg="text" typ="string"></ArgTableRow>
</ArgTable>

## console/settings

**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="sanitize-names" typ="bool">replace reserved characters in file and script names with underscores</ArgTableRow>
<ArgTableRow arg="log-script-errors" typ="bool">write background script failures to log</ArgTableRow>
<ArgTableRow arg="tab-width" typ="num">default tab width in fullscreen editor</ArgTableRow>
</ArgTable>
