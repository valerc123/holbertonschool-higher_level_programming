#!/usr/bin/python3
"""
    Script that fetches status
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("- type: {}".format(type(r)))
    print("- content: {}".format(r))
