#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-18 23:25:48 -0500 (Mon, 18 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab01/exist.bash $
# $Revision: 86073 $

while (( $# != 0 ))
do
    if [[ -r $1 ]]
    then
	printf "File %s is readable!\n" $1
    else
	touch $1
    fi
    shift
done

exit 0