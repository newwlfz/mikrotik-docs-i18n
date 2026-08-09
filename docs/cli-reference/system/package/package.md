# Package

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

## system/package

**Type:** Directory

Commands executed in this menu will take place only on the restart of the router. Until then, you can freely schedule or revert the set actions.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled"></ArgTableRow>
<ArgTableRow arg="A" typ="available"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the package.</ArgTableRow>
<ArgTableRow arg="version" typ="string">Version of the package.</ArgTableRow>
<ArgTableRow arg="build-time" typ="date">Date and time the package was built.</ArgTableRow>
<ArgTableRow arg="scheduled" typ="enum ( | scheduled for uninstall | scheduled for disable | scheduled for enable | Use `apply-changes` to proceed with install)">Scheduled action for the package after the next reboot.</ArgTableRow>
<ArgTableRow arg="bundle" typ="enum">The bundle package this package belongs to.</ArgTableRow>
<ArgTableRow arg="size" typ="num">Size of the package in bytes.</ArgTableRow>
</ArgTable>

### system/package/apply-changes

**Type:** Command

Apply scheduled changes and reboot the device.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">Upgrade only the RouterOS main package, omitting packages that are missing or not uploaded.</ArgTableRow>
</ArgTable>

### system/package/disable

**Type:** Command

Schedule the package to be disabled after the next reboot. No features provided by the package will be accessible.

### system/package/downgrade

**Type:** Command

Prompt for a reboot. During the reboot process, the router will try to downgrade RouterOS to the oldest version possible by checking the packages that are uploaded to the router.

### system/package/enable

**Type:** Command

### system/package/uninstall

**Type:** Command

Schedule the package to be removed from the router. That will take place during the reboot.

### system/package/unschedule

**Type:** Command

### system/package/update

**Type:** Settings Directory

Manage the `check-for-updates` channel and perform RouterOS upgrades.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="channel" typ="enum ()">Upgrade [channel](#channel) to use when checking for new versions.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum ()">Protocol for connecting to the MikroTik download server. Use `http` only if your network blocks HTTPS. HTTPS is recommended.</ArgTableRow>
<ArgTableRow arg="check-certificate" typ="enum ()">Whether and how to validate the server SSL certificate. Always use `yes` to ensure a secure connection.</ArgTableRow>
<ArgTableRow arg="ip-version" typ="enum ()">IP version preference for connecting to the MikroTik download server.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="installed-version" typ="string">Currently installed RouterOS version.</ArgTableRow>
<ArgTableRow arg="latest-version" typ="string">Latest available RouterOS version in the selected [channel](#channel).</ArgTableRow>
<ArgTableRow arg="status" typ="string">Current status of the update process (for example, `New version is available`).</ArgTableRow>
</ArgTable>

#### system/package/update/cancel

**Type:** Command

#### system/package/update/check-for-updates

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="fetch-changelog" typ="switch">Whether to fetch the changelog along with the update check.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="changelog" typ="string">Changelog text for the latest available version.</ArgTableRow>
</ArgTable>

#### system/package/update/download

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">Download only the RouterOS main package, omitting packages that are missing or not uploaded.</ArgTableRow>
</ArgTable>

#### system/package/update/install

**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="ignore-missing" typ="bool" unset="1">Install only the RouterOS main package, omitting packages that are missing or not uploaded.</ArgTableRow>
</ArgTable>
