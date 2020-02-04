#!/usr/bin/python3
"""
"""

from sys import argv
from requests import post


if __name__ == "__main__":
    res = post(argv[1], data={'email': argv[2]})
    print(res.text)
