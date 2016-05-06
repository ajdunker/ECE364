#! /usr/bin/env python3.4

import sys

def getPairwiseDifference(vec):
    if type(vec) != list: return None
    if len(vec) < 1: return None
    diffVec = []
    for i in range(len(vec) - 1):
        diffVec.append(vec[i+1] - vec[i])
    return diffVec

def flatten(l):
    if type(l) != list: return None
    if len(l) < 1: return None
    flatL = []
    for i in l:
        if type(i) != list: return None
        flatL += i
    return flatL

def partition(l, n):
    if type(l) != list: return None
    if len(l) < 1: return None
    partL = []
    subL = []
    for i in l:
        if len(subL) == n:
            partL.append(subL)
            subL = []
        subL.append(i)
    partL.append(subL)
    return partL

def rectifySignal(signal):
    if type(signal) != list: return None
    if len(signal) < 1: return None
    for i in range(len(signal)):
        if signal[i] < 0:
            signal[i] = 0
    return signal

def floatRange(a, b, s):
    if a >= b: return None
    inc = a
    list = []
    while inc <= b:
        list.append(round(inc, 2))
        inc += s
    if list[-1] != b:
        list.append(b)
    return list

def getLongestWord(sentence):
    if type(sentence) != str: return None
    senList = sentence.split()
    if len(senList) < 2: return None
    max = 0
    maxW = ""
    for i in senList:
        if len(i) > max:
            max = len(i)
            maxW = i
    return maxW

def decodeNumbers(numList):
    if type(numList) != list: return None
    decoded = ""
    for i in numList:
        if type(i) != int: return None
        decoded += chr(i)
    return decoded

def getCreditCard(s):
    if len(s) < 1: return None
    ccL = []
    for i in s:
        if i.isdigit():
            ccL.append(int(i))
    return ccL

def main():
    print(getPairwiseDifference([8, 4, 15, 10, 12, 14, 13]))

if __name__ == "__main__":
    main()