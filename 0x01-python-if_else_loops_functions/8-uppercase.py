#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(letter) - num),  end="")
    print()
