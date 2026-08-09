# Serial Interface

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/serial-interface/read

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum">name of the port from port list</ArgTableRow>
<ArgTableRow arg="time" typ="time">timeout for serial terminal access (capture mode)</ArgTableRow>
<ArgTableRow arg="size" typ="num">maximum bytes read from the serial terminal (capture mode)</ArgTableRow>
<ArgTableRow arg="until" typ="string">read from the serial terminal until provided character sequence (capture mode)</ArgTableRow>
<ArgTableRow arg="as-string" typ="switch">do not interpret output as a console value (in capture mode)</ArgTableRow>
</ArgTable>

### system/serial-interface/serial-terminal

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum">name of the port from port list</ArgTableRow>
<ArgTableRow arg="channel" typ="num">port channel that will be used (0 by default)</ArgTableRow>
<ArgTableRow arg="write" typ="string">non-interactively write provided value to the serial terminal</ArgTableRow>
</ArgTable>

### system/serial-interface/start

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum">name of the port from port list</ArgTableRow>
<ArgTableRow arg="channel" typ="num">port channel that will be used (0 by default)</ArgTableRow>
</ArgTable>

### system/serial-interface/stop

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum">name of the port from port list</ArgTableRow>
<ArgTableRow arg="channel" typ="num">port channel that will be used (0 by default)</ArgTableRow>
</ArgTable>

### system/serial-interface/write

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="port" typ="enum">name of the port from port list</ArgTableRow>
<ArgTableRow arg="data" typ="string">non-interactively write provided value to the serial terminal</ArgTableRow>
</ArgTable>
