---
categories:
- Misc
date: '2020-03-05'
slug: file-library
title: Sorting Files
---

Last year I read an interesting article about [the death of the computer file](https://onezero.medium.com/the-death-of-the-computer-file-doc-43cb028c0506).

Even though the convenience of having everything cloud hosted means I use Google Photos/Music/Docs etc, I still keep a backup copy of everything (especially photos) on a NAS as well.

I've got various systems for sorting things but every few years when I format or change computers I often end up losing them in the transfer.
So I thought it would be worth documenting them here for reference.

## Folder Structure

I came across the [Johnny Decimal](https://johnnydecimal.com) system for folder names. I only use the first two numbers not the IDs but even that works pretty well. Took a bit of time to think about how to categorise stuff initially.

## Photos

Many years ago I used to keep photos in folders based on events, and a seperate folder for videos.
But after getting a smartphone that became way too hard to manage.
Now I store them in folders based on the year the file was taken.
But renaming all the files and sorting them into folders can be scripted using [exiftool](https://exiftool.org/filename.html#ex12).

First, rename all photos based on date and time in the photo/video metadata.

```sh
exiftool -d %Y%m%d_%H%M%S%%-c.%%le "-filename<filemodifydate" "-filename<createdate" "-filename<datetimeoriginal" .
```

This is helpful to notice if the metadata is wrong (camera clock was set wrong) before they get shuffled into folders and get lost.
Also allows you to sort the photos chronologically.
I used to (not so much recently) set the title of photos based on the event, you can append that to the end of the filename also.

```sh
exiftool '-filename<%f_${title;}.%e' .
```

Finally, move all the image files from the current directory into a directory hierarchy based on year/month.

```sh
exiftool -d %Y/%m-%b "-directory<filemodifydate" "-directory<createdate" "-directory<datetimeoriginal" .
```

## Music

I found the best way to rename music is to use [beets](http://beets.io).
Although I remember that it was a bit of a pain to setup and to get the config to my liking.

```yaml
per_disc_numbering: yes
default: $format/$albumartist/$year - $album%aunique{}/$disc-$track $artist - $title
singleton: $format/Non-Album/$artist/$artist - $title
comp: $format/Compilations/$year - $album%aunique{}/$disc-$track $artist - $title
```
