#!/usr/bin/python3
""" Lists ten commits of a repository
from most recent to oldest """


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get('https://developer.github.com/v3/repos/{}/{}/commits'.
                     format(sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for comm in r.json()[:10]:
            print("{}: {}".format(comm.get('sha'), comm.get('commit').
                                  get('author').get('name')))
