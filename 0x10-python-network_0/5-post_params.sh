#!/bin/bash
#  Bash script that sends a GET request to the URL
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
