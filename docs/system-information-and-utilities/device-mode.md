# Device-mode

> The device-mode feature restricts router access and limits configuration options to enhance security, available in advanced, home, basic, or ros modes depending on device type and RouterOS version. Changes require physical confirmation via power cycle or button press, with limited update attempts to prevent unauthorized mode changes.

# Device-mode

## Description

The **device-mode** is a feature which sets specific limitations on a device, or limits access to specific configuration options. It helps to protect your router and network from attackers who might gain unauthorized access and use it as a gateway for attacks to other networks.

Available device-modes are *advanced,* *home, basic and ros*. Device-mode configuration is factory pre-installed on routers (for devices with MikroTik RouterOS v7.17 or later). *Advanced (previously called enterprise)* mode is configured for CCR and 1100 series devices, *home* mode is configured for home routers and basic mode is configured for any other type of device. For devices running versions prior to RouterOS version 7.17, all devices use the *advanced/enterprise* mode.

```ros
[admin@MikroTik] > /system/device-mode/print 
                 mode: advanced     
     allowed-versions: 7.13+,6.49.8+
              flagged: no           
     flagging-enabled: yes          
            scheduler: yes          
                socks: yes          
                fetch: yes          
                 pptp: yes          
                 l2tp: yes          
       bandwidth-test: yes          
          traffic-gen: no           
              sniffer: yes          
                ipsec: yes          
                romon: yes          
                proxy: yes          
              hotspot: yes          
                  smb: yes          
                email: yes          
             zerotier: yes          
            container: no           
  install-any-version: no           
           partitions: no           
          routerboard: yes          
        attempt-count: 0   
```

The device-mode can be changed by the authorized RouterOS user, but physical access to the device is required to change it. After changing the device-mode, you need to confirm it, by pressing a button on the device itself, or perform a "cold reboot" - that is, unplug the power. When the change is confirmed, regardless of confirmation mode, the **device will be rebooted**!

## Changing mode of device-mode

```ros
[admin@MikroTik] > /system/device-mode/update mode=home 
  update: please activate by turning power off or pressing reset or mode button 
          in 5m00s
-- [Q quit|D dump|C-z pause]
```

If no power off or button press is performed within the specified time, the mode change is canceled. If another update command is run in parallel, both will be canceled.

:::danger
There are several EOL products which do not "confirm" mode changes with a reset button press. These routers can confirm a mode change only with a power cycle.
:::

In order to protect the device against an attacker who might silently gain access to your router, abuse it with some scripts and simply try to wait until you reboot your router and not even know that at that time you are accepting changes requested by some intruder, you can "update" mode only three times. There is a counter which will count how many update attempts are made and will not allow any more updates. This counter can be reset only when the administrator does power-cycle the router or presses a button when seeing such a warning on mode settings update attempt (same as with accepting any updates).

## Changing device-mode settings using Netinstall or FlashFig

Starting from RouterOS 7.22, it is possible to configure **device‑mode** and **protected‑routerboot** and other settings.

For more information, see the [Netinstall](../getting-started/installation-and-upgrade/netinstall/index.md) and [FlashFig](../management-tools/flashfig.md) documentation.

## Enabling device-mode feature

```ros
[admin@MikroTik] > /system/device-mode/update container=yes 
  update: too many unsuccessful attempts, turn off power or reboot by pressing reset or mode button in 4m55s to reset attempt-count
```

The following commands are available in the /**system/device-mode** menu:

| Property | Description |
| :-- | :-- |
| get | Returns a value that you can assign to a variable or print on the screen. |
| print | Shows the active mode and its properties. |
| update | Applies changes to the specified properties, see below. |

## Available device-mode modes

There are four device modes available for configuration (mode=advanced is the default one), each mode has a subset of features that are not allowed when it is used. Note that there is no mode that has all features enabled. Certain features need to be enabled even if you have "advanced" mode enabled. ROSE device-mode is very similar to advanced mode, but it is made for RDS and similar devices with a wider option to use disks, therefore supporting container installations from the factory. See section "Feature clarification" for more details about what each option means. So, as per the below table it can be seen that "traffic-gen, container, partitions, routerboard" features are always disabled, unless specifically enabled by the admin user.

| **Feature / Property** | **Home** | **Basic** | **Advanced** | **ROSE** |
| :-- | :-- | :-- | :-- | :-- |
| **Bandwidth Test** (/tool/bandwidth-test) | No | No | Yes | Yes |
| **Containers** (/container) | No | No | No | Yes |
| **Email** (/tool/e-mail) | No | Yes | Yes | Yes |
| **Fetch** (/tool/fetch) | No | Yes | Yes | Yes |
| **Hotspot** (/ip/hotspot) | No | No | Yes | Yes |
| **Install Any Version** (`install-any-version`) | No | No | No | No |
| **IPsec** (/ip/ipsec) | Yes | Yes | Yes | Yes |
| **L2TP** (/interface/l2tp) | Yes | Yes | Yes | Yes |
| **Partitions** (/`partitions`) | No | No | No | No |
| **PPTP** (/interface/pptp) | Yes | Yes | Yes | Yes |
| **Proxy** (/ip/proxy) | No | No | Yes | Yes |
| **RoMon** (/tool/romon) | No | Yes | Yes | Yes |
| **Routerboard Settings** (/system/routerboard) | No | No | No | No |
| **Scheduler** (`scheduler`) | No | Yes | Yes | Yes |
| **SMB** (/ip/smb) | Yes | Yes | Yes | Yes |
| **Sniffer** (/tool/sniffer) | No | Yes | Yes | Yes |
| **SOCKS Proxy** (/ip/socks) | No | No | Yes | Yes |
| **Traffic Generator** (/tool/traffic-gen) | No | No | No | No |
| **ZeroTier** (`zerotier`) | No | No | Yes | Yes |

## List of available properties

| Property | Description |
| :-- | :-- |
| **scheduler, socks, fetch, pptp, l2tp, bandwidth-test, traffic-gen, sniffer, ipsec, romon, proxy, hotspot, smb, email, zerotier, container, install-any-version****, partitions, routerboard** (*yes \| no*) | The list of available features, which can be controlled with the **device-mode** option. See section "Feature clarification" for more details about what each option means. |
| **activation-timeout** (default: **5m**); | The reset button or power off activation timeout can be set in the range 00:00:10 .. 1d00:00:00. If the reset button is not pressed (or cold reboot is not performed) during this interval, the update will be canceled. |
| **flagging-enabled** (*yes \| no*; Default: **yes**) | The device will perform configuration analysis and if traces of suspicious code are found, flagged mode will be triggered, setting **flagged=yes**, enabling restrictions described in the **flagged=yes**. See the "[Flagged status](./device-mode.md#flagged-status)" paragraph. |
| **flagged** (*yes \| no*; Default: **no**) | RouterOS employs various mechanisms to detect tampering with its system files. If the system has detected unauthorized access to RouterOS, the status "flagged" is set to yes. If "flagged" is set to yes, for your safety, certain limitations are put in place. See the chapter below for more information. |
| **mode:** (basic, home, advanced, ros; default: **advanced**); | Allows choosing from available modes that will limit device functionality.  By default, **advanced** mode allows options except**traffic-gen, container, partitions,** **install-any-version****, routerboard.** So to use these features, you will need to turn it on by performing a device-mode update.   By default, **home** mode disables the following features: **scheduler, socks, fetch, bandwidth-test, traffic-gen, sniffer, romon, proxy, hotspot, email, zerotier, container,** **install-any-version****, partitions, routerboard.** |

More specific control over the available features is possible. Each of the features controlled by device-mode can be specifically turned on or off.

For instance **scheduler** won't allow performing any action in the `/system/scheduler`. The used device-mode disables all listed features, for instance, if **mode**=home is used, but **zerotier** is required for your setup, a device-mode update `/system/device-mode/update` zerotier=yes will be required with physical access to the device to push the button or cut the power.

#### Advanced example of changing device-mode

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes
[admin@MikroTik] > /system/device-mode/update mode=advanced zerotier=no
```

If the update command specifies any of the mode parameters, this update replaces the entire device-mode configuration. In this case, all "per-feature" settings will be lost, except those specified with this command. For instance:

```ros
[admin@MikroTik] > /system/device-mode/update mode=home email=yes fetch=yes
[admin@MikroTik] > /system/device-mode/print config
   mode: home
  fetch: yes
  email: yes
[admin@MikroTik] > /system/device-mode/update mode=advanced sniffer=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no

```

We see that fetch = yes and email = yes are missing, as they were overridden with the mode change. However, specifying only "per-feature" settings will change only those:

```ros
[admin@MikroTik] > /system/device-mode/update hotspot=no
-- reboot --
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
```

If the feature is disabled, an error message is displayed for interactive commands:

```ros
[admin@MikroTik] > /system/device-mode/print config
     mode: advanced
  sniffer: no
  hotspot: no
[admin@MikroTik] > /tool/sniffer/quick 
failure: not allowed by device-mode
```

However, it is possible to add the configuration to a disabled feature, but there will be a comment showing the disabled feature in the device-mode:

```ros
[admin@MikroTik] > /ip/hotspot/add interface=ether1 
[admin@MikroTik] > /ip/hotspot/print 
Flags: X, S - HTTPS
Columns: NAME, INTERFACE, PROFILE, IDLE-TIMEOUT
#   NAME      INTERFACE  PROFILE  IDLE-TIMEOUT
;;; inactivated, not allowed by device-mode
0 X hotspot1  ether1     default  5m          
```

## Feature clarification

| Feature | Clarification of which menus become unavailable to change |
| :-- | :-- |
| [bandwidth-test](../diagnostics-monitoring-and-troubleshooting/bandwidth-test.md) | *`/tool/bandwidth-test`* *`/tool/bandwidth-server`*  *`/tool/speed-test`* |
| [routerboard](../hardware/routerboard.md) | *`/system/routerboard/settings`* (except auto-upgrade option) |
| [container](../containers/index.md) | all container functionality |
| install-any-version | RouterOS will no longer allow you to install RouterOS version below versions listed under the "allowed-versions" attribute. |
| [email](./e-mail.md) | *`/tool/e-mail`* |
| [fetch](./fetch.md) | *`/tool/fetch`* |
| [hotspot](../authentication-authorization-accounting/hotspot-captive-portal/index.md) | *`/ip/hotspot`* |
| [ipsec](../virtual-private-networks/ipsec/index.mdx) | *`/ip/ipsec`* |
| [l2tp](../virtual-private-networks/l2tp/index.md) | *`/interface/l2tp-server`*  *`/interface/l2tp-client`* |
| [partitions](./partitions.md) | */partitions*  does not allow changing the count of partitions. If your router is unable to boot, it will still be able to boot into your other partitions. No restriction for crash recovery. |
| [pptp](../virtual-private-networks/pptp.md) | *`/interface/pptp-server`*  *`/interface/pptp-client`* |
| [proxy](../network-management/proxy/index.md) | *`/ip/proxy`* |
| [romon](../management-tools/romon.md) | *`/tool/romon`* |
| [scheduler](./scheduler.md) | *`/system/scheduler`* |
| [smb](../storage/smb.md) | *`/ip/smb`* |
| [sniffer](../diagnostics-monitoring-and-troubleshooting/packet-sniffer.md) | *`/tool/sniffer`* |
| [socks](../network-management/socks/index.md) | *`/ip/socks`* |
| [traffic-gen](../diagnostics-monitoring-and-troubleshooting/traffic-generator.md) | *`/tool/traffic-generator`*  *`/tool/flood-ping`*  *`/tool/ping-speed`* |
| [zerotier](../virtual-private-networks/zerotier.md) | */zerotier* |

## Allowed versions

Device mode lists in its parameters an argument called "allowed-versions". This is a list of versions which MikroTik considers as secure and which do not include any serious vulnerabilities which could be used by an attacker.
  
This setting does not depend on the installed RouterOS version and works as a separate protection layer, in order to disallow an attacker to downgrade version step-by-step to reach any known vulnerable RouterOS release. When you upgrade RouterOS to a release where a newer "allowed-versions" list is available, the oldest list will be overwritten. If you downgrade RouterOS, "allowed-versions" list will not change and will remain updated to the latest list. The list is ignored, if device-mode "install-any-version" is enabled.

## Flagged status

Along with the device-mode feature, RouterOS now can analyze the whole configuration at system startup, to determine if there are any signs of unauthorized access to your router. If suspicious configuration is detected, the suspicious configuration will be disabled and the **flagged** parameter will be set to "yes". The device now has a Flagged state and enforces certain limitations.

```ros
[admin@MikroTik] > /system/device-mode/print 
     mode: advanced
  flagged: yes
...
```

If the system has this flagged status, the current configuration works, but it is not possible to perform the following actions:
  
bandwidth-test, traffic-generator, sniffer, as well as configuration actions that enable or create new configuration entries (it will still be possible to disable or delete them) for the following programs: *system scheduler, SOCKS proxy, pptp, l2tp, ipsec, proxy, smb*.  
  
When performing the aforementioned actions while the router has the flagged state, you will receive an error message:

```ros
[admin@MikroTik] > /tool/sniffer/quick 
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
[admin@MikroTik] > /int l2tp-client/add connect-to=1.1.1.1 user=user
failure: configuration flagged, check all router configuration for unauthorized changes and update device-mode
```

To exit the flagged state, you must perform the command "/system/device-mode/update flagged=no". The system will ask you to either press a button, or issue a hard reboot (cut power physically or do a hard reboot of the virtual machine).
  
**Important!** Although the system has disabled any malicious looking rules, which triggered the flagged state, it is crucial to inspect all of your configuration for other unknown things, before exiting the flagged state. If your system has been flagged, assume that your system has been compromised and do a full audit of all settings before re-enabling the system for use. After completing the audit, change all the system passwords and upgrade to the latest RouterOS version.

:::warning
Starting from RouterOS version 7.17, device-mode restricts SwOS/RouterOS transition for dual-boot; in order to enable: `/system/device-mode/update` routerboard=yes
:::
