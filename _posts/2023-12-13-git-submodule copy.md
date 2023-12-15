---
layout: post
title: "Git submodule"
date: 2023-12-13 10:00:00 +1100
categories: tech
tags: git tools
---

## Add a submodule
```bash
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book
```


## Update Submodule to Latest Commit in the Parent Repo

```bash
git pull
git submodule update --init
```

## Pull Latest Changes for Submodules
```bash
git submodule update --remote
```