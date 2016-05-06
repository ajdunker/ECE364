#! /usr/bin/env python3.4
#
# $Author: ee364a11 $
# $Date: 2016-03-08 15:19:40 -0500 (Tue, 08 Mar 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab08/netConverter.py $
# $Revision: 89570 $

from HardwareTasks import *


def verilog2vhdl(ver_line):
    try:
        item = processLine(ver_line)
        rstr = item[1]+": "+item[0] + " PORT MAP("
        for prt in item[2]:
            rstr += prt[0]+"=>"+prt[1]+", "
        rstr = rstr[:-2] + ");"
        return rstr
    except:
        return "Error: Bad Line."
    finally:
        pass


def convertNetlist(sourceFile, targetFile):
    wL = ""
    with open(sourceFile, 'r') as f:
        data = f.readlines()
    with open(targetFile, 'w') as f:
        for item in data:
            wL += verilog2vhdl(item) + "\n"
        f.writelines(wL)

if __name__ == "__main__":
    pass

