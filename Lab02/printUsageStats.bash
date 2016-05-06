#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-26 15:03:57 -0500 (Tue, 26 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab02/printUsageStats.bash $
# $Revision: 86909 $

if [[ $# != 1 ]]
then
    echo "Usage ./printUsageStats.bash <input>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 2
fi

tstamp=$(head -n 1 $1 | cut -d ' ' -f 3)
echo "Parsing file $1. Timestamp: $tstamp"
echo "Your choices are:"
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N Highest mem usages"
echo "4) Top 3 longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"

while ((1))
do

    printf "\nPlease enter your choice: "
    read choice

    if (( choice == 1))
    then
	IDs=$(head -n 1 $1 | cut -d ' ' -f 8)
	echo "Total number of active user IDs: $IDs"
    elif (( choice == 2))
    then
	printf "Enter a value for N: "
	read N
	for (( I=8; I < 8 + N; I++ ))
	do
	    load=$(head -n $I $1 | tail -n 1 | cut -d ' ' -f 9)
	    user=$(head -n $I $1 | tail -n 1 | cut -d ' ' -f 2)
	    echo "User $user is utilizing CPU resources at $load%"
	done
    elif (( choice == 3))
    then
	printf "Enter a value for N: "
	read N
	for (( I=1; I <= N; I++))
	do
	    load=$(tail -n +9 $1 | sort -nr -k10 | head -n $I | tail -n 1 | cut -d ' ' -f 10)
	    user=$(tail -n +9 $1 | sort -nr -k10 | head -n $I | tail -n 1 | cut -d ' ' -f 2)
	    echo "User $user is utilizing mem resources at $load%"
	done
    elif (( choice == 4))
    then
	for (( I=1; I<= 3; I++))
	do
	    pid=$(tail -n +9 $1 | sort -nr -k11 | head -n $I | tail -n 1 | cut -d ' ' -f 1)
	    cmd=$(tail -n +9 $1 | sort -nr -k11 | head -n $I | tail -n 1 | cut -d ' ' -f 12)
	    echo "PID: $pid, cmd: $cmd"
	done
    elif (( choice == 5))
    then
	printf "Please enter a valid username: "
	read user
	coms=$(cat $1 | grep "$user" | cut -d ' ' -f 12)
	arrcom=($coms)
	cpus=$(cat $1 | grep "$user" | cut -d ' ' -f 10)
	arrcpu=($cpus)
	for (( I=0; I < ${#arrcom[*]}; I++))
	do
	    echo "${arrcpu[$I]} ${arrcom[$I]}"
	done
    elif (( choice == 6))
    then
	exit 0
    fi
done

exit 0