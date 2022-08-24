#!/bin/bash
set -e

date

git checkout master
git pull origin master

# Install dependencies
python3 -m pip install -r requirements.txt
wget -nc https://raw.githubusercontent.com/hugovk/flickr-tools/master/flickr_utils.py
