#!/usr/bin/env python3

INPUT = 'string1.py'
OUTPUT = 'string1_clean.py'


def main():
    with open(INPUT, 'r') as o, open(OUTPUT, 'w') as n:

        for line in o:
            if(not line.lstrip().startswith('#')):
                n.write(line)


if __name__ == '__main__':
    main()
