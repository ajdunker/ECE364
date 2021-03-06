#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-25 02:33:16 -0500 (Mon, 25 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab02/run.bash $
# $Revision: 86685 $

if [[ $# != 2 ]]
then
    echo "Usage ./run.bash <input> <output>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not reable"
    exit 2
fi

if gcc $1 -o quick_sim
then
    if [[ -e $2 ]]
    then
	printf "$2 exists. Would you like to delete it? "
	read ans
	if [[ $ans == "y" ]]
	then
	    rm $2
	    filename=$2
	    touch $filename
	elif [[ $ans == "n" ]]
	then
	    printf "Enter a new filename: "
	    read filename
	    touch $filename
	fi
    else
	filename=$2
	touch $filename
    fi
    cache=(1 2 4 8 16 32)
    width=(1 2 4 8 16)
    fastest=999999
    for i in ${cache[*]}
    do
	for j in ${width[*]}
	do
	    commandA=$(quick_sim $i $j a)
	    processor=$(echo $commandA | cut -d ':' -f 2)
	    cache=$(echo $commandA | cut -d ':' -f 4)
	    issue=$(echo $commandA | cut -d ':' -f 6)
	    cpi=$(echo $commandA | cut -d ':' -f 8)
	    time=$(echo $commandA | cut -d ':' -f 10)
	    echo "$processor:$cache:$issue:$cpi:$time" >> $filename
	    if(( $fastest > $time ))
	    then
		ftime=$time
		fproc=$processor
		fcache=$cache
		fissue=$issue
	    fi
	    commandI=$(quick_sim $i $j i)
	    processor=$(echo $commandI | cut -d ':' -f 2)
	    cache=$(echo $commandI | cut -d ':' -f 4)
	    issue=$(echo $commandI | cut -d ':' -f 6)
	    cpi=$(echo $commandI | cut -d ':' -f 8)
	    time=$(echo $commandI | cut -d ':' -f 10)
	    echo "$processor:$cache:$issue:$cpi:$time" >> $filename
	    if(( $fastest > $time ))
	    then
		ftime=$time
		fproc=$processor
		fcache=$cache
		fissue=$issue
	    fi
	done
    done
    echo "Fastest run time achieved by $fproc with the cache size $fcache and issue width $issue was $ftime"
    exit 0
else
    echo "error: quick_sim could not be compiled!"
    exit 1
fi