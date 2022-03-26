#!/usr/bin/env python3

INPUT = 'szoveg.txt'
OUTPUT = 'cpszoveg.txt'


def main():
    f1 = open(INPUT, 'r')
    to = open(OUTPUT, 'w')

    for line in f1:
        to.write(line)

    f1.close()
    to.close()


if __name__ == '__main__':
    main()
