#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-05 19:47:08 -0500 (Sat, 05 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab08/except.py $
# $Revision: 89400 $


def main():
    nums = input("Please enter some values: ").split()
    total = 0
    for num in nums:
        try:
            total += float(num)
        except ValueError:
            pass
        finally:
            pass
    print("The sum is: {}".format(total))

if __name__ == "__main__":
    main()
