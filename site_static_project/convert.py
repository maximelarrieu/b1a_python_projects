#!usr/bin/python3

import markdown

md = open("README.md", "r")
print md.read()
md.close()
# print(md.replace('#', '<h1>'))
