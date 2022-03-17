#!/usr/bin/env python3

def main():
    """Prints out the sum of the first 1000 numbers can be divided by 3 or 5"""
    result = sum([n for n in range(1000) if (n % 3 == 0 or n % 5 == 0)])
    print(result)


if __name__ == '__main__':
    main()
