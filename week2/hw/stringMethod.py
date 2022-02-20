#!/usr/bin/env python3

def main():
    # demonstrating the isdecimal() string method
    # it returns True if all characters are alphanumeric and there is at least one character
    # returns False otherwise
    one = '1'
    two = 'two'
    three = 'thr33'
    empty = ''

    print(f'{one.isdecimal()}, {two.isdecimal()}, {three.isdecimal()}, {empty.isdecimal()}')


if __name__ == '__main__':
    main()
