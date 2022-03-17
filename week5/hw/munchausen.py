#!/usr/bin/env python3

def main():
    i = 0
    while(i < 440000000):
        digits = (int(digit) for digit in str(i))
        if sum(digit ** digit for digit in digits) == i:
            print(i, "(munchausen)")
        print(i)
        i += 1


if __name__ == '__main__':
    main()
