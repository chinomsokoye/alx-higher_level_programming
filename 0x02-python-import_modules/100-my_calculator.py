#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = len(sys.argv)
    if (args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if (operator is "+"):
        print("{} {} {} = {}".format(a, b, operator, add(a, b)))
    elif (operator is "-"):
        print("{} {} {} = {}".format(a, b, operator, sub(a, b)))
    elif (operator is "*"):
        print("{} {} {} = {}".format(a, b, operator, mul(a, b)))
    elif (operator is "/"):
        print("{} {} {} = {}".format(a, b, operator, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)
