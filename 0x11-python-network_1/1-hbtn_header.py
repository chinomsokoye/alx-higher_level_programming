#!/usr/bin/python3
""" Takes in URL, sends request to the URL, display value of the variable
X-Request-Id found in the header of the response """


if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as res:
        head = res.headers.get('X-Request-Id')
        print(head)
