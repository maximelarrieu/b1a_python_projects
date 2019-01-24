#!/usr/bin/python3

def convert(md):
    index = 0
    for index in md:
        md.replace("#", '<h1>')
        md.replace('##', '<h2>')
        md.replace('###', '<h3>')


md_file = open("README.md", "r")
md = md_file.read()
html = convert(md)
print(html)
