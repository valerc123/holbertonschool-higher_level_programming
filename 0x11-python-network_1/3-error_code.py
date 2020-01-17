#!/usr/bin/python3
"""
    Manage urllib.error.HTTPError exceptions
"""

from urllib import error, request
import sys

try:
    with request.urlopen(sys.argv[1]) as req:
        req = req.read().decode('utf-8')
        print(req)
except error.HTTPError as e:
    print("Error code: {}".format(e.code))
