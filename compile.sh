#!/usr/bin/env bash

commit_message=$1

pelican content -o output -s publishconf.py
ghp-import -m "$1" --no-jekyll -b main output
git push origin main
