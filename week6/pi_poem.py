#!/usr/bin/env python3
import math

POEM = """
How I want a drink
alcoholic of course
After the heavy lectures
involving complex functions
"""


def main():
    t = []
    cpi = ''
    strpi = str(math.pi).replace('.', '')[:15]

    for w in POEM.split():
        t.append(str(len(w)))

    cpi = ''.join(t)
    print(cpi)
    print(cpi == strpi)


if __name__ == '__main__':
    main()
