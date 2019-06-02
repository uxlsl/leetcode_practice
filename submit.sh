#!/bin/bash
set -x

for problem in `ls -d */`
do
	problem=${problem%%/}
	leetcode show $problem -gx -l python -o submit
	filename=`ls submit/|grep $problem`
	cp $problem/solution.py submit/$filename
done
