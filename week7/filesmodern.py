#!/usr/bin/env python3

INPUT = 'szoveg.txt'
OUTPUT = 'cszoveg.txt'


def main():
    with open(INPUT, 'r') as f1, open(OUTPUT, 'w') as to:
        for line in f1:
            to.write(line)


if __name__ == '__main__':
    main()
