#!/usr/bin/python3
""" Takes in URL and email, sends POST request, displays body of response """
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    param = {'email': sys.argv[2]}
    body = urllib.parse.urlencode(param)
    body = body.encode('ascii')
    req = urllib.request.Request(sys.argv[1], body)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode("utf-8", "replace"))
