#!/usr/bin/python3
for tebahpla in range(122, 96, -1):
    if (tebahpla % 2 != 0):
        tebahpla -= 32
    print("{:s}".format(chr(tebahpla)), end="")
