---
layout: post
title: "Mac Shell Commands"
date: 2024-01-13 11:2t:00 +1100
categories: tech
tags: mac tools
---


## Count the Files

 To count the total number of files in the folder (including files in subdirectories), use the following command:
   ```
   find . -type f | wc -l
   ```
   - `find . -type f` lists all files (`-type f`) in the current directory (`.`) and its subdirectories.
   - `wc -l` counts the number of lines, which corresponds to the number of files listed by the `find` command.

If you want to count only the files in the current folder without including files in subdirectories, you can use:
   ```
   find . -maxdepth 1 -type f | wc -l
   ```
   - `-maxdepth 1` limits the search to the current directory only.

Remember to replace the directory path with the path to the folder you're interested in. This command will give you the total count of all files in that folder.
