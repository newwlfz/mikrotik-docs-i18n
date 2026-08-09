# Note

> The system note feature in RouterOS allows users to assign custom text messages displayed upon login, with options to show them at CLI or FTP logins and configure their content through the `/system/note` menu or via an uploaded file.

# Note

### Summary

**Sub-menu:** `/system/note`

The system note feature allows you to assign arbitrary text notes or messages that will be displayed on each login right after the banner. For example, you may distribute warnings between system administrators this way, or describe what that particular router actually does. To configure the system note, you may upload a plain text file named **sys-note.txt** on the router's FTP server, or, additionally, edit the settings in this menu

### Properties

| Property | Description |
| :-- | :-- |
| **note** (*string*; Default: ) | Note that will be displayed. |
| **show-at-login** (*yes \| no*; Default: **yes**) | Whether to show the system note on each login |
| **show-at-cli-login** (*yes* \| *no*, Default: **no**) | Whether to show the system note before the telnet login prompt. |

### Example

It is possible to add multi-line notes using an embedded text editor (*`/system/note/edit` note*), for example, add ASCII art to your home router:

```
/system/note/set note=
```

```
                                       .&                                         
                                     @&   @&                                      
                                     @@   @#                                      
                                       @@&                                        
                                ,      @@@      .                                 
                                @@@@@@@@@@@@@@@@@                                 
                                       @@@                                        
                                       @@@                                        
                                       @@@                                        
                          ,@           @@@           &                            
                         @@@@          @@@          @@@@                          
                          @@           @@@           @(                           
                           &@@         @@@         @@@                            
                             @@@@@     @@@     &@@@&                              
                                &@@@@@@@@@@@@@@@&                                 
                                      @@@@@             
```
