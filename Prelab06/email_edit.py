#! /usr/bin/env python3.4
#
# $Author$
# $Date$
# $HeadURL$
# $Revision$

import sys
import re


def main(argv):
    f = open(argv[1], 'r')
    data = f.readlines()
    f.close()
    for i in data:
        i = i.split()
        i[0] = re.sub(r"purdue.edu", r"ecn.purdue.edu", i[0])
        print(i[0]+"\t"+i[1])

if __name__ == "__main__":
    main(sys.argv)
