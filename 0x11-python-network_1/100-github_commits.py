#!/usr/bin/python3
""" Lists ten commits of a repository
from most recent to oldest """


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for com in r.json()[:10]:
            print("{}: {}".format(com.get('sha'), com.get('commit').get(
                'author').get('name')))
