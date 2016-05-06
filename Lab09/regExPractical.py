#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-22 15:09:16 -0400 (Tue, 22 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab09/regExPractical.py $
# $Revision: 89761 $

import re


def getAddress(sentence):
    matches = re.search(r"[0-9a-fA-F]{2}(-|:)[0-9a-fA-F]{2}(-|:)[0-9a-fA-F]{2}(-|:)[0-9a-fA-F]{2}(-|:)[0-9a-fA-F]{2}(-|:)[0-9a-fA-F]{2}", sentence)
    if matches is not None:
        return matches.group(0)
    else:
        return None
    pass

def getSwitches(commandline):
    matches = re.findall(r"[+\\]([a-z])\s+([\w/:.]+)", commandline)
    matches.sort()
    return matches

def getElements(fullAddress):
    matches = re.match(r"(http://|https://)(?P<base>[\w.]+)/(?P<controller>[a-zA-Z0-9]+)/(?P<action>[a-zA-Z0-9]+)$", fullAddress)
    if matches is None:
        return None
    else:
        rtup = (matches.group('base'), matches.group('controller'), matches.group('action'))
        return rtup
