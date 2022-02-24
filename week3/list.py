#!/usr/bin/env python3


def main():
    alist = [10, 12, 15]
    blist = alist[:]
    alist.append(20)
    print(alist)
    print(blist)

    for item in alist:
        print(item)


if __name__ == '__main__':
    main()
