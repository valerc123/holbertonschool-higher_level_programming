#!/usr/bin/python3
"""
    Takes in a letter and sends a POST request to URL
    with the letter as a parameter
"""
from sys import argv
from requests import post, get


if __name__ == "__main__":

    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ''
    res = post("http://0.0.0.0:5000/search_user", data={'q': letter})

    try:
        obj = res.json()
        if not obj:
            print("No result")
        else:
            print('[{}] {}'.format(obj.get('id'), obj.get('name')))
    except ValueError:
        print('Not a valid JSON')
