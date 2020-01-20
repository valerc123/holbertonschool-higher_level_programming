#!/usr/bin/python3
"""Sends a request to the URL, display variable X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as request:
        header = request.headers.get("X-Request-Id")
        print(header)
