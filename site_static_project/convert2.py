#!/usr/bin/python3

#md.replace("#", '<h1>')
#if i == '##':
#    print(md.replace('##', '<h2>'))

#md.replace('###', '<h3>')

print("salut1")
md_file = open("markedown_files/test.md", "r")
body = md_file.read()
print("salut2")
html = md_file.replace("#", "<h1>")
print("salut")
html_file = open("html_files/index.html", "w")
html_file.write(html)
html_file.close()
