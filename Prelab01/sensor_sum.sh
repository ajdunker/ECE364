#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 01:36:17 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab01/sensor_sum.sh $
# $Revision: 86107 $

if [[ $# > 1 ]]
then
    echo "Error, only 1 command argument is accepted."
    exit 1
elif [[ $# == 0 ]]
then
    echo "Usage: sensor_sum.sh <filename>"
    exit 0
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 1
fi

exec 4<$1
while read line <&4
do
    name=$(echo "$line" | cut -d '-' -f 1)
    sum=$(($(echo $line | cut -d ' ' -f 2)+$(echo $line | cut -d ' ' -f 3)+$(echo $line | cut -d ' ' -f 4)))
    echo "$name $sum"
done
