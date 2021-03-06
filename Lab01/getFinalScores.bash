#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 15:13:28 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab01/getFinalScores.bash $
# $Revision: 86182 $

if [[ $# != 1 ]]
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
else
    if [[ ! -r $1 ]]
    then
	echo "Error reading input file: $1"
	exit 2
    else
	FILEOUT=$(echo "$1" | cut -d '.' -f 1)".out"
	if [[ -e $FILEOUT ]]
	then
	    echo "Output file $FILEOUT already exists"
	    exit 3
	else
	    exec 4<$1
	    touch $FILEOUT
	    while read line <&4
	    do
		name=$(echo $line | cut -d ',' -f 1)
		assignments=$(echo $line | cut -d ',' -f 2)
		midterm1=$(echo $line | cut -d ',' -f 3)
		midterm2=$(echo $line | cut -d ',' -f 4)
		project=$(echo $line | cut -d ',' -f 5)
		((final=assignments*15/100+midterm1*30/100+midterm2*30/100+project*25/100))
		echo $name,$final >>$FILEOUT
	    done
	fi
    fi
fi

exit 0