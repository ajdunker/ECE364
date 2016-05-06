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
        i = i.strip().split(':')
        ip, port = i[0], i[1]
        if re.match(r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b", ip):
            if port.isdigit():
                if int(port) < 1024:
                    print("%s:%s - Valid (root privileges required)" % (ip, port))
                elif int(port) < 32767:
                    print("%s:%s - Valid" % (ip, port))
                else:
                    print("%s:%s - Invalid Port Number" % (ip, port))
        else:
            print("%s:%s - Invalid IP Address" % (ip, port))

if __name__ == "__main__":
    main(sys.argv)
