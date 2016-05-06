#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-02-25 15:33:13 -0500 (Thu, 25 Feb 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab05/practical1.py $
# $Revision: 88924 $

import glob

def rowSumIsValid(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[0][i]
    for i in range(1, n):
        temp = 0
        for j in range(n):
            temp += mat[i][j]
        if temp != total:
            return False
    return True


def columnSumIsValid(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][0]
    for i in range(1, n):
        temp = 0
        for j in range(n):
            temp += mat[j][i]
        if temp != total:
            return False
    return True


def magicSquareIsValid(filePath):
    f = open(filePath, 'r')
    data = f.readlines()
    n1 = len(data)
    sqr = []
    for i in range(len(data)):
        data[i] = data[i].strip().split()
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
        sqr.append(data[i])
        if len(data[i]) != n1:
            return False
    if columnSumIsValid(sqr) and rowSumIsValid(sqr):
        return True
    else:
        return False
    return True


def getTotalCost(itemSet):
    nItems = len(itemSet)
    rdict = {}
    files = glob.glob('./Stores/*.txt')
    for file in files:
        f = open(file, 'r')
        stPrice = {}
        store = file[9:-4]
        for line in f:
            data = line.strip().split(',')
            if len(data) == 2:
                stPrice[data[0].strip()] = float(data[1].strip()[1:])
        price = 0
        tempSet = itemSet.copy()
        for i in range(nItems):
            item = tempSet.pop()
            price += stPrice[item[0]] * item[1]
        rdict[store] = round(price, 2)
    return rdict


def getBestPrices(cpuSet):
    nItems = len(cpuSet)
    rdict = {}
    files = glob.glob('./Stores/*.txt')
    for file in files:
        f = open(file, 'r')
        stPrice = {}
        store = file[9:-4]
        for line in f:
            data = line.strip().split(',')
            if len(data) == 2:
                stPrice[data[0].strip()] = float(data[1].strip()[1:])
        tempSet = cpuSet.copy()
        for i in range(nItems):
            item = tempSet.pop()
            if item in stPrice:
                if item in rdict:
                    if rdict[item][0] > round(stPrice[item], 2):
                        rdict[item] = (round(stPrice[item], 2), store)
                else:
                    rdict[item] = (round(stPrice[item], 2), store)
    return rdict


def getMissingItems():
    allCPU = set()
    rdict = {}
    files = glob.glob('./Stores/*.txt')
    for file in files:
        f = open(file, 'r')
        for line in f:
            data = line.strip().split(',')
            if len(data) == 2:
                allCPU.add(data[0].strip())
    for file in files:
        storeCPU = set()
        f = open(file, 'r')
        store = file[9:-4]
        for line in f:
            data = line.strip().split(',')
            if len(data) == 2:
                storeCPU.add(data[0].strip())
        miss = allCPU - storeCPU
        rdict[store] = miss
    return rdict

def main():
    pass

if __name__ == "__main__":
    main()