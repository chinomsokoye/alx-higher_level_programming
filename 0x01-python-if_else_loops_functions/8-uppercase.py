#!/usr/bin/python3
def uppercase(str):
    uppercase = 0
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            uppercase = 32
        else:
            uppercase = 0
        print("{}".format(chr(ord(c) - uppercase)), end="")
    print()
