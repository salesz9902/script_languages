#!/usr/bin/env python3


def main():
    a = [21, 42, 11, 40, 35]

    print(sorted(a))
    print(a)
    a.sort()
    print(a)

    print(sorted(a, reverse=True))


if __name__ == '__main__':
    main()
