#!/bin/bash

set -x

# 安装leetcode 客户端
# https://github.com/skygragon/leetcode-cli
# npm install -g leetcode-cli

mkdir submit 

for problem in `ls -d */`
do
	problem=${problem%%/}
	leetcode show $problem -gx -l python -o submit
	filename=`ls submit/|grep $problem`
	cp $problem/solution.py submit/$filename
	leetcode submit submit/$filename
	sleep 3
done
