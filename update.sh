#!/bin/sh
echo "git add."
git add .
echo "git commit -m $@:" 
git commit -m "$@"
echo "git push:"
git push
