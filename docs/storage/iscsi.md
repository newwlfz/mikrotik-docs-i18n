# iSCSI

> iSCSI enables IP-based storage access with RouterOS supporting both target and initiator modes, featuring properties like iSCSI address, IQN identifiers, and configurable ports for both client and server roles.

# iSCSI

:::info
This feature requires the [Storage](./index.md) package.
:::

iSCSI allows accessing storage over an IP-based network. On the initiator the iSCSI device will appear as a block device. RouterOS supports both target and initiator modes.

## Properties

| Property | Description |
| :-- | :-- |
| **iscsi-address** | IP address of the iSCSI target. (Host device IP) |
| **iscsi-export** | Disables/enables iSCSI on the host device |
| **iscsi-iqn** | Unique identifier used to name the iSCSI target. |
| **iscsi-port** | Network port used by the iSCSI target to listen for incoming connections from initiators. The default port for iSCSI traffic is 3260. |
| **iscsi-server-iqn** | Unique identifier used by the iSCSI server. By default the format for the IQN is iqn.2000-02.com.mikrotik:*slot (starting 7.21beta2)* |
| **iscsi-server-port** | Network port used by the iSCSI server. *(starting 7.21beta2)* |

## Configuration example

Host

```ros
/disk
set pcie1-nvme1 iscsi-export=yes
```

Client

```ros
/disk
add type=iscsi iscsi-address=192.168.1.1 iscsi-iqn=iqn.2000-02.com.mikrotik:pcie1-nvme1
```
