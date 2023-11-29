#!/usr/bin/env python

'''
tag_generator.py


This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

# Dictionary to hold tags and their posts
tag_posts = {}

for filename in filenames:
    with open(filename, 'r', encoding='utf8') as f:
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    for tag in current_tags[1:]:
                        if tag not in tag_posts:
                            tag_posts[tag] = []
                        tag_posts[tag].append(filename)
                    break
            if line.strip() == '---':
                crawl = not crawl

# Remove old tag files
if os.path.exists(tag_dir):
    old_tags = glob.glob(tag_dir + '*.md')
    for tag in old_tags:
        os.remove(tag)
else:
    os.makedirs(tag_dir)

# Create new tag files with links to the posts
for tag, posts in tag_posts.items():
    tag_filename = os.path.join(tag_dir, tag + '.md')
    with open(tag_filename, 'w', encoding='utf8') as f:
        f.write('---\nlayout: tagpage\n' + '\ntag: ' + tag + '\nrobots: noindex\n---\n\n')
        # f.write('## Posts tagged with ' + tag + '\n')
        # for post in posts:
        #     post_name = post.replace(post_dir, '').replace('.md', '')
        #     post_title = post_name.replace('-', ' ').title()
        #     f.write('- [' + post_title + '](' + '/' + post_name + ')\n')

print("Tag pages generated, count:", len(tag_posts))


