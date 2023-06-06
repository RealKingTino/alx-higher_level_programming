#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        x = ord(letter)
        if x >= 97 and x <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[letter]) - num), end="")
    print()
