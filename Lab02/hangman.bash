#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-02-01 00:57:14 -0500 (Mon, 01 Feb 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Lab02/hangman.bash $
# $Revision: 87371 $

words=(banana parsimonious sesquipedalian)
((rand=$RANDOM%3))
ans=${words[$rand]}
len=$(echo $ans | wc -c)
((len=len-1))
A=(0)
for (( I=1; I<=len; I++ ))
do
    A[$I]="."
done

echo "Your word is $len letters long."
printf "Words is: "
for (( I=1; I<=len; I++ ))
do
    printf "${A[$I]}"
done

count=0

while ((1))
do
    match=0
    printf "\n  Make a guess: "
    read guess
    for (( I=1; I<=len; I++ ))
    do
	ansc=$(echo $ans | head -c $I | tail -c 1)
	if [[ $ansc == $guess && ${A[$I]} == "." ]]
	then
	    if (( match == 0 ))
	    then
		printf "  Good going!\n"
		((match=match+1))
	    fi
	    ((count=count+1))
	    A[$I]=$guess
	fi
    done
    
    if (( match == 0 ))
    then
	printf "  Sorry, try again.\n"
    fi

    if (( count == len ))
    then
	printf "\nCongratulations! You guessed the word: $ans\n"
	exit 0
    fi
    printf "  "
    for (( I=1; I<=len; I++ ))
    do
	printf "${A[$I]}"
    done
done