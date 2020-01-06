#!/bin/bash
# Bash script that displays all HTTP methods the server will accept.
curl -is -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d " " 
