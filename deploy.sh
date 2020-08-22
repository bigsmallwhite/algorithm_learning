#!/bin/bash

echo -e "\033[0;32mDeploying updates to GitHub...\033[0m"

# add to cach

git add .

msg="$1 `date +%Y-%m-%d`"

if [ $# -eq 1 ]
  then msg="修改部分代码 `date +%Y-%m-%d`"
fi

git commit -m"$msg"

# push source to github
git push 
