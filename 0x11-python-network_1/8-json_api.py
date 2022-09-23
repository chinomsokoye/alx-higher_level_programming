#!/usr/bin/python3
""" Takes a letter, sends POST request to http://0.0.0.0:5000/search_user """


if __name__ == "__main__":
    import requests
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        diction = r.json()
        if diction == {}:
            print('No result')
        else:
            print("[{}] {}".format(diction.get('id'), diction.get('name')))
    except ValueError:
        print('Not a valid JSON')
