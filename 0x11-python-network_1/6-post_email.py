#!/usr/bin/python3
""" Takes URL and email, sends POST request, display body of response """


if __name__ == "__main__":
    import requests
    import sys
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
