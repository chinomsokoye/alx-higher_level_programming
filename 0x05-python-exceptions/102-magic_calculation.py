#!/usr/bin/python
def magic_calculation(a, b):
    res = 0
    for x in range(1, 3):
        try:
            if (x > a):
                raise Exception("Too far")
            else:
                res += (a ** b) / x
        except Exception:
            res = a + b
            break
    return res
