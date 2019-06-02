#!/bin/bash

# 安装leetcode 客户端
# https://github.com/skygragon/leetcode-cli
set -x

mkdir submit 

for problem in `ls -d */`
do
	problem=${problem%%/}
	leetcode show $problem -gx -l python -o submit
	filename=`ls submit/|grep $problem`
	cp $problem/solution.py submit/$filename
	sleep 3
done
