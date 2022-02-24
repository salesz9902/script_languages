#!/usr/bin/env python3

def getProduct(l):
    prod = 0

    if(len(l) == 0):
        return 1
    else:
        for i in l:
            prod = prod*i
    return prod


def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8]

    print(getProduct(li))


if __name__ == '__main__':
    main()
