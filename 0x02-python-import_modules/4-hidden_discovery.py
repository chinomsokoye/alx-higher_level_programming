#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arr = dir()
    for x in range(0, len(arr)):
        if arr[x][0:2] != "--":
            print("{}".format(arr[x]))
