# Moving your RAID array to a different device

> This page explains how to move a RAID 5 array from an old device to a new one by creating the RAID on the new device, assigning member slots, ejecting disks from the old device, and finally transferring them to the new device where RouterOS automatically mounts the RAID.

# Moving your RAID array to a different device

It is possible to move your RAID array from one device to another.

In this example we are using a RAID 5 array on an RDS2216 consisting of 4 members.

First, on the "new" device, create a RAID and assign the member slots.

```ros
# New device
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

Then, add the currently empty slots to the newly created RAID

```ros
# New device
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4
```

After the RAID has been created and the slots have been assigned to the RAID - on the "old" device, eject the disks you want to switch to the "new" device

```ros
# Old device
/disk/eject nvme1
/disk/eject nvme2
/disk/eject nvme3
/disk/eject nvme4
```

Finally, you can remove the disks from the "old" device and insert them in the assigned slots in the "new" one. RouterOS will automatically detect a RAID superblock and mount the array without any additional input.
