# Files

> The File menu in MikroTik RouterOS allows managing user space files, including creating/editing/deleting files and directories, viewing package details for .npk files, and storing critical files in the 'flash' directory to persist after reboot. It supports file size up to 60KB and provides warnings about RAM disk behavior, write-back caching, and compressed file storage.

# Files

The File menu shows all user space files on the router. It is possible to create a new file or directory, edit the file content, delete a file or directory.  If a RouterOS ".npk" package is uploaded, the file menu will also show package-specific information, for example, architecture, build date and time, etc.

:::warning
It is possible to retrieve content and edit files up to 60KB in size. For accessing contents of larger files, please refer to section [Get File Contents](files.md#get-or-read-file-contents).
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
If the device has a directory named **"flash"** in its file list, then files which you want to be kept after the system reboot/power cycle must be stored within it, as anything outside of it is kept within a RAM disk and will be lost upon reboot. This does not include .npk upgrade files as they will be applied by the upgrade process before the system discards the RAM drive content.

**Warning:** For multicore devices with NAND flash memory (e.g. CCR series routers, RB4011iGS), RouterOS uses a write-back that will cache file changes into RAM memory instead of writing them straight away into flash media. The file changes will be stored on the flash when it is absolutely necessary. The writing can be delayed by up to 40 seconds. This helps to reduce CPU cycles which results in better performance. However, this can cause empty or zero-length files when a device experiences a sudden power loss, because files were not fully saved on the flash.

**Warning:** Please note that in some cases, RouterOS may compress files to occupy less disk space. In such situations, you will still see the original file size in the **File** menu. However, in the **Resource** menu, you may notice that there is more free space than expected.

This is normal behavior, as the compressed file size is used when calculating the free-hdd-space value.
:::

## Properties

| Property | Description |
| :-- | :-- |
| **contents** (*string*; Default: ) | The actual content of the file |
| **creation-time** (*time*) **Warning:** Until RouterOS 7.16  | A time when the file was created  |
| **last-modified** (*time*) | The time when the file was created or last modified. Introduced instead of **creation-time** in RouterOS 7.16.  |
| **name** (*string*) | Name of the file |
| **package-architecture** (*string*) | Architecture that the package is built for. Applies only to RouterOS ".npk" files |
| **package-built-time** (*string*) | A time when the package was built. Applies only to RouterOS ".npk" files |
| **package-name** (*string*) | Name of the installable package. Applies only to RouterOS ".npk" files |
| **package-version** (*string*) | A version of the installable package. Applies only to RouterOS ".npk" files |
| **size** (*integer*) | File size in bytes |
| **type** (*string*) | Type of the file. For folders, the file type is the *directory* |

## File operations

### Create new file or directory

To create a new file or directory:

```ros
[admin@MikroTik] > /file/add name=/flash/filename type=file           
[admin@MikroTik] > file add name=/flash/directory_name type=directory 
```

### Get or read file contents

Using the *get* command, it is possible to retrieve file contents only from files up to 60KB in size. For accessing contents of larger files, use the command *read*. The result is returned as an array.

For example:

```routeros
[admin@MikroTik] > :put [/file/get text.txt contents]
123456

[admin@MikroTik] > /file/read file=text.txt offset=2 chunk-size=3    
  data: 345
```

#### Menu specific properties

| Property | Description |
| :-- | :-- |
| **chunk-size** (*integer [1..32768]*; Default: ) | Chunk size that will be read from file |
| **offset** (*integer;*Default:) | Specifies offset where to start reading file |

### Head or tail a file

Using head and tail functions you can output the first or the last n lines of file contents.

For example:

```routeros
/file/head test.txt n=3 numbered 
 1: 1
 2: 2
 3: 3
```

#### Menu specific properties

| Property | Description |
| :-- | :-- |
| **n** (*integer [1..1000]*; Default: ) | Number of lines to be printed. |
| **numbered** | The presence of the option in the command will add a line number in front of each line. |

### Copy a file or directory

Using a copy command you can clone a file or directory.

For example:

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
