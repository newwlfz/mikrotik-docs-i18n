# Local Update

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

### system/package/local-update

**Type:** Directory

Instead of connecting directly to MikroTik servers, you can upload package files to one of your local RouterOS devices and use it as a local package server.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="download" typ="bool">Whether to download available packages from the local package server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="source" typ="alt { ip6Addr
, ipAddr
 }">IP address of the local package server.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the package.</ArgTableRow>
<ArgTableRow arg="version" typ="string">Version of the package.</ArgTableRow>
<ArgTableRow arg="status" typ="enum (installed | downloaded | downloading | scheduled | available)">Current status of the package.</ArgTableRow>
<ArgTableRow arg="completed" typ="num">Download completion percentage.</ArgTableRow>
</ArgTable>

#### system/package/local-update/download

**Type:** Command

Download specific compatible (matching device architecture) packages that are available on the local package server. Downloaded packages are saved in the root directory.

#### system/package/local-update/download-all

**Type:** Command

Download all compatible (matching device architecture) packages that are available on the local package server. Downloaded packages are saved in the root directory.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="download-beta" typ="bool">Whether to include beta packages when downloading all compatible packages.</ArgTableRow>
<ArgTableRow arg="reboot-after-download" typ="bool">Whether to automatically reboot the device after all packages finish downloading.</ArgTableRow>
</ArgTable>

#### system/package/local-update/mirror

**Type:** Settings Directory

You can mirror packages (for all architectures) from your main local package server by using this menu. Downloaded packages are saved into the `packs` folder in the root directory.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="bool">Whether to enable periodic check and download of packages from the local package server.</ArgTableRow>
<ArgTableRow arg="primary-server" typ="alt { ip6Addr
, ipAddr
 }">IP address of the primary local package server.</ArgTableRow>
<ArgTableRow arg="secondary-server" typ="alt { ip6Addr
, ipAddr
 }">IP address of the secondary local package server.</ArgTableRow>
<ArgTableRow arg="check-interval" typ="time">Time interval at which the device checks the local package server for new package availability. If a new package is located, the package download begins. Only downloads the packages that are not already present on the device.</ArgTableRow>
<ArgTableRow arg="user" typ="string">Username for accessing the local package server.</ArgTableRow>
<ArgTableRow arg="password" typ="string">Password for accessing the local package server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="software-id" typ="string">Software ID of the device.</ArgTableRow>
</ArgTable>

##### system/package/local-update/mirror/force-check

**Type:** Command

#### system/package/local-update/refresh

**Type:** Command

Refresh and check the list of available compatible (matching device architecture) packages on the local package server.

#### system/package/local-update/update-package-source

**Type:** Directory

The server from which to get the package is defined in this list.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="address" typ="alt { ip6Addr
, ipAddr
 }" mandatory="1">IP address of the local package server.</ArgTableRow>
<ArgTableRow arg="user" typ="string" mandatory="1">Username for accessing the local package server.</ArgTableRow>
<ArgTableRow arg="password" typ="string" mandatory="1">Password for accessing the local package server.</ArgTableRow>
</ArgTable>
