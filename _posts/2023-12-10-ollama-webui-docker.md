---
layout: post
title: "Run Ollama web chat locally"
date: 2023-12-10 17:22:00 +1100
categories: tech
tags: AI tools
---

## Build locally
```
git clone https://github.com/ivanfioravanti/chatbot-ollama.git
cd chatbot-ollama
docker build -t chatbot-ollama .
docker run -p 3000:3000 chatbot-ollama
```

## Pull from ghcr
```
docker run -p 3000:3000 ghcr.io/ivanfioravanti/chatbot-ollama:main
```