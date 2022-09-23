#!/usr/bin/python3
""" Lists ten commits of a repository
from most recent to oldest """


if __name__ == "__main__":
    import requests
    import sys
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
