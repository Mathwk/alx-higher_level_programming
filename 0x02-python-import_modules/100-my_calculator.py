#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]
    if op == '+':
        print("{} {} {} = {}".format(num1, op, num2, add(num1, num2)))
    elif op == '-':
        print("{} {} {} = {}".format(num1, op, num2, sub(num1, num2)))
    elif op == '*':
        print("{} {} {} = {}".format(num1, op, num2, mul(num1, num2)))
    elif op == '/':
        print("{} {} {} = {}".format(num1, op, num2, div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
