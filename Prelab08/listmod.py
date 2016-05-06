#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-05 19:47:08 -0500 (Sat, 05 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab08/listmod.py $
# $Revision: 89400 $

from lists import *

first = input("Enter the first list of numbers: ")
second = input("Enter the second list of numbers: ")

list1 = list(map(int, first.split()))
list2 = list(map(int, second.split()))

print("First list: {}".format(list1))
print("Second list: {}".format(list2))

(Median, Sorted_List) = find_median(list1, list2)

print("Merged list: {}".format(Sorted_List))
print("Median: {}".format(Median))
