#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list = dir(hidden)
    for i in range(len(list)):
        if (list[i][0] != '-'):
            print(list[i])
