#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-22 15:10:48 -0400 (Tue, 22 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab07/Institute.py $
# $Revision: 89764 $

import re


class Simulation:
    def __init__(self, simNo, simDate, chipName, chipCount, chipCost):
        self.simulationNumber = simNo
        self.simulationDate = simDate
        self.chipName = chipName
        self.chipCount = chipCount
        self.chipCost = chipCost
        self.simulationCost = chipCount * chipCost

    def __str__(self):
        rstring = '{}: {:03d}, {}, ${:06.2f}'.format(self.chipName, self.simulationNumber, self.simulationDate, self.simulationCost)
        return rstring


class Employee:
    def __init__(self, employeeName, employeeID):
        self.employeeName = employeeName
        self.employeeID = employeeID
        self.simulationsDict = {}

    def addSimulation(self, sim):
        if isinstance(sim, Simulation):
            self.simulationsDict[sim.simulationNumber] = sim

    def getSimulation(self, simNo):
        if simNo in self.simulationsDict:
            return self.simulationsDict[simNo]
        else:
            return None

    def __str__(self):
        rstr = '{}, {}: {:02d} Simulations'.format(self.employeeID, self.employeeName, len(self.simulationsDict))
        return rstr

    def getWorkload(self):
        rstr = '{}, {}: {:02d} Simulations'.format(self.employeeID, self.employeeName, len(self.simulationsDict))
        chips = []
        for item in self.simulationsDict:
            chips.append('\n{}: {:03d}, {}, ${:06.2f}'.format(self.simulationsDict[item].chipName, self.simulationsDict[item].simulationNumber, self.simulationsDict[item].simulationDate, self.simulationsDict[item].simulationCost))
        chips.sort()
        for item in chips:
            rstr += item
        return rstr

    def addWorkload(self, fileName):
        data = readFile(fileName)
        for line in data:
            line = line.strip().split()
            if len(line) == 5:
                sim = Simulation(int(line[0]), line[1], line[2], int(line[3]), float(line[4][1:]))
                self.addSimulation(sim)
        pass


class Facility:
    def __init__(self, facilityName):
        self.facilityName = facilityName
        self.employeesDict = {}

    def addEmployee(self, employee):
        if isinstance(employee, Employee):
            self.employeesDict[employee.employeeName] = employee

    def getEmployees(self, *args):
        empList = []
        for emp in args:
            if emp in self.employeesDict:
                empList.append(self.employeesDict[emp])
        return empList

    def __str__(self):
        rstr = '{}: {:02d} Employees'.format(self.facilityName, len(self.employeesDict))
        emps = []
        for emp in self.employeesDict:
            emps.append('\n{}, {}: {:02d} Simulations'.format(self.employeesDict[emp].employeeID, self.employeesDict[emp].employeeName, len(self.employeesDict[emp].simulationsDict)))
        emps.sort()
        for emp in emps:
            rstr += emp
        return rstr

    def getSimulation(self, simNo):
        for emp in self.employeesDict.values():
            if simNo in emp.simulationsDict.keys():
                return emp.simulationsDict[simNo]
        return None


def readFile(file):
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    return data

def main():
    pass

if __name__ == "__main__":
    main()