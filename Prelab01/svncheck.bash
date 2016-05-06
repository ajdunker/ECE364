#! /bin/bash
#
# $Author: ee364a11 $
# $Date: 2016-01-19 01:00:02 -0500 (Tue, 19 Jan 2016) $
# $HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a11/Prelab01/svncheck.bash $
# $Revision: 86106 $

exec 4<"file_list"
while read line <&4
do
    echo "$line: "
    if [[ $(svn status $line | wc -c) == 0 ]]
    then
	if [[ -x $line ]]
	then
	    echo " file is in SVN and executable"
	else
	    echo " file is in SVN, but not executable. "
	    svn propset svn:executable ON $line
	fi
    else
	if [[ -e $line && -x $line ]]
	then
	    svn add $line
	elif [[ -e $line && ! -x $line ]]
	then
	    echo " file is not executable, would you like to make it? [y/n]"
	    read a
	    if [[ $a == y ]]
	    then
		chmod +x $line
	    fi
	    svn add $line
	elif [[ ! -e $line ]]
	then
	    echo "Error: File $line appears to not exist here or in svn"
	fi
     fi
done

echo "Auto-committing code"
svn commit
exit 0