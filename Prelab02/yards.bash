#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-25 00:39:53 -0500 (Mon, 25 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab02/yards.bash $
# $Revision: 86676 $

if(($#!=1))
then
    echo "Usage: yards.bash <filename>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 2
fi

max=0

while read -a line
do
    sum=0
    avg=0
    var=0
    nTeams=0
    for i in ${line[*]}
    do
	((sum+=$i))
    done
    ((nTeams=${#line[*]}-1))
    ((avg=$sum/$nTeams))
    for i in ${line[*]}
    do
	if (( i!=${line[0]} ))
	then
	    ((variance+=(($avg-$i)*($avg-$i))))
	fi
    done
    ((variance/=$nTeams))
    echo "${line[0]} schools averaged $avg yards receiving with a variance of $variance"
    if(($max<$avg))
    then
	max=$avg
    fi
done < $1
echo "The largest average yardage was $max"
exit 0
