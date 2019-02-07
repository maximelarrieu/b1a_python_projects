#!/usr/bin/python3

import argparse
import markdown
import codecs
import glob
import os

def to_Html(pathMd):
    md_file = codecs.open(pathMd, "r")
    body = md_file.read()
    html = markdown.markdown(body)
    html_file = open("html_files/index.html", "w")
    html_file.write(html)
    html_file.close()

parser = argparse.ArgumentParser()
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'
markdown_directory = 'markedown_files/'
recup_md = glob.glob(markdown_directory + '*.md')
md_files = os.path.join(markdown_directory, recup_md)
html_directory = 'html_files/'

parser.add_argument("-i", input_directory, help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", output_directory, help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()
args.input = args.input_directory
args.ouput = args.output_directory

#if args.input_directory == markdown_directory:
#    print('bonjour')
pathMd = markdown_directory + md_files
to_Html(pathMd)
