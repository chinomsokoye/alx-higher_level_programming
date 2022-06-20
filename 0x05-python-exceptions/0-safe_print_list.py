#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if (my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                couunt += 1
            except IndexError:
                print()
                return (count)
    print()
    return (count)
