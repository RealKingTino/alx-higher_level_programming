#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

print(f"{num_arguments} argument{'s' if num_arguments != 1 else ''}:")
if num_arguments > 0:
    for i, argument in enumerate(arguments):
        position = i + 1
        print(f"{position}: {argument}")
else:
    print(".")
