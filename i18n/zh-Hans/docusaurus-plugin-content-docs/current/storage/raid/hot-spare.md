# 设置热备盘

> 本页说明如何在 RouterOS 中为 RAID 阵列配置热备盘，通过为 RAID 设置分配备用磁盘，在磁盘故障时自动启动重建。

# 设置热备盘

可以为 RAID 阵列分配一个热备盘。当磁盘发生故障时，重建会立即在指定的备用磁盘上启动。

使用所需磁盘数量添加 RAID 阵列：

```ros
/disk/add raid-device-count=4 raid-type=5 type=raid slot=raid5
```

随后，将磁盘以及备用盘添加到 RAID 中。在此例中，我们将 NVMe5 添加为备用盘。

```ros
/disk/set raid-master=raid5 raid-role=0 nvme1
/disk/set raid-master=raid5 raid-role=1 nvme2
/disk/set raid-master=raid5 raid-role=2 nvme3
/disk/set raid-master=raid5 raid-role=3 nvme4

/disk/set raid-master=raid5 raid-role=spare nvme5
```