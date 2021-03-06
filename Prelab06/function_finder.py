#! /usr/bin/env python3.4
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import sys
import re
import os

if len(sys.argv) != 2:
    print("Usage: function_finder.py [python_file_name]")
    exit(1)
if os.path.isfile(sys.argv[1]) == False and os.access(sys.argv[1], os.R_OK) == False:
    print("Error: Could not read %s" % sys.argv[1])
    exit(2)


def main(argv):
    f = open(argv[1], 'r')
    data = f.readlines()
    f.close()
    for line in data:
        match = re.match(r"\w{3}", line)
        if match is not None:
            if match.group() == 'def':
                function = re.match(r"(?P<def>[\w]{3})\s(?P<name>[\w.-_]{1,})\((?P<parameter>[\w.=-_,\s]{1,})", line)
                parameters = re.findall(r"[\w.=-_]{1,}", function.group("parameter"))
                print(function.group("name"))
                for i, param in enumerate(parameters):
                    print('Arg{}:'.format(i+1), param)

if __name__ == "__main__":
    main(sys.argv)
