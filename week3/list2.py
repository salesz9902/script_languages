#!/usr/bin/env python3


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    paros = []

    isIncluded = 10 in li
    print(isIncluded)

    for szam in li:
        if(szam % 2 == 0):
            paros.append(szam)

    print(paros)


if __name__ == '__main__':
    main()
