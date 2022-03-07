#!/usr/bin/env python3


def main():
    oneTo100 = list(range(1, 101))
    digits = str(oneTo100).replace(', ', '').replace('[', '').replace(']', '')

    sumOfDigits = 0
    for i in list(digits):
        sumOfDigits += int(i)

    print(sumOfDigits)


if __name__ == '__main__':
    main()
