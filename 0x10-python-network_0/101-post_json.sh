#!/bin/bash
# curl to json file
curl -s -X POST "$1" -d @./"$2"
