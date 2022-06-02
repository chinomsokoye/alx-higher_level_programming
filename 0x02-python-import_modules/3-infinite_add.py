#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = sum(int(sys.argv[i]) for i in range(1, len(sys.argv)))
    print("{}".format(res))
