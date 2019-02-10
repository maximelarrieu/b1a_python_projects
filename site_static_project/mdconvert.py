#!/usr/bin/python3

import argparse
import markdown
import codecs
import re
import os

def to_Html(markdown_file, html_file):
    md_file = codecs.open(markdown_file, 'r')
    body = md_file.read()
    html = markdown.markdown(body)
    head_html_file = open(head_html, 'r')
    read_html_head = head_html_file.read()
    end_html_file = open(end_html, 'r')
    read_html_end = end_html_file.read()
    html_file = open(html_file, 'w')
    html_file.write(read_html_head)
    html_file.write(html + '\n')
    html_file.write(read_html_end)
    html_file.close()

parser = argparse.ArgumentParser(description="Convertisseur fichier markdown en fichier html")
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'

markdown_file = 'markdown_files/test2.md'
html_file = 'html_files/test2.html'

head_html = 'html_files/head.html'
end_html = 'html_files/end.html'

parser.add_argument( '-i', input_directory, '--input', help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument('-o', output_directory, '--output', help="final folder where files will be generated", action="store_true")
parser.add_argument('-t', template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()

#markdown_directory = args.input
#html_directory = args.output

to_Html(markdown_file, html_file)
