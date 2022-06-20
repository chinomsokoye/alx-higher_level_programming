#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except Exception as exe:
        print("Exception: {}".format(exe), file=sys.stderr)
        return None
