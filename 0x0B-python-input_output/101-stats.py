#!/usr/bin/python3
"""
Module 101-stats
Read stdin line by line
Computes metrics
"""


import sys


def print_size_and_codes(size, stat_codes):
    """Prints sizes and codes"""
    print("File size: {:d}".format(size))
    for i, j in sorted(stat_codes.items()):
        if j:
            print("{:s}: {:d}".format(i, j))


def parse_stdin_and_compute():
    """Parses and computes value"""
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            field = list(map(str, line.strip().split(" ")))
            size += int(field[-1])
            if field[-2] in stat_codes:
                stat_codes[field[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_size_and_codes(size, stat_codes)
    except KeyboardInterrupt:
        print_size_and_codes(size, stat_codes)
        raise
    print_size_and_codes(size, stat_codes)


parse_stdin_and_compute()
