#!/usr/bin/env python3
from math import prod
from itertools import combinations


def findNumbers():
    for combination in combinations(range(1, 45 + 1), 6):
        if prod(combination) == 996300 and sum(combination) == 90:
            return combination


def main():
    print("Nyeroszamok:\n", ",".join(str(c) for c in findNumbers()))


if __name__ == '__main__':
    main()
