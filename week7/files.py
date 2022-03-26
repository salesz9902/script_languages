#!/usr/bin/env python3

INPUT = 'szoveg.txt'


def main():
    f = open(INPUT, 'r')

    for line in f:
        line = line.rstrip('\n')
        if line.endswith('sor.'):
            print(line)

    content = f.read().splitlines()
    print(content)

    f = open('out.txt', 'w')
    print('hello', file=f)
    print('world', file=f)
    f.write('abcd')
    f.write('xyz')

    f.close()


if __name__ == '__main__':
    main()
