#!/usr/bin/python3
"""
"""

from sys import argv
from requests import get


if __name__ == "__main__":
    res = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    obj = res.json()
    print(obj.get('id'))
