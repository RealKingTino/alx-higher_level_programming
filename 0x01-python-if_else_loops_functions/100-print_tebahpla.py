#!/usr/bin/python3
output = ""
for c in range(122, 96, -1):
    if c % 2 == 0:
        output += chr(c - 32)
    else:
        output += chr(c)
print(output)
