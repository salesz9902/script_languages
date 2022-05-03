#!/usr/bin/env python3

def f(li):
    return li[-1]


def main():
    li = [[2, 6], [1, 3], [5, 4]]

    print(sorted(li, key=f))


if __name__ == '__main__':
    main()
