#!/bin/bash
# Bash script that display size in bytes
curl -s "$1" | wc -c
