#!/usr/bin/env python3

def reverseNum(num):
    text = str(num)
    return(text[::-1])


def main():
    print(reverseNum(1977))
    print(reverseNum(12568))


if __name__ == '__main__':
    main()
