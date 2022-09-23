#!/usr/bin/python3
""" Takes in URL, sends request, display response body with variable
value X-Request-Id in response header """


if __name__ == "__main__":
    import requests
    import sys
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
