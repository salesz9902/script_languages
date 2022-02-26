#!/usr/bin/env python3


def help(text):
    return text.replace(' ', '').replace('\n', '')


def main():
    randomstr = '192.20.246.138:\n 6666'
    randomstr2 = '206.130.99.82:\n8080'

    print(help(randomstr))
    print(help(randomstr2))


if __name__ == '__main__':
    main()
