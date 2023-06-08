#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

args = sys.argv[1:]
arg_count = len(args)

if arg_count != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(args[0])
operator = args[1]
b = int(args[2])

result = None

if operator == "+":
    result = add(a, b)
elif operator == "-":
    result = sub(a, b)
elif operator == "*":
    result = mul(a, b)
elif operator == "/":
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

print(f"{a} {operator} {b} = {result}")
sys.exit(0)
