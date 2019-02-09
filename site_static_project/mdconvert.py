#!/usr/bin/python3

import argparse
import markdown
import codecs
import glob
import os

def to_Html(markdown_directory, html_directory):
    counter = 0
    md_file = codecs.open(markdown_directory, "r")
    body = md_file.read()
    html = markdown.markdown(body)
    html_file = open(html_directory + 'index{counter}', "w")
    html_file.write(html)
    html_file.close()
    counter += 1

parser = argparse.ArgumentParser()
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'
markdown_directory = 'markedown_files/'
md_files = os.listdir(markdown_directory)
html_directory = 'html_files/'
#html_files = 'index2.html'

parser.add_argument("-i", input_directory, help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", output_directory, help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()
args.input = args.input_directory
args.ouput = args.output_directory

to_Html(markdown_directory, html_directory)
