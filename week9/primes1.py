#!/usr/bin/env python3
import primefunc as pf


def main():
    li = [num for num in range(100) if pf.is_prime(num)]
    print(li)


if __name__ == '__main__':
    main()
