#!/usr/bin/env python3
import primefunc


def main():
    li = sum([num for num in range(200) if primefunc.is_prime(num)])
    print(li)


if __name__ == '__main__':
    main()
