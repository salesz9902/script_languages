#!/usr/bin/env python3

def main():
    f = open('boxes.txt')
    lines = f.readlines()

    sum = 0
    for line in lines:
        sides = []
        l = line.strip().split('x')
        a, b, c = l
        a = int(a)
        b = int(b)
        c = int(c)
        sides = [int(a), int(b), int(c)]
        sides.sort()
        minarea = sides[0]*sides[1]

        A = 2*(a*b + a*c + b*c)
        sum += minarea+A

    print(sum)


if __name__ == '__main__':
    main()
