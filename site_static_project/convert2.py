#!/usr/bin/python3

def convert(md):
    md.replace("#", '<h1>')
    print(md)
    md.replace('##', '<h2>')
    md.replace('###', '<h3>')


md_file = open("markedown_files/test.md", "r")
md = md_file.read()
html = convert(md)
print(html)
