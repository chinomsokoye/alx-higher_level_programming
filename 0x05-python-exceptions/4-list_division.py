#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("{}".format("out of range"))
        except (ValueError, TypeError):
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            print("{}".format("division by 0"))
        finally:
            new_list.append(res)
    return new_list
