#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 15:13:28 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab01/getCourseStats.bash $
# $Revision: 86182 $


if [[ $# != 1 ]]
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
elif [[ $1 = "ece364" || $1 = "ece337" || $1 = "ece468" ]]
then
    SECS=$(echo ls ./gradebooks/$1*.txt | wc -w)
    for (( I=1; I < $SECS; I++))
    do
	./getFinalScores.bash gradebooks/$1_section$I.txt
	if [[ $? != 0 ]]
	then
	    echo "Error while running getFinalScores.bash"
	    exit 3
	fi
	exec 4<"gradebooks/$1_section$I.out"
	while read line <&4
	do
	    ((NUM=$NUM+1))
	    ((AVG=$AVG+$(echo $line | cut -d ',' -f 2)))
	    if (( $(echo $line | cut -d ',' -f 2) > HIGHS ))
	    then
		HIGHS=$(echo $line | cut -d ',' -f 2)
		HIGHN=$(echo $line | cut -d ',' -f 1)
	    fi
	done
    done
    ((AVG=$AVG/$NUM))
    echo "Total students: $NUM"
    echo "Average score: $AVG"
    echo "$HIGHN had the highest score of $HIGHS"
else
    echo "Error: course $1 is not a valid option."
    exit 5
fi

exit 0