#!/usr/bin/env python3
import sys


def main():
    """A program which can produce different output with another file name."""
    result = ''.join([chr(num) for num in range(97, 122+1)])
    if(sys.argv[0] == './a-z.py'):
        print(result)
    elif(sys.argv[0] == './z-a.py'):
        print(result[::-1])


if __name__ == '__main__':
    main()
