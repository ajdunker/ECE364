#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-02-25 16:20:18 -0500 (Thu, 25 Feb 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab05/scheduler.bash $
# $Revision: 88926 $

if [[ $# != 1 ]]
then
    echo "Usage ./scheduler.bash <input>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not readable"
    exit 2
elif [[ -e "schedule.out" ]]
then
    echo "Error: schedule.out already exists"
    exit 3
fi

people=($(wc -l $1 | tail -n1))

times="07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00"
touch "schedule.out"

printf "\t%s" $times >> "schedule.out"
printf "\n" >> "schedule.out"
I=0
exec 4<$1
A=(0 0 0 0 0 0 0 0 0 0 0 0)
A[0]=$(egrep "[, ]+7:00" $1 | wc -l | tail -n1)
A[1]=$(egrep "[, ]+8:00" $1 | wc -l | tail -n1)
A[2]=$(egrep "[, ]+9:00" $1 | wc -l | tail -n1)
A[3]=$(egrep "10:00" $1 | wc -l | tail -n1)
A[4]=$(egrep "11:00" $1 | wc -l | tail -n1)
A[5]=$(egrep "12:00" $1 | wc -l | tail -n1)
A[6]=$(egrep "13:00" $1 | wc -l | tail -n1)
A[7]=$(egrep "14:00" $1 | wc -l | tail -n1)
A[8]=$(egrep "15:00" $1 | wc -l | tail -n1)
A[9]=$(egrep "16:00" $1 | wc -l | tail -n1)
A[10]=$(egrep "17:00" $1 | wc -l | tail -n1)

echo ${A[0]}

printf "Total\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" ${A[0]} ${A[1]} ${A[2]} ${A[3]} ${A[4]} ${A[5]} ${A[6]} ${A[7]} ${A[8]} ${A[9]} ${A[10]} >> "schedule.out"
printf "\n" >> "schedule.out"

while read line <&4
do
    name=($(echo $line | cut -f1))
    printf "%s" $name >> "schedule.out"
    check=0
    
    printf "\n" >> "schedule.out"
done
