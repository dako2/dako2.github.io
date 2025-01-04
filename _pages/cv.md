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
* Ph.D in Applied Electromagnetics, the University of Arizona, 2016
* M.S. in Microwave Engineering, Harbin Institute of Technology, 2011
* B.S. in Information and Communication Engineering, Harbin Institute of Technology, 2009

Work experience
======
* Spring 2020: Engineer
  * Google Inc., Mountain View, CA

* Fall 2017: Research Assistant
  * Facebook Connectivity, Los Angeles

* Summer 2012: Research Assistant
  * Broadcom Inc., Irvine, CA
  * Duties included: Tagging issues
  * Supervisor: Professor Git
  
Skills
======
* Hardware and software 

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
