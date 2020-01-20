#!/usr/bin/python3
"""
    Get the 10 most recent commits from the repository specified
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    res = get('https://api.github.com/repos/{}/{}/commits'
              .format(argv[2], argv[1]))
    obj = res.json()
    for commit in obj[:10]:
        print('{}: {}'.format(commit.get('sha'),
                              commit.get('commit')
                              .get('author')
                              .get('name')))
