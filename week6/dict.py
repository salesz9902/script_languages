#!/usr/bin/env python3


def main():
    d = {}
    print(type(d))
    d['a'] = 'alfa'
    d['b'] = 'beta'
    d['o'] = 'omega'

    print(d)

    d['g'] = 'gamma'

    print(d['o'])


if __name__ == '__main__':
    main()
