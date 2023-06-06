#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord('a') <= ord(letter) <= ord('z'):
            print(chr(ord(letter) - 32), end="")
        else:
            print(letter, end="")
    print()
