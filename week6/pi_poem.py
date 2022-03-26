#!/usr/bin/env python3
import math

POEM = """
How I want a drink
alcoholic of course
After the heavy lectures
involving complex functions
"""


def main():
    strpi = str(math.pi).replace('.', '')[:15]

    cpi = [str(len(w)) for w in POEM.split()]
    print(''.join(cpi))

    print(''.join(cpi) == strpi)


if __name__ == '__main__':
    main()
