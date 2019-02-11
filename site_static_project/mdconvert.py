#!/usr/bin/python3

import argparse
import markdown
import codecs
import re
import os

head_html = 'html_files/head.html'
end_html = 'html_files/end.html'

def to_Html(markdown_directory, html_directory):
    counter = 0
    for file in markdown_files:
        md_file = codecs.open(f'{markdown_directory}/{file}', 'r')
        body = file.read()
        html = markdown.markdown(body)
        head_html_file = open(head_html, 'r')
        read_html_head = head_html_file.read()
        end_html_file = open(end_html, 'r')
        read_html_end = end_html_file.read()
        html_file = open(f'{html_directory}/index{counter}.html', 'w')
        html_file.write(read_html_head + '\n\t')
        html_file.write(html + '\n')
        html_file.write(read_html_end)
        html_file.close()
        counter += 1

parser = argparse.ArgumentParser(description="Convertisseur fichier markdown en fichier html")
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'

parser.add_argument( '--input', input_directory, help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument('-output', output_directory, help="final folder where files will be generated", action="store_true")
parser.add_argument('-t', template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()

markdown_directory = args.input
html_directory = args.output

markdown_files = os.listdir(markdown_directory)

to_HTML(markdown_directory, html_directory)
