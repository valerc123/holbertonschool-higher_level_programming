#!/usr/bin/python3
"""
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    res = get("https://swapi.co/api/people", params={'search': argv[1]})
    obj = res.json()
    print("Number of results: {}".format(obj.get('count')))
    for person in obj.get('results'):
        print(person.get('name'))
