#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if(i == 8 and j == 9):
            print("{}".format(str(i) + str(j)))
        elif(j > i):
            print("{}".format(str(i) + str(j)) + ", ", end="")
