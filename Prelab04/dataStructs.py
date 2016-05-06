#! /usr/bin/env python3.4

import string
import glob
import filecmp
from decimal import Decimal

def getWordFrequency():
    puncset = set(string.punctuation)
    text = ""
    dict = {}
    files = glob.glob('./files/*.txt')
    for file in files:
        f = open(file, 'r')
        for line in f:
            for word in line:
                text += ' '.join(ch for ch in word if ch not in puncset)
        f.close()
    words = text.split()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

def getUniqueWords(file):
    f = open(file, 'r')
    puncset = set(string.punctuation)
    text = ""
    dict = {}
    for line in f:
        for word in line:
            text += ' '.join(ch for ch in word if ch not in puncset)
    f.close()
    words = text.split()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return len(dict)

def getDuplicates():
    files = glob.glob('./files/*.txt')
    freq = getWordFrequency()
    dict = {}
    for file1 in files:
        matchL = []
        for file2 in files:
            if (filecmp.cmp(file1, file2)):
                matchL.append(file2[8:11])
        if (len(matchL) > 1): dict[file1[8:11]] = (getUniqueWords(file1), sorted(matchL))
    return dict

def getPurchaseReport():
    itemList = open('purchases/Item List.txt', 'r')
    items = itemList.readlines()
    prices = {}
    report = {}
    for item in items:
        sItems = item.split()
        if len(sItems) == 2 and sItems[1] != "Price":
            prices[sItems[0]] = sItems[1][1:]
    purchases = glob.glob('./purchases/purchase*.txt')
    for file in purchases:
        sum = Decimal(0)
        f = open(file, 'r')
        data = f.readlines()
        ID = int(file[21:24])
        for entries in data:
            entry = entries.split()
            if len(entry) > 1 and entry[0] in prices:
                sum += Decimal(entry[1]) * Decimal(prices[entry[0]])
            report[ID] = float(sum)
    return report


def getTotalSold():
    purchases = glob.glob('./purchases/purchase*.txt')
    report = {}
    for file in purchases:
        f = open(file, 'r')
        data = f.readlines()
        for entries in data:
            entry = entries.split()
            if len(entry) > 1 and entry[0] != "Item":
                if entry[0] in report:
                    report[entry[0]] += int(entry[1])
                else:
                    report[entry[0]] = int(entry[1])
    return report

def main():
    return 0

if __name__ == "__main__":
    main()