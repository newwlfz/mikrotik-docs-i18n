# RouterBOARD

> This page documents the `/system/routerboard` menu in MikroTik RouterOS, providing hardware and firmware information such as model, serial number, and current/upgrade firmware versions. It includes upgrade instructions for RouterBOOT firmware and settings to configure boot behavior at the hardware level.

# RouterBOARD

On RouterBOARD devices, you can view basic hardware and firmware information from the `/system/routerboard` menu.

To display this information, run the following command:

```ros
[admin@demo.mt.lv] /system/routerboard/print 
       routerboard: yes                                                      
             model: CCR2116-12G-4S+                                                                                                
     serial-number: MT123456789                                              
     firmware-type: al64v3                                                   
  minimum-firmware: 7.8                                                      
  current-firmware: 7.22.2
  upgrade-firmware: 7.22.2                          
```

The output includes the following details:

## Properties

**Read-only properties:**

| Property | Description |
| :-- | :-- |
| **routerboard** (*yes \| no*) | Indicates whether the device is a RouterBOARD unit. |
| **model** (*string*) | The RouterBOARD model number. |
| **serial-number** (*string*) | The unique serial number of the device. |
| **firmware-type** (*string*) | The type of bootloader firmware used by the device. |
| **minimum-firmware** (*string*) | The firmware version installed at the factory. (was 'factory-firmware') |
| **current-firmware** (*string*) | The version of the RouterBOOT loader currently in use. This should not be confused with the RouterOS operating system version. |
| **upgrade-firmware** (*string*) | RouterOS upgrades may include a new RouterBOOT version file, but it must be applied manually. This line indicates whether a new RouterBOOT file has been found on the device. The file may be included with a recent RouterOS upgrade or uploaded manually as an FWF file. In both cases, the newest available version is shown here. |

## Upgrading RouterBOOT

RouterBOOT upgrades typically include minor improvements to overall RouterBOARD operation. It is recommended to keep the firmware up to date.

To check whether an upgrade is available, compare the **current-firmware** and **upgrade-firmware** values under `/system/routerboard`. If **upgrade-firmware** shows a higher version than **current-firmware**, a newer version is ready to be applied.

### Upgrade Steps

1. Run the upgrade command:

   ```ros
   [admin@mikrotik] /system/routerboard> upgrade
   Do you really want to upgrade firmware? [y/n]
   y
   echo: system,info,critical Firmware upgraded successfully, please reboot for changes to take effect!
   ```

2. When prompted, enter **y** to confirm.

3. Reboot the device to apply the changes:

   ```ros
   /system/reboot
   ```

After the reboot, verify that **current-firmware** matches **upgrade-firmware**, confirming the upgrade was applied successfully.

## Settings

**Path:** `/system/routerboard/settings`

This sub-menu configures RouterBOOT firmware settings that control how the device starts up and operates at the hardware level.

```ros
[admin@MikroTik] /system/routerboard/settings> print 
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
         preboot-etherboot: disabled
             cpu-frequency: 1200MHz
          memory-frequency: 1066DDR
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: disabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

:::warning
Starting from RouterOS version 7.17, the device-mode setting restricts SwOS/RouterOS transitions for dual-boot devices. To enable this feature, run:
`/system/device-mode/update routerboard=yes`
:::

### Property Reference

| Property | Description |
| :--- | :--- |
| **auto-upgrade** (*yes \| no*; Default: **no**) | Whether to upgrade firmware automatically after a RouterOS upgrade. The latest firmware will be applied after an additional reboot. |
| **baud-rate** (*integer*; Default: **115200**) | Choose the onboard RS232 speed in bits per second if installed. Off option allows serial interface to be disabled. |
| **boot-delay** (*time*; Default: **2s**) | How much time to wait for a keystroke while booting. |
| **boot-device** (*nand-if-fail-then-ethernet ...*; Default: **nand-if-fail-then-ethernet**) | Choose the way RouterBOOT loads the operating system:- **ethernet** — boot the device in Etherboot mode;- **flash-boot** — Flashfig mode on startup is enabled. This setting will revert to NAND after a successful configuration change OR once any user logs into the board;- **flash-boot-once-then-nand** — Flashfig mode on startup is enabled for a single boot only, resets to nand-if-fail-then-ethernet after that;- **nand-if-fail-then-ethernet** — boot RouterOS from the NAND, if RouterOS is not booting - it goes to Etherboot automatically. This is the default mode for devices straight out of the box;- **nand-only** — boot RouterOS from the NAND;- **try-ethernet-once-then-nand** — boot device in Etherboot mode once and if no server is available - it will boot directly from the NAND or of the storage type the device is using.**Important:** NoteEtherboot mode is a special state for a MikroTik device that allows you to reinstall your device using Netinstall.There are several ways to put your device into Etherboot mode depending on the device you are using:1. Press the Reset button and power on your device (wait until "USR" led is blinking then stable "On" and when the "USR" led is "Off" - release the Reset button) - the device is booting in bootp mode to reinstall RouterOS using Netinstall.2. Using the serial console, when the device is booting up, keep pressing CTRL+E on your keyboard until the device shows that it is trying bootp protocol.3. Using the serial console, press any key while the device is booting and choose "o" then "1" and "x". |
| **boot-os** (*router-os \| swos*; Default: **router-os**) | Changes the booting operating system for CRS3xx series switches. |
| **boot-protocol** (*bootp \| dhcp ...*; Default: **bootp**) | Boot protocol to use:- **bootp** — the default option for booting RouterOS;- **dhcp** — used for OpenWRT and possibly other OS. |
| **cpu-frequency** (*depends on model*; Default: **depends on model**) | This option allows for changing the CPU frequency of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button in RouterOS version 7 on the keyboard at this prompt. |
| **cpu-mode** (*power-save \| regular*; Default: **power-save**) | Whether to enter CPU suspend mode in HLT instruction. Most OSs use HLT instruction during the CPU idle cycle. When the CPU is in suspend mode, it consumes less power, but in low-temperature conditions, it is recommended to choose a regular mode, so that the overall system temperature would be higher. |
| **enable-jumper-reset** (*yes \| no*; Default: **yes**) | Disable this to avoid accidental setting reset via the onboard jumper. |
| **enter-setup-on** (*any-key \| delete-key*; Default: **any-key**) | Which key will cause the BIOS to enter configuration mode during boot delay. Useful when the serial console prints out symbols during the boot process and goes into RouterBOOT menu by itself. Note that in some serial terminal programs, it is impossible to use the Delete key to enter the setup - in this case, it might be possible to do this with the Backspace key. |
| **force-backup-booter** (*yes \| no*; Default: **no**) | If to use the backup RouterBOOT. This is only useful if the main loader has become corrupted somehow and cannot be fixed. So that you don't have to boot the device with a pushed reset button (which loads the backup loader), you can use this setting to load it every time:- **yes** — backup loader will be used always;- **no** — main booter will be used. |
| **init-delay** (*timeout interval 0s..9s*; Default: ) | Used for mPCIe modems with RB9xx series devices only. In case your modem is not being recognized after a soft reboot, then you might need to add a delay before the USB port is initialized. |
| **memory-frequency** (*depends on model*; Default: **depends on model**) | This option allows changing the memory frequency of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button in RouterOS version 7 button on the keyboard at this prompt. |
| **memory-data-rate** (*depends on the model*; Default: **depends on model**) | This option allows changing the memory data rate of the device. Values depend on the model, to see available options, hit the [?] button in RouterOS version 6 or the [F1] button in RouterOS version 7 button on the keyboard at this prompt. |
| **preboot-etherboot** (*timeout interval 1s..30s*; Default: **disabled**) | Enables preboot etherboot, which runs before the regular boot device. It works the same as boot-device=etherboot, but has an additional timeout value. If an IP address is not received from the Netinstall server before the timeout expires, the regular booting process will start.**Important:** NoteThe preboot-etherboot configuration is stored in the BIOS, downgrading RouterOS to older versions will not disable it. This feature can be disabled from the RouterOS menu or by resetting the BIOS.Since etherboot accepts IP addresses from any BOOTP/DHCP server, use preboot-etherboot-server to start etherboot only when address is received from specified Netinstall server. |
| **preboot-etherboot-server** (*IP address, any*; Default: **any**) | Sets preboot-etherboot to accept IP address only from the specified Netinstall server IP address. By enabling this feature, unintentional etherboot from other BOOTP/DHCP servers can be prevented. |
| **regulatory-domain-ce** (*yes \| no*; Default: **no**) | Enables extra-low TX power for high antenna gain devices (requires a reboot). |
| **silent-boot** (*yes \| no*; Default: **no**) | This option disables beeping sounds during booting:- **yes** — no booting beeps (does not disable the RouterOS: beep command);- **no** — regular booting sound. |
| **disable-pci** (*yes \| no*; Default: **no**) | Specific setting for devices with the MT7621 chip. Allows disabling PCI. |
| **preferred-architecture** (*arm32 \| arm64*; Default: **arm32**) | Specific setting for L009 devices. Allows to update the device to use ARM64 architecture. |
| **etherboot-port** (*interface*; Default: ) | Allows selecting Etherboot/Netinstall interface, only applies to CRS520, CRS804, CRS812. Default port depends on the model. |
| **gpio-function** (*port*; Default: **serial1**) | Specific setting for M33 devices. By default pins 12,13,15,16 are configured for the second "serial1" port usage, they can be resigned for GPIO usage in `/iot/gpio/digital` menu. |

:::danger
Overclocking the CPU or memory is not covered by warranty. If performance issues is suspected to be caused by overclocking, return both frequencies to their nominal values before contacting support.
:::

## Preboot Etherboot

**preboot-etherboot** is a feature that instructs a RouterOS device to search for a Netinstall server on every boot for a specified amount of time, before starting the regular boot process (e.g., RouterOS). This feature is particularly useful for remote reinstallation, as it allows the device to attempt Etherboot on every startup.

**preboot-etherboot-server** specifies that the preboot-etherboot process should accept an IP address only from a Netinstall server with a specific IP address. By default, Etherboot accepts addresses from any BOOTP/DHCP server. This setting allows you to restrict it to a particular Netinstall server, so the device can be reinstalled without being removed from the network.

## Remote Reinstallation

When both features are enabled, the device can be reinstalled remotely without accessing RouterOS or using the reset button.

For example, to start a remote reinstallation:

1. Power cycle the RouterOS device (e.g., using a PoE switch or power controller).
2. The device attempts Etherboot and connects to the Netinstall server.
3. After installation, disable the Netinstall server.
4. Power cycle the device again to complete the process.

## Requirements

To enable **preboot-etherboot** and **preboot-etherboot-server**:

1. Install RouterOS version 7.9 or newer.
2. Upgrade RouterBOOT:

To enable the feature, run:

```ros
/system/routerboard/settings/set preboot-etherboot=9s preboot-etherboot-server=10.10.10.100
```

On every reboot or power cycle, the device will attempt to receive an IP address from the Netinstall server with IP **10.10.10.100** for **9 seconds**. If no such server is available, the device will continue with the normal boot process.

:::warning
If **preboot-etherboot-server** is not specified, the device will accept an IP address from any Netinstall server and enter Etherboot mode, waiting for a reinstall process. DHCP servers will only be used if the RouterBOOT **boot-protocol** is set to **dhcp** (default is **bootp**).
:::

RouterOS reinstallation does not affect BIOS settings. If preboot-etherboot is enabled, the device will continue attempting to enter Etherboot on every boot.

To avoid unintended Etherboot activation without accessing RouterOS, disable any attached Netinstall or DHCP server.

## Protected RouterBOOT

The Protected RouterBOOT feature allows protection of a RouterOS device from physical access by disabling Etherboot and restricting access to the bootloader.

This feature can only be enabled or disabled from within RouterOS after login. There is no RouterBOOT setting to control it directly. These additional options appear only under certain conditions.

:::warning
If you forget the RouterOS admin password while Protected RouterBOOT is enabled, the device cannot be recovered without performing a complete reformat.
:::

## Behavior When Enabled

When this feature is active:

- The reset button and reset pin-hole are disabled.
- The RouterBOOT menu is inaccessible via serial console.
- Etherboot (Netinstall) is disabled.
- The device can only be accessed via RouterOS using a valid admin password.
- This setting can only be enabled or disabled from within RouterOS (no RouterBOOT-level option exists).

:::warning
If you enable Protected RouterBOOT and forget your RouterOS password, **the device cannot be recovered** through normal means.
:::

## Enabling or Disabling

Starting from RouterOS v7, enabling or modifying this feature requires confirmation by pressing the reset or mode button.

You have **60 seconds** to confirm the change.

### Enable (Example)

```ros
[admin@450] > /system/routerboard/settings/set protected-routerboot=enabled
[admin@450] > /system/routerboard/settings/print
                        ;;; press button within 60 seconds to confirm
                            protected routerboot enable
              auto-upgrade: no
                 baud-rate: 115200
                boot-delay: 2s
            enter-setup-on: any-key
               boot-device: nand-if-fail-then-ethernet
             cpu-frequency: auto
             boot-protocol: bootp
       enable-jumper-reset: yes
       force-backup-booter: no
               silent-boot: yes
      protected-routerboot: enabled
      reformat-hold-button: 20s
  reformat-hold-button-max: 10m
```

### Disable (Example)

```ros
/system/routerboard/settings/set protected-routerboot=disabled
```

:::warning
If the button is not pressed within the timeout, the change is not applied.
:::

## Emergency Reformat (Recovery Method)

As an emergency recovery option, it is possible to reset the device by holding the reset button during power-on for longer than the reformat-hold-button time, but less than reformat-hold-button-max.

:::danger
EXTREMELY DANGEROUS. Use this only if you have lost all access to the device.
:::

When triggered, the following actions are performed:

- RouterOS, all files, and configuration are completely and irreversibly erased (NAND re-format).
- All RouterBOOT settings are reset to defaults.
- The device reboots.
- Since boot from NAND fails, the device enters Etherboot mode automatically
Netinstall is required to reinstall RouterOS.

:::note
Reformat on some RouterBOARD devices can take more than 5 minutes.
:::

### Property Reference

| Property | Description |
| :--- | :--- |
| **protected-routerboot** (*enabled \| disabled*; Default: **disabled**) | Disables access to RouterBOOT configuration over serial console and prevents the reset button from changing boot mode (Netinstall is disabled). Access to RouterOS is only possible with a known RouterOS user account with administrative privileges. This setting can only be disabled from within RouterOS. If the RouterOS password is lost, recovery requires a full device reformat using the reset button timing procedure.- **enabled** — Secure mode. RouterOS is accessible only with a valid admin-level user. Serial input is ignored. Etherboot is disabled, and RouterBOOT settings cannot be changed.- **disabled** — Normal operation. RouterBOOT settings are accessible via serial console, and the reset button can be used to enter Netinstall mode. |
| **reformat-hold-button** (*5s..300s*; Default: **20s**) | Defines the minimum time the reset button must be held at power-on to trigger a full device reformat. The hold time must be longer than this value but shorter than `reformat-hold-button-max`. When triggered, the device performs a complete reset operation:- RouterOS, all files, and configuration are permanently erased (NAND reformat).- All RouterBOOT settings are reset to defaults.- The device reboots.- Since NAND boot fails, the device enters Etherboot automatically.- Netinstall is required to reinstall RouterOS.⚠️ **Warning:** This is an extremely dangerous operation and should only be used when all other access methods are unavailable. On some RouterBOARD devices, the reformat process may take more than 5 minutes. The device becomes ready for Netinstall after completion. |
| **reformat-hold-button-max** (*15s..600s*; Default: **10m**) | Defines the maximum allowed time the reset button may be held during a reformat trigger. Works together with `reformat-hold-button` to create a precise time window. For example, setting `reformat-hold-button=60s` and `reformat-hold-button-max=65s` requires the button to be held strictly between 60 and 65 seconds. This increases security by making accidental or guessed resets practically impossible. Introduced in RouterBOOT 3.38.3. |

### LED Indicator

When Protected RouterBOOT is enabled, the LED blinks every second to assist with timing:

- LED off for one second
- LED on for one second

### Support on Older MikroTik Hardware

> **Important:** This section applies only to older devices that display the specific error message described below. Do not modify the bootloader unless instructed to do so by that message.

The Protected RouterBOOT feature is supported on all modern MikroTik devices. However, if you are using an older device whose minimum firmware version is lower than **7.19.3**, you may see the following message when attempting to enable the feature:

> *"The 'protected routerboot' feature requires a backup-routerboot upgrade"*

If you see this message, follow the steps below.

### RouterOS v7 — Upgrade Steps

1. [Upgrade or downgrade](../getting-started/installation-and-upgrade/upgrade.md#manual-upgrade) your device to RouterOS **7.19.3** specifically. You can find this release on the [MikroTik download page](https://mikrotik.com/download).

2. Upgrade the RouterBOOT firmware by running `/system/routerboard/upgrade`, then reboot the device. After rebooting, verify that the **current-firmware** value shown in `/system/routerboard/print` matches the installed RouterOS version shown in `/system/resource/print` — both should be **7.19.3**.

3. Upload the [v7 universal package (all architectures)](https://box.mikrotik.com/f/991c3e94984c4e18b8d6/?dl=1) to the device and reboot again. This updates the **minimum-firmware** version to **7.19.3**, which is required to enable the Protected RouterBOOT feature.

4. Once the above steps are complete, you may upgrade the device to a newer RouterOS release.

### RouterOS v6 — Upgrade Steps

If your device is running RouterOS **v6** and you encounter the same message, follow the same steps as above, with these differences:

- Target version: **6.49.7** (instead of 7.19.3)
- Use the [v6 universal package (all architectures)](https://box.mikrotik.com/f/b062a26b4bd34c55aa52/?dl=1) (instead of the v7 package)

## Mode and Reset Buttons

All MikroTik devices running RouterOS support additional functionality for the **Reset** button. Select RouterBOARD devices also include a **Mode** button, which can be configured to run a custom script when pressed.

---

### Supported Devices (Mode Button)

The following devices support the Mode button:

- RBcAP-2nD (cAP)
- RBcAPGi-5acD2nD (cAP ac)
- RBwsAP5Hac2nD (wsAP ac lite)
- RB750Gr3 (hEX)
- RB760iGS (hEX S)
- RB912R-2nD (LtAP mini, LtAP mini LTE/4G kit)
- RBD52G-5HacD2HnD (hAP ac²)
- RBLHGR (LHG LTE/4G kit)
- RBSXTR (SXT LTE/4G kit)
- CRS328-4C-20S-4S+RM
- CRS328-24P-4S+RM
- CCR1016-12G r2
- CCR1016-12S-1S+ r2
- CCR1036-12G-4S r2
- CCR1036-8G-2S+ r2
- RBD53G-5HacD2HnD (Chateau)
- RBD53GR-5HacD2HnD (hAP ac³)
- E50UG (hEX)
- L41G-2axD (hAP ax lite)
- L009UiGS-RM, L009UiGS-2HaxD-IN
- cAPGi-5HaxD2HaxD (cAP ax)
- C53UiG+5HPaxD2HPaxD (hAP ax³)
- S53UG+5HaxD2HaxD (Chateau ax)
- H53UiG-5HaxQ2HaxQ (Chateau PRO ax)
- CCR2116-12G-4S+
- RDS2216-2XG-4S+4XS-2XQ

---

### Configuration Properties

| Property | Description |
| :--- | :--- |
| **enabled** (*no \| yes*; Default: **no**) | Enables or disables the button functionality. |
| **hold-time** (*time interval Min..Max*; Default: —) | Triggers the button action only when the button is held for a duration within the specified range. Both `Min` and `Max` accept values from `0s` to `1m`. *(Available from RouterOS 6.47beta60 and later.)* |
| **on-event** (*string*; Default: —) | The name of the script to run when the button is pressed. The script must be created and named in the [Script](../developer-guides/scripting) menu. |

:::info
The on-event script for the Mode, Reset, and WPS buttons is executed using `read,write,reboot,ftp,romon,test` permissions.
:::

---

### Basic Mode Button Example

The following example creates a script and assigns it to the Mode button. When the button is pressed, a message is written to the system log.

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button enabled=yes
```

---

### Using the Hold-Time Option (RouterOS 6.47 and Later)

:::info
The `hold-time` option and extended Reset button functionality were introduced in RouterOS 6.47.
:::

You can configure the button to trigger only when held for a specific duration. The example below activates the script when the Mode button is held for between 3 and 5 seconds:

```ros
/system/script/add name=test-mode-button source={:log info message=("mode button pressed");}
/system/routerboard/mode-button/set on-event=test-mode-button hold-time=3..5 enabled=yes
```

---

### Reset Button Configuration

The Reset button is configured in the same way as the Mode button, but uses a different menu path: `/system/routerboard/reset-button`.

```ros
/system/script/add name=test-reset-button source={:log info message=("reset button pressed");}
/system/routerboard/reset-button/set on-event=test-reset-button hold-time=0..10 enabled=yes
```

---

### Example: Toggle LED Dark Mode with the Mode Button

The following script toggles [LED dark mode](./leds.md#led-settings) on and off each time the Mode button is pressed:

```ros
/system/script/add name=dark-mode source={
   :if ([system leds settings get all-leds-off] = "never") do={
      /system/leds/settings/set all-leds-off=immediate
   } else={
      /system/leds/settings/set all-leds-off=never
   }
}
/system/routerboard/mode-button/set enabled=yes on-event=dark-mode
```

---

### WPS Button (D53, C53, S53, and H53 Series)

RouterBoards in the D53, C53, S53, and H53 series include a configurable **WPS button**. It works the same way as the Mode and Reset buttons — it executes a script when pressed.

**Basic WPS button example:**

```ros
/system/script/add name=test-wps-button source={:log info message=("wps button pressed");}
/system/routerboard/wps-button/set on-event=test-wps-button hold-time=0..10 enabled=yes
```

**Trigger WPS pairing via the WPS button or Mode button:**

The script below initiates WPS push-button pairing on all active Wi-Fi access point interfaces. You can assign it to either the WPS button or the Mode button (or both).

```ros
/system/script/add name=wps-accept source={
    :foreach iface in=[/interface/wifi/find where (configuration.mode="ap" && disabled=no)] do={
        /interface/wifi/wps-push-button $iface;
    }
}

/system/routerboard/wps-button/set enabled=yes on-event=wps-accept
/system/routerboard/mode-button/set enabled=yes on-event=wps-accept
```
