#! /usr/bin/env python3.4

import glob
import os
from pprint import pprint

def getDetails():
    details = {}
    studentIDs = {}
    f = open("./files/students.txt", 'r')
    for line in f:
        data = line.split('|')
        if data[0].strip() != "Student Name" and len(data) > 1:
            studentIDs[data[1].strip()] = data[0].strip()
    files = glob.glob('./files/EECS*.txt')
    for file in files:
        f = open(file, 'r')
        for line in f:
            data = line.split()
            if data[0].strip() != "Student" and len(data) > 1:
                if data[0].strip() in studentIDs:
                    if studentIDs[data[0]] in details:
                        details[studentIDs[data[0]]].add((file[12:15], int(data[1])))
                    else:
                        details[studentIDs[data[0]]] = {(file[12:15], int(data[1]))}
    return details

def getStudentList(classNumber):
    studentIDs = {}
    students = []
    f = open("./files/students.txt", 'r')
    for line in f:
        data = line.split('|')
        if data[0].strip() != "Student Name" and len(data) > 1:
            studentIDs[data[1].strip()] = data[0].strip()
    if os.path.isfile("./files/EECS"+classNumber+".txt"):
        f = open("./files/EECS"+classNumber+".txt", 'r')
    else:
        return []
    for line in f:
        data = line.split()
        if data[0].strip() != "Student" and len(data) > 1:
            if data[0].strip() in studentIDs:
                students.append(studentIDs[data[0]])
    return sorted(students)

def searchForName(studentName):
    studentIDs = {}
    classes = {}
    f = open("./files/students.txt", 'r')
    for line in f:
        data = line.split('|')
        if data[0].strip() != "Student Name" and len(data) > 1:
            studentIDs[data[0].strip()] = data[1].strip()
    if studentName in studentIDs:
        details = getDetails()
        studentD = details[studentName]
        for i in studentD:
            classes[i[0]] = i[1]
        return classes
    else:
        return {}

def searchForID(studentID):
    studentIDs = {}
    classes = {}
    f = open("./files/students.txt", 'r')
    for line in f:
        data = line.split('|')
        if data[0].strip() != "Student Name" and len(data) > 1:
            studentIDs[data[1].strip()] = data[0].strip()
    if studentID in studentIDs:
        details = getDetails()
        studentD = details[studentIDs[studentID]]
        for i in studentD:
            classes[i[0]] = i[1]
        return classes
    else:
            return {}

def findScore(studentName, classNumber):
    studentIDs = {}
    f = open("./files/students.txt", 'r')
    for line in f:
        data = line.split('|')
        if data[0].strip() != "Student Name" and len(data) > 1:
            studentIDs[data[0].strip()] = data[1].strip()
    if studentName in studentIDs:
        grades = searchForName(studentName)
        if classNumber in grades:
            return grades[classNumber]
        else:
            return None

def getHighest(classNumber):
    students = getStudentList(classNumber)
    if len(students) < 1:
        return ()
    maxG = 0
    maxS = ""
    for student in students:
        temp = findScore(student, classNumber)
        if temp > maxG:
            maxG = temp
            maxS = student
    maxT = (maxS, float(maxG))
    return maxT

def getLowest(classNumber):
    students = getStudentList(classNumber)
    if len(students) < 1:
        return ()
    lowG = 101
    lowS = ""
    for student in students:
        temp = findScore(student, classNumber)
        if temp < lowG:
            lowG = temp
            lowS = student
    maxT = (lowS, float(lowG))
    return maxT

def getAverageScore(studentName):
    grades = searchForName(studentName)
    if len(grades) < 1:
        return None
    sumScore = 0.0
    for i in grades:
        sumScore += grades[i]
    return(sumScore / len(grades))

def main():
    #pprint(getDetails())
    return 0

if __name__ == "__main__":
    main()