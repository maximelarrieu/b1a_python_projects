#!/usr/bin/python3

import argparse
import markdown
import codecs
import re
import os

def to_Html(markdown_directory, html_directory):
    #number_of_file = 0
    index = 0
    for md_files in md_files_list:
        print(md_files_list[1])
        md_file = codecs.open(md_files_list[index], 'r', 'utf-8')
        body = md_file.read()
        html = markdown.markdown(body)
        html_file = open(html_directory.html, 'w')
        html_file.write(html)
        html_file.close()
        index += 1

parser = argparse.ArgumentParser()
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'

markdown_directory = 'markdown_files/'
md_files_list = os.listdir(markdown_directory)
html_directory = 'html_files/'

parser.add_argument("-i", input_directory, "--input", help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", output_directory, "--output", help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()

markdown_directory = args.input_directory
html_directory = args.output_directory

to_Html(args.input_directory, args.output_directory)
