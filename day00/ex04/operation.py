import sys


def operations(a, b):
    print("Sum:        ", a + b)
    print("Difference:  ", a - b)
    print("Product:    ", a * b)
    try:
        print("Quotient    ", a / b)
    except ZeroDivisionError:
        print("ERROR (div by zero)")
    try:
        print("Remainder   ", a % b)
    except ZeroDivisionError:
        print("ERROR (modulo by zero)")


def main(args):
    if (len(args) == 1):
        print("Example\n    python operations.py 10 3")
    elif len(args) < 3:
        print("InputError: Too few argument")
    elif len(args) > 3:
        print("InputError: Too many argument")
    else:
        try:
            args[1] = int(args[1])
            args[2] = int(args[2])
            operations(args[1], args[2])
        except ValueError:
            print("InputError only numbers")


if __name__ == "__main__":
    main(sys.argv)
