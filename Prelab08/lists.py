#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-05 19:47:08 -0500 (Sat, 05 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab08/lists.py $
# $Revision: 89400 $

import math


def find_median(list1, list2):
    Sorted_List = list1 + list2
    Sorted_List.sort()
    if(len(Sorted_List) % 2 == 0):
        Median = Sorted_List[math.floor((len(Sorted_List) - 1) / 2)]
    else:
        Median = Sorted_List[math.trunc(len(Sorted_List) / 2)]
    return Median, Sorted_List


def main():
    first = input("Enter the first list of numbers: ")
    second = input("Enter the second list of numbers: ")

    list1 = list(map(int, first.split()))
    list2 = list(map(int, second.split()))

    print("First list: {}".format(list1))
    print("Second list: {}".format(list2))

    (Median, Sorted_List) = find_median(list1, list2)

    print("Merged list: {}".format(Sorted_List))
    print("Median: {}".format(Median))

if __name__ == "__main__":
    main()
