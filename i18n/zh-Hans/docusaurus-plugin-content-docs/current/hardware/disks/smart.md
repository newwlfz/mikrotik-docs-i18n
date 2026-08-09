# S.M.A.R.T. 信息

> RouterOS 现已支持对连接的存储设备进行 S.M.A.R.T. 监控，用户可通过 `/disk smart-info` CLI 命令检索硬盘健康状态、错误率等诊断属性。

# S.M.A.R.T. 信息

:::info
此功能需要 [Storage](../../storage/index.md) 软件包。
:::

自 RouterOS 7.23 起，已加入 S.M.A.R.T.（自我监控、分析与报告技术）支持。

S.M.A.R.T. 是内置于现代存储驱动器中的监控系统，可让您监控驱动器的健康状态、性能及错误率。
对于任何支持 S.M.A.R.T. 的已连接存储设备，您可以直接通过 CLI 使用 `/disk smart-info` 命令检索诊断属性。

:::info

部分 USB 硬盘盒可能不支持检索 S.M.A.R.T. 信息。

:::

## 示例输出

```ros
[admin@R2DUTRDS22162XG4S4XS2XQ20DISKS] > disk/smart-info nvme1
Columns: OUTPUT
OUTPUT                                                                     
smartctl 7.1 2019-12-30 r5022 [aarch64-linux-5.6.3] (local build)          
Copyright (C) 2002-19, Bruce Allen, Christian Franke, www.smartmontools.org
=== START OF INFORMATION SECTION ===                                       
Model Number:                       U.2 SSD 4TG2-P                         
Serial Number:                      <S/N>                      
Firmware Version:                   E21T4C                                 
PCI Vendor/Subsystem ID:            0x1bc0                                 
IEEE OUI Identifier:                0x24693e                               
Controller ID:                      0                                      
Number of Namespaces:               1                                      
Namespace 1 Size/Capacity:          960,197,124,096 [960 GB]               
Namespace 1 Formatted LBA Size:     512                                    
Namespace 1 IEEE EUI-64:            <EUI-64>                  
Firmware Updates (0x02):            1 Slot                                 
Optional Admin Commands (0x0017):   Security Format Frmw_DL Self_Test      
Optional NVM Commands (0x0054):     DS_Mngmt Sav/Sel_Feat Timestmp         
Maximum Data Transfer Size:         512 Pages                              
Warning  Comp. Temp. Threshold:     100 Celsius                            
Critical Comp. Temp. Threshold:     110 Celsius                            
Supported Power States                                                     
St Op     Max   Active     Idle   RL RT WL WT  Ent_Lat  Ex_Lat             
 0 +    20.00W       -        -    0  0  0  0        5       5             
Supported LBA Sizes (NSID 0x1)                                             
Id Fmt  Data  Metadt  Rel_Perf                                             
 0 +     512       0         0                                             
=== START OF SMART DATA SECTION ===                                        
SMART overall-health self-assessment test result: PASSED                   
SMART/Health Information (NVMe Log 0x02)                                   
Critical Warning:                   0x00                                   
Temperature:                        33 Celsius                             
Available Spare:                    100%                                   
Available Spare Threshold:          10%                                    
Percentage Used:                    0%                                     
Data Units Read:                    5,774,165 [2.95 TB]                    
Data Units Written:                 10,770,860 [5.51 TB]                   
Host Read Commands:                 75,868,764                             
Host Write Commands:                61,379,337                             
Controller Busy Time:               22                                     
Power Cycles:                       579                                    
Power On Hours:                     4,203                                  
Unsafe Shutdowns:                   105                                    
Media and Data Integrity Errors:    0                                      
Error Information Log Entries:      0                                      
Warning  Comp. Temperature Time:    0                                      
Critical Comp. Temperature Time:    0                                      
Temperature Sensor 1:               45 Celsius                             
Temperature Sensor 2:               33 Celsius                             
Temperature Sensor 3:               33 Celsius                             
Temperature Sensor 4:               34 Celsius                             
Temperature Sensor 5:               34 Celsius                             
Temperature Sensor 6:               35 Celsius                             
Temperature Sensor 7:               32 Celsius                             
Temperature Sensor 8:               31 Celsius                             
Error Information (NVMe Log 0x01, max 64 entries)                          
No Errors Logged      
```