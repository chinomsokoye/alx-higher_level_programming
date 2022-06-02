#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    my_args = len(sys.argv)
    if (my_args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (operator is "+"):
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif (operator is "-"):
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif (operator is "*"):
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif (operator is "/"):
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)
