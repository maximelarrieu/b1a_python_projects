#!/usr/bin/python3

import argparse
import markdown
import codecs

def to_Html():
    md_file = codecs.open("markedown_files/test.md", "r")
    body = md_file.read()
    html = markdown.markdown(body)
    html_file = open("html_files/index.html", "w")
    html_file.write(html)
    html_file.close()

to_Html()

parser = argparse.ArgumentParser()
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'
markdown_directory = 'markedown_files/'

parser.add_argument("-i", input_directory, help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", output_directory, help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()

if arg.input = markdown_directory
