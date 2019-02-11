---
title: "{{ cls }} Functions"
weight: {{ weight }}
---


| **Function**  | **Return Type** | **Description** |
|------------------|-------------|------------------------------------------|
{% for line in Lines -%}
| {{line.code}}{% for param in line.param_list -%}(*{{param}}*){% endfor %} | {{line.ReturnType}}| **Parameters:** <br> {% for param in line.line2 -%} *{{param}}* - <br> {% endfor %}<br>**Description:**<br>...<br>**Examples:**<br>... |
{% endfor %}