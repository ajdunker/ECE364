#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-22 15:09:16 -0400 (Tue, 22 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab09/timeManager.py $
# $Revision: 89761 $

from timeDuration import *


def getTotalEventSpan(eventName):
    event = TimeSpan(0, 0, 0)
    data = readData('Events.txt')
    for line in data:
        line = line.split()
        if line[0] == eventName:
            if line[1][2] == 'h':
                val = int(line[1][0:2]) * int(line[2])
                event = event + TimeSpan(0, 0, val)
            elif line[1][2] == 'd':
                val = int(line[1][0:2]) * int(line[2])
                event = event + TimeSpan(0, val, 0)
            elif line[1][2] == 'w':
                val = int(line[1][0:2]) * int(line[2])
                event = event + TimeSpan(val, 0, 0)
    return event


def rankEventsBySpan(*args):
    eDict = {}
    rList = []
    for el in args:
        eDict[getTotalEventSpan(el).getTotalHours()] = el
    sortL = list(eDict.keys())
    sortL.sort(reverse=True)
    for item in sortL:
        rList.append(eDict[item])
    return rList


def readData(file):
    f = open(file, 'r')
    data = f.readlines()
    return data

