#!/bin/bash
# curl to json file
curl -s -X POST -H "Content-Type: application/json" "$1" -d @./"$2"
