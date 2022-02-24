#!/usr/bin/env python3


from pandas import RangeIndex


def main():
    a = []
    a.append(30)
    a.append(45)
    print(a)
    a.pop(0)
    print(a)


if __name__ == '__main__':
    main()
