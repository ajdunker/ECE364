#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 00:10:42 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab01/sum.bash $
# $Revision: 86103 $

X=0

while (( $# != 0 ))
do
    ((X=$X+1))
    shift
done

echo "$X"

exit 0