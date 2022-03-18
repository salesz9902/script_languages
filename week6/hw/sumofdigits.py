#!/usr/bin/env python3

def main():
    s = 0
    for i in str(2**1000):
        s += int(i)

    print(s)


if __name__ == '__main__':
    main()
