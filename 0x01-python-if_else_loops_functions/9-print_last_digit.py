#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(str(number)[-1])
    print("{}".format(last_digit), end="")
    return(last_digit)
