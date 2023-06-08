#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
num_arguments = len(arguments)
print(f"{num_arguments} arguments:")
for i in range(num_arguments):
    position = i + 1
    argument = arguments[i]
    print(position, ":", argument)
