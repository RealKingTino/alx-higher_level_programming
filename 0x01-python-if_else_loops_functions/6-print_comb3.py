#!/usr/bin/python3
for i in range(0, 9):
    for y in range(i + 1, 10):
        if i == 8 and y == 9:
            print(str(i) + str(y))
        else:
            print(str(i) + str(y) + ", ", end="")
