---
layout: home
title: Home
---


# Welcome to My Blog!

Here are my latest posts:

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <p>Posted on {{ post.date | date: "%b %-d, %Y" }}</p>
    </li>
  {% endfor %}
</ul>
