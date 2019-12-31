#!/usr/bin/env python3
#-*- coding: utf-8 -*-
""" Chrome Coverage to CSS file """

# Standard library imports
import sys
import json

# Third party library imports

# Debug
from pdb import set_trace as st

JSON_COVERAGE = sys.argv[1]
CSS_NAME = sys.argv[2]

def main():
    with open(JSON_COVERAGE, 'r') as json_coverage_file:
        json_coverage = json.loads(json_coverage_file.read())

    for coverage in json_coverage:
        css_name = coverage['url'].split('/')[-1]
        if CSS_NAME != css_name:
            continue
        css_output_file = open(css_name, 'w+')
        for rng in enumerate(coverage['ranges']):
            css_output_file.write(coverage['text'][rng[1]['start']:rng[1]['end']])
        css_output_file.close()

if __name__ == "__main__":
    main()
