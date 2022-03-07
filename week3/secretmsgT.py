#!/usr/bin/env python3
import sys

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

t = 'abcdefghijklmnopqrstuvwxyzabABCDEFGHIJKLMNOPQRSTUVWXYZAB'


def main():
    for c in TEXT:
        pos = t.find(c)
        if(pos == -1):
            sys.stdout.write(c)
        else:
            sys.stdout.write(t[pos+2])


if __name__ == '__main__':
    main()
