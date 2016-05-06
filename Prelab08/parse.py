#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-05 19:47:08 -0500 (Sat, 05 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab08/parse.py $
# $Revision: 89400 $

import sys


def main():
    try:
        f = open(sys.argv[1])
        lines = f.readlines()
        data = [line.split() for line in lines]
        for line in data:
            total = 0
            count = 0
            string = ""
            for item in line:
                try:
                    total += int(item)
                    count += 1
                except ValueError:
                    string += item + ' '
            if total:
                print('{0:.3f}'.format(total/count), string)
            else:
                print(string)
    except IndexError:
        print("Usage: parse.py [filename]")
    except IOError:
        print(sys.argv[1], "is not a readable file.")
    finally:
        pass

if __name__ == "__main__":
    main()
