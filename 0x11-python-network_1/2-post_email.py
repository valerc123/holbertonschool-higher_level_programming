#!/usr/bin/python3
"""
    Sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the response
"""

from urllib import request, parse
import sys


if __name__ == "__main__":

    data = {'email': sys.argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')

    with request.urlopen(sys.argv[1], data) as request:
        req = request.read().decode('utf-8')
        print(req)
