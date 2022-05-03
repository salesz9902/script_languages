#!/usr/bin/env python3

def isPalindrom(word: int) -> bool:
    w: str = str(word)
    if(w == w[::-1]):
        return True
    else:
        return False


def main():
    for i in range(2000000):
        if(isPalindrom(i) and isPalindrom(bin(i)[2:])):
            print(i, bin(i)[2:])


if __name__ == '__main__':
    main()
