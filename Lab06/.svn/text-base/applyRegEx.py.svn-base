#! /usr/bin/env python3.4

import pprint as pp
import re


def getRejectedUsers():
    rlist = []
    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))[;, ]{1,}$", line)
        if matches is not None:
            mtemp = re.match(r"([\w]+),\s([\w]+)[;, ]{1,}$", line)
            if mtemp is not None:
                name = str(mtemp.group(2))+" "+str(mtemp.group(1))
                rlist.append(name)
            else:
                rlist.append(matches.group(1))
    rlist.sort()
    return rlist

def getUsersWithEmails():
    rdict = {}
    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))[;, ]{1,}(?P<email>([\w.-_]+)@([\w.-_]+))", line)
        if matches is not None:
            rdict[fixedName(matches.group("user"))] = matches.group("email")
    return rdict


def getUsersWithPhones():
    rdict = {}
    data = readFile("SiteRegistration.txt")
    for line in data:
        searches = re.search(r"(?P<phone>([\d(\s)-]{10,15}))", line)
        if searches is not None:
            matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
            rdict[fixedName(matches.group("user"))] = fixedPhone(searches.group("phone"))
    return rdict


def getUsersWithStates():
    rdict = {}
    data = readFile("SiteRegistration.txt")
    for line in data:
        searches = re.search(r"(\w+$)|(\w+\s\w+$)", line)
        if searches is not None:
            matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
            rdict[fixedName(matches.group("user"))] = searches.group(0)
    return rdict


def getUsersWithoutEmails():
    rlist = []
    ulist = []
    states = getUsersWithStates()
    phones = getUsersWithPhones()
    emails = getUsersWithEmails()

    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
        ulist.append(fixedName(matches.group("user")))
    for user in ulist:
        if user not in emails:
            if (user in states) or (user in phones):
                rlist.append(user)
    rlist.sort()
    return rlist


def getUsersWithoutPhones():
    rlist = []
    ulist = []
    states = getUsersWithStates()
    phones = getUsersWithPhones()
    emails = getUsersWithEmails()

    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
        ulist.append(fixedName(matches.group("user")))
    for user in ulist:
        if user not in phones:
            if (user in states) or (user in emails):
                rlist.append(user)
    rlist.sort()
    return rlist


def getUsersWithoutStates():
    rlist = []
    ulist = []
    states = getUsersWithStates()
    phones = getUsersWithPhones()
    emails = getUsersWithEmails()

    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
        ulist.append(fixedName(matches.group("user")))
    for user in ulist:
        if user not in states:
            if (user in phones) or (user in emails):
                rlist.append(user)
    rlist.sort()
    return rlist


def getUsersWithCompleteInfo():
    rdict = {}
    ulist = []
    states = getUsersWithStates()
    phones = getUsersWithPhones()
    emails = getUsersWithEmails()

    data = readFile("SiteRegistration.txt")
    for line in data:
        matches = re.match(r"(?P<user>([\w]+\s[\w]+)|([\w]+,\s[\w]+))", line)
        ulist.append(fixedName(matches.group("user")))
    for user in ulist:
        if (user in states) and (user in emails) and (user in phones):
            rdict[user] = (emails[user], phones[user], states[user])
    return rdict


def readFile(file):
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    return data

def fixedName(text):
    temp = re.match(r"([\w]+),\s([\w]+)", text)
    if temp is not None:
        name = str(temp.group(2))+" "+str(temp.group(1))
    else:
        name = text
    return name

def fixedPhone(phone):
    temp = re.match(r"([\d]{3})([\d]{3})([\d]{4})", phone)
    if temp is not None:
        return "(" + temp.group(1) + ") " + temp.group(2) + "-" + temp.group(3)
    temp = re.match(r"([\d]{3})-([\d]{3})-([\d]{4})", phone)
    if temp is not None:
        return "(" + temp.group(1) + ") " + temp.group(2) + "-" + temp.group(3)
    return phone

def main():
    pass

if __name__ == "__main__":
    main()
