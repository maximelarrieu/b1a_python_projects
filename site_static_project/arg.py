#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--idirectory", help="sources files folder (contains markdown files)", action="store_true")
parser.add_argument("-o", "--output-directory", help="final folder where files will be generated", action="store_true")
parser.add_argument("-t", "--template-directory", help="folder containing web models to complete", action="store_true")
args = parser.parse_args()
if args.idirectory:
    print("input-directory")
if args.output-directory:
    print("output-directory")
if args.template-directory:
    print("template-directory")
