---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<style>
.tag-cloud {
  list-style: none;
  padding: 0;
}
.tag-cloud li {
  display: inline-block;
  margin: 0 5px 5px 0;
}
.tag-cloud a {
  background-color: #efefef;
  padding: 5px;
  border-radius: 5px;
  text-decoration: none;
  color: black;
}
</style>


<h2>All tags</h2>
{% capture temptags %}
  {% for tag in site.tags %}
    {{ tag[1].size | plus: 1000 }}#{{ tag[0] }}#{{ tag[1].size }}
  {% endfor %}
{% endcapture %}
{% assign sortedtemptags = temptags | split:' ' | sort | reverse %}

<ul class="tag-cloud">
{% for temptag in sortedtemptags %}
  {% assign tagitems = temptag | split: '#' %}
  {% capture tagname %}{{ tagitems[1] }}{% endcapture %}
   <li><a href="/tag/{{ tagname }}"><code class="highligher-rouge" style="color:#969595;border-color:hsla(0, 0%, 59%,0.6)"><nobr>{{ tagname }}</nobr></code></a></li>
{% endfor %}
</ul>
