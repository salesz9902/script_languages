#!/usr/bin/env python3
import math


class Sphere:
    def __init__(self, r):
        self.r = r

    def a(self):
        return self.r**2 * math.pi * 4

    def v(self):
        return (4 * math.pi * self.r**3) / 3

    def __lt__(self, other):
        return self.a() < other.a()

    def __gt__(self, other):
        return self.a() > other.a()

    def __le__(self, other):
        return self.a() <= other.a()

    def __ge__(self, other):
        return self.a() >= other.a()

    def __str__(self):
        return f'Sphere({self.r})'


class Ellipse:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b * math.pi

    def __str__(self):
        return f'Ellipse({self.a}, {self.b})'


def main():
    sp1 = Sphere(5)
    sp2 = Sphere(7)

    print(f'{sp1} > {sp2} -> {sp1 > sp2}')
    print(f'{sp1} < {sp2} -> {sp1 < sp2}')
    print(f'{sp1} >= {sp2} -> {sp1 >= sp2}')
    print(f'{sp1} <= {sp2} -> {sp1 <= sp2}')


if __name__ == '__main__':
    main()
