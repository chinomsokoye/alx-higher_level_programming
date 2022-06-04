#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or idx >= len(my_list)):
        same_list = my_list.copy()
        return same_list
    del my_list[idx]
    same_list = my_list.copy()
    return same_list
