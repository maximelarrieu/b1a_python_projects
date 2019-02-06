#!/usr/bin/python3

import markdown

md_file = open("markedown_files/test.md", "r")
body = md_file.read()
html = markdown.markdown(body)
html_file = open("html_files/index.html", "w")
html_file.close
