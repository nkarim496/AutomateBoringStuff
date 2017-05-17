#! python
# Usage:
# rsearch.py <regex> - search regex in files in current directory
# rsearch.py <regex> path - search regex in files in path

import sys
import os
import re

# if there are two arguments then change current working directory
pattern = "."
if len(sys.argv) == 3:
    os.chdir(sys.argv[2])
    pattern = re.compile(sys.argv[1])
elif len(sys.argv) == 2:
    pattern = re.compile(sys.argv[1])

# list of file names in cwd
files = os.listdir(os.getcwd())

# iterate through files list
for file in files:
    with open(file, encoding="utf-8") as a_file:
        for line in a_file:
            if pattern.search(line) is not None:
                print("Match found in %s" % a_file.name)
                print(line)
                break
