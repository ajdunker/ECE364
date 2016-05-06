#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-25 19:30:18 -0500 (Mon, 25 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab02/process_temps.bash $
# $Revision: 86794 $

if [[ $# != 1 ]]
then
    echo "Usage: process_temps.bash <input_file>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file"
fi

while read -a line
do
    if [[ $line != "time" ]]
    then
	sum=0
	for i in ${line[*]}
	do
	    if (( i != ${line[0]} ))
	    then
		((sum+=$i))
	    fi
	done
	((num=${#line[*]}-1))
	((avg=$sum/$num))
	echo "Average temperature for time $line is $avg C."
    fi
done < $1