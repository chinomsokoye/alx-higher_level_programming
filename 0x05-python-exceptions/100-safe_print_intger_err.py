#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return False
    return True
