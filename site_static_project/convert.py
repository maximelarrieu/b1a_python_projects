#!usr/bin/python3

md_file = open("markedown_files/test.md", "r")
md = md_file.read()
print(md)

print(md.replace('#', '<h1>'))
print(md.replace('##', '<h2>'))
print(md.replace('###', '<h3>'))
