#!/bin/bash
# Bash script redirect curl
curl  -L -sX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
