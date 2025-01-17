---
layout: archive
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Electrical and Computer Engineering, the University of Arizona, 2011-2016
* M.S. in Microwave Engineering, Harbin Institute of Technology, 2009-2011
* B.S. First Honor Degree in Electronics and Information Engineering, Harbin Institute of Technology, 2005-2009

Work experience
======
* Spring 2020: Senior Hardware Engineer
  * Google Inc., Mountain View, CA

* Fall 2017: Research Engineer
  * Facebook Connectivity, Los Angeles

* 2012: RFIC Engineer Interns
  * Broadcom Inc., Irvine, CA

* 2011-2016: Research Assistant
  * The University of Arizona, Irvine, CA

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
