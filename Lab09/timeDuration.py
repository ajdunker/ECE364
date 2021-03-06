#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-22 15:09:16 -0400 (Tue, 22 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab09/timeDuration.py $
# $Revision: 89761 $

import math

class TimeSpan:

    def __init__(self, weeks, days, hours):
        tdays = 0
        tweek = 0
        if type(weeks) is int and type(days) is int and type(hours) is int:
            if hours >= 0:
                if hours >= 24:
                    tdays = int(math.floor(hours / 24))
                    self.hours = hours % 24
                else:
                    self.hours = hours
            else:
                raise ValueError
            tdays += days
            if tdays >= 0:
                if tdays >= 7:
                    tweek = int(math.floor(tdays / 7))
                    self.days = tdays % 7
                else:
                    self.days = tdays
            else: raise ValueError
            if weeks >= 0:
                self.weeks = tweek + weeks
            else:
                raise ValueError
        else:
            raise TypeError

    def __str__(self):
        # rstring = '{}: {:03d}, {}, ${:06.2f}'.format(self.chipName, self.simulationNumber, self.simulationDate, self.simulationCost)
        rstring = '{:02d}W {:01d}D {:02d}H'.format(self.weeks, self.days, self.hours)
        return rstring

    def getTotalHours(self):
        return (self.weeks * (7 * 24) + self.days * 24 + self.hours)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return TimeSpan(self.weeks + other.weeks, self.days + other.days, self.hours + other.hours)
        else:
            raise TypeError

    def __mul__(self, other):
        if type(other) is int:
            if other <= 0:
                raise ValueError
            else:
                return TimeSpan(self.weeks * other, self.days * other, self.hours * other)
        else:
            raise TypeError

    def __rmul__(self, other):
        if type(other) is int:
            if other > 0:
                return TimeSpan(self.weeks * other, self.days * other, self.hours * other)
            else:
                raise ValueError
        else:
            raise TypeError
