#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            i += int(arg)
    print(i)
