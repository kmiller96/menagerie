#!/usr/bin/env python3

def add(a, b):
    return a + b


def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: add.py <num1> <num2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Error: please provide valid numbers")
        sys.exit(1)

    result = add(a, b)
    if result == int(result):
        print(int(result))
    else:
        print(result)


if __name__ == "__main__":
    main()
