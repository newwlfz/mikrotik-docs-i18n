# app

> -----------

import {ArgTableRow} from '@site/src/components/common';
import {ArgTable} from '@site/src/components/common';

-----------

# app

**Syscap:** app
**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Application is disabled (not downloaded/installed or downloaded but disabled)</ArgTableRow>
<ArgTableRow arg="R" typ="running">Application is actively running and accessible</ArgTableRow>
<ArgTableRow arg="c" typ="custom">Custom application created by the user</ArgTableRow>
<ArgTableRow arg="s" typ="from-app-store">Application installed from a custom app store</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="container-command-lines" typ="object { composite { ,  } { ,  }
 }">Specifies the command-line argument(s) to pass to the application when starting the container</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">Enables or disables automatic updating when a new container image version is available</ArgTableRow>
<ArgTableRow arg="use-https" typ="bool">Uses HTTPS for the application URL. This option will not work on devices that do not support cloud services</ArgTableRow>
<ArgTableRow arg="network" typ="enum (default)">Specifies which network the container will use: internal (behind NAT), lan (on the LAN network), or default (varies per application)</ArgTableRow>
<ArgTableRow arg="network-pvid" typ="num">Sets the Port VLAN ID (PVID) for the container's virtual Ethernet interface in the bridge</ArgTableRow>
<ArgTableRow arg="network-outgoing-access" typ="bool">Allows network outgoing access for the specific container app. When set to no, a mangle drop rule is created</ArgTableRow>
<ArgTableRow arg="firewall-redirects" typ="object { composite { ,  } { ,  }
 }">Configures port redirection from the host device to the container</ArgTableRow>
<ArgTableRow arg="yaml" typ="string">Provides the YAML composition for the application. See the documentation for configuration examples</ArgTableRow>
<ArgTableRow arg="required-mounts" typ="object { composite { ,  } { ,  }
 }">Mount directories required for the container to start. Format: [dir-on-host]:[dir-in-app]</ArgTableRow>
<ArgTableRow arg="extra-mounts" typ="object { composite { ,  } { ,  }
 }">Specifies additional mount points to attach to the container</ArgTableRow>
<ArgTableRow arg="environment" typ="object { super { !
, composite { ,  } { ,  }
  } { !
, composite { ,  } { ,  }
  }
 }">Defines environment variables to be available to the running application. Specify as a list of key-value pair(s)</ArgTableRow>
<ArgTableRow arg="secrets" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="required-hw-devices" typ="object { composite { ,  } { ,  }
 }">Hardware devices that must be present on the host for the container to start. Format: [host-hw-device]:[device-in-app]</ArgTableRow>
<ArgTableRow arg="devices" typ="object { composite { ,  } { ,  }
 }">Specifies additional hardware devices to pass through to the container application</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="app-store-url" typ="string">The URL of the app store from which the application was installed</ArgTableRow>
<ArgTableRow arg="name" typ="string">The application name as defined in the YAML configuration</ArgTableRow>
<ArgTableRow arg="description" typ="string">The application description as defined in the YAML configuration</ArgTableRow>
<ArgTableRow arg="project-page" typ="string">The application project page URL as defined in the YAML configuration</ArgTableRow>
<ArgTableRow arg="category" typ="string">Application functional classification</ArgTableRow>
<ArgTableRow arg="ui-url" typ="string">The generated URL for the application web interface, if available</ArgTableRow>
<ArgTableRow arg="default-credentials" typ="string">The default credentials required for the application</ArgTableRow>
<ArgTableRow arg="status" typ="string">The current status of the application (acquire veth, configuring container(s), downloading/extracting, starting)</ArgTableRow>
<ArgTableRow arg="default-network" typ="enum">The default network used by the application (lan or internal)</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum { none:nv::BADID }">The VETH interface used by the application</ArgTableRow>
<ArgTableRow arg="ip-address" typ="ipAddr">The IP address assigned to the VETH interface</ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { string
 }"></ArgTableRow>
<ArgTableRow arg="cpu-usage" typ="num">The current CPU usage percentage by the application</ArgTableRow>
<ArgTableRow arg="memory-current" typ="num">The amount of memory currently used by the application</ArgTableRow>
<ArgTableRow arg="app-size" typ="num">The total size of the application</ArgTableRow>
<ArgTableRow arg="data-size" typ="num">The size of the data stored by the application</ArgTableRow>
<ArgTableRow arg="configs" typ="object { composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="variables-to-use-in-environment" typ="object { composite { ,  } { ,  }
 }">A list of all variables present in the application environment</ArgTableRow>
</ArgTable>

## app/cleanup

**Package:** container
**Type:** Command

Removes all application data, configuration files, and the container image. This operation is destructive and irreversible.

## app/network

**Package:** container
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="e" typ="external"></ArgTableRow>
<ArgTableRow arg="I" typ="invalid"></ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="allow-outgoing-access" typ="bool"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="network" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="ip" typ="ipAddr"></ArgTableRow>
<ArgTableRow arg="status" typ="string"></ArgTableRow>
<ArgTableRow arg="used-ips" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }"></ArgTableRow>
<ArgTableRow arg="bridge-interface" typ="iface_enum { none:nv::BADID }"></ArgTableRow>
<ArgTableRow arg="cmds" typ="multi { string
 }"></ArgTableRow>
</ArgTable>

## app/remove

**Package:** container
**Type:** Command

Removes the specified application from the system.

## app/restart

**Package:** container
**Type:** Command

Restarts the specified running application.

## app/settings

**Package:** container
**Type:** Settings Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Global setting that specifies which disk will be used for storage operations</ArgTableRow>
<ArgTableRow arg="router-ip" typ="ipAddr">Manually specifies the IP address at which the current RouterOS device can be reached</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none:nv::BADID }">Manually specifies the bridge interface that represents the local area network</ArgTableRow>
<ArgTableRow arg="media-path" typ="file">Manually specifies the directory path where all media files will be stored</ArgTableRow>
<ArgTableRow arg="download-path" typ="file">Manually specifies the directory path where all downloaded content will be stored</ArgTableRow>
<ArgTableRow arg="show-in-webfig" typ="bool">Controls whether links to enabled applications are displayed on the WebFig login page</ArgTableRow>
<ArgTableRow arg="auto-update" typ="bool">Global setting that enables automatic updates for all installed applications packages</ArgTableRow>
<ArgTableRow arg="registry-mirrors" typ="multi { array-id, array-id, composite { ,  } { ,  }
 }">Specifies one or more registry mirror URLs for container image retrieval</ArgTableRow>
<ArgTableRow arg="app-store-urls" typ="multi { array-id, string
 }">URL to a custom app store. Must point to a YAML array where each application is an element</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="assumed-router-ip" typ="ipAddr">Automatically detected network IP address of the RouterOS device</ArgTableRow>
<ArgTableRow arg="assumed-lan-bridge" typ="iface_enum { none:nv::BADID }">Automatically detected bridge interface used for LAN connectivity</ArgTableRow>
<ArgTableRow arg="assumed-media-path" typ="file">Default media storage path, typically located on the system disk</ArgTableRow>
<ArgTableRow arg="assumed-download-path" typ="file">Default download directory path, typically located within the media storage area</ArgTableRow>
<ArgTableRow arg="certificate-status" typ="string"></ArgTableRow>
<ArgTableRow arg="certificate" typ="enum (none)"></ArgTableRow>
</ArgTable>

## app/setup

**Package:** container
**Type:** Command

Starts the setup wizard that automates networking, storage, and registry configuration for the App system.

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="disk" typ="enum (none)">Selected storage disk for application installation</ArgTableRow>
<ArgTableRow arg="lan-bridge" typ="iface_enum { none:nv::BADID }">Selected LAN bridge interface for container networking</ArgTableRow>
<ArgTableRow arg="router-ip-alt" typ="alt { enum
, ipAddr
 }">Manual IP address override for the RouterOS device</ArgTableRow>
</ArgTable>

## app/update

**Package:** container
**Type:** Command

Updates the specified application to the latest available container image.
