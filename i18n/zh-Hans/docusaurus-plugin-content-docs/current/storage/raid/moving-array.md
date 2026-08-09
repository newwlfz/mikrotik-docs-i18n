# 将 RAID 阵列迁移至另一设备

> 本页说明如何将 RAID 5 阵列从旧设备迁移至新设备，方法是在新设备上创建 RAID、分配成员槽位、从旧设备弹出磁盘，最后将其转移至新设备，RouterOS 将自动挂载该 RAID。

# 将 RAID 阵列迁移至另一设备

可以将 RAID 阵列从一台设备迁移至另一台设备。

在本示例中，我们在 RDS2216 上使用由 4 个成员组成的 RAID 5 阵列。

首先，在“新”设备上创建 RAID 并分配成员槽位。

```ros
# 新设备
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

然后，将当前空槽位添加到新创建的 RAID 中

```ros
# 新设备
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4
```

在 RAID 创建完成且槽位已分配给 RAID 后，在“旧”设备上弹出要切换到“新”设备的磁盘

```ros
# 旧设备
/disk/eject nvme1
/disk/eject nvme2
/disk/eject nvme3
/disk/eject nvme4
```

最后，您可以从“旧”设备中取出磁盘，并将其插入“新”设备的指定槽位中。RouterOS 将自动检测 RAID 超级块并挂载该阵列，无需任何额外操作。