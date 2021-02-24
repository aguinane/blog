---
title: Linux Cheatsheat
type: page
---

This is a reference for myself of all the stuff I need to do to set up a new computer after a format.

## Mount Network Shares

This is suprisingly hard in Linux.
Eventually I found this [AskUbuntu answer](https://askubuntu.com/questions/313093/how-do-i-mount-a-cifs-share-via-fstab-and-give-full-rw-to-guest).

First you need to set up user permissions and groups correctly so everyone can have write access (and find out the associated id's).

```shell
id alex
sudo groupadd guinmans
sudo usermod -a -G guinmans alex
getent group guinmans
```

Modify the fstab to mount on boot:
```shell
sudo nano /etc/fstab
```
Add entry for the network shares:
```
//10.0.0.215/media  /media/nasmedia  cifs  vers=3.0,username=<user>,password=<pass>,uid=1000,gid=1002,iocharset=utf8,file_mode=0777,dir_mode=0777,noperm 0 0
//10.0.0.215/files  /media/nasfiles  cifs  vers=3.0,username=<user>,password=<pass>,uid=1000,gid=1002,iocharset=utf8,file_mode=0777,dir_mode=0777,noperm 0 0
```


Run the below to see if it worked:
```shell
mount -a
```

# Installs

``` shell
# Windows file sharing
sudo apt install cifs-utils
# Add right click option to resize images
sudo apt install imagemagick nautilus-image-converter
```
