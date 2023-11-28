---
layout: post
title: "How to create and run Jekyll in a docker container"
date: 2023-11-28 19:22:00 +1100
categories: tech
tags: wiki tools web
---

Creating a new Jekyll site using Docker involves a few steps. You'll use the Jekyll Docker image to run Jekyll commands inside a container, avoiding the need to install Jekyll and its dependencies on your local machine. Here's how to do it:

### 1. Pull the Jekyll Docker Image
First, ensure you have Docker installed on your machine. Then, pull the official Jekyll Docker image:

```bash
docker pull jekyll/jekyll
```

This command downloads the latest Jekyll image to your machine.

### 2. Create a New Jekyll Site
Run the following Docker command to create a new Jekyll site. Replace `my-new-site` with your desired site name:

```bash
docker run --rm -v "$PWD:/srv/jekyll" jekyll/jekyll jekyll new my-new-site
```

This command does the following:
- `--rm`: Automatically remove the container when it exits.
- `-v "$PWD:/srv/jekyll"`: Mounts the current directory on your host to `/srv/jekyll` in the container.
- `jekyll new my-new-site`: Instructs Jekyll to create a new site in a directory named `my-new-site`.

After running this command, you should see a new directory `my-new-site` in your current directory, containing the Jekyll site structure.

### 3. Change Directory to the New Site
Navigate into your new Jekyll site directory:

```bash
cd my-new-site
```

### 4. Add `webrick` to Your Gemfile
Open the `Gemfile` in the root of your Jekyll project and add `webrick`:

```ruby
gem "webrick", "~> 1.7"
```

### 5. Run Jekyll Server Using Docker
To serve your Jekyll site using Docker, run:

```bash
docker run --rm -p 4000:4000 -v "$PWD:/srv/jekyll" jekyll/jekyll jekyll serve --watch --force_polling --incremental
```

This command:
- Serves your Jekyll site on port 4000.
- Maps the current directory to the container, allowing changes you make locally to be reflected in the container.
- Uses the `--watch`, `--force_polling`, and `--incremental` flags to automatically rebuild the site as files are changed.

### 6. Access Your Jekyll Site
Open a web browser and navigate to `http://localhost:4000`. You should see your new Jekyll site.

### 7. Developing Your Site
You can now start developing your site. Any changes you make to the files in the `my-new-site` directory will be reflected in the Docker container, and you can view updates by refreshing your browser.

### 8. Stop the Jekyll Server
To stop the Jekyll server, go to your terminal and press `Ctrl + C`.

By following these steps, you can use Docker to create and serve a new Jekyll site without needing to install Jekyll or its dependencies directly on your machine. This method ensures that your Jekyll environment is consistent and isolated from other projects.


### Notes:
based on ChatGPT