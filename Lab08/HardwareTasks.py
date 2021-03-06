#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-08 15:19:40 -0500 (Tue, 08 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab08/HardwareTasks.py $
# $Revision: 89570 $

import re
import string


def idIsAcceptable(ver_id):
    matches = re.match(r"[\w_]+$", ver_id)
    if matches is not None:
        return True
    return False


def processSingle(ver_assignment):
    matches = re.match(r"\.([\w]+)\(([\w]+)\)$", ver_assignment)
    if matches is not None:
        return matches.group(1), matches.group(2)
    else:
        raise ValueError(ver_assignment)


# \s*([\w_]+)\s+([\w_]+)\s*\((\s*(\.([\w_]+)\(([\w_]+)\)),)+(\.([\w_]+)\(([\w_]+)\))

def processLine(ver_line):
    reList = []
    tupList = []
    matches = re.match(r"\s*([\w]+)\s+([\w]+)\s*\(((\s*\.[\w]+\([\w]+\),)+)\s*(\.[\w]+\([\w]+\))\s*\)$", ver_line)
    if matches is not None:
        reList.append(matches.group(1))
        reList.append(matches.group(2))
        leng = len(matches.groups())
        sL = matches.group(3).split(',')
        for item in sL:
            if len(item) > 0:
                tupList.append(processSingle(item.strip()))
        tupList.append(processSingle(matches.group(leng).strip()))
        reList.append(tuple(tupList))
        return tuple(reList)
    else:
        raise ValueError(ver_line)


if __name__ == "__main__":
    pass
