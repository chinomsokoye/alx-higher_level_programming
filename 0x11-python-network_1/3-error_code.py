#!/usr/bin/python3
""" Takes in URL, sends a request, display body of response """
if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError
    try:
        with urllib.request.urlopen(sys.arrgv[1]) as res:
            print(res.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
