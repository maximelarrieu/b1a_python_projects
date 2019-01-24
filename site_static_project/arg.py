#!/usr/bin/python3

import argparse
import os
import shutil

parser = argparse.ArgumentParser()
input_directory = '--input-directory'
output_directory = '--output-directory'
template_directory = '--template-directory'

parser.add_argument("-i", input_directory, help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", output_directory, help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", template_directory, help="folder containing web models to complete", action="store_true")
args = parser.parse_args()
if args.input_directory:
    print("input-directory")
if args.output_directory:
    shutil.copy('markedown_files/*.md', 'html_files/test.html')
    print("output-directory")
if args.template_directory:
    print("template-directory")
