# 文件

> MikroTik RouterOS 中的“文件”菜单允许管理用户空间文件，包括创建/编辑/删除文件和目录、查看 .npk 包的详细信息，以及将关键文件存储在“flash”目录中以在重启后保留。它支持最大 60KB 的文件大小，并提供关于 RAM 磁盘行为、写回缓存和压缩文件存储的警告。

# 文件

“文件”菜单显示路由器上的所有用户空间文件。可以创建新文件或目录、编辑文件内容、删除文件或目录。如果上传了 RouterOS “.npk” 包，文件菜单还会显示包特定信息，例如架构、构建日期和时间等。

:::warning
可以检索和编辑最大 60KB 的文件内容。如需访问更大文件的内容，请参阅 [获取文件内容](files.md#get-or-read-file-contents) 部分。
:::

```ros
[admin@MikroTik] > /file/print detail 
 0 name=wireless-7.16.1-arm.npk type=package size=1924.1KiB last-modified=2024-11-25 13:14:28 package-name="wireless" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 

 1 name=routeros-7.16.1-arm.npk type=package size=11.1MiB last-modified=2024-11-25 13:14:34 package-name="system" package-version="7.16.1" package-build-time=2024-10-10 14:03:32 
   package-architecture="arm" 

 2 name=flash type=disk last-modified=2024-11-25 13:12:10 

 3 name=flash/skins type=directory last-modified=2024-11-25 13:10:52 

 4 name=flash/skins/newskin.json type=.json file size=0 last-modified=2024-11-25 13:10:52 

 5 name=flash/filename type=file size=0 last-modified=2024-11-25 13:11:58 

 6 name=flash/directory_name type=directory last-modified=2024-11-25 13:12:10 

```

:::danger
如果设备的文件列表中有一个名为 **“flash”** 的目录，那么您希望在系统重启/断电后保留的文件必须存储在其中，因为该目录之外的任何内容都保存在 RAM 磁盘中，重启后会丢失。这不包括 .npk 升级文件，因为它们会在系统丢弃 RAM 驱动器内容之前由升级过程应用。

**警告：** 对于带有 NAND 闪存的多核设备（例如 CCR 系列路由器、RB4011iGS），RouterOS 使用写回机制，将文件更改缓存到 RAM 内存中，而不是立即写入闪存介质。文件更改将在绝对必要时才存储到闪存。写入可能会延迟最多 40 秒。这有助于减少 CPU 周期，从而提高性能。但是，当设备突然断电时，这可能会导致空文件或零长度文件，因为文件未完全保存到闪存中。

**警告：** 请注意，在某些情况下，RouterOS 可能会压缩文件以占用更少的磁盘空间。在这种情况下，您仍然会在**文件**菜单中看到原始文件大小。但是，在**资源**菜单中，您可能会注意到可用空间比预期的要多。

这是正常行为，因为在计算可用硬盘空间值时使用的是压缩后的文件大小。
:::

## 属性

| 属性 | 描述 |
| :-- | :-- |
| **contents** (*字符串*; 默认值: ) | 文件的实际内容 |
| **creation-time** (*时间*) **警告：** 直到 RouterOS 7.16 | 文件创建的时间 |
| **last-modified** (*时间*) | 文件创建或最后修改的时间。在 RouterOS 7.16 中取代 **creation-time** 引入。 |
| **name** (*字符串*) | 文件名 |
| **package-architecture** (*字符串*) | 包所构建的架构。仅适用于 RouterOS “.npk” 文件 |
| **package-built-time** (*字符串*) | 包构建的时间。仅适用于 RouterOS “.npk” 文件 |
| **package-name** (*字符串*) | 可安装包的名称。仅适用于 RouterOS “.npk” 文件 |
| **package-version** (*字符串*) | 可安装包的版本。仅适用于 RouterOS “.npk” 文件 |
| **size** (*整数*) | 文件大小（字节） |
| **type** (*字符串*) | 文件类型。对于文件夹，文件类型为 *directory* |

## 文件操作

### 创建新文件或目录

要创建新文件或目录：

```ros
[admin@MikroTik] > /file/add name=/flash/filename type=file           
[admin@MikroTik] > file add name=/flash/directory_name type=directory 
```

### 获取或读取文件内容

使用 *get* 命令，只能检索最大 60KB 的文件内容。如需访问更大文件的内容，请使用 *read* 命令。结果以数组形式返回。

例如：

```routeros
[admin@MikroTik] > :put [/file/get text.txt contents]
123456

[admin@MikroTik] > /file/read file=text.txt offset=2 chunk-size=3    
  data: 345
```

#### 菜单特定属性

| 属性 | 描述 |
| :-- | :-- |
| **chunk-size** (*整数 [1..32768]*; 默认值: ) | 将从文件读取的块大小 |
| **offset** (*整数*; 默认值: ) | 指定开始读取文件的偏移量 |

### 查看文件头部或尾部

使用 head 和 tail 函数，您可以输出文件内容的前 n 行或后 n 行。

例如：

```routeros
/file/head test.txt n=3 numbered 
 1: 1
 2: 2
 3: 3
```

#### 菜单特定属性

| 属性 | 描述 |
| :-- | :-- |
| **n** (*整数 [1..1000]*; 默认值: ) | 要打印的行数。 |
| **numbered** | 命令中存在该选项将在每行前面添加行号。 |

### 复制文件或目录

使用 copy 命令可以克隆文件或目录。

例如：

```routeros
/file/copy test1.txt name=dir1/test1copy.txt
/file/copy dir1 name=dir2
/file/print 
Columns: NAME, TYPE, SIZE, LAST-MODIFIED
# NAME                TYPE       SIZE  LAST-MODIFIED      
0 dir1                directory        2026-03-17 09:52:08
1 dir2                directory        2026-03-17 09:52:14
2 test1.txt           .txt file     0  2026-03-17 09:51:43
3 dir1/test1copy.txt  .txt file     0  2026-03-17 09:52:08
4 dir2/test1copy.txt  .txt file     0  2026-03-17 09:52:14
```