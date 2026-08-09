# CHR: VirtualBox Installation

> This page provides a step-by-step guide for installing MikroTik RouterOS Cloud Hosted Router (CHR) in VirtualBox, covering VM creation, configuration, and initial setup with login instructions.

# CHR: VirtualBox Installation

## CHR VirtualBox Installation Video

**[![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_video.png)](https://www.youtube.com/watch?v=oHXkaHkSVVo)**

1. **Download VirtualBox**  
   Install the latest version of VirtualBox from the official website.

2. **Download CHR disk image**  
   Download and extract the latest Long-Term, Stable, or Testing version of the Cloud Hosted Router (CHR) VDI image from the [MikroTik download page](https://mikrotik.com/download).

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_01.png)

## Step 1: Create a New Virtual Machine

- Launch VirtualBox.
- Click **New** to create a new virtual machine.

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_02.png)

### Name and Operating System

- **Name**: Enter a VM name (e.g., MikroTik_CHR)
- **Type**: Linux
- **Version**: Other Linux (64-bit)

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_03.png)

## Step 2: Configure Memory Size

- Allocate at least **512 MB RAM** (RouterOS 7 minimum requirement)
- Assign the desired number of CPUs

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_04.png)

## Step 3: Add a Virtual Hard Disk

- Select **Use an Existing Virtual Hard Disk File**
- Choose the downloaded `.vdi` image

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_05.png)

Click **Finish** to create the VM.

## Step 4: Configure Virtual Machine Settings

Select the VM â†’ click **Settings**

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_06.png)

### System

- Disable **Floppy** and **Optical** from boot order

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_06_1.png)

### Processor

- Set the desired number of CPUs

### Network

- Adapter 1:
  - Enable network adapter
  - Attach to **Bridged Adapter** or **NAT** (depending on your setup)

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_07.png)

## Step 5: Start the Virtual Machine

- Click **Start** to boot the VM

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_08.png)

- Login credentials:
  - Username: `admin`
  - Password: *(empty, set immediately after first login)*

![](/docs/getting-started/installation-and-upgrade/install/chr-installation/img/chr_install_virtualbox_09.png)

## Congratulations

You have successfully installed MikroTik CHR on VirtualBox.

You can now proceed with initial RouterOS configuration using the console, WinBox, or WebFig.

## Supported Network and Disk Interfaces

### Network Adapters

- E1000
- RTL8139
- Virtio (paravirtual)

### Disk Controllers

- IDE

> **Warning:** Avoid using the E1000 network adapter unless no better synthetic or paravirtualized option is available. Virtio provides better performance on VirtualBox.
