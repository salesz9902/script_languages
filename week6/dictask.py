#!/usr/bin/env python3


def main():
    d = {}
    print(type(d))
    d['a'] = 'alfa'
    d['b'] = 'beta'
    d['o'] = 'omega'
    d['g'] = 'gamma'

    print(d)

    for w in sorted(d.keys()):
        print(w, ':', d[w])


if __name__ == '__main__':
    main()
