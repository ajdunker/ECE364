#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 00:13:33 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab01/line_num.bash $
# $Revision: 86104 $

if [[ $# > 1 ]]
then
    echo "Error, only 1 command argument is accepted."
    exit 1
elif [[ $# == 0 ]]
then
    echo "Usage: line_num.bash <filename>"
    exit 0
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 1
fi

X=1

exec 4<$1

while read line <&4
do
    echo $X:$line
    ((X=$X+1))
done

exit 0