#!/usr/bin/env python3
import sys


def main():
    if(len(sys.argv) != 3):
        print('Ket parancssori argumentumot kell megadnod!')
    else:
        print(int(sys.argv[1])+int(sys.argv[2]))


if __name__ == '__main__':
    main()
