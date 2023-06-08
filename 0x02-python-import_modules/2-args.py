#!/usr/bin/python3

import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]
    argument = len(arguments)
    if argument == 0:
        print('{} arguments.'.format("0"))
    elif argument == 1:
        print('{} argument:'.format(argument))
    else:
        print('{} arguments:'.format(argument))
    for i in range(argument):
        print('{}: {}'.format(i + 1, arguments[i]))
