#!/usr/bin/python3
"""
    Sends a requests and display the variable
    X-Request-Id in the response header
"""
import requests
import sys


res = requests.get(sys.argv[1])

print(res.headers["X-Request-Id"])
