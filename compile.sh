#!/usr/bin/env bash

commit_message=$1

git add content
git commit -m "$1"
git push -u origin dev

pelican content -o output -s publishconf.py
ghp-import -m "$1" --no-jekyll -b main output
git push origin main
